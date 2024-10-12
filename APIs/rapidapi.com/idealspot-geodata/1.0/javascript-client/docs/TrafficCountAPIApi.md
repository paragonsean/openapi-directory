# IdealSpotGeoData.TrafficCountAPIApi

All URIs are relative to *https://idealspot-geodata.p.rapidapi.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchNearestRoadSegments**](TrafficCountAPIApi.md#fetchNearestRoadSegments) | **GET** /traffic/roads/nearest/{latitude}/{longitude} | Fetch Nearest Road Segments
[**vehicleTrafficCountsforRoadSegment**](TrafficCountAPIApi.md#vehicleTrafficCountsforRoadSegment) | **GET** /traffic/counts/{segment_id} | Vehicle Traffic Counts for Road Segment



## fetchNearestRoadSegments

> SearchRoadSegments fetchNearestRoadSegments(n, latitude, longitude, xRapidAPIKey, xRapidAPIHost)

Fetch Nearest Road Segments

For given latitude and longitude, find &#x60;n&#x60; nearest road segments

### Example

```javascript
import IdealSpotGeoData from 'ideal_spot_geo_data';

let apiInstance = new IdealSpotGeoData.TrafficCountAPIApi();
let n = 56; // Number | Number of road segments to return (between 1 and 20)
let latitude = 3.4; // Number | (Required) Search coordinate latitude
let longitude = 3.4; // Number | (Required) Search coordinate longitude
let xRapidAPIKey = "xRapidAPIKey_example"; // String | (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata
let xRapidAPIHost = "xRapidAPIHost_example"; // String | 
apiInstance.fetchNearestRoadSegments(n, latitude, longitude, xRapidAPIKey, xRapidAPIHost, (error, data, response) => {
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
 **n** | **Number**| Number of road segments to return (between 1 and 20) | 
 **latitude** | **Number**| (Required) Search coordinate latitude | 
 **longitude** | **Number**| (Required) Search coordinate longitude | 
 **xRapidAPIKey** | **String**| (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata | 
 **xRapidAPIHost** | **String**|  | 

### Return type

[**SearchRoadSegments**](SearchRoadSegments.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## vehicleTrafficCountsforRoadSegment

> VehicleTrafficCountsforRoadSegment vehicleTrafficCountsforRoadSegment(segmentId, xRapidAPIKey, xRapidAPIHost)

Vehicle Traffic Counts for Road Segment

Time of day, day of week, and side of street vehicle traffic counts.

### Example

```javascript
import IdealSpotGeoData from 'ideal_spot_geo_data';

let apiInstance = new IdealSpotGeoData.TrafficCountAPIApi();
let segmentId = 56; // Number | (Required) Road segment ID. Fetched from Search Road Segments
let xRapidAPIKey = "xRapidAPIKey_example"; // String | (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata
let xRapidAPIHost = "xRapidAPIHost_example"; // String | 
apiInstance.vehicleTrafficCountsforRoadSegment(segmentId, xRapidAPIKey, xRapidAPIHost, (error, data, response) => {
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
 **segmentId** | **Number**| (Required) Road segment ID. Fetched from Search Road Segments | 
 **xRapidAPIKey** | **String**| (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata | 
 **xRapidAPIHost** | **String**|  | 

### Return type

[**VehicleTrafficCountsforRoadSegment**](VehicleTrafficCountsforRoadSegment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8

