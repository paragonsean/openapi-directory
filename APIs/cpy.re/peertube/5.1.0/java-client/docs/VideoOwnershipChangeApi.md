# VideoOwnershipChangeApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1VideosIdGiveOwnershipPost**](VideoOwnershipChangeApi.md#apiV1VideosIdGiveOwnershipPost) | **POST** /api/v1/videos/{id}/give-ownership | Request ownership change |
| [**apiV1VideosOwnershipGet**](VideoOwnershipChangeApi.md#apiV1VideosOwnershipGet) | **GET** /api/v1/videos/ownership | List video ownership changes |
| [**apiV1VideosOwnershipIdAcceptPost**](VideoOwnershipChangeApi.md#apiV1VideosOwnershipIdAcceptPost) | **POST** /api/v1/videos/ownership/{id}/accept | Accept ownership change request |
| [**apiV1VideosOwnershipIdRefusePost**](VideoOwnershipChangeApi.md#apiV1VideosOwnershipIdRefusePost) | **POST** /api/v1/videos/ownership/{id}/refuse | Refuse ownership change request |


<a id="apiV1VideosIdGiveOwnershipPost"></a>
# **apiV1VideosIdGiveOwnershipPost**
> apiV1VideosIdGiveOwnershipPost(id, username)

Request ownership change

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoOwnershipChangeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoOwnershipChangeApi apiInstance = new VideoOwnershipChangeApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    String username = "username_example"; // String | 
    try {
      apiInstance.apiV1VideosIdGiveOwnershipPost(id, username);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoOwnershipChangeApi#apiV1VideosIdGiveOwnershipPost");
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
| **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | |
| **username** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **400** | changing video ownership to a remote account is not supported yet |  -  |
| **404** | video not found |  -  |

<a id="apiV1VideosOwnershipGet"></a>
# **apiV1VideosOwnershipGet**
> apiV1VideosOwnershipGet()

List video ownership changes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoOwnershipChangeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoOwnershipChangeApi apiInstance = new VideoOwnershipChangeApi(defaultClient);
    try {
      apiInstance.apiV1VideosOwnershipGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoOwnershipChangeApi#apiV1VideosOwnershipGet");
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

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1VideosOwnershipIdAcceptPost"></a>
# **apiV1VideosOwnershipIdAcceptPost**
> apiV1VideosOwnershipIdAcceptPost(id)

Accept ownership change request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoOwnershipChangeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoOwnershipChangeApi apiInstance = new VideoOwnershipChangeApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    try {
      apiInstance.apiV1VideosOwnershipIdAcceptPost(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoOwnershipChangeApi#apiV1VideosOwnershipIdAcceptPost");
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
| **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | |

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
| **403** | cannot terminate an ownership change of another user |  -  |
| **404** | video ownership change not found |  -  |

<a id="apiV1VideosOwnershipIdRefusePost"></a>
# **apiV1VideosOwnershipIdRefusePost**
> apiV1VideosOwnershipIdRefusePost(id)

Refuse ownership change request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoOwnershipChangeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoOwnershipChangeApi apiInstance = new VideoOwnershipChangeApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    try {
      apiInstance.apiV1VideosOwnershipIdRefusePost(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoOwnershipChangeApi#apiV1VideosOwnershipIdRefusePost");
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
| **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | |

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
| **403** | cannot terminate an ownership change of another user |  -  |
| **404** | video ownership change not found |  -  |

