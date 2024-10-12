# TheJiraCloudPlatformRestApi.IssueNavigatorSettingsApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getIssueNavigatorDefaultColumns**](IssueNavigatorSettingsApi.md#getIssueNavigatorDefaultColumns) | **GET** /rest/api/3/settings/columns | Get issue navigator default columns
[**setIssueNavigatorDefaultColumns**](IssueNavigatorSettingsApi.md#setIssueNavigatorDefaultColumns) | **PUT** /rest/api/3/settings/columns | Set issue navigator default columns



## getIssueNavigatorDefaultColumns

> [ColumnItem] getIssueNavigatorDefaultColumns()

Get issue navigator default columns

Returns the default issue navigator columns.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.IssueNavigatorSettingsApi();
apiInstance.getIssueNavigatorDefaultColumns((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[ColumnItem]**](ColumnItem.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setIssueNavigatorDefaultColumns

> Object setIssueNavigatorDefaultColumns(opts)

Set issue navigator default columns

Sets the default issue navigator columns.  The &#x60;columns&#x60; parameter accepts a navigable field value and is expressed as HTML form data. To specify multiple columns, pass multiple &#x60;columns&#x60; parameters. For example, in curl:  &#x60;curl -X PUT -d columns&#x3D;summary -d columns&#x3D;description https://your-domain.atlassian.net/rest/api/3/settings/columns&#x60;  If no column details are sent, then all default columns are removed.  A navigable field is one that can be used as a column on the issue navigator. Find details of navigable issue columns using [Get fields](#api-rest-api-3-field-get).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.IssueNavigatorSettingsApi();
let opts = {
  'requestBody': ["null"] // [String] | A navigable field value.
};
apiInstance.setIssueNavigatorDefaultColumns(opts, (error, data, response) => {
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
 **requestBody** | [**[String]**](String.md)| A navigable field value. | [optional] 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

