# CenitIoRestApiSpecification.FlowApi

All URIs are relative to *https://cenit.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setupFlowGet**](FlowApi.md#setupFlowGet) | **GET** /setup/flow/ | Returns a list of flows
[**setupFlowIdDelete**](FlowApi.md#setupFlowIdDelete) | **DELETE** /setup/flow/{id} | Delete a flow.
[**setupFlowIdGet**](FlowApi.md#setupFlowIdGet) | **GET** /setup/flow/{id} | Retrieve an existing flow
[**setupFlowPost**](FlowApi.md#setupFlowPost) | **POST** /setup/flow/ | Create or update a flow



## setupFlowGet

> [Flow] setupFlowGet()

Returns a list of flows

Returns a list of flows you&#39;ve previously created. The flows are returned in sorted order, with the most recent flow appearing first.

### Example

```javascript
import CenitIoRestApiSpecification from 'cenit_io_rest_api_specification';
let defaultClient = CenitIoRestApiSpecification.ApiClient.instance;
// Configure API key authorization: X-User-Access-Key
let X-User-Access-Key = defaultClient.authentications['X-User-Access-Key'];
X-User-Access-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-User-Access-Token
let X-User-Access-Token = defaultClient.authentications['X-User-Access-Token'];
X-User-Access-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Token.apiKeyPrefix = 'Token';

let apiInstance = new CenitIoRestApiSpecification.FlowApi();
apiInstance.setupFlowGet((error, data, response) => {
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

[**[Flow]**](Flow.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupFlowIdDelete

> setupFlowIdDelete(id)

Delete a flow.

Deletes the specified flow.

### Example

```javascript
import CenitIoRestApiSpecification from 'cenit_io_rest_api_specification';
let defaultClient = CenitIoRestApiSpecification.ApiClient.instance;
// Configure API key authorization: X-User-Access-Key
let X-User-Access-Key = defaultClient.authentications['X-User-Access-Key'];
X-User-Access-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-User-Access-Token
let X-User-Access-Token = defaultClient.authentications['X-User-Access-Token'];
X-User-Access-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Token.apiKeyPrefix = 'Token';

let apiInstance = new CenitIoRestApiSpecification.FlowApi();
let id = "id_example"; // String | Flow ID
apiInstance.setupFlowIdDelete(id, (error, data, response) => {
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
 **id** | **String**| Flow ID | 

### Return type

null (empty response body)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setupFlowIdGet

> Flow setupFlowIdGet(id)

Retrieve an existing flow

Retrieves the details of an existing flow. You need only supply the unique flow identifier that was returned upon flow creation.

### Example

```javascript
import CenitIoRestApiSpecification from 'cenit_io_rest_api_specification';
let defaultClient = CenitIoRestApiSpecification.ApiClient.instance;
// Configure API key authorization: X-User-Access-Key
let X-User-Access-Key = defaultClient.authentications['X-User-Access-Key'];
X-User-Access-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-User-Access-Token
let X-User-Access-Token = defaultClient.authentications['X-User-Access-Token'];
X-User-Access-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Token.apiKeyPrefix = 'Token';

let apiInstance = new CenitIoRestApiSpecification.FlowApi();
let id = "id_example"; // String | Flow ID
apiInstance.setupFlowIdGet(id, (error, data, response) => {
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
 **id** | **String**| Flow ID | 

### Return type

[**Flow**](Flow.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupFlowPost

> Flow setupFlowPost()

Create or update a flow

Creates or updates the specified flow. Any parameters not provided will be left unchanged.

### Example

```javascript
import CenitIoRestApiSpecification from 'cenit_io_rest_api_specification';
let defaultClient = CenitIoRestApiSpecification.ApiClient.instance;
// Configure API key authorization: X-User-Access-Key
let X-User-Access-Key = defaultClient.authentications['X-User-Access-Key'];
X-User-Access-Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-User-Access-Token
let X-User-Access-Token = defaultClient.authentications['X-User-Access-Token'];
X-User-Access-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-User-Access-Token.apiKeyPrefix = 'Token';

let apiInstance = new CenitIoRestApiSpecification.FlowApi();
apiInstance.setupFlowPost((error, data, response) => {
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

[**Flow**](Flow.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

