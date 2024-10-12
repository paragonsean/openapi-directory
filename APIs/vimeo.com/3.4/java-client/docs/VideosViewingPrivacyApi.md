# VideosViewingPrivacyApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVideoPrivacyUser**](VideosViewingPrivacyApi.md#addVideoPrivacyUser) | **PUT** /videos/{video_id}/privacy/users/{user_id} | Permit a specific user to view a private video |
| [**addVideoPrivacyUsers**](VideosViewingPrivacyApi.md#addVideoPrivacyUsers) | **PUT** /videos/{video_id}/privacy/users | Permit a list of users to view a private video |
| [**addVideoPrivacyUsersAlt1**](VideosViewingPrivacyApi.md#addVideoPrivacyUsersAlt1) | **PUT** /channels/{channel_id}/videos/{video_id}/privacy/users | Permit a list of users to view a private video |
| [**deleteVideoPrivacyUser**](VideosViewingPrivacyApi.md#deleteVideoPrivacyUser) | **DELETE** /videos/{video_id}/privacy/users/{user_id} | Restrict a user from viewing a private video |
| [**getVideoPrivacyUsers**](VideosViewingPrivacyApi.md#getVideoPrivacyUsers) | **GET** /videos/{video_id}/privacy/users | Get all the users who can view a user&#39;s private videos by default |
| [**getVideoPrivacyUsersAlt1**](VideosViewingPrivacyApi.md#getVideoPrivacyUsersAlt1) | **GET** /channels/{channel_id}/videos/{video_id}/privacy/users | Get all the users who can view a user&#39;s private videos by default |


<a id="addVideoPrivacyUser"></a>
# **addVideoPrivacyUser**
> User addVideoPrivacyUser(userId, videoId)

Permit a specific user to view a private video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosViewingPrivacyApi;

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

    VideosViewingPrivacyApi apiInstance = new VideosViewingPrivacyApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      User result = apiInstance.addVideoPrivacyUser(userId, videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosViewingPrivacyApi#addVideoPrivacyUser");
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
| **userId** | **BigDecimal**| The ID of the user. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.user+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The user can now view the private video. |  -  |
| **204** | The user can already view this private video. |  -  |
| **403** | The video doesn&#39;t have a user-defined access list. |  -  |

<a id="addVideoPrivacyUsers"></a>
# **addVideoPrivacyUsers**
> List&lt;User&gt; addVideoPrivacyUsers(videoId)

Permit a list of users to view a private video

The body of this request should follow our [batch request format](https://developer.vimeo.com/api/common-formats#batch-requests). Each object must contain a single &#x60;URI&#x60; field, and the value of this field must be the URI of the user who can view this video.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosViewingPrivacyApi;

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

    VideosViewingPrivacyApi apiInstance = new VideosViewingPrivacyApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      List<User> result = apiInstance.addVideoPrivacyUsers(videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosViewingPrivacyApi#addVideoPrivacyUsers");
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
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.user+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The users can now view the private video. |  -  |

<a id="addVideoPrivacyUsersAlt1"></a>
# **addVideoPrivacyUsersAlt1**
> List&lt;User&gt; addVideoPrivacyUsersAlt1(channelId, videoId)

Permit a list of users to view a private video

The body of this request should follow our [batch request format](https://developer.vimeo.com/api/common-formats#batch-requests). Each object must contain a single &#x60;URI&#x60; field, and the value of this field must be the URI of the user who can view this video.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosViewingPrivacyApi;

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

    VideosViewingPrivacyApi apiInstance = new VideosViewingPrivacyApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      List<User> result = apiInstance.addVideoPrivacyUsersAlt1(channelId, videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosViewingPrivacyApi#addVideoPrivacyUsersAlt1");
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
| **channelId** | **BigDecimal**| The ID of the channel. | |
| **videoId** | **BigDecimal**| The ID of the video. | |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.user+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The users can now view the private video. |  -  |

<a id="deleteVideoPrivacyUser"></a>
# **deleteVideoPrivacyUser**
> deleteVideoPrivacyUser(userId, videoId)

Restrict a user from viewing a private video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosViewingPrivacyApi;

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

    VideosViewingPrivacyApi apiInstance = new VideosViewingPrivacyApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.deleteVideoPrivacyUser(userId, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosViewingPrivacyApi#deleteVideoPrivacyUser");
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
| **204** | The user was disallowed from viewing the private video. |  -  |
| **403** | The video isn&#39;t set to a user-defined access list. |  -  |
| **404** | No such user exists. |  -  |

<a id="getVideoPrivacyUsers"></a>
# **getVideoPrivacyUsers**
> List&lt;User&gt; getVideoPrivacyUsers(videoId, page, perPage)

Get all the users who can view a user&#39;s private videos by default

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosViewingPrivacyApi;

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

    VideosViewingPrivacyApi apiInstance = new VideosViewingPrivacyApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    try {
      List<User> result = apiInstance.getVideoPrivacyUsers(videoId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosViewingPrivacyApi#getVideoPrivacyUsers");
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
| **videoId** | **BigDecimal**| The ID of the video. | |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.user+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The users were returned. |  -  |
| **400** | No users can view the private video. |  -  |

<a id="getVideoPrivacyUsersAlt1"></a>
# **getVideoPrivacyUsersAlt1**
> List&lt;User&gt; getVideoPrivacyUsersAlt1(channelId, videoId, page, perPage)

Get all the users who can view a user&#39;s private videos by default

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosViewingPrivacyApi;

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

    VideosViewingPrivacyApi apiInstance = new VideosViewingPrivacyApi(defaultClient);
    BigDecimal channelId = new BigDecimal("927"); // BigDecimal | The ID of the channel.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    try {
      List<User> result = apiInstance.getVideoPrivacyUsersAlt1(channelId, videoId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosViewingPrivacyApi#getVideoPrivacyUsersAlt1");
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
| **channelId** | **BigDecimal**| The ID of the channel. | |
| **videoId** | **BigDecimal**| The ID of the video. | |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.user+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The users were returned. |  -  |
| **400** | No users can view the private video. |  -  |

