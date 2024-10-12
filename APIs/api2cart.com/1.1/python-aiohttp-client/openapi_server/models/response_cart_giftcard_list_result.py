# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.gift_card import GiftCard
from openapi_server import util


class ResponseCartGiftcardListResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, additional_fields: object=None, custom_fields: object=None, gift_card: List[GiftCard]=None):
        """ResponseCartGiftcardListResult - a model defined in OpenAPI

        :param additional_fields: The additional_fields of this ResponseCartGiftcardListResult.
        :param custom_fields: The custom_fields of this ResponseCartGiftcardListResult.
        :param gift_card: The gift_card of this ResponseCartGiftcardListResult.
        """
        self.openapi_types = {
            'additional_fields': object,
            'custom_fields': object,
            'gift_card': List[GiftCard]
        }

        self.attribute_map = {
            'additional_fields': 'additional_fields',
            'custom_fields': 'custom_fields',
            'gift_card': 'gift_card'
        }

        self._additional_fields = additional_fields
        self._custom_fields = custom_fields
        self._gift_card = gift_card

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ResponseCartGiftcardListResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Response_Cart_Giftcard_List_Result of this ResponseCartGiftcardListResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def additional_fields(self):
        """Gets the additional_fields of this ResponseCartGiftcardListResult.


        :return: The additional_fields of this ResponseCartGiftcardListResult.
        :rtype: object
        """
        return self._additional_fields

    @additional_fields.setter
    def additional_fields(self, additional_fields):
        """Sets the additional_fields of this ResponseCartGiftcardListResult.


        :param additional_fields: The additional_fields of this ResponseCartGiftcardListResult.
        :type additional_fields: object
        """

        self._additional_fields = additional_fields

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ResponseCartGiftcardListResult.


        :return: The custom_fields of this ResponseCartGiftcardListResult.
        :rtype: object
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ResponseCartGiftcardListResult.


        :param custom_fields: The custom_fields of this ResponseCartGiftcardListResult.
        :type custom_fields: object
        """

        self._custom_fields = custom_fields

    @property
    def gift_card(self):
        """Gets the gift_card of this ResponseCartGiftcardListResult.


        :return: The gift_card of this ResponseCartGiftcardListResult.
        :rtype: List[GiftCard]
        """
        return self._gift_card

    @gift_card.setter
    def gift_card(self, gift_card):
        """Sets the gift_card of this ResponseCartGiftcardListResult.


        :param gift_card: The gift_card of this ResponseCartGiftcardListResult.
        :type gift_card: List[GiftCard]
        """

        self._gift_card = gift_card
