# RoutingApi

All URIs are relative to *https://api.tomtom.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**routingVersionNumberCalculateReachableRangeOriginContentTypeGet**](RoutingApi.md#routingVersionNumberCalculateReachableRangeOriginContentTypeGet) | **GET** /routing/{versionNumber}/calculateReachableRange/{origin}/{contentType} | Reachable Range |
| [**routingVersionNumberCalculateReachableRangeOriginContentTypePost**](RoutingApi.md#routingVersionNumberCalculateReachableRangeOriginContentTypePost) | **POST** /routing/{versionNumber}/calculateReachableRange/{origin}/{contentType} | Reachable Range |
| [**routingVersionNumberCalculateRouteLocationsContentTypeGet**](RoutingApi.md#routingVersionNumberCalculateRouteLocationsContentTypeGet) | **GET** /routing/{versionNumber}/calculateRoute/{locations}/{contentType} | Calculate Route |
| [**routingVersionNumberCalculateRouteLocationsContentTypePost**](RoutingApi.md#routingVersionNumberCalculateRouteLocationsContentTypePost) | **POST** /routing/{versionNumber}/calculateRoute/{locations}/{contentType} | Calculate Route |


<a id="routingVersionNumberCalculateReachableRangeOriginContentTypeGet"></a>
# **routingVersionNumberCalculateReachableRangeOriginContentTypeGet**
> routingVersionNumberCalculateReachableRangeOriginContentTypeGet(versionNumber, origin, contentType, fuelBudgetInLiters, energyBudgetInkWh, timeBudgetInSec, paramCallback, report, departAt, arriveAt, routeType, traffic, avoid, travelMode, hilliness, windingness, vehicleMaxSpeed, vehicleWeight, vehicleAxleWeight, vehicleLength, vehicleWidth, vehicleHeight, vehicleCommercial, vehicleLoadType, constantSpeedConsumptionInLitersPerHundredkm, currentFuelInLiters, auxiliaryPowerInLitersPerHour, fuelEnergyDensityInMJoulesPerLiter, accelerationEfficiency, decelerationEfficiency, uphillEfficiency, downhillEfficiency, vehicleEngineType, constantSpeedConsumptionInkWhPerHundredkm)

Reachable Range

Calculates a set of locations that can be reached from the origin point.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    Integer versionNumber = 1; // Integer | Service version number. The current value is 1.
    String origin = "52.50931,13.42936"; // String | Point from which the range calculation should start.
    String contentType = "xml"; // String | The content type of the response structure. If the content type is jsonp, a callback method can be specified in the query parameters.
    Float fuelBudgetInLiters = 3.4F; // Float | Fuel budget in liters. Determines the maximum vehicle range using the specified Combustion Consumption Model.
    Float energyBudgetInkWh = 43F; // Float | Electric energy budget in kilowatt hours (kWh). Determines the maximum vehicle range using the specified Electric Consumption Model.
    Float timeBudgetInSec = 3.4F; // Float | Time budget in seconds. Determines the maximum vehicle range using the specified driving time. The consumption parameters in the request will only affect eco-routes, and thereby indirectly the driving time.
    String paramCallback = "callback"; // String | Specifies the jsonp callback method.
    String report = "effectiveSettings"; // String | Specifies which data should be reported for diagnosis purposes.
    String departAt = "now"; // String | The date and time of departure from the origin point. Departure times apart from <i>now</i> must be specified as a dateTime.
    String arriveAt = "arriveAt_example"; // String | The date and time of arrival at the destination point. It must be specified as a dateTime.
    String routeType = "fastest"; // String | The type of route requested.
    Boolean traffic = true; // Boolean | Determines whether current traffic is used in route calculations. Note that information on historic road speeds is always used.
    String avoid = "unpavedRoads"; // String | Specifies whether the routing engine should try to avoid specific types of road segment when calculating the route. Can be specified multiple times. Possible values:   - tollRoads   - motorways   - ferries   - unpavedRoads   - carpools
    String travelMode = "car"; // String | The mode of travel for the requested route.
    String hilliness = "low"; // String | Degree of hilliness for calculating a thrilling route.
    String windingness = "low"; // String | Amount that a thrilling route should wind.
    Integer vehicleMaxSpeed = 0; // Integer | Maximum speed of the vehicle in km/hour.
    Integer vehicleWeight = 0; // Integer | Weight of the vehicle in kilograms.
    Integer vehicleAxleWeight = 0; // Integer | Weight per axle of the vehicle in kg.
    Float vehicleLength = 0F; // Float | Length of the vehicle in meters.
    Float vehicleWidth = 0F; // Float | Width of the vehicle in meters.
    Float vehicleHeight = 0F; // Float | Height of the vehicle in meters.
    Boolean vehicleCommercial = false; // Boolean | Indicates that the vehicle is used for commercial purposes. This means it may not be allowed on certain roads.
    String vehicleLoadType = "vehicleLoadType_example"; // String | Indicates what kinds of hazardous materials the vehicle is carrying (if any). This means it may not be allowed on certain roads. Use these for routing in the US:    - <i>USHazmatClass1</i> Explosives   - <i>USHazmatClass2</i> Compressed gas   - <i>USHazmatClass3</i> Flammable liquids   - <i>USHazmatClass4</i> Flammable solids   - <i>USHazmatClass5</i> Oxidizers   - <i>USHazmatClass6</i> Poisons   - <i>USHazmatClass7</i> Radioactive   - <i>USHazmatClass8</i> Corrosives   - <i>USHazmatClass9</i> Miscellaneous  Use these for routing in all other countries:    - <i>otherHazmatExplosive</i> Explosives   - <i>otherHazmatGeneral</i> Miscellaneous   - <i>otherHazmatHarmfulToWater</i> Harmful to water  vehicleLoadType can be specified multiple times. This parameter is currently only considered for <b>travelMode</b>=<i>truck</i>.
    String constantSpeedConsumptionInLitersPerHundredkm = "constantSpeedConsumptionInLitersPerHundredkm_example"; // String | Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
    Float currentFuelInLiters = 3.4F; // Float | Specifies the current supply of fuel in liters.
    Float auxiliaryPowerInLitersPerHour = 3.4F; // Float | Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour.
    Float fuelEnergyDensityInMJoulesPerLiter = 3.4F; // Float | Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ).
    Float accelerationEfficiency = 3.4F; // Float | Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates (i.e. KineticEnergyGained/ChemicalEnergyConsumed).
    Float decelerationEfficiency = 3.4F; // Float | Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates (i.e. ChemicalEnergySaved/KineticEnergyLost).
    Float uphillEfficiency = 3.4F; // Float | Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation (i.e. PotentialEnergyGained/ChemicalEnergyConsumed).
    Float downhillEfficiency = 3.4F; // Float | Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation (i.e. ChemicalEnergySaved/PotentialEnergyLost).
    String vehicleEngineType = "combustion"; // String | Engine type of the vehicle.
    String constantSpeedConsumptionInkWhPerHundredkm = "50,8.2:130,21.3"; // String | Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
    try {
      apiInstance.routingVersionNumberCalculateReachableRangeOriginContentTypeGet(versionNumber, origin, contentType, fuelBudgetInLiters, energyBudgetInkWh, timeBudgetInSec, paramCallback, report, departAt, arriveAt, routeType, traffic, avoid, travelMode, hilliness, windingness, vehicleMaxSpeed, vehicleWeight, vehicleAxleWeight, vehicleLength, vehicleWidth, vehicleHeight, vehicleCommercial, vehicleLoadType, constantSpeedConsumptionInLitersPerHundredkm, currentFuelInLiters, auxiliaryPowerInLitersPerHour, fuelEnergyDensityInMJoulesPerLiter, accelerationEfficiency, decelerationEfficiency, uphillEfficiency, downhillEfficiency, vehicleEngineType, constantSpeedConsumptionInkWhPerHundredkm);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#routingVersionNumberCalculateReachableRangeOriginContentTypeGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **versionNumber** | **Integer**| Service version number. The current value is 1. | [enum: 1] |
| **origin** | **String**| Point from which the range calculation should start. | |
| **contentType** | **String**| The content type of the response structure. If the content type is jsonp, a callback method can be specified in the query parameters. | [default to xml] [enum: xml, json, jsonp] |
| **fuelBudgetInLiters** | **Float**| Fuel budget in liters. Determines the maximum vehicle range using the specified Combustion Consumption Model. | [optional] |
| **energyBudgetInkWh** | **Float**| Electric energy budget in kilowatt hours (kWh). Determines the maximum vehicle range using the specified Electric Consumption Model. | [optional] |
| **timeBudgetInSec** | **Float**| Time budget in seconds. Determines the maximum vehicle range using the specified driving time. The consumption parameters in the request will only affect eco-routes, and thereby indirectly the driving time. | [optional] |
| **paramCallback** | **String**| Specifies the jsonp callback method. | [optional] [default to callback] |
| **report** | **String**| Specifies which data should be reported for diagnosis purposes. | [optional] [enum: effectiveSettings] |
| **departAt** | **String**| The date and time of departure from the origin point. Departure times apart from &lt;i&gt;now&lt;/i&gt; must be specified as a dateTime. | [optional] [default to now] |
| **arriveAt** | **String**| The date and time of arrival at the destination point. It must be specified as a dateTime. | [optional] |
| **routeType** | **String**| The type of route requested. | [optional] [default to fastest] [enum: fastest, shortest, eco, thrilling] |
| **traffic** | **Boolean**| Determines whether current traffic is used in route calculations. Note that information on historic road speeds is always used. | [optional] [default to true] |
| **avoid** | **String**| Specifies whether the routing engine should try to avoid specific types of road segment when calculating the route. Can be specified multiple times. Possible values:   - tollRoads   - motorways   - ferries   - unpavedRoads   - carpools | [optional] |
| **travelMode** | **String**| The mode of travel for the requested route. | [optional] [default to car] [enum: car, truck, taxi, bus, van, motorcycle, bicycle, pedestrian] |
| **hilliness** | **String**| Degree of hilliness for calculating a thrilling route. | [optional] [default to normal] [enum: low, normal, high] |
| **windingness** | **String**| Amount that a thrilling route should wind. | [optional] [default to normal] [enum: low, normal, high] |
| **vehicleMaxSpeed** | **Integer**| Maximum speed of the vehicle in km/hour. | [optional] [default to 0] |
| **vehicleWeight** | **Integer**| Weight of the vehicle in kilograms. | [optional] [default to 0] |
| **vehicleAxleWeight** | **Integer**| Weight per axle of the vehicle in kg. | [optional] [default to 0] |
| **vehicleLength** | **Float**| Length of the vehicle in meters. | [optional] [default to 0] |
| **vehicleWidth** | **Float**| Width of the vehicle in meters. | [optional] [default to 0] |
| **vehicleHeight** | **Float**| Height of the vehicle in meters. | [optional] [default to 0] |
| **vehicleCommercial** | **Boolean**| Indicates that the vehicle is used for commercial purposes. This means it may not be allowed on certain roads. | [optional] [default to false] |
| **vehicleLoadType** | **String**| Indicates what kinds of hazardous materials the vehicle is carrying (if any). This means it may not be allowed on certain roads. Use these for routing in the US:    - &lt;i&gt;USHazmatClass1&lt;/i&gt; Explosives   - &lt;i&gt;USHazmatClass2&lt;/i&gt; Compressed gas   - &lt;i&gt;USHazmatClass3&lt;/i&gt; Flammable liquids   - &lt;i&gt;USHazmatClass4&lt;/i&gt; Flammable solids   - &lt;i&gt;USHazmatClass5&lt;/i&gt; Oxidizers   - &lt;i&gt;USHazmatClass6&lt;/i&gt; Poisons   - &lt;i&gt;USHazmatClass7&lt;/i&gt; Radioactive   - &lt;i&gt;USHazmatClass8&lt;/i&gt; Corrosives   - &lt;i&gt;USHazmatClass9&lt;/i&gt; Miscellaneous  Use these for routing in all other countries:    - &lt;i&gt;otherHazmatExplosive&lt;/i&gt; Explosives   - &lt;i&gt;otherHazmatGeneral&lt;/i&gt; Miscellaneous   - &lt;i&gt;otherHazmatHarmfulToWater&lt;/i&gt; Harmful to water  vehicleLoadType can be specified multiple times. This parameter is currently only considered for &lt;b&gt;travelMode&lt;/b&gt;&#x3D;&lt;i&gt;truck&lt;/i&gt;. | [optional] |
| **constantSpeedConsumptionInLitersPerHundredkm** | **String**| Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs. | [optional] |
| **currentFuelInLiters** | **Float**| Specifies the current supply of fuel in liters. | [optional] |
| **auxiliaryPowerInLitersPerHour** | **Float**| Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour. | [optional] |
| **fuelEnergyDensityInMJoulesPerLiter** | **Float**| Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ). | [optional] |
| **accelerationEfficiency** | **Float**| Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates (i.e. KineticEnergyGained/ChemicalEnergyConsumed). | [optional] |
| **decelerationEfficiency** | **Float**| Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates (i.e. ChemicalEnergySaved/KineticEnergyLost). | [optional] |
| **uphillEfficiency** | **Float**| Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation (i.e. PotentialEnergyGained/ChemicalEnergyConsumed). | [optional] |
| **downhillEfficiency** | **Float**| Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation (i.e. ChemicalEnergySaved/PotentialEnergyLost). | [optional] |
| **vehicleEngineType** | **String**| Engine type of the vehicle. | [optional] [default to combustion] [enum: combustion, electric] |
| **constantSpeedConsumptionInkWhPerHundredkm** | **String**| Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK: a range was calculated and the body of the response contains the polygon description and further data. |  -  |
| **400** | Bad request: one or more parameters were incorrectly specified or are mutually exclusive, or the origin point specified in the request is not near enough to a road. |  -  |
| **403** | Permission, capacity, or authentication issues:   - Forbidden   - Not authorized   - Account inactive   - Account over queries per second limit   - Account over rate limit   - Rate limit exceeded |  -  |
| **404** | Not Found: the requested resource could not be found, but it may be available again in the future. |  -  |
| **405** | Method Not Allowed: the client used a HTTP method other than GET or POST. |  -  |
| **408** | Request timeout. |  -  |
| **414** | Requested uri is too long. |  -  |
| **500** | An error occurred while processing the request. Please try again later. |  -  |
| **502** | Internal network connectivity issue. |  -  |
| **503** | Service currently unavailable. |  -  |
| **504** | Internal network connectivity issue or a request that has taken too long to complete. |  -  |
| **596** | Service not found. |  -  |

<a id="routingVersionNumberCalculateReachableRangeOriginContentTypePost"></a>
# **routingVersionNumberCalculateReachableRangeOriginContentTypePost**
> routingVersionNumberCalculateReachableRangeOriginContentTypePost(versionNumber, origin, contentType, fuelBudgetInLiters, energyBudgetInkWh, timeBudgetInSec, paramCallback, report, departAt, arriveAt, routeType, traffic, avoid, travelMode, hilliness, windingness, vehicleMaxSpeed, vehicleWeight, vehicleAxleWeight, vehicleLength, vehicleWidth, vehicleHeight, vehicleCommercial, vehicleLoadType, constantSpeedConsumptionInLitersPerHundredkm, currentFuelInLiters, auxiliaryPowerInLitersPerHour, fuelEnergyDensityInMJoulesPerLiter, accelerationEfficiency, decelerationEfficiency, uphillEfficiency, downhillEfficiency, vehicleEngineType, constantSpeedConsumptionInkWhPerHundredkm, calculateReachableRangePostDataParameters)

Reachable Range

Calculates a set of locations that can be reached from the origin point. POST method handles additionally parameters: &lt;em&gt;supportingPoints&lt;/em&gt;, &lt;em&gt;allowVignette&lt;/em&gt;, &lt;em&gt;avoidVignette&lt;/em&gt;, &lt;em&gt;avoidAreas&lt;/em&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    Integer versionNumber = 1; // Integer | Service version number. The current value is 1.
    String origin = "52.50931,13.42936"; // String | Point from which the range calculation should start.
    String contentType = "xml"; // String | The content type of the response structure. If the content type is jsonp, a callback method can be specified in the query parameters.
    Float fuelBudgetInLiters = 3.4F; // Float | Fuel budget in liters. Determines the maximum vehicle range using the specified Combustion Consumption Model.
    Float energyBudgetInkWh = 43F; // Float | Electric energy budget in kilowatt hours (kWh). Determines the maximum vehicle range using the specified Electric Consumption Model.
    Float timeBudgetInSec = 3.4F; // Float | Time budget in seconds. Determines the maximum vehicle range using the specified driving time. The consumption parameters in the request will only affect eco-routes, and thereby indirectly the driving time.
    String paramCallback = "callback"; // String | Specifies the jsonp callback method.
    String report = "effectiveSettings"; // String | Specifies which data should be reported for diagnosis purposes.
    String departAt = "now"; // String | The date and time of departure from the origin point. Departure times apart from <i>now</i> must be specified as a dateTime.
    String arriveAt = "arriveAt_example"; // String | The date and time of arrival at the destination point. It must be specified as a dateTime.
    String routeType = "fastest"; // String | The type of route requested.
    Boolean traffic = true; // Boolean | Determines whether current traffic is used in route calculations. Note that information on historic road speeds is always used.
    String avoid = "unpavedRoads"; // String | Specifies whether the routing engine should try to avoid specific types of road segment when calculating the route. Can be specified multiple times. Possible values:   - tollRoads   - motorways   - ferries   - unpavedRoads   - carpools
    String travelMode = "car"; // String | The mode of travel for the requested route.
    String hilliness = "low"; // String | Degree of hilliness for calculating a thrilling route.
    String windingness = "low"; // String | Amount that a thrilling route should wind.
    Integer vehicleMaxSpeed = 0; // Integer | Maximum speed of the vehicle in km/hour.
    Integer vehicleWeight = 0; // Integer | Weight of the vehicle in kilograms.
    Integer vehicleAxleWeight = 0; // Integer | Weight per axle of the vehicle in kg.
    Float vehicleLength = 0F; // Float | Length of the vehicle in meters.
    Float vehicleWidth = 0F; // Float | Width of the vehicle in meters.
    Float vehicleHeight = 0F; // Float | Height of the vehicle in meters.
    Boolean vehicleCommercial = false; // Boolean | Indicates that the vehicle is used for commercial purposes. This means it may not be allowed on certain roads.
    String vehicleLoadType = "vehicleLoadType_example"; // String | Indicates what kinds of hazardous materials the vehicle is carrying (if any). This means it may not be allowed on certain roads. Use these for routing in the US:    - <i>USHazmatClass1</i> Explosives   - <i>USHazmatClass2</i> Compressed gas   - <i>USHazmatClass3</i> Flammable liquids   - <i>USHazmatClass4</i> Flammable solids   - <i>USHazmatClass5</i> Oxidizers   - <i>USHazmatClass6</i> Poisons   - <i>USHazmatClass7</i> Radioactive   - <i>USHazmatClass8</i> Corrosives   - <i>USHazmatClass9</i> Miscellaneous  Use these for routing in all other countries:    - <i>otherHazmatExplosive</i> Explosives   - <i>otherHazmatGeneral</i> Miscellaneous   - <i>otherHazmatHarmfulToWater</i> Harmful to water  vehicleLoadType can be specified multiple times. This parameter is currently only considered for <b>travelMode</b>=<i>truck</i>.
    String constantSpeedConsumptionInLitersPerHundredkm = "constantSpeedConsumptionInLitersPerHundredkm_example"; // String | Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
    Float currentFuelInLiters = 3.4F; // Float | Specifies the current supply of fuel in liters.
    Float auxiliaryPowerInLitersPerHour = 3.4F; // Float | Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour.
    Float fuelEnergyDensityInMJoulesPerLiter = 3.4F; // Float | Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ).
    Float accelerationEfficiency = 3.4F; // Float | Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates (i.e. KineticEnergyGained/ChemicalEnergyConsumed).
    Float decelerationEfficiency = 3.4F; // Float | Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates (i.e. ChemicalEnergySaved/KineticEnergyLost).
    Float uphillEfficiency = 3.4F; // Float | Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation (i.e. PotentialEnergyGained/ChemicalEnergyConsumed).
    Float downhillEfficiency = 3.4F; // Float | Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation (i.e. ChemicalEnergySaved/PotentialEnergyLost).
    String vehicleEngineType = "combustion"; // String | Engine type of the vehicle.
    String constantSpeedConsumptionInkWhPerHundredkm = "50,8.2:130,21.3"; // String | Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
    CalculateReachableRangePostDataParameters calculateReachableRangePostDataParameters = new CalculateReachableRangePostDataParameters(); // CalculateReachableRangePostDataParameters | 
    try {
      apiInstance.routingVersionNumberCalculateReachableRangeOriginContentTypePost(versionNumber, origin, contentType, fuelBudgetInLiters, energyBudgetInkWh, timeBudgetInSec, paramCallback, report, departAt, arriveAt, routeType, traffic, avoid, travelMode, hilliness, windingness, vehicleMaxSpeed, vehicleWeight, vehicleAxleWeight, vehicleLength, vehicleWidth, vehicleHeight, vehicleCommercial, vehicleLoadType, constantSpeedConsumptionInLitersPerHundredkm, currentFuelInLiters, auxiliaryPowerInLitersPerHour, fuelEnergyDensityInMJoulesPerLiter, accelerationEfficiency, decelerationEfficiency, uphillEfficiency, downhillEfficiency, vehicleEngineType, constantSpeedConsumptionInkWhPerHundredkm, calculateReachableRangePostDataParameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#routingVersionNumberCalculateReachableRangeOriginContentTypePost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **versionNumber** | **Integer**| Service version number. The current value is 1. | [enum: 1] |
| **origin** | **String**| Point from which the range calculation should start. | |
| **contentType** | **String**| The content type of the response structure. If the content type is jsonp, a callback method can be specified in the query parameters. | [default to xml] [enum: xml, json, jsonp] |
| **fuelBudgetInLiters** | **Float**| Fuel budget in liters. Determines the maximum vehicle range using the specified Combustion Consumption Model. | [optional] |
| **energyBudgetInkWh** | **Float**| Electric energy budget in kilowatt hours (kWh). Determines the maximum vehicle range using the specified Electric Consumption Model. | [optional] |
| **timeBudgetInSec** | **Float**| Time budget in seconds. Determines the maximum vehicle range using the specified driving time. The consumption parameters in the request will only affect eco-routes, and thereby indirectly the driving time. | [optional] |
| **paramCallback** | **String**| Specifies the jsonp callback method. | [optional] [default to callback] |
| **report** | **String**| Specifies which data should be reported for diagnosis purposes. | [optional] [enum: effectiveSettings] |
| **departAt** | **String**| The date and time of departure from the origin point. Departure times apart from &lt;i&gt;now&lt;/i&gt; must be specified as a dateTime. | [optional] [default to now] |
| **arriveAt** | **String**| The date and time of arrival at the destination point. It must be specified as a dateTime. | [optional] |
| **routeType** | **String**| The type of route requested. | [optional] [default to fastest] [enum: fastest, shortest, eco, thrilling] |
| **traffic** | **Boolean**| Determines whether current traffic is used in route calculations. Note that information on historic road speeds is always used. | [optional] [default to true] |
| **avoid** | **String**| Specifies whether the routing engine should try to avoid specific types of road segment when calculating the route. Can be specified multiple times. Possible values:   - tollRoads   - motorways   - ferries   - unpavedRoads   - carpools | [optional] |
| **travelMode** | **String**| The mode of travel for the requested route. | [optional] [default to car] [enum: car, truck, taxi, bus, van, motorcycle, bicycle, pedestrian] |
| **hilliness** | **String**| Degree of hilliness for calculating a thrilling route. | [optional] [default to normal] [enum: low, normal, high] |
| **windingness** | **String**| Amount that a thrilling route should wind. | [optional] [default to normal] [enum: low, normal, high] |
| **vehicleMaxSpeed** | **Integer**| Maximum speed of the vehicle in km/hour. | [optional] [default to 0] |
| **vehicleWeight** | **Integer**| Weight of the vehicle in kilograms. | [optional] [default to 0] |
| **vehicleAxleWeight** | **Integer**| Weight per axle of the vehicle in kg. | [optional] [default to 0] |
| **vehicleLength** | **Float**| Length of the vehicle in meters. | [optional] [default to 0] |
| **vehicleWidth** | **Float**| Width of the vehicle in meters. | [optional] [default to 0] |
| **vehicleHeight** | **Float**| Height of the vehicle in meters. | [optional] [default to 0] |
| **vehicleCommercial** | **Boolean**| Indicates that the vehicle is used for commercial purposes. This means it may not be allowed on certain roads. | [optional] [default to false] |
| **vehicleLoadType** | **String**| Indicates what kinds of hazardous materials the vehicle is carrying (if any). This means it may not be allowed on certain roads. Use these for routing in the US:    - &lt;i&gt;USHazmatClass1&lt;/i&gt; Explosives   - &lt;i&gt;USHazmatClass2&lt;/i&gt; Compressed gas   - &lt;i&gt;USHazmatClass3&lt;/i&gt; Flammable liquids   - &lt;i&gt;USHazmatClass4&lt;/i&gt; Flammable solids   - &lt;i&gt;USHazmatClass5&lt;/i&gt; Oxidizers   - &lt;i&gt;USHazmatClass6&lt;/i&gt; Poisons   - &lt;i&gt;USHazmatClass7&lt;/i&gt; Radioactive   - &lt;i&gt;USHazmatClass8&lt;/i&gt; Corrosives   - &lt;i&gt;USHazmatClass9&lt;/i&gt; Miscellaneous  Use these for routing in all other countries:    - &lt;i&gt;otherHazmatExplosive&lt;/i&gt; Explosives   - &lt;i&gt;otherHazmatGeneral&lt;/i&gt; Miscellaneous   - &lt;i&gt;otherHazmatHarmfulToWater&lt;/i&gt; Harmful to water  vehicleLoadType can be specified multiple times. This parameter is currently only considered for &lt;b&gt;travelMode&lt;/b&gt;&#x3D;&lt;i&gt;truck&lt;/i&gt;. | [optional] |
| **constantSpeedConsumptionInLitersPerHundredkm** | **String**| Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs. | [optional] |
| **currentFuelInLiters** | **Float**| Specifies the current supply of fuel in liters. | [optional] |
| **auxiliaryPowerInLitersPerHour** | **Float**| Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour. | [optional] |
| **fuelEnergyDensityInMJoulesPerLiter** | **Float**| Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ). | [optional] |
| **accelerationEfficiency** | **Float**| Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates (i.e. KineticEnergyGained/ChemicalEnergyConsumed). | [optional] |
| **decelerationEfficiency** | **Float**| Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates (i.e. ChemicalEnergySaved/KineticEnergyLost). | [optional] |
| **uphillEfficiency** | **Float**| Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation (i.e. PotentialEnergyGained/ChemicalEnergyConsumed). | [optional] |
| **downhillEfficiency** | **Float**| Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation (i.e. ChemicalEnergySaved/PotentialEnergyLost). | [optional] |
| **vehicleEngineType** | **String**| Engine type of the vehicle. | [optional] [default to combustion] [enum: combustion, electric] |
| **constantSpeedConsumptionInkWhPerHundredkm** | **String**| Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs. | [optional] |
| **calculateReachableRangePostDataParameters** | [**CalculateReachableRangePostDataParameters**](CalculateReachableRangePostDataParameters.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK: a range was calculated and the body of the response contains the polygon description and further data. |  -  |
| **400** | Bad request: one or more parameters were incorrectly specified or are mutually exclusive, or the origin point specified in the request is not near enough to a road. |  -  |
| **403** | Permission, capacity, or authentication issues:   - Forbidden   - Not authorized   - Account inactive   - Account over queries per second limit   - Account over rate limit   - Rate limit exceeded |  -  |
| **404** | Not Found: the requested resource could not be found, but it may be available again in the future. |  -  |
| **405** | Method Not Allowed: the client used a HTTP method other than GET or POST. |  -  |
| **408** | Request timeout. |  -  |
| **414** | Requested uri is too long. |  -  |
| **500** | An error occurred while processing the request. Please try again later. |  -  |
| **502** | Internal network connectivity issue. |  -  |
| **503** | Service currently unavailable. |  -  |
| **504** | Internal network connectivity issue or a request that has taken too long to complete. |  -  |
| **596** | Service not found. |  -  |

<a id="routingVersionNumberCalculateRouteLocationsContentTypeGet"></a>
# **routingVersionNumberCalculateRouteLocationsContentTypeGet**
> routingVersionNumberCalculateRouteLocationsContentTypeGet(versionNumber, locations, contentType, maxAlternatives, alternativeType, minDeviationDistance, minDeviationTime, instructionsType, language, computeBestOrder, routeRepresentation, computeTravelTimeFor, vehicleHeading, sectionType, paramCallback, report, departAt, arriveAt, routeType, traffic, avoid, travelMode, hilliness, windingness, vehicleMaxSpeed, vehicleWeight, vehicleAxleWeight, vehicleLength, vehicleWidth, vehicleHeight, vehicleCommercial, vehicleLoadType, vehicleEngineType, constantSpeedConsumptionInLitersPerHundredkm, currentFuelInLiters, auxiliaryPowerInLitersPerHour, fuelEnergyDensityInMJoulesPerLiter, accelerationEfficiency, decelerationEfficiency, uphillEfficiency, downhillEfficiency, constantSpeedConsumptionInkWhPerHundredkm)

Calculate Route

Calculates a route between an origin and a destination.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    Integer versionNumber = 1; // Integer | Service version number. The current value is 1.
    String locations = "52.50931,13.42936:52.50274,13.43872"; // String | Locations through which the calculated route must pass.
    String contentType = "xml"; // String | The content type of the response structure. If the content type is jsonp, a callback method can be specified in the query parameters.
    Integer maxAlternatives = 0; // Integer | Number of alternative routes to be calculated.
    String alternativeType = "anyRoute"; // String | Determines whether the alternative routes to be calculated should be better with respect to the planning criteria provided than the reference route.
    Integer minDeviationDistance = 0; // Integer | All alternative routes will follow the reference route for the specified minimum number of meters starting from the origin point.
    Integer minDeviationTime = 0; // Integer | All alternative routes will follow the reference route for the specified minimum number of seconds starting from the origin point.
    String instructionsType = "coded"; // String | If specified, guidance instructions will be returned (if available).
    String language = "en-GB"; // String | The language parameter determines the language of the guidance messages.
    Boolean computeBestOrder = false; // Boolean | Re-order the route waypoints to reduce the route length.
    String routeRepresentation = "polyline"; // String | Specifies the representation of the set of routes provided as a response.
    String computeTravelTimeFor = "none"; // String | Specifies whether to return additional travel times using different types of traffic information (none, historic, live) as well as the default best-estimate travel time.
    Integer vehicleHeading = 56; // Integer | The directional heading of the vehicle in degrees. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.).
    String sectionType = "travelMode"; // String | Specifies which section types are explicitly reported in the route response. Can be specified multiple times.   - carTrain, ferry, tunnel or motorway   - pedestrian   - tollRoad   - tollVignette   - country   - travelMode   - traffic
    String paramCallback = "callback"; // String | Specifies the jsonp callback method.
    String report = "effectiveSettings"; // String | Specifies which data should be reported for diagnosis purposes.
    String departAt = "now"; // String | The date and time of departure from the origin point. Departure times apart from <i>now</i> must be specified as a dateTime.
    String arriveAt = "arriveAt_example"; // String | The date and time of arrival at the destination point. It must be specified as a dateTime.
    String routeType = "fastest"; // String | The type of route requested.
    Boolean traffic = true; // Boolean | Determines whether current traffic is used in route calculations. Note that information on historic road speeds is always used.
    String avoid = "unpavedRoads"; // String | Specifies whether the routing engine should try to avoid specific types of road segment when calculating the route. Can be specified multiple times. Possible values:   - tollRoads   - motorways   - ferries   - unpavedRoads   - carpools   - alreadyUsedRoads
    String travelMode = "car"; // String | The mode of travel for the requested route.
    String hilliness = "low"; // String | Degree of hilliness for calculating a thrilling route.
    String windingness = "low"; // String | Amount that a thrilling route should wind.
    Integer vehicleMaxSpeed = 0; // Integer | Maximum speed of the vehicle in km/hour.
    Integer vehicleWeight = 0; // Integer | Weight of the vehicle in kilograms.
    Integer vehicleAxleWeight = 0; // Integer | Weight per axle of the vehicle in kg.
    Float vehicleLength = 0F; // Float | Length of the vehicle in meters.
    Float vehicleWidth = 0F; // Float | Width of the vehicle in meters.
    Float vehicleHeight = 0F; // Float | Height of the vehicle in meters.
    Boolean vehicleCommercial = false; // Boolean | Indicates that the vehicle is used for commercial purposes. This means it may not be allowed on certain roads.
    String vehicleLoadType = "vehicleLoadType_example"; // String | Indicates what kinds of hazardous materials the vehicle is carrying (if any). This means it may not be allowed on certain roads. Use these for routing in the US:    - <i>USHazmatClass1</i> Explosives   - <i>USHazmatClass2</i> Compressed gas   - <i>USHazmatClass3</i> Flammable liquids   - <i>USHazmatClass4</i> Flammable solids   - <i>USHazmatClass5</i> Oxidizers   - <i>USHazmatClass6</i> Poisons   - <i>USHazmatClass7</i> Radioactive   - <i>USHazmatClass8</i> Corrosives   - <i>USHazmatClass9</i> Miscellaneous  Use these for routing in all other countries:    - <i>otherHazmatExplosive</i> Explosives   - <i>otherHazmatGeneral</i> Miscellaneous   - <i>otherHazmatHarmfulToWater</i> Harmful to water  vehicleLoadType can be specified multiple times. This parameter is currently only considered for <b>travelMode</b>=<i>truck</i>.
    String vehicleEngineType = "combustion"; // String | Engine type of the vehicle.
    String constantSpeedConsumptionInLitersPerHundredkm = "constantSpeedConsumptionInLitersPerHundredkm_example"; // String | Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
    Float currentFuelInLiters = 3.4F; // Float | Specifies the current supply of fuel in liters.
    Float auxiliaryPowerInLitersPerHour = 3.4F; // Float | Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour.
    Float fuelEnergyDensityInMJoulesPerLiter = 3.4F; // Float | Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ).
    Float accelerationEfficiency = 3.4F; // Float | Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates (i.e. KineticEnergyGained/ChemicalEnergyConsumed).
    Float decelerationEfficiency = 3.4F; // Float | Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates (i.e. ChemicalEnergySaved/KineticEnergyLost).
    Float uphillEfficiency = 3.4F; // Float | Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation (i.e. PotentialEnergyGained/ChemicalEnergyConsumed).
    Float downhillEfficiency = 3.4F; // Float | Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation (i.e. ChemicalEnergySaved/PotentialEnergyLost).
    String constantSpeedConsumptionInkWhPerHundredkm = "constantSpeedConsumptionInkWhPerHundredkm_example"; // String | Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
    try {
      apiInstance.routingVersionNumberCalculateRouteLocationsContentTypeGet(versionNumber, locations, contentType, maxAlternatives, alternativeType, minDeviationDistance, minDeviationTime, instructionsType, language, computeBestOrder, routeRepresentation, computeTravelTimeFor, vehicleHeading, sectionType, paramCallback, report, departAt, arriveAt, routeType, traffic, avoid, travelMode, hilliness, windingness, vehicleMaxSpeed, vehicleWeight, vehicleAxleWeight, vehicleLength, vehicleWidth, vehicleHeight, vehicleCommercial, vehicleLoadType, vehicleEngineType, constantSpeedConsumptionInLitersPerHundredkm, currentFuelInLiters, auxiliaryPowerInLitersPerHour, fuelEnergyDensityInMJoulesPerLiter, accelerationEfficiency, decelerationEfficiency, uphillEfficiency, downhillEfficiency, constantSpeedConsumptionInkWhPerHundredkm);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#routingVersionNumberCalculateRouteLocationsContentTypeGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **versionNumber** | **Integer**| Service version number. The current value is 1. | [enum: 1] |
| **locations** | **String**| Locations through which the calculated route must pass. | |
| **contentType** | **String**| The content type of the response structure. If the content type is jsonp, a callback method can be specified in the query parameters. | [default to xml] [enum: xml, json, jsonp] |
| **maxAlternatives** | **Integer**| Number of alternative routes to be calculated. | [optional] [default to 0] |
| **alternativeType** | **String**| Determines whether the alternative routes to be calculated should be better with respect to the planning criteria provided than the reference route. | [optional] [default to anyRoute] [enum: anyRoute, betterRoute] |
| **minDeviationDistance** | **Integer**| All alternative routes will follow the reference route for the specified minimum number of meters starting from the origin point. | [optional] [default to 0] |
| **minDeviationTime** | **Integer**| All alternative routes will follow the reference route for the specified minimum number of seconds starting from the origin point. | [optional] [default to 0] |
| **instructionsType** | **String**| If specified, guidance instructions will be returned (if available). | [optional] [enum: coded, text, tagged] |
| **language** | **String**| The language parameter determines the language of the guidance messages. | [optional] [default to en-GB] |
| **computeBestOrder** | **Boolean**| Re-order the route waypoints to reduce the route length. | [optional] [default to false] |
| **routeRepresentation** | **String**| Specifies the representation of the set of routes provided as a response. | [optional] [default to polyline] [enum: polyline, none] |
| **computeTravelTimeFor** | **String**| Specifies whether to return additional travel times using different types of traffic information (none, historic, live) as well as the default best-estimate travel time. | [optional] [default to none] [enum: none, all] |
| **vehicleHeading** | **Integer**| The directional heading of the vehicle in degrees. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.). | [optional] |
| **sectionType** | **String**| Specifies which section types are explicitly reported in the route response. Can be specified multiple times.   - carTrain, ferry, tunnel or motorway   - pedestrian   - tollRoad   - tollVignette   - country   - travelMode   - traffic | [optional] [default to travelMode] |
| **paramCallback** | **String**| Specifies the jsonp callback method. | [optional] [default to callback] |
| **report** | **String**| Specifies which data should be reported for diagnosis purposes. | [optional] [enum: effectiveSettings] |
| **departAt** | **String**| The date and time of departure from the origin point. Departure times apart from &lt;i&gt;now&lt;/i&gt; must be specified as a dateTime. | [optional] [default to now] |
| **arriveAt** | **String**| The date and time of arrival at the destination point. It must be specified as a dateTime. | [optional] |
| **routeType** | **String**| The type of route requested. | [optional] [default to fastest] [enum: fastest, shortest, eco, thrilling] |
| **traffic** | **Boolean**| Determines whether current traffic is used in route calculations. Note that information on historic road speeds is always used. | [optional] [default to true] |
| **avoid** | **String**| Specifies whether the routing engine should try to avoid specific types of road segment when calculating the route. Can be specified multiple times. Possible values:   - tollRoads   - motorways   - ferries   - unpavedRoads   - carpools   - alreadyUsedRoads | [optional] |
| **travelMode** | **String**| The mode of travel for the requested route. | [optional] [default to car] [enum: car, truck, taxi, bus, van, motorcycle, bicycle, pedestrian] |
| **hilliness** | **String**| Degree of hilliness for calculating a thrilling route. | [optional] [default to normal] [enum: low, normal, high] |
| **windingness** | **String**| Amount that a thrilling route should wind. | [optional] [default to normal] [enum: low, normal, high] |
| **vehicleMaxSpeed** | **Integer**| Maximum speed of the vehicle in km/hour. | [optional] [default to 0] |
| **vehicleWeight** | **Integer**| Weight of the vehicle in kilograms. | [optional] [default to 0] |
| **vehicleAxleWeight** | **Integer**| Weight per axle of the vehicle in kg. | [optional] [default to 0] |
| **vehicleLength** | **Float**| Length of the vehicle in meters. | [optional] [default to 0] |
| **vehicleWidth** | **Float**| Width of the vehicle in meters. | [optional] [default to 0] |
| **vehicleHeight** | **Float**| Height of the vehicle in meters. | [optional] [default to 0] |
| **vehicleCommercial** | **Boolean**| Indicates that the vehicle is used for commercial purposes. This means it may not be allowed on certain roads. | [optional] [default to false] |
| **vehicleLoadType** | **String**| Indicates what kinds of hazardous materials the vehicle is carrying (if any). This means it may not be allowed on certain roads. Use these for routing in the US:    - &lt;i&gt;USHazmatClass1&lt;/i&gt; Explosives   - &lt;i&gt;USHazmatClass2&lt;/i&gt; Compressed gas   - &lt;i&gt;USHazmatClass3&lt;/i&gt; Flammable liquids   - &lt;i&gt;USHazmatClass4&lt;/i&gt; Flammable solids   - &lt;i&gt;USHazmatClass5&lt;/i&gt; Oxidizers   - &lt;i&gt;USHazmatClass6&lt;/i&gt; Poisons   - &lt;i&gt;USHazmatClass7&lt;/i&gt; Radioactive   - &lt;i&gt;USHazmatClass8&lt;/i&gt; Corrosives   - &lt;i&gt;USHazmatClass9&lt;/i&gt; Miscellaneous  Use these for routing in all other countries:    - &lt;i&gt;otherHazmatExplosive&lt;/i&gt; Explosives   - &lt;i&gt;otherHazmatGeneral&lt;/i&gt; Miscellaneous   - &lt;i&gt;otherHazmatHarmfulToWater&lt;/i&gt; Harmful to water  vehicleLoadType can be specified multiple times. This parameter is currently only considered for &lt;b&gt;travelMode&lt;/b&gt;&#x3D;&lt;i&gt;truck&lt;/i&gt;. | [optional] |
| **vehicleEngineType** | **String**| Engine type of the vehicle. | [optional] [default to combustion] [enum: combustion, electric] |
| **constantSpeedConsumptionInLitersPerHundredkm** | **String**| Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs. | [optional] |
| **currentFuelInLiters** | **Float**| Specifies the current supply of fuel in liters. | [optional] |
| **auxiliaryPowerInLitersPerHour** | **Float**| Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour. | [optional] |
| **fuelEnergyDensityInMJoulesPerLiter** | **Float**| Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ). | [optional] |
| **accelerationEfficiency** | **Float**| Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates (i.e. KineticEnergyGained/ChemicalEnergyConsumed). | [optional] |
| **decelerationEfficiency** | **Float**| Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates (i.e. ChemicalEnergySaved/KineticEnergyLost). | [optional] |
| **uphillEfficiency** | **Float**| Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation (i.e. PotentialEnergyGained/ChemicalEnergyConsumed). | [optional] |
| **downhillEfficiency** | **Float**| Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation (i.e. ChemicalEnergySaved/PotentialEnergyLost). | [optional] |
| **constantSpeedConsumptionInkWhPerHundredkm** | **String**| Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK: a route was calculated and the body of the response contains the route description and any other requested data. |  -  |
| **400** | Bad request: one or more parameters were incorrectly specified, are mutually exclusive, the points in the request are not connected by the road network or the points in the request are not near enough to a road. |  -  |
| **403** | Permission, capacity, or authentication issues:   - Forbidden   - Not authorized   - Account inactive   - Account over queries per second limit   - Account over rate limit   - Rate limit exceeded |  -  |
| **404** | Not Found: the requested resource could not be found, but it may be available again in the future. |  -  |
| **405** | Method Not Allowed: the client used a HTTP method other than GET or POST. |  -  |
| **408** | Request timeout. |  -  |
| **414** | Requested uri is too long. |  -  |
| **500** | An error occurred while processing the request. Please try again later. |  -  |
| **502** | Internal network connectivity issue. |  -  |
| **503** | Service currently unavailable. |  -  |
| **504** | Internal network connectivity issue or a request that has taken too long to complete. |  -  |
| **596** | Service not found. |  -  |

<a id="routingVersionNumberCalculateRouteLocationsContentTypePost"></a>
# **routingVersionNumberCalculateRouteLocationsContentTypePost**
> routingVersionNumberCalculateRouteLocationsContentTypePost(versionNumber, locations, contentType, maxAlternatives, alternativeType, minDeviationDistance, minDeviationTime, instructionsType, language, computeBestOrder, routeRepresentation, computeTravelTimeFor, vehicleHeading, sectionType, paramCallback, report, departAt, arriveAt, routeType, traffic, avoid, travelMode, hilliness, windingness, vehicleMaxSpeed, vehicleWeight, vehicleAxleWeight, vehicleLength, vehicleWidth, vehicleHeight, vehicleCommercial, vehicleLoadType, vehicleEngineType, constantSpeedConsumptionInLitersPerHundredkm, currentFuelInLiters, auxiliaryPowerInLitersPerHour, fuelEnergyDensityInMJoulesPerLiter, accelerationEfficiency, decelerationEfficiency, uphillEfficiency, downhillEfficiency, constantSpeedConsumptionInkWhPerHundredkm, calculateRoutePostDataParameters)

Calculate Route

Calculates a route between an origin and a destination. POST method handles additionally parameters: &lt;em&gt;supportingPoints&lt;/em&gt;, &lt;em&gt;allowVignette&lt;/em&gt;, &lt;em&gt;avoidVignette&lt;/em&gt;, &lt;em&gt;avoidAreas&lt;/em&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.tomtom.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RoutingApi apiInstance = new RoutingApi(defaultClient);
    Integer versionNumber = 1; // Integer | Service version number. The current value is 1.
    String locations = "52.50931,13.42936:52.50274,13.43872"; // String | Locations through which the calculated route must pass.
    String contentType = "xml"; // String | The content type of the response structure. If the content type is jsonp, a callback method can be specified in the query parameters.
    Integer maxAlternatives = 0; // Integer | Number of alternative routes to be calculated.
    String alternativeType = "anyRoute"; // String | Determines whether the alternative routes to be calculated should be better with respect to the planning criteria provided than the reference route.
    Integer minDeviationDistance = 0; // Integer | All alternative routes will follow the reference route for the specified minimum number of meters starting from the origin point.
    Integer minDeviationTime = 0; // Integer | All alternative routes will follow the reference route for the specified minimum number of seconds starting from the origin point.
    String instructionsType = "coded"; // String | If specified, guidance instructions will be returned (if available).
    String language = "en-GB"; // String | The language parameter determines the language of the guidance messages.
    Boolean computeBestOrder = false; // Boolean | Re-order the route waypoints to reduce the route length.
    String routeRepresentation = "polyline"; // String | Specifies the representation of the set of routes provided as a response.
    String computeTravelTimeFor = "none"; // String | Specifies whether to return additional travel times using different types of traffic information (none, historic, live) as well as the default best-estimate travel time.
    Integer vehicleHeading = 56; // Integer | The directional heading of the vehicle in degrees. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.).
    String sectionType = "travelMode"; // String | Specifies which section types are explicitly reported in the route response. Can be specified multiple times.   - carTrain, ferry, tunnel or motorway   - pedestrian   - tollRoad   - tollVignette   - country   - travelMode   - traffic
    String paramCallback = "callback"; // String | Specifies the jsonp callback method.
    String report = "effectiveSettings"; // String | Specifies which data should be reported for diagnosis purposes.
    String departAt = "now"; // String | The date and time of departure from the origin point. Departure times apart from <i>now</i> must be specified as a dateTime.
    String arriveAt = "arriveAt_example"; // String | The date and time of arrival at the destination point. It must be specified as a dateTime.
    String routeType = "fastest"; // String | The type of route requested.
    Boolean traffic = true; // Boolean | Determines whether current traffic is used in route calculations. Note that information on historic road speeds is always used.
    String avoid = "unpavedRoads"; // String | Specifies whether the routing engine should try to avoid specific types of road segment when calculating the route. Can be specified multiple times. Possible values:   - tollRoads   - motorways   - ferries   - unpavedRoads   - carpools   - alreadyUsedRoads
    String travelMode = "car"; // String | The mode of travel for the requested route.
    String hilliness = "low"; // String | Degree of hilliness for calculating a thrilling route.
    String windingness = "low"; // String | Amount that a thrilling route should wind.
    Integer vehicleMaxSpeed = 0; // Integer | Maximum speed of the vehicle in km/hour.
    Integer vehicleWeight = 0; // Integer | Weight of the vehicle in kilograms.
    Integer vehicleAxleWeight = 0; // Integer | Weight per axle of the vehicle in kg.
    Float vehicleLength = 0F; // Float | Length of the vehicle in meters.
    Float vehicleWidth = 0F; // Float | Width of the vehicle in meters.
    Float vehicleHeight = 0F; // Float | Height of the vehicle in meters.
    Boolean vehicleCommercial = false; // Boolean | Indicates that the vehicle is used for commercial purposes. This means it may not be allowed on certain roads.
    String vehicleLoadType = "vehicleLoadType_example"; // String | Indicates what kinds of hazardous materials the vehicle is carrying (if any). This means it may not be allowed on certain roads. Use these for routing in the US:    - <i>USHazmatClass1</i> Explosives   - <i>USHazmatClass2</i> Compressed gas   - <i>USHazmatClass3</i> Flammable liquids   - <i>USHazmatClass4</i> Flammable solids   - <i>USHazmatClass5</i> Oxidizers   - <i>USHazmatClass6</i> Poisons   - <i>USHazmatClass7</i> Radioactive   - <i>USHazmatClass8</i> Corrosives   - <i>USHazmatClass9</i> Miscellaneous  Use these for routing in all other countries:    - <i>otherHazmatExplosive</i> Explosives   - <i>otherHazmatGeneral</i> Miscellaneous   - <i>otherHazmatHarmfulToWater</i> Harmful to water  vehicleLoadType can be specified multiple times. This parameter is currently only considered for <b>travelMode</b>=<i>truck</i>.
    String vehicleEngineType = "combustion"; // String | Engine type of the vehicle.
    String constantSpeedConsumptionInLitersPerHundredkm = "constantSpeedConsumptionInLitersPerHundredkm_example"; // String | Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
    Float currentFuelInLiters = 3.4F; // Float | Specifies the current supply of fuel in liters.
    Float auxiliaryPowerInLitersPerHour = 3.4F; // Float | Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour.
    Float fuelEnergyDensityInMJoulesPerLiter = 3.4F; // Float | Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ).
    Float accelerationEfficiency = 3.4F; // Float | Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates (i.e. KineticEnergyGained/ChemicalEnergyConsumed).
    Float decelerationEfficiency = 3.4F; // Float | Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates (i.e. ChemicalEnergySaved/KineticEnergyLost).
    Float uphillEfficiency = 3.4F; // Float | Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation (i.e. PotentialEnergyGained/ChemicalEnergyConsumed).
    Float downhillEfficiency = 3.4F; // Float | Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation (i.e. ChemicalEnergySaved/PotentialEnergyLost).
    String constantSpeedConsumptionInkWhPerHundredkm = "constantSpeedConsumptionInkWhPerHundredkm_example"; // String | Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs.
    CalculateRoutePostDataParameters calculateRoutePostDataParameters = new CalculateRoutePostDataParameters(); // CalculateRoutePostDataParameters | 
    try {
      apiInstance.routingVersionNumberCalculateRouteLocationsContentTypePost(versionNumber, locations, contentType, maxAlternatives, alternativeType, minDeviationDistance, minDeviationTime, instructionsType, language, computeBestOrder, routeRepresentation, computeTravelTimeFor, vehicleHeading, sectionType, paramCallback, report, departAt, arriveAt, routeType, traffic, avoid, travelMode, hilliness, windingness, vehicleMaxSpeed, vehicleWeight, vehicleAxleWeight, vehicleLength, vehicleWidth, vehicleHeight, vehicleCommercial, vehicleLoadType, vehicleEngineType, constantSpeedConsumptionInLitersPerHundredkm, currentFuelInLiters, auxiliaryPowerInLitersPerHour, fuelEnergyDensityInMJoulesPerLiter, accelerationEfficiency, decelerationEfficiency, uphillEfficiency, downhillEfficiency, constantSpeedConsumptionInkWhPerHundredkm, calculateRoutePostDataParameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutingApi#routingVersionNumberCalculateRouteLocationsContentTypePost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **versionNumber** | **Integer**| Service version number. The current value is 1. | [enum: 1] |
| **locations** | **String**| Locations through which the calculated route must pass. | |
| **contentType** | **String**| The content type of the response structure. If the content type is jsonp, a callback method can be specified in the query parameters. | [default to xml] [enum: xml, json, jsonp] |
| **maxAlternatives** | **Integer**| Number of alternative routes to be calculated. | [optional] [default to 0] |
| **alternativeType** | **String**| Determines whether the alternative routes to be calculated should be better with respect to the planning criteria provided than the reference route. | [optional] [default to anyRoute] [enum: anyRoute, betterRoute] |
| **minDeviationDistance** | **Integer**| All alternative routes will follow the reference route for the specified minimum number of meters starting from the origin point. | [optional] [default to 0] |
| **minDeviationTime** | **Integer**| All alternative routes will follow the reference route for the specified minimum number of seconds starting from the origin point. | [optional] [default to 0] |
| **instructionsType** | **String**| If specified, guidance instructions will be returned (if available). | [optional] [enum: coded, text, tagged] |
| **language** | **String**| The language parameter determines the language of the guidance messages. | [optional] [default to en-GB] |
| **computeBestOrder** | **Boolean**| Re-order the route waypoints to reduce the route length. | [optional] [default to false] |
| **routeRepresentation** | **String**| Specifies the representation of the set of routes provided as a response. | [optional] [default to polyline] [enum: polyline, none] |
| **computeTravelTimeFor** | **String**| Specifies whether to return additional travel times using different types of traffic information (none, historic, live) as well as the default best-estimate travel time. | [optional] [default to none] [enum: none, all] |
| **vehicleHeading** | **Integer**| The directional heading of the vehicle in degrees. Entered in degrees, measured clockwise from north (so north is 0, east is 90, etc.). | [optional] |
| **sectionType** | **String**| Specifies which section types are explicitly reported in the route response. Can be specified multiple times.   - carTrain, ferry, tunnel or motorway   - pedestrian   - tollRoad   - tollVignette   - country   - travelMode   - traffic | [optional] [default to travelMode] |
| **paramCallback** | **String**| Specifies the jsonp callback method. | [optional] [default to callback] |
| **report** | **String**| Specifies which data should be reported for diagnosis purposes. | [optional] [enum: effectiveSettings] |
| **departAt** | **String**| The date and time of departure from the origin point. Departure times apart from &lt;i&gt;now&lt;/i&gt; must be specified as a dateTime. | [optional] [default to now] |
| **arriveAt** | **String**| The date and time of arrival at the destination point. It must be specified as a dateTime. | [optional] |
| **routeType** | **String**| The type of route requested. | [optional] [default to fastest] [enum: fastest, shortest, eco, thrilling] |
| **traffic** | **Boolean**| Determines whether current traffic is used in route calculations. Note that information on historic road speeds is always used. | [optional] [default to true] |
| **avoid** | **String**| Specifies whether the routing engine should try to avoid specific types of road segment when calculating the route. Can be specified multiple times. Possible values:   - tollRoads   - motorways   - ferries   - unpavedRoads   - carpools   - alreadyUsedRoads | [optional] |
| **travelMode** | **String**| The mode of travel for the requested route. | [optional] [default to car] [enum: car, truck, taxi, bus, van, motorcycle, bicycle, pedestrian] |
| **hilliness** | **String**| Degree of hilliness for calculating a thrilling route. | [optional] [default to normal] [enum: low, normal, high] |
| **windingness** | **String**| Amount that a thrilling route should wind. | [optional] [default to normal] [enum: low, normal, high] |
| **vehicleMaxSpeed** | **Integer**| Maximum speed of the vehicle in km/hour. | [optional] [default to 0] |
| **vehicleWeight** | **Integer**| Weight of the vehicle in kilograms. | [optional] [default to 0] |
| **vehicleAxleWeight** | **Integer**| Weight per axle of the vehicle in kg. | [optional] [default to 0] |
| **vehicleLength** | **Float**| Length of the vehicle in meters. | [optional] [default to 0] |
| **vehicleWidth** | **Float**| Width of the vehicle in meters. | [optional] [default to 0] |
| **vehicleHeight** | **Float**| Height of the vehicle in meters. | [optional] [default to 0] |
| **vehicleCommercial** | **Boolean**| Indicates that the vehicle is used for commercial purposes. This means it may not be allowed on certain roads. | [optional] [default to false] |
| **vehicleLoadType** | **String**| Indicates what kinds of hazardous materials the vehicle is carrying (if any). This means it may not be allowed on certain roads. Use these for routing in the US:    - &lt;i&gt;USHazmatClass1&lt;/i&gt; Explosives   - &lt;i&gt;USHazmatClass2&lt;/i&gt; Compressed gas   - &lt;i&gt;USHazmatClass3&lt;/i&gt; Flammable liquids   - &lt;i&gt;USHazmatClass4&lt;/i&gt; Flammable solids   - &lt;i&gt;USHazmatClass5&lt;/i&gt; Oxidizers   - &lt;i&gt;USHazmatClass6&lt;/i&gt; Poisons   - &lt;i&gt;USHazmatClass7&lt;/i&gt; Radioactive   - &lt;i&gt;USHazmatClass8&lt;/i&gt; Corrosives   - &lt;i&gt;USHazmatClass9&lt;/i&gt; Miscellaneous  Use these for routing in all other countries:    - &lt;i&gt;otherHazmatExplosive&lt;/i&gt; Explosives   - &lt;i&gt;otherHazmatGeneral&lt;/i&gt; Miscellaneous   - &lt;i&gt;otherHazmatHarmfulToWater&lt;/i&gt; Harmful to water  vehicleLoadType can be specified multiple times. This parameter is currently only considered for &lt;b&gt;travelMode&lt;/b&gt;&#x3D;&lt;i&gt;truck&lt;/i&gt;. | [optional] |
| **vehicleEngineType** | **String**| Engine type of the vehicle. | [optional] [default to combustion] [enum: combustion, electric] |
| **constantSpeedConsumptionInLitersPerHundredkm** | **String**| Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs. | [optional] |
| **currentFuelInLiters** | **Float**| Specifies the current supply of fuel in liters. | [optional] |
| **auxiliaryPowerInLitersPerHour** | **Float**| Specifies the amount of fuel consumed for sustaining auxiliary systems of the vehicle, in liters per hour. | [optional] |
| **fuelEnergyDensityInMJoulesPerLiter** | **Float**| Specifies the amount of chemical energy stored in one liter of fuel in megajoules (MJ). | [optional] |
| **accelerationEfficiency** | **Float**| Specifies the efficiency of converting chemical energy stored in fuel to kinetic energy when the vehicle accelerates (i.e. KineticEnergyGained/ChemicalEnergyConsumed). | [optional] |
| **decelerationEfficiency** | **Float**| Specifies the efficiency of converting kinetic energy to saved (not consumed) fuel when the vehicle decelerates (i.e. ChemicalEnergySaved/KineticEnergyLost). | [optional] |
| **uphillEfficiency** | **Float**| Specifies the efficiency of converting chemical energy stored in fuel to potential energy when the vehicle gains elevation (i.e. PotentialEnergyGained/ChemicalEnergyConsumed). | [optional] |
| **downhillEfficiency** | **Float**| Specifies the efficiency of converting potential energy to saved (not consumed) fuel when the vehicle loses elevation (i.e. ChemicalEnergySaved/PotentialEnergyLost). | [optional] |
| **constantSpeedConsumptionInkWhPerHundredkm** | **String**| Specifies the speed-dependent component of consumption. Provided as an unordered list of speed/consumption-rate pairs. | [optional] |
| **calculateRoutePostDataParameters** | [**CalculateRoutePostDataParameters**](CalculateRoutePostDataParameters.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK: a route was calculated and the body of the response contains the route description and any other requested data. |  -  |
| **400** | Bad request: one or more parameters were incorrectly specified, are mutually exclusive, the points in the request are not connected by the road network or the points in the request are not near enough to a road. |  -  |
| **403** | Permission, capacity, or authentication issues:   - Forbidden   - Not authorized   - Account inactive   - Account over queries per second limit   - Account over rate limit   - Rate limit exceeded |  -  |
| **404** | Not Found: the requested resource could not be found, but it may be available again in the future. |  -  |
| **405** | Method Not Allowed: the client used a HTTP method other than GET or POST. |  -  |
| **408** | Request timeout. |  -  |
| **414** | Requested uri is too long. |  -  |
| **500** | An error occurred while processing the request. Please try again later. |  -  |
| **502** | Internal network connectivity issue. |  -  |
| **503** | Service currently unavailable. |  -  |
| **504** | Internal network connectivity issue or a request that has taken too long to complete. |  -  |
| **596** | Service not found. |  -  |

