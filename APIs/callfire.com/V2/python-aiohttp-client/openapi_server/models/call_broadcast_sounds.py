# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CallBroadcastSounds(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, dnc_digit: str=None, dnc_sound_id: int=None, dnc_sound_text: str=None, dnc_sound_text_voice: str=None, live_sound_id: int=None, live_sound_text: str=None, live_sound_text_voice: str=None, machine_sound_id: int=None, machine_sound_text: str=None, machine_sound_text_voice: str=None, transfer_digit: str=None, transfer_number: str=None, transfer_sound_id: int=None, transfer_sound_text: str=None, transfer_sound_text_voice: str=None):
        """CallBroadcastSounds - a model defined in OpenAPI

        :param dnc_digit: The dnc_digit of this CallBroadcastSounds.
        :param dnc_sound_id: The dnc_sound_id of this CallBroadcastSounds.
        :param dnc_sound_text: The dnc_sound_text of this CallBroadcastSounds.
        :param dnc_sound_text_voice: The dnc_sound_text_voice of this CallBroadcastSounds.
        :param live_sound_id: The live_sound_id of this CallBroadcastSounds.
        :param live_sound_text: The live_sound_text of this CallBroadcastSounds.
        :param live_sound_text_voice: The live_sound_text_voice of this CallBroadcastSounds.
        :param machine_sound_id: The machine_sound_id of this CallBroadcastSounds.
        :param machine_sound_text: The machine_sound_text of this CallBroadcastSounds.
        :param machine_sound_text_voice: The machine_sound_text_voice of this CallBroadcastSounds.
        :param transfer_digit: The transfer_digit of this CallBroadcastSounds.
        :param transfer_number: The transfer_number of this CallBroadcastSounds.
        :param transfer_sound_id: The transfer_sound_id of this CallBroadcastSounds.
        :param transfer_sound_text: The transfer_sound_text of this CallBroadcastSounds.
        :param transfer_sound_text_voice: The transfer_sound_text_voice of this CallBroadcastSounds.
        """
        self.openapi_types = {
            'dnc_digit': str,
            'dnc_sound_id': int,
            'dnc_sound_text': str,
            'dnc_sound_text_voice': str,
            'live_sound_id': int,
            'live_sound_text': str,
            'live_sound_text_voice': str,
            'machine_sound_id': int,
            'machine_sound_text': str,
            'machine_sound_text_voice': str,
            'transfer_digit': str,
            'transfer_number': str,
            'transfer_sound_id': int,
            'transfer_sound_text': str,
            'transfer_sound_text_voice': str
        }

        self.attribute_map = {
            'dnc_digit': 'dncDigit',
            'dnc_sound_id': 'dncSoundId',
            'dnc_sound_text': 'dncSoundText',
            'dnc_sound_text_voice': 'dncSoundTextVoice',
            'live_sound_id': 'liveSoundId',
            'live_sound_text': 'liveSoundText',
            'live_sound_text_voice': 'liveSoundTextVoice',
            'machine_sound_id': 'machineSoundId',
            'machine_sound_text': 'machineSoundText',
            'machine_sound_text_voice': 'machineSoundTextVoice',
            'transfer_digit': 'transferDigit',
            'transfer_number': 'transferNumber',
            'transfer_sound_id': 'transferSoundId',
            'transfer_sound_text': 'transferSoundText',
            'transfer_sound_text_voice': 'transferSoundTextVoice'
        }

        self._dnc_digit = dnc_digit
        self._dnc_sound_id = dnc_sound_id
        self._dnc_sound_text = dnc_sound_text
        self._dnc_sound_text_voice = dnc_sound_text_voice
        self._live_sound_id = live_sound_id
        self._live_sound_text = live_sound_text
        self._live_sound_text_voice = live_sound_text_voice
        self._machine_sound_id = machine_sound_id
        self._machine_sound_text = machine_sound_text
        self._machine_sound_text_voice = machine_sound_text_voice
        self._transfer_digit = transfer_digit
        self._transfer_number = transfer_number
        self._transfer_sound_id = transfer_sound_id
        self._transfer_sound_text = transfer_sound_text
        self._transfer_sound_text_voice = transfer_sound_text_voice

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CallBroadcastSounds':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CallBroadcastSounds of this CallBroadcastSounds.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dnc_digit(self):
        """Gets the dnc_digit of this CallBroadcastSounds.

        Digit pressed to place contact in DNC list

        :return: The dnc_digit of this CallBroadcastSounds.
        :rtype: str
        """
        return self._dnc_digit

    @dnc_digit.setter
    def dnc_digit(self, dnc_digit):
        """Sets the dnc_digit of this CallBroadcastSounds.

        Digit pressed to place contact in DNC list

        :param dnc_digit: The dnc_digit of this CallBroadcastSounds.
        :type dnc_digit: str
        """

        self._dnc_digit = dnc_digit

    @property
    def dnc_sound_id(self):
        """Gets the dnc_sound_id of this CallBroadcastSounds.

        An id of sound file to play when recipient decided to opt out and pressed DNC digit

        :return: The dnc_sound_id of this CallBroadcastSounds.
        :rtype: int
        """
        return self._dnc_sound_id

    @dnc_sound_id.setter
    def dnc_sound_id(self, dnc_sound_id):
        """Sets the dnc_sound_id of this CallBroadcastSounds.

        An id of sound file to play when recipient decided to opt out and pressed DNC digit

        :param dnc_sound_id: The dnc_sound_id of this CallBroadcastSounds.
        :type dnc_sound_id: int
        """

        self._dnc_sound_id = dnc_sound_id

    @property
    def dnc_sound_text(self):
        """Gets the dnc_sound_text of this CallBroadcastSounds.

        Text to be turned into sound, plays to notify that Do Not Call digit has been pressed and inform your contact of their placement on the Do Not Call list

        :return: The dnc_sound_text of this CallBroadcastSounds.
        :rtype: str
        """
        return self._dnc_sound_text

    @dnc_sound_text.setter
    def dnc_sound_text(self, dnc_sound_text):
        """Sets the dnc_sound_text of this CallBroadcastSounds.

        Text to be turned into sound, plays to notify that Do Not Call digit has been pressed and inform your contact of their placement on the Do Not Call list

        :param dnc_sound_text: The dnc_sound_text of this CallBroadcastSounds.
        :type dnc_sound_text: str
        """

        self._dnc_sound_text = dnc_sound_text

    @property
    def dnc_sound_text_voice(self):
        """Gets the dnc_sound_text_voice of this CallBroadcastSounds.

        The voice to be used (MALE1, FEMALE1, FEMALE2, SPANISH1, FRENCHCANADIAN1)

        :return: The dnc_sound_text_voice of this CallBroadcastSounds.
        :rtype: str
        """
        return self._dnc_sound_text_voice

    @dnc_sound_text_voice.setter
    def dnc_sound_text_voice(self, dnc_sound_text_voice):
        """Sets the dnc_sound_text_voice of this CallBroadcastSounds.

        The voice to be used (MALE1, FEMALE1, FEMALE2, SPANISH1, FRENCHCANADIAN1)

        :param dnc_sound_text_voice: The dnc_sound_text_voice of this CallBroadcastSounds.
        :type dnc_sound_text_voice: str
        """
        allowed_values = ["MALE1", "FEMALE1", "FEMALE2", "SPANISH1", "FRENCHCANADIAN1"]  # noqa: E501
        if dnc_sound_text_voice not in allowed_values:
            raise ValueError(
                "Invalid value for `dnc_sound_text_voice` ({0}), must be one of {1}"
                .format(dnc_sound_text_voice, allowed_values)
            )

        self._dnc_sound_text_voice = dnc_sound_text_voice

    @property
    def live_sound_id(self):
        """Gets the live_sound_id of this CallBroadcastSounds.

        An id of sound file to play if phone is answered

        :return: The live_sound_id of this CallBroadcastSounds.
        :rtype: int
        """
        return self._live_sound_id

    @live_sound_id.setter
    def live_sound_id(self, live_sound_id):
        """Sets the live_sound_id of this CallBroadcastSounds.

        An id of sound file to play if phone is answered

        :param live_sound_id: The live_sound_id of this CallBroadcastSounds.
        :type live_sound_id: int
        """

        self._live_sound_id = live_sound_id

    @property
    def live_sound_text(self):
        """Gets the live_sound_text of this CallBroadcastSounds.

        Text to be used to turned into a sound. This text will be played when the phone is answered

        :return: The live_sound_text of this CallBroadcastSounds.
        :rtype: str
        """
        return self._live_sound_text

    @live_sound_text.setter
    def live_sound_text(self, live_sound_text):
        """Sets the live_sound_text of this CallBroadcastSounds.

        Text to be used to turned into a sound. This text will be played when the phone is answered

        :param live_sound_text: The live_sound_text of this CallBroadcastSounds.
        :type live_sound_text: str
        """

        self._live_sound_text = live_sound_text

    @property
    def live_sound_text_voice(self):
        """Gets the live_sound_text_voice of this CallBroadcastSounds.

        The voice to be used (MALE1, FEMALE1, FEMALE2, SPANISH1, FRENCHCANADIAN1) for a live sound

        :return: The live_sound_text_voice of this CallBroadcastSounds.
        :rtype: str
        """
        return self._live_sound_text_voice

    @live_sound_text_voice.setter
    def live_sound_text_voice(self, live_sound_text_voice):
        """Sets the live_sound_text_voice of this CallBroadcastSounds.

        The voice to be used (MALE1, FEMALE1, FEMALE2, SPANISH1, FRENCHCANADIAN1) for a live sound

        :param live_sound_text_voice: The live_sound_text_voice of this CallBroadcastSounds.
        :type live_sound_text_voice: str
        """
        allowed_values = ["MALE1", "FEMALE1", "FEMALE2", "SPANISH1", "FRENCHCANADIAN1"]  # noqa: E501
        if live_sound_text_voice not in allowed_values:
            raise ValueError(
                "Invalid value for `live_sound_text_voice` ({0}), must be one of {1}"
                .format(live_sound_text_voice, allowed_values)
            )

        self._live_sound_text_voice = live_sound_text_voice

    @property
    def machine_sound_id(self):
        """Gets the machine_sound_id of this CallBroadcastSounds.

        An id of a sound file to play if answering machine is detected

        :return: The machine_sound_id of this CallBroadcastSounds.
        :rtype: int
        """
        return self._machine_sound_id

    @machine_sound_id.setter
    def machine_sound_id(self, machine_sound_id):
        """Sets the machine_sound_id of this CallBroadcastSounds.

        An id of a sound file to play if answering machine is detected

        :param machine_sound_id: The machine_sound_id of this CallBroadcastSounds.
        :type machine_sound_id: int
        """

        self._machine_sound_id = machine_sound_id

    @property
    def machine_sound_text(self):
        """Gets the machine_sound_text of this CallBroadcastSounds.

        Text to be turned into a sound. This text will be played when answering machine is detected

        :return: The machine_sound_text of this CallBroadcastSounds.
        :rtype: str
        """
        return self._machine_sound_text

    @machine_sound_text.setter
    def machine_sound_text(self, machine_sound_text):
        """Sets the machine_sound_text of this CallBroadcastSounds.

        Text to be turned into a sound. This text will be played when answering machine is detected

        :param machine_sound_text: The machine_sound_text of this CallBroadcastSounds.
        :type machine_sound_text: str
        """

        self._machine_sound_text = machine_sound_text

    @property
    def machine_sound_text_voice(self):
        """Gets the machine_sound_text_voice of this CallBroadcastSounds.

        The voice to be used (MALE1, FEMALE1 , FEMALE2, SPANISH1, FRENCHCANADIAN1) for a machine sound

        :return: The machine_sound_text_voice of this CallBroadcastSounds.
        :rtype: str
        """
        return self._machine_sound_text_voice

    @machine_sound_text_voice.setter
    def machine_sound_text_voice(self, machine_sound_text_voice):
        """Sets the machine_sound_text_voice of this CallBroadcastSounds.

        The voice to be used (MALE1, FEMALE1 , FEMALE2, SPANISH1, FRENCHCANADIAN1) for a machine sound

        :param machine_sound_text_voice: The machine_sound_text_voice of this CallBroadcastSounds.
        :type machine_sound_text_voice: str
        """
        allowed_values = ["MALE1", "FEMALE1", "FEMALE2", "SPANISH1", "FRENCHCANADIAN1"]  # noqa: E501
        if machine_sound_text_voice not in allowed_values:
            raise ValueError(
                "Invalid value for `machine_sound_text_voice` ({0}), must be one of {1}"
                .format(machine_sound_text_voice, allowed_values)
            )

        self._machine_sound_text_voice = machine_sound_text_voice

    @property
    def transfer_digit(self):
        """Gets the transfer_digit of this CallBroadcastSounds.

        Digit pressed to initiate a transfer

        :return: The transfer_digit of this CallBroadcastSounds.
        :rtype: str
        """
        return self._transfer_digit

    @transfer_digit.setter
    def transfer_digit(self, transfer_digit):
        """Sets the transfer_digit of this CallBroadcastSounds.

        Digit pressed to initiate a transfer

        :param transfer_digit: The transfer_digit of this CallBroadcastSounds.
        :type transfer_digit: str
        """

        self._transfer_digit = transfer_digit

    @property
    def transfer_number(self):
        """Gets the transfer_number of this CallBroadcastSounds.

        Phone number in E.164 format (11-digit) to transfer call to.  Example: 12132000384, 67076

        :return: The transfer_number of this CallBroadcastSounds.
        :rtype: str
        """
        return self._transfer_number

    @transfer_number.setter
    def transfer_number(self, transfer_number):
        """Sets the transfer_number of this CallBroadcastSounds.

        Phone number in E.164 format (11-digit) to transfer call to.  Example: 12132000384, 67076

        :param transfer_number: The transfer_number of this CallBroadcastSounds.
        :type transfer_number: str
        """

        self._transfer_number = transfer_number

    @property
    def transfer_sound_id(self):
        """Gets the transfer_sound_id of this CallBroadcastSounds.

        An id of a file to play if call is transferred

        :return: The transfer_sound_id of this CallBroadcastSounds.
        :rtype: int
        """
        return self._transfer_sound_id

    @transfer_sound_id.setter
    def transfer_sound_id(self, transfer_sound_id):
        """Sets the transfer_sound_id of this CallBroadcastSounds.

        An id of a file to play if call is transferred

        :param transfer_sound_id: The transfer_sound_id of this CallBroadcastSounds.
        :type transfer_sound_id: int
        """

        self._transfer_sound_id = transfer_sound_id

    @property
    def transfer_sound_text(self):
        """Gets the transfer_sound_text of this CallBroadcastSounds.

        Text to be turned into a sound. This text will be played when the transfer digit is played

        :return: The transfer_sound_text of this CallBroadcastSounds.
        :rtype: str
        """
        return self._transfer_sound_text

    @transfer_sound_text.setter
    def transfer_sound_text(self, transfer_sound_text):
        """Sets the transfer_sound_text of this CallBroadcastSounds.

        Text to be turned into a sound. This text will be played when the transfer digit is played

        :param transfer_sound_text: The transfer_sound_text of this CallBroadcastSounds.
        :type transfer_sound_text: str
        """

        self._transfer_sound_text = transfer_sound_text

    @property
    def transfer_sound_text_voice(self):
        """Gets the transfer_sound_text_voice of this CallBroadcastSounds.

        The voice to be used (MALE1, FEMALE1, FEMALE2, SPANISH1, FRENCHCANADIAN1) for a sound transfer

        :return: The transfer_sound_text_voice of this CallBroadcastSounds.
        :rtype: str
        """
        return self._transfer_sound_text_voice

    @transfer_sound_text_voice.setter
    def transfer_sound_text_voice(self, transfer_sound_text_voice):
        """Sets the transfer_sound_text_voice of this CallBroadcastSounds.

        The voice to be used (MALE1, FEMALE1, FEMALE2, SPANISH1, FRENCHCANADIAN1) for a sound transfer

        :param transfer_sound_text_voice: The transfer_sound_text_voice of this CallBroadcastSounds.
        :type transfer_sound_text_voice: str
        """
        allowed_values = ["MALE1", "FEMALE1", "FEMALE2", "SPANISH1", "FRENCHCANADIAN1"]  # noqa: E501
        if transfer_sound_text_voice not in allowed_values:
            raise ValueError(
                "Invalid value for `transfer_sound_text_voice` ({0}), must be one of {1}"
                .format(transfer_sound_text_voice, allowed_values)
            )

        self._transfer_sound_text_voice = transfer_sound_text_voice
