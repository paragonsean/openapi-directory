from typing import List, Dict
from aiohttp import web

from openapi_server.models.calculate_reachable_range_post_data_parameters import CalculateReachableRangePostDataParameters
from openapi_server.models.calculate_route_post_data_parameters import CalculateRoutePostDataParameters
from openapi_server import util


async def routing_version_number_calculate_reachable_range_origin_content_type_get(request: web.Request, version_number, origin, content_type, fuel_budget_in_liters=None, energy_budget_ink_wh=None, time_budget_in_sec=None, param_callback=None, report=None, depart_at=None, arrive_at=None, route_type=None, traffic=None, avoid=None, travel_mode=None, hilliness=None, windingness=None, vehicle_max_speed=None, vehicle_weight=None, vehicle_axle_weight=None, vehicle_length=None, vehicle_width=None, vehicle_height=None, vehicle_commercial=None, vehicle_load_type=None, constant_speed_consumption_in_liters_per_hundredkm=None, current_fuel_in_liters=None, auxiliary_power_in_liters_per_hour=None, fuel_energy_density_in_m_joules_per_liter=None, acceleration_efficiency=None, deceleration_efficiency=None, uphill_efficiency=None, downhill_efficiency=None, vehicle_engine_type=None, constant_speed_consumption_ink_wh_per_hundredkm=None) -> web.Response:
    """Reachable Range

    Calculates a set of locations that can be reached from the origin point.

    :param version_number: Service version number. The current value is 1.
    :type version_number: int
    :param origin: Point from which the range calculation should start.
    :type origin: str
    :param content_type: The content type of the response structure. If the content type is jsonp, a callback method can be specified in the query parameters.
    :type content_type: str
    :param fuel_budget_in_liters: Fuel budget in liters. Determines the maximum vehicle range using the specified Combustion Consumption Model.
    :type fuel_budget_in_liters: float
    :param energy_budget_ink_wh: Electric energy budget in kilowatt hours (kWh). Determines the maximum vehicle range using the specified Electric Consumption Model.
    :type energy_budget_ink_wh: float
    :param time_budget_in_sec: Time budget in seconds. Determines the maximum vehicle range using the specified driving time. The consumption parameters in the request will only affect eco-routes, and thereby indirectly the driving time.
    :type time_budget_in_sec: float
    :param param_callback: Specifies the jsonp callback method.
    :type param_callback: str
    :param report: Specifies which data should be reported for diagnosis purposes.
    :type report: str
    :param depart_at: The date and time of departure from the origin point. Departure times apart from &lt;i&gt;now&lt;/i&gt; must be specified as a dateTime.
    :type depart_at: str
    :param arrive_at: The date and time of arrival at the destination point. It must be specified as a dateTime.
    :type arrive_at: str
    :param route_type: The type of route requested.
    :type route_type: str
    :param traffic: Determines whether current traffic is used in route calculations. Note that information on historic road speeds is always used.
    :type traffic: bool
    :param avoid: Specifies whether the routing engine should try to avoid specific types of road segment when calculating the route. Can be specified multiple times. Possible values:   - tollRoads   - motorways   - ferries   - unpavedRoads   - carpools
    :type avoid: str
    :param travel_mode: The mode of travel for the requested route.
    :type travel_mode: str
    :param hilliness: Degree of hilliness for calculating a thrilling route.
    :type hilliness: str
    :param windingness: Amount that a thrilling route should wind.
    :type windingness: str
    :param vehicle_max_speed: Maximum speed of the vehicle in km/hour.
    :type vehicle_max_speed: int
    :param vehicle_weight: Weight of the vehicle in kilograms.
    :type vehicle_weight: int
    :param vehicle_axle_weight: Weight per axle of the vehicle in kg.
    :type vehicle_axle_weight: int
    :param vehicle_length: Length of the vehicle in meters.
    :type vehicle_length: float
    :param vehicle_width: Width of the vehicle in meters.
    :type vehicle_width: float
    :param vehicle_height: Height of the vehicle in meters.
    :type vehicle_height: float
    :param vehicle_commercial: Indicates that the vehicle is used for commercial purposes. This means it may not be allowed on certain roads.
    :type vehicle_commercial: bool
    :param vehicle_load_type: Indicates what kinds of hazardous materials the vehicle is carrying (if any). This means it may not be allowed on certain roads. Use these for routing in the US:    - &lt;i&gt;USHazmatClass1&lt;/i&gt; Explosives   - &lt;i&gt;USHazmatClass2&lt;/i&gt; Compressed gas   - &lt;i&gt;USHazmatClass3&lt;/i&gt; Flammable liquids   - &lt;i&gt;USHazmatClass4&lt;/i&gt; Flammable solids   - &lt;i&gt;USHazmatClass5&lt;/i&gt; Oxidizers   - &lt;i&gt;USHazmatClass6&lt;/i&gt; Poisons   - &lt;i&gt;USHazmatClass7&lt;/i&gt; Radioactive   - &lt;i&gt;USHazmatClass8&lt;/i&gt; Corrosives   - &lt;i&gt;USHazmatClass9&lt;/i&gt; Miscellaneous  Use these for routing in all other countries:    - &lt;i&gt;otherHazmatExplosive&lt;/i&gt; Explosives   - &lt;i&gt;otherHazmatGeneral&lt;/i&gt; Miscellaneous   - &lt;i&gt;otherHazmatHarmfulToWater&lt;/i&gt; Harmful to water  vehicleLoadType can be specified multiple times. This parameter is currently only considered for &lt;b&gt;travelMode&lt;/b&gt;&#x3D;&lt;i&gt;truck&lt;/i&gt;.
    :type vehicle_load_type: str
    :param constant_speed_consumption_in_liters_per_hundredkm: Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
    :type constant_speed_consumption_in_liters_per_hundredkm: str
    :param current_fuel_in_liters: Specifies the current supply of fuel in liters.
    :type current_fuel_in_liters: float
    :param auxiliary_power_in_liters_per_hour: Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour.
    :type auxiliary_power_in_liters_per_hour: float
    :param fuel_energy_density_in_m_joules_per_liter: Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ).
    :type fuel_energy_density_in_m_joules_per_liter: float
    :param acceleration_efficiency: Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates (i.e. KineticEnergyGained/ChemicalEnergyConsumed).
    :type acceleration_efficiency: float
    :param deceleration_efficiency: Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates (i.e. ChemicalEnergySaved/KineticEnergyLost).
    :type deceleration_efficiency: float
    :param uphill_efficiency: Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation (i.e. PotentialEnergyGained/ChemicalEnergyConsumed).
    :type uphill_efficiency: float
    :param downhill_efficiency: Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation (i.e. ChemicalEnergySaved/PotentialEnergyLost).
    :type downhill_efficiency: float
    :param vehicle_engine_type: Engine type of the vehicle.
    :type vehicle_engine_type: str
    :param constant_speed_consumption_ink_wh_per_hundredkm: Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
    :type constant_speed_consumption_ink_wh_per_hundredkm: str

    """
    return web.Response(status=200)


