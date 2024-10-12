# SnykApi.AuditLogsApi

All URIs are relative to *https://api.snyk.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getGroupLevelAuditLogs**](AuditLogsApi.md#getGroupLevelAuditLogs) | **POST** /group/{groupId}/audit | Get group level audit logs
[**getOrganizationLevelAuditLogs**](AuditLogsApi.md#getOrganizationLevelAuditLogs) | **POST** /org/{orgId}/audit | Get organization level audit logs



## getGroupLevelAuditLogs

> getGroupLevelAuditLogs(groupId, opts)

Get group level audit logs



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.AuditLogsApi();
let groupId = "4a18d42f-0706-4ad0-b127-24078731fbea"; // String | The group ID. The `API_KEY` must have access to this group.
let opts = {
  'from': "2019-07-01", // String | The date you wish to fetch results from, in the format YYYY-MM-DD. Default is 3 months ago. Please note that logs are only available for past 3 months.
  'to': "2019-07-07", // String | The date you wish to fetch results until, in the format YYYY-MM-DD. Default is today. Please note that logs are only available for past 3 months.
  'page': 1, // Number | The page of results to request. Audit logs are returned in page sizes of 100
  'sortOrder': "ASC", // String | The sort order of the returned audit logs by date. Values: `ASC`, `DESC`. Default: `DESC`.
  'getGroupLevelAuditLogsRequest': new SnykApi.GetGroupLevelAuditLogsRequest() // GetGroupLevelAuditLogsRequest | 
};
apiInstance.getGroupLevelAuditLogs(groupId, opts, (error, data, response) => {
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
 **groupId** | **String**| The group ID. The &#x60;API_KEY&#x60; must have access to this group. | 
 **from** | **String**| The date you wish to fetch results from, in the format YYYY-MM-DD. Default is 3 months ago. Please note that logs are only available for past 3 months. | [optional] 
 **to** | **String**| The date you wish to fetch results until, in the format YYYY-MM-DD. Default is today. Please note that logs are only available for past 3 months. | [optional] 
 **page** | **Number**| The page of results to request. Audit logs are returned in page sizes of 100 | [optional] 
 **sortOrder** | **String**| The sort order of the returned audit logs by date. Values: &#x60;ASC&#x60;, &#x60;DESC&#x60;. Default: &#x60;DESC&#x60;. | [optional] 
 **getGroupLevelAuditLogsRequest** | [**GetGroupLevelAuditLogsRequest**](GetGroupLevelAuditLogsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8


## getOrganizationLevelAuditLogs

> getOrganizationLevelAuditLogs(orgId, opts)

Get organization level audit logs



### Example

```javascript
import SnykApi from 'snyk_api';

let apiInstance = new SnykApi.AuditLogsApi();
let orgId = "4a18d42f-0706-4ad0-b127-24078731fbea"; // String | The organization ID. The `API_KEY` must have access to this organization.
let opts = {
  'from': "2019-07-01", // String | The date you wish to fetch results from, in the format YYYY-MM-DD. Default is 3 months ago. Please note that logs are only available for past 3 months.
  'to': "2019-07-07", // String | The date you wish to fetch results until, in the format YYYY-MM-DD. Default is today. Please note that logs are only available for past 3 months.
  'page': 1, // Number | The page of results to request. Audit logs are returned in page sizes of 100.
  'sortOrder': "ASC", // String | The sort order of the returned audit logs by date. Values: `ASC`, `DESC`. Default: `DESC`.
  'getOrganizationLevelAuditLogsRequest': new SnykApi.GetOrganizationLevelAuditLogsRequest() // GetOrganizationLevelAuditLogsRequest | 
};
apiInstance.getOrganizationLevelAuditLogs(orgId, opts, (error, data, response) => {
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
 **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | 
 **from** | **String**| The date you wish to fetch results from, in the format YYYY-MM-DD. Default is 3 months ago. Please note that logs are only available for past 3 months. | [optional] 
 **to** | **String**| The date you wish to fetch results until, in the format YYYY-MM-DD. Default is today. Please note that logs are only available for past 3 months. | [optional] 
 **page** | **Number**| The page of results to request. Audit logs are returned in page sizes of 100. | [optional] 
 **sortOrder** | **String**| The sort order of the returned audit logs by date. Values: &#x60;ASC&#x60;, &#x60;DESC&#x60;. Default: &#x60;DESC&#x60;. | [optional] 
 **getOrganizationLevelAuditLogsRequest** | [**GetOrganizationLevelAuditLogsRequest**](GetOrganizationLevelAuditLogsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json; charset=utf-8

