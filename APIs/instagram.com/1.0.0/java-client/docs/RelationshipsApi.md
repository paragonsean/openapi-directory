# RelationshipsApi

All URIs are relative to *https://api.instagram.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersSelfRequestedByGet**](RelationshipsApi.md#usersSelfRequestedByGet) | **GET** /users/self/requested-by | List the users who have requested this user&#39;s permission to follow. |
| [**usersUserIdFollowedByGet**](RelationshipsApi.md#usersUserIdFollowedByGet) | **GET** /users/{user-id}/followed-by | Get the list of users this user is followed by. |
| [**usersUserIdFollowsGet**](RelationshipsApi.md#usersUserIdFollowsGet) | **GET** /users/{user-id}/follows | Get the list of users this user follows. |
| [**usersUserIdRelationshipGet**](RelationshipsApi.md#usersUserIdRelationshipGet) | **GET** /users/{user-id}/relationship | Get information about a relationship to another user. |
| [**usersUserIdRelationshipPost**](RelationshipsApi.md#usersUserIdRelationshipPost) | **POST** /users/{user-id}/relationship | Modify the relationship between the current user and the target user. |


<a id="usersSelfRequestedByGet"></a>
# **usersSelfRequestedByGet**
> UsersInfoResponse usersSelfRequestedByGet()

List the users who have requested this user&#39;s permission to follow.

List the users who have requested this user&#39;s permission to follow.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelationshipsApi;

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

    RelationshipsApi apiInstance = new RelationshipsApi(defaultClient);
    try {
      UsersInfoResponse result = apiInstance.usersSelfRequestedByGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelationshipsApi#usersSelfRequestedByGet");
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

[**UsersInfoResponse**](UsersInfoResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of users who have requested this user&#39;s permission to follow. |  -  |

<a id="usersUserIdFollowedByGet"></a>
# **usersUserIdFollowedByGet**
> UsersPagingResponse usersUserIdFollowedByGet(userId)

Get the list of users this user is followed by.

Get the list of users this user is followed by. To get users followed by the owner of the access token, you can use **self** instead of the &#x60;user-id&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelationshipsApi;

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

    RelationshipsApi apiInstance = new RelationshipsApi(defaultClient);
    String userId = "userId_example"; // String | The ID of a user, or **self** to retrieve information about authenticated user.
    try {
      UsersPagingResponse result = apiInstance.usersUserIdFollowedByGet(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelationshipsApi#usersUserIdFollowedByGet");
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
| **userId** | **String**| The ID of a user, or **self** to retrieve information about authenticated user. | |

### Return type

[**UsersPagingResponse**](UsersPagingResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of users this user is followed by. |  -  |

<a id="usersUserIdFollowsGet"></a>
# **usersUserIdFollowsGet**
> UsersPagingResponse usersUserIdFollowsGet(userId)

Get the list of users this user follows.

Get the list of users this user follows. To get follows of the owner of the access token, you can use **self** instead of the &#x60;user-id&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelationshipsApi;

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

    RelationshipsApi apiInstance = new RelationshipsApi(defaultClient);
    String userId = "userId_example"; // String | The ID of a user, or **self** to retrieve information about authenticated user.
    try {
      UsersPagingResponse result = apiInstance.usersUserIdFollowsGet(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelationshipsApi#usersUserIdFollowsGet");
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
| **userId** | **String**| The ID of a user, or **self** to retrieve information about authenticated user. | |

### Return type

[**UsersPagingResponse**](UsersPagingResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of users this user follows. |  -  |

<a id="usersUserIdRelationshipGet"></a>
# **usersUserIdRelationshipGet**
> RelationshipResponse usersUserIdRelationshipGet(userId)

Get information about a relationship to another user.

Get information about a relationship to another user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelationshipsApi;

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

    RelationshipsApi apiInstance = new RelationshipsApi(defaultClient);
    String userId = "userId_example"; // String | The ID of a user to get information about.
    try {
      RelationshipResponse result = apiInstance.usersUserIdRelationshipGet(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelationshipsApi#usersUserIdRelationshipGet");
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
| **userId** | **String**| The ID of a user to get information about. | |

### Return type

[**RelationshipResponse**](RelationshipResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Relationship information. |  -  |

<a id="usersUserIdRelationshipPost"></a>
# **usersUserIdRelationshipPost**
> RelationshipPostResponse usersUserIdRelationshipPost(userId, action)

Modify the relationship between the current user and the target user.

Modify the relationship between the current user and the target user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelationshipsApi;

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

    RelationshipsApi apiInstance = new RelationshipsApi(defaultClient);
    String userId = "userId_example"; // String | The ID of the target user.
    String action = "follow"; // String | Type of action to apply for relationship with the user.
    try {
      RelationshipPostResponse result = apiInstance.usersUserIdRelationshipPost(userId, action);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelationshipsApi#usersUserIdRelationshipPost");
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
| **userId** | **String**| The ID of the target user. | |
| **action** | **String**| Type of action to apply for relationship with the user. | [enum: follow, unfollow, block, unblock, approve, ignore] |

### Return type

[**RelationshipPostResponse**](RelationshipPostResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Relationship information. |  -  |

