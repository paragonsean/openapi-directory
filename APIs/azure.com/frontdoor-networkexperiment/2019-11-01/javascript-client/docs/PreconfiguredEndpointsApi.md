# NetworkExperiments.PreconfiguredEndpointsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**preconfiguredEndpointsList**](PreconfiguredEndpointsApi.md#preconfiguredEndpointsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName}/PreconfiguredEndpoints | Gets a list of Preconfigured Endpoints



## preconfiguredEndpointsList

> PreconfiguredEndpointList preconfiguredEndpointsList(subscriptionId, apiVersion, resourceGroupName, profileName)

Gets a list of Preconfigured Endpoints

### Example

```javascript
import NetworkExperiments from 'network_experiments';
let defaultClient = NetworkExperiments.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkExperiments.PreconfiguredEndpointsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | The Profile identifier associated with the Tenant and Partner
apiInstance.preconfiguredEndpointsList(subscriptionId, apiVersion, resourceGroupName, profileName, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **profileName** | **String**| The Profile identifier associated with the Tenant and Partner | 

### Return type

[**PreconfiguredEndpointList**](PreconfiguredEndpointList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

