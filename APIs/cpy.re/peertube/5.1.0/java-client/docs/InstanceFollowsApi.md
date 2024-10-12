# InstanceFollowsApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1ServerFollowersGet**](InstanceFollowsApi.md#apiV1ServerFollowersGet) | **GET** /api/v1/server/followers | List instances following the server |
| [**apiV1ServerFollowersNameWithHostAcceptPost**](InstanceFollowsApi.md#apiV1ServerFollowersNameWithHostAcceptPost) | **POST** /api/v1/server/followers/{nameWithHost}/accept | Accept a pending follower to your server |
| [**apiV1ServerFollowersNameWithHostDelete**](InstanceFollowsApi.md#apiV1ServerFollowersNameWithHostDelete) | **DELETE** /api/v1/server/followers/{nameWithHost} | Remove or reject a follower to your server |
| [**apiV1ServerFollowersNameWithHostRejectPost**](InstanceFollowsApi.md#apiV1ServerFollowersNameWithHostRejectPost) | **POST** /api/v1/server/followers/{nameWithHost}/reject | Reject a pending follower to your server |
| [**apiV1ServerFollowingGet**](InstanceFollowsApi.md#apiV1ServerFollowingGet) | **GET** /api/v1/server/following | List instances followed by the server |
| [**apiV1ServerFollowingHostOrHandleDelete**](InstanceFollowsApi.md#apiV1ServerFollowingHostOrHandleDelete) | **DELETE** /api/v1/server/following/{hostOrHandle} | Unfollow an actor (PeerTube instance, channel or account) |
| [**apiV1ServerFollowingPost**](InstanceFollowsApi.md#apiV1ServerFollowingPost) | **POST** /api/v1/server/following | Follow a list of actors (PeerTube instance, channel or account) |


<a id="apiV1ServerFollowersGet"></a>
# **apiV1ServerFollowersGet**
> GetAccountFollowers200Response apiV1ServerFollowersGet(state, actorType, start, count, sort)

List instances following the server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceFollowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    InstanceFollowsApi apiInstance = new InstanceFollowsApi(defaultClient);
    String state = "pending"; // String | 
    String actorType = "Person"; // String | 
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    try {
      GetAccountFollowers200Response result = apiInstance.apiV1ServerFollowersGet(state, actorType, start, count, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceFollowsApi#apiV1ServerFollowersGet");
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
| **state** | **String**|  | [optional] [enum: pending, accepted] |
| **actorType** | **String**|  | [optional] [enum: Person, Application, Group, Service, Organization] |
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**| Sort column | [optional] |

### Return type

[**GetAccountFollowers200Response**](GetAccountFollowers200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1ServerFollowersNameWithHostAcceptPost"></a>
# **apiV1ServerFollowersNameWithHostAcceptPost**
> apiV1ServerFollowersNameWithHostAcceptPost(nameWithHost)

Accept a pending follower to your server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceFollowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstanceFollowsApi apiInstance = new InstanceFollowsApi(defaultClient);
    String nameWithHost = "nameWithHost_example"; // String | The remote actor handle to remove from your followers
    try {
      apiInstance.apiV1ServerFollowersNameWithHostAcceptPost(nameWithHost);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceFollowsApi#apiV1ServerFollowersNameWithHostAcceptPost");
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
| **nameWithHost** | **String**| The remote actor handle to remove from your followers | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **404** | follower not found |  -  |

<a id="apiV1ServerFollowersNameWithHostDelete"></a>
# **apiV1ServerFollowersNameWithHostDelete**
> apiV1ServerFollowersNameWithHostDelete(nameWithHost)

Remove or reject a follower to your server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceFollowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstanceFollowsApi apiInstance = new InstanceFollowsApi(defaultClient);
    String nameWithHost = "nameWithHost_example"; // String | The remote actor handle to remove from your followers
    try {
      apiInstance.apiV1ServerFollowersNameWithHostDelete(nameWithHost);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceFollowsApi#apiV1ServerFollowersNameWithHostDelete");
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
| **nameWithHost** | **String**| The remote actor handle to remove from your followers | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **404** | follower not found |  -  |

<a id="apiV1ServerFollowersNameWithHostRejectPost"></a>
# **apiV1ServerFollowersNameWithHostRejectPost**
> apiV1ServerFollowersNameWithHostRejectPost(nameWithHost)

Reject a pending follower to your server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceFollowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstanceFollowsApi apiInstance = new InstanceFollowsApi(defaultClient);
    String nameWithHost = "nameWithHost_example"; // String | The remote actor handle to remove from your followers
    try {
      apiInstance.apiV1ServerFollowersNameWithHostRejectPost(nameWithHost);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceFollowsApi#apiV1ServerFollowersNameWithHostRejectPost");
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
| **nameWithHost** | **String**| The remote actor handle to remove from your followers | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **404** | follower not found |  -  |

<a id="apiV1ServerFollowingGet"></a>
# **apiV1ServerFollowingGet**
> GetAccountFollowers200Response apiV1ServerFollowingGet(state, actorType, start, count, sort)

List instances followed by the server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceFollowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    InstanceFollowsApi apiInstance = new InstanceFollowsApi(defaultClient);
    String state = "pending"; // String | 
    String actorType = "Person"; // String | 
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    try {
      GetAccountFollowers200Response result = apiInstance.apiV1ServerFollowingGet(state, actorType, start, count, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceFollowsApi#apiV1ServerFollowingGet");
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
| **state** | **String**|  | [optional] [enum: pending, accepted] |
| **actorType** | **String**|  | [optional] [enum: Person, Application, Group, Service, Organization] |
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**| Sort column | [optional] |

### Return type

[**GetAccountFollowers200Response**](GetAccountFollowers200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1ServerFollowingHostOrHandleDelete"></a>
# **apiV1ServerFollowingHostOrHandleDelete**
> apiV1ServerFollowingHostOrHandleDelete(hostOrHandle)

Unfollow an actor (PeerTube instance, channel or account)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceFollowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstanceFollowsApi apiInstance = new InstanceFollowsApi(defaultClient);
    String hostOrHandle = "hostOrHandle_example"; // String | The hostOrHandle to unfollow
    try {
      apiInstance.apiV1ServerFollowingHostOrHandleDelete(hostOrHandle);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceFollowsApi#apiV1ServerFollowingHostOrHandleDelete");
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
| **hostOrHandle** | **String**| The hostOrHandle to unfollow | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **404** | host or handle not found |  -  |

<a id="apiV1ServerFollowingPost"></a>
# **apiV1ServerFollowingPost**
> apiV1ServerFollowingPost(apiV1ServerFollowingPostRequest)

Follow a list of actors (PeerTube instance, channel or account)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InstanceFollowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InstanceFollowsApi apiInstance = new InstanceFollowsApi(defaultClient);
    ApiV1ServerFollowingPostRequest apiV1ServerFollowingPostRequest = new ApiV1ServerFollowingPostRequest(); // ApiV1ServerFollowingPostRequest | 
    try {
      apiInstance.apiV1ServerFollowingPost(apiV1ServerFollowingPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling InstanceFollowsApi#apiV1ServerFollowingPost");
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
| **apiV1ServerFollowingPostRequest** | [**ApiV1ServerFollowingPostRequest**](ApiV1ServerFollowingPostRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **500** | cannot follow a non-HTTPS server |  -  |

