# VideosEmbedPrivacyApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVideoPrivacyDomain**](VideosEmbedPrivacyApi.md#addVideoPrivacyDomain) | **PUT** /videos/{video_id}/privacy/domains/{domain} | Permit a video to be embedded on a domain |
| [**deleteVideoPrivacyDomain**](VideosEmbedPrivacyApi.md#deleteVideoPrivacyDomain) | **DELETE** /videos/{video_id}/privacy/domains/{domain} | Restrict a video from being embedded on a domain |
| [**getVideoPrivacyDomains**](VideosEmbedPrivacyApi.md#getVideoPrivacyDomains) | **GET** /videos/{video_id}/privacy/domains | Get all the domains on which a video can be embedded |


<a id="addVideoPrivacyDomain"></a>
# **addVideoPrivacyDomain**
> addVideoPrivacyDomain(domain, videoId)

Permit a video to be embedded on a domain

If domain privacy is enabled for this video, this method permits the video to be embedded on the specified domain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosEmbedPrivacyApi;

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

    VideosEmbedPrivacyApi apiInstance = new VideosEmbedPrivacyApi(defaultClient);
    String domain = "example.com"; // String | The domain name.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.addVideoPrivacyDomain(domain, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosEmbedPrivacyApi#addVideoPrivacyDomain");
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
| **domain** | **String**| The domain name. | |
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
| **204** | The video is now embeddable on the domain. |  -  |
| **403** | The video doesn&#39;t have a user-defined access list. |  -  |

<a id="deleteVideoPrivacyDomain"></a>
# **deleteVideoPrivacyDomain**
> deleteVideoPrivacyDomain(domain, videoId)

Restrict a video from being embedded on a domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosEmbedPrivacyApi;

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

    VideosEmbedPrivacyApi apiInstance = new VideosEmbedPrivacyApi(defaultClient);
    String domain = "example.com"; // String | The domain name.
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    try {
      apiInstance.deleteVideoPrivacyDomain(domain, videoId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosEmbedPrivacyApi#deleteVideoPrivacyDomain");
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
| **domain** | **String**| The domain name. | |
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
| **204** | The video was disallowed from being embedded on the domain. |  -  |
| **403** | The video isn&#39;t set to a user-defined access list. |  -  |
| **404** | No such domain exists. |  -  |

<a id="getVideoPrivacyDomains"></a>
# **getVideoPrivacyDomains**
> List&lt;Domain&gt; getVideoPrivacyDomains(videoId, page, perPage)

Get all the domains on which a video can be embedded

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosEmbedPrivacyApi;

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

    VideosEmbedPrivacyApi apiInstance = new VideosEmbedPrivacyApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    try {
      List<Domain> result = apiInstance.getVideoPrivacyDomains(videoId, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosEmbedPrivacyApi#getVideoPrivacyDomains");
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

[**List&lt;Domain&gt;**](Domain.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.domain+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The domains were returned. |  -  |
| **403** | There are no domains on which the video can be embedded. |  -  |

