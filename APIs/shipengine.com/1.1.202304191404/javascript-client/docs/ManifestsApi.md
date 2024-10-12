# ShipEngineApi.ManifestsApi

All URIs are relative to *https://api.shipengine.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createManifest**](ManifestsApi.md#createManifest) | **POST** /v1/manifests | Create Manifest
[**getManifestById**](ManifestsApi.md#getManifestById) | **GET** /v1/manifests/{manifest_id} | Get Manifest By Id
[**getManifestRequestById**](ManifestsApi.md#getManifestRequestById) | **GET** /v1/manifests/requests/{manifest_request_id} | Get Manifest Request By Id
[**listManifests**](ManifestsApi.md#listManifests) | **GET** /v1/manifests | List Manifests



## createManifest

> CreateManifestResponseBody createManifest(createManifestRequestBody)

Create Manifest

Each ShipEngine manifest is created for a specific warehouse, so you&#39;ll need to provide the warehouse_id rather than the ship_from address. You can create a warehouse for each location that you want to create manifests for. 

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.ManifestsApi();
let createManifestRequestBody = new ShipEngineApi.CreateManifestRequestBody(); // CreateManifestRequestBody | 
apiInstance.createManifest(createManifestRequestBody, (error, data, response) => {
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
 **createManifestRequestBody** | [**CreateManifestRequestBody**](CreateManifestRequestBody.md)|  | 

### Return type

[**CreateManifestResponseBody**](CreateManifestResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getManifestById

> GetManifestByIdResponseBody getManifestById(manifestId)

Get Manifest By Id

Get Manifest By Id

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.ManifestsApi();
let manifestId = "manifestId_example"; // String | The Manifest Id
apiInstance.getManifestById(manifestId, (error, data, response) => {
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
 **manifestId** | **String**| The Manifest Id | 

### Return type

[**GetManifestByIdResponseBody**](GetManifestByIdResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getManifestRequestById

> CreateManifestResponseBody getManifestRequestById(manifestRequestId)

Get Manifest Request By Id

Get Manifest Request By Id

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.ManifestsApi();
let manifestRequestId = "manifestRequestId_example"; // String | The Manifest Request Id
apiInstance.getManifestRequestById(manifestRequestId, (error, data, response) => {
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
 **manifestRequestId** | **String**| The Manifest Request Id | 

### Return type

[**CreateManifestResponseBody**](CreateManifestResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listManifests

> ListManifestsResponseBody listManifests(opts)

List Manifests

Similar to querying shipments, we allow you to query manifests since there will likely be a large number over a long period of time.

### Example

```javascript
import ShipEngineApi from 'ship_engine_api';
let defaultClient = ShipEngineApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ShipEngineApi.ManifestsApi();
let opts = {
  'warehouseId': "warehouseId_example", // String | Warehouse ID
  'shipDateStart': new Date("2018-09-23T15:00:00.000Z"), // Date | ship date start range
  'shipDateEnd': new Date("2018-09-23T15:00:00.000Z"), // Date | ship date end range
  'createdAtStart': new Date("2019-03-12T19:24:13.657Z"), // Date | Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time)
  'createdAtEnd': new Date("2019-03-12T19:24:13.657Z"), // Date | Used to create a filter for when a resource was created, (ex. A shipment that was created before a certain time)
  'carrierId': "carrierId_example", // String | Carrier ID
  'page': 2, // Number | Return a specific page of results. Defaults to the first page. If set to a number that's greater than the number of pages of results, an empty page is returned. 
  'pageSize': 50, // Number | The number of results to return per response.
  'labelIds': ["se-28529731"] // [String] | 
};
apiInstance.listManifests(opts, (error, data, response) => {
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
 **warehouseId** | **String**| Warehouse ID | [optional] 
 **shipDateStart** | **Date**| ship date start range | [optional] 
 **shipDateEnd** | **Date**| ship date end range | [optional] 
 **createdAtStart** | **Date**| Used to create a filter for when a resource was created (ex. A shipment that was created after a certain time) | [optional] 
 **createdAtEnd** | **Date**| Used to create a filter for when a resource was created, (ex. A shipment that was created before a certain time) | [optional] 
 **carrierId** | **String**| Carrier ID | [optional] 
 **page** | **Number**| Return a specific page of results. Defaults to the first page. If set to a number that&#39;s greater than the number of pages of results, an empty page is returned.  | [optional] [default to 1]
 **pageSize** | **Number**| The number of results to return per response. | [optional] [default to 25]
 **labelIds** | [**[String]**](String.md)|  | [optional] 

### Return type

[**ListManifestsResponseBody**](ListManifestsResponseBody.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

