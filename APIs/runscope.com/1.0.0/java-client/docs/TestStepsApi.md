# TestStepsApi

All URIs are relative to *https://api.runscope.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bucketsBucketKeyTestsTestIdStepsGet**](TestStepsApi.md#bucketsBucketKeyTestsTestIdStepsGet) | **GET** /buckets/{bucketKey}/tests/{testId}/steps | List test steps for a test. |
| [**bucketsBucketKeyTestsTestIdStepsPost**](TestStepsApi.md#bucketsBucketKeyTestsTestIdStepsPost) | **POST** /buckets/{bucketKey}/tests/{testId}/steps | Add new test step. |
| [**bucketsBucketKeyTestsTestIdStepsStepIdDelete**](TestStepsApi.md#bucketsBucketKeyTestsTestIdStepsStepIdDelete) | **DELETE** /buckets/{bucketKey}/tests/{testId}/steps/{stepId} | Delete a step from a test. |
| [**bucketsBucketKeyTestsTestIdStepsStepIdPut**](TestStepsApi.md#bucketsBucketKeyTestsTestIdStepsStepIdPut) | **PUT** /buckets/{bucketKey}/tests/{testId}/steps/{stepId} | Update the details of a single test step. |


<a id="bucketsBucketKeyTestsTestIdStepsGet"></a>
# **bucketsBucketKeyTestsTestIdStepsGet**
> bucketsBucketKeyTestsTestIdStepsGet(bucketKey, testId)

List test steps for a test.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestStepsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    TestStepsApi apiInstance = new TestStepsApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    String testId = "testId_example"; // String | Unique identifier for a test
    try {
      apiInstance.bucketsBucketKeyTestsTestIdStepsGet(bucketKey, testId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestStepsApi#bucketsBucketKeyTestsTestIdStepsGet");
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
| **200** | List of test steps for a test |  -  |

<a id="bucketsBucketKeyTestsTestIdStepsPost"></a>
# **bucketsBucketKeyTestsTestIdStepsPost**
> bucketsBucketKeyTestsTestIdStepsPost(bucketKey, testId, testStep)

Add new test step.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestStepsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    TestStepsApi apiInstance = new TestStepsApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    String testId = "testId_example"; // String | Unique identifier for a test
    TestStep testStep = new TestStep(); // TestStep | 
    try {
      apiInstance.bucketsBucketKeyTestsTestIdStepsPost(bucketKey, testId, testStep);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestStepsApi#bucketsBucketKeyTestsTestIdStepsPost");
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
| **testStep** | [**TestStep**](TestStep.md)|  | |

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Details of the new test step. |  -  |
| **400** | Must send valid JSON object to create a new test step |  -  |

<a id="bucketsBucketKeyTestsTestIdStepsStepIdDelete"></a>
# **bucketsBucketKeyTestsTestIdStepsStepIdDelete**
> bucketsBucketKeyTestsTestIdStepsStepIdDelete(bucketKey, testId, stepId)

Delete a step from a test.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestStepsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    TestStepsApi apiInstance = new TestStepsApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    String testId = "testId_example"; // String | Unique identifier for a test
    String stepId = "stepId_example"; // String | Unique identifier for a test step
    try {
      apiInstance.bucketsBucketKeyTestsTestIdStepsStepIdDelete(bucketKey, testId, stepId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestStepsApi#bucketsBucketKeyTestsTestIdStepsStepIdDelete");
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
| **stepId** | **String**| Unique identifier for a test step | |

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

<a id="bucketsBucketKeyTestsTestIdStepsStepIdPut"></a>
# **bucketsBucketKeyTestsTestIdStepsStepIdPut**
> bucketsBucketKeyTestsTestIdStepsStepIdPut(bucketKey, testId, stepId, testStep)

Update the details of a single test step.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestStepsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    TestStepsApi apiInstance = new TestStepsApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    String testId = "testId_example"; // String | Unique identifier for a test
    String stepId = "stepId_example"; // String | Unique identifier for a test step
    TestStep testStep = new TestStep(); // TestStep | 
    try {
      apiInstance.bucketsBucketKeyTestsTestIdStepsStepIdPut(bucketKey, testId, stepId, testStep);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestStepsApi#bucketsBucketKeyTestsTestIdStepsStepIdPut");
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
| **stepId** | **String**| Unique identifier for a test step | |
| **testStep** | [**TestStep**](TestStep.md)|  | |

### Return type

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of test steps for a test |  -  |
| **400** | Unable to update template &#39;{stepId}&#39; for test &#39;{testId}&#39; |  -  |

