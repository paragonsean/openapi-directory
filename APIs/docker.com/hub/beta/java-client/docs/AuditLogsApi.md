# AuditLogsApi

All URIs are relative to *https://hub.docker.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**auditLogsGetAuditActions**](AuditLogsApi.md#auditLogsGetAuditActions) | **GET** /v2/auditlogs/{account}/actions | Returns list of audit log actions. |
| [**auditLogsGetAuditLogs**](AuditLogsApi.md#auditLogsGetAuditLogs) | **GET** /v2/auditlogs/{account} | Returns list of audit log  events. |


<a id="auditLogsGetAuditActions"></a>
# **auditLogsGetAuditActions**
> GetAuditActionsResponse auditLogsGetAuditActions(account)

Returns list of audit log actions.

Get audit log actions for a namespace to be used as a filter for querying audit events.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuditLogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    AuditLogsApi apiInstance = new AuditLogsApi(defaultClient);
    String account = "account_example"; // String | Namespace to query audit log actions for.
    try {
      GetAuditActionsResponse result = apiInstance.auditLogsGetAuditActions(account);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditLogsApi#auditLogsGetAuditActions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **account** | **String**| Namespace to query audit log actions for. | |

### Return type

[**GetAuditActionsResponse**](GetAuditActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **429** |  |  -  |
| **500** |  |  -  |
| **0** | An unexpected error response. |  -  |

<a id="auditLogsGetAuditLogs"></a>
# **auditLogsGetAuditLogs**
> GetAuditLogsResponse auditLogsGetAuditLogs(account, action, name, actor, from, to, page, pageSize)

Returns list of audit log  events.

Get audit log events for a given namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuditLogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    AuditLogsApi apiInstance = new AuditLogsApi(defaultClient);
    String account = "account_example"; // String | Namespace to query audit logs for.
    String action = "action_example"; // String | action name one of [\"repo.tag.push\", ...]. Optional parameter to filter specific audit log actions.
    String name = "name_example"; // String | name. Optional parameter to filter audit log events to a specific name. For repository events, this is the name of the repository. For organization events, this is the name of the organization. For team member events, this is the username of the team member.
    String actor = "actor_example"; // String | actor name. Optional parameter to filter audit log events to the specific user who triggered the event.
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | Start of the time window you wish to query audit events for.
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | End of the time window you wish to query audit events for.
    Integer page = 1; // Integer | page - specify page number. Page number to get.
    Integer pageSize = 25; // Integer | page_size - specify page size. Number of events to return per page.
    try {
      GetAuditLogsResponse result = apiInstance.auditLogsGetAuditLogs(account, action, name, actor, from, to, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditLogsApi#auditLogsGetAuditLogs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **account** | **String**| Namespace to query audit logs for. | |
| **action** | **String**| action name one of [\&quot;repo.tag.push\&quot;, ...]. Optional parameter to filter specific audit log actions. | [optional] |
| **name** | **String**| name. Optional parameter to filter audit log events to a specific name. For repository events, this is the name of the repository. For organization events, this is the name of the organization. For team member events, this is the username of the team member. | [optional] |
| **actor** | **String**| actor name. Optional parameter to filter audit log events to the specific user who triggered the event. | [optional] |
| **from** | **OffsetDateTime**| Start of the time window you wish to query audit events for. | [optional] |
| **to** | **OffsetDateTime**| End of the time window you wish to query audit events for. | [optional] |
| **page** | **Integer**| page - specify page number. Page number to get. | [optional] [default to 1] |
| **pageSize** | **Integer**| page_size - specify page size. Number of events to return per page. | [optional] [default to 25] |

### Return type

[**GetAuditLogsResponse**](GetAuditLogsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **429** |  |  -  |
| **500** |  |  -  |
| **0** | An unexpected error response. |  -  |

