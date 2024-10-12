# MySqlManagementClient.PrivateLinkResourcesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateLinkResourcesGet**](PrivateLinkResourcesApi.md#privateLinkResourcesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/privateLinkResources/{groupName} | 
[**privateLinkResourcesListByServer**](PrivateLinkResourcesApi.md#privateLinkResourcesListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/privateLinkResources | 



## privateLinkResourcesGet

> PrivateLinkResource privateLinkResourcesGet(resourceGroupName, serverName, groupName, subscriptionId, apiVersion)



Gets a private link resource for MySQL server.

### Example

```javascript
import MySqlManagementClient from 'my_sql_management_client';
let defaultClient = MySqlManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MySqlManagementClient.PrivateLinkResourcesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let serverName = "serverName_example"; // String | The name of the server.
let groupName = "groupName_example"; // String | The name of the private link resource.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.privateLinkResourcesGet(resourceGroupName, serverName, groupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **serverName** | **String**| The name of the server. | 
 **groupName** | **String**| The name of the private link resource. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**PrivateLinkResource**](PrivateLinkResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateLinkResourcesListByServer

> PrivateLinkResourceListResult privateLinkResourcesListByServer(resourceGroupName, serverName, subscriptionId, apiVersion)



Gets the private link resources for MySQL server.

### Example

```javascript
import MySqlManagementClient from 'my_sql_management_client';
let defaultClient = MySqlManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MySqlManagementClient.PrivateLinkResourcesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let serverName = "serverName_example"; // String | The name of the server.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.privateLinkResourcesListByServer(resourceGroupName, serverName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **serverName** | **String**| The name of the server. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**PrivateLinkResourceListResult**](PrivateLinkResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

