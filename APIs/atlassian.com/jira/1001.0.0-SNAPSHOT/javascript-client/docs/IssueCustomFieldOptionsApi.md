# TheJiraCloudPlatformRestApi.IssueCustomFieldOptionsApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCustomFieldOption**](IssueCustomFieldOptionsApi.md#createCustomFieldOption) | **POST** /rest/api/3/field/{fieldId}/context/{contextId}/option | Create custom field options (context)
[**deleteCustomFieldOption**](IssueCustomFieldOptionsApi.md#deleteCustomFieldOption) | **DELETE** /rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId} | Delete custom field options (context)
[**getCustomFieldOption**](IssueCustomFieldOptionsApi.md#getCustomFieldOption) | **GET** /rest/api/3/customFieldOption/{id} | Get custom field option
[**getOptionsForContext**](IssueCustomFieldOptionsApi.md#getOptionsForContext) | **GET** /rest/api/3/field/{fieldId}/context/{contextId}/option | Get custom field options (context)
[**reorderCustomFieldOptions**](IssueCustomFieldOptionsApi.md#reorderCustomFieldOptions) | **PUT** /rest/api/3/field/{fieldId}/context/{contextId}/option/move | Reorder custom field options (context)
[**updateCustomFieldOption**](IssueCustomFieldOptionsApi.md#updateCustomFieldOption) | **PUT** /rest/api/3/field/{fieldId}/context/{contextId}/option | Update custom field options (context)



## createCustomFieldOption

> CustomFieldCreatedContextOptionsList createCustomFieldOption(fieldId, contextId, bulkCustomFieldOptionCreateRequest)

Create custom field options (context)

Creates options and, where the custom select field is of the type Select List (cascading), cascading options for a custom select field. The options are added to a context of the field.  The maximum number of options that can be created per request is 1000 and each field can have a maximum of 10000 options.  This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.**  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.IssueCustomFieldOptionsApi();
let fieldId = "fieldId_example"; // String | The ID of the custom field.
let contextId = 789; // Number | The ID of the context.
let bulkCustomFieldOptionCreateRequest = {"options":[{"disabled":false,"value":"Scranton"},{"disabled":true,"optionId":"10000","value":"Manhattan"},{"disabled":false,"value":"The Electric City"}]}; // BulkCustomFieldOptionCreateRequest | 
apiInstance.createCustomFieldOption(fieldId, contextId, bulkCustomFieldOptionCreateRequest, (error, data, response) => {
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
 **fieldId** | **String**| The ID of the custom field. | 
 **contextId** | **Number**| The ID of the context. | 
 **bulkCustomFieldOptionCreateRequest** | [**BulkCustomFieldOptionCreateRequest**](BulkCustomFieldOptionCreateRequest.md)|  | 

### Return type

[**CustomFieldCreatedContextOptionsList**](CustomFieldCreatedContextOptionsList.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteCustomFieldOption

> deleteCustomFieldOption(fieldId, contextId, optionId)

Delete custom field options (context)

Deletes a custom field option.  Options with cascading options cannot be deleted without deleting the cascading options first.  This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.**  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.IssueCustomFieldOptionsApi();
let fieldId = "fieldId_example"; // String | The ID of the custom field.
let contextId = 789; // Number | The ID of the context from which an option should be deleted.
let optionId = 789; // Number | The ID of the option to delete.
apiInstance.deleteCustomFieldOption(fieldId, contextId, optionId, (error, data, response) => {
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
 **fieldId** | **String**| The ID of the custom field. | 
 **contextId** | **Number**| The ID of the context from which an option should be deleted. | 
 **optionId** | **Number**| The ID of the option to delete. | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCustomFieldOption

> CustomFieldOption getCustomFieldOption(id)

Get custom field option

Returns a custom field option. For example, an option in a select list.  Note that this operation **only works for issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource**, it cannot be used with issue field select list options created by Connect apps.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** The custom field option is returned as follows:   *  if the user has the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).  *  if the user has the *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the custom field is used in, and the field is visible in at least one layout the user has permission to view.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.IssueCustomFieldOptionsApi();
let id = "id_example"; // String | The ID of the custom field option.
apiInstance.getCustomFieldOption(id, (error, data, response) => {
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
 **id** | **String**| The ID of the custom field option. | 

### Return type

[**CustomFieldOption**](CustomFieldOption.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getOptionsForContext

> PageBeanCustomFieldContextOption getOptionsForContext(fieldId, contextId, opts)

Get custom field options (context)

Returns a [paginated](#pagination) list of all custom field option for a context. Options are returned first then cascading options, in the order they display in Jira.  This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.**  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.IssueCustomFieldOptionsApi();
let fieldId = "fieldId_example"; // String | The ID of the custom field.
let contextId = 789; // Number | The ID of the context.
let opts = {
  'optionId': 789, // Number | The ID of the option.
  'onlyOptions': false, // Boolean | Whether only options are returned.
  'startAt': 0, // Number | The index of the first item to return in a page of results (page offset).
  'maxResults': 100 // Number | The maximum number of items to return per page.
};
apiInstance.getOptionsForContext(fieldId, contextId, opts, (error, data, response) => {
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
 **fieldId** | **String**| The ID of the custom field. | 
 **contextId** | **Number**| The ID of the context. | 
 **optionId** | **Number**| The ID of the option. | [optional] 
 **onlyOptions** | **Boolean**| Whether only options are returned. | [optional] [default to false]
 **startAt** | **Number**| The index of the first item to return in a page of results (page offset). | [optional] [default to 0]
 **maxResults** | **Number**| The maximum number of items to return per page. | [optional] [default to 100]

### Return type

[**PageBeanCustomFieldContextOption**](PageBeanCustomFieldContextOption.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reorderCustomFieldOptions

> Object reorderCustomFieldOptions(fieldId, contextId, orderOfCustomFieldOptions)

Reorder custom field options (context)

Changes the order of custom field options or cascading options in a context.  This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.**  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.IssueCustomFieldOptionsApi();
let fieldId = "fieldId_example"; // String | The ID of the custom field.
let contextId = 789; // Number | The ID of the context.
let orderOfCustomFieldOptions = {"customFieldOptionIds":["10001","10002"],"position":"First"}; // OrderOfCustomFieldOptions | 
apiInstance.reorderCustomFieldOptions(fieldId, contextId, orderOfCustomFieldOptions, (error, data, response) => {
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
 **fieldId** | **String**| The ID of the custom field. | 
 **contextId** | **Number**| The ID of the context. | 
 **orderOfCustomFieldOptions** | [**OrderOfCustomFieldOptions**](OrderOfCustomFieldOptions.md)|  | 

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCustomFieldOption

> CustomFieldUpdatedContextOptionsList updateCustomFieldOption(fieldId, contextId, bulkCustomFieldOptionUpdateRequest)

Update custom field options (context)

Updates the options of a custom field.  If any of the options are not found, no options are updated. Options where the values in the request match the current values aren&#39;t updated and aren&#39;t reported in the response.  Note that this operation **only works for issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource**, it cannot be used with issue field select list options created by Connect apps.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.IssueCustomFieldOptionsApi();
let fieldId = "fieldId_example"; // String | The ID of the custom field.
let contextId = 789; // Number | The ID of the context.
let bulkCustomFieldOptionUpdateRequest = {"options":[{"disabled":false,"id":"10001","value":"Scranton"},{"disabled":true,"id":"10002","value":"Manhattan"},{"disabled":false,"id":"10003","value":"The Electric City"}]}; // BulkCustomFieldOptionUpdateRequest | 
apiInstance.updateCustomFieldOption(fieldId, contextId, bulkCustomFieldOptionUpdateRequest, (error, data, response) => {
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
 **fieldId** | **String**| The ID of the custom field. | 
 **contextId** | **Number**| The ID of the context. | 
 **bulkCustomFieldOptionUpdateRequest** | [**BulkCustomFieldOptionUpdateRequest**](BulkCustomFieldOptionUpdateRequest.md)|  | 

### Return type

[**CustomFieldUpdatedContextOptionsList**](CustomFieldUpdatedContextOptionsList.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

