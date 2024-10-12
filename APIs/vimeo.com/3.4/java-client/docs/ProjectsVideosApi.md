# ProjectsVideosApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVideoToProject**](ProjectsVideosApi.md#addVideoToProject) | **PUT** /users/{user_id}/projects/{project_id}/videos/{video_id} | Add a specific video to a project |
| [**addVideoToProjectAlt1**](ProjectsVideosApi.md#addVideoToProjectAlt1) | **PUT** /me/projects/{project_id}/videos/{video_id} | Add a specific video to a project |
| [**addVideosToProject**](ProjectsVideosApi.md#addVideosToProject) | **PUT** /users/{user_id}/projects/{project_id}/videos | Add a list of videos to a project |
| [**addVideosToProjectAlt1**](ProjectsVideosApi.md#addVideosToProjectAlt1) | **PUT** /me/projects/{project_id}/videos | Add a list of videos to a project |
| [**getProjectVideos**](ProjectsVideosApi.md#getProjectVideos) | **GET** /users/{user_id}/projects/{project_id}/videos | Get all the videos in a project |
| [**getProjectVideosAlt1**](ProjectsVideosApi.md#getProjectVideosAlt1) | **GET** /me/projects/{project_id}/videos | Get all the videos in a project |
| [**removeVideoFromProject**](ProjectsVideosApi.md#removeVideoFromProject) | **DELETE** /users/{user_id}/projects/{project_id}/videos/{video_id} | Remove a specific video from a project |
| [**removeVideoFromProjectAlt1**](ProjectsVideosApi.md#removeVideoFromProjectAlt1) | **DELETE** /me/projects/{project_id}/videos/{video_id} | Remove a specific video from a project |
| [**removeVideosFromProject**](ProjectsVideosApi.md#removeVideosFromProject) | **DELETE** /users/{user_id}/projects/{project_id}/videos | Remove a list of videos from a project |
| [**removeVideosFromProjectAlt1**](ProjectsVideosApi.md#removeVideosFromProjectAlt1) | **DELETE** /me/projects/{project_id}/videos | Remove a list of videos from a project |


<a id="addVideoToProject"></a>
# **addVideoToProject**
> addVideoToProject(projectId, userId, videoId)

Add a specific video to a project

This method adds a single video to the specified project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsVideosApi apiInstance = new ProjectsVideosApi(defaultClient);
    BigDecimal projectId = new BigDecimal("12345"); // BigDecimal | The ID of the project.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.addVideoToProject(projectId, userId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsVideosApi#addVideoToProject");
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
| **projectId** | **BigDecimal**| The ID of the project. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The video was added. |  -  |
| **404** | Error code 5000: No such user, project, or video exists. |  -  |

<a id="addVideoToProjectAlt1"></a>
# **addVideoToProjectAlt1**
> addVideoToProjectAlt1(projectId, videoId)

Add a specific video to a project

This method adds a single video to the specified project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsVideosApi apiInstance = new ProjectsVideosApi(defaultClient);
    BigDecimal projectId = new BigDecimal("12345"); // BigDecimal | The ID of the project.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.addVideoToProjectAlt1(projectId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsVideosApi#addVideoToProjectAlt1");
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
| **projectId** | **BigDecimal**| The ID of the project. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The video was added. |  -  |
| **404** | Error code 5000: No such user, project, or video exists. |  -  |

<a id="addVideosToProject"></a>
# **addVideosToProject**
> addVideosToProject(projectId, userId, uris)

Add a list of videos to a project

This method adds multiple videos to the specified project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsVideosApi apiInstance = new ProjectsVideosApi(defaultClient);
    BigDecimal projectId = new BigDecimal("12345"); // BigDecimal | The ID of the project.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    String uris = "/videos/258684937,/videos/273576296"; // String | A comma-separated list of video URIs to add.
    try {
      apiInstance.addVideosToProject(projectId, userId, uris);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsVideosApi#addVideosToProject");
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
| **projectId** | **BigDecimal**| The ID of the project. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **uris** | **String**| A comma-separated list of video URIs to add. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The videos were added. |  -  |
| **400** | Error code 2204: The input is invalid. |  -  |
| **401** | Error code 8000: The user credentials are invalid. |  -  |
| **404** | Error code 5000: No such project or video exists. |  -  |

<a id="addVideosToProjectAlt1"></a>
# **addVideosToProjectAlt1**
> addVideosToProjectAlt1(projectId, uris)

Add a list of videos to a project

This method adds multiple videos to the specified project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsVideosApi apiInstance = new ProjectsVideosApi(defaultClient);
    BigDecimal projectId = new BigDecimal("12345"); // BigDecimal | The ID of the project.
    String uris = "/videos/258684937,/videos/273576296"; // String | A comma-separated list of video URIs to add.
    try {
      apiInstance.addVideosToProjectAlt1(projectId, uris);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsVideosApi#addVideosToProjectAlt1");
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
| **projectId** | **BigDecimal**| The ID of the project. | |
| **uris** | **String**| A comma-separated list of video URIs to add. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The videos were added. |  -  |
| **400** | Error code 2204: The input is invalid. |  -  |
| **401** | Error code 8000: The user credentials are invalid. |  -  |
| **404** | Error code 5000: No such project or video exists. |  -  |

<a id="getProjectVideos"></a>
# **getProjectVideos**
> List&lt;Video&gt; getProjectVideos(projectId, userId, direction, page, perPage, sort)

Get all the videos in a project

This method gets all the videos that belong to the specified project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsVideosApi apiInstance = new ProjectsVideosApi(defaultClient);
    BigDecimal projectId = new BigDecimal("12345"); // BigDecimal | The ID of the project.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    String direction = "asc"; // String | The sort direction of the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String sort = "alphabetical"; // String | The way to sort the results.
    try {
      List<Video> result = apiInstance.getProjectVideos(projectId, userId, direction, page, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsVideosApi#getProjectVideos");
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
| **projectId** | **BigDecimal**| The ID of the project. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: alphabetical, date, default, duration, last_user_action_event_date] |

### Return type

[**List&lt;Video&gt;**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The videos were returned. |  -  |
| **401** | Error code 8000: The user credentials are invalid. |  -  |
| **404** | Error code 5000: No such project exists. |  -  |

<a id="getProjectVideosAlt1"></a>
# **getProjectVideosAlt1**
> List&lt;Video&gt; getProjectVideosAlt1(projectId, direction, page, perPage, sort)

Get all the videos in a project

This method gets all the videos that belong to the specified project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsVideosApi apiInstance = new ProjectsVideosApi(defaultClient);
    BigDecimal projectId = new BigDecimal("12345"); // BigDecimal | The ID of the project.
    String direction = "asc"; // String | The sort direction of the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String sort = "alphabetical"; // String | The way to sort the results.
    try {
      List<Video> result = apiInstance.getProjectVideosAlt1(projectId, direction, page, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsVideosApi#getProjectVideosAlt1");
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
| **projectId** | **BigDecimal**| The ID of the project. | |
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: alphabetical, date, default, duration, last_user_action_event_date] |

### Return type

[**List&lt;Video&gt;**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The videos were returned. |  -  |
| **401** | Error code 8000: The user credentials are invalid. |  -  |
| **404** | Error code 5000: No such project exists. |  -  |

<a id="removeVideoFromProject"></a>
# **removeVideoFromProject**
> removeVideoFromProject(projectId, userId, videoId)

Remove a specific video from a project

This method removes a single video from the specified project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsVideosApi apiInstance = new ProjectsVideosApi(defaultClient);
    BigDecimal projectId = new BigDecimal("12345"); // BigDecimal | The ID of the project.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.removeVideoFromProject(projectId, userId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsVideosApi#removeVideoFromProject");
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
| **projectId** | **BigDecimal**| The ID of the project. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The video was removed. |  -  |
| **400** | Error code 2204: The input is invalid. |  -  |
| **401** | Error code 8000: The user credentials are invalid. |  -  |
| **404** | Error code 5000: No such video exists in the project. |  -  |

<a id="removeVideoFromProjectAlt1"></a>
# **removeVideoFromProjectAlt1**
> removeVideoFromProjectAlt1(projectId, videoId)

Remove a specific video from a project

This method removes a single video from the specified project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsVideosApi apiInstance = new ProjectsVideosApi(defaultClient);
    BigDecimal projectId = new BigDecimal("12345"); // BigDecimal | The ID of the project.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.removeVideoFromProjectAlt1(projectId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsVideosApi#removeVideoFromProjectAlt1");
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
| **projectId** | **BigDecimal**| The ID of the project. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The video was removed. |  -  |
| **400** | Error code 2204: The input is invalid. |  -  |
| **401** | Error code 8000: The user credentials are invalid. |  -  |
| **404** | Error code 5000: No such video exists in the project. |  -  |

<a id="removeVideosFromProject"></a>
# **removeVideosFromProject**
> removeVideosFromProject(projectId, userId, uris, shouldDeleteClips)

Remove a list of videos from a project

This method removed multiple videos from the specified project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsVideosApi apiInstance = new ProjectsVideosApi(defaultClient);
    BigDecimal projectId = new BigDecimal("12345"); // BigDecimal | The ID of the project.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    String uris = "/videos/258684937,/videos/273576296"; // String | A comma-separated list of the video URIs to remove.
    Boolean shouldDeleteClips = false; // Boolean | Whether to delete the videos when removing them from the project.
    try {
      apiInstance.removeVideosFromProject(projectId, userId, uris, shouldDeleteClips);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsVideosApi#removeVideosFromProject");
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
| **projectId** | **BigDecimal**| The ID of the project. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **uris** | **String**| A comma-separated list of the video URIs to remove. | |
| **shouldDeleteClips** | **Boolean**| Whether to delete the videos when removing them from the project. | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The videos were removed. |  -  |
| **400** | Error code 2204: The input is invalid. |  -  |
| **401** | Error code 8000: The user credentials are invalid. |  -  |
| **404** | Error code 5000: No such project exists. |  -  |

<a id="removeVideosFromProjectAlt1"></a>
# **removeVideosFromProjectAlt1**
> removeVideosFromProjectAlt1(projectId, uris, shouldDeleteClips)

Remove a list of videos from a project

This method removed multiple videos from the specified project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsVideosApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsVideosApi apiInstance = new ProjectsVideosApi(defaultClient);
    BigDecimal projectId = new BigDecimal("12345"); // BigDecimal | The ID of the project.
    String uris = "/videos/258684937,/videos/273576296"; // String | A comma-separated list of the video URIs to remove.
    Boolean shouldDeleteClips = false; // Boolean | Whether to delete the videos when removing them from the project.
    try {
      apiInstance.removeVideosFromProjectAlt1(projectId, uris, shouldDeleteClips);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsVideosApi#removeVideosFromProjectAlt1");
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
| **projectId** | **BigDecimal**| The ID of the project. | |
| **uris** | **String**| A comma-separated list of the video URIs to remove. | |
| **shouldDeleteClips** | **Boolean**| Whether to delete the videos when removing them from the project. | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The videos were removed. |  -  |
| **400** | Error code 2204: The input is invalid. |  -  |
| **401** | Error code 8000: The user credentials are invalid. |  -  |
| **404** | Error code 5000: No such project exists. |  -  |

