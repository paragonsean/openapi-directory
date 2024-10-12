# TestEnvironmentsApi

All URIs are relative to *https://api.runscope.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bucketsBucketKeyTestsTestIdEnvironmentsEnvironmentIdPut**](TestEnvironmentsApi.md#bucketsBucketKeyTestsTestIdEnvironmentsEnvironmentIdPut) | **PUT** /buckets/{bucketKey}/tests/{testId}/environments/{environmentId} | Update the details of a test environment. |
| [**bucketsBucketKeyTestsTestIdEnvironmentsGet**](TestEnvironmentsApi.md#bucketsBucketKeyTestsTestIdEnvironmentsGet) | **GET** /buckets/{bucketKey}/tests/{testId}/environments | Return details of the test&#39;s environments (only those that belong to the specified test) |
| [**bucketsBucketKeyTestsTestIdEnvironmentsPost**](TestEnvironmentsApi.md#bucketsBucketKeyTestsTestIdEnvironmentsPost) | **POST** /buckets/{bucketKey}/tests/{testId}/environments | Create new test environment. |


<a id="bucketsBucketKeyTestsTestIdEnvironmentsEnvironmentIdPut"></a>
# **bucketsBucketKeyTestsTestIdEnvironmentsEnvironmentIdPut**
> bucketsBucketKeyTestsTestIdEnvironmentsEnvironmentIdPut(bucketKey, testId, environmentId, modifiedEnvironment)

Update the details of a test environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    TestEnvironmentsApi apiInstance = new TestEnvironmentsApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    String testId = "testId_example"; // String | Unique identifier for a test
    String environmentId = "environmentId_example"; // String | Unique identifier for a test environment
    Environment modifiedEnvironment = new Environment(); // Environment | 
    try {
      apiInstance.bucketsBucketKeyTestsTestIdEnvironmentsEnvironmentIdPut(bucketKey, testId, environmentId, modifiedEnvironment);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestEnvironmentsApi#bucketsBucketKeyTestsTestIdEnvironmentsEnvironmentIdPut");
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
| **bucketKey** | **String**| Unique identifier for a bucket | |
| **testId** | **String**| Unique identifier for a test | |
| **environmentId** | **String**| Unique identifier for a test environment | |
| **modifiedEnvironment** | [**Environment**](Environment.md)|  | |

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Details of the modified test environment. |  -  |

<a id="bucketsBucketKeyTestsTestIdEnvironmentsGet"></a>
# **bucketsBucketKeyTestsTestIdEnvironmentsGet**
> BucketsBucketKeyTestsTestIdEnvironmentsGet200Response bucketsBucketKeyTestsTestIdEnvironmentsGet(bucketKey, testId)

Return details of the test&#39;s environments (only those that belong to the specified test)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    TestEnvironmentsApi apiInstance = new TestEnvironmentsApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    String testId = "testId_example"; // String | Unique identifier for a test
    try {
      BucketsBucketKeyTestsTestIdEnvironmentsGet200Response result = apiInstance.bucketsBucketKeyTestsTestIdEnvironmentsGet(bucketKey, testId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestEnvironmentsApi#bucketsBucketKeyTestsTestIdEnvironmentsGet");
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
| **bucketKey** | **String**| Unique identifier for a bucket | |
| **testId** | **String**| Unique identifier for a test | |

### Return type

[**BucketsBucketKeyTestsTestIdEnvironmentsGet200Response**](BucketsBucketKeyTestsTestIdEnvironmentsGet200Response.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of environments belonging to this test. |  -  |

<a id="bucketsBucketKeyTestsTestIdEnvironmentsPost"></a>
# **bucketsBucketKeyTestsTestIdEnvironmentsPost**
> bucketsBucketKeyTestsTestIdEnvironmentsPost(bucketKey, testId, newEnvironment)

Create new test environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    TestEnvironmentsApi apiInstance = new TestEnvironmentsApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    String testId = "testId_example"; // String | Unique identifier for a test
    Environment newEnvironment = new Environment(); // Environment | 
    try {
      apiInstance.bucketsBucketKeyTestsTestIdEnvironmentsPost(bucketKey, testId, newEnvironment);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestEnvironmentsApi#bucketsBucketKeyTestsTestIdEnvironmentsPost");
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
| **bucketKey** | **String**| Unique identifier for a bucket | |
| **testId** | **String**| Unique identifier for a test | |
| **newEnvironment** | [**Environment**](Environment.md)|  | |

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Details of the new test environment. |  -  |

