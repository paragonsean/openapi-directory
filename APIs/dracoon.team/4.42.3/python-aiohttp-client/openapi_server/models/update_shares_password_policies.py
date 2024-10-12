# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.character_rules import CharacterRules
from openapi_server import util


class UpdateSharesPasswordPolicies(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, character_rules: CharacterRules=None, min_length: int=None, reject_dictionary_words: bool=None, reject_keyboard_patterns: bool=None, reject_user_info: bool=None):
        """UpdateSharesPasswordPolicies - a model defined in OpenAPI

        :param character_rules: The character_rules of this UpdateSharesPasswordPolicies.
        :param min_length: The min_length of this UpdateSharesPasswordPolicies.
        :param reject_dictionary_words: The reject_dictionary_words of this UpdateSharesPasswordPolicies.
        :param reject_keyboard_patterns: The reject_keyboard_patterns of this UpdateSharesPasswordPolicies.
        :param reject_user_info: The reject_user_info of this UpdateSharesPasswordPolicies.
        """
        self.openapi_types = {
            'character_rules': CharacterRules,
            'min_length': int,
            'reject_dictionary_words': bool,
            'reject_keyboard_patterns': bool,
            'reject_user_info': bool
        }

        self.attribute_map = {
            'character_rules': 'characterRules',
            'min_length': 'minLength',
            'reject_dictionary_words': 'rejectDictionaryWords',
            'reject_keyboard_patterns': 'rejectKeyboardPatterns',
            'reject_user_info': 'rejectUserInfo'
        }

        self._character_rules = character_rules
        self._min_length = min_length
        self._reject_dictionary_words = reject_dictionary_words
        self._reject_keyboard_patterns = reject_keyboard_patterns
        self._reject_user_info = reject_user_info

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateSharesPasswordPolicies':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UpdateSharesPasswordPolicies of this UpdateSharesPasswordPolicies.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def character_rules(self):
        """Gets the character_rules of this UpdateSharesPasswordPolicies.


        :return: The character_rules of this UpdateSharesPasswordPolicies.
        :rtype: CharacterRules
        """
        return self._character_rules

    @character_rules.setter
    def character_rules(self, character_rules):
        """Sets the character_rules of this UpdateSharesPasswordPolicies.


        :param character_rules: The character_rules of this UpdateSharesPasswordPolicies.
        :type character_rules: CharacterRules
        """

        self._character_rules = character_rules

    @property
    def min_length(self):
        """Gets the min_length of this UpdateSharesPasswordPolicies.

        Minimum number of characters a password must contain

        :return: The min_length of this UpdateSharesPasswordPolicies.
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this UpdateSharesPasswordPolicies.

        Minimum number of characters a password must contain

        :param min_length: The min_length of this UpdateSharesPasswordPolicies.
        :type min_length: int
        """
        if min_length is not None and min_length > 1024:
            raise ValueError("Invalid value for `min_length`, must be a value less than or equal to `1024`")
        if min_length is not None and min_length < 1:
            raise ValueError("Invalid value for `min_length`, must be a value greater than or equal to `1`")

        self._min_length = min_length

    @property
    def reject_dictionary_words(self):
        """Gets the reject_dictionary_words of this UpdateSharesPasswordPolicies.

        Determines whether a password must NOT contain word(s) from a dictionary

        :return: The reject_dictionary_words of this UpdateSharesPasswordPolicies.
        :rtype: bool
        """
        return self._reject_dictionary_words

    @reject_dictionary_words.setter
    def reject_dictionary_words(self, reject_dictionary_words):
        """Sets the reject_dictionary_words of this UpdateSharesPasswordPolicies.

        Determines whether a password must NOT contain word(s) from a dictionary

        :param reject_dictionary_words: The reject_dictionary_words of this UpdateSharesPasswordPolicies.
        :type reject_dictionary_words: bool
        """

        self._reject_dictionary_words = reject_dictionary_words

    @property
    def reject_keyboard_patterns(self):
        """Gets the reject_keyboard_patterns of this UpdateSharesPasswordPolicies.

        Determines whether a password must NOT contain keyboard patterns (e.g. `qwertz`, `asdf`)  (min. 4 character pattern)

        :return: The reject_keyboard_patterns of this UpdateSharesPasswordPolicies.
        :rtype: bool
        """
        return self._reject_keyboard_patterns

    @reject_keyboard_patterns.setter
    def reject_keyboard_patterns(self, reject_keyboard_patterns):
        """Sets the reject_keyboard_patterns of this UpdateSharesPasswordPolicies.

        Determines whether a password must NOT contain keyboard patterns (e.g. `qwertz`, `asdf`)  (min. 4 character pattern)

        :param reject_keyboard_patterns: The reject_keyboard_patterns of this UpdateSharesPasswordPolicies.
        :type reject_keyboard_patterns: bool
        """

        self._reject_keyboard_patterns = reject_keyboard_patterns

    @property
    def reject_user_info(self):
        """Gets the reject_user_info of this UpdateSharesPasswordPolicies.

        Determines whether a password must NOT contain user info (first name, last name, email, user name)

        :return: The reject_user_info of this UpdateSharesPasswordPolicies.
        :rtype: bool
        """
        return self._reject_user_info

    @reject_user_info.setter
    def reject_user_info(self, reject_user_info):
        """Sets the reject_user_info of this UpdateSharesPasswordPolicies.

        Determines whether a password must NOT contain user info (first name, last name, email, user name)

        :param reject_user_info: The reject_user_info of this UpdateSharesPasswordPolicies.
        :type reject_user_info: bool
        """

        self._reject_user_info = reject_user_info
