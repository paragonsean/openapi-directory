# DirectoryApiApi

All URIs are relative to *https://listen-api.listennotes.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBestPodcasts**](DirectoryApiApi.md#getBestPodcasts) | **GET** /best_podcasts | Fetch a list of best podcasts by genre |
| [**getCuratedPodcastById**](DirectoryApiApi.md#getCuratedPodcastById) | **GET** /curated_podcasts/{id} | Fetch a curated list of podcasts by id |
| [**getCuratedPodcasts**](DirectoryApiApi.md#getCuratedPodcasts) | **GET** /curated_podcasts | Fetch curated lists of podcasts |
| [**getEpisodeById**](DirectoryApiApi.md#getEpisodeById) | **GET** /episodes/{id} | Fetch detailed meta data for an episode by id |
| [**getEpisodeRecommendations**](DirectoryApiApi.md#getEpisodeRecommendations) | **GET** /episodes/{id}/recommendations | Fetch recommendations for an episode |
| [**getEpisodesInBatch**](DirectoryApiApi.md#getEpisodesInBatch) | **POST** /episodes | Batch fetch basic meta data for episodes |
| [**getGenres**](DirectoryApiApi.md#getGenres) | **GET** /genres | Fetch a list of podcast genres |
| [**getLanguages**](DirectoryApiApi.md#getLanguages) | **GET** /languages | Fetch a list of supported languages for podcasts |
| [**getPodcastById**](DirectoryApiApi.md#getPodcastById) | **GET** /podcasts/{id} | Fetch detailed meta data and episodes for a podcast by id |
| [**getPodcastRecommendations**](DirectoryApiApi.md#getPodcastRecommendations) | **GET** /podcasts/{id}/recommendations | Fetch recommendations for a podcast |
| [**getPodcastsInBatch**](DirectoryApiApi.md#getPodcastsInBatch) | **POST** /podcasts | Batch fetch basic meta data for podcasts |
| [**getRegions**](DirectoryApiApi.md#getRegions) | **GET** /regions | Fetch a list of supported countries/regions for best podcasts |
| [**justListen**](DirectoryApiApi.md#justListen) | **GET** /just_listen | Fetch a random podcast episode |


<a id="getBestPodcasts"></a>
# **getBestPodcasts**
> BestPodcastsResponse getBestPodcasts(xListenAPIKey, genreId, page, region, publisherRegion, language, sort, safeMode)

Fetch a list of best podcasts by genre

Get a list of curated best podcasts by genre, which are curated by Listen Notes staffs based on various signals from the Internet, e.g., top charts on other podcast platforms, recommendations from mainstream media, user activities on listennotes.com... You can get the genre ids from &#x60;GET /genres&#x60; endpoint. This endpoint returns same data as https://www.listennotes.com/best-podcasts/ 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoryApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    DirectoryApiApi apiInstance = new DirectoryApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    String genreId = "genreId_example"; // String | You can get the id from `GET /genres`. If not specified, it'll be the overall best podcasts, which can be considered as a special genre.
    Integer page = 56; // Integer | Page number of those podcasts in this genre.
    String region = "us"; // String | Filter best podcasts by country/region. Please note that podcasts that are \"best\" in a country/region may not be produced in that country/region. For example, a podcast from the US may be very popular in Canada. You can get the supported country codes (e.g., us, jp, gb...) from `GET /regions`. If not specified, you'll get \"best podcasts\" in United States. 
    String publisherRegion = "publisherRegion_example"; // String | Filter best podcasts by the publisher's country/region. This is to narrow down the results to include \"best podcasts\" produced in a specific country/region. You can get the supported country codes (e.g., us, jp, gb...) from `GET /regions`. If not specified, you'll get \"best podcasts\" produced in any country/region. If you want to get a country/region's \"best podcasts\" that are also produced in that country/region, then you need to specify both **region** and **publisher_region**, e.g., `region=jp` and `publisher_region=jp`. 
    String language = "language_example"; // String | Filter best podcasts by language. You can get a list of supported languages (e.g., English, Chinese, Japanese...) from `GET /languages`. If not specified, you'll get \"best podcasts\" in any language. 
    String sort = "recent_added_first"; // String | How do you want to sort these podcasts? If you'd like to sort by popularity, please use **listen_score**. 
    Integer safeMode = 0; // Integer | Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no.
    try {
      BestPodcastsResponse result = apiInstance.getBestPodcasts(xListenAPIKey, genreId, page, region, publisherRegion, language, sort, safeMode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoryApiApi#getBestPodcasts");
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
| **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | |
| **genreId** | **String**| You can get the id from &#x60;GET /genres&#x60;. If not specified, it&#39;ll be the overall best podcasts, which can be considered as a special genre. | [optional] |
| **page** | **Integer**| Page number of those podcasts in this genre. | [optional] |
| **region** | **String**| Filter best podcasts by country/region. Please note that podcasts that are \&quot;best\&quot; in a country/region may not be produced in that country/region. For example, a podcast from the US may be very popular in Canada. You can get the supported country codes (e.g., us, jp, gb...) from &#x60;GET /regions&#x60;. If not specified, you&#39;ll get \&quot;best podcasts\&quot; in United States.  | [optional] [default to us] |
| **publisherRegion** | **String**| Filter best podcasts by the publisher&#39;s country/region. This is to narrow down the results to include \&quot;best podcasts\&quot; produced in a specific country/region. You can get the supported country codes (e.g., us, jp, gb...) from &#x60;GET /regions&#x60;. If not specified, you&#39;ll get \&quot;best podcasts\&quot; produced in any country/region. If you want to get a country/region&#39;s \&quot;best podcasts\&quot; that are also produced in that country/region, then you need to specify both **region** and **publisher_region**, e.g., &#x60;region&#x3D;jp&#x60; and &#x60;publisher_region&#x3D;jp&#x60;.  | [optional] |
| **language** | **String**| Filter best podcasts by language. You can get a list of supported languages (e.g., English, Chinese, Japanese...) from &#x60;GET /languages&#x60;. If not specified, you&#39;ll get \&quot;best podcasts\&quot; in any language.  | [optional] |
| **sort** | **String**| How do you want to sort these podcasts? If you&#39;d like to sort by popularity, please use **listen_score**.  | [optional] [default to recent_added_first] [enum: recent_added_first, oldest_added_first, recent_published_first, oldest_published_first, listen_score] |
| **safeMode** | **Integer**| Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no. | [optional] [default to 0] [enum: 0, 1] |

### Return type

[**BestPodcastsResponse**](BestPodcastsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **401** |  |  -  |
| **404** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

<a id="getCuratedPodcastById"></a>
# **getCuratedPodcastById**
> CuratedListFull getCuratedPodcastById(xListenAPIKey, id)

Fetch a curated list of podcasts by id

Get detailed meta data of all podcasts in a specific curated list. This endpoint returns same data as https://www.listennotes.com/curated-podcasts/ 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoryApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    DirectoryApiApi apiInstance = new DirectoryApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    String id = "id_example"; // String | id for a specific curated list of podcasts. You can get the id from the response of `GET /search?type=curated` or `GET /curated_podcasts`. 
    try {
      CuratedListFull result = apiInstance.getCuratedPodcastById(xListenAPIKey, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoryApiApi#getCuratedPodcastById");
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
| **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | |
| **id** | **String**| id for a specific curated list of podcasts. You can get the id from the response of &#x60;GET /search?type&#x3D;curated&#x60; or &#x60;GET /curated_podcasts&#x60;.  | |

### Return type

[**CuratedListFull**](CuratedListFull.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **401** |  |  -  |
| **404** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

<a id="getCuratedPodcasts"></a>
# **getCuratedPodcasts**
> GetCuratedPodcastsResponse getCuratedPodcasts(xListenAPIKey, page)

Fetch curated lists of podcasts

A bunch of curated lists from online media. For each list, you&#39;ll get basic info of up to 5 podcasts. To get detailed meta data of all podcasts in a specific list, you need to use &#x60;GET /curated_podcasts/{id}&#x60;. We add new curated lists to the database on a daily basis. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoryApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    DirectoryApiApi apiInstance = new DirectoryApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    Integer page = 1; // Integer | Page number of curated lists.
    try {
      GetCuratedPodcastsResponse result = apiInstance.getCuratedPodcasts(xListenAPIKey, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoryApiApi#getCuratedPodcasts");
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
| **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | |
| **page** | **Integer**| Page number of curated lists. | [optional] [default to 1] |

### Return type

[**GetCuratedPodcastsResponse**](GetCuratedPodcastsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **401** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

<a id="getEpisodeById"></a>
# **getEpisodeById**
> EpisodeFull getEpisodeById(xListenAPIKey, id, showTranscript)

Fetch detailed meta data for an episode by id

Fetch detailed meta data for a specific episode.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoryApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    DirectoryApiApi apiInstance = new DirectoryApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    String id = "id_example"; // String | id for a specific episode. You can get episode id from using other endpoints, e.g., `GET /search`...
    Integer showTranscript = 0; // Integer | To include the transcript of this episode or not? If it is 1, then include the transcript in the **transcript** field. The default value is 0 - we don't include transcript by default, because 1) it would make the response data very big, thus slow response time; 2) less than 1% of episodes have transcripts. The transcript field is available only in the PRO/ENTERPRISE plan.
    try {
      EpisodeFull result = apiInstance.getEpisodeById(xListenAPIKey, id, showTranscript);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoryApiApi#getEpisodeById");
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
| **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | |
| **id** | **String**| id for a specific episode. You can get episode id from using other endpoints, e.g., &#x60;GET /search&#x60;... | |
| **showTranscript** | **Integer**| To include the transcript of this episode or not? If it is 1, then include the transcript in the **transcript** field. The default value is 0 - we don&#39;t include transcript by default, because 1) it would make the response data very big, thus slow response time; 2) less than 1% of episodes have transcripts. The transcript field is available only in the PRO/ENTERPRISE plan. | [optional] [default to 0] |

### Return type

[**EpisodeFull**](EpisodeFull.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **401** |  |  -  |
| **404** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

<a id="getEpisodeRecommendations"></a>
# **getEpisodeRecommendations**
> GetEpisodeRecommendationsResponse getEpisodeRecommendations(xListenAPIKey, id, safeMode)

Fetch recommendations for an episode

Fetch up to 8 episode recommendations based on the given episode id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoryApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    DirectoryApiApi apiInstance = new DirectoryApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    String id = "254444fa6cf64a43a95292a70eb6869b"; // String | Episode id.
    Integer safeMode = 0; // Integer | Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no.
    try {
      GetEpisodeRecommendationsResponse result = apiInstance.getEpisodeRecommendations(xListenAPIKey, id, safeMode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoryApiApi#getEpisodeRecommendations");
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
| **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | |
| **id** | **String**| Episode id. | |
| **safeMode** | **Integer**| Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no. | [optional] [default to 0] [enum: 0, 1] |

### Return type

[**GetEpisodeRecommendationsResponse**](GetEpisodeRecommendationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **401** |  |  -  |
| **404** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

<a id="getEpisodesInBatch"></a>
# **getEpisodesInBatch**
> GetEpisodesInBatchResponse getEpisodesInBatch(xListenAPIKey, ids)

Batch fetch basic meta data for episodes

Batch fetch basic meta data for up to 10 episodes. This endpoint could be used to implement custom playlists for individual episodes. For detailed meta data of an individual episode, you need to use &#x60;GET /episodes/{id}&#x60;. This endpoint is available only in the PRO/ENTERPRISE plan. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoryApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    DirectoryApiApi apiInstance = new DirectoryApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    String ids = "ids_example"; // String | Comma-separated list of episode ids.
    try {
      GetEpisodesInBatchResponse result = apiInstance.getEpisodesInBatch(xListenAPIKey, ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoryApiApi#getEpisodesInBatch");
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
| **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | |
| **ids** | **String**| Comma-separated list of episode ids. | |

### Return type

[**GetEpisodesInBatchResponse**](GetEpisodesInBatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **401** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

<a id="getGenres"></a>
# **getGenres**
> GetGenresResponse getGenres(xListenAPIKey, topLevelOnly)

Fetch a list of podcast genres

Get a list of podcast genres that are supported in Listen Notes. The genre id can be passed to other endpoints as a parameter to get podcasts in a specific genre, e.g., &#x60;GET /best_podcasts&#x60;, &#x60;GET /search&#x60;... You may want to cache the list of genres on the client side. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoryApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    DirectoryApiApi apiInstance = new DirectoryApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    Integer topLevelOnly = 0; // Integer | Just show top level genres? If 1, yes, just show top level genres. If 0, no, show all genres. 
    try {
      GetGenresResponse result = apiInstance.getGenres(xListenAPIKey, topLevelOnly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoryApiApi#getGenres");
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
| **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | |
| **topLevelOnly** | **Integer**| Just show top level genres? If 1, yes, just show top level genres. If 0, no, show all genres.  | [optional] [default to 0] [enum: 0, 1] |

### Return type

[**GetGenresResponse**](GetGenresResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **401** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

<a id="getLanguages"></a>
# **getLanguages**
> GetLanguagesResponse getLanguages(xListenAPIKey)

Fetch a list of supported languages for podcasts

Get a list of languages that are supported in Listen Notes database. You can use the language string as query parameter in &#x60;GET /search&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoryApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    DirectoryApiApi apiInstance = new DirectoryApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    try {
      GetLanguagesResponse result = apiInstance.getLanguages(xListenAPIKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoryApiApi#getLanguages");
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
| **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | |

### Return type

[**GetLanguagesResponse**](GetLanguagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **401** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

<a id="getPodcastById"></a>
# **getPodcastById**
> PodcastFull getPodcastById(xListenAPIKey, id, nextEpisodePubDate, sort)

Fetch detailed meta data and episodes for a podcast by id

Fetch detailed meta data and episodes for a specific podcast (up to 10 episodes each time). You can use the **next_episode_pub_date** parameter to do pagination and fetch more episodes. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoryApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    DirectoryApiApi apiInstance = new DirectoryApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    String id = "4d3fe717742d4963a85562e9f84d8c79"; // String | Podcast id. You can get podcast id from using other endpoints, e.g., `GET /search`, `GET /best_podcasts`...
    Integer nextEpisodePubDate = 1479154463000; // Integer | For episodes pagination. It's the value of **next_episode_pub_date** from the response of last request. If not specified, just return latest 10 episodes or oldest 10 episodes, depending on the value of the **sort** parameter. 
    String sort = "recent_first"; // String | How do you want to sort the episodes of this podcast? 
    try {
      PodcastFull result = apiInstance.getPodcastById(xListenAPIKey, id, nextEpisodePubDate, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoryApiApi#getPodcastById");
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
| **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | |
| **id** | **String**| Podcast id. You can get podcast id from using other endpoints, e.g., &#x60;GET /search&#x60;, &#x60;GET /best_podcasts&#x60;... | |
| **nextEpisodePubDate** | **Integer**| For episodes pagination. It&#39;s the value of **next_episode_pub_date** from the response of last request. If not specified, just return latest 10 episodes or oldest 10 episodes, depending on the value of the **sort** parameter.  | [optional] |
| **sort** | **String**| How do you want to sort the episodes of this podcast?  | [optional] [default to recent_first] [enum: recent_first, oldest_first] |

### Return type

[**PodcastFull**](PodcastFull.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **401** |  |  -  |
| **404** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

<a id="getPodcastRecommendations"></a>
# **getPodcastRecommendations**
> GetPodcastRecommendationsResponse getPodcastRecommendations(xListenAPIKey, id, safeMode)

Fetch recommendations for a podcast

Fetch up to 8 podcast recommendations based on the given podcast id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoryApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    DirectoryApiApi apiInstance = new DirectoryApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    String id = "25212ac3c53240a880dd5032e547047b"; // String | Podcast id.
    Integer safeMode = 0; // Integer | Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no.
    try {
      GetPodcastRecommendationsResponse result = apiInstance.getPodcastRecommendations(xListenAPIKey, id, safeMode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoryApiApi#getPodcastRecommendations");
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
| **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | |
| **id** | **String**| Podcast id. | |
| **safeMode** | **Integer**| Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no. | [optional] [default to 0] [enum: 0, 1] |

### Return type

[**GetPodcastRecommendationsResponse**](GetPodcastRecommendationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **401** |  |  -  |
| **404** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

<a id="getPodcastsInBatch"></a>
# **getPodcastsInBatch**
> GetPodcastsInBatchResponse getPodcastsInBatch(xListenAPIKey, ids, itunesIds, nextEpisodePubDate, rsses, showLatestEpisodes, spotifyIds)

Batch fetch basic meta data for podcasts

Batch fetch basic meta data for up to 10 podcasts. This endpoint could be used to build something like OPML import, allowing users to import a bunch of podcasts via rss urls. For detailed meta data (including episodes) of an individual podcast, you need to use &#x60;GET /podcasts/{id}&#x60;. This endpoint is available only in the PRO/ENTERPRISE plan. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoryApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    DirectoryApiApi apiInstance = new DirectoryApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    String ids = "ids_example"; // String | Comma-separated list of podcast ids.
    String itunesIds = "itunesIds_example"; // String | Comma-separated Apple Podcasts (iTunes) ids, e.g., 659155419
    Integer nextEpisodePubDate = 56; // Integer | For latest episodes pagination. It's the value of **next_episode_pub_date** from the response of last request. If not specified, just return latest 15 episodes. 
    String rsses = "rsses_example"; // String | Comma-separated rss urls.
    Integer showLatestEpisodes = 0; // Integer | Whether or not to fetch up to 15 latest episodes from these podcasts, sorted by pub_date. 1 is yes, and 0 is no. 
    String spotifyIds = "spotifyIds_example"; // String | Comma-separated Spotify ids, e.g., 3DDfEsKDIDrTlnPOiG4ZF4
    try {
      GetPodcastsInBatchResponse result = apiInstance.getPodcastsInBatch(xListenAPIKey, ids, itunesIds, nextEpisodePubDate, rsses, showLatestEpisodes, spotifyIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoryApiApi#getPodcastsInBatch");
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
| **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | |
| **ids** | **String**| Comma-separated list of podcast ids. | [optional] |
| **itunesIds** | **String**| Comma-separated Apple Podcasts (iTunes) ids, e.g., 659155419 | [optional] |
| **nextEpisodePubDate** | **Integer**| For latest episodes pagination. It&#39;s the value of **next_episode_pub_date** from the response of last request. If not specified, just return latest 15 episodes.  | [optional] |
| **rsses** | **String**| Comma-separated rss urls. | [optional] |
| **showLatestEpisodes** | **Integer**| Whether or not to fetch up to 15 latest episodes from these podcasts, sorted by pub_date. 1 is yes, and 0 is no.  | [optional] [default to 0] [enum: 0, 1] |
| **spotifyIds** | **String**| Comma-separated Spotify ids, e.g., 3DDfEsKDIDrTlnPOiG4ZF4 | [optional] |

### Return type

[**GetPodcastsInBatchResponse**](GetPodcastsInBatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **401** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

<a id="getRegions"></a>
# **getRegions**
> GetRegionsResponse getRegions(xListenAPIKey)

Fetch a list of supported countries/regions for best podcasts

It returns a dictionary of country codes (e.g., us, gb...) &amp; country names (United States, United Kingdom...). The country code is used in the query parameter **region** of &#x60;GET /best_podcasts&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoryApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    DirectoryApiApi apiInstance = new DirectoryApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    try {
      GetRegionsResponse result = apiInstance.getRegions(xListenAPIKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoryApiApi#getRegions");
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
| **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | |

### Return type

[**GetRegionsResponse**](GetRegionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **401** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

<a id="justListen"></a>
# **justListen**
> EpisodeSimple justListen(xListenAPIKey)

Fetch a random podcast episode

Recently published episodes are more likely to be fetched. Good luck!

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectoryApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    DirectoryApiApi apiInstance = new DirectoryApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    try {
      EpisodeSimple result = apiInstance.justListen(xListenAPIKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectoryApiApi#justListen");
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
| **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | |

### Return type

[**EpisodeSimple**](EpisodeSimple.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **401** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

