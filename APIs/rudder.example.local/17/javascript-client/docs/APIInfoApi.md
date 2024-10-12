# RudderApi.APIInfoApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiGeneralInformations**](APIInfoApi.md#apiGeneralInformations) | **GET** /info | List all endoints
[**apiInformations**](APIInfoApi.md#apiInformations) | **GET** /info/details/{endpointName} | Get information about one API endpoint
[**apiSubInformations**](APIInfoApi.md#apiSubInformations) | **GET** /info/{sectionId} | Get information on endpoint in a section



## apiGeneralInformations

> ApiGeneralInformations200Response apiGeneralInformations()

List all endoints

List all endpoints and their version

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.APIInfoApi();
apiInstance.apiGeneralInformations((error, data, response) => {
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

[**ApiGeneralInformations200Response**](ApiGeneralInformations200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiInformations

> ApiInformations200Response apiInformations(endpointName)

Get information about one API endpoint

Get the description and the list of supported version for one API endpoint

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.APIInfoApi();
let endpointName = "listAcceptedNodes"; // String | Name of the endpoint for which one wants information
apiInstance.apiInformations(endpointName, (error, data, response) => {
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
 **endpointName** | **String**| Name of the endpoint for which one wants information | 

### Return type

[**ApiInformations200Response**](ApiInformations200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiSubInformations

> ApiSubInformations200Response apiSubInformations(sectionId)

Get information on endpoint in a section

Get all endpoints in the given section with their supported version.

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.APIInfoApi();
let sectionId = "nodes"; // String | Id of the API section
apiInstance.apiSubInformations(sectionId, (error, data, response) => {
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
 **sectionId** | **String**| Id of the API section | 

### Return type

[**ApiSubInformations200Response**](ApiSubInformations200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

