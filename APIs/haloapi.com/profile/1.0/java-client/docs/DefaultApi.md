# DefaultApi

All URIs are relative to *https://www.haloapi.com/profile*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**halo5PlayerAppearance**](DefaultApi.md#halo5PlayerAppearance) | **GET** /h5/profiles/{player}/appearance | Halo 5 - Player Appearance |
| [**halo5PlayerEmblemImage**](DefaultApi.md#halo5PlayerEmblemImage) | **GET** /h5/profiles/{player}/emblem | Halo 5 - Player Emblem Image |
| [**halo5PlayerSpartanImage**](DefaultApi.md#halo5PlayerSpartanImage) | **GET** /h5/profiles/{player}/spartan | Halo 5 - Player Spartan Image |


<a id="halo5PlayerAppearance"></a>
# **halo5PlayerAppearance**
> halo5PlayerAppearance(player)

Halo 5 - Player Appearance

&lt;p&gt;This Endpoint retrieves appearance information for a player.&lt;/p&gt; &lt;p&gt;If the player is a member of a Company, the Company&#39;s ID and Name will be provided. Additional Company information is available via the Stats API.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;July 14, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.haloapi.com/profile");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String player = "player_example"; // String | The Player's Gamertag
    try {
      apiInstance.halo5PlayerAppearance(player);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5PlayerAppearance");
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
| **player** | **String**| The Player&#39;s Gamertag | |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response body will contain the Metadata for the Player-created Game Variant. |  -  |
| **404** | Specified Player was not found. |  -  |
| **500** | Internal Server Error. |  -  |

<a id="halo5PlayerEmblemImage"></a>
# **halo5PlayerEmblemImage**
> halo5PlayerEmblemImage(player, size)

Halo 5 - Player Emblem Image

&lt;p&gt;This Endpoint returns an HTTP Redirect (302 Found) response to the caller with the URL of an image of the Player&#39;s Emblem. The initial request to this API that returns the HTTP Redirect is throttled and requires a Subscription Key. However, the image itself (at hostname \&quot;image.halocdn.com\&quot;) is not throttled and does not require a Subscription Key. Note that if the Player later changes their Emblem, the image itself is not refreshed and will need to be refreshed via a new request to this API.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;August 12, 2019:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Expanded documentation for the HTTP 400 response code to cover unsupported emblem component(s).&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;July 14, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Halo 5 - Emblem Image\&quot; to \&quot;Halo 5 - Player Emblem Image\&quot;.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Emblem Image\&quot; to \&quot;Halo 5 - Emblem Image\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.haloapi.com/profile");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String player = "player_example"; // String | The Player's Gamertag.
    BigDecimal size = new BigDecimal(78); // BigDecimal | An optional size (specified in pixels) of the image requested. When specified, this value must be one of the following values: 95, 128, 190, 256, 512. If a value is specified that is not in this list, the API returns HTTP 400 (\"Bad Request\"). If the size is empty or missing, the API will use 256.
    try {
      apiInstance.halo5PlayerEmblemImage(player, size);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5PlayerEmblemImage");
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
| **player** | **String**| The Player&#39;s Gamertag. | |
| **size** | **BigDecimal**| An optional size (specified in pixels) of the image requested. When specified, this value must be one of the following values: 95, 128, 190, 256, 512. If a value is specified that is not in this list, the API returns HTTP 400 (\&quot;Bad Request\&quot;). If the size is empty or missing, the API will use 256. | [optional] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | Golden Path. The Location header should point at the corresponding Emblem image. |  -  |
| **400** | An unsupported value was provided for a query string parameter or the Player&#39;s Emblem contains unsupported component(s) and cannot be rendered at this time. |  -  |
| **404** | Specified Player was not found. |  -  |
| **500** | Internal Server Error. |  -  |

<a id="halo5PlayerSpartanImage"></a>
# **halo5PlayerSpartanImage**
> halo5PlayerSpartanImage(player, size, crop)

Halo 5 - Player Spartan Image

&lt;p&gt;This Endpoint returns an HTTP Redirect (302 Found) response to the caller with the URL of an image of the Player&#39;s Spartan&#39;s appearance. The initial request to this API that returns the HTTP Redirect is throttled and requires a Subscription Key. However, the image itself (at hostname \&quot;image.halocdn.com\&quot;) is not throttled and does not require a Subscription Key. Note that if the Player later changes their Spartan&#39;s appearance, the image itself is not refreshed and will need to be refreshed via a new request to this API.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;August 12, 2019:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Expanded documentation for the HTTP 400 response code to cover unsupported armor component(s).&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;July 14, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Halo 5 - Spartan Image\&quot; to \&quot;Halo 5 - Player Spartan Image\&quot;.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Spartan Image\&quot; to \&quot;Halo 5 - Spartan Image\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.haloapi.com/profile");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String player = "player_example"; // String | The Player's Gamertag.
    BigDecimal size = new BigDecimal(78); // BigDecimal | An optional size (specified in pixels) of the image requested. When specified, this value must be one of the following values: 95, 128, 190, 256, 512. If a value is specified that is not in this list, the API returns HTTP 400 (\"Bad Request\"). If the size is empty or missing, the API will use 256.
    String crop = "crop_example"; // String | An optional crop that will be used to determine what portion of the Spartan is returned in the image. The value must be either \"full\" or \"portrait\". If no value is specified \"full\" is used. If an unsupported value is provided, the API returns HTTP 400 (\"Bad Request\").
    try {
      apiInstance.halo5PlayerSpartanImage(player, size, crop);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#halo5PlayerSpartanImage");
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
| **player** | **String**| The Player&#39;s Gamertag. | |
| **size** | **BigDecimal**| An optional size (specified in pixels) of the image requested. When specified, this value must be one of the following values: 95, 128, 190, 256, 512. If a value is specified that is not in this list, the API returns HTTP 400 (\&quot;Bad Request\&quot;). If the size is empty or missing, the API will use 256. | [optional] |
| **crop** | **String**| An optional crop that will be used to determine what portion of the Spartan is returned in the image. The value must be either \&quot;full\&quot; or \&quot;portrait\&quot;. If no value is specified \&quot;full\&quot; is used. If an unsupported value is provided, the API returns HTTP 400 (\&quot;Bad Request\&quot;). | [optional] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | Golden Path. The Location header should point at the corresponding Spartan image. |  -  |
| **400** | An unsupported value was provided for a query string parameter or the Player&#39;s Spartan is equipped with unsupported component(s) and cannot be rendered at this time. |  -  |
| **404** | Specified Player was not found. |  -  |
| **500** | Internal Server Error. |  -  |