async def routing_version_number_calculate_reachable_range_origin_content_type_post(request: web.Request, version_number, origin, content_type, fuel_budget_in_liters=None, energy_budget_ink_wh=None, time_budget_in_sec=None, param_callback=None, report=None, depart_at=None, arrive_at=None, route_type=None, traffic=None, avoid=None, travel_mode=None, hilliness=None, windingness=None, vehicle_max_speed=None, vehicle_weight=None, vehicle_axle_weight=None, vehicle_length=None, vehicle_width=None, vehicle_height=None, vehicle_commercial=None, vehicle_load_type=None, constant_speed_consumption_in_liters_per_hundredkm=None, current_fuel_in_liters=None, auxiliary_power_in_liters_per_hour=None, fuel_energy_density_in_m_joules_per_liter=None, acceleration_efficiency=None, deceleration_efficiency=None, uphill_efficiency=None, downhill_efficiency=None, vehicle_engine_type=None, constant_speed_consumption_ink_wh_per_hundredkm=None, body=None) -> web.Response:
    """Reachable Range

    Calculates a set of locations that can be reached from the origin point. POST method handles additionally parameters: &lt;em&gt;supportingPoints&lt;/em&gt;, &lt;em&gt;allowVignette&lt;/em&gt;, &lt;em&gt;avoidVignette&lt;/em&gt;, &lt;em&gt;avoidAreas&lt;/em&gt;.

    :param version_number: Service version number. The current value is 1.
    :type version_number: int
    :param origin: Point from which the range calculation should start.
    :type origin: str
    :param content_type: The content type of the response structure. If the content type is jsonp, a callback method can be specified in the query parameters.
    :type content_type: str
    :param fuel_budget_in_liters: Fuel budget in liters. Determines the maximum vehicle range using the specified Combustion Consumption Model.
    :type fuel_budget_in_liters: float
    :param energy_budget_ink_wh: Electric energy budget in kilowatt hours (kWh). Determines the maximum vehicle range using the specified Electric Consumption Model.
    :type energy_budget_ink_wh: float
    :param time_budget_in_sec: Time budget in seconds. Determines the maximum vehicle range using the specified driving time. The consumption parameters in the request will only affect eco-routes, and thereby indirectly the driving time.
    :type time_budget_in_sec: float
    :param param_callback: Specifies the jsonp callback method.
    :type param_callback: str
    :param report: Specifies which data should be reported for diagnosis purposes.
    :type report: str
    :param depart_at: The date and time of departure from the origin point. Departure times apart from &lt;i&gt;now&lt;/i&gt; must be specified as a dateTime.
    :type depart_at: str
    :param arrive_at: The date and time of arrival at the destination point. It must be specified as a dateTime.
    :type arrive_at: str
    :param route_type: The type of route requested.
    :type route_type: str
    :param traffic: Determines whether current traffic is used in route calculations. Note that information on historic road speeds is always used.
    :type traffic: bool
    :param avoid: Specifies whether the routing engine should try to avoid specific types of road segment when calculating the route. Can be specified multiple times. Possible values:   - tollRoads   - motorways   - ferries   - unpavedRoads   - carpools
    :type avoid: str
    :param travel_mode: The mode of travel for the requested route.
    :type travel_mode: str
    :param hilliness: Degree of hilliness for calculating a thrilling route.
    :type hilliness: str
    :param windingness: Amount that a thrilling route should wind.
    :type windingness: str
    :param vehicle_max_speed: Maximum speed of the vehicle in km/hour.
    :type vehicle_max_speed: int
    :param vehicle_weight: Weight of the vehicle in kilograms.
    :type vehicle_weight: int
    :param vehicle_axle_weight: Weight per axle of the vehicle in kg.
    :type vehicle_axle_weight: int
    :param vehicle_length: Length of the vehicle in meters.
    :type vehicle_length: float
    :param vehicle_width: Width of the vehicle in meters.
    :type vehicle_width: float
    :param vehicle_height: Height of the vehicle in meters.
    :type vehicle_height: float
    :param vehicle_commercial: Indicates that the vehicle is used for commercial purposes. This means it may not be allowed on certain roads.
    :type vehicle_commercial: bool
    :param vehicle_load_type: Indicates what kinds of hazardous materials the vehicle is carrying (if any). This means it may not be allowed on certain roads. Use these for routing in the US:    - &lt;i&gt;USHazmatClass1&lt;/i&gt; Explosives   - &lt;i&gt;USHazmatClass2&lt;/i&gt; Compressed gas   - &lt;i&gt;USHazmatClass3&lt;/i&gt; Flammable liquids   - &lt;i&gt;USHazmatClass4&lt;/i&gt; Flammable solids   - &lt;i&gt;USHazmatClass5&lt;/i&gt; Oxidizers   - &lt;i&gt;USHazmatClass6&lt;/i&gt; Poisons   - &lt;i&gt;USHazmatClass7&lt;/i&gt; Radioactive   - &lt;i&gt;USHazmatClass8&lt;/i&gt; Corrosives   - &lt;i&gt;USHazmatClass9&lt;/i&gt; Miscellaneous  Use these for routing in all other countries:    - &lt;i&gt;otherHazmatExplosive&lt;/i&gt; Explosives   - &lt;i&gt;otherHazmatGeneral&lt;/i&gt; Miscellaneous   - &lt;i&gt;otherHazmatHarmfulToWater&lt;/i&gt; Harmful to water  vehicleLoadType can be specified multiple times. This parameter is currently only considered for &lt;b&gt;travelMode&lt;/b&gt;&#x3D;&lt;i&gt;truck&lt;/i&gt;.
    :type vehicle_load_type: str
    :param constant_speed_consumption_in_liters_per_hundredkm: Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
    :type constant_speed_consumption_in_liters_per_hundredkm: str
    :param current_fuel_in_liters: Specifies the current supply of fuel in liters.
    :type current_fuel_in_liters: float
    :param auxiliary_power_in_liters_per_hour: Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour.
    :type auxiliary_power_in_liters_per_hour: float
    :param fuel_energy_density_in_m_joules_per_liter: Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ).
    :type fuel_energy_density_in_m_joules_per_liter: float
    :param acceleration_efficiency: Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates (i.e. KineticEnergyGained/ChemicalEnergyConsumed).
    :type acceleration_efficiency: float
    :param deceleration_efficiency: Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates (i.e. ChemicalEnergySaved/KineticEnergyLost).
    :type deceleration_efficiency: float
    :param uphill_efficiency: Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation (i.e. PotentialEnergyGained/ChemicalEnergyConsumed).
    :type uphill_efficiency: float
    :param downhill_efficiency: Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation (i.e. ChemicalEnergySaved/PotentialEnergyLost).
    :type downhill_efficiency: float
    :param vehicle_engine_type: Engine type of the vehicle.
    :type vehicle_engine_type: str
    :param constant_speed_consumption_ink_wh_per_hundredkm: Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
    :type constant_speed_consumption_ink_wh_per_hundredkm: str
    :param body: 
    :type body: dict | bytes

    """
    body = CalculateReachableRangePostDataParameters.from_dict(body)
    return web.Response(status=200)


