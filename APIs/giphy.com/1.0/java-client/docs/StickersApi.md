# StickersApi

All URIs are relative to *https://api.giphy.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**randomSticker**](StickersApi.md#randomSticker) | **GET** /stickers/random | Random Sticker |
| [**searchStickers**](StickersApi.md#searchStickers) | **GET** /stickers/search | Search Stickers |
| [**translateSticker**](StickersApi.md#translateSticker) | **GET** /stickers/translate | Translate phrase to Sticker |
| [**trendingStickers**](StickersApi.md#trendingStickers) | **GET** /stickers/trending | Trending Stickers |


<a id="randomSticker"></a>
# **randomSticker**
> RandomGif200Response randomSticker(tag, rating)

Random Sticker

Returns a random GIF, limited by tag. Excluding the tag parameter will return a random GIF from the GIPHY catalog. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StickersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.giphy.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    StickersApi apiInstance = new StickersApi(defaultClient);
    String tag = "tag_example"; // String | Filters results by specified tag.
    String rating = "rating_example"; // String | Filters results by specified rating.
    try {
      RandomGif200Response result = apiInstance.randomSticker(tag, rating);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StickersApi#randomSticker");
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
| **tag** | **String**| Filters results by specified tag. | [optional] |
| **rating** | **String**| Filters results by specified rating. | [optional] |

### Return type

[**RandomGif200Response**](RandomGif200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your request was formatted incorrectly or missing required parameters. |  -  |
| **403** | You weren&#39;t authorized to make your request; most likely this indicates an issue with your API Key. |  -  |
| **404** | The particular GIF you are requesting was not found. This occurs, for example, if you request a GIF by an id that does not exist. |  -  |
| **429** | Your API Key is making too many requests. Read about [requesting a Production Key](https://developers.giphy.com/docs/#access) to upgrade your API Key rate limits.  |  -  |

<a id="searchStickers"></a>
# **searchStickers**
> GetGifsById200Response searchStickers(q, limit, offset, rating, lang)

Search Stickers

Replicates the functionality and requirements of the classic GIPHY search, but returns animated stickers rather than GIFs. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StickersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.giphy.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    StickersApi apiInstance = new StickersApi(defaultClient);
    String q = "q_example"; // String | Search query term or prhase.
    Integer limit = 25; // Integer | The maximum number of records to return.
    Integer offset = 0; // Integer | An optional results offset.
    String rating = "rating_example"; // String | Filters results by specified rating.
    String lang = "lang_example"; // String | Specify default language for regional content; use a 2-letter ISO 639-1 language code.
    try {
      GetGifsById200Response result = apiInstance.searchStickers(q, limit, offset, rating, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StickersApi#searchStickers");
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
| **q** | **String**| Search query term or prhase. | |
| **limit** | **Integer**| The maximum number of records to return. | [optional] [default to 25] |
| **offset** | **Integer**| An optional results offset. | [optional] [default to 0] |
| **rating** | **String**| Filters results by specified rating. | [optional] |
| **lang** | **String**| Specify default language for regional content; use a 2-letter ISO 639-1 language code. | [optional] |

### Return type

[**GetGifsById200Response**](GetGifsById200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Search results |  -  |
| **400** | Your request was formatted incorrectly or missing required parameters. |  -  |
| **403** | You weren&#39;t authorized to make your request; most likely this indicates an issue with your API Key. |  -  |
| **404** | The particular GIF you are requesting was not found. This occurs, for example, if you request a GIF by an id that does not exist. |  -  |
| **429** | Your API Key is making too many requests. Read about [requesting a Production Key](https://developers.giphy.com/docs/#access) to upgrade your API Key rate limits.  |  -  |

<a id="translateSticker"></a>
# **translateSticker**
> RandomGif200Response translateSticker(s)

Translate phrase to Sticker

The translate API draws on search, but uses the GIPHY &#x60;special sauce&#x60; to handle translating from one vocabulary to another. In this case, words and phrases to GIFs. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StickersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.giphy.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    StickersApi apiInstance = new StickersApi(defaultClient);
    String s = "s_example"; // String | Search term.
    try {
      RandomGif200Response result = apiInstance.translateSticker(s);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StickersApi#translateSticker");
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
| **s** | **String**| Search term. | |

### Return type

[**RandomGif200Response**](RandomGif200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your request was formatted incorrectly or missing required parameters. |  -  |
| **403** | You weren&#39;t authorized to make your request; most likely this indicates an issue with your API Key. |  -  |
| **404** | The particular GIF you are requesting was not found. This occurs, for example, if you request a GIF by an id that does not exist. |  -  |
| **429** | Your API Key is making too many requests. Read about [requesting a Production Key](https://developers.giphy.com/docs/#access) to upgrade your API Key rate limits.  |  -  |

<a id="trendingStickers"></a>
# **trendingStickers**
> GetGifsById200Response trendingStickers(limit, offset, rating)

Trending Stickers

Fetch Stickers currently trending online. Hand curated by the GIPHY editorial team. Returns 25 results by default. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StickersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.giphy.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    StickersApi apiInstance = new StickersApi(defaultClient);
    Integer limit = 25; // Integer | The maximum number of records to return.
    Integer offset = 0; // Integer | An optional results offset.
    String rating = "rating_example"; // String | Filters results by specified rating.
    try {
      GetGifsById200Response result = apiInstance.trendingStickers(limit, offset, rating);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StickersApi#trendingStickers");
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
| **limit** | **Integer**| The maximum number of records to return. | [optional] [default to 25] |
| **offset** | **Integer**| An optional results offset. | [optional] [default to 0] |
| **rating** | **String**| Filters results by specified rating. | [optional] |

### Return type

[**GetGifsById200Response**](GetGifsById200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your request was formatted incorrectly or missing required parameters. |  -  |
| **403** | You weren&#39;t authorized to make your request; most likely this indicates an issue with your API Key. |  -  |
| **404** | The particular GIF you are requesting was not found. This occurs, for example, if you request a GIF by an id that does not exist. |  -  |
| **429** | Your API Key is making too many requests. Read about [requesting a Production Key](https://developers.giphy.com/docs/#access) to upgrade your API Key rate limits.  |  -  |

