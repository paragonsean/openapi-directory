# ArtistsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v3ArtistsImagesGet**](ArtistsApi.md#v3ArtistsImagesGet) | **GET** /v3/artists/images | Search for images by a photographer |
| [**v3ArtistsVideosGet**](ArtistsApi.md#v3ArtistsVideosGet) | **GET** /v3/artists/videos | Search for videos by a photographer |


<a id="v3ArtistsImagesGet"></a>
# **v3ArtistsImagesGet**
> v3ArtistsImagesGet(acceptLanguage, artistName, fields, page, pageSize)

Search for images by a photographer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: Api-Key
    ApiKeyAuth Api-Key = (ApiKeyAuth) defaultClient.getAuthentication("Api-Key");
    Api-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Api-Key.setApiKeyPrefix("Token");

    ArtistsApi apiInstance = new ArtistsApi(defaultClient);
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    String artistName = "artistName_example"; // String | Name of artist for desired images
    List<ArtistsImageSearchFieldValues> fields = Arrays.asList(); // List<ArtistsImageSearchFieldValues> | Comma separated list of fields. Allows restricting which fields are returned. If no fields are selected, the summary_set of fields are returned.
    Integer page = 1; // Integer | Identifies page to return. Default page is 1.
    Integer pageSize = 10; // Integer | Specifies page size. Default page_size is 10, maximum page_size is 100.
    try {
      apiInstance.v3ArtistsImagesGet(acceptLanguage, artistName, fields, page, pageSize);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtistsApi#v3ArtistsImagesGet");
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
| **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] |
| **artistName** | **String**| Name of artist for desired images | [optional] |
| **fields** | [**List&lt;ArtistsImageSearchFieldValues&gt;**](ArtistsImageSearchFieldValues.md)| Comma separated list of fields. Allows restricting which fields are returned. If no fields are selected, the summary_set of fields are returned. | [optional] |
| **page** | **Integer**| Identifies page to return. Default page is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| Specifies page size. Default page_size is 10, maximum page_size is 100. | [optional] [default to 10] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | InvalidParameterValue |  -  |
| **401** | Unauthorized |  -  |

<a id="v3ArtistsVideosGet"></a>
# **v3ArtistsVideosGet**
> v3ArtistsVideosGet(acceptLanguage, artistName, fields, page, pageSize)

Search for videos by a photographer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: Api-Key
    ApiKeyAuth Api-Key = (ApiKeyAuth) defaultClient.getAuthentication("Api-Key");
    Api-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Api-Key.setApiKeyPrefix("Token");

    ArtistsApi apiInstance = new ArtistsApi(defaultClient);
    String acceptLanguage = "acceptLanguage_example"; // String | Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    String artistName = "artistName_example"; // String | Name of artist for desired images
    List<ArtistsVideoSearchFieldValues> fields = Arrays.asList(); // List<ArtistsVideoSearchFieldValues> | Comma separated list of fields. Allows restricting which fields are returned. If no fields are selected, the summary_set of fields are returned.
    Integer page = 1; // Integer | Identifies page to return. Default page is 1.
    Integer pageSize = 10; // Integer | Specifies page size. Default page_size is 10, maximum page_size is 100.
    try {
      apiInstance.v3ArtistsVideosGet(acceptLanguage, artistName, fields, page, pageSize);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtistsApi#v3ArtistsVideosGet");
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
| **acceptLanguage** | **String**| Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only). | [optional] |
| **artistName** | **String**| Name of artist for desired images | [optional] |
| **fields** | [**List&lt;ArtistsVideoSearchFieldValues&gt;**](ArtistsVideoSearchFieldValues.md)| Comma separated list of fields. Allows restricting which fields are returned. If no fields are selected, the summary_set of fields are returned. | [optional] |
| **page** | **Integer**| Identifies page to return. Default page is 1. | [optional] [default to 1] |
| **pageSize** | **Integer**| Specifies page size. Default page_size is 10, maximum page_size is 100. | [optional] [default to 10] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | InvalidParameterValue |  -  |
| **401** | Unauthorized |  -  |

