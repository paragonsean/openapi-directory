# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CartCouponAdd200ResponseResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, coupon_id: str=None):
        """CartCouponAdd200ResponseResult - a model defined in OpenAPI

        :param coupon_id: The coupon_id of this CartCouponAdd200ResponseResult.
        """
        self.openapi_types = {
            'coupon_id': str
        }

        self.attribute_map = {
            'coupon_id': 'coupon_id'
        }

        self._coupon_id = coupon_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CartCouponAdd200ResponseResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CartCouponAdd_200_response_result of this CartCouponAdd200ResponseResult.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def coupon_id(self):
        """Gets the coupon_id of this CartCouponAdd200ResponseResult.


        :return: The coupon_id of this CartCouponAdd200ResponseResult.
        :rtype: str
        """
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, coupon_id):
        """Sets the coupon_id of this CartCouponAdd200ResponseResult.


        :param coupon_id: The coupon_id of this CartCouponAdd200ResponseResult.
        :type coupon_id: str
        """

        self._coupon_id = coupon_id
