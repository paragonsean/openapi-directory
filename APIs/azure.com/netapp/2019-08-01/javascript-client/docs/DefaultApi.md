# MicrosoftNetApp.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**netAppResourceCheckFilePathAvailability**](DefaultApi.md#netAppResourceCheckFilePathAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.NetApp/locations/{location}/checkFilePathAvailability | Check file path availability
[**netAppResourceCheckNameAvailability**](DefaultApi.md#netAppResourceCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.NetApp/locations/{location}/checkNameAvailability | Check resource name availability



## netAppResourceCheckFilePathAvailability

> ResourceNameAvailability netAppResourceCheckFilePathAvailability(subscriptionId, location, apiVersion, body)

Check file path availability

Check if a file path is available.

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | The location
let apiVersion = "'2019-08-01'"; // String | Version of the API to be used with the client request.
let body = new MicrosoftNetApp.ResourceNameAvailabilityRequest(); // ResourceNameAvailabilityRequest | File path availability request.
apiInstance.netAppResourceCheckFilePathAvailability(subscriptionId, location, apiVersion, body, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| The location | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2019-08-01&#39;]
 **body** | [**ResourceNameAvailabilityRequest**](ResourceNameAvailabilityRequest.md)| File path availability request. | 

### Return type

[**ResourceNameAvailability**](ResourceNameAvailability.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## netAppResourceCheckNameAvailability

> ResourceNameAvailability netAppResourceCheckNameAvailability(subscriptionId, location, apiVersion, body)

Check resource name availability

Check if a resource name is available.

### Example

```javascript
import MicrosoftNetApp from 'microsoft_net_app';
let defaultClient = MicrosoftNetApp.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftNetApp.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | The location
let apiVersion = "'2019-08-01'"; // String | Version of the API to be used with the client request.
let body = new MicrosoftNetApp.ResourceNameAvailabilityRequest(); // ResourceNameAvailabilityRequest | Name availability request.
apiInstance.netAppResourceCheckNameAvailability(subscriptionId, location, apiVersion, body, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| The location | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | [default to &#39;2019-08-01&#39;]
 **body** | [**ResourceNameAvailabilityRequest**](ResourceNameAvailabilityRequest.md)| Name availability request. | 

### Return type

[**ResourceNameAvailability**](ResourceNameAvailability.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

