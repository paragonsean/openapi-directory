# CoursesApi

All URIs are relative to *https://api.iqualify.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**coursesContentIdActivationsGet**](CoursesApi.md#coursesContentIdActivationsGet) | **GET** /courses/{contentId}/activations | Find activations for a contentId |
| [**coursesContentIdGet**](CoursesApi.md#coursesContentIdGet) | **GET** /courses/{contentId} | Find course by contentId |
| [**coursesContentIdPermissionsGet**](CoursesApi.md#coursesContentIdPermissionsGet) | **GET** /courses/{contentId}/permissions | Find users who have access to the contentId provided |
| [**coursesGet**](CoursesApi.md#coursesGet) | **GET** /courses | Find courses |
| [**coursesRootContentIdPermissionsUserEmailPost**](CoursesApi.md#coursesRootContentIdPermissionsUserEmailPost) | **POST** /courses/{rootContentId}/permissions/{userEmail} | Update course access |


<a id="coursesContentIdActivationsGet"></a>
# **coursesContentIdActivationsGet**
> ActivationResponse coursesContentIdActivationsGet(contentId)

Find activations for a contentId

Responds with all activations for the contentId provided.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CoursesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    CoursesApi apiInstance = new CoursesApi(defaultClient);
    String contentId = "contentId_example"; // String | The content Id
    try {
      ActivationResponse result = apiInstance.coursesContentIdActivationsGet(contentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CoursesApi#coursesContentIdActivationsGet");
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

### Return type

[**ActivationResponse**](ActivationResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Activation list. |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="coursesContentIdGet"></a>
# **coursesContentIdGet**
> CourseMetaResponse coursesContentIdGet(contentId)

Find course by contentId

Responds with a course matching the contentId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CoursesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    CoursesApi apiInstance = new CoursesApi(defaultClient);
    String contentId = "contentId_example"; // String | The content Id
    try {
      CourseMetaResponse result = apiInstance.coursesContentIdGet(contentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CoursesApi#coursesContentIdGet");
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

### Return type

[**CourseMetaResponse**](CourseMetaResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Course detail |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="coursesContentIdPermissionsGet"></a>
# **coursesContentIdPermissionsGet**
> UserPermission coursesContentIdPermissionsGet(contentId)

Find users who have access to the contentId provided

Responds with users who have access to a specific course by contentId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CoursesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    CoursesApi apiInstance = new CoursesApi(defaultClient);
    String contentId = "contentId_example"; // String | The content Id
    try {
      UserPermission result = apiInstance.coursesContentIdPermissionsGet(contentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CoursesApi#coursesContentIdPermissionsGet");
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

### Return type

[**UserPermission**](UserPermission.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of users who have access to the content ID provided. |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="coursesGet"></a>
# **coursesGet**
> List&lt;CourseResponse&gt; coursesGet()

Find courses

Responds with all courses (draft and published.)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CoursesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    CoursesApi apiInstance = new CoursesApi(defaultClient);
    try {
      List<CourseResponse> result = apiInstance.coursesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CoursesApi#coursesGet");
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

[**List&lt;CourseResponse&gt;**](CourseResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All courses (draft and published) in the organisation. |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |

<a id="coursesRootContentIdPermissionsUserEmailPost"></a>
# **coursesRootContentIdPermissionsUserEmailPost**
> CoursesRootContentIdPermissionsUserEmailPost201Response coursesRootContentIdPermissionsUserEmailPost(rootContentId, userEmail, permissionToBeGrantedToTheUser)

Update course access

Provide a user with access to a specific course by rootContentId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CoursesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    CoursesApi apiInstance = new CoursesApi(defaultClient);
    String rootContentId = "rootContentId_example"; // String | The content Id
    String userEmail = "userEmail_example"; // String | The user email
    PermissionToBeGrantedToTheUser permissionToBeGrantedToTheUser = new PermissionToBeGrantedToTheUser(); // PermissionToBeGrantedToTheUser | 
    try {
      CoursesRootContentIdPermissionsUserEmailPost201Response result = apiInstance.coursesRootContentIdPermissionsUserEmailPost(rootContentId, userEmail, permissionToBeGrantedToTheUser);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CoursesApi#coursesRootContentIdPermissionsUserEmailPost");
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
| **rootContentId** | **String**| The content Id | |
| **userEmail** | **String**| The user email | |
| **permissionToBeGrantedToTheUser** | [**PermissionToBeGrantedToTheUser**](PermissionToBeGrantedToTheUser.md)|  | |

### Return type

[**CoursesRootContentIdPermissionsUserEmailPost201Response**](CoursesRootContentIdPermissionsUserEmailPost201Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | user successfully added to the course with the specified permission. |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

