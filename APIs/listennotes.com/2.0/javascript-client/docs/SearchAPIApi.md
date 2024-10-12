# ListenApiPodcastSearchDirectoryAndInsightsApi.SearchAPIApi

All URIs are relative to *https://listen-api.listennotes.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRelatedSearches**](SearchAPIApi.md#getRelatedSearches) | **GET** /related_searches | Fetch related search terms
[**getTrendingSearches**](SearchAPIApi.md#getTrendingSearches) | **GET** /trending_searches | Fetch trending search terms
[**search**](SearchAPIApi.md#search) | **GET** /search | Full-text search
[**spellcheck**](SearchAPIApi.md#spellcheck) | **GET** /spellcheck | Spell check on a search term
[**typeahead**](SearchAPIApi.md#typeahead) | **GET** /typeahead | Typeahead search



## getRelatedSearches

> RelatedSearchesResponse getRelatedSearches(xListenAPIKey, q)

Fetch related search terms

Suggest related search terms. The results are more comprehensive than from &#x60;GET /typeahead&#x60;. This endpoint is available only in the PRO/ENTERPRISE plan.

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.SearchAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
let q = "q_example"; // String | Search term, e.g., person, place, topic... 
apiInstance.getRelatedSearches(xListenAPIKey, q, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | 
 **q** | **String**| Search term, e.g., person, place, topic...  | 

### Return type

[**RelatedSearchesResponse**](RelatedSearchesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrendingSearches

> TrendingSearchesResponse getTrendingSearches(xListenAPIKey)

Fetch trending search terms

Fetch up to 10 most recent trending search terms on the Listen Notes platform.

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.SearchAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
apiInstance.getTrendingSearches(xListenAPIKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | 

### Return type

[**TrendingSearchesResponse**](TrendingSearchesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## search

> SearchResponse search(xListenAPIKey, q, opts)

Full-text search

Full-text search on episodes, podcasts, or curated lists of podcasts. Use the &#x60;offset&#x60; parameter to paginate through search results. The FREE plan allows to see up to 30 search results (or &#x60;offset&#x60; &lt; 30) per query. The PRO plan allows to see up to 300 search results (or &#x60;offset&#x60; &lt; 300) per query. The ENTERPRISE plan allows to see up to 10,000 search results (or &#x60;offset&#x60; &lt; 10000) per query. 

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.SearchAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
let q = "q_example"; // String | Search term, e.g., person, place, topic... You can use double quotes to do verbatim match, e.g., \"game of thrones\". Otherwise, it's fuzzy search. 
let opts = {
  'sortByDate': 0, // Number | Sort by date or not? If 0, then sort by relevance. If 1, then sort by date. 
  'type': "'episode'", // String | What type of contents do you want to search for?  
  'offset': 0, // Number | Offset for search results, for pagination. You'll use **next_offset** from response for this parameter. 
  'lenMin': 0, // Number | Minimum audio length in minutes. Applicable only when **type** parameter is **episode** or **podcast**. If **type** parameter is **episode**, it's for audio length of an episode. If **type** parameter is **podcast**, it's for average audio length of all episodes in a podcast. 
  'lenMax': 56, // Number | Maximum audio length in minutes. Applicable only when **type** parameter is **episode** or **podcast**. If **type** parameter is **episode**, it's for audio length of an episode. If **type** parameter is **podcast**, it's for average audio length of all episodes in a podcast. 
  'episodeCountMin': 56, // Number | Minimum number of episodes. Applicable only when type parameter is **podcast**. 
  'episodeCountMax': 56, // Number | Maximum number of episodes. Applicable only when type parameter is **podcast**. 
  'updateFreqMin': 56, // Number | Minimum update frequency in hours (how frequently does a podcast release a new episode). For example, if you want to find \"weekly\" podcasts, then you can set **update_freq_min**=144 hours (or 6 days) and **update_freq_max**=192 hours (or 8 days). Applicable only when type parameter is **podcast**. 
  'updateFreqMax': 56, // Number | Maximum update frequency in hours (how frequently does a podcast release a new episode). For example, if you want to find \"weekly\" podcasts, then you can set **update_freq_min**=144 hours (or 6 days) and **update_freq_max**=192 hours (or 8 days). Applicable only when type parameter is **podcast**. 
  'genreIds': "genreIds_example", // String | A comma-delimited string of a list of genre ids. If not specified, then all genres are included. You can find the id and the name of all genres from `GET /genres`. It works only when **type** is *episode* or *podcast*. 
  'publishedBefore': 56, // Number | Only show episodes/podcasts/curated lists published before this timestamp (in milliseconds). If **published_before** & **published_after** are used at the same time, **published_before** should be bigger than **published_after**. 
  'publishedAfter': 0, // Number | Only show episodes/podcasts/curated lists published after this timestamp (in milliseconds). If **published_before** & **published_after** are used at the same time, **published_before** should be bigger than **published_after**. 
  'onlyIn': "'title,description,author,audio'", // String | A comma-delimited string to search only in specific fields. Allowed values are title, description, author, and audio. If not specified, then search every fields. 
  'language': "language_example", // String | Limit search results to a specific language. If not specified, it'll be any language. You can get a list of supported languages from `GET /languages`. It works only when **type** is *episode* or *podcast*. 
  'region': "region_example", // String | Limit search results to a specific region (e.g., us, gb, in...). If not specified, it'll be any region. You can get the supported country codes from `GET /regions`. It works only when **type** is *episode* or *podcast*. 
  'ocid': "ocid_example", // String | A comma-delimited string of podcast ids (up to 5 podcasts) - you can get a podcast id from the **podcast_id** field in response. This parameter is to limit search results from only a few specific podcasts. It works only when **type** is *episode*. 
  'ncid': "ncid_example", // String | A comma-delimited string of podcast ids (up to 5 podcasts) - you can get a podcast id from the **podcast_id** field in response. This parameter is to exclude search results of a few specific podcasts. It works only when **type** is *episode*. 
  'safeMode': 0, // Number | Whether or not to exclude podcasts/episodes with explicit language. 1 is yes and 0 is no. It works only when **type** is *episode* or *podcast*. 
  'uniquePodcasts': 0, // Number | Whether or not to keep only one episode per podcast in search results. 1 is yes and 0 is no. It works only when **type** is *episode*. 
  'pageSize': 10 // Number | The maximum number of search results per page. A valid value should be an integer between 1 and 10 (inclusive). 
};
apiInstance.search(xListenAPIKey, q, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | 
 **q** | **String**| Search term, e.g., person, place, topic... You can use double quotes to do verbatim match, e.g., \&quot;game of thrones\&quot;. Otherwise, it&#39;s fuzzy search.  | 
 **sortByDate** | **Number**| Sort by date or not? If 0, then sort by relevance. If 1, then sort by date.  | [optional] [default to 0]
 **type** | **String**| What type of contents do you want to search for?   | [optional] [default to &#39;episode&#39;]
 **offset** | **Number**| Offset for search results, for pagination. You&#39;ll use **next_offset** from response for this parameter.  | [optional] [default to 0]
 **lenMin** | **Number**| Minimum audio length in minutes. Applicable only when **type** parameter is **episode** or **podcast**. If **type** parameter is **episode**, it&#39;s for audio length of an episode. If **type** parameter is **podcast**, it&#39;s for average audio length of all episodes in a podcast.  | [optional] [default to 0]
 **lenMax** | **Number**| Maximum audio length in minutes. Applicable only when **type** parameter is **episode** or **podcast**. If **type** parameter is **episode**, it&#39;s for audio length of an episode. If **type** parameter is **podcast**, it&#39;s for average audio length of all episodes in a podcast.  | [optional] 
 **episodeCountMin** | **Number**| Minimum number of episodes. Applicable only when type parameter is **podcast**.  | [optional] 
 **episodeCountMax** | **Number**| Maximum number of episodes. Applicable only when type parameter is **podcast**.  | [optional] 
 **updateFreqMin** | **Number**| Minimum update frequency in hours (how frequently does a podcast release a new episode). For example, if you want to find \&quot;weekly\&quot; podcasts, then you can set **update_freq_min**&#x3D;144 hours (or 6 days) and **update_freq_max**&#x3D;192 hours (or 8 days). Applicable only when type parameter is **podcast**.  | [optional] 
 **updateFreqMax** | **Number**| Maximum update frequency in hours (how frequently does a podcast release a new episode). For example, if you want to find \&quot;weekly\&quot; podcasts, then you can set **update_freq_min**&#x3D;144 hours (or 6 days) and **update_freq_max**&#x3D;192 hours (or 8 days). Applicable only when type parameter is **podcast**.  | [optional] 
 **genreIds** | **String**| A comma-delimited string of a list of genre ids. If not specified, then all genres are included. You can find the id and the name of all genres from &#x60;GET /genres&#x60;. It works only when **type** is *episode* or *podcast*.  | [optional] 
 **publishedBefore** | **Number**| Only show episodes/podcasts/curated lists published before this timestamp (in milliseconds). If **published_before** &amp; **published_after** are used at the same time, **published_before** should be bigger than **published_after**.  | [optional] 
 **publishedAfter** | **Number**| Only show episodes/podcasts/curated lists published after this timestamp (in milliseconds). If **published_before** &amp; **published_after** are used at the same time, **published_before** should be bigger than **published_after**.  | [optional] [default to 0]
 **onlyIn** | **String**| A comma-delimited string to search only in specific fields. Allowed values are title, description, author, and audio. If not specified, then search every fields.  | [optional] [default to &#39;title,description,author,audio&#39;]
 **language** | **String**| Limit search results to a specific language. If not specified, it&#39;ll be any language. You can get a list of supported languages from &#x60;GET /languages&#x60;. It works only when **type** is *episode* or *podcast*.  | [optional] 
 **region** | **String**| Limit search results to a specific region (e.g., us, gb, in...). If not specified, it&#39;ll be any region. You can get the supported country codes from &#x60;GET /regions&#x60;. It works only when **type** is *episode* or *podcast*.  | [optional] 
 **ocid** | **String**| A comma-delimited string of podcast ids (up to 5 podcasts) - you can get a podcast id from the **podcast_id** field in response. This parameter is to limit search results from only a few specific podcasts. It works only when **type** is *episode*.  | [optional] 
 **ncid** | **String**| A comma-delimited string of podcast ids (up to 5 podcasts) - you can get a podcast id from the **podcast_id** field in response. This parameter is to exclude search results of a few specific podcasts. It works only when **type** is *episode*.  | [optional] 
 **safeMode** | **Number**| Whether or not to exclude podcasts/episodes with explicit language. 1 is yes and 0 is no. It works only when **type** is *episode* or *podcast*.  | [optional] [default to 0]
 **uniquePodcasts** | **Number**| Whether or not to keep only one episode per podcast in search results. 1 is yes and 0 is no. It works only when **type** is *episode*.  | [optional] [default to 0]
 **pageSize** | **Number**| The maximum number of search results per page. A valid value should be an integer between 1 and 10 (inclusive).  | [optional] [default to 10]

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## spellcheck

> SpellCheckResponse spellcheck(xListenAPIKey, q)

Spell check on a search term

Suggest a list of words that correct the spelling errors of a search term. This endpoint is available only in the PRO/ENTERPRISE plan.

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.SearchAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
let q = "q_example"; // String | Search term, e.g., person, place, topic... 
apiInstance.spellcheck(xListenAPIKey, q, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | 
 **q** | **String**| Search term, e.g., person, place, topic...  | 

### Return type

[**SpellCheckResponse**](SpellCheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## typeahead

> TypeaheadResponse typeahead(xListenAPIKey, q, opts)

Typeahead search

Suggest search terms, podcast genres, and podcasts.

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.SearchAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
let q = "q_example"; // String | Search term, e.g., person, place, topic... You can use double quotes to do verbatim match, e.g., \"game of thrones\". Otherwise, it's fuzzy search. 
let opts = {
  'showPodcasts': 0, // Number | Autosuggest podcasts. This only searches podcast title and publisher and returns very limited info of 5 podcasts. 1 is yes, 0 is no. It's a bit slow to autosuggest podcasts, so we turn it off by default. If show_podcasts=1, you can also pass iTunes id (e.g., 474722933) to the q parameter to fetch podcast meta data. 
  'showGenres': 0, // Number | Whether or not to autosuggest genres. 1 is yes, 0 is no. 
  'safeMode': 0 // Number | Whether or not to exclude podcasts/episodes with explicit language. 1 is yes and 0 is no. It works only when **show_podcasts** is *1*. 
};
apiInstance.typeahead(xListenAPIKey, q, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xListenAPIKey** | **String**| Get API Key on listennotes.com/api | 
 **q** | **String**| Search term, e.g., person, place, topic... You can use double quotes to do verbatim match, e.g., \&quot;game of thrones\&quot;. Otherwise, it&#39;s fuzzy search.  | 
 **showPodcasts** | **Number**| Autosuggest podcasts. This only searches podcast title and publisher and returns very limited info of 5 podcasts. 1 is yes, 0 is no. It&#39;s a bit slow to autosuggest podcasts, so we turn it off by default. If show_podcasts&#x3D;1, you can also pass iTunes id (e.g., 474722933) to the q parameter to fetch podcast meta data.  | [optional] [default to 0]
 **showGenres** | **Number**| Whether or not to autosuggest genres. 1 is yes, 0 is no.  | [optional] [default to 0]
 **safeMode** | **Number**| Whether or not to exclude podcasts/episodes with explicit language. 1 is yes and 0 is no. It works only when **show_podcasts** is *1*.  | [optional] [default to 0]

### Return type

[**TypeaheadResponse**](TypeaheadResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

