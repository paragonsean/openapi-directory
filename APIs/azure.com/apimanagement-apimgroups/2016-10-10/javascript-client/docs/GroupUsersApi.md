# ApiManagementClient.GroupUsersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groupUsersCreate**](GroupUsersApi.md#groupUsersCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/groups/{groupId}/users/{uid} | 
[**groupUsersDelete**](GroupUsersApi.md#groupUsersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/groups/{groupId}/users/{uid} | 
[**groupUsersListByGroups**](GroupUsersApi.md#groupUsersListByGroups) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/groups/{groupId}/users | 



## groupUsersCreate

> groupUsersCreate(resourceGroupName, serviceName, groupId, uid, apiVersion, subscriptionId)



Adds a user to the specified group.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.GroupUsersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let groupId = "groupId_example"; // String | Group identifier. Must be unique in the current API Management service instance.
let uid = "uid_example"; // String | User identifier. Must be unique in the current API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.groupUsersCreate(resourceGroupName, serviceName, groupId, uid, apiVersion, subscriptionId, (error, data, response) => {
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
 **serviceName** | **String**| The name of the API Management service. | 
 **groupId** | **String**| Group identifier. Must be unique in the current API Management service instance. | 
 **uid** | **String**| User identifier. Must be unique in the current API Management service instance. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupUsersDelete

> groupUsersDelete(resourceGroupName, serviceName, groupId, uid, apiVersion, subscriptionId)



Remove existing user from existing group.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.GroupUsersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let groupId = "groupId_example"; // String | Group identifier. Must be unique in the current API Management service instance.
let uid = "uid_example"; // String | User identifier. Must be unique in the current API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.groupUsersDelete(resourceGroupName, serviceName, groupId, uid, apiVersion, subscriptionId, (error, data, response) => {
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
 **serviceName** | **String**| The name of the API Management service. | 
 **groupId** | **String**| Group identifier. Must be unique in the current API Management service instance. | 
 **uid** | **String**| User identifier. Must be unique in the current API Management service instance. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupUsersListByGroups

> GroupUsersListByGroups200Response groupUsersListByGroups(resourceGroupName, serviceName, groupId, apiVersion, subscriptionId, opts)



Lists a collection of the members of the group, specified by its identifier.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.GroupUsersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let groupId = "groupId_example"; // String | Group identifier. Must be unique in the current API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'filter': "filter_example", // String | | Field            | Supported operators    | Supported functions               | |------------------|------------------------|-----------------------------------| | id               | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | firstName        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | lastName         | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | email            | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state            | eq                     | N/A                               | | registrationDate | ge, le, eq, ne, gt, lt | N/A                               | | note             | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |
  'top': 56, // Number | Number of records to return.
  'skip': 56 // Number | Number of records to skip.
};
apiInstance.groupUsersListByGroups(resourceGroupName, serviceName, groupId, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **serviceName** | **String**| The name of the API Management service. | 
 **groupId** | **String**| Group identifier. Must be unique in the current API Management service instance. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **filter** | **String**| | Field            | Supported operators    | Supported functions               | |------------------|------------------------|-----------------------------------| | id               | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | firstName        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | lastName         | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | email            | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state            | eq                     | N/A                               | | registrationDate | ge, le, eq, ne, gt, lt | N/A                               | | note             | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | [optional] 
 **top** | **Number**| Number of records to return. | [optional] 
 **skip** | **Number**| Number of records to skip. | [optional] 

### Return type

[**GroupUsersListByGroups200Response**](GroupUsersListByGroups200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

