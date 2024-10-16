# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.create_network_floor_plan_request_bottom_left_corner import CreateNetworkFloorPlanRequestBottomLeftCorner
from openapi_server.models.create_network_floor_plan_request_bottom_right_corner import CreateNetworkFloorPlanRequestBottomRightCorner
from openapi_server.models.create_network_floor_plan_request_center import CreateNetworkFloorPlanRequestCenter
from openapi_server.models.create_network_floor_plan_request_top_left_corner import CreateNetworkFloorPlanRequestTopLeftCorner
from openapi_server.models.create_network_floor_plan_request_top_right_corner import CreateNetworkFloorPlanRequestTopRightCorner
from openapi_server import util


class CreateNetworkFloorPlanRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bottom_left_corner: CreateNetworkFloorPlanRequestBottomLeftCorner=None, bottom_right_corner: CreateNetworkFloorPlanRequestBottomRightCorner=None, center: CreateNetworkFloorPlanRequestCenter=None, image_contents: str=None, name: str=None, top_left_corner: CreateNetworkFloorPlanRequestTopLeftCorner=None, top_right_corner: CreateNetworkFloorPlanRequestTopRightCorner=None):
        """CreateNetworkFloorPlanRequest - a model defined in OpenAPI

        :param bottom_left_corner: The bottom_left_corner of this CreateNetworkFloorPlanRequest.
        :param bottom_right_corner: The bottom_right_corner of this CreateNetworkFloorPlanRequest.
        :param center: The center of this CreateNetworkFloorPlanRequest.
        :param image_contents: The image_contents of this CreateNetworkFloorPlanRequest.
        :param name: The name of this CreateNetworkFloorPlanRequest.
        :param top_left_corner: The top_left_corner of this CreateNetworkFloorPlanRequest.
        :param top_right_corner: The top_right_corner of this CreateNetworkFloorPlanRequest.
        """
        self.openapi_types = {
            'bottom_left_corner': CreateNetworkFloorPlanRequestBottomLeftCorner,
            'bottom_right_corner': CreateNetworkFloorPlanRequestBottomRightCorner,
            'center': CreateNetworkFloorPlanRequestCenter,
            'image_contents': str,
            'name': str,
            'top_left_corner': CreateNetworkFloorPlanRequestTopLeftCorner,
            'top_right_corner': CreateNetworkFloorPlanRequestTopRightCorner
        }

        self.attribute_map = {
            'bottom_left_corner': 'bottomLeftCorner',
            'bottom_right_corner': 'bottomRightCorner',
            'center': 'center',
            'image_contents': 'imageContents',
            'name': 'name',
            'top_left_corner': 'topLeftCorner',
            'top_right_corner': 'topRightCorner'
        }

        self._bottom_left_corner = bottom_left_corner
        self._bottom_right_corner = bottom_right_corner
        self._center = center
        self._image_contents = image_contents
        self._name = name
        self._top_left_corner = top_left_corner
        self._top_right_corner = top_right_corner

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CreateNetworkFloorPlanRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The createNetworkFloorPlan_request of this CreateNetworkFloorPlanRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bottom_left_corner(self):
        """Gets the bottom_left_corner of this CreateNetworkFloorPlanRequest.


        :return: The bottom_left_corner of this CreateNetworkFloorPlanRequest.
        :rtype: CreateNetworkFloorPlanRequestBottomLeftCorner
        """
        return self._bottom_left_corner

    @bottom_left_corner.setter
    def bottom_left_corner(self, bottom_left_corner):
        """Sets the bottom_left_corner of this CreateNetworkFloorPlanRequest.


        :param bottom_left_corner: The bottom_left_corner of this CreateNetworkFloorPlanRequest.
        :type bottom_left_corner: CreateNetworkFloorPlanRequestBottomLeftCorner
        """

        self._bottom_left_corner = bottom_left_corner

    @property
    def bottom_right_corner(self):
        """Gets the bottom_right_corner of this CreateNetworkFloorPlanRequest.


        :return: The bottom_right_corner of this CreateNetworkFloorPlanRequest.
        :rtype: CreateNetworkFloorPlanRequestBottomRightCorner
        """
        return self._bottom_right_corner

    @bottom_right_corner.setter
    def bottom_right_corner(self, bottom_right_corner):
        """Sets the bottom_right_corner of this CreateNetworkFloorPlanRequest.


        :param bottom_right_corner: The bottom_right_corner of this CreateNetworkFloorPlanRequest.
        :type bottom_right_corner: CreateNetworkFloorPlanRequestBottomRightCorner
        """

        self._bottom_right_corner = bottom_right_corner

    @property
    def center(self):
        """Gets the center of this CreateNetworkFloorPlanRequest.


        :return: The center of this CreateNetworkFloorPlanRequest.
        :rtype: CreateNetworkFloorPlanRequestCenter
        """
        return self._center

    @center.setter
    def center(self, center):
        """Sets the center of this CreateNetworkFloorPlanRequest.


        :param center: The center of this CreateNetworkFloorPlanRequest.
        :type center: CreateNetworkFloorPlanRequestCenter
        """

        self._center = center

    @property
    def image_contents(self):
        """Gets the image_contents of this CreateNetworkFloorPlanRequest.

        The file contents (a base 64 encoded string) of your image. Supported formats are PNG, GIF, and JPG. Note that all images are saved as PNG files, regardless of the format they are uploaded in.

        :return: The image_contents of this CreateNetworkFloorPlanRequest.
        :rtype: str
        """
        return self._image_contents

    @image_contents.setter
    def image_contents(self, image_contents):
        """Sets the image_contents of this CreateNetworkFloorPlanRequest.

        The file contents (a base 64 encoded string) of your image. Supported formats are PNG, GIF, and JPG. Note that all images are saved as PNG files, regardless of the format they are uploaded in.

        :param image_contents: The image_contents of this CreateNetworkFloorPlanRequest.
        :type image_contents: str
        """
        if image_contents is None:
            raise ValueError("Invalid value for `image_contents`, must not be `None`")

        self._image_contents = image_contents

    @property
    def name(self):
        """Gets the name of this CreateNetworkFloorPlanRequest.

        The name of your floor plan.

        :return: The name of this CreateNetworkFloorPlanRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateNetworkFloorPlanRequest.

        The name of your floor plan.

        :param name: The name of this CreateNetworkFloorPlanRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def top_left_corner(self):
        """Gets the top_left_corner of this CreateNetworkFloorPlanRequest.


        :return: The top_left_corner of this CreateNetworkFloorPlanRequest.
        :rtype: CreateNetworkFloorPlanRequestTopLeftCorner
        """
        return self._top_left_corner

    @top_left_corner.setter
    def top_left_corner(self, top_left_corner):
        """Sets the top_left_corner of this CreateNetworkFloorPlanRequest.


        :param top_left_corner: The top_left_corner of this CreateNetworkFloorPlanRequest.
        :type top_left_corner: CreateNetworkFloorPlanRequestTopLeftCorner
        """

        self._top_left_corner = top_left_corner

    @property
    def top_right_corner(self):
        """Gets the top_right_corner of this CreateNetworkFloorPlanRequest.


        :return: The top_right_corner of this CreateNetworkFloorPlanRequest.
        :rtype: CreateNetworkFloorPlanRequestTopRightCorner
        """
        return self._top_right_corner

    @top_right_corner.setter
    def top_right_corner(self, top_right_corner):
        """Sets the top_right_corner of this CreateNetworkFloorPlanRequest.


        :param top_right_corner: The top_right_corner of this CreateNetworkFloorPlanRequest.
        :type top_right_corner: CreateNetworkFloorPlanRequestTopRightCorner
        """

        self._top_right_corner = top_right_corner
