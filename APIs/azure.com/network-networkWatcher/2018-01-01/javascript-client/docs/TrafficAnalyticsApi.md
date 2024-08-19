# NetworkManagementClient.TrafficAnalyticsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networkWatchersGetFlowLogStatus_0**](TrafficAnalyticsApi.md#networkWatchersGetFlowLogStatus_0) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/queryFlowLogStatus | 
[**networkWatchersSetFlowLogConfiguration_0**](TrafficAnalyticsApi.md#networkWatchersSetFlowLogConfiguration_0) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/configureFlowLog | 



## networkWatchersGetFlowLogStatus_0

> FlowLogInformation networkWatchersGetFlowLogStatus_0(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Queries status of flow log and traffic analytics (optional) on a specified resource.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.TrafficAnalyticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the network watcher resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher resource.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.FlowLogStatusParameters(); // FlowLogStatusParameters | Parameters that define a resource to query flow log and traffic analytics (optional) status.
apiInstance.networkWatchersGetFlowLogStatus_0(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the network watcher resource group. | 
 **networkWatcherName** | **String**| The name of the network watcher resource. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**FlowLogStatusParameters**](FlowLogStatusParameters.md)| Parameters that define a resource to query flow log and traffic analytics (optional) status. | 

### Return type

[**FlowLogInformation**](FlowLogInformation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## networkWatchersSetFlowLogConfiguration_0

> FlowLogInformation networkWatchersSetFlowLogConfiguration_0(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Configures flow log and traffic analytics (optional) on a specified resource.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.TrafficAnalyticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the network watcher resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher resource.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.FlowLogInformation(); // FlowLogInformation | Parameters that define the configuration of flow log.
apiInstance.networkWatchersSetFlowLogConfiguration_0(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the network watcher resource group. | 
 **networkWatcherName** | **String**| The name of the network watcher resource. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**FlowLogInformation**](FlowLogInformation.md)| Parameters that define the configuration of flow log. | 

### Return type

[**FlowLogInformation**](FlowLogInformation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

