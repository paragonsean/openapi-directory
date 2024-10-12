# NetworkManagementClient.ApplicationSecurityGroupsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicationSecurityGroupsCreateOrUpdate**](ApplicationSecurityGroupsApi.md#applicationSecurityGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationSecurityGroups/{applicationSecurityGroupName} | 
[**applicationSecurityGroupsDelete**](ApplicationSecurityGroupsApi.md#applicationSecurityGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationSecurityGroups/{applicationSecurityGroupName} | 
[**applicationSecurityGroupsGet**](ApplicationSecurityGroupsApi.md#applicationSecurityGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationSecurityGroups/{applicationSecurityGroupName} | 
[**applicationSecurityGroupsList**](ApplicationSecurityGroupsApi.md#applicationSecurityGroupsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationSecurityGroups | 
[**applicationSecurityGroupsListAll**](ApplicationSecurityGroupsApi.md#applicationSecurityGroupsListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/applicationSecurityGroups | 



## applicationSecurityGroupsCreateOrUpdate

> ApplicationSecurityGroup applicationSecurityGroupsCreateOrUpdate(resourceGroupName, applicationSecurityGroupName, apiVersion, subscriptionId, parameters)



Creates or updates an application security group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationSecurityGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let applicationSecurityGroupName = "applicationSecurityGroupName_example"; // String | The name of the application security group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.ApplicationSecurityGroup(); // ApplicationSecurityGroup | Parameters supplied to the create or update ApplicationSecurityGroup operation.
apiInstance.applicationSecurityGroupsCreateOrUpdate(resourceGroupName, applicationSecurityGroupName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **applicationSecurityGroupName** | **String**| The name of the application security group. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ApplicationSecurityGroup**](ApplicationSecurityGroup.md)| Parameters supplied to the create or update ApplicationSecurityGroup operation. | 

### Return type

[**ApplicationSecurityGroup**](ApplicationSecurityGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## applicationSecurityGroupsDelete

> applicationSecurityGroupsDelete(resourceGroupName, applicationSecurityGroupName, apiVersion, subscriptionId)



Deletes the specified application security group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationSecurityGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let applicationSecurityGroupName = "applicationSecurityGroupName_example"; // String | The name of the application security group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.applicationSecurityGroupsDelete(resourceGroupName, applicationSecurityGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **applicationSecurityGroupName** | **String**| The name of the application security group. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## applicationSecurityGroupsGet

> ApplicationSecurityGroup applicationSecurityGroupsGet(resourceGroupName, applicationSecurityGroupName, apiVersion, subscriptionId)



Gets information about the specified application security group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationSecurityGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let applicationSecurityGroupName = "applicationSecurityGroupName_example"; // String | The name of the application security group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.applicationSecurityGroupsGet(resourceGroupName, applicationSecurityGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **applicationSecurityGroupName** | **String**| The name of the application security group. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ApplicationSecurityGroup**](ApplicationSecurityGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationSecurityGroupsList

> ApplicationSecurityGroupListResult applicationSecurityGroupsList(resourceGroupName, apiVersion, subscriptionId)



Gets all the application security groups in a resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationSecurityGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.applicationSecurityGroupsList(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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

[**ApplicationSecurityGroupListResult**](ApplicationSecurityGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationSecurityGroupsListAll

> ApplicationSecurityGroupListResult applicationSecurityGroupsListAll(apiVersion, subscriptionId)



Gets all application security groups in a subscription.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationSecurityGroupsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.applicationSecurityGroupsListAll(apiVersion, subscriptionId, (error, data, response) => {
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

[**ApplicationSecurityGroupListResult**](ApplicationSecurityGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

