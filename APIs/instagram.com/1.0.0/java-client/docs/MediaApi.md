# MediaApi

All URIs are relative to *https://api.instagram.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mediaMediaIdGet**](MediaApi.md#mediaMediaIdGet) | **GET** /media/{media-id} | Get information about a media object. |
| [**mediaPopularGet**](MediaApi.md#mediaPopularGet) | **GET** /media/popular | Get a list of currently popular media. |
| [**mediaSearchGet**](MediaApi.md#mediaSearchGet) | **GET** /media/search | Search for media in a given area. |
| [**mediaShortcodeShortcodeGet**](MediaApi.md#mediaShortcodeShortcodeGet) | **GET** /media/shortcode/{shortcode} | Get information about a media object. |


<a id="mediaMediaIdGet"></a>
# **mediaMediaIdGet**
> MediaEntryResponse mediaMediaIdGet(mediaId)

Get information about a media object.

Get information about a media object. The returned type key will allow you to differentiate between image and video media.  **Note:** if you authenticate with an OAuth Token, you will receive the user_has_liked key which quickly tells you whether the current user has liked this media item. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaApi;

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

    MediaApi apiInstance = new MediaApi(defaultClient);
    String mediaId = "mediaId_example"; // String | The ID of the media resource.
    try {
      MediaEntryResponse result = apiInstance.mediaMediaIdGet(mediaId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaApi#mediaMediaIdGet");
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
| **mediaId** | **String**| The ID of the media resource. | |

### Return type

[**MediaEntryResponse**](MediaEntryResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Media resource information. |  -  |

<a id="mediaPopularGet"></a>
# **mediaPopularGet**
> MediaSearchResponse mediaPopularGet()

Get a list of currently popular media.

Get a list of what media is most popular at the moment. Can return mix of &#x60;image&#x60; and &#x60;video&#x60; types.  **Warning:** [Deprecated](http://instagram.com/developer/changelog/) for Apps created **on or after** Nov 17, 2015 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaApi;

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

    MediaApi apiInstance = new MediaApi(defaultClient);
    try {
      MediaSearchResponse result = apiInstance.mediaPopularGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaApi#mediaPopularGet");
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

[**MediaSearchResponse**](MediaSearchResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Found media resources (without likes information). |  -  |

<a id="mediaSearchGet"></a>
# **mediaSearchGet**
> MediaSearchResponse mediaSearchGet(lat, lng, minTimestamp, maxTimestamp, distance)

Search for media in a given area.

Search for media in a given area. The default time span is set to 5 days. The time span must not exceed 7 days. Defaults time stamps cover the last 5 days. Can return mix of &#x60;image&#x60; and &#x60;video&#x60; types. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaApi;

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

    MediaApi apiInstance = new MediaApi(defaultClient);
    Double lat = 3.4D; // Double | Latitude of the center search coordinate. If used, `lng` is required.
    Double lng = 3.4D; // Double | Longitude of the center search coordinate. If used, `lat` is required.
    Long minTimestamp = 56L; // Long | A unix timestamp. All media returned will be taken later than this timestamp.
    Long maxTimestamp = 56L; // Long | A unix timestamp. All media returned will be taken earlier than this timestamp.
    Integer distance = 56; // Integer | Default is 1km (distance=1000), max distance is 5km.
    try {
      MediaSearchResponse result = apiInstance.mediaSearchGet(lat, lng, minTimestamp, maxTimestamp, distance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaApi#mediaSearchGet");
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
| **lat** | **Double**| Latitude of the center search coordinate. If used, &#x60;lng&#x60; is required. | |
| **lng** | **Double**| Longitude of the center search coordinate. If used, &#x60;lat&#x60; is required. | |
| **minTimestamp** | **Long**| A unix timestamp. All media returned will be taken later than this timestamp. | [optional] |
| **maxTimestamp** | **Long**| A unix timestamp. All media returned will be taken earlier than this timestamp. | [optional] |
| **distance** | **Integer**| Default is 1km (distance&#x3D;1000), max distance is 5km. | [optional] |

### Return type

[**MediaSearchResponse**](MediaSearchResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Found media resources (without likes information) in a given area. |  -  |

<a id="mediaShortcodeShortcodeGet"></a>
# **mediaShortcodeShortcodeGet**
> MediaEntryResponse mediaShortcodeShortcodeGet(shortcode)

Get information about a media object.

This endpoint returns the same response as &#x60;GET /media/{media-id}&#x60;.  A media object&#39;s shortcode can be found in its shortlink URL. An example shortlink is &#x60;http://instagram.com/p/D/&#x60;, its corresponding shortcode is &#x60;D&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaApi;

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

    MediaApi apiInstance = new MediaApi(defaultClient);
    String shortcode = "shortcode_example"; // String | The short code of the media resource.
    try {
      MediaEntryResponse result = apiInstance.mediaShortcodeShortcodeGet(shortcode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaApi#mediaShortcodeShortcodeGet");
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
| **shortcode** | **String**| The short code of the media resource. | |

### Return type

[**MediaEntryResponse**](MediaEntryResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Media resource information. |  -  |

