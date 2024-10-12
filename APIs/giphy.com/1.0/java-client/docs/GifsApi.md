# GifsApi

All URIs are relative to *https://api.giphy.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getGifById**](GifsApi.md#getGifById) | **GET** /gifs/{gifId} | Get GIF by Id |
| [**getGifsById**](GifsApi.md#getGifsById) | **GET** /gifs | Get GIFs by ID |
| [**randomGif**](GifsApi.md#randomGif) | **GET** /gifs/random | Random GIF |
| [**searchGifs**](GifsApi.md#searchGifs) | **GET** /gifs/search | Search GIFs |
| [**translateGif**](GifsApi.md#translateGif) | **GET** /gifs/translate | Translate phrase to GIF |
| [**trendingGifs**](GifsApi.md#trendingGifs) | **GET** /gifs/trending | Trending GIFs |


<a id="getGifById"></a>
# **getGifById**
> RandomGif200Response getGifById(gifId)

Get GIF by Id

Returns a GIF given that GIF&#39;s unique ID 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GifsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.giphy.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GifsApi apiInstance = new GifsApi(defaultClient);
    Integer gifId = 56; // Integer | Filters results by specified GIF ID.
    try {
      RandomGif200Response result = apiInstance.getGifById(gifId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GifsApi#getGifById");
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
| **gifId** | **Integer**| Filters results by specified GIF ID. | |

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

<a id="getGifsById"></a>
# **getGifsById**
> GetGifsById200Response getGifsById(ids)

Get GIFs by ID

A multiget version of the get GIF by ID endpoint. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GifsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.giphy.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GifsApi apiInstance = new GifsApi(defaultClient);
    String ids = "ids_example"; // String | Filters results by specified GIF IDs, separated by commas.
    try {
      GetGifsById200Response result = apiInstance.getGifsById(ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GifsApi#getGifsById");
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
| **ids** | **String**| Filters results by specified GIF IDs, separated by commas. | [optional] |

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

<a id="randomGif"></a>
# **randomGif**
> RandomGif200Response randomGif(tag, rating)

Random GIF

Returns a random GIF, limited by tag. Excluding the tag parameter will return a random GIF from the GIPHY catalog. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GifsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.giphy.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GifsApi apiInstance = new GifsApi(defaultClient);
    String tag = "tag_example"; // String | Filters results by specified tag.
    String rating = "rating_example"; // String | Filters results by specified rating.
    try {
      RandomGif200Response result = apiInstance.randomGif(tag, rating);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GifsApi#randomGif");
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

<a id="searchGifs"></a>
# **searchGifs**
> GetGifsById200Response searchGifs(q, limit, offset, rating, lang)

Search GIFs

Search all GIPHY GIFs for a word or phrase. Punctuation will be stripped and ignored.  Use a plus or url encode for phrases. Example paul+rudd, ryan+gosling or american+psycho. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GifsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.giphy.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GifsApi apiInstance = new GifsApi(defaultClient);
    String q = "q_example"; // String | Search query term or prhase.
    Integer limit = 25; // Integer | The maximum number of records to return.
    Integer offset = 0; // Integer | An optional results offset.
    String rating = "rating_example"; // String | Filters results by specified rating.
    String lang = "lang_example"; // String | Specify default language for regional content; use a 2-letter ISO 639-1 language code.
    try {
      GetGifsById200Response result = apiInstance.searchGifs(q, limit, offset, rating, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GifsApi#searchGifs");
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

<a id="translateGif"></a>
# **translateGif**
> RandomGif200Response translateGif(s)

Translate phrase to GIF

The translate API draws on search, but uses the GIPHY &#x60;special sauce&#x60; to handle translating from one vocabulary to another. In this case, words and phrases to GIF 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GifsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.giphy.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GifsApi apiInstance = new GifsApi(defaultClient);
    String s = "s_example"; // String | Search term.
    try {
      RandomGif200Response result = apiInstance.translateGif(s);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GifsApi#translateGif");
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

<a id="trendingGifs"></a>
# **trendingGifs**
> GetGifsById200Response trendingGifs(limit, offset, rating)

Trending GIFs

Fetch GIFs currently trending online. Hand curated by the GIPHY editorial team.  The data returned mirrors the GIFs showcased on the GIPHY homepage. Returns 25 results by default. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GifsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.giphy.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    GifsApi apiInstance = new GifsApi(defaultClient);
    Integer limit = 25; // Integer | The maximum number of records to return.
    Integer offset = 0; // Integer | An optional results offset.
    String rating = "rating_example"; // String | Filters results by specified rating.
    try {
      GetGifsById200Response result = apiInstance.trendingGifs(limit, offset, rating);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GifsApi#trendingGifs");
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

