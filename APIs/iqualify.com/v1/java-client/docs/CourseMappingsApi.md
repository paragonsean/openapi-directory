# CourseMappingsApi

All URIs are relative to *https://api.iqualify.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**courseMappingsExternalcourseExternalCourseIdGet**](CourseMappingsApi.md#courseMappingsExternalcourseExternalCourseIdGet) | **GET** /course-mappings/externalcourse/{externalCourseId} | Find course mappings by externalCourseId |
| [**courseMappingsGet**](CourseMappingsApi.md#courseMappingsGet) | **GET** /course-mappings | Find course mappings |
| [**courseMappingsOfferingIdExternalCourseIdDelete**](CourseMappingsApi.md#courseMappingsOfferingIdExternalCourseIdDelete) | **DELETE** /course-mappings/{offeringId}/{externalCourseId} | Remove course mapping |
| [**courseMappingsOfferingIdExternalCourseIdPut**](CourseMappingsApi.md#courseMappingsOfferingIdExternalCourseIdPut) | **PUT** /course-mappings/{offeringId}/{externalCourseId} | Add course mapping |
| [**courseMappingsOfferingIdGet**](CourseMappingsApi.md#courseMappingsOfferingIdGet) | **GET** /course-mappings/{offeringId} | Find course mappings by offeringId |


<a id="courseMappingsExternalcourseExternalCourseIdGet"></a>
# **courseMappingsExternalcourseExternalCourseIdGet**
> List&lt;String&gt; courseMappingsExternalcourseExternalCourseIdGet(externalCourseId)

Find course mappings by externalCourseId

Responds with course mapping details by externalCourseId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CourseMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    CourseMappingsApi apiInstance = new CourseMappingsApi(defaultClient);
    String externalCourseId = "externalCourseId_example"; // String | external course's id
    try {
      List<String> result = apiInstance.courseMappingsExternalcourseExternalCourseIdGet(externalCourseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CourseMappingsApi#courseMappingsExternalcourseExternalCourseIdGet");
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
| **externalCourseId** | **String**| external course&#39;s id | |

### Return type

**List&lt;String&gt;**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Course Mapping |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="courseMappingsGet"></a>
# **courseMappingsGet**
> Map&lt;String, String&gt; courseMappingsGet()

Find course mappings

Returns all course mappings for course offerings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CourseMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    CourseMappingsApi apiInstance = new CourseMappingsApi(defaultClient);
    try {
      Map<String, String> result = apiInstance.courseMappingsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CourseMappingsApi#courseMappingsGet");
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

**Map&lt;String, String&gt;**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Course Mappings |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |

<a id="courseMappingsOfferingIdExternalCourseIdDelete"></a>
# **courseMappingsOfferingIdExternalCourseIdDelete**
> List&lt;String&gt; courseMappingsOfferingIdExternalCourseIdDelete(offeringId, externalCourseId)

Remove course mapping

Removes the course mapping between the offering and the externalCourseId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CourseMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    CourseMappingsApi apiInstance = new CourseMappingsApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String externalCourseId = "externalCourseId_example"; // String | external course's id
    try {
      List<String> result = apiInstance.courseMappingsOfferingIdExternalCourseIdDelete(offeringId, externalCourseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CourseMappingsApi#courseMappingsOfferingIdExternalCourseIdDelete");
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
| **offeringId** | **String**| offering&#39;s id | |
| **externalCourseId** | **String**| external course&#39;s id | |

### Return type

**List&lt;String&gt;**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Course Mapping |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="courseMappingsOfferingIdExternalCourseIdPut"></a>
# **courseMappingsOfferingIdExternalCourseIdPut**
> List&lt;String&gt; courseMappingsOfferingIdExternalCourseIdPut(offeringId, externalCourseId)

Add course mapping

Creates a mapping between the offering and the externalCourseId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CourseMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    CourseMappingsApi apiInstance = new CourseMappingsApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String externalCourseId = "externalCourseId_example"; // String | external course's id
    try {
      List<String> result = apiInstance.courseMappingsOfferingIdExternalCourseIdPut(offeringId, externalCourseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CourseMappingsApi#courseMappingsOfferingIdExternalCourseIdPut");
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
| **offeringId** | **String**| offering&#39;s id | |
| **externalCourseId** | **String**| external course&#39;s id | |

### Return type

**List&lt;String&gt;**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Course Mapping |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="courseMappingsOfferingIdGet"></a>
# **courseMappingsOfferingIdGet**
> List&lt;String&gt; courseMappingsOfferingIdGet(offeringId)

Find course mappings by offeringId

Responds with course mapping details by offeringId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CourseMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    CourseMappingsApi apiInstance = new CourseMappingsApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    try {
      List<String> result = apiInstance.courseMappingsOfferingIdGet(offeringId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CourseMappingsApi#courseMappingsOfferingIdGet");
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
| **offeringId** | **String**| offering&#39;s id | |

### Return type

**List&lt;String&gt;**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Course Mapping |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

