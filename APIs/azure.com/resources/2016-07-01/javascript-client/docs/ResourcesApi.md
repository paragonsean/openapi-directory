# ResourceManagementClient.ResourcesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourcesCheckExistence**](ResourcesApi.md#resourcesCheckExistence) | **HEAD** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName} | 
[**resourcesCreateOrUpdate**](ResourcesApi.md#resourcesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName} | 
[**resourcesDelete**](ResourcesApi.md#resourcesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName} | 
[**resourcesGet**](ResourcesApi.md#resourcesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName} | 
[**resourcesList**](ResourcesApi.md#resourcesList) | **GET** /subscriptions/{subscriptionId}/resources | 
[**resourcesMoveResources**](ResourcesApi.md#resourcesMoveResources) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{sourceResourceGroupName}/moveResources | 
[**resourcesUpdate**](ResourcesApi.md#resourcesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName} | 



## resourcesCheckExistence

> resourcesCheckExistence(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId)



Checks whether resource exists.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourcesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | Resource identity.
let parentResourcePath = "parentResourcePath_example"; // String | Resource identity.
let resourceType = "resourceType_example"; // String | Resource identity.
let resourceName = "resourceName_example"; // String | Resource identity.
let apiVersion = "apiVersion_example"; // String | Api version to use.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.resourcesCheckExistence(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **resourceProviderNamespace** | **String**| Resource identity. | 
 **parentResourcePath** | **String**| Resource identity. | 
 **resourceType** | **String**| Resource identity. | 
 **resourceName** | **String**| Resource identity. | 
 **apiVersion** | **String**| Api version to use. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## resourcesCreateOrUpdate

> GenericResource resourcesCreateOrUpdate(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, parameters)



Create a resource.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourcesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | Resource identity.
let parentResourcePath = "parentResourcePath_example"; // String | Resource identity.
let resourceType = "resourceType_example"; // String | Resource identity.
let resourceName = "resourceName_example"; // String | Resource identity.
let apiVersion = "apiVersion_example"; // String | Api version to use.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ResourceManagementClient.GenericResource(); // GenericResource | Create or update resource parameters.
apiInstance.resourcesCreateOrUpdate(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceProviderNamespace** | **String**| Resource identity. | 
 **parentResourcePath** | **String**| Resource identity. | 
 **resourceType** | **String**| Resource identity. | 
 **resourceName** | **String**| Resource identity. | 
 **apiVersion** | **String**| Api version to use. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**GenericResource**](GenericResource.md)| Create or update resource parameters. | 

### Return type

[**GenericResource**](GenericResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resourcesDelete

> resourcesDelete(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId)



Delete resource and all of its resources. 

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourcesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | Resource identity.
let parentResourcePath = "parentResourcePath_example"; // String | Resource identity.
let resourceType = "resourceType_example"; // String | Resource identity.
let resourceName = "resourceName_example"; // String | Resource identity.
let apiVersion = "apiVersion_example"; // String | Api version to use.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.resourcesDelete(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **resourceProviderNamespace** | **String**| Resource identity. | 
 **parentResourcePath** | **String**| Resource identity. | 
 **resourceType** | **String**| Resource identity. | 
 **resourceName** | **String**| Resource identity. | 
 **apiVersion** | **String**| Api version to use. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## resourcesGet

> GenericResource resourcesGet(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId)



Returns a resource belonging to a resource group.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourcesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | Resource identity.
let parentResourcePath = "parentResourcePath_example"; // String | Resource identity.
let resourceType = "resourceType_example"; // String | Resource identity.
let resourceName = "resourceName_example"; // String | Resource identity.
let apiVersion = "apiVersion_example"; // String | Api version to use.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.resourcesGet(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceProviderNamespace** | **String**| Resource identity. | 
 **parentResourcePath** | **String**| Resource identity. | 
 **resourceType** | **String**| Resource identity. | 
 **resourceName** | **String**| Resource identity. | 
 **apiVersion** | **String**| Api version to use. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**GenericResource**](GenericResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesList

> ResourceListResult resourcesList(apiVersion, subscriptionId, opts)



Get all of the resources under a subscription.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourcesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.
  'expand': "expand_example", // String | The $expand query parameter.
  'top': 56 // Number | Query parameters. If null is passed returns all resource groups.
};
apiInstance.resourcesList(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **expand** | **String**| The $expand query parameter. | [optional] 
 **top** | **Number**| Query parameters. If null is passed returns all resource groups. | [optional] 

### Return type

[**ResourceListResult**](ResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesMoveResources

> resourcesMoveResources(sourceResourceGroupName, apiVersion, subscriptionId, parameters)



Move resources from one resource group to another. The resources being moved should all be in the same resource group.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourcesApi();
let sourceResourceGroupName = "sourceResourceGroupName_example"; // String | Source resource group name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ResourceManagementClient.ResourcesMoveInfo(); // ResourcesMoveInfo | move resources' parameters.
apiInstance.resourcesMoveResources(sourceResourceGroupName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **sourceResourceGroupName** | **String**| Source resource group name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ResourcesMoveInfo**](ResourcesMoveInfo.md)| move resources&#39; parameters. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## resourcesUpdate

> GenericResource resourcesUpdate(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, parameters)



Updates a resource.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourcesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group for the resource. The name is case insensitive.
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
let parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
let resourceType = "resourceType_example"; // String | The resource type of the resource to update.
let resourceName = "resourceName_example"; // String | The name of the resource to update.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ResourceManagementClient.GenericResource(); // GenericResource | Parameters for updating the resource.
apiInstance.resourcesUpdate(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group for the resource. The name is case insensitive. | 
 **resourceProviderNamespace** | **String**| The namespace of the resource provider. | 
 **parentResourcePath** | **String**| The parent resource identity. | 
 **resourceType** | **String**| The resource type of the resource to update. | 
 **resourceName** | **String**| The name of the resource to update. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**GenericResource**](GenericResource.md)| Parameters for updating the resource. | 

### Return type

[**GenericResource**](GenericResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

