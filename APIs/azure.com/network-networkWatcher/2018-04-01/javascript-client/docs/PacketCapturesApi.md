# NetworkManagementClient.PacketCapturesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**packetCapturesCreate**](PacketCapturesApi.md#packetCapturesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName} | 
[**packetCapturesDelete**](PacketCapturesApi.md#packetCapturesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName} | 
[**packetCapturesGet**](PacketCapturesApi.md#packetCapturesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName} | 
[**packetCapturesGetStatus**](PacketCapturesApi.md#packetCapturesGetStatus) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}/queryStatus | 
[**packetCapturesList**](PacketCapturesApi.md#packetCapturesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures | 
[**packetCapturesStop**](PacketCapturesApi.md#packetCapturesStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkWatchers/{networkWatcherName}/packetCaptures/{packetCaptureName}/stop | 



## packetCapturesCreate

> PacketCaptureResult packetCapturesCreate(resourceGroupName, networkWatcherName, packetCaptureName, apiVersion, subscriptionId, parameters)



Create and start a packet capture on the specified VM.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PacketCapturesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
let packetCaptureName = "packetCaptureName_example"; // String | The name of the packet capture session.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.PacketCapture(); // PacketCapture | Parameters that define the create packet capture operation.
apiInstance.packetCapturesCreate(resourceGroupName, networkWatcherName, packetCaptureName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **packetCaptureName** | **String**| The name of the packet capture session. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**PacketCapture**](PacketCapture.md)| Parameters that define the create packet capture operation. | 

### Return type

[**PacketCaptureResult**](PacketCaptureResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## packetCapturesDelete

> packetCapturesDelete(resourceGroupName, networkWatcherName, packetCaptureName, apiVersion, subscriptionId)



Deletes the specified packet capture session.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PacketCapturesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
let packetCaptureName = "packetCaptureName_example"; // String | The name of the packet capture session.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.packetCapturesDelete(resourceGroupName, networkWatcherName, packetCaptureName, apiVersion, subscriptionId, (error, data, response) => {
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
 **packetCaptureName** | **String**| The name of the packet capture session. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## packetCapturesGet

> PacketCaptureResult packetCapturesGet(resourceGroupName, networkWatcherName, packetCaptureName, apiVersion, subscriptionId)



Gets a packet capture session by name.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PacketCapturesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
let packetCaptureName = "packetCaptureName_example"; // String | The name of the packet capture session.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.packetCapturesGet(resourceGroupName, networkWatcherName, packetCaptureName, apiVersion, subscriptionId, (error, data, response) => {
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
 **packetCaptureName** | **String**| The name of the packet capture session. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**PacketCaptureResult**](PacketCaptureResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## packetCapturesGetStatus

> PacketCaptureQueryStatusResult packetCapturesGetStatus(resourceGroupName, networkWatcherName, packetCaptureName, apiVersion, subscriptionId)



Query the status of a running packet capture session.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PacketCapturesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the Network Watcher resource.
let packetCaptureName = "packetCaptureName_example"; // String | The name given to the packet capture session.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.packetCapturesGetStatus(resourceGroupName, networkWatcherName, packetCaptureName, apiVersion, subscriptionId, (error, data, response) => {
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
 **networkWatcherName** | **String**| The name of the Network Watcher resource. | 
 **packetCaptureName** | **String**| The name given to the packet capture session. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**PacketCaptureQueryStatusResult**](PacketCaptureQueryStatusResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## packetCapturesList

> PacketCaptureListResult packetCapturesList(resourceGroupName, networkWatcherName, apiVersion, subscriptionId)



Lists all packet capture sessions within the specified resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PacketCapturesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the Network Watcher resource.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.packetCapturesList(resourceGroupName, networkWatcherName, apiVersion, subscriptionId, (error, data, response) => {
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
 **networkWatcherName** | **String**| The name of the Network Watcher resource. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**PacketCaptureListResult**](PacketCaptureListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## packetCapturesStop

> packetCapturesStop(resourceGroupName, networkWatcherName, packetCaptureName, apiVersion, subscriptionId)



Stops a specified packet capture session.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.PacketCapturesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let networkWatcherName = "networkWatcherName_example"; // String | The name of the network watcher.
let packetCaptureName = "packetCaptureName_example"; // String | The name of the packet capture session.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.packetCapturesStop(resourceGroupName, networkWatcherName, packetCaptureName, apiVersion, subscriptionId, (error, data, response) => {
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
 **packetCaptureName** | **String**| The name of the packet capture session. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

