# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.api_core_dto_tags_tag import ApiCoreDtoTagsTag
from openapi_server import util


class ApiCoreDtoClickStreamHitDatapointInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, creation_date: str=None, datapoint_favourite: bool=None, datapoint_id: int=None, datapoint_name: str=None, datapoint_title: str=None, datapoint_type: str=None, destination_url: str=None, group_id: int=None, group_name: str=None, is_ab_test: bool=None, is_private_shared: bool=None, is_public: bool=None, notes: str=None, status: str=None, tags: List[ApiCoreDtoTagsTag]=None, tracking_code: str=None):
        """ApiCoreDtoClickStreamHitDatapointInfo - a model defined in OpenAPI

        :param creation_date: The creation_date of this ApiCoreDtoClickStreamHitDatapointInfo.
        :param datapoint_favourite: The datapoint_favourite of this ApiCoreDtoClickStreamHitDatapointInfo.
        :param datapoint_id: The datapoint_id of this ApiCoreDtoClickStreamHitDatapointInfo.
        :param datapoint_name: The datapoint_name of this ApiCoreDtoClickStreamHitDatapointInfo.
        :param datapoint_title: The datapoint_title of this ApiCoreDtoClickStreamHitDatapointInfo.
        :param datapoint_type: The datapoint_type of this ApiCoreDtoClickStreamHitDatapointInfo.
        :param destination_url: The destination_url of this ApiCoreDtoClickStreamHitDatapointInfo.
        :param group_id: The group_id of this ApiCoreDtoClickStreamHitDatapointInfo.
        :param group_name: The group_name of this ApiCoreDtoClickStreamHitDatapointInfo.
        :param is_ab_test: The is_ab_test of this ApiCoreDtoClickStreamHitDatapointInfo.
        :param is_private_shared: The is_private_shared of this ApiCoreDtoClickStreamHitDatapointInfo.
        :param is_public: The is_public of this ApiCoreDtoClickStreamHitDatapointInfo.
        :param notes: The notes of this ApiCoreDtoClickStreamHitDatapointInfo.
        :param status: The status of this ApiCoreDtoClickStreamHitDatapointInfo.
        :param tags: The tags of this ApiCoreDtoClickStreamHitDatapointInfo.
        :param tracking_code: The tracking_code of this ApiCoreDtoClickStreamHitDatapointInfo.
        """
        self.openapi_types = {
            'creation_date': str,
            'datapoint_favourite': bool,
            'datapoint_id': int,
            'datapoint_name': str,
            'datapoint_title': str,
            'datapoint_type': str,
            'destination_url': str,
            'group_id': int,
            'group_name': str,
            'is_ab_test': bool,
            'is_private_shared': bool,
            'is_public': bool,
            'notes': str,
            'status': str,
            'tags': List[ApiCoreDtoTagsTag],
            'tracking_code': str
        }

        self.attribute_map = {
            'creation_date': 'creationDate',
            'datapoint_favourite': 'datapointFavourite',
            'datapoint_id': 'datapointId',
            'datapoint_name': 'datapointName',
            'datapoint_title': 'datapointTitle',
            'datapoint_type': 'datapointType',
            'destination_url': 'destinationUrl',
            'group_id': 'groupId',
            'group_name': 'groupName',
            'is_ab_test': 'isABTest',
            'is_private_shared': 'isPrivateShared',
            'is_public': 'isPublic',
            'notes': 'notes',
            'status': 'status',
            'tags': 'tags',
            'tracking_code': 'trackingCode'
        }

        self._creation_date = creation_date
        self._datapoint_favourite = datapoint_favourite
        self._datapoint_id = datapoint_id
        self._datapoint_name = datapoint_name
        self._datapoint_title = datapoint_title
        self._datapoint_type = datapoint_type
        self._destination_url = destination_url
        self._group_id = group_id
        self._group_name = group_name
        self._is_ab_test = is_ab_test
        self._is_private_shared = is_private_shared
        self._is_public = is_public
        self._notes = notes
        self._status = status
        self._tags = tags
        self._tracking_code = tracking_code

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ApiCoreDtoClickStreamHitDatapointInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Api.Core.Dto.ClickStream.HitDatapointInfo of this ApiCoreDtoClickStreamHitDatapointInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def creation_date(self):
        """Gets the creation_date of this ApiCoreDtoClickStreamHitDatapointInfo.

         (A date in \"YmdHis\" format)

        :return: The creation_date of this ApiCoreDtoClickStreamHitDatapointInfo.
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ApiCoreDtoClickStreamHitDatapointInfo.

         (A date in \"YmdHis\" format)

        :param creation_date: The creation_date of this ApiCoreDtoClickStreamHitDatapointInfo.
        :type creation_date: str
        """

        self._creation_date = creation_date

    @property
    def datapoint_favourite(self):
        """Gets the datapoint_favourite of this ApiCoreDtoClickStreamHitDatapointInfo.


        :return: The datapoint_favourite of this ApiCoreDtoClickStreamHitDatapointInfo.
        :rtype: bool
        """
        return self._datapoint_favourite

    @datapoint_favourite.setter
    def datapoint_favourite(self, datapoint_favourite):
        """Sets the datapoint_favourite of this ApiCoreDtoClickStreamHitDatapointInfo.


        :param datapoint_favourite: The datapoint_favourite of this ApiCoreDtoClickStreamHitDatapointInfo.
        :type datapoint_favourite: bool
        """

        self._datapoint_favourite = datapoint_favourite

    @property
    def datapoint_id(self):
        """Gets the datapoint_id of this ApiCoreDtoClickStreamHitDatapointInfo.


        :return: The datapoint_id of this ApiCoreDtoClickStreamHitDatapointInfo.
        :rtype: int
        """
        return self._datapoint_id

    @datapoint_id.setter
    def datapoint_id(self, datapoint_id):
        """Sets the datapoint_id of this ApiCoreDtoClickStreamHitDatapointInfo.


        :param datapoint_id: The datapoint_id of this ApiCoreDtoClickStreamHitDatapointInfo.
        :type datapoint_id: int
        """

        self._datapoint_id = datapoint_id

    @property
    def datapoint_name(self):
        """Gets the datapoint_name of this ApiCoreDtoClickStreamHitDatapointInfo.


        :return: The datapoint_name of this ApiCoreDtoClickStreamHitDatapointInfo.
        :rtype: str
        """
        return self._datapoint_name

    @datapoint_name.setter
    def datapoint_name(self, datapoint_name):
        """Sets the datapoint_name of this ApiCoreDtoClickStreamHitDatapointInfo.


        :param datapoint_name: The datapoint_name of this ApiCoreDtoClickStreamHitDatapointInfo.
        :type datapoint_name: str
        """

        self._datapoint_name = datapoint_name

    @property
    def datapoint_title(self):
        """Gets the datapoint_title of this ApiCoreDtoClickStreamHitDatapointInfo.


        :return: The datapoint_title of this ApiCoreDtoClickStreamHitDatapointInfo.
        :rtype: str
        """
        return self._datapoint_title

    @datapoint_title.setter
    def datapoint_title(self, datapoint_title):
        """Sets the datapoint_title of this ApiCoreDtoClickStreamHitDatapointInfo.


        :param datapoint_title: The datapoint_title of this ApiCoreDtoClickStreamHitDatapointInfo.
        :type datapoint_title: str
        """

        self._datapoint_title = datapoint_title

    @property
    def datapoint_type(self):
        """Gets the datapoint_type of this ApiCoreDtoClickStreamHitDatapointInfo.


        :return: The datapoint_type of this ApiCoreDtoClickStreamHitDatapointInfo.
        :rtype: str
        """
        return self._datapoint_type

    @datapoint_type.setter
    def datapoint_type(self, datapoint_type):
        """Sets the datapoint_type of this ApiCoreDtoClickStreamHitDatapointInfo.


        :param datapoint_type: The datapoint_type of this ApiCoreDtoClickStreamHitDatapointInfo.
        :type datapoint_type: str
        """

        self._datapoint_type = datapoint_type

    @property
    def destination_url(self):
        """Gets the destination_url of this ApiCoreDtoClickStreamHitDatapointInfo.


        :return: The destination_url of this ApiCoreDtoClickStreamHitDatapointInfo.
        :rtype: str
        """
        return self._destination_url

    @destination_url.setter
    def destination_url(self, destination_url):
        """Sets the destination_url of this ApiCoreDtoClickStreamHitDatapointInfo.


        :param destination_url: The destination_url of this ApiCoreDtoClickStreamHitDatapointInfo.
        :type destination_url: str
        """

        self._destination_url = destination_url

    @property
    def group_id(self):
        """Gets the group_id of this ApiCoreDtoClickStreamHitDatapointInfo.


        :return: The group_id of this ApiCoreDtoClickStreamHitDatapointInfo.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ApiCoreDtoClickStreamHitDatapointInfo.


        :param group_id: The group_id of this ApiCoreDtoClickStreamHitDatapointInfo.
        :type group_id: int
        """

        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this ApiCoreDtoClickStreamHitDatapointInfo.


        :return: The group_name of this ApiCoreDtoClickStreamHitDatapointInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ApiCoreDtoClickStreamHitDatapointInfo.


        :param group_name: The group_name of this ApiCoreDtoClickStreamHitDatapointInfo.
        :type group_name: str
        """

        self._group_name = group_name

    @property
    def is_ab_test(self):
        """Gets the is_ab_test of this ApiCoreDtoClickStreamHitDatapointInfo.


        :return: The is_ab_test of this ApiCoreDtoClickStreamHitDatapointInfo.
        :rtype: bool
        """
        return self._is_ab_test

    @is_ab_test.setter
    def is_ab_test(self, is_ab_test):
        """Sets the is_ab_test of this ApiCoreDtoClickStreamHitDatapointInfo.


        :param is_ab_test: The is_ab_test of this ApiCoreDtoClickStreamHitDatapointInfo.
        :type is_ab_test: bool
        """

        self._is_ab_test = is_ab_test

    @property
    def is_private_shared(self):
        """Gets the is_private_shared of this ApiCoreDtoClickStreamHitDatapointInfo.


        :return: The is_private_shared of this ApiCoreDtoClickStreamHitDatapointInfo.
        :rtype: bool
        """
        return self._is_private_shared

    @is_private_shared.setter
    def is_private_shared(self, is_private_shared):
        """Sets the is_private_shared of this ApiCoreDtoClickStreamHitDatapointInfo.


        :param is_private_shared: The is_private_shared of this ApiCoreDtoClickStreamHitDatapointInfo.
        :type is_private_shared: bool
        """

        self._is_private_shared = is_private_shared

    @property
    def is_public(self):
        """Gets the is_public of this ApiCoreDtoClickStreamHitDatapointInfo.


        :return: The is_public of this ApiCoreDtoClickStreamHitDatapointInfo.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this ApiCoreDtoClickStreamHitDatapointInfo.


        :param is_public: The is_public of this ApiCoreDtoClickStreamHitDatapointInfo.
        :type is_public: bool
        """

        self._is_public = is_public

    @property
    def notes(self):
        """Gets the notes of this ApiCoreDtoClickStreamHitDatapointInfo.


        :return: The notes of this ApiCoreDtoClickStreamHitDatapointInfo.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this ApiCoreDtoClickStreamHitDatapointInfo.


        :param notes: The notes of this ApiCoreDtoClickStreamHitDatapointInfo.
        :type notes: str
        """

        self._notes = notes

    @property
    def status(self):
        """Gets the status of this ApiCoreDtoClickStreamHitDatapointInfo.


        :return: The status of this ApiCoreDtoClickStreamHitDatapointInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiCoreDtoClickStreamHitDatapointInfo.


        :param status: The status of this ApiCoreDtoClickStreamHitDatapointInfo.
        :type status: str
        """
        allowed_values = ["Active", "Paused", "Abuse", "Deleted"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this ApiCoreDtoClickStreamHitDatapointInfo.


        :return: The tags of this ApiCoreDtoClickStreamHitDatapointInfo.
        :rtype: List[ApiCoreDtoTagsTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ApiCoreDtoClickStreamHitDatapointInfo.


        :param tags: The tags of this ApiCoreDtoClickStreamHitDatapointInfo.
        :type tags: List[ApiCoreDtoTagsTag]
        """

        self._tags = tags

    @property
    def tracking_code(self):
        """Gets the tracking_code of this ApiCoreDtoClickStreamHitDatapointInfo.


        :return: The tracking_code of this ApiCoreDtoClickStreamHitDatapointInfo.
        :rtype: str
        """
        return self._tracking_code

    @tracking_code.setter
    def tracking_code(self, tracking_code):
        """Sets the tracking_code of this ApiCoreDtoClickStreamHitDatapointInfo.


        :param tracking_code: The tracking_code of this ApiCoreDtoClickStreamHitDatapointInfo.
        :type tracking_code: str
        """

        self._tracking_code = tracking_code
