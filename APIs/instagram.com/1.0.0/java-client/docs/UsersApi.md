# UsersApi

All URIs are relative to *https://api.instagram.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersSearchGet**](UsersApi.md#usersSearchGet) | **GET** /users/search | Search for a user by name. |
| [**usersSelfFeedGet**](UsersApi.md#usersSelfFeedGet) | **GET** /users/self/feed | See the authenticated user&#39;s feed. |
| [**usersSelfMediaLikedGet**](UsersApi.md#usersSelfMediaLikedGet) | **GET** /users/self/media/liked | See the list of media liked by the authenticated user. |
| [**usersUserIdGet**](UsersApi.md#usersUserIdGet) | **GET** /users/{user-id} | Get basic information about a user. |
| [**usersUserIdMediaRecentGet**](UsersApi.md#usersUserIdMediaRecentGet) | **GET** /users/{user-id}/media/recent | Get the most recent media published by a user. |


<a id="usersSearchGet"></a>
# **usersSearchGet**
> UsersInfoResponse usersSearchGet(q, count)

Search for a user by name.

Search for a user by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.instagram.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: instagram_auth
    OAuth instagram_auth = (OAuth) defaultClient.getAuthentication("instagram_auth");
    instagram_auth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String q = "q_example"; // String | A query string.
    Integer count = 56; // Integer | Number of users to return.
    try {
      UsersInfoResponse result = apiInstance.usersSearchGet(q, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersSearchGet");
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
| **q** | **String**| A query string. | |
| **count** | **Integer**| Number of users to return. | [optional] |

### Return type

[**UsersInfoResponse**](UsersInfoResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of found users. |  -  |

<a id="usersSelfFeedGet"></a>
# **usersSelfFeedGet**
> MediaListResponse usersSelfFeedGet(count, minId, maxId)

See the authenticated user&#39;s feed.

See the authenticated user&#39;s feed.  **Warning:** [Deprecated](http://instagram.com/developer/changelog/) for Apps created **on or after** Nov 17, 2015 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.instagram.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: instagram_auth
    OAuth instagram_auth = (OAuth) defaultClient.getAuthentication("instagram_auth");
    instagram_auth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer count = 56; // Integer | Count of media to return.
    String minId = "minId_example"; // String | Return media later than this `min_id`.
    String maxId = "maxId_example"; // String | Return media earlier than this `max_id`.
    try {
      MediaListResponse result = apiInstance.usersSelfFeedGet(count, minId, maxId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersSelfFeedGet");
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
| **count** | **Integer**| Count of media to return. | [optional] |
| **minId** | **String**| Return media later than this &#x60;min_id&#x60;. | [optional] |
| **maxId** | **String**| Return media earlier than this &#x60;max_id&#x60;. | [optional] |

### Return type

[**MediaListResponse**](MediaListResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Users feed entries. |  -  |

<a id="usersSelfMediaLikedGet"></a>
# **usersSelfMediaLikedGet**
> MediaListResponse usersSelfMediaLikedGet(count, maxLikeId)

See the list of media liked by the authenticated user.

See the list of media liked by the authenticated user. Private media is returned as long as the authenticated user has permission to view that media. Liked media lists are only available for the currently authenticated user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.instagram.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: instagram_auth
    OAuth instagram_auth = (OAuth) defaultClient.getAuthentication("instagram_auth");
    instagram_auth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer count = 56; // Integer | Count of media to return.
    String maxLikeId = "maxLikeId_example"; // String | Return media liked before this id.
    try {
      MediaListResponse result = apiInstance.usersSelfMediaLikedGet(count, maxLikeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersSelfMediaLikedGet");
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
| **count** | **Integer**| Count of media to return. | [optional] |
| **maxLikeId** | **String**| Return media liked before this id. | [optional] |

### Return type

[**MediaListResponse**](MediaListResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Users media entries. |  -  |

<a id="usersUserIdGet"></a>
# **usersUserIdGet**
> UserResponse usersUserIdGet(userId)

Get basic information about a user.

Get basic information about a user. To get information about the owner of the access token, you can use **self** instead of the &#x60;user-id&#x60;.  Security scope &#x60;public_content&#x60; is required to read information about other users. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.instagram.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: instagram_auth
    OAuth instagram_auth = (OAuth) defaultClient.getAuthentication("instagram_auth");
    instagram_auth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | The ID of a user to get information about, or **self** to retrieve information about authenticated user.
    try {
      UserResponse result = apiInstance.usersUserIdGet(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUserIdGet");
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
| **userId** | **String**| The ID of a user to get information about, or **self** to retrieve information about authenticated user. | |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User basic information. |  -  |
| **404** | Not Found, user with such ID does not exist. |  -  |

<a id="usersUserIdMediaRecentGet"></a>
# **usersUserIdMediaRecentGet**
> MediaListResponse usersUserIdMediaRecentGet(userId, count, maxTimestamp, minTimestamp, minId, maxId)

Get the most recent media published by a user.

Get the most recent media published by a user. To get the most recent media published by the owner of the access token, you can use **self** instead of the &#x60;user-id&#x60;.  Security scope &#x60;public_content&#x60; is required to read information about other users. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.instagram.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: instagram_auth
    OAuth instagram_auth = (OAuth) defaultClient.getAuthentication("instagram_auth");
    instagram_auth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | The ID of a user to get recent media of, or **self** to retrieve media of authenticated user.
    Integer count = 56; // Integer | Count of media to return.
    Long maxTimestamp = 56L; // Long | Return media before this UNIX timestamp.
    Long minTimestamp = 56L; // Long | Return media after this UNIX timestamp.
    String minId = "minId_example"; // String | Return media later than this `min_id`.
    String maxId = "maxId_example"; // String | Return media earlier than this `max_id`.
    try {
      MediaListResponse result = apiInstance.usersUserIdMediaRecentGet(userId, count, maxTimestamp, minTimestamp, minId, maxId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUserIdMediaRecentGet");
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
| **userId** | **String**| The ID of a user to get recent media of, or **self** to retrieve media of authenticated user. | |
| **count** | **Integer**| Count of media to return. | [optional] |
| **maxTimestamp** | **Long**| Return media before this UNIX timestamp. | [optional] |
| **minTimestamp** | **Long**| Return media after this UNIX timestamp. | [optional] |
| **minId** | **String**| Return media later than this &#x60;min_id&#x60;. | [optional] |
| **maxId** | **String**| Return media earlier than this &#x60;max_id&#x60;. | [optional] |

### Return type

[**MediaListResponse**](MediaListResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Users media entries. |  -  |

