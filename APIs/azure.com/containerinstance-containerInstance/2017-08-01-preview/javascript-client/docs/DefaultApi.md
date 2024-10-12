# ContainerInstanceManagementClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**containerGroupsCreateOrUpdate**](DefaultApi.md#containerGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName} | Create or update container groups.
[**containerGroupsDelete**](DefaultApi.md#containerGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName} | Delete the specified container group.
[**containerGroupsGet**](DefaultApi.md#containerGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName} | Get the properties of the specified container group.
[**containerGroupsList**](DefaultApi.md#containerGroupsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ContainerInstance/containerGroups | Get a list of container groups in the specified subscription.
[**containerGroupsListByResourceGroup**](DefaultApi.md#containerGroupsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups | Get a list of container groups in the specified subscription and resource group.
[**containerLogsList**](DefaultApi.md#containerLogsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerInstance/containerGroups/{containerGroupName}/containers/{containerName}/logs | Get the logs for a specified container instance.



## containerGroupsCreateOrUpdate

> ContainerGroup containerGroupsCreateOrUpdate(subscriptionId, apiVersion, resourceGroupName, containerGroupName, containerGroup)

Create or update container groups.

Create or update container groups with specified configurations.

### Example

```javascript
import ContainerInstanceManagementClient from 'container_instance_management_client';
let defaultClient = ContainerInstanceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerInstanceManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to contain the container group to be created or updated.
let containerGroupName = "containerGroupName_example"; // String | The name of the container group to be created or updated.
let containerGroup = new ContainerInstanceManagementClient.ContainerGroup(); // ContainerGroup | The properties of the container group to be created or updated.
apiInstance.containerGroupsCreateOrUpdate(subscriptionId, apiVersion, resourceGroupName, containerGroupName, containerGroup, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version | 
 **resourceGroupName** | **String**| The name of the resource group to contain the container group to be created or updated. | 
 **containerGroupName** | **String**| The name of the container group to be created or updated. | 
 **containerGroup** | [**ContainerGroup**](ContainerGroup.md)| The properties of the container group to be created or updated. | 

### Return type

[**ContainerGroup**](ContainerGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## containerGroupsDelete

> ContainerGroup containerGroupsDelete(subscriptionId, apiVersion, resourceGroupName, containerGroupName)

Delete the specified container group.

Delete the specified container group in the specified subscription and resource group. The operation does not delete other resources provided by the user, such as volumes.

### Example

```javascript
import ContainerInstanceManagementClient from 'container_instance_management_client';
let defaultClient = ContainerInstanceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerInstanceManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the container group.
let containerGroupName = "containerGroupName_example"; // String | The name of the container group to be deleted.
apiInstance.containerGroupsDelete(subscriptionId, apiVersion, resourceGroupName, containerGroupName, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version | 
 **resourceGroupName** | **String**| The name of the resource group that contains the container group. | 
 **containerGroupName** | **String**| The name of the container group to be deleted. | 

### Return type

[**ContainerGroup**](ContainerGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## containerGroupsGet

> ContainerGroup containerGroupsGet(subscriptionId, apiVersion, resourceGroupName, containerGroupName)

Get the properties of the specified container group.

Gets the properties of the specified container group in the specified subscription and resource group. The operation returns the properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes.

### Example

```javascript
import ContainerInstanceManagementClient from 'container_instance_management_client';
let defaultClient = ContainerInstanceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerInstanceManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the container group.
let containerGroupName = "containerGroupName_example"; // String | The name of the container group.
apiInstance.containerGroupsGet(subscriptionId, apiVersion, resourceGroupName, containerGroupName, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version | 
 **resourceGroupName** | **String**| The name of the resource group that contains the container group. | 
 **containerGroupName** | **String**| The name of the container group. | 

### Return type

[**ContainerGroup**](ContainerGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## containerGroupsList

> ContainerGroupListResult containerGroupsList(subscriptionId, apiVersion)

Get a list of container groups in the specified subscription.

Get a list of container groups in the specified subscription. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes.

### Example

```javascript
import ContainerInstanceManagementClient from 'container_instance_management_client';
let defaultClient = ContainerInstanceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerInstanceManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version
apiInstance.containerGroupsList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version | 

### Return type

[**ContainerGroupListResult**](ContainerGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## containerGroupsListByResourceGroup

> ContainerGroupListResult containerGroupsListByResourceGroup(subscriptionId, apiVersion, resourceGroupName)

Get a list of container groups in the specified subscription and resource group.

Get a list of container groups in a specified subscription and resource group. This operation returns properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes.

### Example

```javascript
import ContainerInstanceManagementClient from 'container_instance_management_client';
let defaultClient = ContainerInstanceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerInstanceManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the container group.
apiInstance.containerGroupsListByResourceGroup(subscriptionId, apiVersion, resourceGroupName, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version | 
 **resourceGroupName** | **String**| The name of the resource group that contains the container group. | 

### Return type

[**ContainerGroupListResult**](ContainerGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## containerLogsList

> Logs containerLogsList(subscriptionId, apiVersion, resourceGroupName, containerName, containerGroupName, opts)

Get the logs for a specified container instance.

Get the logs for a specified container instance in a specified resource group and container group.

### Example

```javascript
import ContainerInstanceManagementClient from 'container_instance_management_client';
let defaultClient = ContainerInstanceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContainerInstanceManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the container instance.
let containerName = "containerName_example"; // String | The name of the container instance.
let containerGroupName = "containerGroupName_example"; // String | The name of the container group the container instance belongs to.
let opts = {
  'tail': 56 // Number | The number of lines to show from the tail of the container instance log. If not provided, all available logs are shown up to 4mb.
};
apiInstance.containerLogsList(subscriptionId, apiVersion, resourceGroupName, containerName, containerGroupName, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version | 
 **resourceGroupName** | **String**| The name of the resource group that contains the container instance. | 
 **containerName** | **String**| The name of the container instance. | 
 **containerGroupName** | **String**| The name of the container group the container instance belongs to. | 
 **tail** | **Number**| The number of lines to show from the tail of the container instance log. If not provided, all available logs are shown up to 4mb. | [optional] 

### Return type

[**Logs**](Logs.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

