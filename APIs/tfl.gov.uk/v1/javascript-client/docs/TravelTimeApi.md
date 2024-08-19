# TransportForLondonUnifiedApi.TravelTimeApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**travelTimeGetCompareOverlay**](TravelTimeApi.md#travelTimeGetCompareOverlay) | **GET** /TravelTimes/compareOverlay/{z}/mapcenter/{mapCenterLat}/{mapCenterLon}/pinlocation/{pinLat}/{pinLon}/dimensions/{width}/{height} | Gets the TravelTime overlay.
[**travelTimeGetOverlay**](TravelTimeApi.md#travelTimeGetOverlay) | **GET** /TravelTimes/overlay/{z}/mapcenter/{mapCenterLat}/{mapCenterLon}/pinlocation/{pinLat}/{pinLon}/dimensions/{width}/{height} | Gets the TravelTime overlay.



## travelTimeGetCompareOverlay

> Object travelTimeGetCompareOverlay(z, pinLat, pinLon, mapCenterLat, mapCenterLon, scenarioTitle, timeOfDayId, modeId, width, height, direction, travelTimeInterval, compareType, compareValue)

Gets the TravelTime overlay.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.TravelTimeApi();
let z = 56; // Number | The zoom level.
let pinLat = 3.4; // Number | The latitude of the pin.
let pinLon = 3.4; // Number | The longitude of the pin.
let mapCenterLat = 3.4; // Number | The map center latitude.
let mapCenterLon = 3.4; // Number | The map center longitude.
let scenarioTitle = "scenarioTitle_example"; // String | The title of the scenario.
let timeOfDayId = "timeOfDayId_example"; // String | The id for the time of day (AM/INTER/PM)
let modeId = "modeId_example"; // String | The id of the mode.
let width = 56; // Number | The width of the requested overlay.
let height = 56; // Number | The height of the requested overlay.
let direction = "direction_example"; // String | The direction of travel.
let travelTimeInterval = 56; // Number | The total minutes between the travel time bands
let compareType = "compareType_example"; // String | 
let compareValue = "compareValue_example"; // String | 
apiInstance.travelTimeGetCompareOverlay(z, pinLat, pinLon, mapCenterLat, mapCenterLon, scenarioTitle, timeOfDayId, modeId, width, height, direction, travelTimeInterval, compareType, compareValue, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **z** | **Number**| The zoom level. | 
 **pinLat** | **Number**| The latitude of the pin. | 
 **pinLon** | **Number**| The longitude of the pin. | 
 **mapCenterLat** | **Number**| The map center latitude. | 
 **mapCenterLon** | **Number**| The map center longitude. | 
 **scenarioTitle** | **String**| The title of the scenario. | 
 **timeOfDayId** | **String**| The id for the time of day (AM/INTER/PM) | 
 **modeId** | **String**| The id of the mode. | 
 **width** | **Number**| The width of the requested overlay. | 
 **height** | **Number**| The height of the requested overlay. | 
 **direction** | **String**| The direction of travel. | 
 **travelTimeInterval** | **Number**| The total minutes between the travel time bands | 
 **compareType** | **String**|  | 
 **compareValue** | **String**|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## travelTimeGetOverlay

> Object travelTimeGetOverlay(z, pinLat, pinLon, mapCenterLat, mapCenterLon, scenarioTitle, timeOfDayId, modeId, width, height, direction, travelTimeInterval)

Gets the TravelTime overlay.

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.TravelTimeApi();
let z = 56; // Number | The zoom level.
let pinLat = 3.4; // Number | The latitude of the pin.
let pinLon = 3.4; // Number | The longitude of the pin.
let mapCenterLat = 3.4; // Number | The map center latitude.
let mapCenterLon = 3.4; // Number | The map center longitude.
let scenarioTitle = "scenarioTitle_example"; // String | The title of the scenario.
let timeOfDayId = "timeOfDayId_example"; // String | The id for the time of day (AM/INTER/PM)
let modeId = "modeId_example"; // String | The id of the mode.
let width = 56; // Number | The width of the requested overlay.
let height = 56; // Number | The height of the requested overlay.
let direction = "direction_example"; // String | The direction of travel.
let travelTimeInterval = 56; // Number | The total minutes between the travel time bands
apiInstance.travelTimeGetOverlay(z, pinLat, pinLon, mapCenterLat, mapCenterLon, scenarioTitle, timeOfDayId, modeId, width, height, direction, travelTimeInterval, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **z** | **Number**| The zoom level. | 
 **pinLat** | **Number**| The latitude of the pin. | 
 **pinLon** | **Number**| The longitude of the pin. | 
 **mapCenterLat** | **Number**| The map center latitude. | 
 **mapCenterLon** | **Number**| The map center longitude. | 
 **scenarioTitle** | **String**| The title of the scenario. | 
 **timeOfDayId** | **String**| The id for the time of day (AM/INTER/PM) | 
 **modeId** | **String**| The id of the mode. | 
 **width** | **Number**| The width of the requested overlay. | 
 **height** | **Number**| The height of the requested overlay. | 
 **direction** | **String**| The direction of travel. | 
 **travelTimeInterval** | **Number**| The total minutes between the travel time bands | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

