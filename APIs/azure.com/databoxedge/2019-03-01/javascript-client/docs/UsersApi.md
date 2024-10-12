# DataBoxEdgeManagementClient.UsersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersCreateOrUpdate**](UsersApi.md#usersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/users/{name} | 
[**usersDelete**](UsersApi.md#usersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/users/{name} | 
[**usersGet**](UsersApi.md#usersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/users/{name} | 
[**usersListByDataBoxEdgeDevice**](UsersApi.md#usersListByDataBoxEdgeDevice) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/users | 



## usersCreateOrUpdate

> User usersCreateOrUpdate(deviceName, name, subscriptionId, resourceGroupName, apiVersion, user)



Creates a new user or updates an existing user&#39;s information on a data box edge/gateway device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.UsersApi();
let deviceName = "deviceName_example"; // String | The device name.
let name = "name_example"; // String | The user name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
let user = new DataBoxEdgeManagementClient.User(); // User | The user details.
apiInstance.usersCreateOrUpdate(deviceName, name, subscriptionId, resourceGroupName, apiVersion, user, (error, data, response) => {
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
 **name** | **String**| The user name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 
 **user** | [**User**](User.md)| The user details. | 

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersDelete

> usersDelete(deviceName, name, subscriptionId, resourceGroupName, apiVersion)



Deletes the user on a databox edge/gateway device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.UsersApi();
let deviceName = "deviceName_example"; // String | The device name.
let name = "name_example"; // String | The user name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.usersDelete(deviceName, name, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **name** | **String**| The user name. | 
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


## usersGet

> User usersGet(deviceName, name, subscriptionId, resourceGroupName, apiVersion)



Gets the properties of the specified user.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.UsersApi();
let deviceName = "deviceName_example"; // String | The device name.
let name = "name_example"; // String | The user name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.usersGet(deviceName, name, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **name** | **String**| The user name. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**User**](User.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersListByDataBoxEdgeDevice

> UserList usersListByDataBoxEdgeDevice(deviceName, subscriptionId, resourceGroupName, apiVersion)



Gets all the users registered on a data box edge/gateway device.

### Example

```javascript
import DataBoxEdgeManagementClient from 'data_box_edge_management_client';
let defaultClient = DataBoxEdgeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataBoxEdgeManagementClient.UsersApi();
let deviceName = "deviceName_example"; // String | The device name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.usersListByDataBoxEdgeDevice(deviceName, subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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

[**UserList**](UserList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

