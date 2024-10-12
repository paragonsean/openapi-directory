# MySubscriptionsApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1UsersMeSubscriptionsExistGet**](MySubscriptionsApi.md#apiV1UsersMeSubscriptionsExistGet) | **GET** /api/v1/users/me/subscriptions/exist | Get if subscriptions exist for my user |
| [**apiV1UsersMeSubscriptionsGet**](MySubscriptionsApi.md#apiV1UsersMeSubscriptionsGet) | **GET** /api/v1/users/me/subscriptions | Get my user subscriptions |
| [**apiV1UsersMeSubscriptionsPost**](MySubscriptionsApi.md#apiV1UsersMeSubscriptionsPost) | **POST** /api/v1/users/me/subscriptions | Add subscription to my user |
| [**apiV1UsersMeSubscriptionsSubscriptionHandleDelete**](MySubscriptionsApi.md#apiV1UsersMeSubscriptionsSubscriptionHandleDelete) | **DELETE** /api/v1/users/me/subscriptions/{subscriptionHandle} | Delete subscription of my user |
| [**apiV1UsersMeSubscriptionsSubscriptionHandleGet**](MySubscriptionsApi.md#apiV1UsersMeSubscriptionsSubscriptionHandleGet) | **GET** /api/v1/users/me/subscriptions/{subscriptionHandle} | Get subscription of my user |
| [**apiV1UsersMeSubscriptionsVideosGet**](MySubscriptionsApi.md#apiV1UsersMeSubscriptionsVideosGet) | **GET** /api/v1/users/me/subscriptions/videos | List videos of subscriptions of my user |


<a id="apiV1UsersMeSubscriptionsExistGet"></a>
# **apiV1UsersMeSubscriptionsExistGet**
> Object apiV1UsersMeSubscriptionsExistGet(uris)

Get if subscriptions exist for my user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MySubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MySubscriptionsApi apiInstance = new MySubscriptionsApi(defaultClient);
    List<URI> uris = Arrays.asList(); // List<URI> | list of uris to check if each is part of the user subscriptions
    try {
      Object result = apiInstance.apiV1UsersMeSubscriptionsExistGet(uris);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MySubscriptionsApi#apiV1UsersMeSubscriptionsExistGet");
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
| **uris** | [**List&lt;URI&gt;**](URI.md)| list of uris to check if each is part of the user subscriptions | |

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1UsersMeSubscriptionsGet"></a>
# **apiV1UsersMeSubscriptionsGet**
> VideoChannelList apiV1UsersMeSubscriptionsGet(start, count, sort)

Get my user subscriptions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MySubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MySubscriptionsApi apiInstance = new MySubscriptionsApi(defaultClient);
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    try {
      VideoChannelList result = apiInstance.apiV1UsersMeSubscriptionsGet(start, count, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MySubscriptionsApi#apiV1UsersMeSubscriptionsGet");
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
| **sort** | **String**| Sort column | [optional] |

### Return type

[**VideoChannelList**](VideoChannelList.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1UsersMeSubscriptionsPost"></a>
# **apiV1UsersMeSubscriptionsPost**
> apiV1UsersMeSubscriptionsPost(apiV1UsersMeSubscriptionsPostRequest)

Add subscription to my user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MySubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MySubscriptionsApi apiInstance = new MySubscriptionsApi(defaultClient);
    ApiV1UsersMeSubscriptionsPostRequest apiV1UsersMeSubscriptionsPostRequest = new ApiV1UsersMeSubscriptionsPostRequest(); // ApiV1UsersMeSubscriptionsPostRequest | 
    try {
      apiInstance.apiV1UsersMeSubscriptionsPost(apiV1UsersMeSubscriptionsPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MySubscriptionsApi#apiV1UsersMeSubscriptionsPost");
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
| **apiV1UsersMeSubscriptionsPostRequest** | [**ApiV1UsersMeSubscriptionsPostRequest**](ApiV1UsersMeSubscriptionsPostRequest.md)|  | [optional] |

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
| **200** | successful operation |  -  |

<a id="apiV1UsersMeSubscriptionsSubscriptionHandleDelete"></a>
# **apiV1UsersMeSubscriptionsSubscriptionHandleDelete**
> apiV1UsersMeSubscriptionsSubscriptionHandleDelete(subscriptionHandle)

Delete subscription of my user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MySubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MySubscriptionsApi apiInstance = new MySubscriptionsApi(defaultClient);
    String subscriptionHandle = "my_username | my_username@example.com"; // String | The subscription handle
    try {
      apiInstance.apiV1UsersMeSubscriptionsSubscriptionHandleDelete(subscriptionHandle);
    } catch (ApiException e) {
      System.err.println("Exception when calling MySubscriptionsApi#apiV1UsersMeSubscriptionsSubscriptionHandleDelete");
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
| **subscriptionHandle** | **String**| The subscription handle | |

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

<a id="apiV1UsersMeSubscriptionsSubscriptionHandleGet"></a>
# **apiV1UsersMeSubscriptionsSubscriptionHandleGet**
> VideoChannel apiV1UsersMeSubscriptionsSubscriptionHandleGet(subscriptionHandle)

Get subscription of my user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MySubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MySubscriptionsApi apiInstance = new MySubscriptionsApi(defaultClient);
    String subscriptionHandle = "my_username | my_username@example.com"; // String | The subscription handle
    try {
      VideoChannel result = apiInstance.apiV1UsersMeSubscriptionsSubscriptionHandleGet(subscriptionHandle);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MySubscriptionsApi#apiV1UsersMeSubscriptionsSubscriptionHandleGet");
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
| **subscriptionHandle** | **String**| The subscription handle | |

### Return type

[**VideoChannel**](VideoChannel.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1UsersMeSubscriptionsVideosGet"></a>
# **apiV1UsersMeSubscriptionsVideosGet**
> VideoListResponse apiV1UsersMeSubscriptionsVideosGet(categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched)

List videos of subscriptions of my user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MySubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    MySubscriptionsApi apiInstance = new MySubscriptionsApi(defaultClient);
    GetAccountVideosCategoryOneOfParameter categoryOneOf = new GetAccountVideosCategoryOneOfParameter(); // GetAccountVideosCategoryOneOfParameter | category id of the video (see [/videos/categories](#operation/getCategories))
    Boolean isLive = true; // Boolean | whether or not the video is a live
    GetAccountVideosTagsOneOfParameter tagsOneOf = new GetAccountVideosTagsOneOfParameter(); // GetAccountVideosTagsOneOfParameter | tag(s) of the video
    GetAccountVideosTagsAllOfParameter tagsAllOf = new GetAccountVideosTagsAllOfParameter(); // GetAccountVideosTagsAllOfParameter | tag(s) of the video, where all should be present in the video
    GetAccountVideosLicenceOneOfParameter licenceOneOf = new GetAccountVideosLicenceOneOfParameter(); // GetAccountVideosLicenceOneOfParameter | licence id of the video (see [/videos/licences](#operation/getLicences))
    GetAccountVideosLanguageOneOfParameter languageOneOf = new GetAccountVideosLanguageOneOfParameter(); // GetAccountVideosLanguageOneOfParameter | language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language
    String nsfw = "true"; // String | whether to include nsfw videos, if any
    Boolean isLocal = true; // Boolean | **PeerTube >= 4.0** Display only local or remote videos
    Integer include = 0; // Integer | **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES 
    VideoPrivacySet privacyOneOf = VideoPrivacySet.fromValue("1"); // VideoPrivacySet | **PeerTube >= 4.0** Display only videos in this specific privacy/privacies
    Boolean hasHLSFiles = true; // Boolean | **PeerTube >= 4.0** Display only videos that have HLS files
    Boolean hasWebtorrentFiles = true; // Boolean | **PeerTube >= 4.0** Display only videos that have WebTorrent files
    String skipCount = "true"; // String | if you don't need the `total` in the response
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "name"; // String | 
    Boolean excludeAlreadyWatched = true; // Boolean | Whether or not to exclude videos that are in the user's video history
    try {
      VideoListResponse result = apiInstance.apiV1UsersMeSubscriptionsVideosGet(categoryOneOf, isLive, tagsOneOf, tagsAllOf, licenceOneOf, languageOneOf, nsfw, isLocal, include, privacyOneOf, hasHLSFiles, hasWebtorrentFiles, skipCount, start, count, sort, excludeAlreadyWatched);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MySubscriptionsApi#apiV1UsersMeSubscriptionsVideosGet");
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
| **categoryOneOf** | [**GetAccountVideosCategoryOneOfParameter**](.md)| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] |
| **isLive** | **Boolean**| whether or not the video is a live | [optional] |
| **tagsOneOf** | [**GetAccountVideosTagsOneOfParameter**](.md)| tag(s) of the video | [optional] |
| **tagsAllOf** | [**GetAccountVideosTagsAllOfParameter**](.md)| tag(s) of the video, where all should be present in the video | [optional] |
| **licenceOneOf** | [**GetAccountVideosLicenceOneOfParameter**](.md)| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] |
| **languageOneOf** | [**GetAccountVideosLanguageOneOfParameter**](.md)| language id of the video (see [/videos/languages](#operation/getLanguages)). Use &#x60;_unknown&#x60; to filter on videos that don&#39;t have a video language | [optional] |
| **nsfw** | **String**| whether to include nsfw videos, if any | [optional] [enum: true, false] |
| **isLocal** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only local or remote videos | [optional] |
| **include** | **Integer**| **PeerTube &gt;&#x3D; 4.0** Include additional videos in results (can be combined using bitwise or operator) - &#x60;0&#x60; NONE - &#x60;1&#x60; NOT_PUBLISHED_STATE - &#x60;2&#x60; BLACKLISTED - &#x60;4&#x60; BLOCKED_OWNER - &#x60;8&#x60; FILES  | [optional] [enum: 0, 1, 2, 4, 8] |
| **privacyOneOf** | [**VideoPrivacySet**](.md)| **PeerTube &gt;&#x3D; 4.0** Display only videos in this specific privacy/privacies | [optional] [enum: 1, 2, 3, 4] |
| **hasHLSFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have HLS files | [optional] |
| **hasWebtorrentFiles** | **Boolean**| **PeerTube &gt;&#x3D; 4.0** Display only videos that have WebTorrent files | [optional] |
| **skipCount** | **String**| if you don&#39;t need the &#x60;total&#x60; in the response | [optional] [default to false] [enum: true, false] |
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**|  | [optional] [enum: name, -duration, -createdAt, -publishedAt, -views, -likes, -trending, -hot, -best] |
| **excludeAlreadyWatched** | **Boolean**| Whether or not to exclude videos that are in the user&#39;s video history | [optional] |

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

