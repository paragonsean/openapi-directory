# UserApi

All URIs are relative to *https://api.flat.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gerUserLikes**](UserApi.md#gerUserLikes) | **GET** /users/{user}/likes | List liked scores |
| [**getUser**](UserApi.md#getUser) | **GET** /users/{user} | Get a public user profile |
| [**getUserScores**](UserApi.md#getUserScores) | **GET** /users/{user}/scores | List user&#39;s scores |


<a id="gerUserLikes"></a>
# **gerUserLikes**
> List&lt;ScoreDetails&gt; gerUserLikes(user, ids)

List liked scores

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UserApi apiInstance = new UserApi(defaultClient);
    String user = "user_example"; // String | Unique identifier of a Flat user. If you authenticated, you can use `me` to refer to the current user. 
    Boolean ids = true; // Boolean | Return only the identifiers of the scores
    try {
      List<ScoreDetails> result = apiInstance.gerUserLikes(user, ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#gerUserLikes");
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
| **user** | **String**| Unique identifier of a Flat user. If you authenticated, you can use &#x60;me&#x60; to refer to the current user.  | |
| **ids** | **Boolean**| Return only the identifiers of the scores | [optional] |

### Return type

[**List&lt;ScoreDetails&gt;**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of liked scores |  -  |
| **0** | Error |  -  |

<a id="getUser"></a>
# **getUser**
> UserPublic getUser(user)

Get a public user profile

Get a public profile of a Flat User. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UserApi apiInstance = new UserApi(defaultClient);
    String user = "user_example"; // String | This route parameter is the unique identifier of the user. You can specify an email instead of an unique identifier. If you are executing this request authenticated, you can use `me` as a value instead of the current User unique identifier to work on the current authenticated user. 
    try {
      UserPublic result = apiInstance.getUser(user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#getUser");
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
| **user** | **String**| This route parameter is the unique identifier of the user. You can specify an email instead of an unique identifier. If you are executing this request authenticated, you can use &#x60;me&#x60; as a value instead of the current User unique identifier to work on the current authenticated user.  | |

### Return type

[**UserPublic**](UserPublic.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The user public details |  -  |
| **0** | Error |  -  |

<a id="getUserScores"></a>
# **getUserScores**
> List&lt;ScoreDetails&gt; getUserScores(user, parent)

List user&#39;s scores

Get the list of public scores owned by a User.  **DEPRECATED**: Please note that the current behavior will be deprecrated on **2019-01-01**. This method will no longer list private and shared scores, but only public scores of a Flat account. If you want to access to private scores, please use the [Collections API](#tag/Collection) instead. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    UserApi apiInstance = new UserApi(defaultClient);
    String user = "user_example"; // String | Unique identifier of a Flat user. If you authenticated, you can use `me` to refer to the current user. 
    String parent = "parent_example"; // String | Filter the score forked from the score id `parent`
    try {
      List<ScoreDetails> result = apiInstance.getUserScores(user, parent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#getUserScores");
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
| **user** | **String**| Unique identifier of a Flat user. If you authenticated, you can use &#x60;me&#x60; to refer to the current user.  | |
| **parent** | **String**| Filter the score forked from the score id &#x60;parent&#x60; | [optional] |

### Return type

[**List&lt;ScoreDetails&gt;**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The user scores |  -  |
| **0** | Error |  -  |