async def routing_version_number_calculate_route_locations_content_type_get(request: web.Request, version_number, locations, content_type, max_alternatives=None, alternative_type=None, min_deviation_distance=None, min_deviation_time=None, instructions_type=None, language=None, compute_best_order=None, route_representation=None, compute_travel_time_for=None, vehicle_heading=None, section_type=None, param_callback=None, report=None, depart_at=None, arrive_at=None, route_type=None, traffic=None, avoid=None, travel_mode=None, hilliness=None, windingness=None, vehicle_max_speed=None, vehicle_weight=None, vehicle_axle_weight=None, vehicle_length=None, vehicle_width=None, vehicle_height=None, vehicle_commercial=None, vehicle_load_type=None, vehicle_engine_type=None, constant_speed_consumption_in_liters_per_hundredkm=None, current_fuel_in_liters=None, auxiliary_power_in_liters_per_hour=None, fuel_energy_density_in_m_joules_per_liter=None, acceleration_efficiency=None, deceleration_efficiency=None, uphill_efficiency=None, downhill_efficiency=None, constant_speed_consumption_ink_wh_per_hundredkm=None) -> web.Response:
    """Calculate Route

    Calculates a route between an origin and a destination.

    :param version_number: Service version number. The current value is 1.
    :type version_number: int
    :param locations: Locations through which the calculated route must pass.
    :type locations: str
    :param content_type: The content type of the response structure. If the content type is jsonp, a callback method can be specified in the query parameters.
    :type content_type: str
    :param max_alternatives: Number of alternative routes to be calculated.
    :type max_alternatives: int
    :param alternative_type: Determines whether the alternative routes to be calculated should be better with respect to the planning criteria provided than the reference route.
    :type alternative_type: str
    :param min_deviation_distance: All alternative routes will follow the reference route for the specified minimum number of meters starting from the origin point.
    :type min_deviation_distance: int
    :param min_deviation_time: All alternative routes will follow the reference route for the specified minimum number of seconds starting from the origin point.
    :type min_deviation_time: int
    :param instructions_type: If specified, guidance instructions will be returned (if available).
    :type instructions_type: str
    :param language: The language parameter determines the language of the guidance messages.
    :type language: str
    :param compute_best_order: Re-order the route waypoints to reduce the route length.
    :type compute_best_order: bool
    :param route_representation: Specifies the representation of the set of routes provided as a response.
    :type route_representation: str
    :param compute_travel_time_for: Specifies whether to return additional travel times using different types of traffic information (none, historic, live) as well as the default best-estimate travel time.
    :type compute_travel_time_for: str
    :param vehicle_heading: The directional heading of the vehicle in degrees. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.).
    :type vehicle_heading: int
    :param section_type: Specifies which section types are explicitly reported in the route response. Can be specified multiple times.   - carTrain, ferry, tunnel or motorway   - pedestrian   - tollRoad   - tollVignette   - country   - travelMode   - traffic
    :type section_type: str
    :param param_callback: Specifies the jsonp callback method.
    :type param_callback: str
    :param report: Specifies which data should be reported for diagnosis purposes.
    :type report: str
    :param depart_at: The date and time of departure from the origin point. Departure times apart from &lt;i&gt;now&lt;/i&gt; must be specified as a dateTime.
    :type depart_at: str
    :param arrive_at: The date and time of arrival at the destination point. It must be specified as a dateTime.
    :type arrive_at: str
    :param route_type: The type of route requested.
    :type route_type: str
    :param traffic: Determines whether current traffic is used in route calculations. Note that information on historic road speeds is always used.
    :type traffic: bool
    :param avoid: Specifies whether the routing engine should try to avoid specific types of road segment when calculating the route. Can be specified multiple times. Possible values:   - tollRoads   - motorways   - ferries   - unpavedRoads   - carpools   - alreadyUsedRoads
    :type avoid: str
    :param travel_mode: The mode of travel for the requested route.
    :type travel_mode: str
    :param hilliness: Degree of hilliness for calculating a thrilling route.
    :type hilliness: str
    :param windingness: Amount that a thrilling route should wind.
    :type windingness: str
    :param vehicle_max_speed: Maximum speed of the vehicle in km/hour.
    :type vehicle_max_speed: int
    :param vehicle_weight: Weight of the vehicle in kilograms.
    :type vehicle_weight: int
    :param vehicle_axle_weight: Weight per axle of the vehicle in kg.
    :type vehicle_axle_weight: int
    :param vehicle_length: Length of the vehicle in meters.
    :type vehicle_length: float
    :param vehicle_width: Width of the vehicle in meters.
    :type vehicle_width: float
    :param vehicle_height: Height of the vehicle in meters.
    :type vehicle_height: float
    :param vehicle_commercial: Indicates that the vehicle is used for commercial purposes. This means it may not be allowed on certain roads.
    :type vehicle_commercial: bool
    :param vehicle_load_type: Indicates what kinds of hazardous materials the vehicle is carrying (if any). This means it may not be allowed on certain roads. Use these for routing in the US:    - &lt;i&gt;USHazmatClass1&lt;/i&gt; Explosives   - &lt;i&gt;USHazmatClass2&lt;/i&gt; Compressed gas   - &lt;i&gt;USHazmatClass3&lt;/i&gt; Flammable liquids   - &lt;i&gt;USHazmatClass4&lt;/i&gt; Flammable solids   - &lt;i&gt;USHazmatClass5&lt;/i&gt; Oxidizers   - &lt;i&gt;USHazmatClass6&lt;/i&gt; Poisons   - &lt;i&gt;USHazmatClass7&lt;/i&gt; Radioactive   - &lt;i&gt;USHazmatClass8&lt;/i&gt; Corrosives   - &lt;i&gt;USHazmatClass9&lt;/i&gt; Miscellaneous  Use these for routing in all other countries:    - &lt;i&gt;otherHazmatExplosive&lt;/i&gt; Explosives   - &lt;i&gt;otherHazmatGeneral&lt;/i&gt; Miscellaneous   - &lt;i&gt;otherHazmatHarmfulToWater&lt;/i&gt; Harmful to water  vehicleLoadType can be specified multiple times. This parameter is currently only considered for &lt;b&gt;travelMode&lt;/b&gt;&#x3D;&lt;i&gt;truck&lt;/i&gt;.
    :type vehicle_load_type: str
    :param vehicle_engine_type: Engine type of the vehicle.
    :type vehicle_engine_type: str
    :param constant_speed_consumption_in_liters_per_hundredkm: Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
    :type constant_speed_consumption_in_liters_per_hundredkm: str
    :param current_fuel_in_liters: Specifies the current supply of fuel in liters.
    :type current_fuel_in_liters: float
    :param auxiliary_power_in_liters_per_hour: Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour.
    :type auxiliary_power_in_liters_per_hour: float
    :param fuel_energy_density_in_m_joules_per_liter: Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ).
    :type fuel_energy_density_in_m_joules_per_liter: float
    :param acceleration_efficiency: Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates (i.e. KineticEnergyGained/ChemicalEnergyConsumed).
    :type acceleration_efficiency: float
    :param deceleration_efficiency: Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates (i.e. ChemicalEnergySaved/KineticEnergyLost).
    :type deceleration_efficiency: float
    :param uphill_efficiency: Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation (i.e. PotentialEnergyGained/ChemicalEnergyConsumed).
    :type uphill_efficiency: float
    :param downhill_efficiency: Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation (i.e. ChemicalEnergySaved/PotentialEnergyLost).
    :type downhill_efficiency: float
    :param constant_speed_consumption_ink_wh_per_hundredkm: Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
    :type constant_speed_consumption_ink_wh_per_hundredkm: str

    """
    return web.Response(status=200)


