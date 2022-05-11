from collections import OrderedDict
from random import choice
from rant_exceptions import RantLookupException
from typing import TextIO


class LookupEntry:
    def __init__(self, forms: OrderedDict[str, str], tags: set[str] = None):
        self.forms = forms
        self.tags = tags

    def __getitem__(self, form: str):
        return self.forms[form]

    def has_any_tag_of(self, tags: set[str]) -> bool:
        if tags is None or self.tags is None:
            return False
        return not self.tags.isdisjoint(tags)


class LookupDictionary:
    def __init__(self, name: str, forms: list[str]):
        self.name = name
        self.forms = forms
        self.entries = list[LookupEntry]()
        self.labels = dict[str, LookupEntry]()

    def add(self, forms: list[str], tags: set[str] = None):
        if len(forms) != len(self.forms):
            raise RantLookupException(
                "[LookupDictionary.add] wrong number of forms provided")
        lookup = LookupEntry(OrderedDict(zip(self.forms, forms)), tags)
        self.entries.append(lookup)

    def clear_labels(self):
        self.labels = dict[str, LookupEntry]()

    def get(self, form: str, tags_positive: set[str] = None, tags_negative: set[str] = None,
            label_positive: str = None, labels_negative: set[str] = None) -> str:
        if form not in self.forms:
            raise RantLookupException(
                f"[LookupDictionary.get] dictionary '{self.name}' has no form '{form}'")
        if label_positive and label_positive in self.labels:
            return self.labels[label_positive][form]
        valid_choices = list[LookupEntry]()
        if not tags_negative and not tags_positive:
            valid_choices = list.copy(self.entries)
        else:
            for entry in self.entries:
                valid = False
                if not tags_positive or entry.has_any_tag_of(tags_positive):
                    valid = True
                if entry.has_any_tag_of(tags_negative):
                    valid = False
                if valid:
                    valid_choices.append(entry)
        if not valid_choices:
            valid_choices = self.entries
        if labels_negative:
            for label in labels_negative:
                if label in self.labels and self.labels[label] in valid_choices:
                    valid_choices.remove(self.labels[label])
        chosen_entry = choice(valid_choices)
        if label_positive:
            self.labels[label_positive] = chosen_entry
        return chosen_entry[form]


class LookupDictionaryFactory:
    def __init__(self):
        pass

    def get_forms(self, forms_line: str) -> list[str]:
        return forms_line.split()[1:]

    def get_name(self, name_line: str) -> str:
        return name_line.split()[1]

    def get_entry(self, entry_line: str) -> list[str]:
        return entry_line.split('/')

    def read_from_file(self, input_file: TextIO) -> LookupDictionary:
        name = str()
        forms = list[str]()
        entries = list[list[str]]()
        dictionary = None
        for line in input_file:
            if dictionary:
                if line.startswith("#") or not line.strip():
                    continue
                else:
                    entry = self.get_entry(line)
                    if len(entry) == len(forms):
                        dictionary.add(entry)
            if name and forms:
                if dictionary is None:
                    dictionary = LookupDictionary(name, forms)
            else:
                if line.startswith("#name"):
                    name = self.get_name(line)
                    continue
                elif line.startswith("#forms") or line.startswith("#subs"):
                    forms = self.get_forms(line)
                    continue
        return dictionary




