# SharedEnvironmentsApi

All URIs are relative to *https://api.runscope.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bucketsBucketKeyEnvironmentsEnvironmentIdPut**](SharedEnvironmentsApi.md#bucketsBucketKeyEnvironmentsEnvironmentIdPut) | **PUT** /buckets/{bucketKey}/environments/{environmentId} | Update the details of a shared environment. |
| [**bucketsBucketKeyEnvironmentsGet**](SharedEnvironmentsApi.md#bucketsBucketKeyEnvironmentsGet) | **GET** /buckets/{bucketKey}/environments | Returns list of shared environments for a specified bucket. |
| [**bucketsBucketKeyEnvironmentsPost**](SharedEnvironmentsApi.md#bucketsBucketKeyEnvironmentsPost) | **POST** /buckets/{bucketKey}/environments | Create new shared environment. |


<a id="bucketsBucketKeyEnvironmentsEnvironmentIdPut"></a>
# **bucketsBucketKeyEnvironmentsEnvironmentIdPut**
> bucketsBucketKeyEnvironmentsEnvironmentIdPut(bucketKey, environmentId, modifiedEnvironment)

Update the details of a shared environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    SharedEnvironmentsApi apiInstance = new SharedEnvironmentsApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    String environmentId = "environmentId_example"; // String | Unique identifier for a test environment
    Environment modifiedEnvironment = new Environment(); // Environment | 
    try {
      apiInstance.bucketsBucketKeyEnvironmentsEnvironmentIdPut(bucketKey, environmentId, modifiedEnvironment);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedEnvironmentsApi#bucketsBucketKeyEnvironmentsEnvironmentIdPut");
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

<a id="bucketsBucketKeyEnvironmentsGet"></a>
# **bucketsBucketKeyEnvironmentsGet**
> bucketsBucketKeyEnvironmentsGet(bucketKey)

Returns list of shared environments for a specified bucket.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    SharedEnvironmentsApi apiInstance = new SharedEnvironmentsApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    try {
      apiInstance.bucketsBucketKeyEnvironmentsGet(bucketKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedEnvironmentsApi#bucketsBucketKeyEnvironmentsGet");
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

null (empty response body)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of shared environments belonging to this bucket. |  -  |

<a id="bucketsBucketKeyEnvironmentsPost"></a>
# **bucketsBucketKeyEnvironmentsPost**
> bucketsBucketKeyEnvironmentsPost(bucketKey, newEnvironment)

Create new shared environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    SharedEnvironmentsApi apiInstance = new SharedEnvironmentsApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    Environment newEnvironment = new Environment(); // Environment | 
    try {
      apiInstance.bucketsBucketKeyEnvironmentsPost(bucketKey, newEnvironment);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedEnvironmentsApi#bucketsBucketKeyEnvironmentsPost");
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

