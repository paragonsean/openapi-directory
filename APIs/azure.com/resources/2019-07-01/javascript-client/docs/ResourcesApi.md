# ResourceManagementClient.ResourcesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resourcesCheckExistence**](ResourcesApi.md#resourcesCheckExistence) | **HEAD** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName} | 
[**resourcesCheckExistenceById**](ResourcesApi.md#resourcesCheckExistenceById) | **HEAD** /{resourceId} | 
[**resourcesCreateOrUpdate**](ResourcesApi.md#resourcesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName} | 
[**resourcesCreateOrUpdateById**](ResourcesApi.md#resourcesCreateOrUpdateById) | **PUT** /{resourceId} | 
[**resourcesDelete**](ResourcesApi.md#resourcesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName} | 
[**resourcesDeleteById**](ResourcesApi.md#resourcesDeleteById) | **DELETE** /{resourceId} | 
[**resourcesGet**](ResourcesApi.md#resourcesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName} | 
[**resourcesGetById**](ResourcesApi.md#resourcesGetById) | **GET** /{resourceId} | 
[**resourcesList**](ResourcesApi.md#resourcesList) | **GET** /subscriptions/{subscriptionId}/resources | 
[**resourcesMoveResources**](ResourcesApi.md#resourcesMoveResources) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{sourceResourceGroupName}/moveResources | Moves resources from one resource group to another resource group.
[**resourcesUpdate**](ResourcesApi.md#resourcesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName} | 
[**resourcesUpdateById**](ResourcesApi.md#resourcesUpdateById) | **PATCH** /{resourceId} | 
[**resourcesValidateMoveResources**](ResourcesApi.md#resourcesValidateMoveResources) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{sourceResourceGroupName}/validateMoveResources | Validates whether resources can be moved from one resource group to another resource group.



## resourcesCheckExistence

> resourcesCheckExistence(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId)



Checks whether a resource exists.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourcesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the resource to check. The name is case insensitive.
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The resource provider of the resource to check.
let parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
let resourceType = "resourceType_example"; // String | The resource type.
let resourceName = "resourceName_example"; // String | The name of the resource to check whether it exists.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
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
 **resourceGroupName** | **String**| The name of the resource group containing the resource to check. The name is case insensitive. | 
 **resourceProviderNamespace** | **String**| The resource provider of the resource to check. | 
 **parentResourcePath** | **String**| The parent resource identity. | 
 **resourceType** | **String**| The resource type. | 
 **resourceName** | **String**| The name of the resource to check whether it exists. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesCheckExistenceById

> resourcesCheckExistenceById(resourceId, apiVersion)



Checks by ID whether a resource exists.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourcesApi();
let resourceId = "resourceId_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name}
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
apiInstance.resourcesCheckExistenceById(resourceId, apiVersion, (error, data, response) => {
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
 **resourceId** | **String**| The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name} | 
 **apiVersion** | **String**| The API version to use for the operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesCreateOrUpdate

> GenericResource resourcesCreateOrUpdate(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, parameters)



Creates a resource.

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
let resourceType = "resourceType_example"; // String | The resource type of the resource to create.
let resourceName = "resourceName_example"; // String | The name of the resource to create.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new ResourceManagementClient.GenericResource(); // GenericResource | Parameters for creating or updating the resource.
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
 **resourceGroupName** | **String**| The name of the resource group for the resource. The name is case insensitive. | 
 **resourceProviderNamespace** | **String**| The namespace of the resource provider. | 
 **parentResourcePath** | **String**| The parent resource identity. | 
 **resourceType** | **String**| The resource type of the resource to create. | 
 **resourceName** | **String**| The name of the resource to create. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**GenericResource**](GenericResource.md)| Parameters for creating or updating the resource. | 

### Return type

[**GenericResource**](GenericResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resourcesCreateOrUpdateById

> GenericResource resourcesCreateOrUpdateById(resourceId, apiVersion, parameters)



Create a resource by ID.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourcesApi();
let resourceId = "resourceId_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name}
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let parameters = new ResourceManagementClient.GenericResource(); // GenericResource | Create or update resource parameters.
apiInstance.resourcesCreateOrUpdateById(resourceId, apiVersion, parameters, (error, data, response) => {
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
 **resourceId** | **String**| The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name} | 
 **apiVersion** | **String**| The API version to use for the operation. | 
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



Deletes a resource.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourcesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource to delete. The name is case insensitive.
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
let parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
let resourceType = "resourceType_example"; // String | The resource type.
let resourceName = "resourceName_example"; // String | The name of the resource to delete.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource to delete. The name is case insensitive. | 
 **resourceProviderNamespace** | **String**| The namespace of the resource provider. | 
 **parentResourcePath** | **String**| The parent resource identity. | 
 **resourceType** | **String**| The resource type. | 
 **resourceName** | **String**| The name of the resource to delete. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesDeleteById

> resourcesDeleteById(resourceId, apiVersion)



Deletes a resource by ID.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourcesApi();
let resourceId = "resourceId_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name}
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
apiInstance.resourcesDeleteById(resourceId, apiVersion, (error, data, response) => {
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
 **resourceId** | **String**| The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name} | 
 **apiVersion** | **String**| The API version to use for the operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesGet

> GenericResource resourcesGet(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId)



Gets a resource.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourcesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the resource to get. The name is case insensitive.
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
let parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
let resourceType = "resourceType_example"; // String | The resource type of the resource.
let resourceName = "resourceName_example"; // String | The name of the resource to get.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
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
 **resourceGroupName** | **String**| The name of the resource group containing the resource to get. The name is case insensitive. | 
 **resourceProviderNamespace** | **String**| The namespace of the resource provider. | 
 **parentResourcePath** | **String**| The parent resource identity. | 
 **resourceType** | **String**| The resource type of the resource. | 
 **resourceName** | **String**| The name of the resource to get. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**GenericResource**](GenericResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesGetById

> GenericResource resourcesGetById(resourceId, apiVersion)



Gets a resource by ID.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourcesApi();
let resourceId = "resourceId_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name}
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
apiInstance.resourcesGetById(resourceId, apiVersion, (error, data, response) => {
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
 **resourceId** | **String**| The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name} | 
 **apiVersion** | **String**| The API version to use for the operation. | 

### Return type

[**GenericResource**](GenericResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesList

> ResourceListResult resourcesList(apiVersion, subscriptionId, opts)



Get all the resources in a subscription.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourcesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.<br><br>The properties you can use for eq (equals) or ne (not equals) are: location, resourceType, name, resourceGroup, identity, identity/principalId, plan, plan/publisher, plan/product, plan/name, plan/version, and plan/promotionCode.<br><br>For example, to filter by a resource type, use: $filter=resourceType eq 'Microsoft.Network/virtualNetworks'<br><br>You can use substringof(value, property) in the filter. The properties you can use for substring are: name and resourceGroup.<br><br>For example, to get all resources with 'demo' anywhere in the name, use: $filter=substringof('demo', name)<br><br>You can link more than one substringof together by adding and/or operators.<br><br>You can filter by tag names and values. For example, to filter for a tag name and value, use $filter=tagName eq 'tag1' and tagValue eq 'Value1'<br><br>You can use some properties together when filtering. The combinations you can use are: substringof and/or resourceType, plan and plan/publisher and plan/name, identity and identity/principalId.
  'expand': "expand_example", // String | The $expand query parameter. You can expand createdTime and changedTime. For example, to expand both properties, use $expand=changedTime,createdTime
  'top': 56 // Number | The number of results to return. If null is passed, returns all resource groups.
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **filter** | **String**| The filter to apply on the operation.&lt;br&gt;&lt;br&gt;The properties you can use for eq (equals) or ne (not equals) are: location, resourceType, name, resourceGroup, identity, identity/principalId, plan, plan/publisher, plan/product, plan/name, plan/version, and plan/promotionCode.&lt;br&gt;&lt;br&gt;For example, to filter by a resource type, use: $filter&#x3D;resourceType eq &#39;Microsoft.Network/virtualNetworks&#39;&lt;br&gt;&lt;br&gt;You can use substringof(value, property) in the filter. The properties you can use for substring are: name and resourceGroup.&lt;br&gt;&lt;br&gt;For example, to get all resources with &#39;demo&#39; anywhere in the name, use: $filter&#x3D;substringof(&#39;demo&#39;, name)&lt;br&gt;&lt;br&gt;You can link more than one substringof together by adding and/or operators.&lt;br&gt;&lt;br&gt;You can filter by tag names and values. For example, to filter for a tag name and value, use $filter&#x3D;tagName eq &#39;tag1&#39; and tagValue eq &#39;Value1&#39;&lt;br&gt;&lt;br&gt;You can use some properties together when filtering. The combinations you can use are: substringof and/or resourceType, plan and plan/publisher and plan/name, identity and identity/principalId. | [optional] 
 **expand** | **String**| The $expand query parameter. You can expand createdTime and changedTime. For example, to expand both properties, use $expand&#x3D;changedTime,createdTime | [optional] 
 **top** | **Number**| The number of results to return. If null is passed, returns all resource groups. | [optional] 

### Return type

[**ResourceListResult**](ResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourcesMoveResources

> resourcesMoveResources(sourceResourceGroupName, apiVersion, subscriptionId, parameters)

Moves resources from one resource group to another resource group.

The resources to move must be in the same source resource group. The target resource group may be in a different subscription. When moving resources, both the source group and the target group are locked for the duration of the operation. Write and delete operations are blocked on the groups until the move completes. 

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourcesApi();
let sourceResourceGroupName = "sourceResourceGroupName_example"; // String | The name of the resource group containing the resources to move.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new ResourceManagementClient.ResourcesMoveInfo(); // ResourcesMoveInfo | Parameters for moving resources.
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
 **sourceResourceGroupName** | **String**| The name of the resource group containing the resources to move. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**ResourcesMoveInfo**](ResourcesMoveInfo.md)| Parameters for moving resources. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


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
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**GenericResource**](GenericResource.md)| Parameters for updating the resource. | 

### Return type

[**GenericResource**](GenericResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resourcesUpdateById

> GenericResource resourcesUpdateById(resourceId, apiVersion, parameters)



Updates a resource by ID.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourcesApi();
let resourceId = "resourceId_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name}
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let parameters = new ResourceManagementClient.GenericResource(); // GenericResource | Update resource parameters.
apiInstance.resourcesUpdateById(resourceId, apiVersion, parameters, (error, data, response) => {
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
 **resourceId** | **String**| The fully qualified ID of the resource, including the resource name and resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/{resource-provider-namespace}/{resource-type}/{resource-name} | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **parameters** | [**GenericResource**](GenericResource.md)| Update resource parameters. | 

### Return type

[**GenericResource**](GenericResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resourcesValidateMoveResources

> resourcesValidateMoveResources(sourceResourceGroupName, apiVersion, subscriptionId, parameters)

Validates whether resources can be moved from one resource group to another resource group.

This operation checks whether the specified resources can be moved to the target. The resources to move must be in the same source resource group. The target resource group may be in a different subscription. If validation succeeds, it returns HTTP response code 204 (no content). If validation fails, it returns HTTP response code 409 (Conflict) with an error message. Retrieve the URL in the Location header value to check the result of the long-running operation.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.ResourcesApi();
let sourceResourceGroupName = "sourceResourceGroupName_example"; // String | The name of the resource group containing the resources to validate for move.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new ResourceManagementClient.ResourcesMoveInfo(); // ResourcesMoveInfo | Parameters for moving resources.
apiInstance.resourcesValidateMoveResources(sourceResourceGroupName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **sourceResourceGroupName** | **String**| The name of the resource group containing the resources to validate for move. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**ResourcesMoveInfo**](ResourcesMoveInfo.md)| Parameters for moving resources. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

