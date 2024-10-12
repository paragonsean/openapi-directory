# MediaApi

All URIs are relative to *https://etmdb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mediaSearchRead**](MediaApi.md#mediaSearchRead) | **GET** /api/v1/media/search/{movie_title} | Return movie media search result |
| [**mediaSearchallRead**](MediaApi.md#mediaSearchallRead) | **GET** /api/v1/media/searchall/{user} | Return cast media search result |


<a id="mediaSearchRead"></a>
# **mediaSearchRead**
> mediaSearchRead(movieTitle)

Return movie media search result

Return movie media search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search media for movies * You can use both Amharic or English charset/font to search  For more details on how media is listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    MediaApi apiInstance = new MediaApi(defaultClient);
    String movieTitle = "movieTitle_example"; // String | 
    try {
      apiInstance.mediaSearchRead(movieTitle);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaApi#mediaSearchRead");
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
| **movieTitle** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="mediaSearchallRead"></a>
# **mediaSearchallRead**
> mediaSearchallRead(user)

Return cast media search result

Return cast media search result  ### Response Class (Status 200) __{user}__ argument can be * artist first name * artist last name * artist username  For more details on how cast media is listed [see here][ref]. [ref]: https://etmdb.com/en/cast-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    MediaApi apiInstance = new MediaApi(defaultClient);
    String user = "user_example"; // String | 
    try {
      apiInstance.mediaSearchallRead(user);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaApi#mediaSearchallRead");
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
| **user** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

