# DefaultApi

All URIs are relative to *https://app.code-scan.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**jobGet**](DefaultApi.md#jobGet) | **GET** /job | Get the status of a job |
| [**jobPost**](DefaultApi.md#jobPost) | **POST** /job | Queues a job |


<a id="jobGet"></a>
# **jobGet**
> Job jobGet(jobId)

Get the status of a job

Fetches the status of a job

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.code-scan.com/api");
    
    // Configure HTTP basic authorization: codescan_auth
    HttpBasicAuth codescan_auth = (HttpBasicAuth) defaultClient.getAuthentication("codescan_auth");
    codescan_auth.setUsername("YOUR USERNAME");
    codescan_auth.setPassword("YOUR PASSWORD");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String jobId = "jobId_example"; // String | Id of the Job to retrieve
    try {
      Job result = apiInstance.jobGet(jobId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobGet");
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
| **jobId** | **String**| Id of the Job to retrieve | |

### Return type

[**Job**](Job.md)

### Authorization

[codescan_auth](../README.md#codescan_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Profile information for a user |  -  |
| **0** | Unexpected error |  -  |

<a id="jobPost"></a>
# **jobPost**
> Job jobPost(job)

Queues a job

Creates a new job

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.code-scan.com/api");
    
    // Configure HTTP basic authorization: codescan_auth
    HttpBasicAuth codescan_auth = (HttpBasicAuth) defaultClient.getAuthentication("codescan_auth");
    codescan_auth.setUsername("YOUR USERNAME");
    codescan_auth.setPassword("YOUR PASSWORD");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    NewJob job = new NewJob(); // NewJob | Id of the Job to retrieve
    try {
      Job result = apiInstance.jobPost(job);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#jobPost");
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
| **job** | [**NewJob**](NewJob.md)| Id of the Job to retrieve | |

### Return type

[**Job**](Job.md)

### Authorization

[codescan_auth](../README.md#codescan_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Profile information for a user |  -  |
| **0** | Unexpected error |  -  |

