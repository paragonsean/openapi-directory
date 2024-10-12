# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.reference_vm_fragment import ReferenceVmFragment
from openapi_server import util


class ResourceSettingsFragment(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, gallery_image_resource_id: str=None, reference_vm: ReferenceVmFragment=None, size: str=None):
        """ResourceSettingsFragment - a model defined in OpenAPI

        :param gallery_image_resource_id: The gallery_image_resource_id of this ResourceSettingsFragment.
        :param reference_vm: The reference_vm of this ResourceSettingsFragment.
        :param size: The size of this ResourceSettingsFragment.
        """
        self.openapi_types = {
            'gallery_image_resource_id': str,
            'reference_vm': ReferenceVmFragment,
            'size': str
        }

        self.attribute_map = {
            'gallery_image_resource_id': 'galleryImageResourceId',
            'reference_vm': 'referenceVm',
            'size': 'size'
        }

        self._gallery_image_resource_id = gallery_image_resource_id
        self._reference_vm = reference_vm
        self._size = size

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ResourceSettingsFragment':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ResourceSettingsFragment of this ResourceSettingsFragment.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def gallery_image_resource_id(self):
        """Gets the gallery_image_resource_id of this ResourceSettingsFragment.

        The resource id of the gallery image used for creating the virtual machine

        :return: The gallery_image_resource_id of this ResourceSettingsFragment.
        :rtype: str
        """
        return self._gallery_image_resource_id

    @gallery_image_resource_id.setter
    def gallery_image_resource_id(self, gallery_image_resource_id):
        """Sets the gallery_image_resource_id of this ResourceSettingsFragment.

        The resource id of the gallery image used for creating the virtual machine

        :param gallery_image_resource_id: The gallery_image_resource_id of this ResourceSettingsFragment.
        :type gallery_image_resource_id: str
        """

        self._gallery_image_resource_id = gallery_image_resource_id

    @property
    def reference_vm(self):
        """Gets the reference_vm of this ResourceSettingsFragment.


        :return: The reference_vm of this ResourceSettingsFragment.
        :rtype: ReferenceVmFragment
        """
        return self._reference_vm

    @reference_vm.setter
    def reference_vm(self, reference_vm):
        """Sets the reference_vm of this ResourceSettingsFragment.


        :param reference_vm: The reference_vm of this ResourceSettingsFragment.
        :type reference_vm: ReferenceVmFragment
        """

        self._reference_vm = reference_vm

    @property
    def size(self):
        """Gets the size of this ResourceSettingsFragment.

        The size of the virtual machine

        :return: The size of this ResourceSettingsFragment.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ResourceSettingsFragment.

        The size of the virtual machine

        :param size: The size of this ResourceSettingsFragment.
        :type size: str
        """
        allowed_values = ["Basic", "Standard", "Performance"]  # noqa: E501
        if size not in allowed_values:
            raise ValueError(
                "Invalid value for `size` ({0}), must be one of {1}"
                .format(size, allowed_values)
            )

        self._size = size
