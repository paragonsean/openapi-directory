# TurbineLabsApi.ZoneApi

All URIs are relative to *https://api.turbinelabs.io/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zoneGet**](ZoneApi.md#zoneGet) | **GET** /zone | get a list of zones
[**zonePost**](ZoneApi.md#zonePost) | **POST** /zone | create zone
[**zoneZoneKeyDelete**](ZoneApi.md#zoneZoneKeyDelete) | **DELETE** /zone/{zoneKey} | delete zone
[**zoneZoneKeyGet**](ZoneApi.md#zoneZoneKeyGet) | **GET** /zone/{zoneKey} | get zone



## zoneGet

> MultiZoneResult zoneGet(opts)

get a list of zones

Get all zones. possibly with filters 

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.ZoneApi();
let opts = {
  'filters': "filters_example" // String | A JSON encoded array of ZoneFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ZoneFilter will be included. 
};
apiInstance.zoneGet(opts, (error, data, response) => {
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
 **filters** | **String**| A JSON encoded array of ZoneFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ZoneFilter will be included.  | [optional] 

### Return type

[**MultiZoneResult**](MultiZoneResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## zonePost

> ZoneResult zonePost(zone)

create zone

Create a new zone. 

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.ZoneApi();
let zone = new TurbineLabsApi.ZoneCreate(); // ZoneCreate | the zone to create
apiInstance.zonePost(zone, (error, data, response) => {
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
 **zone** | [**ZoneCreate**](ZoneCreate.md)| the zone to create | 

### Return type

[**ZoneResult**](ZoneResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## zoneZoneKeyDelete

> Object zoneZoneKeyDelete(zoneKey, checksum)

delete zone

Delete a zone. 

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.ZoneApi();
let zoneKey = "9cd24183-f848-48f8-6f55-0f0724070000"; // String | the zone key
let checksum = "9cd24183-f848-48f8-6f55-0f07240700b9"; // String | the current checksum of the zone to be deleted
apiInstance.zoneZoneKeyDelete(zoneKey, checksum, (error, data, response) => {
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
 **zoneKey** | **String**| the zone key | 
 **checksum** | **String**| the current checksum of the zone to be deleted | 

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## zoneZoneKeyGet

> ZoneResult zoneZoneKeyGet(zoneKey)

get zone

Get details for a single zone 

### Example

```javascript
import TurbineLabsApi from 'turbine_labs_api';
let defaultClient = TurbineLabsApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new TurbineLabsApi.ZoneApi();
let zoneKey = "9cd24183-f848-48f8-6f55-0f0724070000"; // String | the zone key
apiInstance.zoneZoneKeyGet(zoneKey, (error, data, response) => {
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
 **zoneKey** | **String**| the zone key | 

### Return type

[**ZoneResult**](ZoneResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

