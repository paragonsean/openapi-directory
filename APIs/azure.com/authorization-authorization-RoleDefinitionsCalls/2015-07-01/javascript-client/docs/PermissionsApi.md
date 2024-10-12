# AuthorizationManagementClient.PermissionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**permissionsListForResource**](PermissionsApi.md#permissionsListForResource) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/permissions | 
[**permissionsListForResourceGroup**](PermissionsApi.md#permissionsListForResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Authorization/permissions | 



## permissionsListForResource

> PermissionGetResult permissionsListForResource(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId)



Gets all permissions the caller has for a resource.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.PermissionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the resource. The name is case insensitive.
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
let parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
let resourceType = "resourceType_example"; // String | The resource type of the resource.
let resourceName = "resourceName_example"; // String | The name of the resource to get the permissions for.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.permissionsListForResource(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the resource. The name is case insensitive. | 
 **resourceProviderNamespace** | **String**| The namespace of the resource provider. | 
 **parentResourcePath** | **String**| The parent resource identity. | 
 **resourceType** | **String**| The resource type of the resource. | 
 **resourceName** | **String**| The name of the resource to get the permissions for. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**PermissionGetResult**](PermissionGetResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## permissionsListForResourceGroup

> PermissionGetResult permissionsListForResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets all permissions the caller has for a resource group.

### Example

```javascript
import AuthorizationManagementClient from 'authorization_management_client';
let defaultClient = AuthorizationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthorizationManagementClient.PermissionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get the permissions for. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.permissionsListForResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group to get the permissions for. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**PermissionGetResult**](PermissionGetResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

