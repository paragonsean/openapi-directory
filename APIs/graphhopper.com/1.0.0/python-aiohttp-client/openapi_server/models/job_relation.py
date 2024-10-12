# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class JobRelation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ids: List[str]=None, type: str=None, vehicle_id: str=None):
        """JobRelation - a model defined in OpenAPI

        :param ids: The ids of this JobRelation.
        :param type: The type of this JobRelation.
        :param vehicle_id: The vehicle_id of this JobRelation.
        """
        self.openapi_types = {
            'ids': List[str],
            'type': str,
            'vehicle_id': str
        }

        self.attribute_map = {
            'ids': 'ids',
            'type': 'type',
            'vehicle_id': 'vehicle_id'
        }

        self._ids = ids
        self._type = type
        self._vehicle_id = vehicle_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'JobRelation':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The JobRelation of this JobRelation.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ids(self):
        """Gets the ids of this JobRelation.

        Specifies an array of shipment and/or service ids that are in relation. If you deal with services then you need to use the id of your services in ids. To also consider sequences of the pickups and deliveries of your shipments, you need to use a special ID, i.e. use your shipment id plus the keyword `_pickup` or `_delivery`. If you want to place a service or shipment activity at the beginning of your route, use the special ID `start`. In turn, use `end` to place it at the end of the route.

        :return: The ids of this JobRelation.
        :rtype: List[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this JobRelation.

        Specifies an array of shipment and/or service ids that are in relation. If you deal with services then you need to use the id of your services in ids. To also consider sequences of the pickups and deliveries of your shipments, you need to use a special ID, i.e. use your shipment id plus the keyword `_pickup` or `_delivery`. If you want to place a service or shipment activity at the beginning of your route, use the special ID `start`. In turn, use `end` to place it at the end of the route.

        :param ids: The ids of this JobRelation.
        :type ids: List[str]
        """
        if ids is None:
            raise ValueError("Invalid value for `ids`, must not be `None`")

        self._ids = ids

    @property
    def type(self):
        """Gets the type of this JobRelation.

        Specifies the type of relation. It must be either of type `in_same_route`, `in_sequence` or `in_direct_sequence`.  `in_same_route`: As the name suggest, it enforces the specified services or shipments to be in the same route. It can be specified as follows:  ```json {    \"type\": \"in_same_route\",    \"ids\": [\"serv_i_id\",\"serv_j_id\"] } ```  This enforces service i to be in the same route as service j no matter which vehicle will be employed. If a specific vehicle (driver) is required to conduct this, just add a `vehicle_id` like this:  ``` {    \"type\": \"in_same_route\",    \"ids\": [\"serv_i_id\",\"serv_j_id\"],    \"vehicle_id\": \"vehicle1\" } ```  This not only enforce service i and j to be in the same route, but also makes sure that both services are in the route of `vehicle1`.  *Tip*: This way initial loads and vehicle routes can be modelled. For example, if your vehicles are already on the road and new orders come in, then vehicles can still be rescheduled subject to the orders that have already been assigned to these vehicles.    `in_sequence`: This relation type enforces n jobs to be in sequence. It can be specified as  ```json {    \"type\": \"in_sequence\",    \"ids\": [\"serv_i_id\",\"serv_j_id\"] } ```  which means that service j need to be in the same route as service i AND it needs to occur somewhere after service i. As described above if a specific vehicle needs to conduct this, just add `vehicle_id`.   `in_direct_sequence`: This enforces n services or shipments to be in direct sequence. It can be specified as  ```json {    \"type\": \"in_direct_sequence\",    \"ids\": [\"serv_i_id\",\"serv_j_id\",\"serv_k_id\"] } ```  yielding service j to occur directly after service i, and service k to occur directly after service j i.e. in strong order. Again, a vehicle can be assigned a priority by adding a `vehicle_id` to the relation.   *Special IDs*: If you look at the previous example and you want service i to be the first in the route, use the special ID `start` as follows:  ```json {    \"type\": \"in_direct_sequence\",    \"ids\": [\"start\",\"serv_i_id\",\"serv_j_id\",\"serv_k_id\"] } ```  Latter enforces the direct sequence of i, j and k at the beginning of the route. If this sequence should be bound to the end of the route, use the special ID `end` like this:  ```json {    \"type\": \"in_direct_sequence\",    \"ids\": [\"serv_i_id\",\"service_j_id\",\"serv_k_id\",\"end\"] } ```  If you deal with services then you need to use the 'id' of your services in the field 'ids'. To also consider sequences of the pickups and deliveries of your shipments, you need to use a special ID, i.e. use the shipment id plus the keyword `_pickup` or `_delivery`. For example, to ensure that the pickup and delivery of the shipment with the id 'my_shipment' are direct neighbors, you need the following specification:  ``` {    \"type\": \"in_direct_sequence\",    \"ids\": [\"my_ship_pickup\",\"my_ship_delivery\"] } ```  

        :return: The type of this JobRelation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this JobRelation.

        Specifies the type of relation. It must be either of type `in_same_route`, `in_sequence` or `in_direct_sequence`.  `in_same_route`: As the name suggest, it enforces the specified services or shipments to be in the same route. It can be specified as follows:  ```json {    \"type\": \"in_same_route\",    \"ids\": [\"serv_i_id\",\"serv_j_id\"] } ```  This enforces service i to be in the same route as service j no matter which vehicle will be employed. If a specific vehicle (driver) is required to conduct this, just add a `vehicle_id` like this:  ``` {    \"type\": \"in_same_route\",    \"ids\": [\"serv_i_id\",\"serv_j_id\"],    \"vehicle_id\": \"vehicle1\" } ```  This not only enforce service i and j to be in the same route, but also makes sure that both services are in the route of `vehicle1`.  *Tip*: This way initial loads and vehicle routes can be modelled. For example, if your vehicles are already on the road and new orders come in, then vehicles can still be rescheduled subject to the orders that have already been assigned to these vehicles.    `in_sequence`: This relation type enforces n jobs to be in sequence. It can be specified as  ```json {    \"type\": \"in_sequence\",    \"ids\": [\"serv_i_id\",\"serv_j_id\"] } ```  which means that service j need to be in the same route as service i AND it needs to occur somewhere after service i. As described above if a specific vehicle needs to conduct this, just add `vehicle_id`.   `in_direct_sequence`: This enforces n services or shipments to be in direct sequence. It can be specified as  ```json {    \"type\": \"in_direct_sequence\",    \"ids\": [\"serv_i_id\",\"serv_j_id\",\"serv_k_id\"] } ```  yielding service j to occur directly after service i, and service k to occur directly after service j i.e. in strong order. Again, a vehicle can be assigned a priority by adding a `vehicle_id` to the relation.   *Special IDs*: If you look at the previous example and you want service i to be the first in the route, use the special ID `start` as follows:  ```json {    \"type\": \"in_direct_sequence\",    \"ids\": [\"start\",\"serv_i_id\",\"serv_j_id\",\"serv_k_id\"] } ```  Latter enforces the direct sequence of i, j and k at the beginning of the route. If this sequence should be bound to the end of the route, use the special ID `end` like this:  ```json {    \"type\": \"in_direct_sequence\",    \"ids\": [\"serv_i_id\",\"service_j_id\",\"serv_k_id\",\"end\"] } ```  If you deal with services then you need to use the 'id' of your services in the field 'ids'. To also consider sequences of the pickups and deliveries of your shipments, you need to use a special ID, i.e. use the shipment id plus the keyword `_pickup` or `_delivery`. For example, to ensure that the pickup and delivery of the shipment with the id 'my_shipment' are direct neighbors, you need the following specification:  ``` {    \"type\": \"in_direct_sequence\",    \"ids\": [\"my_ship_pickup\",\"my_ship_delivery\"] } ```  

        :param type: The type of this JobRelation.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def vehicle_id(self):
        """Gets the vehicle_id of this JobRelation.

        Id of pre-assigned vehicle, i.e. the vehicle id that is determined to conduct the services and shipments in this relation.

        :return: The vehicle_id of this JobRelation.
        :rtype: str
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id):
        """Sets the vehicle_id of this JobRelation.

        Id of pre-assigned vehicle, i.e. the vehicle id that is determined to conduct the services and shipments in this relation.

        :param vehicle_id: The vehicle_id of this JobRelation.
        :type vehicle_id: str
        """

        self._vehicle_id = vehicle_id
