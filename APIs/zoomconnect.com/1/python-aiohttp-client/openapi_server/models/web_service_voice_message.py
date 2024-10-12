# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.link import Link
from openapi_server import util


class WebServiceVoiceMessage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, audio_file_url: str=None, campaign: str=None, date_time_sent: datetime=None, deleted: bool=None, language: str=None, links: List[Link]=None, message: str=None, message_status: str=None, to_number: str=None, user_data_field: str=None, voice_message_id: str=None):
        """WebServiceVoiceMessage - a model defined in OpenAPI

        :param audio_file_url: The audio_file_url of this WebServiceVoiceMessage.
        :param campaign: The campaign of this WebServiceVoiceMessage.
        :param date_time_sent: The date_time_sent of this WebServiceVoiceMessage.
        :param deleted: The deleted of this WebServiceVoiceMessage.
        :param language: The language of this WebServiceVoiceMessage.
        :param links: The links of this WebServiceVoiceMessage.
        :param message: The message of this WebServiceVoiceMessage.
        :param message_status: The message_status of this WebServiceVoiceMessage.
        :param to_number: The to_number of this WebServiceVoiceMessage.
        :param user_data_field: The user_data_field of this WebServiceVoiceMessage.
        :param voice_message_id: The voice_message_id of this WebServiceVoiceMessage.
        """
        self.openapi_types = {
            'audio_file_url': str,
            'campaign': str,
            'date_time_sent': datetime,
            'deleted': bool,
            'language': str,
            'links': List[Link],
            'message': str,
            'message_status': str,
            'to_number': str,
            'user_data_field': str,
            'voice_message_id': str
        }

        self.attribute_map = {
            'audio_file_url': 'audioFileUrl',
            'campaign': 'campaign',
            'date_time_sent': 'dateTimeSent',
            'deleted': 'deleted',
            'language': 'language',
            'links': 'links',
            'message': 'message',
            'message_status': 'messageStatus',
            'to_number': 'toNumber',
            'user_data_field': 'userDataField',
            'voice_message_id': 'voiceMessageId'
        }

        self._audio_file_url = audio_file_url
        self._campaign = campaign
        self._date_time_sent = date_time_sent
        self._deleted = deleted
        self._language = language
        self._links = links
        self._message = message
        self._message_status = message_status
        self._to_number = to_number
        self._user_data_field = user_data_field
        self._voice_message_id = voice_message_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'WebServiceVoiceMessage':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The WebServiceVoiceMessage of this WebServiceVoiceMessage.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def audio_file_url(self):
        """Gets the audio_file_url of this WebServiceVoiceMessage.


        :return: The audio_file_url of this WebServiceVoiceMessage.
        :rtype: str
        """
        return self._audio_file_url

    @audio_file_url.setter
    def audio_file_url(self, audio_file_url):
        """Sets the audio_file_url of this WebServiceVoiceMessage.


        :param audio_file_url: The audio_file_url of this WebServiceVoiceMessage.
        :type audio_file_url: str
        """

        self._audio_file_url = audio_file_url

    @property
    def campaign(self):
        """Gets the campaign of this WebServiceVoiceMessage.


        :return: The campaign of this WebServiceVoiceMessage.
        :rtype: str
        """
        return self._campaign

    @campaign.setter
    def campaign(self, campaign):
        """Sets the campaign of this WebServiceVoiceMessage.


        :param campaign: The campaign of this WebServiceVoiceMessage.
        :type campaign: str
        """

        self._campaign = campaign

    @property
    def date_time_sent(self):
        """Gets the date_time_sent of this WebServiceVoiceMessage.


        :return: The date_time_sent of this WebServiceVoiceMessage.
        :rtype: datetime
        """
        return self._date_time_sent

    @date_time_sent.setter
    def date_time_sent(self, date_time_sent):
        """Sets the date_time_sent of this WebServiceVoiceMessage.


        :param date_time_sent: The date_time_sent of this WebServiceVoiceMessage.
        :type date_time_sent: datetime
        """

        self._date_time_sent = date_time_sent

    @property
    def deleted(self):
        """Gets the deleted of this WebServiceVoiceMessage.


        :return: The deleted of this WebServiceVoiceMessage.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this WebServiceVoiceMessage.


        :param deleted: The deleted of this WebServiceVoiceMessage.
        :type deleted: bool
        """

        self._deleted = deleted

    @property
    def language(self):
        """Gets the language of this WebServiceVoiceMessage.


        :return: The language of this WebServiceVoiceMessage.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this WebServiceVoiceMessage.


        :param language: The language of this WebServiceVoiceMessage.
        :type language: str
        """

        self._language = language

    @property
    def links(self):
        """Gets the links of this WebServiceVoiceMessage.


        :return: The links of this WebServiceVoiceMessage.
        :rtype: List[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this WebServiceVoiceMessage.


        :param links: The links of this WebServiceVoiceMessage.
        :type links: List[Link]
        """

        self._links = links

    @property
    def message(self):
        """Gets the message of this WebServiceVoiceMessage.


        :return: The message of this WebServiceVoiceMessage.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this WebServiceVoiceMessage.


        :param message: The message of this WebServiceVoiceMessage.
        :type message: str
        """

        self._message = message

    @property
    def message_status(self):
        """Gets the message_status of this WebServiceVoiceMessage.


        :return: The message_status of this WebServiceVoiceMessage.
        :rtype: str
        """
        return self._message_status

    @message_status.setter
    def message_status(self, message_status):
        """Sets the message_status of this WebServiceVoiceMessage.


        :param message_status: The message_status of this WebServiceVoiceMessage.
        :type message_status: str
        """

        self._message_status = message_status

    @property
    def to_number(self):
        """Gets the to_number of this WebServiceVoiceMessage.


        :return: The to_number of this WebServiceVoiceMessage.
        :rtype: str
        """
        return self._to_number

    @to_number.setter
    def to_number(self, to_number):
        """Sets the to_number of this WebServiceVoiceMessage.


        :param to_number: The to_number of this WebServiceVoiceMessage.
        :type to_number: str
        """

        self._to_number = to_number

    @property
    def user_data_field(self):
        """Gets the user_data_field of this WebServiceVoiceMessage.


        :return: The user_data_field of this WebServiceVoiceMessage.
        :rtype: str
        """
        return self._user_data_field

    @user_data_field.setter
    def user_data_field(self, user_data_field):
        """Sets the user_data_field of this WebServiceVoiceMessage.


        :param user_data_field: The user_data_field of this WebServiceVoiceMessage.
        :type user_data_field: str
        """

        self._user_data_field = user_data_field

    @property
    def voice_message_id(self):
        """Gets the voice_message_id of this WebServiceVoiceMessage.


        :return: The voice_message_id of this WebServiceVoiceMessage.
        :rtype: str
        """
        return self._voice_message_id

    @voice_message_id.setter
    def voice_message_id(self, voice_message_id):
        """Sets the voice_message_id of this WebServiceVoiceMessage.


        :param voice_message_id: The voice_message_id of this WebServiceVoiceMessage.
        :type voice_message_id: str
        """

        self._voice_message_id = voice_message_id
