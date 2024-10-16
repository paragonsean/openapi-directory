# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.notification_relationships_owner_user import NotificationRelationshipsOwnerUser
from openapi_server.models.notification_relationships_resource import NotificationRelationshipsResource
from openapi_server.models.notification_relationships_share import NotificationRelationshipsShare
from openapi_server import util


class NotificationRelationships(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, owner_user: NotificationRelationshipsOwnerUser=None, resource: NotificationRelationshipsResource=None, share: NotificationRelationshipsShare=None):
        """NotificationRelationships - a model defined in OpenAPI

        :param owner_user: The owner_user of this NotificationRelationships.
        :param resource: The resource of this NotificationRelationships.
        :param share: The share of this NotificationRelationships.
        """
        self.openapi_types = {
            'owner_user': NotificationRelationshipsOwnerUser,
            'resource': NotificationRelationshipsResource,
            'share': NotificationRelationshipsShare
        }

        self.attribute_map = {
            'owner_user': 'ownerUser',
            'resource': 'resource',
            'share': 'share'
        }

        self._owner_user = owner_user
        self._resource = resource
        self._share = share

    @classmethod
    def from_dict(cls, dikt: dict) -> 'NotificationRelationships':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Notification_relationships of this NotificationRelationships.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def owner_user(self):
        """Gets the owner_user of this NotificationRelationships.


        :return: The owner_user of this NotificationRelationships.
        :rtype: NotificationRelationshipsOwnerUser
        """
        return self._owner_user

    @owner_user.setter
    def owner_user(self, owner_user):
        """Sets the owner_user of this NotificationRelationships.


        :param owner_user: The owner_user of this NotificationRelationships.
        :type owner_user: NotificationRelationshipsOwnerUser
        """

        self._owner_user = owner_user

    @property
    def resource(self):
        """Gets the resource of this NotificationRelationships.


        :return: The resource of this NotificationRelationships.
        :rtype: NotificationRelationshipsResource
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this NotificationRelationships.


        :param resource: The resource of this NotificationRelationships.
        :type resource: NotificationRelationshipsResource
        """

        self._resource = resource

    @property
    def share(self):
        """Gets the share of this NotificationRelationships.


        :return: The share of this NotificationRelationships.
        :rtype: NotificationRelationshipsShare
        """
        return self._share

    @share.setter
    def share(self, share):
        """Sets the share of this NotificationRelationships.


        :param share: The share of this NotificationRelationships.
        :type share: NotificationRelationshipsShare
        """

        self._share = share
