# MyHistoryApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1UsersMeHistoryVideosGet**](MyHistoryApi.md#apiV1UsersMeHistoryVideosGet) | **GET** /api/v1/users/me/history/videos | List watched videos history |
| [**apiV1UsersMeHistoryVideosRemovePost**](MyHistoryApi.md#apiV1UsersMeHistoryVideosRemovePost) | **POST** /api/v1/users/me/history/videos/remove | Clear video history |
| [**apiV1UsersMeHistoryVideosVideoIdDelete**](MyHistoryApi.md#apiV1UsersMeHistoryVideosVideoIdDelete) | **DELETE** /api/v1/users/me/history/videos/{videoId} | Delete history element |


<a id="apiV1UsersMeHistoryVideosGet"></a>
# **apiV1UsersMeHistoryVideosGet**
> VideoListResponse apiV1UsersMeHistoryVideosGet(start, count, search)

List watched videos history

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyHistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MyHistoryApi apiInstance = new MyHistoryApi(defaultClient);
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String search = "search_example"; // String | Plain text search, applied to various parts of the model depending on endpoint
    try {
      VideoListResponse result = apiInstance.apiV1UsersMeHistoryVideosGet(start, count, search);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyHistoryApi#apiV1UsersMeHistoryVideosGet");
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
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **search** | **String**| Plain text search, applied to various parts of the model depending on endpoint | [optional] |

### Return type

[**VideoListResponse**](VideoListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1UsersMeHistoryVideosRemovePost"></a>
# **apiV1UsersMeHistoryVideosRemovePost**
> apiV1UsersMeHistoryVideosRemovePost(beforeDate)

Clear video history

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyHistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MyHistoryApi apiInstance = new MyHistoryApi(defaultClient);
    OffsetDateTime beforeDate = OffsetDateTime.now(); // OffsetDateTime | history before this date will be deleted
    try {
      apiInstance.apiV1UsersMeHistoryVideosRemovePost(beforeDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyHistoryApi#apiV1UsersMeHistoryVideosRemovePost");
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
| **beforeDate** | **OffsetDateTime**| history before this date will be deleted | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |

<a id="apiV1UsersMeHistoryVideosVideoIdDelete"></a>
# **apiV1UsersMeHistoryVideosVideoIdDelete**
> apiV1UsersMeHistoryVideosVideoIdDelete(videoId)

Delete history element

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyHistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MyHistoryApi apiInstance = new MyHistoryApi(defaultClient);
    Integer videoId = 56; // Integer | 
    try {
      apiInstance.apiV1UsersMeHistoryVideosVideoIdDelete(videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyHistoryApi#apiV1UsersMeHistoryVideosVideoIdDelete");
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
| **videoId** | **Integer**|  | |

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

