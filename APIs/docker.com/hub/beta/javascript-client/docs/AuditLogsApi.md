# DockerHubApi.AuditLogsApi

All URIs are relative to *https://hub.docker.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auditLogsGetAuditActions**](AuditLogsApi.md#auditLogsGetAuditActions) | **GET** /v2/auditlogs/{account}/actions | Returns list of audit log actions.
[**auditLogsGetAuditLogs**](AuditLogsApi.md#auditLogsGetAuditLogs) | **GET** /v2/auditlogs/{account} | Returns list of audit log  events.



## auditLogsGetAuditActions

> GetAuditActionsResponse auditLogsGetAuditActions(account)

Returns list of audit log actions.

Get audit log actions for a namespace to be used as a filter for querying audit events.

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.AuditLogsApi();
let account = "account_example"; // String | Namespace to query audit log actions for.
apiInstance.auditLogsGetAuditActions(account, (error, data, response) => {
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
 **account** | **String**| Namespace to query audit log actions for. | 

### Return type

[**GetAuditActionsResponse**](GetAuditActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## auditLogsGetAuditLogs

> GetAuditLogsResponse auditLogsGetAuditLogs(account, opts)

Returns list of audit log  events.

Get audit log events for a given namespace.

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.AuditLogsApi();
let account = "account_example"; // String | Namespace to query audit logs for.
let opts = {
  'action': "action_example", // String | action name one of [\"repo.tag.push\", ...]. Optional parameter to filter specific audit log actions.
  'name': "name_example", // String | name. Optional parameter to filter audit log events to a specific name. For repository events, this is the name of the repository. For organization events, this is the name of the organization. For team member events, this is the username of the team member.
  'actor': "actor_example", // String | actor name. Optional parameter to filter audit log events to the specific user who triggered the event.
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | Start of the time window you wish to query audit events for.
  'to': new Date("2013-10-20T19:20:30+01:00"), // Date | End of the time window you wish to query audit events for.
  'page': 1, // Number | page - specify page number. Page number to get.
  'pageSize': 25 // Number | page_size - specify page size. Number of events to return per page.
};
apiInstance.auditLogsGetAuditLogs(account, opts, (error, data, response) => {
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
 **account** | **String**| Namespace to query audit logs for. | 
 **action** | **String**| action name one of [\&quot;repo.tag.push\&quot;, ...]. Optional parameter to filter specific audit log actions. | [optional] 
 **name** | **String**| name. Optional parameter to filter audit log events to a specific name. For repository events, this is the name of the repository. For organization events, this is the name of the organization. For team member events, this is the username of the team member. | [optional] 
 **actor** | **String**| actor name. Optional parameter to filter audit log events to the specific user who triggered the event. | [optional] 
 **from** | **Date**| Start of the time window you wish to query audit events for. | [optional] 
 **to** | **Date**| End of the time window you wish to query audit events for. | [optional] 
 **page** | **Number**| page - specify page number. Page number to get. | [optional] [default to 1]
 **pageSize** | **Number**| page_size - specify page size. Number of events to return per page. | [optional] [default to 25]

### Return type

[**GetAuditLogsResponse**](GetAuditLogsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

