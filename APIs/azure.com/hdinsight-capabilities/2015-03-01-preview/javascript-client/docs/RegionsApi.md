# HdInsightManagementClient.RegionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locationGetCapabilities**](RegionsApi.md#locationGetCapabilities) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.HDInsight/locations/{location}/capabilities | 



## locationGetCapabilities

> CapabilitiesResult locationGetCapabilities(location, apiVersion, subscriptionId)



Gets the capabilities for the specified location.

### Example

```javascript
import HdInsightManagementClient from 'hd_insight_management_client';
let defaultClient = HdInsightManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HdInsightManagementClient.RegionsApi();
let location = "location_example"; // String | The location to get capabilities for.
let apiVersion = "apiVersion_example"; // String | The HDInsight client API Version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.locationGetCapabilities(location, apiVersion, subscriptionId, (error, data, response) => {
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
 **location** | **String**| The location to get capabilities for. | 
 **apiVersion** | **String**| The HDInsight client API Version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**CapabilitiesResult**](CapabilitiesResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

