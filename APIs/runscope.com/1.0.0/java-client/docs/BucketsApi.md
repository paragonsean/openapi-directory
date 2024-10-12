# BucketsApi

All URIs are relative to *https://api.runscope.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bucketsBucketKeyDelete**](BucketsApi.md#bucketsBucketKeyDelete) | **DELETE** /buckets/{bucketKey} | Delete a single bucket resource. |
| [**bucketsBucketKeyGet**](BucketsApi.md#bucketsBucketKeyGet) | **GET** /buckets/{bucketKey} | Returns a single bucket resource. |
| [**bucketsGet**](BucketsApi.md#bucketsGet) | **GET** /buckets | Returns a list of buckets. |
| [**bucketsPost**](BucketsApi.md#bucketsPost) | **POST** /buckets | Create a new bucket |


<a id="bucketsBucketKeyDelete"></a>
# **bucketsBucketKeyDelete**
> bucketsBucketKeyDelete(bucketKey)

Delete a single bucket resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    try {
      apiInstance.bucketsBucketKeyDelete(bucketKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#bucketsBucketKeyDelete");
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content with no body. |  -  |
| **0** | Unexpected error |  -  |

<a id="bucketsBucketKeyGet"></a>
# **bucketsBucketKeyGet**
> Bucket bucketsBucketKeyGet(bucketKey)

Returns a single bucket resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    String bucketKey = "bucketKey_example"; // String | Unique identifier for a bucket
    try {
      Bucket result = apiInstance.bucketsBucketKeyGet(bucketKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#bucketsBucketKeyGet");
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

[**Bucket**](Bucket.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bucket details. |  -  |
| **0** | Unexpected error |  -  |

<a id="bucketsGet"></a>
# **bucketsGet**
> BucketsGet200Response bucketsGet()

Returns a list of buckets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    try {
      BucketsGet200Response result = apiInstance.bucketsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#bucketsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BucketsGet200Response**](BucketsGet200Response.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of buckets associated with this authenticated account. |  -  |
| **0** | Unexpected error |  -  |

<a id="bucketsPost"></a>
# **bucketsPost**
> Bucket bucketsPost(newBucket)

Create a new bucket

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BucketsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.runscope.com");
    
    // Configure OAuth2 access token for authorization: runscope_auth
    OAuth runscope_auth = (OAuth) defaultClient.getAuthentication("runscope_auth");
    runscope_auth.setAccessToken("YOUR ACCESS TOKEN");

    BucketsApi apiInstance = new BucketsApi(defaultClient);
    NewBucket newBucket = new NewBucket(); // NewBucket | 
    try {
      Bucket result = apiInstance.bucketsPost(newBucket);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BucketsApi#bucketsPost");
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
| **newBucket** | [**NewBucket**](NewBucket.md)|  | |

### Return type

[**Bucket**](Bucket.md)

### Authorization

[runscope_auth](../README.md#runscope_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bucket details. |  -  |
| **0** | Unexpected error |  -  |

