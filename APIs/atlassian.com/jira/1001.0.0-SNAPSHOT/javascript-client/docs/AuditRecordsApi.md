# TheJiraCloudPlatformRestApi.AuditRecordsApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAuditRecords**](AuditRecordsApi.md#getAuditRecords) | **GET** /rest/api/3/auditing/record | Get audit records



## getAuditRecords

> AuditRecords getAuditRecords(opts)

Get audit records

Returns a list of audit records. The list can be filtered to include items:   *  where each item in &#x60;filter&#x60; has at least one match in any of these fields:           *  &#x60;summary&#x60;      *  &#x60;category&#x60;      *  &#x60;eventSource&#x60;      *  &#x60;objectItem.name&#x60; If the object is a user, account ID is available to filter.      *  &#x60;objectItem.parentName&#x60;      *  &#x60;objectItem.typeName&#x60;      *  &#x60;changedValues.changedFrom&#x60;      *  &#x60;changedValues.changedTo&#x60;      *  &#x60;remoteAddress&#x60;          For example, if &#x60;filter&#x60; contains *man ed*, an audit record containing &#x60;summary\&quot;: \&quot;User added to group\&quot;&#x60; and &#x60;\&quot;category\&quot;: \&quot;group management\&quot;&#x60; is returned.  *  created on or after a date and time.  *  created or or before a date and time.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

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

let apiInstance = new TheJiraCloudPlatformRestApi.AuditRecordsApi();
let opts = {
  'offset': 0, // Number | The number of records to skip before returning the first result.
  'limit': 1000, // Number | The maximum number of results to return.
  'filter': "filter_example", // String | The strings to match with audit field content, space separated.
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | The date and time on or after which returned audit records must have been created. If `to` is provided `from` must be before `to` or no audit records are returned.
  'to': new Date("2013-10-20T19:20:30+01:00") // Date | The date and time on or before which returned audit results must have been created. If `from` is provided `to` must be after `from` or no audit records are returned.
};
apiInstance.getAuditRecords(opts, (error, data, response) => {
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
 **offset** | **Number**| The number of records to skip before returning the first result. | [optional] [default to 0]
 **limit** | **Number**| The maximum number of results to return. | [optional] [default to 1000]
 **filter** | **String**| The strings to match with audit field content, space separated. | [optional] 
 **from** | **Date**| The date and time on or after which returned audit records must have been created. If &#x60;to&#x60; is provided &#x60;from&#x60; must be before &#x60;to&#x60; or no audit records are returned. | [optional] 
 **to** | **Date**| The date and time on or before which returned audit results must have been created. If &#x60;from&#x60; is provided &#x60;to&#x60; must be after &#x60;from&#x60; or no audit records are returned. | [optional] 

### Return type

[**AuditRecords**](AuditRecords.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

