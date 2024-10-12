# TestsApi

All URIs are relative to *https://api.runscope.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bucketsBucketKeyTestsGet**](TestsApi.md#bucketsBucketKeyTestsGet) | **GET** /buckets/{bucketKey}/tests | Returns a list of tests. |
| [**bucketsBucketKeyTestsPost**](TestsApi.md#bucketsBucketKeyTestsPost) | **POST** /buckets/{bucketKey}/tests | Create a test. |
| [**bucketsBucketKeyTestsTestIdDelete**](TestsApi.md#bucketsBucketKeyTestsTestIdDelete) | **DELETE** /buckets/{bucketKey}/tests/{testId} | Delete a test, including all steps, schedules, test-specific environments and results. |
| [**bucketsBucketKeyTestsTestIdGet**](TestsApi.md#bucketsBucketKeyTestsTestIdGet) | **GET** /buckets/{bucketKey}/tests/{testId} | Retrieve the details of a given test by ID. |
| [**bucketsBucketKeyTestsTestIdMetricsGet**](TestsApi.md#bucketsBucketKeyTestsTestIdMetricsGet) | **GET** /buckets/{bucketKey}/tests/{testId}/metrics | Return details of the test metrics for the specified timeframe. |
| [**bucketsBucketKeyTestsTestIdPut**](TestsApi.md#bucketsBucketKeyTestsTestIdPut) | **PUT** /buckets/{bucketKey}/tests/{testId} | Modify a test&#39;s name, description, default environment and its steps. To modify other individual properties of a test, make requests to the steps, environments, and schedules subresources of the test. |


<a id="bucketsBucketKeyTestsGet"></a>
# **bucketsBucketKeyTestsGet**
> BucketsBucketKeyTestsGet200Response bucketsBucketKeyTestsGet(bucketKey)

Returns a list of tests.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    TestsApi apiInstance = new TestsApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    try {
      BucketsBucketKeyTestsGet200Response result = apiInstance.bucketsBucketKeyTestsGet(bucketKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestsApi#bucketsBucketKeyTestsGet");
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

### Return type

[**BucketsBucketKeyTestsGet200Response**](BucketsBucketKeyTestsGet200Response.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of tests for this bucket |  -  |

<a id="bucketsBucketKeyTestsPost"></a>
# **bucketsBucketKeyTestsPost**
> BucketsBucketKeyTestsGet200Response bucketsBucketKeyTestsPost(bucketKey, newTest)

Create a test.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    TestsApi apiInstance = new TestsApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    Test newTest = new Test(); // Test | 
    try {
      BucketsBucketKeyTestsGet200Response result = apiInstance.bucketsBucketKeyTestsPost(bucketKey, newTest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestsApi#bucketsBucketKeyTestsPost");
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
| **newTest** | [**Test**](Test.md)|  | |

### Return type

[**BucketsBucketKeyTestsGet200Response**](BucketsBucketKeyTestsGet200Response.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of tests for this bucket |  -  |

<a id="bucketsBucketKeyTestsTestIdDelete"></a>
# **bucketsBucketKeyTestsTestIdDelete**
> bucketsBucketKeyTestsTestIdDelete(bucketKey, testId)

Delete a test, including all steps, schedules, test-specific environments and results.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    TestsApi apiInstance = new TestsApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    String testId = "testId_example"; // String | Unique identifier for a test
    try {
      apiInstance.bucketsBucketKeyTestsTestIdDelete(bucketKey, testId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestsApi#bucketsBucketKeyTestsTestIdDelete");
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

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content with no body. |  -  |

<a id="bucketsBucketKeyTestsTestIdGet"></a>
# **bucketsBucketKeyTestsTestIdGet**
> TestDetail bucketsBucketKeyTestsTestIdGet(bucketKey, testId)

Retrieve the details of a given test by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    TestsApi apiInstance = new TestsApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    String testId = "testId_example"; // String | Unique identifier for a test
    try {
      TestDetail result = apiInstance.bucketsBucketKeyTestsTestIdGet(bucketKey, testId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestsApi#bucketsBucketKeyTestsTestIdGet");
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

[**TestDetail**](TestDetail.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an object with the details of the given test. |  -  |
| **0** | Unexpected error |  -  |

<a id="bucketsBucketKeyTestsTestIdMetricsGet"></a>
# **bucketsBucketKeyTestsTestIdMetricsGet**
> Metrics bucketsBucketKeyTestsTestIdMetricsGet(bucketKey, testId)

Return details of the test metrics for the specified timeframe.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    TestsApi apiInstance = new TestsApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    String testId = "testId_example"; // String | Unique identifier for a test
    try {
      Metrics result = apiInstance.bucketsBucketKeyTestsTestIdMetricsGet(bucketKey, testId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestsApi#bucketsBucketKeyTestsTestIdMetricsGet");
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

[**Metrics**](Metrics.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of average response times and additional performance metrics belonging to this test. |  -  |

<a id="bucketsBucketKeyTestsTestIdPut"></a>
# **bucketsBucketKeyTestsTestIdPut**
> TestDetail bucketsBucketKeyTestsTestIdPut(bucketKey, testId)

Modify a test&#39;s name, description, default environment and its steps. To modify other individual properties of a test, make requests to the steps, environments, and schedules subresources of the test.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    TestsApi apiInstance = new TestsApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    String testId = "testId_example"; // String | Unique identifier for a test
    try {
      TestDetail result = apiInstance.bucketsBucketKeyTestsTestIdPut(bucketKey, testId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestsApi#bucketsBucketKeyTestsTestIdPut");
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

[**TestDetail**](TestDetail.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Returns 201 and the updated test&#39;s JSON description if the test is successfully updated. |  -  |
| **0** | Unexpected error |  -  |

