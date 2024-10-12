# BulkexportsV1ExportApi

All URIs are relative to *https://bulkexports.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchExport**](BulkexportsV1ExportApi.md#fetchExport) | **GET** /v1/Exports/{ResourceType} |  |


<a id="fetchExport"></a>
# **fetchExport**
> BulkexportsV1Export fetchExport(resourceType)



Fetch a specific Export.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkexportsV1ExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bulkexports.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    BulkexportsV1ExportApi apiInstance = new BulkexportsV1ExportApi(defaultClient);
    String resourceType = "resourceType_example"; // String | The type of communication – Messages, Calls, Conferences, and Participants
    try {
      BulkexportsV1Export result = apiInstance.fetchExport(resourceType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkexportsV1ExportApi#fetchExport");
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
| **resourceType** | **String**| The type of communication – Messages, Calls, Conferences, and Participants | |

### Return type

[**BulkexportsV1Export**](BulkexportsV1Export.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

