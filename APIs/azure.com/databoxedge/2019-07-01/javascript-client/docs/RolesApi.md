# DataBoxEdgeManagementClient.RolesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rolesCreateOrUpdate**](RolesApi.md#rolesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/roles/{name} | 
[**rolesDelete**](RolesApi.md#rolesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/roles/{name} | 
[**rolesGet**](RolesApi.md#rolesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/roles/{name} | 
[**rolesListByDataBoxEdgeDevice**](RolesApi.md#rolesListByDataBoxEdgeDevice) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/roles | 



## rolesCreateOrUpdate

> Role rolesCreateOrUpdate(deviceName, name, subscriptionId, resourceGroupName, apiVersion, role)



Create or update a role.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.RolesApi();
let deviceName = "deviceName_example"; // String | The device name.
let name = "name_example"; // String | The role name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
let role = new DataBoxEdgeManagementClient.Role(); // Role | The role properties.
apiInstance.rolesCreateOrUpdate(deviceName, name, subscriptionId, resourceGroupName, apiVersion, role, (error, data, response) => {
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
 **name** | **String**| The role name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 
 **role** | [**Role**](Role.md)| The role properties. | 

### Return type

[**Role**](Role.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## rolesDelete

> rolesDelete(deviceName, name, subscriptionId, resourceGroupName, apiVersion)



Deletes the role on the device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.RolesApi();
let deviceName = "deviceName_example"; // String | The device name.
let name = "name_example"; // String | The role name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.rolesDelete(deviceName, name, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **name** | **String**| The role name. | 
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


## rolesGet

> Role rolesGet(deviceName, name, subscriptionId, resourceGroupName, apiVersion)



Gets a specific role by name.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.RolesApi();
let deviceName = "deviceName_example"; // String | The device name.
let name = "name_example"; // String | The role name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.rolesGet(deviceName, name, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **name** | **String**| The role name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**Role**](Role.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rolesListByDataBoxEdgeDevice

> RoleList rolesListByDataBoxEdgeDevice(deviceName, subscriptionId, resourceGroupName, apiVersion)



Lists all the roles configured in a Data Box Edge/Data Box Gateway device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.RolesApi();
let deviceName = "deviceName_example"; // String | The device name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.rolesListByDataBoxEdgeDevice(deviceName, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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

[**RoleList**](RoleList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

