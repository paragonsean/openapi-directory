# TheJiraCloudPlatformRestApi.IssueCustomFieldValuesAppsApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updateCustomFieldValue**](IssueCustomFieldValuesAppsApi.md#updateCustomFieldValue) | **PUT** /rest/api/3/app/field/{fieldIdOrKey}/value | Update custom field value
[**updateMultipleCustomFieldValues**](IssueCustomFieldValuesAppsApi.md#updateMultipleCustomFieldValues) | **POST** /rest/api/3/app/field/value | Update custom fields



## updateCustomFieldValue

> Object updateCustomFieldValue(fieldIdOrKey, customFieldValueUpdateDetails, opts)

Update custom field value

Updates the value of a custom field on one or more issues. Custom fields can only be updated by the Forge app that created them.  **[Permissions](#permissions) required:** Only the app that created the custom field can update its values with this operation.

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

let apiInstance = new TheJiraCloudPlatformRestApi.IssueCustomFieldValuesAppsApi();
let fieldIdOrKey = "fieldIdOrKey_example"; // String | The ID or key of the custom field. For example, `customfield_10010`.
let customFieldValueUpdateDetails = {"updates":[{"issueIds":[10010],"value":"new value"}]}; // CustomFieldValueUpdateDetails | 
let opts = {
  'generateChangelog': true // Boolean | Whether to generate a changelog for this update.
};
apiInstance.updateCustomFieldValue(fieldIdOrKey, customFieldValueUpdateDetails, opts, (error, data, response) => {
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
 **fieldIdOrKey** | **String**| The ID or key of the custom field. For example, &#x60;customfield_10010&#x60;. | 
 **customFieldValueUpdateDetails** | [**CustomFieldValueUpdateDetails**](CustomFieldValueUpdateDetails.md)|  | 
 **generateChangelog** | **Boolean**| Whether to generate a changelog for this update. | [optional] [default to true]

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMultipleCustomFieldValues

> Object updateMultipleCustomFieldValues(multipleCustomFieldValuesUpdateDetails, opts)

Update custom fields

Updates the value of one or more custom fields on one or more issues. Combinations of custom field and issue should be unique within the request. Custom fields can only be updated by the Forge app that created them.  **[Permissions](#permissions) required:** Only the app that created the custom field can update its values with this operation.

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

let apiInstance = new TheJiraCloudPlatformRestApi.IssueCustomFieldValuesAppsApi();
let multipleCustomFieldValuesUpdateDetails = {"updates":[{"customField":"customfield_10010","issueIds":[10010,10011],"value":"new value"},{"customField":"customfield_10011","issueIds":[10010],"value":1000}]}; // MultipleCustomFieldValuesUpdateDetails | 
let opts = {
  'generateChangelog': true // Boolean | Whether to generate a changelog for this update.
};
apiInstance.updateMultipleCustomFieldValues(multipleCustomFieldValuesUpdateDetails, opts, (error, data, response) => {
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
 **multipleCustomFieldValuesUpdateDetails** | [**MultipleCustomFieldValuesUpdateDetails**](MultipleCustomFieldValuesUpdateDetails.md)|  | 
 **generateChangelog** | **Boolean**| Whether to generate a changelog for this update. | [optional] [default to true]

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

