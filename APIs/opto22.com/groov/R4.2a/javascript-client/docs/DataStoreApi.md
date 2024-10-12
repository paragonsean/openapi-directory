# GroovViewPublicApi.DataStoreApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchReadTags**](DataStoreApi.md#batchReadTags) | **POST** /v1/data-store/read | 
[**listAllTags**](DataStoreApi.md#listAllTags) | **GET** /v1/data-store/tags | 
[**listDeviceTags**](DataStoreApi.md#listDeviceTags) | **GET** /v1/data-store/devices/{id}/tags | 
[**listDevices**](DataStoreApi.md#listDevices) | **GET** /v1/data-store/devices | 
[**readTag**](DataStoreApi.md#readTag) | **GET** /v1/data-store/read/{id} | 
[**writeTag**](DataStoreApi.md#writeTag) | **POST** /v1/data-store/write/{id} | 



## batchReadTags

> [TagValue] batchReadTags(tags)



Read selected tags from the data store. Authorized for admins and editors.

### Example

```javascript
import GroovViewPublicApi from 'groov_view_public_api';
let defaultClient = GroovViewPublicApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GroovViewPublicApi.DataStoreApi();
let tags = [new GroovViewPublicApi.TagReference()]; // [TagReference] | Tag references for the tags to read.
apiInstance.batchReadTags(tags, (error, data, response) => {
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
 **tags** | [**[TagReference]**](TagReference.md)| Tag references for the tags to read. | 

### Return type

[**[TagValue]**](TagValue.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAllTags

> [TagDefinition] listAllTags()



List all data store tags defined in the project. Authorized for admins and editors.

### Example

```javascript
import GroovViewPublicApi from 'groov_view_public_api';
let defaultClient = GroovViewPublicApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GroovViewPublicApi.DataStoreApi();
apiInstance.listAllTags((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[TagDefinition]**](TagDefinition.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDeviceTags

> [TagDefinition] listDeviceTags(id)



List tags of the given device. Authorized for admins and editors.

### Example

```javascript
import GroovViewPublicApi from 'groov_view_public_api';
let defaultClient = GroovViewPublicApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GroovViewPublicApi.DataStoreApi();
let id = 3.4; // Number | ID of the device to use.
apiInstance.listDeviceTags(id, (error, data, response) => {
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
 **id** | **Number**| ID of the device to use. | 

### Return type

[**[TagDefinition]**](TagDefinition.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDevices

> [DataStoreDevice] listDevices()



List devices available in the data store. Authorized for admins and editors.

### Example

```javascript
import GroovViewPublicApi from 'groov_view_public_api';
let defaultClient = GroovViewPublicApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GroovViewPublicApi.DataStoreApi();
apiInstance.listDevices((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[DataStoreDevice]**](DataStoreDevice.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## readTag

> TagValue readTag(id, opts)



Read the current value of a single tag. Authorized for admins and editors.

### Example

```javascript
import GroovViewPublicApi from 'groov_view_public_api';
let defaultClient = GroovViewPublicApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GroovViewPublicApi.DataStoreApi();
let id = 3.4; // Number | ID of the tag to read.
let opts = {
  'index': 0.0, // Number | Table index to start reading at.
  'count': 1.0 // Number | Number of elements to read from a table.
};
apiInstance.readTag(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the tag to read. | 
 **index** | **Number**| Table index to start reading at. | [optional] [default to 0.0]
 **count** | **Number**| Number of elements to read from a table. | [optional] [default to 1.0]

### Return type

[**TagValue**](TagValue.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## writeTag

> TagValue writeTag(id, value, opts)



Writes a new value to the given tag. Authorized for admins and editors.

### Example

```javascript
import GroovViewPublicApi from 'groov_view_public_api';
let defaultClient = GroovViewPublicApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GroovViewPublicApi.DataStoreApi();
let id = 3.4; // Number | ID of the tag to write.
let value = "value_example"; // String | Value to write to the tag. Must be a string, number, or boolean.
let opts = {
  'index': 0.0 // Number | For array tags, the index to write the value to.
};
apiInstance.writeTag(id, value, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the tag to write. | 
 **value** | **String**| Value to write to the tag. Must be a string, number, or boolean. | 
 **index** | **Number**| For array tags, the index to write the value to. | [optional] [default to 0.0]

### Return type

[**TagValue**](TagValue.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

