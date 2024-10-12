# AuditLogsApi

All URIs are relative to *https://api.snyk.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getGroupLevelAuditLogs**](AuditLogsApi.md#getGroupLevelAuditLogs) | **POST** /group/{groupId}/audit | Get group level audit logs |
| [**getOrganizationLevelAuditLogs**](AuditLogsApi.md#getOrganizationLevelAuditLogs) | **POST** /org/{orgId}/audit | Get organization level audit logs |


<a id="getGroupLevelAuditLogs"></a>
# **getGroupLevelAuditLogs**
> getGroupLevelAuditLogs(groupId, from, to, page, sortOrder, getGroupLevelAuditLogsRequest)

Get group level audit logs



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
    defaultClient.setBasePath("https://api.snyk.io/v1");

    AuditLogsApi apiInstance = new AuditLogsApi(defaultClient);
    String groupId = "4a18d42f-0706-4ad0-b127-24078731fbea"; // String | The group ID. The `API_KEY` must have access to this group.
    String from = "2019-07-01"; // String | The date you wish to fetch results from, in the format YYYY-MM-DD. Default is 3 months ago. Please note that logs are only available for past 3 months.
    String to = "2019-07-07"; // String | The date you wish to fetch results until, in the format YYYY-MM-DD. Default is today. Please note that logs are only available for past 3 months.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page of results to request. Audit logs are returned in page sizes of 100
    String sortOrder = "ASC"; // String | The sort order of the returned audit logs by date. Values: `ASC`, `DESC`. Default: `DESC`.
    GetGroupLevelAuditLogsRequest getGroupLevelAuditLogsRequest = new GetGroupLevelAuditLogsRequest(); // GetGroupLevelAuditLogsRequest | 
    try {
      apiInstance.getGroupLevelAuditLogs(groupId, from, to, page, sortOrder, getGroupLevelAuditLogsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditLogsApi#getGroupLevelAuditLogs");
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
| **groupId** | **String**| The group ID. The &#x60;API_KEY&#x60; must have access to this group. | |
| **from** | **String**| The date you wish to fetch results from, in the format YYYY-MM-DD. Default is 3 months ago. Please note that logs are only available for past 3 months. | [optional] |
| **to** | **String**| The date you wish to fetch results until, in the format YYYY-MM-DD. Default is today. Please note that logs are only available for past 3 months. | [optional] |
| **page** | **BigDecimal**| The page of results to request. Audit logs are returned in page sizes of 100 | [optional] |
| **sortOrder** | **String**| The sort order of the returned audit logs by date. Values: &#x60;ASC&#x60;, &#x60;DESC&#x60;. Default: &#x60;DESC&#x60;. | [optional] |
| **getGroupLevelAuditLogsRequest** | [**GetGroupLevelAuditLogsRequest**](GetGroupLevelAuditLogsRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Link -  <br>  |

<a id="getOrganizationLevelAuditLogs"></a>
# **getOrganizationLevelAuditLogs**
> getOrganizationLevelAuditLogs(orgId, from, to, page, sortOrder, getOrganizationLevelAuditLogsRequest)

Get organization level audit logs



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
    defaultClient.setBasePath("https://api.snyk.io/v1");

    AuditLogsApi apiInstance = new AuditLogsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbea"; // String | The organization ID. The `API_KEY` must have access to this organization.
    String from = "2019-07-01"; // String | The date you wish to fetch results from, in the format YYYY-MM-DD. Default is 3 months ago. Please note that logs are only available for past 3 months.
    String to = "2019-07-07"; // String | The date you wish to fetch results until, in the format YYYY-MM-DD. Default is today. Please note that logs are only available for past 3 months.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page of results to request. Audit logs are returned in page sizes of 100.
    String sortOrder = "ASC"; // String | The sort order of the returned audit logs by date. Values: `ASC`, `DESC`. Default: `DESC`.
    GetOrganizationLevelAuditLogsRequest getOrganizationLevelAuditLogsRequest = new GetOrganizationLevelAuditLogsRequest(); // GetOrganizationLevelAuditLogsRequest | 
    try {
      apiInstance.getOrganizationLevelAuditLogs(orgId, from, to, page, sortOrder, getOrganizationLevelAuditLogsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditLogsApi#getOrganizationLevelAuditLogs");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **from** | **String**| The date you wish to fetch results from, in the format YYYY-MM-DD. Default is 3 months ago. Please note that logs are only available for past 3 months. | [optional] |
| **to** | **String**| The date you wish to fetch results until, in the format YYYY-MM-DD. Default is today. Please note that logs are only available for past 3 months. | [optional] |
| **page** | **BigDecimal**| The page of results to request. Audit logs are returned in page sizes of 100. | [optional] |
| **sortOrder** | **String**| The sort order of the returned audit logs by date. Values: &#x60;ASC&#x60;, &#x60;DESC&#x60;. Default: &#x60;DESC&#x60;. | [optional] |
| **getOrganizationLevelAuditLogsRequest** | [**GetOrganizationLevelAuditLogsRequest**](GetOrganizationLevelAuditLogsRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Link -  <br>  |

