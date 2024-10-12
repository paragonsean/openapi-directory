# Routing.RoutingApi

All URIs are relative to *https://api.tomtom.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**routingVersionNumberCalculateReachableRangeOriginContentTypeGet**](RoutingApi.md#routingVersionNumberCalculateReachableRangeOriginContentTypeGet) | **GET** /routing/{versionNumber}/calculateReachableRange/{origin}/{contentType} | Reachable Range
[**routingVersionNumberCalculateReachableRangeOriginContentTypePost**](RoutingApi.md#routingVersionNumberCalculateReachableRangeOriginContentTypePost) | **POST** /routing/{versionNumber}/calculateReachableRange/{origin}/{contentType} | Reachable Range
[**routingVersionNumberCalculateRouteLocationsContentTypeGet**](RoutingApi.md#routingVersionNumberCalculateRouteLocationsContentTypeGet) | **GET** /routing/{versionNumber}/calculateRoute/{locations}/{contentType} | Calculate Route
[**routingVersionNumberCalculateRouteLocationsContentTypePost**](RoutingApi.md#routingVersionNumberCalculateRouteLocationsContentTypePost) | **POST** /routing/{versionNumber}/calculateRoute/{locations}/{contentType} | Calculate Route



## routingVersionNumberCalculateReachableRangeOriginContentTypeGet

> routingVersionNumberCalculateReachableRangeOriginContentTypeGet(versionNumber, origin, contentType, opts)

Reachable Range

Calculates a set of locations that can be reached from the origin point.

### Example

```javascript
import Routing from 'routing';
let defaultClient = Routing.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Routing.RoutingApi();
let versionNumber = 56; // Number | Service version number. The current value is 1.
let origin = "52.50931,13.42936"; // String | Point from which the range calculation should start.
let contentType = "'xml'"; // String | The content type of the response structure. If the content type is jsonp, a callback method can be specified in the query parameters.
let opts = {
  'fuelBudgetInLiters': 3.4, // Number | Fuel budget in liters. Determines the maximum vehicle range using the specified Combustion Consumption Model.
  'energyBudgetInkWh': 43, // Number | Electric energy budget in kilowatt hours (kWh). Determines the maximum vehicle range using the specified Electric Consumption Model.
  'timeBudgetInSec': 3.4, // Number | Time budget in seconds. Determines the maximum vehicle range using the specified driving time. The consumption parameters in the request will only affect eco-routes, and thereby indirectly the driving time.
  'callback': "'callback'", // String | Specifies the jsonp callback method.
  'report': "report_example", // String | Specifies which data should be reported for diagnosis purposes.
  'departAt': "'now'", // String | The date and time of departure from the origin point. Departure times apart from <i>now</i> must be specified as a dateTime.
  'arriveAt': "arriveAt_example", // String | The date and time of arrival at the destination point. It must be specified as a dateTime.
  'routeType': "'fastest'", // String | The type of route requested.
  'traffic': true, // Boolean | Determines whether current traffic is used in route calculations. Note that information on historic road speeds is always used.
  'avoid': "unpavedRoads", // String | Specifies whether the routing engine should try to avoid specific types of road segment when calculating the route. Can be specified multiple times. Possible values:   - tollRoads   - motorways   - ferries   - unpavedRoads   - carpools
  'travelMode': "'car'", // String | The mode of travel for the requested route.
  'hilliness': "'normal'", // String | Degree of hilliness for calculating a thrilling route.
  'windingness': "'normal'", // String | Amount that a thrilling route should wind.
  'vehicleMaxSpeed': 0, // Number | Maximum speed of the vehicle in km/hour.
  'vehicleWeight': 0, // Number | Weight of the vehicle in kilograms.
  'vehicleAxleWeight': 0, // Number | Weight per axle of the vehicle in kg.
  'vehicleLength': 0, // Number | Length of the vehicle in meters.
  'vehicleWidth': 0, // Number | Width of the vehicle in meters.
  'vehicleHeight': 0, // Number | Height of the vehicle in meters.
  'vehicleCommercial': false, // Boolean | Indicates that the vehicle is used for commercial purposes. This means it may not be allowed on certain roads.
  'vehicleLoadType': "vehicleLoadType_example", // String | Indicates what kinds of hazardous materials the vehicle is carrying (if any). This means it may not be allowed on certain roads. Use these for routing in the US:    - <i>USHazmatClass1</i> Explosives   - <i>USHazmatClass2</i> Compressed gas   - <i>USHazmatClass3</i> Flammable liquids   - <i>USHazmatClass4</i> Flammable solids   - <i>USHazmatClass5</i> Oxidizers   - <i>USHazmatClass6</i> Poisons   - <i>USHazmatClass7</i> Radioactive   - <i>USHazmatClass8</i> Corrosives   - <i>USHazmatClass9</i> Miscellaneous  Use these for routing in all other countries:    - <i>otherHazmatExplosive</i> Explosives   - <i>otherHazmatGeneral</i> Miscellaneous   - <i>otherHazmatHarmfulToWater</i> Harmful to water  vehicleLoadType can be specified multiple times. This parameter is currently only considered for <b>travelMode</b>=<i>truck</i>.
  'constantSpeedConsumptionInLitersPerHundredkm': "constantSpeedConsumptionInLitersPerHundredkm_example", // String | Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
  'currentFuelInLiters': 3.4, // Number | Specifies the current supply of fuel in liters.
  'auxiliaryPowerInLitersPerHour': 3.4, // Number | Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour.
  'fuelEnergyDensityInMJoulesPerLiter': 3.4, // Number | Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ).
  'accelerationEfficiency': 3.4, // Number | Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates (i.e. KineticEnergyGained/ChemicalEnergyConsumed).
  'decelerationEfficiency': 3.4, // Number | Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates (i.e. ChemicalEnergySaved/KineticEnergyLost).
  'uphillEfficiency': 3.4, // Number | Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation (i.e. PotentialEnergyGained/ChemicalEnergyConsumed).
  'downhillEfficiency': 3.4, // Number | Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation (i.e. ChemicalEnergySaved/PotentialEnergyLost).
  'vehicleEngineType': "electric", // String | Engine type of the vehicle.
  'constantSpeedConsumptionInkWhPerHundredkm': "50,8.2:130,21.3" // String | Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
};
apiInstance.routingVersionNumberCalculateReachableRangeOriginContentTypeGet(versionNumber, origin, contentType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionNumber** | **Number**| Service version number. The current value is 1. | 
 **origin** | **String**| Point from which the range calculation should start. | 
 **contentType** | **String**| The content type of the response structure. If the content type is jsonp, a callback method can be specified in the query parameters. | [default to &#39;xml&#39;]
 **fuelBudgetInLiters** | **Number**| Fuel budget in liters. Determines the maximum vehicle range using the specified Combustion Consumption Model. | [optional] 
 **energyBudgetInkWh** | **Number**| Electric energy budget in kilowatt hours (kWh). Determines the maximum vehicle range using the specified Electric Consumption Model. | [optional] 
 **timeBudgetInSec** | **Number**| Time budget in seconds. Determines the maximum vehicle range using the specified driving time. The consumption parameters in the request will only affect eco-routes, and thereby indirectly the driving time. | [optional] 
 **callback** | **String**| Specifies the jsonp callback method. | [optional] [default to &#39;callback&#39;]
 **report** | **String**| Specifies which data should be reported for diagnosis purposes. | [optional] 
 **departAt** | **String**| The date and time of departure from the origin point. Departure times apart from &lt;i&gt;now&lt;/i&gt; must be specified as a dateTime. | [optional] [default to &#39;now&#39;]
 **arriveAt** | **String**| The date and time of arrival at the destination point. It must be specified as a dateTime. | [optional] 
 **routeType** | **String**| The type of route requested. | [optional] [default to &#39;fastest&#39;]
 **traffic** | **Boolean**| Determines whether current traffic is used in route calculations. Note that information on historic road speeds is always used. | [optional] [default to true]
 **avoid** | **String**| Specifies whether the routing engine should try to avoid specific types of road segment when calculating the route. Can be specified multiple times. Possible values:   - tollRoads   - motorways   - ferries   - unpavedRoads   - carpools | [optional] 
 **travelMode** | **String**| The mode of travel for the requested route. | [optional] [default to &#39;car&#39;]
 **hilliness** | **String**| Degree of hilliness for calculating a thrilling route. | [optional] [default to &#39;normal&#39;]
 **windingness** | **String**| Amount that a thrilling route should wind. | [optional] [default to &#39;normal&#39;]
 **vehicleMaxSpeed** | **Number**| Maximum speed of the vehicle in km/hour. | [optional] [default to 0]
 **vehicleWeight** | **Number**| Weight of the vehicle in kilograms. | [optional] [default to 0]
 **vehicleAxleWeight** | **Number**| Weight per axle of the vehicle in kg. | [optional] [default to 0]
 **vehicleLength** | **Number**| Length of the vehicle in meters. | [optional] [default to 0]
 **vehicleWidth** | **Number**| Width of the vehicle in meters. | [optional] [default to 0]
 **vehicleHeight** | **Number**| Height of the vehicle in meters. | [optional] [default to 0]
 **vehicleCommercial** | **Boolean**| Indicates that the vehicle is used for commercial purposes. This means it may not be allowed on certain roads. | [optional] [default to false]
 **vehicleLoadType** | **String**| Indicates what kinds of hazardous materials the vehicle is carrying (if any). This means it may not be allowed on certain roads. Use these for routing in the US:    - &lt;i&gt;USHazmatClass1&lt;/i&gt; Explosives   - &lt;i&gt;USHazmatClass2&lt;/i&gt; Compressed gas   - &lt;i&gt;USHazmatClass3&lt;/i&gt; Flammable liquids   - &lt;i&gt;USHazmatClass4&lt;/i&gt; Flammable solids   - &lt;i&gt;USHazmatClass5&lt;/i&gt; Oxidizers   - &lt;i&gt;USHazmatClass6&lt;/i&gt; Poisons   - &lt;i&gt;USHazmatClass7&lt;/i&gt; Radioactive   - &lt;i&gt;USHazmatClass8&lt;/i&gt; Corrosives   - &lt;i&gt;USHazmatClass9&lt;/i&gt; Miscellaneous  Use these for routing in all other countries:    - &lt;i&gt;otherHazmatExplosive&lt;/i&gt; Explosives   - &lt;i&gt;otherHazmatGeneral&lt;/i&gt; Miscellaneous   - &lt;i&gt;otherHazmatHarmfulToWater&lt;/i&gt; Harmful to water  vehicleLoadType can be specified multiple times. This parameter is currently only considered for &lt;b&gt;travelMode&lt;/b&gt;&#x3D;&lt;i&gt;truck&lt;/i&gt;. | [optional] 
 **constantSpeedConsumptionInLitersPerHundredkm** | **String**| Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs. | [optional] 
 **currentFuelInLiters** | **Number**| Specifies the current supply of fuel in liters. | [optional] 
 **auxiliaryPowerInLitersPerHour** | **Number**| Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour. | [optional] 
 **fuelEnergyDensityInMJoulesPerLiter** | **Number**| Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ). | [optional] 
 **accelerationEfficiency** | **Number**| Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates (i.e. KineticEnergyGained/ChemicalEnergyConsumed). | [optional] 
 **decelerationEfficiency** | **Number**| Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates (i.e. ChemicalEnergySaved/KineticEnergyLost). | [optional] 
 **uphillEfficiency** | **Number**| Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation (i.e. PotentialEnergyGained/ChemicalEnergyConsumed). | [optional] 
 **downhillEfficiency** | **Number**| Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation (i.e. ChemicalEnergySaved/PotentialEnergyLost). | [optional] 
 **vehicleEngineType** | **String**| Engine type of the vehicle. | [optional] [default to &#39;combustion&#39;]
 **constantSpeedConsumptionInkWhPerHundredkm** | **String**| Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs. | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## routingVersionNumberCalculateReachableRangeOriginContentTypePost

> routingVersionNumberCalculateReachableRangeOriginContentTypePost(versionNumber, origin, contentType, opts)

Reachable Range

Calculates a set of locations that can be reached from the origin point. POST method handles additionally parameters: &lt;em&gt;supportingPoints&lt;/em&gt;, &lt;em&gt;allowVignette&lt;/em&gt;, &lt;em&gt;avoidVignette&lt;/em&gt;, &lt;em&gt;avoidAreas&lt;/em&gt;.

### Example

```javascript
import Routing from 'routing';
let defaultClient = Routing.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Routing.RoutingApi();
let versionNumber = 56; // Number | Service version number. The current value is 1.
let origin = "52.50931,13.42936"; // String | Point from which the range calculation should start.
let contentType = "'xml'"; // String | The content type of the response structure. If the content type is jsonp, a callback method can be specified in the query parameters.
let opts = {
  'fuelBudgetInLiters': 3.4, // Number | Fuel budget in liters. Determines the maximum vehicle range using the specified Combustion Consumption Model.
  'energyBudgetInkWh': 43, // Number | Electric energy budget in kilowatt hours (kWh). Determines the maximum vehicle range using the specified Electric Consumption Model.
  'timeBudgetInSec': 3.4, // Number | Time budget in seconds. Determines the maximum vehicle range using the specified driving time. The consumption parameters in the request will only affect eco-routes, and thereby indirectly the driving time.
  'callback': "'callback'", // String | Specifies the jsonp callback method.
  'report': "report_example", // String | Specifies which data should be reported for diagnosis purposes.
  'departAt': "'now'", // String | The date and time of departure from the origin point. Departure times apart from <i>now</i> must be specified as a dateTime.
  'arriveAt': "arriveAt_example", // String | The date and time of arrival at the destination point. It must be specified as a dateTime.
  'routeType': "'fastest'", // String | The type of route requested.
  'traffic': true, // Boolean | Determines whether current traffic is used in route calculations. Note that information on historic road speeds is always used.
  'avoid': "unpavedRoads", // String | Specifies whether the routing engine should try to avoid specific types of road segment when calculating the route. Can be specified multiple times. Possible values:   - tollRoads   - motorways   - ferries   - unpavedRoads   - carpools
  'travelMode': "'car'", // String | The mode of travel for the requested route.
  'hilliness': "'normal'", // String | Degree of hilliness for calculating a thrilling route.
  'windingness': "'normal'", // String | Amount that a thrilling route should wind.
  'vehicleMaxSpeed': 0, // Number | Maximum speed of the vehicle in km/hour.
  'vehicleWeight': 0, // Number | Weight of the vehicle in kilograms.
  'vehicleAxleWeight': 0, // Number | Weight per axle of the vehicle in kg.
  'vehicleLength': 0, // Number | Length of the vehicle in meters.
  'vehicleWidth': 0, // Number | Width of the vehicle in meters.
  'vehicleHeight': 0, // Number | Height of the vehicle in meters.
  'vehicleCommercial': false, // Boolean | Indicates that the vehicle is used for commercial purposes. This means it may not be allowed on certain roads.
  'vehicleLoadType': "vehicleLoadType_example", // String | Indicates what kinds of hazardous materials the vehicle is carrying (if any). This means it may not be allowed on certain roads. Use these for routing in the US:    - <i>USHazmatClass1</i> Explosives   - <i>USHazmatClass2</i> Compressed gas   - <i>USHazmatClass3</i> Flammable liquids   - <i>USHazmatClass4</i> Flammable solids   - <i>USHazmatClass5</i> Oxidizers   - <i>USHazmatClass6</i> Poisons   - <i>USHazmatClass7</i> Radioactive   - <i>USHazmatClass8</i> Corrosives   - <i>USHazmatClass9</i> Miscellaneous  Use these for routing in all other countries:    - <i>otherHazmatExplosive</i> Explosives   - <i>otherHazmatGeneral</i> Miscellaneous   - <i>otherHazmatHarmfulToWater</i> Harmful to water  vehicleLoadType can be specified multiple times. This parameter is currently only considered for <b>travelMode</b>=<i>truck</i>.
  'constantSpeedConsumptionInLitersPerHundredkm': "constantSpeedConsumptionInLitersPerHundredkm_example", // String | Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
  'currentFuelInLiters': 3.4, // Number | Specifies the current supply of fuel in liters.
  'auxiliaryPowerInLitersPerHour': 3.4, // Number | Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour.
  'fuelEnergyDensityInMJoulesPerLiter': 3.4, // Number | Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ).
  'accelerationEfficiency': 3.4, // Number | Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates (i.e. KineticEnergyGained/ChemicalEnergyConsumed).
  'decelerationEfficiency': 3.4, // Number | Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates (i.e. ChemicalEnergySaved/KineticEnergyLost).
  'uphillEfficiency': 3.4, // Number | Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation (i.e. PotentialEnergyGained/ChemicalEnergyConsumed).
  'downhillEfficiency': 3.4, // Number | Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation (i.e. ChemicalEnergySaved/PotentialEnergyLost).
  'vehicleEngineType': "electric", // String | Engine type of the vehicle.
  'constantSpeedConsumptionInkWhPerHundredkm': "50,8.2:130,21.3", // String | Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
  'calculateReachableRangePostDataParameters': new Routing.CalculateReachableRangePostDataParameters() // CalculateReachableRangePostDataParameters | 
};
apiInstance.routingVersionNumberCalculateReachableRangeOriginContentTypePost(versionNumber, origin, contentType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionNumber** | **Number**| Service version number. The current value is 1. | 
 **origin** | **String**| Point from which the range calculation should start. | 
 **contentType** | **String**| The content type of the response structure. If the content type is jsonp, a callback method can be specified in the query parameters. | [default to &#39;xml&#39;]
 **fuelBudgetInLiters** | **Number**| Fuel budget in liters. Determines the maximum vehicle range using the specified Combustion Consumption Model. | [optional] 
 **energyBudgetInkWh** | **Number**| Electric energy budget in kilowatt hours (kWh). Determines the maximum vehicle range using the specified Electric Consumption Model. | [optional] 
 **timeBudgetInSec** | **Number**| Time budget in seconds. Determines the maximum vehicle range using the specified driving time. The consumption parameters in the request will only affect eco-routes, and thereby indirectly the driving time. | [optional] 
 **callback** | **String**| Specifies the jsonp callback method. | [optional] [default to &#39;callback&#39;]
 **report** | **String**| Specifies which data should be reported for diagnosis purposes. | [optional] 
 **departAt** | **String**| The date and time of departure from the origin point. Departure times apart from &lt;i&gt;now&lt;/i&gt; must be specified as a dateTime. | [optional] [default to &#39;now&#39;]
 **arriveAt** | **String**| The date and time of arrival at the destination point. It must be specified as a dateTime. | [optional] 
 **routeType** | **String**| The type of route requested. | [optional] [default to &#39;fastest&#39;]
 **traffic** | **Boolean**| Determines whether current traffic is used in route calculations. Note that information on historic road speeds is always used. | [optional] [default to true]
 **avoid** | **String**| Specifies whether the routing engine should try to avoid specific types of road segment when calculating the route. Can be specified multiple times. Possible values:   - tollRoads   - motorways   - ferries   - unpavedRoads   - carpools | [optional] 
 **travelMode** | **String**| The mode of travel for the requested route. | [optional] [default to &#39;car&#39;]
 **hilliness** | **String**| Degree of hilliness for calculating a thrilling route. | [optional] [default to &#39;normal&#39;]
 **windingness** | **String**| Amount that a thrilling route should wind. | [optional] [default to &#39;normal&#39;]
 **vehicleMaxSpeed** | **Number**| Maximum speed of the vehicle in km/hour. | [optional] [default to 0]
 **vehicleWeight** | **Number**| Weight of the vehicle in kilograms. | [optional] [default to 0]
 **vehicleAxleWeight** | **Number**| Weight per axle of the vehicle in kg. | [optional] [default to 0]
 **vehicleLength** | **Number**| Length of the vehicle in meters. | [optional] [default to 0]
 **vehicleWidth** | **Number**| Width of the vehicle in meters. | [optional] [default to 0]
 **vehicleHeight** | **Number**| Height of the vehicle in meters. | [optional] [default to 0]
 **vehicleCommercial** | **Boolean**| Indicates that the vehicle is used for commercial purposes. This means it may not be allowed on certain roads. | [optional] [default to false]
 **vehicleLoadType** | **String**| Indicates what kinds of hazardous materials the vehicle is carrying (if any). This means it may not be allowed on certain roads. Use these for routing in the US:    - &lt;i&gt;USHazmatClass1&lt;/i&gt; Explosives   - &lt;i&gt;USHazmatClass2&lt;/i&gt; Compressed gas   - &lt;i&gt;USHazmatClass3&lt;/i&gt; Flammable liquids   - &lt;i&gt;USHazmatClass4&lt;/i&gt; Flammable solids   - &lt;i&gt;USHazmatClass5&lt;/i&gt; Oxidizers   - &lt;i&gt;USHazmatClass6&lt;/i&gt; Poisons   - &lt;i&gt;USHazmatClass7&lt;/i&gt; Radioactive   - &lt;i&gt;USHazmatClass8&lt;/i&gt; Corrosives   - &lt;i&gt;USHazmatClass9&lt;/i&gt; Miscellaneous  Use these for routing in all other countries:    - &lt;i&gt;otherHazmatExplosive&lt;/i&gt; Explosives   - &lt;i&gt;otherHazmatGeneral&lt;/i&gt; Miscellaneous   - &lt;i&gt;otherHazmatHarmfulToWater&lt;/i&gt; Harmful to water  vehicleLoadType can be specified multiple times. This parameter is currently only considered for &lt;b&gt;travelMode&lt;/b&gt;&#x3D;&lt;i&gt;truck&lt;/i&gt;. | [optional] 
 **constantSpeedConsumptionInLitersPerHundredkm** | **String**| Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs. | [optional] 
 **currentFuelInLiters** | **Number**| Specifies the current supply of fuel in liters. | [optional] 
 **auxiliaryPowerInLitersPerHour** | **Number**| Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour. | [optional] 
 **fuelEnergyDensityInMJoulesPerLiter** | **Number**| Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ). | [optional] 
 **accelerationEfficiency** | **Number**| Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates (i.e. KineticEnergyGained/ChemicalEnergyConsumed). | [optional] 
 **decelerationEfficiency** | **Number**| Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates (i.e. ChemicalEnergySaved/KineticEnergyLost). | [optional] 
 **uphillEfficiency** | **Number**| Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation (i.e. PotentialEnergyGained/ChemicalEnergyConsumed). | [optional] 
 **downhillEfficiency** | **Number**| Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation (i.e. ChemicalEnergySaved/PotentialEnergyLost). | [optional] 
 **vehicleEngineType** | **String**| Engine type of the vehicle. | [optional] [default to &#39;combustion&#39;]
 **constantSpeedConsumptionInkWhPerHundredkm** | **String**| Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs. | [optional] 
 **calculateReachableRangePostDataParameters** | [**CalculateReachableRangePostDataParameters**](CalculateReachableRangePostDataParameters.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: Not defined


## routingVersionNumberCalculateRouteLocationsContentTypeGet

> routingVersionNumberCalculateRouteLocationsContentTypeGet(versionNumber, locations, contentType, opts)

Calculate Route

Calculates a route between an origin and a destination.

### Example

```javascript
import Routing from 'routing';
let defaultClient = Routing.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Routing.RoutingApi();
let versionNumber = 56; // Number | Service version number. The current value is 1.
let locations = "52.50931,13.42936:52.50274,13.43872"; // String | Locations through which the calculated route must pass.
let contentType = "'xml'"; // String | The content type of the response structure. If the content type is jsonp, a callback method can be specified in the query parameters.
let opts = {
  'maxAlternatives': 0, // Number | Number of alternative routes to be calculated.
  'alternativeType': "'anyRoute'", // String | Determines whether the alternative routes to be calculated should be better with respect to the planning criteria provided than the reference route.
  'minDeviationDistance': 0, // Number | All alternative routes will follow the reference route for the specified minimum number of meters starting from the origin point.
  'minDeviationTime': 0, // Number | All alternative routes will follow the reference route for the specified minimum number of seconds starting from the origin point.
  'instructionsType': "instructionsType_example", // String | If specified, guidance instructions will be returned (if available).
  'language': "'en-GB'", // String | The language parameter determines the language of the guidance messages.
  'computeBestOrder': false, // Boolean | Re-order the route waypoints to reduce the route length.
  'routeRepresentation': "'polyline'", // String | Specifies the representation of the set of routes provided as a response.
  'computeTravelTimeFor': "'none'", // String | Specifies whether to return additional travel times using different types of traffic information (none, historic, live) as well as the default best-estimate travel time.
  'vehicleHeading': 56, // Number | The directional heading of the vehicle in degrees. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.).
  'sectionType': "'travelMode'", // String | Specifies which section types are explicitly reported in the route response. Can be specified multiple times.   - carTrain, ferry, tunnel or motorway   - pedestrian   - tollRoad   - tollVignette   - country   - travelMode   - traffic
  'callback': "'callback'", // String | Specifies the jsonp callback method.
  'report': "report_example", // String | Specifies which data should be reported for diagnosis purposes.
  'departAt': "'now'", // String | The date and time of departure from the origin point. Departure times apart from <i>now</i> must be specified as a dateTime.
  'arriveAt': "arriveAt_example", // String | The date and time of arrival at the destination point. It must be specified as a dateTime.
  'routeType': "'fastest'", // String | The type of route requested.
  'traffic': true, // Boolean | Determines whether current traffic is used in route calculations. Note that information on historic road speeds is always used.
  'avoid': "unpavedRoads", // String | Specifies whether the routing engine should try to avoid specific types of road segment when calculating the route. Can be specified multiple times. Possible values:   - tollRoads   - motorways   - ferries   - unpavedRoads   - carpools   - alreadyUsedRoads
  'travelMode': "'car'", // String | The mode of travel for the requested route.
  'hilliness': "'normal'", // String | Degree of hilliness for calculating a thrilling route.
  'windingness': "'normal'", // String | Amount that a thrilling route should wind.
  'vehicleMaxSpeed': 0, // Number | Maximum speed of the vehicle in km/hour.
  'vehicleWeight': 0, // Number | Weight of the vehicle in kilograms.
  'vehicleAxleWeight': 0, // Number | Weight per axle of the vehicle in kg.
  'vehicleLength': 0, // Number | Length of the vehicle in meters.
  'vehicleWidth': 0, // Number | Width of the vehicle in meters.
  'vehicleHeight': 0, // Number | Height of the vehicle in meters.
  'vehicleCommercial': false, // Boolean | Indicates that the vehicle is used for commercial purposes. This means it may not be allowed on certain roads.
  'vehicleLoadType': "vehicleLoadType_example", // String | Indicates what kinds of hazardous materials the vehicle is carrying (if any). This means it may not be allowed on certain roads. Use these for routing in the US:    - <i>USHazmatClass1</i> Explosives   - <i>USHazmatClass2</i> Compressed gas   - <i>USHazmatClass3</i> Flammable liquids   - <i>USHazmatClass4</i> Flammable solids   - <i>USHazmatClass5</i> Oxidizers   - <i>USHazmatClass6</i> Poisons   - <i>USHazmatClass7</i> Radioactive   - <i>USHazmatClass8</i> Corrosives   - <i>USHazmatClass9</i> Miscellaneous  Use these for routing in all other countries:    - <i>otherHazmatExplosive</i> Explosives   - <i>otherHazmatGeneral</i> Miscellaneous   - <i>otherHazmatHarmfulToWater</i> Harmful to water  vehicleLoadType can be specified multiple times. This parameter is currently only considered for <b>travelMode</b>=<i>truck</i>.
  'vehicleEngineType': "'combustion'", // String | Engine type of the vehicle.
  'constantSpeedConsumptionInLitersPerHundredkm': "constantSpeedConsumptionInLitersPerHundredkm_example", // String | Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
  'currentFuelInLiters': 3.4, // Number | Specifies the current supply of fuel in liters.
  'auxiliaryPowerInLitersPerHour': 3.4, // Number | Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour.
  'fuelEnergyDensityInMJoulesPerLiter': 3.4, // Number | Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ).
  'accelerationEfficiency': 3.4, // Number | Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates (i.e. KineticEnergyGained/ChemicalEnergyConsumed).
  'decelerationEfficiency': 3.4, // Number | Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates (i.e. ChemicalEnergySaved/KineticEnergyLost).
  'uphillEfficiency': 3.4, // Number | Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation (i.e. PotentialEnergyGained/ChemicalEnergyConsumed).
  'downhillEfficiency': 3.4, // Number | Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation (i.e. ChemicalEnergySaved/PotentialEnergyLost).
  'constantSpeedConsumptionInkWhPerHundredkm': "constantSpeedConsumptionInkWhPerHundredkm_example" // String | Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
};
apiInstance.routingVersionNumberCalculateRouteLocationsContentTypeGet(versionNumber, locations, contentType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionNumber** | **Number**| Service version number. The current value is 1. | 
 **locations** | **String**| Locations through which the calculated route must pass. | 
 **contentType** | **String**| The content type of the response structure. If the content type is jsonp, a callback method can be specified in the query parameters. | [default to &#39;xml&#39;]
 **maxAlternatives** | **Number**| Number of alternative routes to be calculated. | [optional] [default to 0]
 **alternativeType** | **String**| Determines whether the alternative routes to be calculated should be better with respect to the planning criteria provided than the reference route. | [optional] [default to &#39;anyRoute&#39;]
 **minDeviationDistance** | **Number**| All alternative routes will follow the reference route for the specified minimum number of meters starting from the origin point. | [optional] [default to 0]
 **minDeviationTime** | **Number**| All alternative routes will follow the reference route for the specified minimum number of seconds starting from the origin point. | [optional] [default to 0]
 **instructionsType** | **String**| If specified, guidance instructions will be returned (if available). | [optional] 
 **language** | **String**| The language parameter determines the language of the guidance messages. | [optional] [default to &#39;en-GB&#39;]
 **computeBestOrder** | **Boolean**| Re-order the route waypoints to reduce the route length. | [optional] [default to false]
 **routeRepresentation** | **String**| Specifies the representation of the set of routes provided as a response. | [optional] [default to &#39;polyline&#39;]
 **computeTravelTimeFor** | **String**| Specifies whether to return additional travel times using different types of traffic information (none, historic, live) as well as the default best-estimate travel time. | [optional] [default to &#39;none&#39;]
 **vehicleHeading** | **Number**| The directional heading of the vehicle in degrees. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.). | [optional] 
 **sectionType** | **String**| Specifies which section types are explicitly reported in the route response. Can be specified multiple times.   - carTrain, ferry, tunnel or motorway   - pedestrian   - tollRoad   - tollVignette   - country   - travelMode   - traffic | [optional] [default to &#39;travelMode&#39;]
 **callback** | **String**| Specifies the jsonp callback method. | [optional] [default to &#39;callback&#39;]
 **report** | **String**| Specifies which data should be reported for diagnosis purposes. | [optional] 
 **departAt** | **String**| The date and time of departure from the origin point. Departure times apart from &lt;i&gt;now&lt;/i&gt; must be specified as a dateTime. | [optional] [default to &#39;now&#39;]
 **arriveAt** | **String**| The date and time of arrival at the destination point. It must be specified as a dateTime. | [optional] 
 **routeType** | **String**| The type of route requested. | [optional] [default to &#39;fastest&#39;]
 **traffic** | **Boolean**| Determines whether current traffic is used in route calculations. Note that information on historic road speeds is always used. | [optional] [default to true]
 **avoid** | **String**| Specifies whether the routing engine should try to avoid specific types of road segment when calculating the route. Can be specified multiple times. Possible values:   - tollRoads   - motorways   - ferries   - unpavedRoads   - carpools   - alreadyUsedRoads | [optional] 
 **travelMode** | **String**| The mode of travel for the requested route. | [optional] [default to &#39;car&#39;]
 **hilliness** | **String**| Degree of hilliness for calculating a thrilling route. | [optional] [default to &#39;normal&#39;]
 **windingness** | **String**| Amount that a thrilling route should wind. | [optional] [default to &#39;normal&#39;]
 **vehicleMaxSpeed** | **Number**| Maximum speed of the vehicle in km/hour. | [optional] [default to 0]
 **vehicleWeight** | **Number**| Weight of the vehicle in kilograms. | [optional] [default to 0]
 **vehicleAxleWeight** | **Number**| Weight per axle of the vehicle in kg. | [optional] [default to 0]
 **vehicleLength** | **Number**| Length of the vehicle in meters. | [optional] [default to 0]
 **vehicleWidth** | **Number**| Width of the vehicle in meters. | [optional] [default to 0]
 **vehicleHeight** | **Number**| Height of the vehicle in meters. | [optional] [default to 0]
 **vehicleCommercial** | **Boolean**| Indicates that the vehicle is used for commercial purposes. This means it may not be allowed on certain roads. | [optional] [default to false]
 **vehicleLoadType** | **String**| Indicates what kinds of hazardous materials the vehicle is carrying (if any). This means it may not be allowed on certain roads. Use these for routing in the US:    - &lt;i&gt;USHazmatClass1&lt;/i&gt; Explosives   - &lt;i&gt;USHazmatClass2&lt;/i&gt; Compressed gas   - &lt;i&gt;USHazmatClass3&lt;/i&gt; Flammable liquids   - &lt;i&gt;USHazmatClass4&lt;/i&gt; Flammable solids   - &lt;i&gt;USHazmatClass5&lt;/i&gt; Oxidizers   - &lt;i&gt;USHazmatClass6&lt;/i&gt; Poisons   - &lt;i&gt;USHazmatClass7&lt;/i&gt; Radioactive   - &lt;i&gt;USHazmatClass8&lt;/i&gt; Corrosives   - &lt;i&gt;USHazmatClass9&lt;/i&gt; Miscellaneous  Use these for routing in all other countries:    - &lt;i&gt;otherHazmatExplosive&lt;/i&gt; Explosives   - &lt;i&gt;otherHazmatGeneral&lt;/i&gt; Miscellaneous   - &lt;i&gt;otherHazmatHarmfulToWater&lt;/i&gt; Harmful to water  vehicleLoadType can be specified multiple times. This parameter is currently only considered for &lt;b&gt;travelMode&lt;/b&gt;&#x3D;&lt;i&gt;truck&lt;/i&gt;. | [optional] 
 **vehicleEngineType** | **String**| Engine type of the vehicle. | [optional] [default to &#39;combustion&#39;]
 **constantSpeedConsumptionInLitersPerHundredkm** | **String**| Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs. | [optional] 
 **currentFuelInLiters** | **Number**| Specifies the current supply of fuel in liters. | [optional] 
 **auxiliaryPowerInLitersPerHour** | **Number**| Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour. | [optional] 
 **fuelEnergyDensityInMJoulesPerLiter** | **Number**| Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ). | [optional] 
 **accelerationEfficiency** | **Number**| Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates (i.e. KineticEnergyGained/ChemicalEnergyConsumed). | [optional] 
 **decelerationEfficiency** | **Number**| Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates (i.e. ChemicalEnergySaved/KineticEnergyLost). | [optional] 
 **uphillEfficiency** | **Number**| Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation (i.e. PotentialEnergyGained/ChemicalEnergyConsumed). | [optional] 
 **downhillEfficiency** | **Number**| Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation (i.e. ChemicalEnergySaved/PotentialEnergyLost). | [optional] 
 **constantSpeedConsumptionInkWhPerHundredkm** | **String**| Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs. | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## routingVersionNumberCalculateRouteLocationsContentTypePost

> routingVersionNumberCalculateRouteLocationsContentTypePost(versionNumber, locations, contentType, opts)

Calculate Route

Calculates a route between an origin and a destination. POST method handles additionally parameters: &lt;em&gt;supportingPoints&lt;/em&gt;, &lt;em&gt;allowVignette&lt;/em&gt;, &lt;em&gt;avoidVignette&lt;/em&gt;, &lt;em&gt;avoidAreas&lt;/em&gt;.

### Example

```javascript
import Routing from 'routing';
let defaultClient = Routing.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new Routing.RoutingApi();
let versionNumber = 56; // Number | Service version number. The current value is 1.
let locations = "52.50931,13.42936:52.50274,13.43872"; // String | Locations through which the calculated route must pass.
let contentType = "'xml'"; // String | The content type of the response structure. If the content type is jsonp, a callback method can be specified in the query parameters.
let opts = {
  'maxAlternatives': 0, // Number | Number of alternative routes to be calculated.
  'alternativeType': "'anyRoute'", // String | Determines whether the alternative routes to be calculated should be better with respect to the planning criteria provided than the reference route.
  'minDeviationDistance': 0, // Number | All alternative routes will follow the reference route for the specified minimum number of meters starting from the origin point.
  'minDeviationTime': 0, // Number | All alternative routes will follow the reference route for the specified minimum number of seconds starting from the origin point.
  'instructionsType': "instructionsType_example", // String | If specified, guidance instructions will be returned (if available).
  'language': "'en-GB'", // String | The language parameter determines the language of the guidance messages.
  'computeBestOrder': false, // Boolean | Re-order the route waypoints to reduce the route length.
  'routeRepresentation': "'polyline'", // String | Specifies the representation of the set of routes provided as a response.
  'computeTravelTimeFor': "'none'", // String | Specifies whether to return additional travel times using different types of traffic information (none, historic, live) as well as the default best-estimate travel time.
  'vehicleHeading': 56, // Number | The directional heading of the vehicle in degrees. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.).
  'sectionType': "'travelMode'", // String | Specifies which section types are explicitly reported in the route response. Can be specified multiple times.   - carTrain, ferry, tunnel or motorway   - pedestrian   - tollRoad   - tollVignette   - country   - travelMode   - traffic
  'callback': "'callback'", // String | Specifies the jsonp callback method.
  'report': "report_example", // String | Specifies which data should be reported for diagnosis purposes.
  'departAt': "'now'", // String | The date and time of departure from the origin point. Departure times apart from <i>now</i> must be specified as a dateTime.
  'arriveAt': "arriveAt_example", // String | The date and time of arrival at the destination point. It must be specified as a dateTime.
  'routeType': "'fastest'", // String | The type of route requested.
  'traffic': true, // Boolean | Determines whether current traffic is used in route calculations. Note that information on historic road speeds is always used.
  'avoid': "unpavedRoads", // String | Specifies whether the routing engine should try to avoid specific types of road segment when calculating the route. Can be specified multiple times. Possible values:   - tollRoads   - motorways   - ferries   - unpavedRoads   - carpools   - alreadyUsedRoads
  'travelMode': "'car'", // String | The mode of travel for the requested route.
  'hilliness': "'normal'", // String | Degree of hilliness for calculating a thrilling route.
  'windingness': "'normal'", // String | Amount that a thrilling route should wind.
  'vehicleMaxSpeed': 0, // Number | Maximum speed of the vehicle in km/hour.
  'vehicleWeight': 0, // Number | Weight of the vehicle in kilograms.
  'vehicleAxleWeight': 0, // Number | Weight per axle of the vehicle in kg.
  'vehicleLength': 0, // Number | Length of the vehicle in meters.
  'vehicleWidth': 0, // Number | Width of the vehicle in meters.
  'vehicleHeight': 0, // Number | Height of the vehicle in meters.
  'vehicleCommercial': false, // Boolean | Indicates that the vehicle is used for commercial purposes. This means it may not be allowed on certain roads.
  'vehicleLoadType': "vehicleLoadType_example", // String | Indicates what kinds of hazardous materials the vehicle is carrying (if any). This means it may not be allowed on certain roads. Use these for routing in the US:    - <i>USHazmatClass1</i> Explosives   - <i>USHazmatClass2</i> Compressed gas   - <i>USHazmatClass3</i> Flammable liquids   - <i>USHazmatClass4</i> Flammable solids   - <i>USHazmatClass5</i> Oxidizers   - <i>USHazmatClass6</i> Poisons   - <i>USHazmatClass7</i> Radioactive   - <i>USHazmatClass8</i> Corrosives   - <i>USHazmatClass9</i> Miscellaneous  Use these for routing in all other countries:    - <i>otherHazmatExplosive</i> Explosives   - <i>otherHazmatGeneral</i> Miscellaneous   - <i>otherHazmatHarmfulToWater</i> Harmful to water  vehicleLoadType can be specified multiple times. This parameter is currently only considered for <b>travelMode</b>=<i>truck</i>.
  'vehicleEngineType': "'combustion'", // String | Engine type of the vehicle.
  'constantSpeedConsumptionInLitersPerHundredkm': "constantSpeedConsumptionInLitersPerHundredkm_example", // String | Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
  'currentFuelInLiters': 3.4, // Number | Specifies the current supply of fuel in liters.
  'auxiliaryPowerInLitersPerHour': 3.4, // Number | Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour.
  'fuelEnergyDensityInMJoulesPerLiter': 3.4, // Number | Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ).
  'accelerationEfficiency': 3.4, // Number | Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates (i.e. KineticEnergyGained/ChemicalEnergyConsumed).
  'decelerationEfficiency': 3.4, // Number | Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates (i.e. ChemicalEnergySaved/KineticEnergyLost).
  'uphillEfficiency': 3.4, // Number | Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation (i.e. PotentialEnergyGained/ChemicalEnergyConsumed).
  'downhillEfficiency': 3.4, // Number | Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation (i.e. ChemicalEnergySaved/PotentialEnergyLost).
  'constantSpeedConsumptionInkWhPerHundredkm': "constantSpeedConsumptionInkWhPerHundredkm_example", // String | Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
  'calculateRoutePostDataParameters': new Routing.CalculateRoutePostDataParameters() // CalculateRoutePostDataParameters | 
};
apiInstance.routingVersionNumberCalculateRouteLocationsContentTypePost(versionNumber, locations, contentType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versionNumber** | **Number**| Service version number. The current value is 1. | 
 **locations** | **String**| Locations through which the calculated route must pass. | 
 **contentType** | **String**| The content type of the response structure. If the content type is jsonp, a callback method can be specified in the query parameters. | [default to &#39;xml&#39;]
 **maxAlternatives** | **Number**| Number of alternative routes to be calculated. | [optional] [default to 0]
 **alternativeType** | **String**| Determines whether the alternative routes to be calculated should be better with respect to the planning criteria provided than the reference route. | [optional] [default to &#39;anyRoute&#39;]
 **minDeviationDistance** | **Number**| All alternative routes will follow the reference route for the specified minimum number of meters starting from the origin point. | [optional] [default to 0]
 **minDeviationTime** | **Number**| All alternative routes will follow the reference route for the specified minimum number of seconds starting from the origin point. | [optional] [default to 0]
 **instructionsType** | **String**| If specified, guidance instructions will be returned (if available). | [optional] 
 **language** | **String**| The language parameter determines the language of the guidance messages. | [optional] [default to &#39;en-GB&#39;]
 **computeBestOrder** | **Boolean**| Re-order the route waypoints to reduce the route length. | [optional] [default to false]
 **routeRepresentation** | **String**| Specifies the representation of the set of routes provided as a response. | [optional] [default to &#39;polyline&#39;]
 **computeTravelTimeFor** | **String**| Specifies whether to return additional travel times using different types of traffic information (none, historic, live) as well as the default best-estimate travel time. | [optional] [default to &#39;none&#39;]
 **vehicleHeading** | **Number**| The directional heading of the vehicle in degrees. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.). | [optional] 
 **sectionType** | **String**| Specifies which section types are explicitly reported in the route response. Can be specified multiple times.   - carTrain, ferry, tunnel or motorway   - pedestrian   - tollRoad   - tollVignette   - country   - travelMode   - traffic | [optional] [default to &#39;travelMode&#39;]
 **callback** | **String**| Specifies the jsonp callback method. | [optional] [default to &#39;callback&#39;]
 **report** | **String**| Specifies which data should be reported for diagnosis purposes. | [optional] 
 **departAt** | **String**| The date and time of departure from the origin point. Departure times apart from &lt;i&gt;now&lt;/i&gt; must be specified as a dateTime. | [optional] [default to &#39;now&#39;]
 **arriveAt** | **String**| The date and time of arrival at the destination point. It must be specified as a dateTime. | [optional] 
 **routeType** | **String**| The type of route requested. | [optional] [default to &#39;fastest&#39;]
 **traffic** | **Boolean**| Determines whether current traffic is used in route calculations. Note that information on historic road speeds is always used. | [optional] [default to true]
 **avoid** | **String**| Specifies whether the routing engine should try to avoid specific types of road segment when calculating the route. Can be specified multiple times. Possible values:   - tollRoads   - motorways   - ferries   - unpavedRoads   - carpools   - alreadyUsedRoads | [optional] 
 **travelMode** | **String**| The mode of travel for the requested route. | [optional] [default to &#39;car&#39;]
 **hilliness** | **String**| Degree of hilliness for calculating a thrilling route. | [optional] [default to &#39;normal&#39;]
 **windingness** | **String**| Amount that a thrilling route should wind. | [optional] [default to &#39;normal&#39;]
 **vehicleMaxSpeed** | **Number**| Maximum speed of the vehicle in km/hour. | [optional] [default to 0]
 **vehicleWeight** | **Number**| Weight of the vehicle in kilograms. | [optional] [default to 0]
 **vehicleAxleWeight** | **Number**| Weight per axle of the vehicle in kg. | [optional] [default to 0]
 **vehicleLength** | **Number**| Length of the vehicle in meters. | [optional] [default to 0]
 **vehicleWidth** | **Number**| Width of the vehicle in meters. | [optional] [default to 0]
 **vehicleHeight** | **Number**| Height of the vehicle in meters. | [optional] [default to 0]
 **vehicleCommercial** | **Boolean**| Indicates that the vehicle is used for commercial purposes. This means it may not be allowed on certain roads. | [optional] [default to false]
 **vehicleLoadType** | **String**| Indicates what kinds of hazardous materials the vehicle is carrying (if any). This means it may not be allowed on certain roads. Use these for routing in the US:    - &lt;i&gt;USHazmatClass1&lt;/i&gt; Explosives   - &lt;i&gt;USHazmatClass2&lt;/i&gt; Compressed gas   - &lt;i&gt;USHazmatClass3&lt;/i&gt; Flammable liquids   - &lt;i&gt;USHazmatClass4&lt;/i&gt; Flammable solids   - &lt;i&gt;USHazmatClass5&lt;/i&gt; Oxidizers   - &lt;i&gt;USHazmatClass6&lt;/i&gt; Poisons   - &lt;i&gt;USHazmatClass7&lt;/i&gt; Radioactive   - &lt;i&gt;USHazmatClass8&lt;/i&gt; Corrosives   - &lt;i&gt;USHazmatClass9&lt;/i&gt; Miscellaneous  Use these for routing in all other countries:    - &lt;i&gt;otherHazmatExplosive&lt;/i&gt; Explosives   - &lt;i&gt;otherHazmatGeneral&lt;/i&gt; Miscellaneous   - &lt;i&gt;otherHazmatHarmfulToWater&lt;/i&gt; Harmful to water  vehicleLoadType can be specified multiple times. This parameter is currently only considered for &lt;b&gt;travelMode&lt;/b&gt;&#x3D;&lt;i&gt;truck&lt;/i&gt;. | [optional] 
 **vehicleEngineType** | **String**| Engine type of the vehicle. | [optional] [default to &#39;combustion&#39;]
 **constantSpeedConsumptionInLitersPerHundredkm** | **String**| Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs. | [optional] 
 **currentFuelInLiters** | **Number**| Specifies the current supply of fuel in liters. | [optional] 
 **auxiliaryPowerInLitersPerHour** | **Number**| Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour. | [optional] 
 **fuelEnergyDensityInMJoulesPerLiter** | **Number**| Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ). | [optional] 
 **accelerationEfficiency** | **Number**| Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates (i.e. KineticEnergyGained/ChemicalEnergyConsumed). | [optional] 
 **decelerationEfficiency** | **Number**| Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates (i.e. ChemicalEnergySaved/KineticEnergyLost). | [optional] 
 **uphillEfficiency** | **Number**| Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation (i.e. PotentialEnergyGained/ChemicalEnergyConsumed). | [optional] 
 **downhillEfficiency** | **Number**| Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation (i.e. ChemicalEnergySaved/PotentialEnergyLost). | [optional] 
 **constantSpeedConsumptionInkWhPerHundredkm** | **String**| Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs. | [optional] 
 **calculateRoutePostDataParameters** | [**CalculateRoutePostDataParameters**](CalculateRoutePostDataParameters.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: Not defined

