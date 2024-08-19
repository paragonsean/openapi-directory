# EDrvApi.VehiclesApi

All URIs are relative to *http://api.edrv.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getVehicle**](VehiclesApi.md#getVehicle) | **GET** /v1/vehicles/{id} | 
[**getVehicleBattery**](VehiclesApi.md#getVehicleBattery) | **GET** /v1/vehicles/{id}/battery | 
[**getVehicleCharge**](VehiclesApi.md#getVehicleCharge) | **GET** /v1/vehicles/{id}/charge | 
[**getVehicleLocation**](VehiclesApi.md#getVehicleLocation) | **GET** /v1/vehicles/{id}/location | 
[**getVehicleOdometer**](VehiclesApi.md#getVehicleOdometer) | **GET** /v1/vehicles/{id}/odometer | 
[**getVehicles**](VehiclesApi.md#getVehicles) | **GET** /v1/vehicles | 
[**postCharge**](VehiclesApi.md#postCharge) | **POST** /v1/vehicles/{id}/charge | 



## getVehicle

> getVehicle(id, opts)



Get a vehicle&#39;s data

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.VehiclesApi();
let id = "id_example"; // String | The vehicule id that needs to be fetched
let opts = {
  'includeDriver': true, // Boolean | Populate driver
  'includeToken': true, // Boolean | Populate token
  'includeOrganization': true // Boolean | Populate organization
};
apiInstance.getVehicle(id, opts, (error, data, response) => {
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
 **id** | **String**| The vehicule id that needs to be fetched | 
 **includeDriver** | **Boolean**| Populate driver | [optional] 
 **includeToken** | **Boolean**| Populate token | [optional] 
 **includeOrganization** | **Boolean**| Populate organization | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getVehicleBattery

> getVehicleBattery(id)



Get a vehicle&#39;s battery

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.VehiclesApi();
let id = "id_example"; // String | The vehicle id that needs to be fetched
apiInstance.getVehicleBattery(id, (error, data, response) => {
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
 **id** | **String**| The vehicle id that needs to be fetched | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getVehicleCharge

> getVehicleCharge(id)



Get a vehicle&#39;s charge

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.VehiclesApi();
let id = "id_example"; // String | The vehicle id that needs to be fetched
apiInstance.getVehicleCharge(id, (error, data, response) => {
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
 **id** | **String**| The vehicle id that needs to be fetched | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getVehicleLocation

> getVehicleLocation(id)



Get a vehicle&#39;s location

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.VehiclesApi();
let id = "id_example"; // String | The vehicle id that needs to be fetched
apiInstance.getVehicleLocation(id, (error, data, response) => {
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
 **id** | **String**| The vehicle id that needs to be fetched | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getVehicleOdometer

> getVehicleOdometer(id)



Get a vehicle&#39;s odometer

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.VehiclesApi();
let id = "id_example"; // String | The vehicle id that needs to be fetched
apiInstance.getVehicleOdometer(id, (error, data, response) => {
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
 **id** | **String**| The vehicle id that needs to be fetched | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getVehicles

> GetDrivers200Response getVehicles(opts)



List all vehicles

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.VehiclesApi();
let opts = {
  'active': true, // Boolean | Get a list of active vehicles
  'paginateLimit': 20, // Number | Number of results per page
  'paginatePage': "paginatePage_example", // String | The queried page index
  'paginateEnabled': true, // Boolean | Enable pagination
  'sortBy': "'createdAt'", // String | Sort data by this key
  'sortOrder': "'desc'", // String | asc to sort ascending (default is desc - descending)
  'createdAtGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'createdAtLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'updatedAtGte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'updatedAtLte': new Date("2013-10-20T19:20:30+01:00"), // Date | Date as ISO String
  'includeDriver': true, // Boolean | Populate driver
  'includeToken': true, // Boolean | Populate token
  'includeOrganization': true // Boolean | Populate organization
};
apiInstance.getVehicles(opts, (error, data, response) => {
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
 **active** | **Boolean**| Get a list of active vehicles | [optional] 
 **paginateLimit** | **Number**| Number of results per page | [optional] [default to 20]
 **paginatePage** | **String**| The queried page index | [optional] 
 **paginateEnabled** | **Boolean**| Enable pagination | [optional] [default to true]
 **sortBy** | **String**| Sort data by this key | [optional] [default to &#39;createdAt&#39;]
 **sortOrder** | **String**| asc to sort ascending (default is desc - descending) | [optional] [default to &#39;desc&#39;]
 **createdAtGte** | **Date**| Date as ISO String | [optional] 
 **createdAtLte** | **Date**| Date as ISO String | [optional] 
 **updatedAtGte** | **Date**| Date as ISO String | [optional] 
 **updatedAtLte** | **Date**| Date as ISO String | [optional] 
 **includeDriver** | **Boolean**| Populate driver | [optional] 
 **includeToken** | **Boolean**| Populate token | [optional] 
 **includeOrganization** | **Boolean**| Populate organization | [optional] 

### Return type

[**GetDrivers200Response**](GetDrivers200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postCharge

> PatchChargeStation200Response postCharge(id, postChargeRequest)



Change charge

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.VehiclesApi();
let id = "id_example"; // String | The vehicle id that needs to be fetched
let postChargeRequest = new EDrvApi.PostChargeRequest(); // PostChargeRequest | Include command properties to send here
apiInstance.postCharge(id, postChargeRequest, (error, data, response) => {
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
 **id** | **String**| The vehicle id that needs to be fetched | 
 **postChargeRequest** | [**PostChargeRequest**](PostChargeRequest.md)| Include command properties to send here | 

### Return type

[**PatchChargeStation200Response**](PatchChargeStation200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

