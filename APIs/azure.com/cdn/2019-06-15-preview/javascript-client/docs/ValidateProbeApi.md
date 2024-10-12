# CdnManagementClient.ValidateProbeApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validateProbe**](ValidateProbeApi.md#validateProbe) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Cdn/validateProbe | 



## validateProbe

> ValidateProbeOutput validateProbe(subscriptionId, apiVersion, validateProbeInput)



Check if the probe path is a valid path and the file can be accessed. Probe path is the path to a file hosted on the origin server to help accelerate the delivery of dynamic content via the CDN endpoint. This path is relative to the origin path specified in the endpoint configuration.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.ValidateProbeApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
let validateProbeInput = new CdnManagementClient.ValidateProbeInput(); // ValidateProbeInput | Input to check.
apiInstance.validateProbe(subscriptionId, apiVersion, validateProbeInput, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 
 **validateProbeInput** | [**ValidateProbeInput**](ValidateProbeInput.md)| Input to check. | 

### Return type

[**ValidateProbeOutput**](ValidateProbeOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

