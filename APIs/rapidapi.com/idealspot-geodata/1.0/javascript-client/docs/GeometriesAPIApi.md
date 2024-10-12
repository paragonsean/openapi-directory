# IdealSpotGeoData.GeometriesAPIApi

All URIs are relative to *https://idealspot-geodata.p.rapidapi.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchAdministrativeRegionsusingLatLng**](GeometriesAPIApi.md#fetchAdministrativeRegionsusingLatLng) | **GET** /geometries/regions/intersecting/{latitude}/{longitude} | Fetch Administrative Regions using Lat/Lng
[**fetchGeometries**](GeometriesAPIApi.md#fetchGeometries) | **GET** /geometries/geometry | Fetch Geometries



## fetchAdministrativeRegionsusingLatLng

> FetchAdministrativeRegionsusingLatLng fetchAdministrativeRegionsusingLatLng(latitude, longitude, xRapidAPIKey, xRapidAPIHost)

Fetch Administrative Regions using Lat/Lng

For given latitude and longitude, find intersecting administrative regions. Region polygons are simplified for web mapping.

### Example

```javascript
import IdealSpotGeoData from 'ideal_spot_geo_data';

let apiInstance = new IdealSpotGeoData.GeometriesAPIApi();
let latitude = 3.4; // Number | (Required) Search coordinate latitude
let longitude = 3.4; // Number | (Required) Search coordinate longitude
let xRapidAPIKey = "xRapidAPIKey_example"; // String | (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata
let xRapidAPIHost = "xRapidAPIHost_example"; // String | 
apiInstance.fetchAdministrativeRegionsusingLatLng(latitude, longitude, xRapidAPIKey, xRapidAPIHost, (error, data, response) => {
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
 **latitude** | **Number**| (Required) Search coordinate latitude | 
 **longitude** | **Number**| (Required) Search coordinate longitude | 
 **xRapidAPIKey** | **String**| (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata | 
 **xRapidAPIHost** | **String**|  | 

### Return type

[**FetchAdministrativeRegionsusingLatLng**](FetchAdministrativeRegionsusingLatLng.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## fetchGeometries

> Describetheregionwithin5minutedriveTimeofageographicpoint fetchGeometries(location, xRapidAPIKey, xRapidAPIHost)

Fetch Geometries

Fetch location GeoJSON

### Example

```javascript
import IdealSpotGeoData from 'ideal_spot_geo_data';

let apiInstance = new IdealSpotGeoData.GeometriesAPIApi();
let location = "location_example"; // String | (Required) Represents a buffer, region, or custom polygon specification. Accepts the `Location` model (as a `Buffer`, `Region`, or `Custom Polygon`) formatted as a JSON string. Multiple `location` query parameters are allowed. NOTE: When requesting multiple locations, you must include brackets(i.e. `?location[]=...&location[]=...`). If not included, only the last location will be used.
let xRapidAPIKey = "xRapidAPIKey_example"; // String | (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata
let xRapidAPIHost = "xRapidAPIHost_example"; // String | 
apiInstance.fetchGeometries(location, xRapidAPIKey, xRapidAPIHost, (error, data, response) => {
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
 **location** | **String**| (Required) Represents a buffer, region, or custom polygon specification. Accepts the &#x60;Location&#x60; model (as a &#x60;Buffer&#x60;, &#x60;Region&#x60;, or &#x60;Custom Polygon&#x60;) formatted as a JSON string. Multiple &#x60;location&#x60; query parameters are allowed. NOTE: When requesting multiple locations, you must include brackets(i.e. &#x60;?location[]&#x3D;...&amp;location[]&#x3D;...&#x60;). If not included, only the last location will be used. | 
 **xRapidAPIKey** | **String**| (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata | 
 **xRapidAPIHost** | **String**|  | 

### Return type

[**Describetheregionwithin5minutedriveTimeofageographicpoint**](Describetheregionwithin5minutedriveTimeofageographicpoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8

