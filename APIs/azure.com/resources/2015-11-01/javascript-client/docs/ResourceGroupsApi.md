# ResourceManagementClient.ResourceGroupsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourceGroupsCheckExistence**](ResourceGroupsApi.md#resourceGroupsCheckExistence) | **HEAD** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName} | 
[**resourceGroupsCreateOrUpdate**](ResourceGroupsApi.md#resourceGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName} | 
[**resourceGroupsDelete**](ResourceGroupsApi.md#resourceGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName} | 
[**resourceGroupsGet**](ResourceGroupsApi.md#resourceGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName} | 
[**resourceGroupsList**](ResourceGroupsApi.md#resourceGroupsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups | 
[**resourceGroupsListResources**](ResourceGroupsApi.md#resourceGroupsListResources) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/resources | 
[**resourceGroupsPatch**](ResourceGroupsApi.md#resourceGroupsPatch) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName} | 



## resourceGroupsCheckExistence

> resourceGroupsCheckExistence(resourceGroupName, apiVersion, subscriptionId)



Checks whether resource group exists.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourceGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to check. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.resourceGroupsCheckExistence(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group to check. The name is case insensitive. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## resourceGroupsCreateOrUpdate

> ResourceGroup resourceGroupsCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, parameters)



Create a resource group.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourceGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to be created or updated.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ResourceManagementClient.ResourceGroup(); // ResourceGroup | Parameters supplied to the create or update resource group service operation.
apiInstance.resourceGroupsCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group to be created or updated. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ResourceGroup**](ResourceGroup.md)| Parameters supplied to the create or update resource group service operation. | 

### Return type

[**ResourceGroup**](ResourceGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resourceGroupsDelete

> resourceGroupsDelete(resourceGroupName, apiVersion, subscriptionId)



Begin deleting resource group.To determine whether the operation has finished processing the request, call GetLongRunningOperationStatus.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourceGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to be deleted. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.resourceGroupsDelete(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group to be deleted. The name is case insensitive. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## resourceGroupsGet

> ResourceGroup resourceGroupsGet(resourceGroupName, apiVersion, subscriptionId)



Get a resource group.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourceGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.resourceGroupsGet(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ResourceGroup**](ResourceGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourceGroupsList

> ResourceGroupListResult resourceGroupsList(apiVersion, subscriptionId, opts)



Gets a collection of resource groups.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourceGroupsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.
  'top': 56 // Number | Query parameters. If null is passed returns all resource groups.
};
apiInstance.resourceGroupsList(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 
 **top** | **Number**| Query parameters. If null is passed returns all resource groups. | [optional] 

### Return type

[**ResourceGroupListResult**](ResourceGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourceGroupsListResources

> ResourceListResult resourceGroupsListResources(resourceGroupName, apiVersion, subscriptionId, opts)



Get all of the resources under a subscription.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourceGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Query parameters. If null is passed returns all resource groups.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.
  'top': 56 // Number | Query parameters. If null is passed returns all resource groups.
};
apiInstance.resourceGroupsListResources(resourceGroupName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Query parameters. If null is passed returns all resource groups. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 
 **top** | **Number**| Query parameters. If null is passed returns all resource groups. | [optional] 

### Return type

[**ResourceListResult**](ResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourceGroupsPatch

> ResourceGroup resourceGroupsPatch(resourceGroupName, apiVersion, subscriptionId, parameters)



Resource groups can be updated through a simple PATCH operation to a group address. The format of the request is the same as that for creating a resource groups, though if a field is unspecified current value will be carried over. 

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourceGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to be created or updated. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ResourceManagementClient.ResourceGroup(); // ResourceGroup | Parameters supplied to the update state resource group service operation.
apiInstance.resourceGroupsPatch(resourceGroupName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group to be created or updated. The name is case insensitive. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ResourceGroup**](ResourceGroup.md)| Parameters supplied to the update state resource group service operation. | 

### Return type

[**ResourceGroup**](ResourceGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

