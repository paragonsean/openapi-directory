# ListenApiPodcastSearchDirectoryAndInsightsApi.DirectoryAPIApi

All URIs are relative to *https://listen-api.listennotes.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBestPodcasts**](DirectoryAPIApi.md#getBestPodcasts) | **GET** /best_podcasts | Fetch a list of best podcasts by genre
[**getCuratedPodcastById**](DirectoryAPIApi.md#getCuratedPodcastById) | **GET** /curated_podcasts/{id} | Fetch a curated list of podcasts by id
[**getCuratedPodcasts**](DirectoryAPIApi.md#getCuratedPodcasts) | **GET** /curated_podcasts | Fetch curated lists of podcasts
[**getEpisodeById**](DirectoryAPIApi.md#getEpisodeById) | **GET** /episodes/{id} | Fetch detailed meta data for an episode by id
[**getEpisodeRecommendations**](DirectoryAPIApi.md#getEpisodeRecommendations) | **GET** /episodes/{id}/recommendations | Fetch recommendations for an episode
[**getEpisodesInBatch**](DirectoryAPIApi.md#getEpisodesInBatch) | **POST** /episodes | Batch fetch basic meta data for episodes
[**getGenres**](DirectoryAPIApi.md#getGenres) | **GET** /genres | Fetch a list of podcast genres
[**getLanguages**](DirectoryAPIApi.md#getLanguages) | **GET** /languages | Fetch a list of supported languages for podcasts
[**getPodcastById**](DirectoryAPIApi.md#getPodcastById) | **GET** /podcasts/{id} | Fetch detailed meta data and episodes for a podcast by id
[**getPodcastRecommendations**](DirectoryAPIApi.md#getPodcastRecommendations) | **GET** /podcasts/{id}/recommendations | Fetch recommendations for a podcast
[**getPodcastsInBatch**](DirectoryAPIApi.md#getPodcastsInBatch) | **POST** /podcasts | Batch fetch basic meta data for podcasts
[**getRegions**](DirectoryAPIApi.md#getRegions) | **GET** /regions | Fetch a list of supported countries/regions for best podcasts
[**justListen**](DirectoryAPIApi.md#justListen) | **GET** /just_listen | Fetch a random podcast episode



## getBestPodcasts

> BestPodcastsResponse getBestPodcasts(xListenAPIKey, opts)

Fetch a list of best podcasts by genre

Get a list of curated best podcasts by genre, which are curated by Listen Notes staffs based on various signals from the Internet, e.g., top charts on other podcast platforms, recommendations from mainstream media, user activities on listennotes.com... You can get the genre ids from &#x60;GET /genres&#x60; endpoint. This endpoint returns same data as https://www.listennotes.com/best-podcasts/ 

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.DirectoryAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
let opts = {
  'genreId': "genreId_example", // String | You can get the id from `GET /genres`. If not specified, it'll be the overall best podcasts, which can be considered as a special genre.
  'page': 56, // Number | Page number of those podcasts in this genre.
  'region': "'us'", // String | Filter best podcasts by country/region. Please note that podcasts that are \"best\" in a country/region may not be produced in that country/region. For example, a podcast from the US may be very popular in Canada. You can get the supported country codes (e.g., us, jp, gb...) from `GET /regions`. If not specified, you'll get \"best podcasts\" in United States. 
  'publisherRegion': "publisherRegion_example", // String | Filter best podcasts by the publisher's country/region. This is to narrow down the results to include \"best podcasts\" produced in a specific country/region. You can get the supported country codes (e.g., us, jp, gb...) from `GET /regions`. If not specified, you'll get \"best podcasts\" produced in any country/region. If you want to get a country/region's \"best podcasts\" that are also produced in that country/region, then you need to specify both **region** and **publisher_region**, e.g., `region=jp` and `publisher_region=jp`. 
  'language': "language_example", // String | Filter best podcasts by language. You can get a list of supported languages (e.g., English, Chinese, Japanese...) from `GET /languages`. If not specified, you'll get \"best podcasts\" in any language. 
  'sort': "listen_score", // String | How do you want to sort these podcasts? If you'd like to sort by popularity, please use **listen_score**. 
  'safeMode': 0 // Number | Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no.
};
apiInstance.getBestPodcasts(xListenAPIKey, opts, (error, data, response) => {
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
 **genreId** | **String**| You can get the id from &#x60;GET /genres&#x60;. If not specified, it&#39;ll be the overall best podcasts, which can be considered as a special genre. | [optional] 
 **page** | **Number**| Page number of those podcasts in this genre. | [optional] 
 **region** | **String**| Filter best podcasts by country/region. Please note that podcasts that are \&quot;best\&quot; in a country/region may not be produced in that country/region. For example, a podcast from the US may be very popular in Canada. You can get the supported country codes (e.g., us, jp, gb...) from &#x60;GET /regions&#x60;. If not specified, you&#39;ll get \&quot;best podcasts\&quot; in United States.  | [optional] [default to &#39;us&#39;]
 **publisherRegion** | **String**| Filter best podcasts by the publisher&#39;s country/region. This is to narrow down the results to include \&quot;best podcasts\&quot; produced in a specific country/region. You can get the supported country codes (e.g., us, jp, gb...) from &#x60;GET /regions&#x60;. If not specified, you&#39;ll get \&quot;best podcasts\&quot; produced in any country/region. If you want to get a country/region&#39;s \&quot;best podcasts\&quot; that are also produced in that country/region, then you need to specify both **region** and **publisher_region**, e.g., &#x60;region&#x3D;jp&#x60; and &#x60;publisher_region&#x3D;jp&#x60;.  | [optional] 
 **language** | **String**| Filter best podcasts by language. You can get a list of supported languages (e.g., English, Chinese, Japanese...) from &#x60;GET /languages&#x60;. If not specified, you&#39;ll get \&quot;best podcasts\&quot; in any language.  | [optional] 
 **sort** | **String**| How do you want to sort these podcasts? If you&#39;d like to sort by popularity, please use **listen_score**.  | [optional] [default to &#39;recent_added_first&#39;]
 **safeMode** | **Number**| Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no. | [optional] [default to 0]

### Return type

[**BestPodcastsResponse**](BestPodcastsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCuratedPodcastById

> CuratedListFull getCuratedPodcastById(xListenAPIKey, id)

Fetch a curated list of podcasts by id

Get detailed meta data of all podcasts in a specific curated list. This endpoint returns same data as https://www.listennotes.com/curated-podcasts/ 

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.DirectoryAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
let id = "id_example"; // String | id for a specific curated list of podcasts. You can get the id from the response of `GET /search?type=curated` or `GET /curated_podcasts`. 
apiInstance.getCuratedPodcastById(xListenAPIKey, id, (error, data, response) => {
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
 **id** | **String**| id for a specific curated list of podcasts. You can get the id from the response of &#x60;GET /search?type&#x3D;curated&#x60; or &#x60;GET /curated_podcasts&#x60;.  | 

### Return type

[**CuratedListFull**](CuratedListFull.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCuratedPodcasts

> GetCuratedPodcastsResponse getCuratedPodcasts(xListenAPIKey, opts)

Fetch curated lists of podcasts

A bunch of curated lists from online media. For each list, you&#39;ll get basic info of up to 5 podcasts. To get detailed meta data of all podcasts in a specific list, you need to use &#x60;GET /curated_podcasts/{id}&#x60;. We add new curated lists to the database on a daily basis. 

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.DirectoryAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
let opts = {
  'page': 2 // Number | Page number of curated lists.
};
apiInstance.getCuratedPodcasts(xListenAPIKey, opts, (error, data, response) => {
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
 **page** | **Number**| Page number of curated lists. | [optional] [default to 1]

### Return type

[**GetCuratedPodcastsResponse**](GetCuratedPodcastsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEpisodeById

> EpisodeFull getEpisodeById(xListenAPIKey, id, opts)

Fetch detailed meta data for an episode by id

Fetch detailed meta data for a specific episode.

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.DirectoryAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
let id = "id_example"; // String | id for a specific episode. You can get episode id from using other endpoints, e.g., `GET /search`...
let opts = {
  'showTranscript': 0 // Number | To include the transcript of this episode or not? If it is 1, then include the transcript in the **transcript** field. The default value is 0 - we don't include transcript by default, because 1) it would make the response data very big, thus slow response time; 2) less than 1% of episodes have transcripts. The transcript field is available only in the PRO/ENTERPRISE plan.
};
apiInstance.getEpisodeById(xListenAPIKey, id, opts, (error, data, response) => {
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
 **id** | **String**| id for a specific episode. You can get episode id from using other endpoints, e.g., &#x60;GET /search&#x60;... | 
 **showTranscript** | **Number**| To include the transcript of this episode or not? If it is 1, then include the transcript in the **transcript** field. The default value is 0 - we don&#39;t include transcript by default, because 1) it would make the response data very big, thus slow response time; 2) less than 1% of episodes have transcripts. The transcript field is available only in the PRO/ENTERPRISE plan. | [optional] [default to 0]

### Return type

[**EpisodeFull**](EpisodeFull.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEpisodeRecommendations

> GetEpisodeRecommendationsResponse getEpisodeRecommendations(xListenAPIKey, id, opts)

Fetch recommendations for an episode

Fetch up to 8 episode recommendations based on the given episode id.

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.DirectoryAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
let id = "254444fa6cf64a43a95292a70eb6869b"; // String | Episode id.
let opts = {
  'safeMode': 0 // Number | Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no.
};
apiInstance.getEpisodeRecommendations(xListenAPIKey, id, opts, (error, data, response) => {
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
 **id** | **String**| Episode id. | 
 **safeMode** | **Number**| Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no. | [optional] [default to 0]

### Return type

[**GetEpisodeRecommendationsResponse**](GetEpisodeRecommendationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEpisodesInBatch

> GetEpisodesInBatchResponse getEpisodesInBatch(xListenAPIKey, ids)

Batch fetch basic meta data for episodes

Batch fetch basic meta data for up to 10 episodes. This endpoint could be used to implement custom playlists for individual episodes. For detailed meta data of an individual episode, you need to use &#x60;GET /episodes/{id}&#x60;. This endpoint is available only in the PRO/ENTERPRISE plan. 

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.DirectoryAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
let ids = "ids_example"; // String | Comma-separated list of episode ids.
apiInstance.getEpisodesInBatch(xListenAPIKey, ids, (error, data, response) => {
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
 **ids** | **String**| Comma-separated list of episode ids. | 

### Return type

[**GetEpisodesInBatchResponse**](GetEpisodesInBatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## getGenres

> GetGenresResponse getGenres(xListenAPIKey, opts)

Fetch a list of podcast genres

Get a list of podcast genres that are supported in Listen Notes. The genre id can be passed to other endpoints as a parameter to get podcasts in a specific genre, e.g., &#x60;GET /best_podcasts&#x60;, &#x60;GET /search&#x60;... You may want to cache the list of genres on the client side. 

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.DirectoryAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
let opts = {
  'topLevelOnly': 0 // Number | Just show top level genres? If 1, yes, just show top level genres. If 0, no, show all genres. 
};
apiInstance.getGenres(xListenAPIKey, opts, (error, data, response) => {
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
 **topLevelOnly** | **Number**| Just show top level genres? If 1, yes, just show top level genres. If 0, no, show all genres.  | [optional] [default to 0]

### Return type

[**GetGenresResponse**](GetGenresResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLanguages

> GetLanguagesResponse getLanguages(xListenAPIKey)

Fetch a list of supported languages for podcasts

Get a list of languages that are supported in Listen Notes database. You can use the language string as query parameter in &#x60;GET /search&#x60;. 

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.DirectoryAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
apiInstance.getLanguages(xListenAPIKey, (error, data, response) => {
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

[**GetLanguagesResponse**](GetLanguagesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPodcastById

> PodcastFull getPodcastById(xListenAPIKey, id, opts)

Fetch detailed meta data and episodes for a podcast by id

Fetch detailed meta data and episodes for a specific podcast (up to 10 episodes each time). You can use the **next_episode_pub_date** parameter to do pagination and fetch more episodes. 

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.DirectoryAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
let id = "4d3fe717742d4963a85562e9f84d8c79"; // String | Podcast id. You can get podcast id from using other endpoints, e.g., `GET /search`, `GET /best_podcasts`...
let opts = {
  'nextEpisodePubDate': 1479154463000, // Number | For episodes pagination. It's the value of **next_episode_pub_date** from the response of last request. If not specified, just return latest 10 episodes or oldest 10 episodes, depending on the value of the **sort** parameter. 
  'sort': "recent_first" // String | How do you want to sort the episodes of this podcast? 
};
apiInstance.getPodcastById(xListenAPIKey, id, opts, (error, data, response) => {
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
 **id** | **String**| Podcast id. You can get podcast id from using other endpoints, e.g., &#x60;GET /search&#x60;, &#x60;GET /best_podcasts&#x60;... | 
 **nextEpisodePubDate** | **Number**| For episodes pagination. It&#39;s the value of **next_episode_pub_date** from the response of last request. If not specified, just return latest 10 episodes or oldest 10 episodes, depending on the value of the **sort** parameter.  | [optional] 
 **sort** | **String**| How do you want to sort the episodes of this podcast?  | [optional] [default to &#39;recent_first&#39;]

### Return type

[**PodcastFull**](PodcastFull.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPodcastRecommendations

> GetPodcastRecommendationsResponse getPodcastRecommendations(xListenAPIKey, id, opts)

Fetch recommendations for a podcast

Fetch up to 8 podcast recommendations based on the given podcast id.

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.DirectoryAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
let id = "25212ac3c53240a880dd5032e547047b"; // String | Podcast id.
let opts = {
  'safeMode': 0 // Number | Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no.
};
apiInstance.getPodcastRecommendations(xListenAPIKey, id, opts, (error, data, response) => {
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
 **id** | **String**| Podcast id. | 
 **safeMode** | **Number**| Whether or not to exclude podcasts with explicit language. 1 is yes, and 0 is no. | [optional] [default to 0]

### Return type

[**GetPodcastRecommendationsResponse**](GetPodcastRecommendationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPodcastsInBatch

> GetPodcastsInBatchResponse getPodcastsInBatch(xListenAPIKey, opts)

Batch fetch basic meta data for podcasts

Batch fetch basic meta data for up to 10 podcasts. This endpoint could be used to build something like OPML import, allowing users to import a bunch of podcasts via rss urls. For detailed meta data (including episodes) of an individual podcast, you need to use &#x60;GET /podcasts/{id}&#x60;. This endpoint is available only in the PRO/ENTERPRISE plan. 

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.DirectoryAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
let opts = {
  'ids': "ids_example", // String | Comma-separated list of podcast ids.
  'itunesIds': "itunesIds_example", // String | Comma-separated Apple Podcasts (iTunes) ids, e.g., 659155419
  'nextEpisodePubDate': 56, // Number | For latest episodes pagination. It's the value of **next_episode_pub_date** from the response of last request. If not specified, just return latest 15 episodes. 
  'rsses': "rsses_example", // String | Comma-separated rss urls.
  'showLatestEpisodes': 0, // Number | Whether or not to fetch up to 15 latest episodes from these podcasts, sorted by pub_date. 1 is yes, and 0 is no. 
  'spotifyIds': "spotifyIds_example" // String | Comma-separated Spotify ids, e.g., 3DDfEsKDIDrTlnPOiG4ZF4
};
apiInstance.getPodcastsInBatch(xListenAPIKey, opts, (error, data, response) => {
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
 **ids** | **String**| Comma-separated list of podcast ids. | [optional] 
 **itunesIds** | **String**| Comma-separated Apple Podcasts (iTunes) ids, e.g., 659155419 | [optional] 
 **nextEpisodePubDate** | **Number**| For latest episodes pagination. It&#39;s the value of **next_episode_pub_date** from the response of last request. If not specified, just return latest 15 episodes.  | [optional] 
 **rsses** | **String**| Comma-separated rss urls. | [optional] 
 **showLatestEpisodes** | **Number**| Whether or not to fetch up to 15 latest episodes from these podcasts, sorted by pub_date. 1 is yes, and 0 is no.  | [optional] [default to 0]
 **spotifyIds** | **String**| Comma-separated Spotify ids, e.g., 3DDfEsKDIDrTlnPOiG4ZF4 | [optional] 

### Return type

[**GetPodcastsInBatchResponse**](GetPodcastsInBatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## getRegions

> GetRegionsResponse getRegions(xListenAPIKey)

Fetch a list of supported countries/regions for best podcasts

It returns a dictionary of country codes (e.g., us, gb...) &amp; country names (United States, United Kingdom...). The country code is used in the query parameter **region** of &#x60;GET /best_podcasts&#x60;. 

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.DirectoryAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
apiInstance.getRegions(xListenAPIKey, (error, data, response) => {
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

[**GetRegionsResponse**](GetRegionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## justListen

> EpisodeSimple justListen(xListenAPIKey)

Fetch a random podcast episode

Recently published episodes are more likely to be fetched. Good luck!

### Example

```javascript
import ListenApiPodcastSearchDirectoryAndInsightsApi from 'listen_api_podcast_search_directory_and_insights_api';

let apiInstance = new ListenApiPodcastSearchDirectoryAndInsightsApi.DirectoryAPIApi();
let xListenAPIKey = "xListenAPIKey_example"; // String | Get API Key on listennotes.com/api
apiInstance.justListen(xListenAPIKey, (error, data, response) => {
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

[**EpisodeSimple**](EpisodeSimple.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

