# AppConfigurationManagementClient.PrivateLinkResourcesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateLinkResourcesGet**](PrivateLinkResourcesApi.md#privateLinkResourcesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateLinkResources/{groupName} | 
[**privateLinkResourcesListByConfigurationStore**](PrivateLinkResourcesApi.md#privateLinkResourcesListByConfigurationStore) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateLinkResources | 



## privateLinkResourcesGet

> PrivateLinkResource privateLinkResourcesGet(subscriptionId, resourceGroupName, configStoreName, apiVersion, groupName)



Gets a private link resource that need to be created for a configuration store.

### Example

```javascript
import AppConfigurationManagementClient from 'app_configuration_management_client';
let defaultClient = AppConfigurationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppConfigurationManagementClient.PrivateLinkResourcesApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let configStoreName = "configStoreName_example"; // String | The name of the configuration store.
let apiVersion = "apiVersion_example"; // String | The client API version.
let groupName = "groupName_example"; // String | The name of the private link resource group.
apiInstance.privateLinkResourcesGet(subscriptionId, resourceGroupName, configStoreName, apiVersion, groupName, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | 
 **configStoreName** | **String**| The name of the configuration store. | 
 **apiVersion** | **String**| The client API version. | 
 **groupName** | **String**| The name of the private link resource group. | 

### Return type

[**PrivateLinkResource**](PrivateLinkResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateLinkResourcesListByConfigurationStore

> PrivateLinkResourceListResult privateLinkResourcesListByConfigurationStore(subscriptionId, resourceGroupName, configStoreName, apiVersion)



Gets the private link resources that need to be created for a configuration store.

### Example

```javascript
import AppConfigurationManagementClient from 'app_configuration_management_client';
let defaultClient = AppConfigurationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppConfigurationManagementClient.PrivateLinkResourcesApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let configStoreName = "configStoreName_example"; // String | The name of the configuration store.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.privateLinkResourcesListByConfigurationStore(subscriptionId, resourceGroupName, configStoreName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | 
 **configStoreName** | **String**| The name of the configuration store. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

[**PrivateLinkResourceListResult**](PrivateLinkResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

