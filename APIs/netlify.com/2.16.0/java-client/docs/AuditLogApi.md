# AuditLogApi

All URIs are relative to *https://api.netlify.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listAccountAuditEvents**](AuditLogApi.md#listAccountAuditEvents) | **GET** /accounts/{account_id}/audit |  |


<a id="listAccountAuditEvents"></a>
# **listAccountAuditEvents**
> List&lt;AuditLog&gt; listAccountAuditEvents(accountId, query, logType, page, perPage)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuditLogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    AuditLogApi apiInstance = new AuditLogApi(defaultClient);
    String accountId = "accountId_example"; // String | 
    String query = "query_example"; // String | 
    String logType = "logType_example"; // String | 
    Integer page = 56; // Integer | 
    Integer perPage = 56; // Integer | 
    try {
      List<AuditLog> result = apiInstance.listAccountAuditEvents(accountId, query, logType, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditLogApi#listAccountAuditEvents");
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
| **accountId** | **String**|  | |
| **query** | **String**|  | [optional] |
| **logType** | **String**|  | [optional] |
| **page** | **Integer**|  | [optional] |
| **perPage** | **Integer**|  | [optional] |

### Return type

[**List&lt;AuditLog&gt;**](AuditLog.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

