# CourseMetadataApi

All URIs are relative to *https://api.iqualify.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**coursesContentIdMetadataCategoryPut**](CourseMetadataApi.md#coursesContentIdMetadataCategoryPut) | **PUT** /courses/{contentId}/metadata/category | Update course category |
| [**coursesContentIdMetadataLevelPut**](CourseMetadataApi.md#coursesContentIdMetadataLevelPut) | **PUT** /courses/{contentId}/metadata/level | Update course level |
| [**coursesContentIdMetadataTagsPut**](CourseMetadataApi.md#coursesContentIdMetadataTagsPut) | **PUT** /courses/{contentId}/metadata/tags | Update course tags |
| [**coursesContentIdMetadataTopicPut**](CourseMetadataApi.md#coursesContentIdMetadataTopicPut) | **PUT** /courses/{contentId}/metadata/topic | Update course topic |


<a id="coursesContentIdMetadataCategoryPut"></a>
# **coursesContentIdMetadataCategoryPut**
> CourseMetaResponse coursesContentIdMetadataCategoryPut(contentId, coursesContentIdMetadataCategoryPutRequest)

Update course category

Add or update course category in the metadata of a course.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CourseMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    CourseMetadataApi apiInstance = new CourseMetadataApi(defaultClient);
    String contentId = "contentId_example"; // String | The content Id
    CoursesContentIdMetadataCategoryPutRequest coursesContentIdMetadataCategoryPutRequest = new CoursesContentIdMetadataCategoryPutRequest(); // CoursesContentIdMetadataCategoryPutRequest | 
    try {
      CourseMetaResponse result = apiInstance.coursesContentIdMetadataCategoryPut(contentId, coursesContentIdMetadataCategoryPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CourseMetadataApi#coursesContentIdMetadataCategoryPut");
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
| **contentId** | **String**| The content Id | |
| **coursesContentIdMetadataCategoryPutRequest** | [**CoursesContentIdMetadataCategoryPutRequest**](CoursesContentIdMetadataCategoryPutRequest.md)|  | |

### Return type

[**CourseMetaResponse**](CourseMetaResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Course detail |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="coursesContentIdMetadataLevelPut"></a>
# **coursesContentIdMetadataLevelPut**
> CourseMetaResponse coursesContentIdMetadataLevelPut(contentId, coursesContentIdMetadataLevelPutRequest)

Update course level

Add or update the course level in the metadata of a course.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CourseMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    CourseMetadataApi apiInstance = new CourseMetadataApi(defaultClient);
    String contentId = "contentId_example"; // String | The content Id
    CoursesContentIdMetadataLevelPutRequest coursesContentIdMetadataLevelPutRequest = new CoursesContentIdMetadataLevelPutRequest(); // CoursesContentIdMetadataLevelPutRequest | 
    try {
      CourseMetaResponse result = apiInstance.coursesContentIdMetadataLevelPut(contentId, coursesContentIdMetadataLevelPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CourseMetadataApi#coursesContentIdMetadataLevelPut");
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
| **contentId** | **String**| The content Id | |
| **coursesContentIdMetadataLevelPutRequest** | [**CoursesContentIdMetadataLevelPutRequest**](CoursesContentIdMetadataLevelPutRequest.md)|  | |

### Return type

[**CourseMetaResponse**](CourseMetaResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Course detail |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="coursesContentIdMetadataTagsPut"></a>
# **coursesContentIdMetadataTagsPut**
> CourseMetaResponse coursesContentIdMetadataTagsPut(contentId, coursesContentIdMetadataTagsPutRequest)

Update course tags

Add or update course tags in the metadata of a course.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CourseMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    CourseMetadataApi apiInstance = new CourseMetadataApi(defaultClient);
    String contentId = "contentId_example"; // String | The content Id
    CoursesContentIdMetadataTagsPutRequest coursesContentIdMetadataTagsPutRequest = new CoursesContentIdMetadataTagsPutRequest(); // CoursesContentIdMetadataTagsPutRequest | 
    try {
      CourseMetaResponse result = apiInstance.coursesContentIdMetadataTagsPut(contentId, coursesContentIdMetadataTagsPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CourseMetadataApi#coursesContentIdMetadataTagsPut");
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
| **contentId** | **String**| The content Id | |
| **coursesContentIdMetadataTagsPutRequest** | [**CoursesContentIdMetadataTagsPutRequest**](CoursesContentIdMetadataTagsPutRequest.md)|  | |

### Return type

[**CourseMetaResponse**](CourseMetaResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Course detail |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="coursesContentIdMetadataTopicPut"></a>
# **coursesContentIdMetadataTopicPut**
> CourseMetaResponse coursesContentIdMetadataTopicPut(contentId, coursesContentIdMetadataTopicPutRequest)

Update course topic

Add or update the course topic in the metadata of a course.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CourseMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    CourseMetadataApi apiInstance = new CourseMetadataApi(defaultClient);
    String contentId = "contentId_example"; // String | The content Id
    CoursesContentIdMetadataTopicPutRequest coursesContentIdMetadataTopicPutRequest = new CoursesContentIdMetadataTopicPutRequest(); // CoursesContentIdMetadataTopicPutRequest | 
    try {
      CourseMetaResponse result = apiInstance.coursesContentIdMetadataTopicPut(contentId, coursesContentIdMetadataTopicPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CourseMetadataApi#coursesContentIdMetadataTopicPut");
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
| **contentId** | **String**| The content Id | |
| **coursesContentIdMetadataTopicPutRequest** | [**CoursesContentIdMetadataTopicPutRequest**](CoursesContentIdMetadataTopicPutRequest.md)|  | |

### Return type

[**CourseMetaResponse**](CourseMetaResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Course detail |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

