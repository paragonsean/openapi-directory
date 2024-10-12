# ResourceManagementClient.TagsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tagsCreateOrUpdate**](TagsApi.md#tagsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/tagNames/{tagName} | 
[**tagsCreateOrUpdateValue**](TagsApi.md#tagsCreateOrUpdateValue) | **PUT** /subscriptions/{subscriptionId}/tagNames/{tagName}/tagValues/{tagValue} | 
[**tagsDelete**](TagsApi.md#tagsDelete) | **DELETE** /subscriptions/{subscriptionId}/tagNames/{tagName} | 
[**tagsDeleteValue**](TagsApi.md#tagsDeleteValue) | **DELETE** /subscriptions/{subscriptionId}/tagNames/{tagName}/tagValues/{tagValue} | 
[**tagsList**](TagsApi.md#tagsList) | **GET** /subscriptions/{subscriptionId}/tagNames | 



## tagsCreateOrUpdate

> TagDetails tagsCreateOrUpdate(tagName, apiVersion, subscriptionId)



Create a subscription resource tag.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.TagsApi();
let tagName = "tagName_example"; // String | The name of the tag.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
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
 **tagName** | **String**| The name of the tag. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**TagDetails**](TagDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagsCreateOrUpdateValue

> TagValue tagsCreateOrUpdateValue(tagName, tagValue, apiVersion, subscriptionId)



Create a subscription resource tag value.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.TagsApi();
let tagName = "tagName_example"; // String | The name of the tag.
let tagValue = "tagValue_example"; // String | The value of the tag.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
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
 **tagValue** | **String**| The value of the tag. | 
 **apiVersion** | **String**| Client Api Version. | 
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



Delete a subscription resource tag.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.TagsApi();
let tagName = "tagName_example"; // String | The name of the tag.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## tagsDeleteValue

> tagsDeleteValue(tagName, tagValue, apiVersion, subscriptionId)



Delete a subscription resource tag value.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.TagsApi();
let tagName = "tagName_example"; // String | The name of the tag.
let tagValue = "tagValue_example"; // String | The value of the tag.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
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
 **tagValue** | **String**| The value of the tag. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## tagsList

> TagsListResult tagsList(apiVersion, subscriptionId)



Get a list of subscription resource tags.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.TagsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**TagsListResult**](TagsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

