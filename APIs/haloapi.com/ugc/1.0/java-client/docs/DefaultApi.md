# DefaultApi

All URIs are relative to *https://www.haloapi.com/ugc*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**call58acde292109180bdcacc40c**](DefaultApi.md#call58acde292109180bdcacc40c) | **GET** /h5/players/{player}/gamevariants/{variant} | Halo 5 - Player Game Variant |
| [**call58acde292109180bdcacc40d**](DefaultApi.md#call58acde292109180bdcacc40d) | **GET** /h5/players/{player}/gamevariants | Halo 5 - Player Game Variants |
| [**call58acde292109180bdcacc40e**](DefaultApi.md#call58acde292109180bdcacc40e) | **GET** /h5/players/{player}/mapvariants/{variant} | Halo 5 - Player Map Variant |
| [**call58acde292109180bdcacc40f**](DefaultApi.md#call58acde292109180bdcacc40f) | **GET** /h5/players/{player}/mapvariants | Halo 5 - Player Map Variants |


<a id="call58acde292109180bdcacc40c"></a>
# **call58acde292109180bdcacc40c**
> call58acde292109180bdcacc40c(player, variant)

Halo 5 - Player Game Variant

&lt;p&gt;Retrieves Metadata about a Player-created Game Variant.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Get Game Variant\&quot; to \&quot;Halo 5 - Player Game Variant\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;August 5, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/ugc");
    
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
    String player = "player_example"; // String | The Gamertag of the Player that owns the Game Variant.
    String variant = "variant_example"; // String | The ID for the Game Variant.
    try {
      apiInstance.call58acde292109180bdcacc40c(player, variant);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call58acde292109180bdcacc40c");
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
| **player** | **String**| The Gamertag of the Player that owns the Game Variant. | |
| **variant** | **String**| The ID for the Game Variant. | |

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
| **400** | Specified Gamertag is malformed or the Game Variant ID is malformed. |  -  |
| **404** | The player does not exist or the Game Variant does not exist in the provided Player&#39;s file share. |  -  |
| **500** | Internal Server Error |  -  |

<a id="call58acde292109180bdcacc40d"></a>
# **call58acde292109180bdcacc40d**
> call58acde292109180bdcacc40d(player, start, count, sort, order)

Halo 5 - Player Game Variants

&lt;p&gt;Retrieves a list of Game Variants created by a Player.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;List Game Variants\&quot; to \&quot;Halo 5 - Player Game Variants\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;August 5, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/ugc");
    
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
    String player = "player_example"; // String | The Gamertag of the Player that owns the listed Game Variants.
    BigDecimal start = new BigDecimal(78); // BigDecimal | When specified, this indicates the starting index (0-based) for which the list of results will begin at.
    BigDecimal count = new BigDecimal(78); // BigDecimal | When specified, this indicates the maximum quantity of items the caller would like returned in the response.
    BigDecimal sort = new BigDecimal(78); // BigDecimal | When specified, this indicates what field should be used to sort the results as the primary sort order. When omitted, \"modified\" (descending) is the assumed primary sort order. Allowed sort fields are: name, description, accessibility, created, modified, bookmarkCount.
    BigDecimal order = new BigDecimal(78); // BigDecimal | When specified, this indicates the ordering that will be applied. When omitted, \"desc\" is assumed. Allowed order values are: asc, desc.
    try {
      apiInstance.call58acde292109180bdcacc40d(player, start, count, sort, order);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call58acde292109180bdcacc40d");
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
| **player** | **String**| The Gamertag of the Player that owns the listed Game Variants. | |
| **start** | **BigDecimal**| When specified, this indicates the starting index (0-based) for which the list of results will begin at. | [optional] |
| **count** | **BigDecimal**| When specified, this indicates the maximum quantity of items the caller would like returned in the response. | [optional] |
| **sort** | **BigDecimal**| When specified, this indicates what field should be used to sort the results as the primary sort order. When omitted, \&quot;modified\&quot; (descending) is the assumed primary sort order. Allowed sort fields are: name, description, accessibility, created, modified, bookmarkCount. | [optional] |
| **order** | **BigDecimal**| When specified, this indicates the ordering that will be applied. When omitted, \&quot;desc\&quot; is assumed. Allowed order values are: asc, desc. | [optional] |

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
| **200** | The response body will contain a list of the Player-created Game Variants. |  -  |
| **400** | Specified Gamertag is malformed. |  -  |
| **404** | The player does not exist. |  -  |
| **500** | Internal Server Error |  -  |

<a id="call58acde292109180bdcacc40e"></a>
# **call58acde292109180bdcacc40e**
> call58acde292109180bdcacc40e(player, variant)

Halo 5 - Player Map Variant

&lt;p&gt;Retrieves Metadata about a Player-created Map Variant.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;Get Map Variant\&quot; to \&quot;Halo 5 - Player Map Variant\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;August 5, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/ugc");
    
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
    String player = "player_example"; // String | The Gamertag of the Player that owns the Map Variant.
    String variant = "variant_example"; // String | The ID for the Map Variant.
    try {
      apiInstance.call58acde292109180bdcacc40e(player, variant);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call58acde292109180bdcacc40e");
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
| **player** | **String**| The Gamertag of the Player that owns the Map Variant. | |
| **variant** | **String**| The ID for the Map Variant. | |

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
| **200** | The response body will contain the Metadata for the Player-created Map Variant. |  -  |
| **400** | Specified Gamertag is malformed or the Map Variant ID is malformed. |  -  |
| **404** | The Player does not exist or the Map Variant does not exist in the provided Player&#39;s file share. |  -  |
| **500** | Internal Server Error |  -  |

<a id="call58acde292109180bdcacc40f"></a>
# **call58acde292109180bdcacc40f**
> call58acde292109180bdcacc40f(player, start, count, sort, order)

Halo 5 - Player Map Variants

&lt;p&gt;Retrieves a list Map Variants created by a Player.&lt;/p&gt; &lt;br /&gt; &lt;h4&gt;Changelog&lt;/h4&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;February 21, 2017:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Renamed Endpoint from \&quot;List Map Variants\&quot; to \&quot;Halo 5 - Player Map Variants\&quot;.&lt;/li&gt;         &lt;li&gt;Removed \&quot;{title}\&quot; Request Parameter.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; &lt;div class&#x3D;\&quot;panel-body\&quot;&gt;     &lt;p&gt;&lt;strong&gt;August 5, 2016:&lt;/strong&gt;&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;Added Endpoint.&lt;/li&gt;     &lt;/ul&gt; &lt;/div&gt; 

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
    defaultClient.setBasePath("https://www.haloapi.com/ugc");
    
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
    String player = "player_example"; // String | The Gamertag of the Player that owns the listed Map Variants.
    BigDecimal start = new BigDecimal(78); // BigDecimal | When specified, this indicates the starting index (0-based) for which the list of results will begin at.
    BigDecimal count = new BigDecimal(78); // BigDecimal | When specified, this indicates the maximum quantity of items the caller would like returned in the response.
    BigDecimal sort = new BigDecimal(78); // BigDecimal | When specified, this indicates what field should be used to sort the results as the primary sort order. When omitted, \"modified\" (descending) is the assumed primary sort order. Allowed sort fields are: name, description, accessibility, created, modified, bookmarkCount.
    BigDecimal order = new BigDecimal(78); // BigDecimal | When specified, this indicates the ordering that will be applied. When omitted, \"desc\" is assumed. Allowed order values are: asc, desc.
    try {
      apiInstance.call58acde292109180bdcacc40f(player, start, count, sort, order);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call58acde292109180bdcacc40f");
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
| **player** | **String**| The Gamertag of the Player that owns the listed Map Variants. | |
| **start** | **BigDecimal**| When specified, this indicates the starting index (0-based) for which the list of results will begin at. | [optional] |
| **count** | **BigDecimal**| When specified, this indicates the maximum quantity of items the caller would like returned in the response. | [optional] |
| **sort** | **BigDecimal**| When specified, this indicates what field should be used to sort the results as the primary sort order. When omitted, \&quot;modified\&quot; (descending) is the assumed primary sort order. Allowed sort fields are: name, description, accessibility, created, modified, bookmarkCount. | [optional] |
| **order** | **BigDecimal**| When specified, this indicates the ordering that will be applied. When omitted, \&quot;desc\&quot; is assumed. Allowed order values are: asc, desc. | [optional] |

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
| **200** | The response body will contain a list of the Player-created Map Variants. |  -  |
| **400** | Specified Gamertag is malformed. |  -  |
| **404** | The Player does not exist. |  -  |
| **500** | Internal Server Error |  -  |

