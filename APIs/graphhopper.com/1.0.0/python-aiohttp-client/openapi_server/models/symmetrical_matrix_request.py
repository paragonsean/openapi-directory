# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.vehicle_profile_id import VehicleProfileId
from openapi_server import util


class SymmetricalMatrixRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, curbsides: List[str]=None, fail_fast: bool=True, out_arrays: List[str]=None, point_hints: List[str]=None, points: List[List[float]]=None, snap_preventions: List[str]=None, turn_costs: bool=False, vehicle: VehicleProfileId=None):
        """SymmetricalMatrixRequest - a model defined in OpenAPI

        :param curbsides: The curbsides of this SymmetricalMatrixRequest.
        :param fail_fast: The fail_fast of this SymmetricalMatrixRequest.
        :param out_arrays: The out_arrays of this SymmetricalMatrixRequest.
        :param point_hints: The point_hints of this SymmetricalMatrixRequest.
        :param points: The points of this SymmetricalMatrixRequest.
        :param snap_preventions: The snap_preventions of this SymmetricalMatrixRequest.
        :param turn_costs: The turn_costs of this SymmetricalMatrixRequest.
        :param vehicle: The vehicle of this SymmetricalMatrixRequest.
        """
        self.openapi_types = {
            'curbsides': List[str],
            'fail_fast': bool,
            'out_arrays': List[str],
            'point_hints': List[str],
            'points': List[List[float]],
            'snap_preventions': List[str],
            'turn_costs': bool,
            'vehicle': VehicleProfileId
        }

        self.attribute_map = {
            'curbsides': 'curbsides',
            'fail_fast': 'fail_fast',
            'out_arrays': 'out_arrays',
            'point_hints': 'point_hints',
            'points': 'points',
            'snap_preventions': 'snap_preventions',
            'turn_costs': 'turn_costs',
            'vehicle': 'vehicle'
        }

        self._curbsides = curbsides
        self._fail_fast = fail_fast
        self._out_arrays = out_arrays
        self._point_hints = point_hints
        self._points = points
        self._snap_preventions = snap_preventions
        self._turn_costs = turn_costs
        self._vehicle = vehicle

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SymmetricalMatrixRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SymmetricalMatrixRequest of this SymmetricalMatrixRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def curbsides(self):
        """Gets the curbsides of this SymmetricalMatrixRequest.

        Optional parameter. It specifies on which side a point should be relative to the driver when she leaves/arrives at a start/target/via point. You need to specify this parameter for either none or all points. Only supported for motor vehicles and OpenStreetMap.

        :return: The curbsides of this SymmetricalMatrixRequest.
        :rtype: List[str]
        """
        return self._curbsides

    @curbsides.setter
    def curbsides(self, curbsides):
        """Sets the curbsides of this SymmetricalMatrixRequest.

        Optional parameter. It specifies on which side a point should be relative to the driver when she leaves/arrives at a start/target/via point. You need to specify this parameter for either none or all points. Only supported for motor vehicles and OpenStreetMap.

        :param curbsides: The curbsides of this SymmetricalMatrixRequest.
        :type curbsides: List[str]
        """

        self._curbsides = curbsides

    @property
    def fail_fast(self):
        """Gets the fail_fast of this SymmetricalMatrixRequest.

        Specifies whether or not the matrix calculation should return with an error as soon as possible in case some points cannot be found or some points are not connected. If set to `false` the time/weight/distance matrix will be calculated for all valid points and contain the `null` value for all entries that could not be calculated. The `hint` field of the response will also contain additional information about what went wrong (see its documentation).

        :return: The fail_fast of this SymmetricalMatrixRequest.
        :rtype: bool
        """
        return self._fail_fast

    @fail_fast.setter
    def fail_fast(self, fail_fast):
        """Sets the fail_fast of this SymmetricalMatrixRequest.

        Specifies whether or not the matrix calculation should return with an error as soon as possible in case some points cannot be found or some points are not connected. If set to `false` the time/weight/distance matrix will be calculated for all valid points and contain the `null` value for all entries that could not be calculated. The `hint` field of the response will also contain additional information about what went wrong (see its documentation).

        :param fail_fast: The fail_fast of this SymmetricalMatrixRequest.
        :type fail_fast: bool
        """

        self._fail_fast = fail_fast

    @property
    def out_arrays(self):
        """Gets the out_arrays of this SymmetricalMatrixRequest.

        Specifies which matrices should be included in the response. Specify one or more of the following options `weights`, `times`, `distances`. The units of the entries of `distances` are meters, of `times` are seconds and of `weights` is arbitrary and it can differ for different vehicles or versions of this API.

        :return: The out_arrays of this SymmetricalMatrixRequest.
        :rtype: List[str]
        """
        return self._out_arrays

    @out_arrays.setter
    def out_arrays(self, out_arrays):
        """Sets the out_arrays of this SymmetricalMatrixRequest.

        Specifies which matrices should be included in the response. Specify one or more of the following options `weights`, `times`, `distances`. The units of the entries of `distances` are meters, of `times` are seconds and of `weights` is arbitrary and it can differ for different vehicles or versions of this API.

        :param out_arrays: The out_arrays of this SymmetricalMatrixRequest.
        :type out_arrays: List[str]
        """

        self._out_arrays = out_arrays

    @property
    def point_hints(self):
        """Gets the point_hints of this SymmetricalMatrixRequest.

        Optional parameter. Specifies a hint for each point in the `points` array to prefer a certain street for the closest location lookup. E.g. if there is an address or house with two or more neighboring streets you can control for which street the closest location is looked up.

        :return: The point_hints of this SymmetricalMatrixRequest.
        :rtype: List[str]
        """
        return self._point_hints

    @point_hints.setter
    def point_hints(self, point_hints):
        """Sets the point_hints of this SymmetricalMatrixRequest.

        Optional parameter. Specifies a hint for each point in the `points` array to prefer a certain street for the closest location lookup. E.g. if there is an address or house with two or more neighboring streets you can control for which street the closest location is looked up.

        :param point_hints: The point_hints of this SymmetricalMatrixRequest.
        :type point_hints: List[str]
        """

        self._point_hints = point_hints

    @property
    def points(self):
        """Gets the points of this SymmetricalMatrixRequest.

        Specify multiple points for which the weight-, route-, time- or distance-matrix should be calculated as follows: `[longitude,latitude]`. In this case the origins are identical to the destinations. Thus, if there are N points, NxN entries are calculated. The order of the point parameter is important. Specify at least three points. Cannot be used together with `from_point` or `to_point.`.

        :return: The points of this SymmetricalMatrixRequest.
        :rtype: List[List[float]]
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this SymmetricalMatrixRequest.

        Specify multiple points for which the weight-, route-, time- or distance-matrix should be calculated as follows: `[longitude,latitude]`. In this case the origins are identical to the destinations. Thus, if there are N points, NxN entries are calculated. The order of the point parameter is important. Specify at least three points. Cannot be used together with `from_point` or `to_point.`.

        :param points: The points of this SymmetricalMatrixRequest.
        :type points: List[List[float]]
        """

        self._points = points

    @property
    def snap_preventions(self):
        """Gets the snap_preventions of this SymmetricalMatrixRequest.

        Optional parameter to avoid snapping to a certain road class or road environment. Current supported values `motorway`, `trunk`, `ferry`, `tunnel`, `bridge` and `ford`

        :return: The snap_preventions of this SymmetricalMatrixRequest.
        :rtype: List[str]
        """
        return self._snap_preventions

    @snap_preventions.setter
    def snap_preventions(self, snap_preventions):
        """Sets the snap_preventions of this SymmetricalMatrixRequest.

        Optional parameter to avoid snapping to a certain road class or road environment. Current supported values `motorway`, `trunk`, `ferry`, `tunnel`, `bridge` and `ford`

        :param snap_preventions: The snap_preventions of this SymmetricalMatrixRequest.
        :type snap_preventions: List[str]
        """

        self._snap_preventions = snap_preventions

    @property
    def turn_costs(self):
        """Gets the turn_costs of this SymmetricalMatrixRequest.

        Specifies if turn restrictions should be considered. Enabling this option increases the matrix computation time. Only supported for motor vehicles and OpenStreetMap.

        :return: The turn_costs of this SymmetricalMatrixRequest.
        :rtype: bool
        """
        return self._turn_costs

    @turn_costs.setter
    def turn_costs(self, turn_costs):
        """Sets the turn_costs of this SymmetricalMatrixRequest.

        Specifies if turn restrictions should be considered. Enabling this option increases the matrix computation time. Only supported for motor vehicles and OpenStreetMap.

        :param turn_costs: The turn_costs of this SymmetricalMatrixRequest.
        :type turn_costs: bool
        """

        self._turn_costs = turn_costs

    @property
    def vehicle(self):
        """Gets the vehicle of this SymmetricalMatrixRequest.


        :return: The vehicle of this SymmetricalMatrixRequest.
        :rtype: VehicleProfileId
        """
        return self._vehicle

    @vehicle.setter
    def vehicle(self, vehicle):
        """Sets the vehicle of this SymmetricalMatrixRequest.


        :param vehicle: The vehicle of this SymmetricalMatrixRequest.
        :type vehicle: VehicleProfileId
        """

        self._vehicle = vehicle
