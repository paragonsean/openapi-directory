# AzureAppConfiguration.KeyValuesApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkKeyValue**](KeyValuesApi.md#checkKeyValue) | **HEAD** /kv/{key} | Requests the headers and status of the given resource.
[**checkKeyValues**](KeyValuesApi.md#checkKeyValues) | **HEAD** /kv | Requests the headers and status of the given resource.
[**deleteKeyValue**](KeyValuesApi.md#deleteKeyValue) | **DELETE** /kv/{key} | Deletes a key-value.
[**getKeyValue**](KeyValuesApi.md#getKeyValue) | **GET** /kv/{key} | Gets a single key-value.
[**getKeyValues**](KeyValuesApi.md#getKeyValues) | **GET** /kv | Gets a list of key-values.
[**putKeyValue**](KeyValuesApi.md#putKeyValue) | **PUT** /kv/{key} | Creates a key-value.



## checkKeyValue

> checkKeyValue(key, apiVersion, opts)

Requests the headers and status of the given resource.

### Example

```javascript
import AzureAppConfiguration from 'azure_app_configuration';

let apiInstance = new AzureAppConfiguration.KeyValuesApi();
let key = "key_example"; // String | The key of the key-value to retrieve.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let opts = {
  'label': "label_example", // String | The label of the key-value to retrieve.
  'syncToken': "syncToken_example", // String | Used to guarantee real-time consistency between requests.
  'acceptDatetime': "acceptDatetime_example", // String | Requests the server to respond with the state of the resource at the specified time.
  'ifMatch': "ifMatch_example", // String | Used to perform an operation only if the targeted resource's etag matches the value provided.
  'ifNoneMatch': "ifNoneMatch_example", // String | Used to perform an operation only if the targeted resource's etag does not match the value provided.
  'select': ["null"] // [String] | Used to select what fields are present in the returned resource(s).
};
apiInstance.checkKeyValue(key, apiVersion, opts, (error, data, response) => {
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
 **key** | **String**| The key of the key-value to retrieve. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **label** | **String**| The label of the key-value to retrieve. | [optional] 
 **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] 
 **acceptDatetime** | **String**| Requests the server to respond with the state of the resource at the specified time. | [optional] 
 **ifMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag matches the value provided. | [optional] 
 **ifNoneMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag does not match the value provided. | [optional] 
 **select** | [**[String]**](String.md)| Used to select what fields are present in the returned resource(s). | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## checkKeyValues

> checkKeyValues(apiVersion, opts)

Requests the headers and status of the given resource.

### Example

```javascript
import AzureAppConfiguration from 'azure_app_configuration';

let apiInstance = new AzureAppConfiguration.KeyValuesApi();
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let opts = {
  'key': "key_example", // String | A filter used to match keys.
  'label': "label_example", // String | A filter used to match labels
  'syncToken': "syncToken_example", // String | Used to guarantee real-time consistency between requests.
  'after': "after_example", // String | Instructs the server to return elements that appear after the element referred to by the specified token.
  'acceptDatetime': "acceptDatetime_example", // String | Requests the server to respond with the state of the resource at the specified time.
  'select': ["null"] // [String] | Used to select what fields are present in the returned resource(s).
};
apiInstance.checkKeyValues(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **key** | **String**| A filter used to match keys. | [optional] 
 **label** | **String**| A filter used to match labels | [optional] 
 **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] 
 **after** | **String**| Instructs the server to return elements that appear after the element referred to by the specified token. | [optional] 
 **acceptDatetime** | **String**| Requests the server to respond with the state of the resource at the specified time. | [optional] 
 **select** | [**[String]**](String.md)| Used to select what fields are present in the returned resource(s). | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteKeyValue

> KeyValue deleteKeyValue(key, apiVersion, opts)

Deletes a key-value.

### Example

```javascript
import AzureAppConfiguration from 'azure_app_configuration';

let apiInstance = new AzureAppConfiguration.KeyValuesApi();
let key = "key_example"; // String | The key of the key-value to delete.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let opts = {
  'label': "label_example", // String | The label of the key-value to delete.
  'syncToken': "syncToken_example", // String | Used to guarantee real-time consistency between requests.
  'ifMatch': "ifMatch_example" // String | Used to perform an operation only if the targeted resource's etag matches the value provided.
};
apiInstance.deleteKeyValue(key, apiVersion, opts, (error, data, response) => {
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
 **key** | **String**| The key of the key-value to delete. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **label** | **String**| The label of the key-value to delete. | [optional] 
 **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] 
 **ifMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag matches the value provided. | [optional] 

### Return type

[**KeyValue**](KeyValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.microsoft.appconfig.kv+json, application/json, application/problem+json


## getKeyValue

> KeyValue getKeyValue(key, apiVersion, opts)

Gets a single key-value.

### Example

```javascript
import AzureAppConfiguration from 'azure_app_configuration';

let apiInstance = new AzureAppConfiguration.KeyValuesApi();
let key = "key_example"; // String | The key of the key-value to retrieve.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let opts = {
  'label': "label_example", // String | The label of the key-value to retrieve.
  'syncToken': "syncToken_example", // String | Used to guarantee real-time consistency between requests.
  'acceptDatetime': "acceptDatetime_example", // String | Requests the server to respond with the state of the resource at the specified time.
  'ifMatch': "ifMatch_example", // String | Used to perform an operation only if the targeted resource's etag matches the value provided.
  'ifNoneMatch': "ifNoneMatch_example", // String | Used to perform an operation only if the targeted resource's etag does not match the value provided.
  'select': ["null"] // [String] | Used to select what fields are present in the returned resource(s).
};
apiInstance.getKeyValue(key, apiVersion, opts, (error, data, response) => {
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
 **key** | **String**| The key of the key-value to retrieve. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **label** | **String**| The label of the key-value to retrieve. | [optional] 
 **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] 
 **acceptDatetime** | **String**| Requests the server to respond with the state of the resource at the specified time. | [optional] 
 **ifMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag matches the value provided. | [optional] 
 **ifNoneMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag does not match the value provided. | [optional] 
 **select** | [**[String]**](String.md)| Used to select what fields are present in the returned resource(s). | [optional] 

### Return type

[**KeyValue**](KeyValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.microsoft.appconfig.kv+json, application/json, application/problem+json


## getKeyValues

> KeyValueListResult getKeyValues(apiVersion, opts)

Gets a list of key-values.

### Example

```javascript
import AzureAppConfiguration from 'azure_app_configuration';

let apiInstance = new AzureAppConfiguration.KeyValuesApi();
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let opts = {
  'key': "key_example", // String | A filter used to match keys.
  'label': "label_example", // String | A filter used to match labels
  'syncToken': "syncToken_example", // String | Used to guarantee real-time consistency between requests.
  'after': "after_example", // String | Instructs the server to return elements that appear after the element referred to by the specified token.
  'acceptDatetime': "acceptDatetime_example", // String | Requests the server to respond with the state of the resource at the specified time.
  'select': ["null"] // [String] | Used to select what fields are present in the returned resource(s).
};
apiInstance.getKeyValues(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **key** | **String**| A filter used to match keys. | [optional] 
 **label** | **String**| A filter used to match labels | [optional] 
 **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] 
 **after** | **String**| Instructs the server to return elements that appear after the element referred to by the specified token. | [optional] 
 **acceptDatetime** | **String**| Requests the server to respond with the state of the resource at the specified time. | [optional] 
 **select** | [**[String]**](String.md)| Used to select what fields are present in the returned resource(s). | [optional] 

### Return type

[**KeyValueListResult**](KeyValueListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.microsoft.appconfig.kvset+json, application/json, application/problem+json


## putKeyValue

> KeyValue putKeyValue(key, apiVersion, opts)

Creates a key-value.

### Example

```javascript
import AzureAppConfiguration from 'azure_app_configuration';

let apiInstance = new AzureAppConfiguration.KeyValuesApi();
let key = "key_example"; // String | The key of the key-value to create.
let apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
let opts = {
  'label': "label_example", // String | The label of the key-value to create.
  'syncToken': "syncToken_example", // String | Used to guarantee real-time consistency between requests.
  'ifMatch': "ifMatch_example", // String | Used to perform an operation only if the targeted resource's etag matches the value provided.
  'ifNoneMatch': "ifNoneMatch_example", // String | Used to perform an operation only if the targeted resource's etag does not match the value provided.
  'entity': new AzureAppConfiguration.KeyValue() // KeyValue | The key-value to create.
};
apiInstance.putKeyValue(key, apiVersion, opts, (error, data, response) => {
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
 **key** | **String**| The key of the key-value to create. | 
 **apiVersion** | **String**| The API version to be used with the HTTP request. | 
 **label** | **String**| The label of the key-value to create. | [optional] 
 **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] 
 **ifMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag matches the value provided. | [optional] 
 **ifNoneMatch** | **String**| Used to perform an operation only if the targeted resource&#39;s etag does not match the value provided. | [optional] 
 **entity** | [**KeyValue**](KeyValue.md)| The key-value to create. | [optional] 

### Return type

[**KeyValue**](KeyValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/vnd.microsoft.appconfig.kv+json, application/vnd.microsoft.appconfig.kvset+json, application/json, text/json, application/*+json, application/json-patch+json
- **Accept**: application/vnd.microsoft.appconfig.kv+json, application/json, application/problem+json

