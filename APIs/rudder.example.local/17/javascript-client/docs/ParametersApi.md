# RudderApi.ParametersApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createParameter**](ParametersApi.md#createParameter) | **PUT** /parameters | Create a new parameter
[**deleteParameter**](ParametersApi.md#deleteParameter) | **DELETE** /parameters/{parameterId} | Delete a parameter
[**listParameters**](ParametersApi.md#listParameters) | **GET** /parameters | List all global parameters
[**parameterDetails**](ParametersApi.md#parameterDetails) | **GET** /parameters/{parameterId} | Get the value of a parameter
[**updateParameter**](ParametersApi.md#updateParameter) | **POST** /parameters/{parameterId} | Update a parameter&#39;s value



## createParameter

> CreateParameter200Response createParameter(parameter)

Create a new parameter

Create a new global parameter

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ParametersApi();
let parameter = new RudderApi.Parameter(); // Parameter | 
apiInstance.createParameter(parameter, (error, data, response) => {
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
 **parameter** | [**Parameter**](Parameter.md)|  | 

### Return type

[**CreateParameter200Response**](CreateParameter200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteParameter

> DeleteParameter200Response deleteParameter(parameterId)

Delete a parameter

Delete an existing parameter

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ParametersApi();
let parameterId = "rudder_file_edit_header"; // String | Id of the parameter to manage
apiInstance.deleteParameter(parameterId, (error, data, response) => {
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
 **parameterId** | **String**| Id of the parameter to manage | 

### Return type

[**DeleteParameter200Response**](DeleteParameter200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listParameters

> ListParameters200Response listParameters()

List all global parameters

Get the current value of all the global parameters

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ParametersApi();
apiInstance.listParameters((error, data, response) => {
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

[**ListParameters200Response**](ListParameters200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## parameterDetails

> ParameterDetails200Response parameterDetails(parameterId)

Get the value of a parameter

Get the current value of a given parameter

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ParametersApi();
let parameterId = "rudder_file_edit_header"; // String | Id of the parameter to manage
apiInstance.parameterDetails(parameterId, (error, data, response) => {
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
 **parameterId** | **String**| Id of the parameter to manage | 

### Return type

[**ParameterDetails200Response**](ParameterDetails200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateParameter

> UpdateParameter200Response updateParameter(parameterId)

Update a parameter&#39;s value

Update the properties of a parameter

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ParametersApi();
let parameterId = "rudder_file_edit_header"; // String | Id of the parameter to manage
apiInstance.updateParameter(parameterId, (error, data, response) => {
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
 **parameterId** | **String**| Id of the parameter to manage | 

### Return type

[**UpdateParameter200Response**](UpdateParameter200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

