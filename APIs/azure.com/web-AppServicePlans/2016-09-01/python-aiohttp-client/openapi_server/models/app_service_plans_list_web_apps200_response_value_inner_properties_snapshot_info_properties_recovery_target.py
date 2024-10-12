# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AppServicePlansListWebApps200ResponseValueInnerPropertiesSnapshotInfoPropertiesRecoveryTarget(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, location: str=None):
        """AppServicePlansListWebApps200ResponseValueInnerPropertiesSnapshotInfoPropertiesRecoveryTarget - a model defined in OpenAPI

        :param id: The id of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSnapshotInfoPropertiesRecoveryTarget.
        :param location: The location of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSnapshotInfoPropertiesRecoveryTarget.
        """
        self.openapi_types = {
            'id': str,
            'location': str
        }

        self.attribute_map = {
            'id': 'id',
            'location': 'location'
        }

        self._id = id
        self._location = location

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AppServicePlansListWebApps200ResponseValueInnerPropertiesSnapshotInfoPropertiesRecoveryTarget':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AppServicePlans_ListWebApps_200_response_value_inner_properties_snapshotInfo_properties_recoveryTarget of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSnapshotInfoPropertiesRecoveryTarget.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSnapshotInfoPropertiesRecoveryTarget.

        ARM resource ID of the target app.  /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName} for production slots and  /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slotName} for other slots.

        :return: The id of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSnapshotInfoPropertiesRecoveryTarget.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSnapshotInfoPropertiesRecoveryTarget.

        ARM resource ID of the target app.  /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName} for production slots and  /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slotName} for other slots.

        :param id: The id of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSnapshotInfoPropertiesRecoveryTarget.
        :type id: str
        """

        self._id = id

    @property
    def location(self):
        """Gets the location of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSnapshotInfoPropertiesRecoveryTarget.

        Geographical location of the target web app, e.g. SouthEastAsia, SouthCentralUS

        :return: The location of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSnapshotInfoPropertiesRecoveryTarget.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSnapshotInfoPropertiesRecoveryTarget.

        Geographical location of the target web app, e.g. SouthEastAsia, SouthCentralUS

        :param location: The location of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSnapshotInfoPropertiesRecoveryTarget.
        :type location: str
        """

        self._location = location
