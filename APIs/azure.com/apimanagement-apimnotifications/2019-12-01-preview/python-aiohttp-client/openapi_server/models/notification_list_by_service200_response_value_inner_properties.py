# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.notification_list_by_service200_response_value_inner_properties_recipients import NotificationListByService200ResponseValueInnerPropertiesRecipients
from openapi_server import util


class NotificationListByService200ResponseValueInnerProperties(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, recipients: NotificationListByService200ResponseValueInnerPropertiesRecipients=None, title: str=None):
        """NotificationListByService200ResponseValueInnerProperties - a model defined in OpenAPI

        :param description: The description of this NotificationListByService200ResponseValueInnerProperties.
        :param recipients: The recipients of this NotificationListByService200ResponseValueInnerProperties.
        :param title: The title of this NotificationListByService200ResponseValueInnerProperties.
        """
        self.openapi_types = {
            'description': str,
            'recipients': NotificationListByService200ResponseValueInnerPropertiesRecipients,
            'title': str
        }

        self.attribute_map = {
            'description': 'description',
            'recipients': 'recipients',
            'title': 'title'
        }

        self._description = description
        self._recipients = recipients
        self._title = title

    @classmethod
    def from_dict(cls, dikt: dict) -> 'NotificationListByService200ResponseValueInnerProperties':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Notification_ListByService_200_response_value_inner_properties of this NotificationListByService200ResponseValueInnerProperties.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this NotificationListByService200ResponseValueInnerProperties.

        Description of the Notification.

        :return: The description of this NotificationListByService200ResponseValueInnerProperties.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NotificationListByService200ResponseValueInnerProperties.

        Description of the Notification.

        :param description: The description of this NotificationListByService200ResponseValueInnerProperties.
        :type description: str
        """

        self._description = description

    @property
    def recipients(self):
        """Gets the recipients of this NotificationListByService200ResponseValueInnerProperties.


        :return: The recipients of this NotificationListByService200ResponseValueInnerProperties.
        :rtype: NotificationListByService200ResponseValueInnerPropertiesRecipients
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this NotificationListByService200ResponseValueInnerProperties.


        :param recipients: The recipients of this NotificationListByService200ResponseValueInnerProperties.
        :type recipients: NotificationListByService200ResponseValueInnerPropertiesRecipients
        """

        self._recipients = recipients

    @property
    def title(self):
        """Gets the title of this NotificationListByService200ResponseValueInnerProperties.

        Title of the Notification.

        :return: The title of this NotificationListByService200ResponseValueInnerProperties.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NotificationListByService200ResponseValueInnerProperties.

        Title of the Notification.

        :param title: The title of this NotificationListByService200ResponseValueInnerProperties.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")
        if title is not None and len(title) > 1000:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `1000`")
        if title is not None and len(title) < 1:
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `1`")

        self._title = title
