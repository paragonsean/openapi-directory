# AuditingApi

All URIs are relative to *http://backend.id4i.de*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listOrganizationChangeLog**](AuditingApi.md#listOrganizationChangeLog) | **GET** /api/v1/changelog/organization/{organizationId}/ | List change log entries of an organization |


<a id="listOrganizationChangeLog"></a>
# **listOrganizationChangeLog**
> PaginatedResponseOfChangeLogEntry listOrganizationChangeLog(organizationId, messageMimeType, fromDate, toDate, offset, limit)

List change log entries of an organization

Listing change log entries of the specified organization id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuditingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://backend.id4i.de");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AuditingApi apiInstance = new AuditingApi(defaultClient);
    String organizationId = "organizationId_example"; // String | The namespace identifying the organization whose change log entries are to be listed
    String messageMimeType = "text/mustache"; // String | The Mime-type for the message format that should be returned. e.g. 'text/plain' or 'text/mustache' 
    OffsetDateTime fromDate = OffsetDateTime.now(); // OffsetDateTime | From date time as UTC Date-Time format
    OffsetDateTime toDate = OffsetDateTime.now(); // OffsetDateTime | To date time as UTC Date-Time format
    Integer offset = 56; // Integer | Start with the n-th element
    Integer limit = 56; // Integer | The maximum count of returned elements
    try {
      PaginatedResponseOfChangeLogEntry result = apiInstance.listOrganizationChangeLog(organizationId, messageMimeType, fromDate, toDate, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuditingApi#listOrganizationChangeLog");
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
| **organizationId** | **String**| The namespace identifying the organization whose change log entries are to be listed | |
| **messageMimeType** | **String**| The Mime-type for the message format that should be returned. e.g. &#39;text/plain&#39; or &#39;text/mustache&#39;  | [optional] [default to text/mustache] |
| **fromDate** | **OffsetDateTime**| From date time as UTC Date-Time format | [optional] |
| **toDate** | **OffsetDateTime**| To date time as UTC Date-Time format | [optional] |
| **offset** | **Integer**| Start with the n-th element | [optional] |
| **limit** | **Integer**| The maximum count of returned elements | [optional] |

### Return type

[**PaginatedResponseOfChangeLogEntry**](PaginatedResponseOfChangeLogEntry.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method not allowed |  -  |
| **406** | Not Acceptable |  -  |
| **415** | Unsupported Media Type |  -  |
| **500** | Internal Server Error |  -  |

