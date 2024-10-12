# BulkexportsV1JobApi

All URIs are relative to *https://bulkexports.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteJob**](BulkexportsV1JobApi.md#deleteJob) | **DELETE** /v1/Exports/Jobs/{JobSid} |  |
| [**fetchJob**](BulkexportsV1JobApi.md#fetchJob) | **GET** /v1/Exports/Jobs/{JobSid} |  |


<a id="deleteJob"></a>
# **deleteJob**
> deleteJob(jobSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkexportsV1JobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bulkexports.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    BulkexportsV1JobApi apiInstance = new BulkexportsV1JobApi(defaultClient);
    String jobSid = "jobSid_example"; // String | The unique string that that we created to identify the Bulk Export job
    try {
      apiInstance.deleteJob(jobSid);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkexportsV1JobApi#deleteJob");
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
| **jobSid** | **String**| The unique string that that we created to identify the Bulk Export job | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchJob"></a>
# **fetchJob**
> BulkexportsV1ExportJob fetchJob(jobSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkexportsV1JobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bulkexports.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    BulkexportsV1JobApi apiInstance = new BulkexportsV1JobApi(defaultClient);
    String jobSid = "jobSid_example"; // String | The unique string that that we created to identify the Bulk Export job
    try {
      BulkexportsV1ExportJob result = apiInstance.fetchJob(jobSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkexportsV1JobApi#fetchJob");
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
| **jobSid** | **String**| The unique string that that we created to identify the Bulk Export job | |

### Return type

[**BulkexportsV1ExportJob**](BulkexportsV1ExportJob.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

