# NetworkManagementClient.FlowLogsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**flowLogsCreateOrUpdate**](FlowLogsApi.md#flowLogsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/flowLogs/{flowLogName} | 
[**flowLogsDelete**](FlowLogsApi.md#flowLogsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/flowLogs/{flowLogName} | 
[**flowLogsGet**](FlowLogsApi.md#flowLogsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/flowLogs/{flowLogName} | 
[**flowLogsList**](FlowLogsApi.md#flowLogsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/flowLogs | 



## flowLogsCreateOrUpdate

> FlowLog flowLogsCreateOrUpdate(resourceGroupName, networkWatcherName, flowLogName, apiVersion, subscriptionId, parameters)



Create or update a flow log for the specified network security group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.FlowLogsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
let flowLogName = "flowLogName_example"; // String | The name of the flow log.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.FlowLog(); // FlowLog | Parameters that define the create or update flow log resource.
apiInstance.flowLogsCreateOrUpdate(resourceGroupName, networkWatcherName, flowLogName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **networkWatcherName** | **String**| The name of the network watcher. | 
 **flowLogName** | **String**| The name of the flow log. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**FlowLog**](FlowLog.md)| Parameters that define the create or update flow log resource. | 

### Return type

[**FlowLog**](FlowLog.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## flowLogsDelete

> flowLogsDelete(resourceGroupName, networkWatcherName, flowLogName, apiVersion, subscriptionId)



Deletes the specified flow log resource.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.FlowLogsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
let flowLogName = "flowLogName_example"; // String | The name of the flow log resource.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.flowLogsDelete(resourceGroupName, networkWatcherName, flowLogName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **networkWatcherName** | **String**| The name of the network watcher. | 
 **flowLogName** | **String**| The name of the flow log resource. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## flowLogsGet

> FlowLog flowLogsGet(resourceGroupName, networkWatcherName, flowLogName, apiVersion, subscriptionId)



Gets a flow log resource by name.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.FlowLogsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
let flowLogName = "flowLogName_example"; // String | The name of the flow log resource.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.flowLogsGet(resourceGroupName, networkWatcherName, flowLogName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **networkWatcherName** | **String**| The name of the network watcher. | 
 **flowLogName** | **String**| The name of the flow log resource. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**FlowLog**](FlowLog.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## flowLogsList

> FlowLogListResult flowLogsList(resourceGroupName, networkWatcherName, apiVersion, subscriptionId)



Lists all flow log resources for the specified Network Watcher.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.FlowLogsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing Network Watcher.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the Network Watcher resource.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.flowLogsList(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing Network Watcher. | 
 **networkWatcherName** | **String**| The name of the Network Watcher resource. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**FlowLogListResult**](FlowLogListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

