# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SharedLines(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, b_lto_tr_border_id: str=None, bottom_border_id: str=None, connector_id: str=None, dash_type_id: int=None, head_end_height_id: int=None, head_end_type_id: int=None, head_end_width_id: int=None, id: str=None, left_border_id: str=None, line_map_id: str=None, right_border_id: str=None, shape_id: str=None, t_lto_br_border_id: str=None, tail_end_height_id: int=None, tail_end_type_id: int=None, tail_end_width_id: int=None, top_border_id: str=None, weight: int=None):
        """SharedLines - a model defined in OpenAPI

        :param b_lto_tr_border_id: The b_lto_tr_border_id of this SharedLines.
        :param bottom_border_id: The bottom_border_id of this SharedLines.
        :param connector_id: The connector_id of this SharedLines.
        :param dash_type_id: The dash_type_id of this SharedLines.
        :param head_end_height_id: The head_end_height_id of this SharedLines.
        :param head_end_type_id: The head_end_type_id of this SharedLines.
        :param head_end_width_id: The head_end_width_id of this SharedLines.
        :param id: The id of this SharedLines.
        :param left_border_id: The left_border_id of this SharedLines.
        :param line_map_id: The line_map_id of this SharedLines.
        :param right_border_id: The right_border_id of this SharedLines.
        :param shape_id: The shape_id of this SharedLines.
        :param t_lto_br_border_id: The t_lto_br_border_id of this SharedLines.
        :param tail_end_height_id: The tail_end_height_id of this SharedLines.
        :param tail_end_type_id: The tail_end_type_id of this SharedLines.
        :param tail_end_width_id: The tail_end_width_id of this SharedLines.
        :param top_border_id: The top_border_id of this SharedLines.
        :param weight: The weight of this SharedLines.
        """
        self.openapi_types = {
            'b_lto_tr_border_id': str,
            'bottom_border_id': str,
            'connector_id': str,
            'dash_type_id': int,
            'head_end_height_id': int,
            'head_end_type_id': int,
            'head_end_width_id': int,
            'id': str,
            'left_border_id': str,
            'line_map_id': str,
            'right_border_id': str,
            'shape_id': str,
            't_lto_br_border_id': str,
            'tail_end_height_id': int,
            'tail_end_type_id': int,
            'tail_end_width_id': int,
            'top_border_id': str,
            'weight': int
        }

        self.attribute_map = {
            'b_lto_tr_border_id': 'bLtoTRBorderId',
            'bottom_border_id': 'bottomBorderId',
            'connector_id': 'connectorId',
            'dash_type_id': 'dashTypeId',
            'head_end_height_id': 'headEndHeightId',
            'head_end_type_id': 'headEndTypeId',
            'head_end_width_id': 'headEndWidthId',
            'id': 'id',
            'left_border_id': 'leftBorderId',
            'line_map_id': 'lineMapId',
            'right_border_id': 'rightBorderId',
            'shape_id': 'shapeId',
            't_lto_br_border_id': 'tLtoBRBorderId',
            'tail_end_height_id': 'tailEndHeightId',
            'tail_end_type_id': 'tailEndTypeId',
            'tail_end_width_id': 'tailEndWidthId',
            'top_border_id': 'topBorderId',
            'weight': 'weight'
        }

        self._b_lto_tr_border_id = b_lto_tr_border_id
        self._bottom_border_id = bottom_border_id
        self._connector_id = connector_id
        self._dash_type_id = dash_type_id
        self._head_end_height_id = head_end_height_id
        self._head_end_type_id = head_end_type_id
        self._head_end_width_id = head_end_width_id
        self._id = id
        self._left_border_id = left_border_id
        self._line_map_id = line_map_id
        self._right_border_id = right_border_id
        self._shape_id = shape_id
        self._t_lto_br_border_id = t_lto_br_border_id
        self._tail_end_height_id = tail_end_height_id
        self._tail_end_type_id = tail_end_type_id
        self._tail_end_width_id = tail_end_width_id
        self._top_border_id = top_border_id
        self._weight = weight

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SharedLines':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Shared.Lines of this SharedLines.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def b_lto_tr_border_id(self):
        """Gets the b_lto_tr_border_id of this SharedLines.


        :return: The b_lto_tr_border_id of this SharedLines.
        :rtype: str
        """
        return self._b_lto_tr_border_id

    @b_lto_tr_border_id.setter
    def b_lto_tr_border_id(self, b_lto_tr_border_id):
        """Sets the b_lto_tr_border_id of this SharedLines.


        :param b_lto_tr_border_id: The b_lto_tr_border_id of this SharedLines.
        :type b_lto_tr_border_id: str
        """

        self._b_lto_tr_border_id = b_lto_tr_border_id

    @property
    def bottom_border_id(self):
        """Gets the bottom_border_id of this SharedLines.


        :return: The bottom_border_id of this SharedLines.
        :rtype: str
        """
        return self._bottom_border_id

    @bottom_border_id.setter
    def bottom_border_id(self, bottom_border_id):
        """Sets the bottom_border_id of this SharedLines.


        :param bottom_border_id: The bottom_border_id of this SharedLines.
        :type bottom_border_id: str
        """

        self._bottom_border_id = bottom_border_id

    @property
    def connector_id(self):
        """Gets the connector_id of this SharedLines.


        :return: The connector_id of this SharedLines.
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """Sets the connector_id of this SharedLines.


        :param connector_id: The connector_id of this SharedLines.
        :type connector_id: str
        """

        self._connector_id = connector_id

    @property
    def dash_type_id(self):
        """Gets the dash_type_id of this SharedLines.


        :return: The dash_type_id of this SharedLines.
        :rtype: int
        """
        return self._dash_type_id

    @dash_type_id.setter
    def dash_type_id(self, dash_type_id):
        """Sets the dash_type_id of this SharedLines.


        :param dash_type_id: The dash_type_id of this SharedLines.
        :type dash_type_id: int
        """

        self._dash_type_id = dash_type_id

    @property
    def head_end_height_id(self):
        """Gets the head_end_height_id of this SharedLines.


        :return: The head_end_height_id of this SharedLines.
        :rtype: int
        """
        return self._head_end_height_id

    @head_end_height_id.setter
    def head_end_height_id(self, head_end_height_id):
        """Sets the head_end_height_id of this SharedLines.


        :param head_end_height_id: The head_end_height_id of this SharedLines.
        :type head_end_height_id: int
        """

        self._head_end_height_id = head_end_height_id

    @property
    def head_end_type_id(self):
        """Gets the head_end_type_id of this SharedLines.


        :return: The head_end_type_id of this SharedLines.
        :rtype: int
        """
        return self._head_end_type_id

    @head_end_type_id.setter
    def head_end_type_id(self, head_end_type_id):
        """Sets the head_end_type_id of this SharedLines.


        :param head_end_type_id: The head_end_type_id of this SharedLines.
        :type head_end_type_id: int
        """

        self._head_end_type_id = head_end_type_id

    @property
    def head_end_width_id(self):
        """Gets the head_end_width_id of this SharedLines.


        :return: The head_end_width_id of this SharedLines.
        :rtype: int
        """
        return self._head_end_width_id

    @head_end_width_id.setter
    def head_end_width_id(self, head_end_width_id):
        """Sets the head_end_width_id of this SharedLines.


        :param head_end_width_id: The head_end_width_id of this SharedLines.
        :type head_end_width_id: int
        """

        self._head_end_width_id = head_end_width_id

    @property
    def id(self):
        """Gets the id of this SharedLines.


        :return: The id of this SharedLines.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedLines.


        :param id: The id of this SharedLines.
        :type id: str
        """

        self._id = id

    @property
    def left_border_id(self):
        """Gets the left_border_id of this SharedLines.


        :return: The left_border_id of this SharedLines.
        :rtype: str
        """
        return self._left_border_id

    @left_border_id.setter
    def left_border_id(self, left_border_id):
        """Sets the left_border_id of this SharedLines.


        :param left_border_id: The left_border_id of this SharedLines.
        :type left_border_id: str
        """

        self._left_border_id = left_border_id

    @property
    def line_map_id(self):
        """Gets the line_map_id of this SharedLines.


        :return: The line_map_id of this SharedLines.
        :rtype: str
        """
        return self._line_map_id

    @line_map_id.setter
    def line_map_id(self, line_map_id):
        """Sets the line_map_id of this SharedLines.


        :param line_map_id: The line_map_id of this SharedLines.
        :type line_map_id: str
        """

        self._line_map_id = line_map_id

    @property
    def right_border_id(self):
        """Gets the right_border_id of this SharedLines.


        :return: The right_border_id of this SharedLines.
        :rtype: str
        """
        return self._right_border_id

    @right_border_id.setter
    def right_border_id(self, right_border_id):
        """Sets the right_border_id of this SharedLines.


        :param right_border_id: The right_border_id of this SharedLines.
        :type right_border_id: str
        """

        self._right_border_id = right_border_id

    @property
    def shape_id(self):
        """Gets the shape_id of this SharedLines.


        :return: The shape_id of this SharedLines.
        :rtype: str
        """
        return self._shape_id

    @shape_id.setter
    def shape_id(self, shape_id):
        """Sets the shape_id of this SharedLines.


        :param shape_id: The shape_id of this SharedLines.
        :type shape_id: str
        """

        self._shape_id = shape_id

    @property
    def t_lto_br_border_id(self):
        """Gets the t_lto_br_border_id of this SharedLines.


        :return: The t_lto_br_border_id of this SharedLines.
        :rtype: str
        """
        return self._t_lto_br_border_id

    @t_lto_br_border_id.setter
    def t_lto_br_border_id(self, t_lto_br_border_id):
        """Sets the t_lto_br_border_id of this SharedLines.


        :param t_lto_br_border_id: The t_lto_br_border_id of this SharedLines.
        :type t_lto_br_border_id: str
        """

        self._t_lto_br_border_id = t_lto_br_border_id

    @property
    def tail_end_height_id(self):
        """Gets the tail_end_height_id of this SharedLines.


        :return: The tail_end_height_id of this SharedLines.
        :rtype: int
        """
        return self._tail_end_height_id

    @tail_end_height_id.setter
    def tail_end_height_id(self, tail_end_height_id):
        """Sets the tail_end_height_id of this SharedLines.


        :param tail_end_height_id: The tail_end_height_id of this SharedLines.
        :type tail_end_height_id: int
        """

        self._tail_end_height_id = tail_end_height_id

    @property
    def tail_end_type_id(self):
        """Gets the tail_end_type_id of this SharedLines.


        :return: The tail_end_type_id of this SharedLines.
        :rtype: int
        """
        return self._tail_end_type_id

    @tail_end_type_id.setter
    def tail_end_type_id(self, tail_end_type_id):
        """Sets the tail_end_type_id of this SharedLines.


        :param tail_end_type_id: The tail_end_type_id of this SharedLines.
        :type tail_end_type_id: int
        """

        self._tail_end_type_id = tail_end_type_id

    @property
    def tail_end_width_id(self):
        """Gets the tail_end_width_id of this SharedLines.


        :return: The tail_end_width_id of this SharedLines.
        :rtype: int
        """
        return self._tail_end_width_id

    @tail_end_width_id.setter
    def tail_end_width_id(self, tail_end_width_id):
        """Sets the tail_end_width_id of this SharedLines.


        :param tail_end_width_id: The tail_end_width_id of this SharedLines.
        :type tail_end_width_id: int
        """

        self._tail_end_width_id = tail_end_width_id

    @property
    def top_border_id(self):
        """Gets the top_border_id of this SharedLines.


        :return: The top_border_id of this SharedLines.
        :rtype: str
        """
        return self._top_border_id

    @top_border_id.setter
    def top_border_id(self, top_border_id):
        """Sets the top_border_id of this SharedLines.


        :param top_border_id: The top_border_id of this SharedLines.
        :type top_border_id: str
        """

        self._top_border_id = top_border_id

    @property
    def weight(self):
        """Gets the weight of this SharedLines.


        :return: The weight of this SharedLines.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this SharedLines.


        :param weight: The weight of this SharedLines.
        :type weight: int
        """

        self._weight = weight
