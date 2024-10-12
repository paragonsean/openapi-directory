# NetworkManagementClient.ExpressRouteLinksApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expressRouteLinksGet**](ExpressRouteLinksApi.md#expressRouteLinksGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName}/links/{linkName} | 
[**expressRouteLinksList**](ExpressRouteLinksApi.md#expressRouteLinksList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/ExpressRoutePorts/{expressRoutePortName}/links | 



## expressRouteLinksGet

> ExpressRouteLink expressRouteLinksGet(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName, linkName)



Retrieves the specified ExpressRouteLink resource.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRouteLinksApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let expressRoutePortName = "expressRoutePortName_example"; // String | The name of the ExpressRoutePort resource.
let linkName = "linkName_example"; // String | The name of the ExpressRouteLink resource.
apiInstance.expressRouteLinksGet(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName, linkName, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **expressRoutePortName** | **String**| The name of the ExpressRoutePort resource. | 
 **linkName** | **String**| The name of the ExpressRouteLink resource. | 

### Return type

[**ExpressRouteLink**](ExpressRouteLink.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expressRouteLinksList

> ExpressRouteLinkListResult expressRouteLinksList(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName)



Retrieve the ExpressRouteLink sub-resources of the specified ExpressRoutePort resource.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRouteLinksApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let expressRoutePortName = "expressRoutePortName_example"; // String | The name of the ExpressRoutePort resource.
apiInstance.expressRouteLinksList(subscriptionId, apiVersion, resourceGroupName, expressRoutePortName, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **expressRoutePortName** | **String**| The name of the ExpressRoutePort resource. | 

### Return type

[**ExpressRouteLinkListResult**](ExpressRouteLinkListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

