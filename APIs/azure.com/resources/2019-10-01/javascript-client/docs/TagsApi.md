# ResourceManagementClient.TagsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tagsCreateOrUpdate**](TagsApi.md#tagsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/tagNames/{tagName} | Creates a predefined tag name.
[**tagsCreateOrUpdateAtScope**](TagsApi.md#tagsCreateOrUpdateAtScope) | **PUT** /{scope}/providers/Microsoft.Resources/tags/default | Creates or updates the entire set of tags on a resource or subscription.
[**tagsCreateOrUpdateValue**](TagsApi.md#tagsCreateOrUpdateValue) | **PUT** /subscriptions/{subscriptionId}/tagNames/{tagName}/tagValues/{tagValue} | Creates a predefined value for a predefined tag name.
[**tagsDelete**](TagsApi.md#tagsDelete) | **DELETE** /subscriptions/{subscriptionId}/tagNames/{tagName} | Deletes a predefined tag name.
[**tagsDeleteAtScope**](TagsApi.md#tagsDeleteAtScope) | **DELETE** /{scope}/providers/Microsoft.Resources/tags/default | Deletes the entire set of tags on a resource or subscription.
[**tagsDeleteValue**](TagsApi.md#tagsDeleteValue) | **DELETE** /subscriptions/{subscriptionId}/tagNames/{tagName}/tagValues/{tagValue} | Deletes a predefined tag value for a predefined tag name.
[**tagsGetAtScope**](TagsApi.md#tagsGetAtScope) | **GET** /{scope}/providers/Microsoft.Resources/tags/default | Gets the entire set of tags on a resource or subscription.
[**tagsList**](TagsApi.md#tagsList) | **GET** /subscriptions/{subscriptionId}/tagNames | Gets a summary of tag usage under the subscription.
[**tagsUpdateAtScope**](TagsApi.md#tagsUpdateAtScope) | **PATCH** /{scope}/providers/Microsoft.Resources/tags/default | Selectively updates the set of tags on a resource or subscription.



## tagsCreateOrUpdate

> TagDetails tagsCreateOrUpdate(tagName, apiVersion, subscriptionId)

Creates a predefined tag name.

This operation allows adding a name to the list of predefined tag names for the given subscription. A tag name can have a maximum of 512 characters and is case-insensitive. Tag names cannot have the following prefixes which are reserved for Azure use: &#39;microsoft&#39;, &#39;azure&#39;, &#39;windows&#39;.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.TagsApi();
let tagName = "tagName_example"; // String | The name of the tag to create.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.tagsCreateOrUpdate(tagName, apiVersion, subscriptionId, (error, data, response) => {
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
 **tagName** | **String**| The name of the tag to create. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**TagDetails**](TagDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagsCreateOrUpdateAtScope

> TagsResource tagsCreateOrUpdateAtScope(scope, apiVersion, parameters)

Creates or updates the entire set of tags on a resource or subscription.

This operation allows adding or replacing the entire set of tags on the specified resource or subscription. The specified entity can have a maximum of 50 tags.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.TagsApi();
let scope = "scope_example"; // String | The resource scope.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let parameters = new ResourceManagementClient.TagsResource(); // TagsResource | 
apiInstance.tagsCreateOrUpdateAtScope(scope, apiVersion, parameters, (error, data, response) => {
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
 **scope** | **String**| The resource scope. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **parameters** | [**TagsResource**](TagsResource.md)|  | 

### Return type

[**TagsResource**](TagsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagsCreateOrUpdateValue

> TagValue tagsCreateOrUpdateValue(tagName, tagValue, apiVersion, subscriptionId)

Creates a predefined value for a predefined tag name.

This operation allows adding a value to the list of predefined values for an existing predefined tag name. A tag value can have a maximum of 256 characters.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.TagsApi();
let tagName = "tagName_example"; // String | The name of the tag.
let tagValue = "tagValue_example"; // String | The value of the tag to create.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.tagsCreateOrUpdateValue(tagName, tagValue, apiVersion, subscriptionId, (error, data, response) => {
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
 **tagName** | **String**| The name of the tag. | 
 **tagValue** | **String**| The value of the tag to create. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**TagValue**](TagValue.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagsDelete

> tagsDelete(tagName, apiVersion, subscriptionId)

Deletes a predefined tag name.

This operation allows deleting a name from the list of predefined tag names for the given subscription. The name being deleted must not be in use as a tag name for any resource. All predefined values for the given name must have already been deleted.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.TagsApi();
let tagName = "tagName_example"; // String | The name of the tag.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.tagsDelete(tagName, apiVersion, subscriptionId, (error, data, response) => {
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
 **tagName** | **String**| The name of the tag. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagsDeleteAtScope

> tagsDeleteAtScope(scope, apiVersion)

Deletes the entire set of tags on a resource or subscription.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.TagsApi();
let scope = "scope_example"; // String | The resource scope.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.tagsDeleteAtScope(scope, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The resource scope. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagsDeleteValue

> tagsDeleteValue(tagName, tagValue, apiVersion, subscriptionId)

Deletes a predefined tag value for a predefined tag name.

This operation allows deleting a value from the list of predefined values for an existing predefined tag name. The value being deleted must not be in use as a tag value for the given tag name for any resource.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.TagsApi();
let tagName = "tagName_example"; // String | The name of the tag.
let tagValue = "tagValue_example"; // String | The value of the tag to delete.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.tagsDeleteValue(tagName, tagValue, apiVersion, subscriptionId, (error, data, response) => {
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
 **tagName** | **String**| The name of the tag. | 
 **tagValue** | **String**| The value of the tag to delete. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagsGetAtScope

> TagsResource tagsGetAtScope(scope, apiVersion)

Gets the entire set of tags on a resource or subscription.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.TagsApi();
let scope = "scope_example"; // String | The resource scope.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.tagsGetAtScope(scope, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The resource scope. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**TagsResource**](TagsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagsList

> TagsListResult tagsList(apiVersion, subscriptionId)

Gets a summary of tag usage under the subscription.

This operation performs a union of predefined tags, resource tags, resource group tags and subscription tags, and returns a summary of usage for each tag name and value under the given subscription. In case of a large number of tags, this operation may return a previously cached result.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.TagsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.tagsList(apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**TagsListResult**](TagsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagsUpdateAtScope

> TagsResource tagsUpdateAtScope(scope, apiVersion, parameters)

Selectively updates the set of tags on a resource or subscription.

This operation allows replacing, merging or selectively deleting tags on the specified resource or subscription. The specified entity can have a maximum of 50 tags at the end of the operation. The &#39;replace&#39; option replaces the entire set of existing tags with a new set. The &#39;merge&#39; option allows adding tags with new names and updating the values of tags with existing names. The &#39;delete&#39; option allows selectively deleting tags based on given names or name/value pairs.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.TagsApi();
let scope = "scope_example"; // String | The resource scope.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let parameters = new ResourceManagementClient.TagsPatchResource(); // TagsPatchResource | 
apiInstance.tagsUpdateAtScope(scope, apiVersion, parameters, (error, data, response) => {
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
 **scope** | **String**| The resource scope. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **parameters** | [**TagsPatchResource**](TagsPatchResource.md)|  | 

### Return type

[**TagsResource**](TagsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

