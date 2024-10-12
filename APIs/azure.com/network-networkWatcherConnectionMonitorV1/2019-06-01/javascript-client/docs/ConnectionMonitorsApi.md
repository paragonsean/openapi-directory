# NetworkManagementClient.ConnectionMonitorsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connectionMonitorsCreateOrUpdate**](ConnectionMonitorsApi.md#connectionMonitorsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName} | 
[**connectionMonitorsDelete**](ConnectionMonitorsApi.md#connectionMonitorsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName} | 
[**connectionMonitorsGet**](ConnectionMonitorsApi.md#connectionMonitorsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName} | 
[**connectionMonitorsList**](ConnectionMonitorsApi.md#connectionMonitorsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors | 
[**connectionMonitorsQuery**](ConnectionMonitorsApi.md#connectionMonitorsQuery) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}/query | 
[**connectionMonitorsStart**](ConnectionMonitorsApi.md#connectionMonitorsStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}/start | 
[**connectionMonitorsStop**](ConnectionMonitorsApi.md#connectionMonitorsStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName}/stop | 
[**connectionMonitorsUpdateTags**](ConnectionMonitorsApi.md#connectionMonitorsUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectionMonitors/{connectionMonitorName} | 



## connectionMonitorsCreateOrUpdate

> ConnectionMonitorResult connectionMonitorsCreateOrUpdate(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId, parameters)



Create or update a connection monitor.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ConnectionMonitorsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing Network Watcher.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the Network Watcher resource.
let connectionMonitorName = "connectionMonitorName_example"; // String | The name of the connection monitor.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.ConnectionMonitor(); // ConnectionMonitor | Parameters that define the operation to create a connection monitor.
apiInstance.connectionMonitorsCreateOrUpdate(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **connectionMonitorName** | **String**| The name of the connection monitor. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ConnectionMonitor**](ConnectionMonitor.md)| Parameters that define the operation to create a connection monitor. | 

### Return type

[**ConnectionMonitorResult**](ConnectionMonitorResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## connectionMonitorsDelete

> connectionMonitorsDelete(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId)



Deletes the specified connection monitor.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ConnectionMonitorsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing Network Watcher.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the Network Watcher resource.
let connectionMonitorName = "connectionMonitorName_example"; // String | The name of the connection monitor.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.connectionMonitorsDelete(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing Network Watcher. | 
 **networkWatcherName** | **String**| The name of the Network Watcher resource. | 
 **connectionMonitorName** | **String**| The name of the connection monitor. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionMonitorsGet

> ConnectionMonitorResult connectionMonitorsGet(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId)



Gets a connection monitor by name.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ConnectionMonitorsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing Network Watcher.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the Network Watcher resource.
let connectionMonitorName = "connectionMonitorName_example"; // String | The name of the connection monitor.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.connectionMonitorsGet(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId, (error, data, response) => {
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
 **connectionMonitorName** | **String**| The name of the connection monitor. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ConnectionMonitorResult**](ConnectionMonitorResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionMonitorsList

> ConnectionMonitorListResult connectionMonitorsList(resourceGroupName, networkWatcherName, apiVersion, subscriptionId)



Lists all connection monitors for the specified Network Watcher.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ConnectionMonitorsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing Network Watcher.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the Network Watcher resource.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.connectionMonitorsList(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, (error, data, response) => {
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

[**ConnectionMonitorListResult**](ConnectionMonitorListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionMonitorsQuery

> ConnectionMonitorQueryResult connectionMonitorsQuery(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId)



Query a snapshot of the most recent connection states.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ConnectionMonitorsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing Network Watcher.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the Network Watcher resource.
let connectionMonitorName = "connectionMonitorName_example"; // String | The name given to the connection monitor.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.connectionMonitorsQuery(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId, (error, data, response) => {
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
 **connectionMonitorName** | **String**| The name given to the connection monitor. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ConnectionMonitorQueryResult**](ConnectionMonitorQueryResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionMonitorsStart

> connectionMonitorsStart(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId)



Starts the specified connection monitor.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ConnectionMonitorsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing Network Watcher.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the Network Watcher resource.
let connectionMonitorName = "connectionMonitorName_example"; // String | The name of the connection monitor.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.connectionMonitorsStart(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing Network Watcher. | 
 **networkWatcherName** | **String**| The name of the Network Watcher resource. | 
 **connectionMonitorName** | **String**| The name of the connection monitor. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionMonitorsStop

> connectionMonitorsStop(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId)



Stops the specified connection monitor.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ConnectionMonitorsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing Network Watcher.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the Network Watcher resource.
let connectionMonitorName = "connectionMonitorName_example"; // String | The name of the connection monitor.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.connectionMonitorsStop(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing Network Watcher. | 
 **networkWatcherName** | **String**| The name of the Network Watcher resource. | 
 **connectionMonitorName** | **String**| The name of the connection monitor. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionMonitorsUpdateTags

> ConnectionMonitorResult connectionMonitorsUpdateTags(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId, parameters)



Update tags of the specified connection monitor.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ConnectionMonitorsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
let connectionMonitorName = "connectionMonitorName_example"; // String | The name of the connection monitor.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.ConnectionMonitorsUpdateTagsRequest(); // ConnectionMonitorsUpdateTagsRequest | Parameters supplied to update connection monitor tags.
apiInstance.connectionMonitorsUpdateTags(resourceGroupName, networkWatcherName, connectionMonitorName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **connectionMonitorName** | **String**| The name of the connection monitor. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ConnectionMonitorsUpdateTagsRequest**](ConnectionMonitorsUpdateTagsRequest.md)| Parameters supplied to update connection monitor tags. | 

### Return type

[**ConnectionMonitorResult**](ConnectionMonitorResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