async def routing_version_number_calculate_route_locations_content_type_post(request: web.Request, version_number, locations, content_type, max_alternatives=None, alternative_type=None, min_deviation_distance=None, min_deviation_time=None, instructions_type=None, language=None, compute_best_order=None, route_representation=None, compute_travel_time_for=None, vehicle_heading=None, section_type=None, param_callback=None, report=None, depart_at=None, arrive_at=None, route_type=None, traffic=None, avoid=None, travel_mode=None, hilliness=None, windingness=None, vehicle_max_speed=None, vehicle_weight=None, vehicle_axle_weight=None, vehicle_length=None, vehicle_width=None, vehicle_height=None, vehicle_commercial=None, vehicle_load_type=None, vehicle_engine_type=None, constant_speed_consumption_in_liters_per_hundredkm=None, current_fuel_in_liters=None, auxiliary_power_in_liters_per_hour=None, fuel_energy_density_in_m_joules_per_liter=None, acceleration_efficiency=None, deceleration_efficiency=None, uphill_efficiency=None, downhill_efficiency=None, constant_speed_consumption_ink_wh_per_hundredkm=None, body=None) -> web.Response:
    """Calculate Route

    Calculates a route between an origin and a destination. POST method handles additionally parameters: &lt;em&gt;supportingPoints&lt;/em&gt;, &lt;em&gt;allowVignette&lt;/em&gt;, &lt;em&gt;avoidVignette&lt;/em&gt;, &lt;em&gt;avoidAreas&lt;/em&gt;.

    :param version_number: Service version number. The current value is 1.
    :type version_number: int
    :param locations: Locations through which the calculated route must pass.
    :type locations: str
    :param content_type: The content type of the response structure. If the content type is jsonp, a callback method can be specified in the query parameters.
    :type content_type: str
    :param max_alternatives: Number of alternative routes to be calculated.
    :type max_alternatives: int
    :param alternative_type: Determines whether the alternative routes to be calculated should be better with respect to the planning criteria provided than the reference route.
    :type alternative_type: str
    :param min_deviation_distance: All alternative routes will follow the reference route for the specified minimum number of meters starting from the origin point.
    :type min_deviation_distance: int
    :param min_deviation_time: All alternative routes will follow the reference route for the specified minimum number of seconds starting from the origin point.
    :type min_deviation_time: int
    :param instructions_type: If specified, guidance instructions will be returned (if available).
    :type instructions_type: str
    :param language: The language parameter determines the language of the guidance messages.
    :type language: str
    :param compute_best_order: Re-order the route waypoints to reduce the route length.
    :type compute_best_order: bool
    :param route_representation: Specifies the representation of the set of routes provided as a response.
    :type route_representation: str
    :param compute_travel_time_for: Specifies whether to return additional travel times using different types of traffic information (none, historic, live) as well as the default best-estimate travel time.
    :type compute_travel_time_for: str
    :param vehicle_heading: The directional heading of the vehicle in degrees. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.).
    :type vehicle_heading: int
    :param section_type: Specifies which section types are explicitly reported in the route response. Can be specified multiple times.   - carTrain, ferry, tunnel or motorway   - pedestrian   - tollRoad   - tollVignette   - country   - travelMode   - traffic
    :type section_type: str
    :param param_callback: Specifies the jsonp callback method.
    :type param_callback: str
    :param report: Specifies which data should be reported for diagnosis purposes.
    :type report: str
    :param depart_at: The date and time of departure from the origin point. Departure times apart from &lt;i&gt;now&lt;/i&gt; must be specified as a dateTime.
    :type depart_at: str
    :param arrive_at: The date and time of arrival at the destination point. It must be specified as a dateTime.
    :type arrive_at: str
    :param route_type: The type of route requested.
    :type route_type: str
    :param traffic: Determines whether current traffic is used in route calculations. Note that information on historic road speeds is always used.
    :type traffic: bool
    :param avoid: Specifies whether the routing engine should try to avoid specific types of road segment when calculating the route. Can be specified multiple times. Possible values:   - tollRoads   - motorways   - ferries   - unpavedRoads   - carpools   - alreadyUsedRoads
    :type avoid: str
    :param travel_mode: The mode of travel for the requested route.
    :type travel_mode: str
    :param hilliness: Degree of hilliness for calculating a thrilling route.
    :type hilliness: str
    :param windingness: Amount that a thrilling route should wind.
    :type windingness: str
    :param vehicle_max_speed: Maximum speed of the vehicle in km/hour.
    :type vehicle_max_speed: int
    :param vehicle_weight: Weight of the vehicle in kilograms.
    :type vehicle_weight: int
    :param vehicle_axle_weight: Weight per axle of the vehicle in kg.
    :type vehicle_axle_weight: int
    :param vehicle_length: Length of the vehicle in meters.
    :type vehicle_length: float
    :param vehicle_width: Width of the vehicle in meters.
    :type vehicle_width: float
    :param vehicle_height: Height of the vehicle in meters.
    :type vehicle_height: float
    :param vehicle_commercial: Indicates that the vehicle is used for commercial purposes. This means it may not be allowed on certain roads.
    :type vehicle_commercial: bool
    :param vehicle_load_type: Indicates what kinds of hazardous materials the vehicle is carrying (if any). This means it may not be allowed on certain roads. Use these for routing in the US:    - &lt;i&gt;USHazmatClass1&lt;/i&gt; Explosives   - &lt;i&gt;USHazmatClass2&lt;/i&gt; Compressed gas   - &lt;i&gt;USHazmatClass3&lt;/i&gt; Flammable liquids   - &lt;i&gt;USHazmatClass4&lt;/i&gt; Flammable solids   - &lt;i&gt;USHazmatClass5&lt;/i&gt; Oxidizers   - &lt;i&gt;USHazmatClass6&lt;/i&gt; Poisons   - &lt;i&gt;USHazmatClass7&lt;/i&gt; Radioactive   - &lt;i&gt;USHazmatClass8&lt;/i&gt; Corrosives   - &lt;i&gt;USHazmatClass9&lt;/i&gt; Miscellaneous  Use these for routing in all other countries:    - &lt;i&gt;otherHazmatExplosive&lt;/i&gt; Explosives   - &lt;i&gt;otherHazmatGeneral&lt;/i&gt; Miscellaneous   - &lt;i&gt;otherHazmatHarmfulToWater&lt;/i&gt; Harmful to water  vehicleLoadType can be specified multiple times. This parameter is currently only considered for &lt;b&gt;travelMode&lt;/b&gt;&#x3D;&lt;i&gt;truck&lt;/i&gt;.
    :type vehicle_load_type: str
    :param vehicle_engine_type: Engine type of the vehicle.
    :type vehicle_engine_type: str
    :param constant_speed_consumption_in_liters_per_hundredkm: Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
    :type constant_speed_consumption_in_liters_per_hundredkm: str
    :param current_fuel_in_liters: Specifies the current supply of fuel in liters.
    :type current_fuel_in_liters: float
    :param auxiliary_power_in_liters_per_hour: Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour.
    :type auxiliary_power_in_liters_per_hour: float
    :param fuel_energy_density_in_m_joules_per_liter: Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ).
    :type fuel_energy_density_in_m_joules_per_liter: float
    :param acceleration_efficiency: Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates (i.e. KineticEnergyGained/ChemicalEnergyConsumed).
    :type acceleration_efficiency: float
    :param deceleration_efficiency: Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates (i.e. ChemicalEnergySaved/KineticEnergyLost).
    :type deceleration_efficiency: float
    :param uphill_efficiency: Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation (i.e. PotentialEnergyGained/ChemicalEnergyConsumed).
    :type uphill_efficiency: float
    :param downhill_efficiency: Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation (i.e. ChemicalEnergySaved/PotentialEnergyLost).
    :type downhill_efficiency: float
    :param constant_speed_consumption_ink_wh_per_hundredkm: Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
    :type constant_speed_consumption_ink_wh_per_hundredkm: str
    :param body: 
    :type body: dict | bytes

    """
    body = CalculateRoutePostDataParameters.from_dict(body)
    return web.Response(status=200)
