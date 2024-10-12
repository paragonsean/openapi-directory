# TraktApi.EpisodesApi

All URIs are relative to *https://api.trakt.tv*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getASingleEpisodeForAShow**](EpisodesApi.md#getASingleEpisodeForAShow) | **GET** /shows/{id}/seasons/{season}/episodes/{episode} | Get a single episode for a show
[**getAllEpisodeComments**](EpisodesApi.md#getAllEpisodeComments) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/comments/{sort} | Get all episode comments
[**getAllEpisodeTranslations**](EpisodesApi.md#getAllEpisodeTranslations) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/translations/{language} | Get all episode translations
[**getAllPeopleForAnEpisode**](EpisodesApi.md#getAllPeopleForAnEpisode) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/people | Get all people for an episode
[**getEpisodeRatings**](EpisodesApi.md#getEpisodeRatings) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/ratings | Get episode ratings
[**getEpisodeStats**](EpisodesApi.md#getEpisodeStats) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/stats | Get episode stats
[**getListsContainingThisEpisode**](EpisodesApi.md#getListsContainingThisEpisode) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/lists/{type}/{sort} | Get lists containing this episode
[**showsIdSeasonsSeasonEpisodesEpisodeWatchingGet**](EpisodesApi.md#showsIdSeasonsSeasonEpisodesEpisodeWatchingGet) | **GET** /shows/{id}/seasons/{season}/episodes/{episode}/watching | Get users watching right now



## getASingleEpisodeForAShow

> getASingleEpisodeForAShow(id, season, episode, opts)

Get a single episode for a show

#### &amp;#10024; Extended Info  Returns a single episode&#39;s details. All date and times are in UTC and were calculated using the episode&#39;s &#x60;air_date&#x60; and show&#39;s &#x60;country&#x60; and &#x60;air_time&#x60;.  **Note:** If the &#x60;first_aired&#x60; is unknown, it will be set to &#x60;null&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.EpisodesApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let season = 1; // Number | season number
let episode = 1; // Number | episode number
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getASingleEpisodeForAShow(id, season, episode, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | 
 **season** | **Number**| season number | 
 **episode** | **Number**| episode number | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllEpisodeComments

> getAllEpisodeComments(id, season, episode, sort, opts)

Get all episode comments

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for an episode. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, most &#x60;replies&#x60;, &#x60;highest&#x60; rated, &#x60;lowest&#x60; rated, and most &#x60;plays&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.EpisodesApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let season = 1; // Number | season number
let episode = 1; // Number | episode number
let sort = "newest"; // String | how to sort
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllEpisodeComments(id, season, episode, sort, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | 
 **season** | **Number**| season number | 
 **episode** | **Number**| episode number | 
 **sort** | **String**| how to sort | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllEpisodeTranslations

> getAllEpisodeTranslations(id, season, episode, language, opts)

Get all episode translations

Returns all translations for an episode, including language and translated values for title and overview.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.EpisodesApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let season = 1; // Number | season number
let episode = 1; // Number | episode number
let language = "es"; // String | 2 character language code
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllEpisodeTranslations(id, season, episode, language, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | 
 **season** | **Number**| season number | 
 **episode** | **Number**| episode number | 
 **language** | **String**| 2 character language code | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllPeopleForAnEpisode

> getAllPeopleForAnEpisode(id, season, episode, opts)

Get all people for an episode

#### &amp;#10024; Extended Info  Returns all &#x60;cast&#x60; and &#x60;crew&#x60; for an episode. Each &#x60;cast&#x60; member will have a &#x60;characters&#x60; array and a standard &#x60;person&#x60; object.  The &#x60;crew&#x60; object will be broken up by department into &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, and &#x60;editing&#x60; (if there are people for those crew positions). Each of those members will have a &#x60;jobs&#x60; array and a standard &#x60;person&#x60; object.  #### Guest Stars  If you add &#x60;?extended&#x3D;guest_stars&#x60; to the URL, it will return all guest stars that appeared in the episode.  **Note:** This returns a lot of data, so please only use this extended parameter if you actually need it!

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.EpisodesApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let season = 1; // Number | season number
let episode = 1; // Number | episode number
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllPeopleForAnEpisode(id, season, episode, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | 
 **season** | **Number**| season number | 
 **episode** | **Number**| episode number | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEpisodeRatings

> getEpisodeRatings(id, season, episode, opts)

Get episode ratings

Returns rating (between 0 and 10) and distribution for an episode.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.EpisodesApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let season = 1; // Number | season number
let episode = 12; // Number | episode number
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getEpisodeRatings(id, season, episode, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | 
 **season** | **Number**| season number | 
 **episode** | **Number**| episode number | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEpisodeStats

> getEpisodeStats(id, season, episode, opts)

Get episode stats

Returns lots of episode stats.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.EpisodesApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let season = 1; // Number | season number
let episode = 1; // Number | episode number
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getEpisodeStats(id, season, episode, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | 
 **season** | **Number**| season number | 
 **episode** | **Number**| episode number | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getListsContainingThisEpisode

> getListsContainingThisEpisode(id, season, episode, type, sort, opts)

Get lists containing this episode

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all lists that contain this episode. By default, &#x60;personal&#x60; lists are returned sorted by the most &#x60;popular&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.EpisodesApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let season = 1; // Number | season number
let episode = 1; // Number | episode number
let type = "personal"; // String | Filter for a specific list type
let sort = "popular"; // String | How to sort
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getListsContainingThisEpisode(id, season, episode, type, sort, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | 
 **season** | **Number**| season number | 
 **episode** | **Number**| episode number | 
 **type** | **String**| Filter for a specific list type | 
 **sort** | **String**| How to sort | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showsIdSeasonsSeasonEpisodesEpisodeWatchingGet

> showsIdSeasonsSeasonEpisodesEpisodeWatchingGet(id, season, episode, opts)

Get users watching right now

#### &amp;#10024; Extended Info  Returns all users watching this episode right now.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.EpisodesApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let season = 1; // Number | season number
let episode = 1; // Number | episode number
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.showsIdSeasonsSeasonEpisodesEpisodeWatchingGet(id, season, episode, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Trakt ID, Trakt slug, or IMDB ID | 
 **season** | **Number**| season number | 
 **episode** | **Number**| episode number | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

