# Apacta.DrivingTypesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkDeleteDrivingTypes**](DrivingTypesApi.md#bulkDeleteDrivingTypes) | **DELETE** /driving_types/bulkDelete | Bulk delete driving types
[**deleteDrivingTypesDrivingTypeId**](DrivingTypesApi.md#deleteDrivingTypesDrivingTypeId) | **DELETE** /driving_types/{driving_type_id} | Delete driving type
[**getDrivingTypes**](DrivingTypesApi.md#getDrivingTypes) | **GET** /driving_types | List the driving types of the company
[**getDrivingTypesDrivingTypeId**](DrivingTypesApi.md#getDrivingTypesDrivingTypeId) | **GET** /driving_types/{driving_type_id} | View driving type
[**postDrivingTypes**](DrivingTypesApi.md#postDrivingTypes) | **POST** /driving_types | Create driving type
[**putDrivingTypesDrivingTypeId**](DrivingTypesApi.md#putDrivingTypesDrivingTypeId) | **PUT** /driving_types/{driving_type_id} | Edit driving type



## bulkDeleteDrivingTypes

> EmptySuccessResponse bulkDeleteDrivingTypes(bulkActionRequestBody)

Bulk delete driving types

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.DrivingTypesApi();
let bulkActionRequestBody = new Apacta.BulkActionRequestBody(); // BulkActionRequestBody | Driving types ids
apiInstance.bulkDeleteDrivingTypes(bulkActionRequestBody, (error, data, response) => {
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
 **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| Driving types ids | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDrivingTypesDrivingTypeId

> EmptySuccessResponse deleteDrivingTypesDrivingTypeId(drivingTypeId)

Delete driving type

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.DrivingTypesApi();
let drivingTypeId = "drivingTypeId_example"; // String | 
apiInstance.deleteDrivingTypesDrivingTypeId(drivingTypeId, (error, data, response) => {
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
 **drivingTypeId** | **String**|  | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDrivingTypes

> GetDrivingTypes200Response getDrivingTypes(opts)

List the driving types of the company

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.DrivingTypesApi();
let opts = {
  'q': "q_example", // String | 
  'sort': "sort_example", // String | 
  'direction': "direction_example" // String | 
};
apiInstance.getDrivingTypes(opts, (error, data, response) => {
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
 **q** | **String**|  | [optional] 
 **sort** | **String**|  | [optional] 
 **direction** | **String**|  | [optional] 

### Return type

[**GetDrivingTypes200Response**](GetDrivingTypes200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDrivingTypesDrivingTypeId

> DrivingType getDrivingTypesDrivingTypeId(drivingTypeId, drivingTypeId2)

View driving type

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.DrivingTypesApi();
let drivingTypeId = "drivingTypeId_example"; // String | 
let drivingTypeId2 = "drivingTypeId_example"; // String | 
apiInstance.getDrivingTypesDrivingTypeId(drivingTypeId, drivingTypeId2, (error, data, response) => {
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
 **drivingTypeId** | **String**|  | 
 **drivingTypeId2** | **String**|  | 

### Return type

[**DrivingType**](DrivingType.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postDrivingTypes

> CreateSuccessResponse postDrivingTypes(opts)

Create driving type

### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.DrivingTypesApi();
let opts = {
  'postDrivingTypesRequest': new Apacta.PostDrivingTypesRequest() // PostDrivingTypesRequest | 
};
apiInstance.postDrivingTypes(opts, (error, data, response) => {
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
 **postDrivingTypesRequest** | [**PostDrivingTypesRequest**](PostDrivingTypesRequest.md)|  | [optional] 

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putDrivingTypesDrivingTypeId

> DrivingType putDrivingTypesDrivingTypeId(drivingTypeId)

Edit driving type



### Example

```javascript
import Apacta from 'apacta';

let apiInstance = new Apacta.DrivingTypesApi();
let drivingTypeId = "drivingTypeId_example"; // String | 
apiInstance.putDrivingTypesDrivingTypeId(drivingTypeId, (error, data, response) => {
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
 **drivingTypeId** | **String**|  | 

### Return type

[**DrivingType**](DrivingType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

