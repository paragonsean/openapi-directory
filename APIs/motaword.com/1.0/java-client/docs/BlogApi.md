# BlogApi

All URIs are relative to *https://api.motaword.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBlogPosts**](BlogApi.md#getBlogPosts) | **GET** /blogs | Get blog posts - ordered by created desc by default |


<a id="getBlogPosts"></a>
# **getBlogPosts**
> BlogArticleList getBlogPosts(locale, fallback, page, perPage)

Get blog posts - ordered by created desc by default

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    BlogApi apiInstance = new BlogApi(defaultClient);
    String locale = "locale_example"; // String | Article language, default `en`. When no blog article is available and `fallback=true` is specified, it falls back to `en`.
    Boolean fallback = true; // Boolean | When `true`, and no article is found in the locale, it falls back to `locale=en`.
    Long page = 1L; // Long | 
    Long perPage = 1L; // Long | 
    try {
      BlogArticleList result = apiInstance.getBlogPosts(locale, fallback, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlogApi#getBlogPosts");
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
| **locale** | **String**| Article language, default &#x60;en&#x60;. When no blog article is available and &#x60;fallback&#x3D;true&#x60; is specified, it falls back to &#x60;en&#x60;. | [optional] |
| **fallback** | **Boolean**| When &#x60;true&#x60;, and no article is found in the locale, it falls back to &#x60;locale&#x3D;en&#x60;. | [optional] |
| **page** | **Long**|  | [optional] [default to 1] |
| **perPage** | **Long**|  | [optional] [default to 1] |

### Return type

[**BlogArticleList**](BlogArticleList.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of blog articles |  -  |

