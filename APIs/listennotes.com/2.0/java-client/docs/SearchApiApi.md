# SearchApiApi

All URIs are relative to *https://listen-api.listennotes.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRelatedSearches**](SearchApiApi.md#getRelatedSearches) | **GET** /related_searches | Fetch related search terms |
| [**getTrendingSearches**](SearchApiApi.md#getTrendingSearches) | **GET** /trending_searches | Fetch trending search terms |
| [**search**](SearchApiApi.md#search) | **GET** /search | Full-text search |
| [**spellcheck**](SearchApiApi.md#spellcheck) | **GET** /spellcheck | Spell check on a search term |
| [**typeahead**](SearchApiApi.md#typeahead) | **GET** /typeahead | Typeahead search |


<a id="getRelatedSearches"></a>
# **getRelatedSearches**
> RelatedSearchesResponse getRelatedSearches(xListenAPIKey, q)

Fetch related search terms

Suggest related search terms. The results are more comprehensive than from &#x60;GET /typeahead&#x60;. This endpoint is available only in the PRO/ENTERPRISE plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    SearchApiApi apiInstance = new SearchApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    String q = "q_example"; // String | Search term, e.g., person, place, topic... 
    try {
      RelatedSearchesResponse result = apiInstance.getRelatedSearches(xListenAPIKey, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApiApi#getRelatedSearches");
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
| **q** | **String**| Search term, e.g., person, place, topic...  | |

### Return type

[**RelatedSearchesResponse**](RelatedSearchesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **400** |  |  -  |
| **401** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

<a id="getTrendingSearches"></a>
# **getTrendingSearches**
> TrendingSearchesResponse getTrendingSearches(xListenAPIKey)

Fetch trending search terms

Fetch up to 10 most recent trending search terms on the Listen Notes platform.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    SearchApiApi apiInstance = new SearchApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    try {
      TrendingSearchesResponse result = apiInstance.getTrendingSearches(xListenAPIKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApiApi#getTrendingSearches");
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

[**TrendingSearchesResponse**](TrendingSearchesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **400** |  |  -  |
| **401** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

<a id="search"></a>
# **search**
> SearchResponse search(xListenAPIKey, q, sortByDate, type, offset, lenMin, lenMax, episodeCountMin, episodeCountMax, updateFreqMin, updateFreqMax, genreIds, publishedBefore, publishedAfter, onlyIn, language, region, ocid, ncid, safeMode, uniquePodcasts, pageSize)

Full-text search

Full-text search on episodes, podcasts, or curated lists of podcasts. Use the &#x60;offset&#x60; parameter to paginate through search results. The FREE plan allows to see up to 30 search results (or &#x60;offset&#x60; &lt; 30) per query. The PRO plan allows to see up to 300 search results (or &#x60;offset&#x60; &lt; 300) per query. The ENTERPRISE plan allows to see up to 10,000 search results (or &#x60;offset&#x60; &lt; 10000) per query. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    SearchApiApi apiInstance = new SearchApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    String q = "q_example"; // String | Search term, e.g., person, place, topic... You can use double quotes to do verbatim match, e.g., \"game of thrones\". Otherwise, it's fuzzy search. 
    Integer sortByDate = 0; // Integer | Sort by date or not? If 0, then sort by relevance. If 1, then sort by date. 
    String type = "episode"; // String | What type of contents do you want to search for?  
    Integer offset = 0; // Integer | Offset for search results, for pagination. You'll use **next_offset** from response for this parameter. 
    Integer lenMin = 0; // Integer | Minimum audio length in minutes. Applicable only when **type** parameter is **episode** or **podcast**. If **type** parameter is **episode**, it's for audio length of an episode. If **type** parameter is **podcast**, it's for average audio length of all episodes in a podcast. 
    Integer lenMax = 56; // Integer | Maximum audio length in minutes. Applicable only when **type** parameter is **episode** or **podcast**. If **type** parameter is **episode**, it's for audio length of an episode. If **type** parameter is **podcast**, it's for average audio length of all episodes in a podcast. 
    Integer episodeCountMin = 56; // Integer | Minimum number of episodes. Applicable only when type parameter is **podcast**. 
    Integer episodeCountMax = 56; // Integer | Maximum number of episodes. Applicable only when type parameter is **podcast**. 
    Integer updateFreqMin = 56; // Integer | Minimum update frequency in hours (how frequently does a podcast release a new episode). For example, if you want to find \"weekly\" podcasts, then you can set **update_freq_min**=144 hours (or 6 days) and **update_freq_max**=192 hours (or 8 days). Applicable only when type parameter is **podcast**. 
    Integer updateFreqMax = 56; // Integer | Maximum update frequency in hours (how frequently does a podcast release a new episode). For example, if you want to find \"weekly\" podcasts, then you can set **update_freq_min**=144 hours (or 6 days) and **update_freq_max**=192 hours (or 8 days). Applicable only when type parameter is **podcast**. 
    String genreIds = "genreIds_example"; // String | A comma-delimited string of a list of genre ids. If not specified, then all genres are included. You can find the id and the name of all genres from `GET /genres`. It works only when **type** is *episode* or *podcast*. 
    Integer publishedBefore = 56; // Integer | Only show episodes/podcasts/curated lists published before this timestamp (in milliseconds). If **published_before** & **published_after** are used at the same time, **published_before** should be bigger than **published_after**. 
    Integer publishedAfter = 0; // Integer | Only show episodes/podcasts/curated lists published after this timestamp (in milliseconds). If **published_before** & **published_after** are used at the same time, **published_before** should be bigger than **published_after**. 
    String onlyIn = "title,description,author,audio"; // String | A comma-delimited string to search only in specific fields. Allowed values are title, description, author, and audio. If not specified, then search every fields. 
    String language = "language_example"; // String | Limit search results to a specific language. If not specified, it'll be any language. You can get a list of supported languages from `GET /languages`. It works only when **type** is *episode* or *podcast*. 
    String region = "region_example"; // String | Limit search results to a specific region (e.g., us, gb, in...). If not specified, it'll be any region. You can get the supported country codes from `GET /regions`. It works only when **type** is *episode* or *podcast*. 
    String ocid = "ocid_example"; // String | A comma-delimited string of podcast ids (up to 5 podcasts) - you can get a podcast id from the **podcast_id** field in response. This parameter is to limit search results from only a few specific podcasts. It works only when **type** is *episode*. 
    String ncid = "ncid_example"; // String | A comma-delimited string of podcast ids (up to 5 podcasts) - you can get a podcast id from the **podcast_id** field in response. This parameter is to exclude search results of a few specific podcasts. It works only when **type** is *episode*. 
    Integer safeMode = 0; // Integer | Whether or not to exclude podcasts/episodes with explicit language. 1 is yes and 0 is no. It works only when **type** is *episode* or *podcast*. 
    Integer uniquePodcasts = 0; // Integer | Whether or not to keep only one episode per podcast in search results. 1 is yes and 0 is no. It works only when **type** is *episode*. 
    Integer pageSize = 10; // Integer | The maximum number of search results per page. A valid value should be an integer between 1 and 10 (inclusive). 
    try {
      SearchResponse result = apiInstance.search(xListenAPIKey, q, sortByDate, type, offset, lenMin, lenMax, episodeCountMin, episodeCountMax, updateFreqMin, updateFreqMax, genreIds, publishedBefore, publishedAfter, onlyIn, language, region, ocid, ncid, safeMode, uniquePodcasts, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApiApi#search");
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
| **q** | **String**| Search term, e.g., person, place, topic... You can use double quotes to do verbatim match, e.g., \&quot;game of thrones\&quot;. Otherwise, it&#39;s fuzzy search.  | |
| **sortByDate** | **Integer**| Sort by date or not? If 0, then sort by relevance. If 1, then sort by date.  | [optional] [default to 0] [enum: 0, 1] |
| **type** | **String**| What type of contents do you want to search for?   | [optional] [default to episode] [enum: episode, podcast, curated] |
| **offset** | **Integer**| Offset for search results, for pagination. You&#39;ll use **next_offset** from response for this parameter.  | [optional] [default to 0] |
| **lenMin** | **Integer**| Minimum audio length in minutes. Applicable only when **type** parameter is **episode** or **podcast**. If **type** parameter is **episode**, it&#39;s for audio length of an episode. If **type** parameter is **podcast**, it&#39;s for average audio length of all episodes in a podcast.  | [optional] [default to 0] |
| **lenMax** | **Integer**| Maximum audio length in minutes. Applicable only when **type** parameter is **episode** or **podcast**. If **type** parameter is **episode**, it&#39;s for audio length of an episode. If **type** parameter is **podcast**, it&#39;s for average audio length of all episodes in a podcast.  | [optional] |
| **episodeCountMin** | **Integer**| Minimum number of episodes. Applicable only when type parameter is **podcast**.  | [optional] |
| **episodeCountMax** | **Integer**| Maximum number of episodes. Applicable only when type parameter is **podcast**.  | [optional] |
| **updateFreqMin** | **Integer**| Minimum update frequency in hours (how frequently does a podcast release a new episode). For example, if you want to find \&quot;weekly\&quot; podcasts, then you can set **update_freq_min**&#x3D;144 hours (or 6 days) and **update_freq_max**&#x3D;192 hours (or 8 days). Applicable only when type parameter is **podcast**.  | [optional] |
| **updateFreqMax** | **Integer**| Maximum update frequency in hours (how frequently does a podcast release a new episode). For example, if you want to find \&quot;weekly\&quot; podcasts, then you can set **update_freq_min**&#x3D;144 hours (or 6 days) and **update_freq_max**&#x3D;192 hours (or 8 days). Applicable only when type parameter is **podcast**.  | [optional] |
| **genreIds** | **String**| A comma-delimited string of a list of genre ids. If not specified, then all genres are included. You can find the id and the name of all genres from &#x60;GET /genres&#x60;. It works only when **type** is *episode* or *podcast*.  | [optional] |
| **publishedBefore** | **Integer**| Only show episodes/podcasts/curated lists published before this timestamp (in milliseconds). If **published_before** &amp; **published_after** are used at the same time, **published_before** should be bigger than **published_after**.  | [optional] |
| **publishedAfter** | **Integer**| Only show episodes/podcasts/curated lists published after this timestamp (in milliseconds). If **published_before** &amp; **published_after** are used at the same time, **published_before** should be bigger than **published_after**.  | [optional] [default to 0] |
| **onlyIn** | **String**| A comma-delimited string to search only in specific fields. Allowed values are title, description, author, and audio. If not specified, then search every fields.  | [optional] [default to title,description,author,audio] |
| **language** | **String**| Limit search results to a specific language. If not specified, it&#39;ll be any language. You can get a list of supported languages from &#x60;GET /languages&#x60;. It works only when **type** is *episode* or *podcast*.  | [optional] |
| **region** | **String**| Limit search results to a specific region (e.g., us, gb, in...). If not specified, it&#39;ll be any region. You can get the supported country codes from &#x60;GET /regions&#x60;. It works only when **type** is *episode* or *podcast*.  | [optional] |
| **ocid** | **String**| A comma-delimited string of podcast ids (up to 5 podcasts) - you can get a podcast id from the **podcast_id** field in response. This parameter is to limit search results from only a few specific podcasts. It works only when **type** is *episode*.  | [optional] |
| **ncid** | **String**| A comma-delimited string of podcast ids (up to 5 podcasts) - you can get a podcast id from the **podcast_id** field in response. This parameter is to exclude search results of a few specific podcasts. It works only when **type** is *episode*.  | [optional] |
| **safeMode** | **Integer**| Whether or not to exclude podcasts/episodes with explicit language. 1 is yes and 0 is no. It works only when **type** is *episode* or *podcast*.  | [optional] [default to 0] [enum: 0, 1] |
| **uniquePodcasts** | **Integer**| Whether or not to keep only one episode per podcast in search results. 1 is yes and 0 is no. It works only when **type** is *episode*.  | [optional] [default to 0] [enum: 0, 1] |
| **pageSize** | **Integer**| The maximum number of search results per page. A valid value should be an integer between 1 and 10 (inclusive).  | [optional] [default to 10] |

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **400** |  |  -  |
| **401** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

<a id="spellcheck"></a>
# **spellcheck**
> SpellCheckResponse spellcheck(xListenAPIKey, q)

Spell check on a search term

Suggest a list of words that correct the spelling errors of a search term. This endpoint is available only in the PRO/ENTERPRISE plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    SearchApiApi apiInstance = new SearchApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    String q = "q_example"; // String | Search term, e.g., person, place, topic... 
    try {
      SpellCheckResponse result = apiInstance.spellcheck(xListenAPIKey, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApiApi#spellcheck");
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
| **q** | **String**| Search term, e.g., person, place, topic...  | |

### Return type

[**SpellCheckResponse**](SpellCheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **400** |  |  -  |
| **401** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

<a id="typeahead"></a>
# **typeahead**
> TypeaheadResponse typeahead(xListenAPIKey, q, showPodcasts, showGenres, safeMode)

Typeahead search

Suggest search terms, podcast genres, and podcasts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://listen-api.listennotes.com/api/v2");

    SearchApiApi apiInstance = new SearchApiApi(defaultClient);
    String xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
    String q = "q_example"; // String | Search term, e.g., person, place, topic... You can use double quotes to do verbatim match, e.g., \"game of thrones\". Otherwise, it's fuzzy search. 
    Integer showPodcasts = 0; // Integer | Autosuggest podcasts. This only searches podcast title and publisher and returns very limited info of 5 podcasts. 1 is yes, 0 is no. It's a bit slow to autosuggest podcasts, so we turn it off by default. If show_podcasts=1, you can also pass iTunes id (e.g., 474722933) to the q parameter to fetch podcast meta data. 
    Integer showGenres = 0; // Integer | Whether or not to autosuggest genres. 1 is yes, 0 is no. 
    Integer safeMode = 0; // Integer | Whether or not to exclude podcasts/episodes with explicit language. 1 is yes and 0 is no. It works only when **show_podcasts** is *1*. 
    try {
      TypeaheadResponse result = apiInstance.typeahead(xListenAPIKey, q, showPodcasts, showGenres, safeMode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApiApi#typeahead");
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
| **q** | **String**| Search term, e.g., person, place, topic... You can use double quotes to do verbatim match, e.g., \&quot;game of thrones\&quot;. Otherwise, it&#39;s fuzzy search.  | |
| **showPodcasts** | **Integer**| Autosuggest podcasts. This only searches podcast title and publisher and returns very limited info of 5 podcasts. 1 is yes, 0 is no. It&#39;s a bit slow to autosuggest podcasts, so we turn it off by default. If show_podcasts&#x3D;1, you can also pass iTunes id (e.g., 474722933) to the q parameter to fetch podcast meta data.  | [optional] [default to 0] [enum: 0, 1] |
| **showGenres** | **Integer**| Whether or not to autosuggest genres. 1 is yes, 0 is no.  | [optional] [default to 0] [enum: 0, 1] |
| **safeMode** | **Integer**| Whether or not to exclude podcasts/episodes with explicit language. 1 is yes and 0 is no. It works only when **show_podcasts** is *1*.  | [optional] [default to 0] [enum: 0, 1] |

### Return type

[**TypeaheadResponse**](TypeaheadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * X-ListenAPI-FreeQuota -  <br>  * X-ListenAPI-NextBillingDate -  <br>  * X-ListenAPI-Usage -  <br>  * X-listenAPI-Latency-Seconds -  <br>  |
| **400** |  |  -  |
| **401** |  |  -  |
| **429** |  |  -  |
| **5XX** |  |  -  |

