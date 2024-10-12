# TheJiraCloudPlatformRestApi.IssueCustomFieldConfigurationAppsApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCustomFieldConfiguration**](IssueCustomFieldConfigurationAppsApi.md#getCustomFieldConfiguration) | **GET** /rest/api/3/app/field/{fieldIdOrKey}/context/configuration | Get custom field configurations
[**updateCustomFieldConfiguration**](IssueCustomFieldConfigurationAppsApi.md#updateCustomFieldConfiguration) | **PUT** /rest/api/3/app/field/{fieldIdOrKey}/context/configuration | Update custom field configurations



## getCustomFieldConfiguration

> PageBeanContextualConfiguration getCustomFieldConfiguration(fieldIdOrKey, opts)

Get custom field configurations

Returns a [paginated](#pagination) list of configurations for a custom field created by a [Forge app](https://developer.atlassian.com/platform/forge/).  The result can be filtered by one of these criteria:   *  &#x60;id&#x60;.  *  &#x60;fieldContextId&#x60;.  *  &#x60;issueId&#x60;.  *  &#x60;projectKeyOrId&#x60; and &#x60;issueTypeId&#x60;.  Otherwise, all configurations are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the Forge app that created the custom field.

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

let apiInstance = new TheJiraCloudPlatformRestApi.IssueCustomFieldConfigurationAppsApi();
let fieldIdOrKey = "fieldIdOrKey_example"; // String | The ID or key of the custom field, for example `customfield_10000`.
let opts = {
  'id': [null], // [Number] | The list of configuration IDs. To include multiple configurations, separate IDs with an ampersand: `id=10000&id=10001`. Can't be provided with `fieldContextId`, `issueId`, `projectKeyOrId`, or `issueTypeId`.
  'fieldContextId': [null], // [Number] | The list of field context IDs. To include multiple field contexts, separate IDs with an ampersand: `fieldContextId=10000&fieldContextId=10001`. Can't be provided with `id`, `issueId`, `projectKeyOrId`, or `issueTypeId`.
  'issueId': 789, // Number | The ID of the issue to filter results by. If the issue doesn't exist, an empty list is returned. Can't be provided with `projectKeyOrId`, or `issueTypeId`.
  'projectKeyOrId': "projectKeyOrId_example", // String | The ID or key of the project to filter results by. Must be provided with `issueTypeId`. Can't be provided with `issueId`.
  'issueTypeId': "issueTypeId_example", // String | The ID of the issue type to filter results by. Must be provided with `projectKeyOrId`. Can't be provided with `issueId`.
  'startAt': 0, // Number | The index of the first item to return in a page of results (page offset).
  'maxResults': 100 // Number | The maximum number of items to return per page.
};
apiInstance.getCustomFieldConfiguration(fieldIdOrKey, opts, (error, data, response) => {
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
 **fieldIdOrKey** | **String**| The ID or key of the custom field, for example &#x60;customfield_10000&#x60;. | 
 **id** | [**[Number]**](Number.md)| The list of configuration IDs. To include multiple configurations, separate IDs with an ampersand: &#x60;id&#x3D;10000&amp;id&#x3D;10001&#x60;. Can&#39;t be provided with &#x60;fieldContextId&#x60;, &#x60;issueId&#x60;, &#x60;projectKeyOrId&#x60;, or &#x60;issueTypeId&#x60;. | [optional] 
 **fieldContextId** | [**[Number]**](Number.md)| The list of field context IDs. To include multiple field contexts, separate IDs with an ampersand: &#x60;fieldContextId&#x3D;10000&amp;fieldContextId&#x3D;10001&#x60;. Can&#39;t be provided with &#x60;id&#x60;, &#x60;issueId&#x60;, &#x60;projectKeyOrId&#x60;, or &#x60;issueTypeId&#x60;. | [optional] 
 **issueId** | **Number**| The ID of the issue to filter results by. If the issue doesn&#39;t exist, an empty list is returned. Can&#39;t be provided with &#x60;projectKeyOrId&#x60;, or &#x60;issueTypeId&#x60;. | [optional] 
 **projectKeyOrId** | **String**| The ID or key of the project to filter results by. Must be provided with &#x60;issueTypeId&#x60;. Can&#39;t be provided with &#x60;issueId&#x60;. | [optional] 
 **issueTypeId** | **String**| The ID of the issue type to filter results by. Must be provided with &#x60;projectKeyOrId&#x60;. Can&#39;t be provided with &#x60;issueId&#x60;. | [optional] 
 **startAt** | **Number**| The index of the first item to return in a page of results (page offset). | [optional] [default to 0]
 **maxResults** | **Number**| The maximum number of items to return per page. | [optional] [default to 100]

### Return type

[**PageBeanContextualConfiguration**](PageBeanContextualConfiguration.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCustomFieldConfiguration

> Object updateCustomFieldConfiguration(fieldIdOrKey, customFieldConfigurations)

Update custom field configurations

Update the configuration for contexts of a custom field created by a [Forge app](https://developer.atlassian.com/platform/forge/).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the Forge app that created the custom field.

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

let apiInstance = new TheJiraCloudPlatformRestApi.IssueCustomFieldConfigurationAppsApi();
let fieldIdOrKey = "fieldIdOrKey_example"; // String | The ID or key of the custom field, for example `customfield_10000`.
let customFieldConfigurations = {"configurations":[{"id":"10000"},{"configuration":{"maxValue":10000,"minValue":0},"id":"10001","schema":{"properties":{"amount":{"type":"number"},"currency":{"type":"string"}},"required":["amount","currency"]}}]}; // CustomFieldConfigurations | 
apiInstance.updateCustomFieldConfiguration(fieldIdOrKey, customFieldConfigurations, (error, data, response) => {
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
 **fieldIdOrKey** | **String**| The ID or key of the custom field, for example &#x60;customfield_10000&#x60;. | 
 **customFieldConfigurations** | [**CustomFieldConfigurations**](CustomFieldConfigurations.md)|  | 

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

