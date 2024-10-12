# MixedReality.ProxyApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkNameAvailabilityLocal**](ProxyApi.md#checkNameAvailabilityLocal) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.MixedReality/locations/{location}/checkNameAvailability | 
[**operationsList**](ProxyApi.md#operationsList) | **GET** /providers/Microsoft.MixedReality/operations | 



## checkNameAvailabilityLocal

> CheckNameAvailabilityResponse checkNameAvailabilityLocal(subscriptionId, location, apiVersion, checkNameAvailability)



Check Name Availability for local uniqueness

### Example

```javascript
import MixedReality from 'mixed_reality';
let defaultClient = MixedReality.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MixedReality.ProxyApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let location = "location_example"; // String | The location in which uniqueness will be verified.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let checkNameAvailability = new MixedReality.CheckNameAvailabilityRequest(); // CheckNameAvailabilityRequest | Check Name Availability Request.
apiInstance.checkNameAvailabilityLocal(subscriptionId, location, apiVersion, checkNameAvailability, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID. | 
 **location** | **String**| The location in which uniqueness will be verified. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **checkNameAvailability** | [**CheckNameAvailabilityRequest**](CheckNameAvailabilityRequest.md)| Check Name Availability Request. | 

### Return type

[**CheckNameAvailabilityResponse**](CheckNameAvailabilityResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## operationsList

> OperationPage operationsList(apiVersion)



Exposing Available Operations

### Example

```javascript
import MixedReality from 'mixed_reality';
let defaultClient = MixedReality.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MixedReality.ProxyApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.operationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**OperationPage**](OperationPage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

