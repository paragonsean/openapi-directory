# NetworkManagementClient.NetworkWatchersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networkWatchersCheckConnectivity**](NetworkWatchersApi.md#networkWatchersCheckConnectivity) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/connectivityCheck | 
[**networkWatchersCreateOrUpdate**](NetworkWatchersApi.md#networkWatchersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName} | 
[**networkWatchersDelete**](NetworkWatchersApi.md#networkWatchersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName} | 
[**networkWatchersGet**](NetworkWatchersApi.md#networkWatchersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName} | 
[**networkWatchersGetAzureReachabilityReport**](NetworkWatchersApi.md#networkWatchersGetAzureReachabilityReport) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/azureReachabilityReport | 
[**networkWatchersGetFlowLogStatus**](NetworkWatchersApi.md#networkWatchersGetFlowLogStatus) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/queryFlowLogStatus | 
[**networkWatchersGetNextHop**](NetworkWatchersApi.md#networkWatchersGetNextHop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/nextHop | 
[**networkWatchersGetTopology**](NetworkWatchersApi.md#networkWatchersGetTopology) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/topology | 
[**networkWatchersGetTroubleshooting**](NetworkWatchersApi.md#networkWatchersGetTroubleshooting) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/troubleshoot | 
[**networkWatchersGetTroubleshootingResult**](NetworkWatchersApi.md#networkWatchersGetTroubleshootingResult) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/queryTroubleshootResult | 
[**networkWatchersGetVMSecurityRules**](NetworkWatchersApi.md#networkWatchersGetVMSecurityRules) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/securityGroupView | 
[**networkWatchersList**](NetworkWatchersApi.md#networkWatchersList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers | 
[**networkWatchersListAll**](NetworkWatchersApi.md#networkWatchersListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/networkWatchers | 
[**networkWatchersListAvailableProviders**](NetworkWatchersApi.md#networkWatchersListAvailableProviders) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/availableProvidersList | 
[**networkWatchersSetFlowLogConfiguration**](NetworkWatchersApi.md#networkWatchersSetFlowLogConfiguration) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/configureFlowLog | 
[**networkWatchersUpdateTags**](NetworkWatchersApi.md#networkWatchersUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName} | 
[**networkWatchersVerifyIPFlow**](NetworkWatchersApi.md#networkWatchersVerifyIPFlow) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/ipFlowVerify | 



## networkWatchersCheckConnectivity

> ConnectivityInformation networkWatchersCheckConnectivity(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Verifies the possibility of establishing a direct TCP connection from a virtual machine to a given endpoint including another VM or an arbitrary remote server.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkWatchersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the network watcher resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher resource.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.ConnectivityParameters(); // ConnectivityParameters | Parameters that determine how the connectivity check will be performed.
apiInstance.networkWatchersCheckConnectivity(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **parameters** | [**ConnectivityParameters**](ConnectivityParameters.md)| Parameters that determine how the connectivity check will be performed. | 

### Return type

[**ConnectivityInformation**](ConnectivityInformation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## networkWatchersCreateOrUpdate

> NetworkWatcher networkWatchersCreateOrUpdate(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Creates or updates a network watcher in the specified resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkWatchersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.NetworkWatcher(); // NetworkWatcher | Parameters that define the network watcher resource.
apiInstance.networkWatchersCreateOrUpdate(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**NetworkWatcher**](NetworkWatcher.md)| Parameters that define the network watcher resource. | 

### Return type

[**NetworkWatcher**](NetworkWatcher.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## networkWatchersDelete

> networkWatchersDelete(resourceGroupName, networkWatcherName, apiVersion, subscriptionId)



Deletes the specified network watcher resource.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkWatchersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.networkWatchersDelete(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## networkWatchersGet

> NetworkWatcher networkWatchersGet(resourceGroupName, networkWatcherName, apiVersion, subscriptionId)



Gets the specified network watcher by resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkWatchersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.networkWatchersGet(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**NetworkWatcher**](NetworkWatcher.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## networkWatchersGetAzureReachabilityReport

> AzureReachabilityReport networkWatchersGetAzureReachabilityReport(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Gets the relative latency score for internet service providers from a specified location to Azure regions.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkWatchersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the network watcher resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher resource.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.AzureReachabilityReportParameters(); // AzureReachabilityReportParameters | Parameters that determine Azure reachability report configuration.
apiInstance.networkWatchersGetAzureReachabilityReport(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **parameters** | [**AzureReachabilityReportParameters**](AzureReachabilityReportParameters.md)| Parameters that determine Azure reachability report configuration. | 

### Return type

[**AzureReachabilityReport**](AzureReachabilityReport.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## networkWatchersGetFlowLogStatus

> FlowLogInformation networkWatchersGetFlowLogStatus(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Queries status of flow log and traffic analytics (optional) on a specified resource.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkWatchersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the network watcher resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher resource.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.FlowLogStatusParameters(); // FlowLogStatusParameters | Parameters that define a resource to query flow log and traffic analytics (optional) status.
apiInstance.networkWatchersGetFlowLogStatus(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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


## networkWatchersGetNextHop

> NextHopResult networkWatchersGetNextHop(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Gets the next hop from the specified VM.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkWatchersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.NextHopParameters(); // NextHopParameters | Parameters that define the source and destination endpoint.
apiInstance.networkWatchersGetNextHop(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**NextHopParameters**](NextHopParameters.md)| Parameters that define the source and destination endpoint. | 

### Return type

[**NextHopResult**](NextHopResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## networkWatchersGetTopology

> Topology networkWatchersGetTopology(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Gets the current network topology by resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkWatchersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.TopologyParameters(); // TopologyParameters | Parameters that define the representation of topology.
apiInstance.networkWatchersGetTopology(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**TopologyParameters**](TopologyParameters.md)| Parameters that define the representation of topology. | 

### Return type

[**Topology**](Topology.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## networkWatchersGetTroubleshooting

> TroubleshootingResult networkWatchersGetTroubleshooting(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Initiate troubleshooting on a specified resource

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkWatchersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher resource.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.TroubleshootingParameters(); // TroubleshootingParameters | Parameters that define the resource to troubleshoot.
apiInstance.networkWatchersGetTroubleshooting(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **networkWatcherName** | **String**| The name of the network watcher resource. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**TroubleshootingParameters**](TroubleshootingParameters.md)| Parameters that define the resource to troubleshoot. | 

### Return type

[**TroubleshootingResult**](TroubleshootingResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## networkWatchersGetTroubleshootingResult

> TroubleshootingResult networkWatchersGetTroubleshootingResult(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Get the last completed troubleshooting result on a specified resource

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkWatchersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher resource.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.QueryTroubleshootingParameters(); // QueryTroubleshootingParameters | Parameters that define the resource to query the troubleshooting result.
apiInstance.networkWatchersGetTroubleshootingResult(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **networkWatcherName** | **String**| The name of the network watcher resource. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**QueryTroubleshootingParameters**](QueryTroubleshootingParameters.md)| Parameters that define the resource to query the troubleshooting result. | 

### Return type

[**TroubleshootingResult**](TroubleshootingResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## networkWatchersGetVMSecurityRules

> SecurityGroupViewResult networkWatchersGetVMSecurityRules(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Gets the configured and effective security group rules on the specified VM.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkWatchersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.SecurityGroupViewParameters(); // SecurityGroupViewParameters | Parameters that define the VM to check security groups for.
apiInstance.networkWatchersGetVMSecurityRules(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**SecurityGroupViewParameters**](SecurityGroupViewParameters.md)| Parameters that define the VM to check security groups for. | 

### Return type

[**SecurityGroupViewResult**](SecurityGroupViewResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## networkWatchersList

> NetworkWatcherListResult networkWatchersList(resourceGroupName, apiVersion, subscriptionId)



Gets all network watchers by resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkWatchersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.networkWatchersList(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**NetworkWatcherListResult**](NetworkWatcherListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## networkWatchersListAll

> NetworkWatcherListResult networkWatchersListAll(apiVersion, subscriptionId)



Gets all network watchers by subscription.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkWatchersApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.networkWatchersListAll(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**NetworkWatcherListResult**](NetworkWatcherListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## networkWatchersListAvailableProviders

> AvailableProvidersList networkWatchersListAvailableProviders(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Lists all available internet service providers for a specified Azure region.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkWatchersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the network watcher resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher resource.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.AvailableProvidersListParameters(); // AvailableProvidersListParameters | Parameters that scope the list of available providers.
apiInstance.networkWatchersListAvailableProviders(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **parameters** | [**AvailableProvidersListParameters**](AvailableProvidersListParameters.md)| Parameters that scope the list of available providers. | 

### Return type

[**AvailableProvidersList**](AvailableProvidersList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## networkWatchersSetFlowLogConfiguration

> FlowLogInformation networkWatchersSetFlowLogConfiguration(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Configures flow log and traffic analytics (optional) on a specified resource.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkWatchersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the network watcher resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher resource.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.FlowLogInformation(); // FlowLogInformation | Parameters that define the configuration of flow log.
apiInstance.networkWatchersSetFlowLogConfiguration(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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


## networkWatchersUpdateTags

> NetworkWatcher networkWatchersUpdateTags(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Updates a network watcher tags.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkWatchersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.NetworkWatchersUpdateTagsRequest(); // NetworkWatchersUpdateTagsRequest | Parameters supplied to update network watcher tags.
apiInstance.networkWatchersUpdateTags(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**NetworkWatchersUpdateTagsRequest**](NetworkWatchersUpdateTagsRequest.md)| Parameters supplied to update network watcher tags. | 

### Return type

[**NetworkWatcher**](NetworkWatcher.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## networkWatchersVerifyIPFlow

> VerificationIPFlowResult networkWatchersVerifyIPFlow(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters)



Verify IP flow from the specified VM to a location given the currently configured NSG rules.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.NetworkWatchersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.VerificationIPFlowParameters(); // VerificationIPFlowParameters | Parameters that define the IP flow to be verified.
apiInstance.networkWatchersVerifyIPFlow(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**VerificationIPFlowParameters**](VerificationIPFlowParameters.md)| Parameters that define the IP flow to be verified. | 

### Return type

[**VerificationIPFlowResult**](VerificationIPFlowResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

