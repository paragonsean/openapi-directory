# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.slide_connector_details import SlideConnectorDetails
from openapi_server.models.slide_graphics_details import SlideGraphicsDetails
from openapi_server.models.slide_group_element_types_details import SlideGroupElementTypesDetails
from openapi_server.models.slide_groups_details import SlideGroupsDetails
from openapi_server.models.slide_shape_trees_details import SlideShapeTreesDetails
from openapi_server.models.slide_shapes_details import SlideShapesDetails
from openapi_server import util


class SlideGroupElementsDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, child_group_elements: List[SlideGroupElementsDetails]=None, connector: SlideConnectorDetails=None, date_created: datetime=None, date_modified: datetime=None, graphic: SlideGraphicsDetails=None, group: SlideGroupsDetails=None, group_element_type_id: int=None, group_element_type_pk: str=None, id: str=None, parent_group_element: SlideGroupElementsDetails=None, parent_group_element_id: str=None, shape: SlideShapesDetails=None, shape_tree: SlideShapeTreesDetails=None, shape_tree_id: str=None, type_info: SlideGroupElementTypesDetails=None, ultimate_parent_shape_tree_id: str=None, user_created: str=None, user_modified: str=None):
        """SlideGroupElementsDetails - a model defined in OpenAPI

        :param child_group_elements: The child_group_elements of this SlideGroupElementsDetails.
        :param connector: The connector of this SlideGroupElementsDetails.
        :param date_created: The date_created of this SlideGroupElementsDetails.
        :param date_modified: The date_modified of this SlideGroupElementsDetails.
        :param graphic: The graphic of this SlideGroupElementsDetails.
        :param group: The group of this SlideGroupElementsDetails.
        :param group_element_type_id: The group_element_type_id of this SlideGroupElementsDetails.
        :param group_element_type_pk: The group_element_type_pk of this SlideGroupElementsDetails.
        :param id: The id of this SlideGroupElementsDetails.
        :param parent_group_element: The parent_group_element of this SlideGroupElementsDetails.
        :param parent_group_element_id: The parent_group_element_id of this SlideGroupElementsDetails.
        :param shape: The shape of this SlideGroupElementsDetails.
        :param shape_tree: The shape_tree of this SlideGroupElementsDetails.
        :param shape_tree_id: The shape_tree_id of this SlideGroupElementsDetails.
        :param type_info: The type_info of this SlideGroupElementsDetails.
        :param ultimate_parent_shape_tree_id: The ultimate_parent_shape_tree_id of this SlideGroupElementsDetails.
        :param user_created: The user_created of this SlideGroupElementsDetails.
        :param user_modified: The user_modified of this SlideGroupElementsDetails.
        """
        self.openapi_types = {
            'child_group_elements': List[SlideGroupElementsDetails],
            'connector': SlideConnectorDetails,
            'date_created': datetime,
            'date_modified': datetime,
            'graphic': SlideGraphicsDetails,
            'group': SlideGroupsDetails,
            'group_element_type_id': int,
            'group_element_type_pk': str,
            'id': str,
            'parent_group_element': SlideGroupElementsDetails,
            'parent_group_element_id': str,
            'shape': SlideShapesDetails,
            'shape_tree': SlideShapeTreesDetails,
            'shape_tree_id': str,
            'type_info': SlideGroupElementTypesDetails,
            'ultimate_parent_shape_tree_id': str,
            'user_created': str,
            'user_modified': str
        }

        self.attribute_map = {
            'child_group_elements': 'childGroupElements',
            'connector': 'connector',
            'date_created': 'dateCreated',
            'date_modified': 'dateModified',
            'graphic': 'graphic',
            'group': 'group',
            'group_element_type_id': 'groupElementTypeId',
            'group_element_type_pk': 'groupElementTypePk',
            'id': 'id',
            'parent_group_element': 'parentGroupElement',
            'parent_group_element_id': 'parentGroupElementId',
            'shape': 'shape',
            'shape_tree': 'shapeTree',
            'shape_tree_id': 'shapeTreeId',
            'type_info': 'typeInfo',
            'ultimate_parent_shape_tree_id': 'ultimateParentShapeTreeId',
            'user_created': 'userCreated',
            'user_modified': 'userModified'
        }

        self._child_group_elements = child_group_elements
        self._connector = connector
        self._date_created = date_created
        self._date_modified = date_modified
        self._graphic = graphic
        self._group = group
        self._group_element_type_id = group_element_type_id
        self._group_element_type_pk = group_element_type_pk
        self._id = id
        self._parent_group_element = parent_group_element
        self._parent_group_element_id = parent_group_element_id
        self._shape = shape
        self._shape_tree = shape_tree
        self._shape_tree_id = shape_tree_id
        self._type_info = type_info
        self._ultimate_parent_shape_tree_id = ultimate_parent_shape_tree_id
        self._user_created = user_created
        self._user_modified = user_modified

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SlideGroupElementsDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Slide.GroupElements.Details of this SlideGroupElementsDetails.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def child_group_elements(self):
        """Gets the child_group_elements of this SlideGroupElementsDetails.


        :return: The child_group_elements of this SlideGroupElementsDetails.
        :rtype: List[SlideGroupElementsDetails]
        """
        return self._child_group_elements

    @child_group_elements.setter
    def child_group_elements(self, child_group_elements):
        """Sets the child_group_elements of this SlideGroupElementsDetails.


        :param child_group_elements: The child_group_elements of this SlideGroupElementsDetails.
        :type child_group_elements: List[SlideGroupElementsDetails]
        """

        self._child_group_elements = child_group_elements

    @property
    def connector(self):
        """Gets the connector of this SlideGroupElementsDetails.


        :return: The connector of this SlideGroupElementsDetails.
        :rtype: SlideConnectorDetails
        """
        return self._connector

    @connector.setter
    def connector(self, connector):
        """Sets the connector of this SlideGroupElementsDetails.


        :param connector: The connector of this SlideGroupElementsDetails.
        :type connector: SlideConnectorDetails
        """

        self._connector = connector

    @property
    def date_created(self):
        """Gets the date_created of this SlideGroupElementsDetails.


        :return: The date_created of this SlideGroupElementsDetails.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SlideGroupElementsDetails.


        :param date_created: The date_created of this SlideGroupElementsDetails.
        :type date_created: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this SlideGroupElementsDetails.


        :return: The date_modified of this SlideGroupElementsDetails.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SlideGroupElementsDetails.


        :param date_modified: The date_modified of this SlideGroupElementsDetails.
        :type date_modified: datetime
        """

        self._date_modified = date_modified

    @property
    def graphic(self):
        """Gets the graphic of this SlideGroupElementsDetails.


        :return: The graphic of this SlideGroupElementsDetails.
        :rtype: SlideGraphicsDetails
        """
        return self._graphic

    @graphic.setter
    def graphic(self, graphic):
        """Sets the graphic of this SlideGroupElementsDetails.


        :param graphic: The graphic of this SlideGroupElementsDetails.
        :type graphic: SlideGraphicsDetails
        """

        self._graphic = graphic

    @property
    def group(self):
        """Gets the group of this SlideGroupElementsDetails.


        :return: The group of this SlideGroupElementsDetails.
        :rtype: SlideGroupsDetails
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this SlideGroupElementsDetails.


        :param group: The group of this SlideGroupElementsDetails.
        :type group: SlideGroupsDetails
        """

        self._group = group

    @property
    def group_element_type_id(self):
        """Gets the group_element_type_id of this SlideGroupElementsDetails.


        :return: The group_element_type_id of this SlideGroupElementsDetails.
        :rtype: int
        """
        return self._group_element_type_id

    @group_element_type_id.setter
    def group_element_type_id(self, group_element_type_id):
        """Sets the group_element_type_id of this SlideGroupElementsDetails.


        :param group_element_type_id: The group_element_type_id of this SlideGroupElementsDetails.
        :type group_element_type_id: int
        """

        self._group_element_type_id = group_element_type_id

    @property
    def group_element_type_pk(self):
        """Gets the group_element_type_pk of this SlideGroupElementsDetails.


        :return: The group_element_type_pk of this SlideGroupElementsDetails.
        :rtype: str
        """
        return self._group_element_type_pk

    @group_element_type_pk.setter
    def group_element_type_pk(self, group_element_type_pk):
        """Sets the group_element_type_pk of this SlideGroupElementsDetails.


        :param group_element_type_pk: The group_element_type_pk of this SlideGroupElementsDetails.
        :type group_element_type_pk: str
        """

        self._group_element_type_pk = group_element_type_pk

    @property
    def id(self):
        """Gets the id of this SlideGroupElementsDetails.


        :return: The id of this SlideGroupElementsDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SlideGroupElementsDetails.


        :param id: The id of this SlideGroupElementsDetails.
        :type id: str
        """

        self._id = id

    @property
    def parent_group_element(self):
        """Gets the parent_group_element of this SlideGroupElementsDetails.


        :return: The parent_group_element of this SlideGroupElementsDetails.
        :rtype: SlideGroupElementsDetails
        """
        return self._parent_group_element

    @parent_group_element.setter
    def parent_group_element(self, parent_group_element):
        """Sets the parent_group_element of this SlideGroupElementsDetails.


        :param parent_group_element: The parent_group_element of this SlideGroupElementsDetails.
        :type parent_group_element: SlideGroupElementsDetails
        """

        self._parent_group_element = parent_group_element

    @property
    def parent_group_element_id(self):
        """Gets the parent_group_element_id of this SlideGroupElementsDetails.


        :return: The parent_group_element_id of this SlideGroupElementsDetails.
        :rtype: str
        """
        return self._parent_group_element_id

    @parent_group_element_id.setter
    def parent_group_element_id(self, parent_group_element_id):
        """Sets the parent_group_element_id of this SlideGroupElementsDetails.


        :param parent_group_element_id: The parent_group_element_id of this SlideGroupElementsDetails.
        :type parent_group_element_id: str
        """

        self._parent_group_element_id = parent_group_element_id

    @property
    def shape(self):
        """Gets the shape of this SlideGroupElementsDetails.


        :return: The shape of this SlideGroupElementsDetails.
        :rtype: SlideShapesDetails
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this SlideGroupElementsDetails.


        :param shape: The shape of this SlideGroupElementsDetails.
        :type shape: SlideShapesDetails
        """

        self._shape = shape

    @property
    def shape_tree(self):
        """Gets the shape_tree of this SlideGroupElementsDetails.


        :return: The shape_tree of this SlideGroupElementsDetails.
        :rtype: SlideShapeTreesDetails
        """
        return self._shape_tree

    @shape_tree.setter
    def shape_tree(self, shape_tree):
        """Sets the shape_tree of this SlideGroupElementsDetails.


        :param shape_tree: The shape_tree of this SlideGroupElementsDetails.
        :type shape_tree: SlideShapeTreesDetails
        """

        self._shape_tree = shape_tree

    @property
    def shape_tree_id(self):
        """Gets the shape_tree_id of this SlideGroupElementsDetails.


        :return: The shape_tree_id of this SlideGroupElementsDetails.
        :rtype: str
        """
        return self._shape_tree_id

    @shape_tree_id.setter
    def shape_tree_id(self, shape_tree_id):
        """Sets the shape_tree_id of this SlideGroupElementsDetails.


        :param shape_tree_id: The shape_tree_id of this SlideGroupElementsDetails.
        :type shape_tree_id: str
        """

        self._shape_tree_id = shape_tree_id

    @property
    def type_info(self):
        """Gets the type_info of this SlideGroupElementsDetails.


        :return: The type_info of this SlideGroupElementsDetails.
        :rtype: SlideGroupElementTypesDetails
        """
        return self._type_info

    @type_info.setter
    def type_info(self, type_info):
        """Sets the type_info of this SlideGroupElementsDetails.


        :param type_info: The type_info of this SlideGroupElementsDetails.
        :type type_info: SlideGroupElementTypesDetails
        """

        self._type_info = type_info

    @property
    def ultimate_parent_shape_tree_id(self):
        """Gets the ultimate_parent_shape_tree_id of this SlideGroupElementsDetails.


        :return: The ultimate_parent_shape_tree_id of this SlideGroupElementsDetails.
        :rtype: str
        """
        return self._ultimate_parent_shape_tree_id

    @ultimate_parent_shape_tree_id.setter
    def ultimate_parent_shape_tree_id(self, ultimate_parent_shape_tree_id):
        """Sets the ultimate_parent_shape_tree_id of this SlideGroupElementsDetails.


        :param ultimate_parent_shape_tree_id: The ultimate_parent_shape_tree_id of this SlideGroupElementsDetails.
        :type ultimate_parent_shape_tree_id: str
        """

        self._ultimate_parent_shape_tree_id = ultimate_parent_shape_tree_id

    @property
    def user_created(self):
        """Gets the user_created of this SlideGroupElementsDetails.


        :return: The user_created of this SlideGroupElementsDetails.
        :rtype: str
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        """Sets the user_created of this SlideGroupElementsDetails.


        :param user_created: The user_created of this SlideGroupElementsDetails.
        :type user_created: str
        """

        self._user_created = user_created

    @property
    def user_modified(self):
        """Gets the user_modified of this SlideGroupElementsDetails.


        :return: The user_modified of this SlideGroupElementsDetails.
        :rtype: str
        """
        return self._user_modified

    @user_modified.setter
    def user_modified(self, user_modified):
        """Sets the user_modified of this SlideGroupElementsDetails.


        :param user_modified: The user_modified of this SlideGroupElementsDetails.
        :type user_modified: str
        """

        self._user_modified = user_modified
