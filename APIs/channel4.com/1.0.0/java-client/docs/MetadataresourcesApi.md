# MetadataresourcesApi

All URIs are relative to *http://channel4.com/pmlsd*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**brandEPGAtomFeed**](MetadataresourcesApi.md#brandEPGAtomFeed) | **GET** /{brand-web-safe-title}/epg.atom | Brand EPG Atom Feed |
| [**call4oDFeed**](MetadataresourcesApi.md#call4oDFeed) | **GET** /{brand-web-safe-title}/4od.atom | 4oD Feed |
| [**clipDetailAtomFeed**](MetadataresourcesApi.md#clipDetailAtomFeed) | **GET** /{brand-web-safe-title}/videos/{clip-asset-id}.atom | Clip Detail Atom Feed |
| [**clipsLandingFeedBrandSeriesAndEpisodeLevels**](MetadataresourcesApi.md#clipsLandingFeedBrandSeriesAndEpisodeLevels) | **GET** /{brand-web-safe-title}/videos/all.atom | Clips Landing Feed Brand Series and Episode Levels |
| [**clipsLandingFeedBrandSeriesAndEpisodeLevels2**](MetadataresourcesApi.md#clipsLandingFeedBrandSeriesAndEpisodeLevels2) | **GET** /{brand-web-safe-title}/videos/series-{series_number}.atom | Clips Landing Feed Brand Series and Episode Levels(2) |
| [**clipsLandingFeedBrandSeriesAndEpisodeLevels3**](MetadataresourcesApi.md#clipsLandingFeedBrandSeriesAndEpisodeLevels3) | **GET** /{brand-web-safe-title}/videos/series-{series_number}/episode-{episode_number}.atom | Clips Landing Feed Brand Series and Episode Levels(3) |
| [**comingSoonFeed**](MetadataresourcesApi.md#comingSoonFeed) | **GET** /coming-soon.atom | Coming Soon feed |
| [**comingSoonFeed2**](MetadataresourcesApi.md#comingSoonFeed2) | **GET** /coming-soon/{category}.atom | Coming Soon feed(2) |
| [**episodeGuideFeedEpisodeDetail**](MetadataresourcesApi.md#episodeGuideFeedEpisodeDetail) | **GET** /{brand-web-safe-title}/episode-guide/series-{series_number}/episode-{episode_number}.atom | Episode Guide Feed Episode Detail |
| [**episodeGuideFeedSeriesDetail**](MetadataresourcesApi.md#episodeGuideFeedSeriesDetail) | **GET** /{brand-web-safe-title}/episode-guide/series-{series_number}.atom | Episode Guide Feed Series Detail |
| [**episodeGuideFeedSeriesLanding**](MetadataresourcesApi.md#episodeGuideFeedSeriesLanding) | **GET** /{brand-web-safe-title}/episode-guide.atom | Episode Guide Feed Series Landing |
| [**hubFeed**](MetadataresourcesApi.md#hubFeed) | **GET** /{brand-web-safe-title}.atom | Hub Feed |
| [**programmeFeed**](MetadataresourcesApi.md#programmeFeed) | **GET** /programme/{programme-id}.atom | Programme Feed |


<a id="brandEPGAtomFeed"></a>
# **brandEPGAtomFeed**
> Atom brandEPGAtomFeed(brandWebSafeTitle, platform)

Brand EPG Atom Feed

This feed contains metadata about upcoming electronic programme guide (EPG)    information for a brand. The entry details upcoming transmission slots for    this brand.    http://api.channel4.com/pmlsd/brand-web-safe-title/epg.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/the-simpsons/epg.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    MetadataresourcesApi apiInstance = new MetadataresourcesApi(defaultClient);
    String brandWebSafeTitle = "brandWebSafeTitle_example"; // String | Title of the programme for which you seek EPG information
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.brandEPGAtomFeed(brandWebSafeTitle, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataresourcesApi#brandEPGAtomFeed");
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
| **brandWebSafeTitle** | **String**| Title of the programme for which you seek EPG information | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="call4oDFeed"></a>
# **call4oDFeed**
> Atom call4oDFeed(brandWebSafeTitle, platform)

4oD Feed

A feed containing all available on-demand long-form content for a specified    brand. The entries for the 4oD feed contain references to each long-form    asset for a brand, ordered by series number and episode number.    http://api.channel4.com/pmlsd/[brand-web-safe-title]/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/the-it-crowd/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    MetadataresourcesApi apiInstance = new MetadataresourcesApi(defaultClient);
    String brandWebSafeTitle = "brandWebSafeTitle_example"; // String | The title of the programme for which you seek on-demand content
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.call4oDFeed(brandWebSafeTitle, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataresourcesApi#call4oDFeed");
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
| **brandWebSafeTitle** | **String**| The title of the programme for which you seek on-demand content | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="clipDetailAtomFeed"></a>
# **clipDetailAtomFeed**
> Atom clipDetailAtomFeed(brandWebSafeTitle, clipAssetId, platform)

Clip Detail Atom Feed

A feed containing metadata about a single short-form video (clip).    http://api.channel4.com/pmlsd/brand-web-safe-title/videos/clip-asset-id.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/the-it-crowd/videos/TCGS_CLIP_0000001015.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    MetadataresourcesApi apiInstance = new MetadataresourcesApi(defaultClient);
    String brandWebSafeTitle = "brandWebSafeTitle_example"; // String | Title of the brand for which you seek a clip
    String clipAssetId = "clipAssetId_example"; // String | Asset id for this clip
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.clipDetailAtomFeed(brandWebSafeTitle, clipAssetId, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataresourcesApi#clipDetailAtomFeed");
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
| **brandWebSafeTitle** | **String**| Title of the brand for which you seek a clip | |
| **clipAssetId** | **String**| Asset id for this clip | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="clipsLandingFeedBrandSeriesAndEpisodeLevels"></a>
# **clipsLandingFeedBrandSeriesAndEpisodeLevels**
> Atom clipsLandingFeedBrandSeriesAndEpisodeLevels(brandWebSafeTitle, platform)

Clips Landing Feed Brand Series and Episode Levels

A feed containing metadata about all the short-form (clip) videos. The clips    feed can be accessed at different levels: the content is then filtered    depending on the level, but the structure is identical.When accessed: from    the top, the feed contains all the clips for the brand;  at series level,    the feed contains only clips from the series; and  at episode level, the    feed contains only clips for the episode (and is very unlikely to require    pagination). The entries for the Clips Landing Feed contain references to    each short-form asset.    http://api.channel4.com/pmlsd/brand-web-safe-title/videos/all.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/peep-show/videos.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    MetadataresourcesApi apiInstance = new MetadataresourcesApi(defaultClient);
    String brandWebSafeTitle = "brandWebSafeTitle_example"; // String | Title of brand to which clips belong
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.clipsLandingFeedBrandSeriesAndEpisodeLevels(brandWebSafeTitle, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataresourcesApi#clipsLandingFeedBrandSeriesAndEpisodeLevels");
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
| **brandWebSafeTitle** | **String**| Title of brand to which clips belong | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="clipsLandingFeedBrandSeriesAndEpisodeLevels2"></a>
# **clipsLandingFeedBrandSeriesAndEpisodeLevels2**
> Atom clipsLandingFeedBrandSeriesAndEpisodeLevels2(brandWebSafeTitle, seriesNumber, platform)

Clips Landing Feed Brand Series and Episode Levels(2)

A feed containing metadata about all the short-form (clip) videos. The clips    feed can be accessed at different levels: the content is then filtered    depending on the level, but the structure is identical.When accessed: from    the top, the feed contains all the clips for the brand;  at series level,    the feed contains only clips from the series; and  at episode level, the    feed contains only clips for the episode (and is very unlikely to require    pagination). The entries for the Clips Landing Feed contain references to    each short-form asset.    http://api.channel4.com/pmlsd/brand-web-safe-title/videos/series-series_number.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/peep-show/videos.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    MetadataresourcesApi apiInstance = new MetadataresourcesApi(defaultClient);
    String brandWebSafeTitle = "brandWebSafeTitle_example"; // String | Title of brand to which clips belong
    String seriesNumber = "seriesNumber_example"; // String | Unique identifier of series to which clips belong
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.clipsLandingFeedBrandSeriesAndEpisodeLevels2(brandWebSafeTitle, seriesNumber, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataresourcesApi#clipsLandingFeedBrandSeriesAndEpisodeLevels2");
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
| **brandWebSafeTitle** | **String**| Title of brand to which clips belong | |
| **seriesNumber** | **String**| Unique identifier of series to which clips belong | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="clipsLandingFeedBrandSeriesAndEpisodeLevels3"></a>
# **clipsLandingFeedBrandSeriesAndEpisodeLevels3**
> Atom clipsLandingFeedBrandSeriesAndEpisodeLevels3(brandWebSafeTitle, seriesNumber, episodeNumber, platform)

Clips Landing Feed Brand Series and Episode Levels(3)

A feed containing metadata about all the short-form (clip) videos. The clips    feed can be accessed at different levels: the content is then filtered    depending on the level, but the structure is identical.When accessed: from    the top, the feed contains all the clips for the brand;  at series level,    the feed contains only clips from the series; and  at episode level, the    feed contains only clips for the episode (and is very unlikely to require    pagination). The entries for the Clips Landing Feed contain references to    each short-form asset.    http://api.channel4.com/pmlsd/brand-web-safe-title/videos/series-series_number/episode-episode_number.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/peep-show/videos.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    MetadataresourcesApi apiInstance = new MetadataresourcesApi(defaultClient);
    String brandWebSafeTitle = "brandWebSafeTitle_example"; // String | Title of brand to which clips belong
    String seriesNumber = "seriesNumber_example"; // String | Unique identifier of series to which clips belong
    String episodeNumber = "episodeNumber_example"; // String | Unique identifier of episode to which clips belong
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.clipsLandingFeedBrandSeriesAndEpisodeLevels3(brandWebSafeTitle, seriesNumber, episodeNumber, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataresourcesApi#clipsLandingFeedBrandSeriesAndEpisodeLevels3");
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
| **brandWebSafeTitle** | **String**| Title of brand to which clips belong | |
| **seriesNumber** | **String**| Unique identifier of series to which clips belong | |
| **episodeNumber** | **String**| Unique identifier of episode to which clips belong | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="comingSoonFeed"></a>
# **comingSoonFeed**
> Atom comingSoonFeed(platform)

Coming Soon feed

Coming Soon feed display a list of episodes coming soon to linear TV so that    I can promote new Channel 4 content.    http://api.channel4.com/pmlsd/coming-soon.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/coming-soon.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    MetadataresourcesApi apiInstance = new MetadataresourcesApi(defaultClient);
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.comingSoonFeed(platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataresourcesApi#comingSoonFeed");
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
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="comingSoonFeed2"></a>
# **comingSoonFeed2**
> Atom comingSoonFeed2(category, platform)

Coming Soon feed(2)

Coming Soon feed display a list of episodes coming soon to linear TV so that    I can promote new Channel 4 content.    http://api.channel4.com/pmlsd/coming-soon/[category].atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/coming-soon.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    MetadataresourcesApi apiInstance = new MetadataresourcesApi(defaultClient);
    String category = "category_example"; // String | The category websafe_title to filter the coming soon programmes on TV.
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.comingSoonFeed2(category, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataresourcesApi#comingSoonFeed2");
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
| **category** | **String**| The category websafe_title to filter the coming soon programmes on TV. | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="episodeGuideFeedEpisodeDetail"></a>
# **episodeGuideFeedEpisodeDetail**
> Atom episodeGuideFeedEpisodeDetail(brandWebSafeTitle, seriesNumber, episodeNumber, platform)

Episode Guide Feed Episode Detail

A feed containing metadata about a specified episode. (This feed does not    contain any entries and only contains a feed element regarding this    episode.)    http://api.channel4.com/pmlsd/brand-web-safe-title/episode-guide/series-series_number/episode-episode_number.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/the-it-crowd/episode-guide/series-1/episode-1.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    MetadataresourcesApi apiInstance = new MetadataresourcesApi(defaultClient);
    String brandWebSafeTitle = "brandWebSafeTitle_example"; // String | Title of the brand to which the episode belongs
    String seriesNumber = "seriesNumber_example"; // String | Unique enumerated identifier of the series within its brand to which the episode belongs
    String episodeNumber = "episodeNumber_example"; // String | Unique enumerated identifier of the episode within its series
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.episodeGuideFeedEpisodeDetail(brandWebSafeTitle, seriesNumber, episodeNumber, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataresourcesApi#episodeGuideFeedEpisodeDetail");
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
| **brandWebSafeTitle** | **String**| Title of the brand to which the episode belongs | |
| **seriesNumber** | **String**| Unique enumerated identifier of the series within its brand to which the episode belongs | |
| **episodeNumber** | **String**| Unique enumerated identifier of the episode within its series | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="episodeGuideFeedSeriesDetail"></a>
# **episodeGuideFeedSeriesDetail**
> Atom episodeGuideFeedSeriesDetail(brandWebSafeTitle, seriesNumber, platform)

Episode Guide Feed Series Detail

A feed containing metadata about all the episodes for a specific series. The    entries in this feed contain references to each of the episodes (where    metadata has been published), with some convenient links.    http://api.channel4.com/pmlsd/brand-web-safe-title/episode-guide/series-series_number.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/chelmsford-123/episode-guide/series-1.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    MetadataresourcesApi apiInstance = new MetadataresourcesApi(defaultClient);
    String brandWebSafeTitle = "brandWebSafeTitle_example"; // String | The title of the programme for which you seek series-related information
    String seriesNumber = "seriesNumber_example"; // String | Unique enumerated identifier of the series within its brand
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.episodeGuideFeedSeriesDetail(brandWebSafeTitle, seriesNumber, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataresourcesApi#episodeGuideFeedSeriesDetail");
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
| **brandWebSafeTitle** | **String**| The title of the programme for which you seek series-related information | |
| **seriesNumber** | **String**| Unique enumerated identifier of the series within its brand | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="episodeGuideFeedSeriesLanding"></a>
# **episodeGuideFeedSeriesLanding**
> Atom episodeGuideFeedSeriesLanding(brandWebSafeTitle, platform)

Episode Guide Feed Series Landing

A feed containing metadata about all series for a specified brand. The    entries in this feed contain references to each of the series (where    metadata has been published), with some convenient links.    http://api.channel4.com/pmlsd/brand-web-safe-title/episode-guide.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/father-ted/episode-guide.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    MetadataresourcesApi apiInstance = new MetadataresourcesApi(defaultClient);
    String brandWebSafeTitle = "brandWebSafeTitle_example"; // String | The title of the programme for which you seek episode-guide information
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.episodeGuideFeedSeriesLanding(brandWebSafeTitle, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataresourcesApi#episodeGuideFeedSeriesLanding");
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
| **brandWebSafeTitle** | **String**| The title of the programme for which you seek episode-guide information | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="hubFeed"></a>
# **hubFeed**
> Atom hubFeed(brandWebSafeTitle, platform)

Hub Feed

The basis for all brand information    http://api.channel4.com/pmlsd/brand-web-safe-title.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/the-it-crowd.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    MetadataresourcesApi apiInstance = new MetadataresourcesApi(defaultClient);
    String brandWebSafeTitle = "brandWebSafeTitle_example"; // String | The title of the programme for which you seek associated data
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.hubFeed(brandWebSafeTitle, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataresourcesApi#hubFeed");
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
| **brandWebSafeTitle** | **String**| The title of the programme for which you seek associated data | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="programmeFeed"></a>
# **programmeFeed**
> Atom programmeFeed(programmeId, platform)

Programme Feed

A feed containing all long-form content currently or previously available    for a specified Programme Id. The entries for the Programme feed contain    references to long-form assets for each platform.    http://api.channel4.com/pmlsd/programme/[programme-id].atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx    http://api.channel4.com/pmlsd/programme/33881-001/4od.atom?apikey&#x3D;xxxxxxxxxxxxxxxxxxxxxxxx

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataresourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://channel4.com/pmlsd");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    MetadataresourcesApi apiInstance = new MetadataresourcesApi(defaultClient);
    String programmeId = "programmeId_example"; // String | The websafe programme identifier for the episode for which you seek on-demand content
    String platform = "c4"; // String | The platform to use for the query. Alias 'client'.
    try {
      Atom result = apiInstance.programmeFeed(programmeId, platform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataresourcesApi#programmeFeed");
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
| **programmeId** | **String**| The websafe programme identifier for the episode for which you seek on-demand content | |
| **platform** | **String**| The platform to use for the query. Alias &#39;client&#39;. | [optional] [enum: c4, ps3, yv, ios, fm, p06, ctv, freesat, android, samsung] |

### Return type

[**Atom**](Atom.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

