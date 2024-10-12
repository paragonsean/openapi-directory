# DataBoxEdgeManagementClient.SharesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sharesCreateOrUpdate**](SharesApi.md#sharesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/shares/{name} | Creates a new share or updates an existing share on the device.
[**sharesDelete**](SharesApi.md#sharesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/shares/{name} | 
[**sharesGet**](SharesApi.md#sharesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/shares/{name} | Gets a share by name.
[**sharesListByDataBoxEdgeDevice**](SharesApi.md#sharesListByDataBoxEdgeDevice) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/shares | Lists all the shares in a data box edge/gateway device.
[**sharesRefresh**](SharesApi.md#sharesRefresh) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/shares/{name}/refresh | Refreshes the share metadata with the data from the cloud.



## sharesCreateOrUpdate

> Share sharesCreateOrUpdate(deviceName, name, subscriptionId, resourceGroupName, apiVersion, share)

Creates a new share or updates an existing share on the device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.SharesApi();
let deviceName = "deviceName_example"; // String | The device name.
let name = "name_example"; // String | The share name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
let share = new DataBoxEdgeManagementClient.Share(); // Share | The share properties.
apiInstance.sharesCreateOrUpdate(deviceName, name, subscriptionId, resourceGroupName, apiVersion, share, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **name** | **String**| The share name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 
 **share** | [**Share**](Share.md)| The share properties. | 

### Return type

[**Share**](Share.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sharesDelete

> sharesDelete(deviceName, name, subscriptionId, resourceGroupName, apiVersion)



Deletes the share on the data box edge/gateway device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.SharesApi();
let deviceName = "deviceName_example"; // String | The device name.
let name = "name_example"; // String | The share name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.sharesDelete(deviceName, name, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **name** | **String**| The share name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sharesGet

> Share sharesGet(deviceName, name, subscriptionId, resourceGroupName, apiVersion)

Gets a share by name.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.SharesApi();
let deviceName = "deviceName_example"; // String | The device name.
let name = "name_example"; // String | The share name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.sharesGet(deviceName, name, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **name** | **String**| The share name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**Share**](Share.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sharesListByDataBoxEdgeDevice

> ShareList sharesListByDataBoxEdgeDevice(deviceName, subscriptionId, resourceGroupName, apiVersion)

Lists all the shares in a data box edge/gateway device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.SharesApi();
let deviceName = "deviceName_example"; // String | The device name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.sharesListByDataBoxEdgeDevice(deviceName, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**ShareList**](ShareList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sharesRefresh

> sharesRefresh(deviceName, name, subscriptionId, resourceGroupName, apiVersion)

Refreshes the share metadata with the data from the cloud.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.SharesApi();
let deviceName = "deviceName_example"; // String | The device name.
let name = "name_example"; // String | The share name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.sharesRefresh(deviceName, name, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The device name. | 
 **name** | **String**| The share name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

