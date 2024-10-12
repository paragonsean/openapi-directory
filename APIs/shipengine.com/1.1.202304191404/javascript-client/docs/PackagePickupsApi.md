# ShipEngineApi.PackagePickupsApi

All URIs are relative to *https://api.shipengine.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteScheduledPickup**](PackagePickupsApi.md#deleteScheduledPickup) | **DELETE** /v1/pickups/{pickup_id} | Delete a Scheduled Pickup
[**getPickupById**](PackagePickupsApi.md#getPickupById) | **GET** /v1/pickups/{pickup_id} | Get Pickup By ID
[**listScheduledPickups**](PackagePickupsApi.md#listScheduledPickups) | **GET** /v1/pickups | List Scheduled Pickups
[**schedulePickup**](PackagePickupsApi.md#schedulePickup) | **POST** /v1/pickups | Schedule a Pickup



## deleteScheduledPickup

> DeletePickupByIdResponseBody deleteScheduledPickup(pickupId)

Delete a Scheduled Pickup

Delete a previously-scheduled pickup by ID

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.PackagePickupsApi();
let pickupId = "pickupId_example"; // String | 
apiInstance.deleteScheduledPickup(pickupId, (error, data, response) => {
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
 **pickupId** | **String**|  | 

### Return type

[**DeletePickupByIdResponseBody**](DeletePickupByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPickupById

> GetPickupByIdResponseBody getPickupById(pickupId)

Get Pickup By ID

Get Pickup By ID

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.PackagePickupsApi();
let pickupId = "pickupId_example"; // String | 
apiInstance.getPickupById(pickupId, (error, data, response) => {
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
 **pickupId** | **String**|  | 

### Return type

[**GetPickupByIdResponseBody**](GetPickupByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listScheduledPickups

> GetPickupsResponseBody listScheduledPickups(opts)

List Scheduled Pickups

List all pickups that have been scheduled for this carrier

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.PackagePickupsApi();
let opts = {
  'carrierId': "carrierId_example", // String | Carrier ID
  'warehouseId': "warehouseId_example", // String | Warehouse ID
  'createdAtStart': new Date("2019-03-12T19:24:13.657Z"), // Date | Only return scheduled pickups that were created on or after a specific date/time
  'createdAtEnd': new Date("2019-03-12T19:24:13.657Z"), // Date | Only return scheduled pickups that were created on or before a specific date/time
  'page': 2, // Number | Return a specific page of results. Defaults to the first page. If set to a number that's greater than the number of pages of results, an empty page is returned. 
  'pageSize': 50 // Number | The number of results to return per response.
};
apiInstance.listScheduledPickups(opts, (error, data, response) => {
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
 **carrierId** | **String**| Carrier ID | [optional] 
 **warehouseId** | **String**| Warehouse ID | [optional] 
 **createdAtStart** | **Date**| Only return scheduled pickups that were created on or after a specific date/time | [optional] 
 **createdAtEnd** | **Date**| Only return scheduled pickups that were created on or before a specific date/time | [optional] 
 **page** | **Number**| Return a specific page of results. Defaults to the first page. If set to a number that&#39;s greater than the number of pages of results, an empty page is returned.  | [optional] [default to 1]
 **pageSize** | **Number**| The number of results to return per response. | [optional] [default to 25]

### Return type

[**GetPickupsResponseBody**](GetPickupsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulePickup

> SchedulePickupResponseBody schedulePickup(schedulePickupRequestBody)

Schedule a Pickup

Schedule a package pickup with a carrier

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.PackagePickupsApi();
let schedulePickupRequestBody = new ShipEngineApi.SchedulePickupRequestBody(); // SchedulePickupRequestBody | 
apiInstance.schedulePickup(schedulePickupRequestBody, (error, data, response) => {
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
 **schedulePickupRequestBody** | [**SchedulePickupRequestBody**](SchedulePickupRequestBody.md)|  | 

### Return type

[**SchedulePickupResponseBody**](SchedulePickupResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

