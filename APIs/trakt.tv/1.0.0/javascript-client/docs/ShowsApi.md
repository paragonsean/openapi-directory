# TraktApi.ShowsApi

All URIs are relative to *https://api.trakt.tv*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getASingleShow**](ShowsApi.md#getASingleShow) | **GET** /shows/{id} | Get a single show
[**getAllPeopleForAShow**](ShowsApi.md#getAllPeopleForAShow) | **GET** /shows/{id}/people | Get all people for a show
[**getAllShowAliases**](ShowsApi.md#getAllShowAliases) | **GET** /shows/{id}/aliases | Get all show aliases
[**getAllShowCertifications**](ShowsApi.md#getAllShowCertifications) | **GET** /shows/{id}/certifications | Get all show certifications
[**getAllShowComments**](ShowsApi.md#getAllShowComments) | **GET** /shows/{id}/comments/{sort} | Get all show comments
[**getAllShowTranslations**](ShowsApi.md#getAllShowTranslations) | **GET** /shows/{id}/translations/{language} | Get all show translations
[**getLastEpisode**](ShowsApi.md#getLastEpisode) | **GET** /shows/{id}/last_episode | Get last episode
[**getListsContainingThisShow**](ShowsApi.md#getListsContainingThisShow) | **GET** /shows/{id}/lists/{type}/{sort} | Get lists containing this show
[**getNextEpisode**](ShowsApi.md#getNextEpisode) | **GET** /shows/{id}/next_episode | Get next episode
[**getPopularShows**](ShowsApi.md#getPopularShows) | **GET** /shows/popular | Get popular shows
[**getRecentlyUpdatedShowTraktIDs**](ShowsApi.md#getRecentlyUpdatedShowTraktIDs) | **GET** /shows/updates/id/{start_date} | Get recently updated show Trakt IDs
[**getRecentlyUpdatedShows**](ShowsApi.md#getRecentlyUpdatedShows) | **GET** /shows/updates/{start_date} | Get recently updated shows
[**getRelatedShows**](ShowsApi.md#getRelatedShows) | **GET** /shows/{id}/related | Get related shows
[**getShowCollectionProgress**](ShowsApi.md#getShowCollectionProgress) | **GET** /shows/{id}/progress/collection | Get show collection progress
[**getShowRatings**](ShowsApi.md#getShowRatings) | **GET** /shows/{id}/ratings | Get show ratings
[**getShowStats**](ShowsApi.md#getShowStats) | **GET** /shows/{id}/stats | Get show stats
[**getShowStudios**](ShowsApi.md#getShowStudios) | **GET** /shows/{id}/studios | Get show studios
[**getShowWatchedProgress**](ShowsApi.md#getShowWatchedProgress) | **GET** /shows/{id}/progress/watched | Get show watched progress
[**getTheMostAnticipatedShows**](ShowsApi.md#getTheMostAnticipatedShows) | **GET** /shows/anticipated | Get the most anticipated shows
[**getTheMostCollectedShows**](ShowsApi.md#getTheMostCollectedShows) | **GET** /shows/collected/{period} | Get the most collected shows
[**getTheMostPlayedShows**](ShowsApi.md#getTheMostPlayedShows) | **GET** /shows/played/{period} | Get the most played shows
[**getTheMostRecommendedShows**](ShowsApi.md#getTheMostRecommendedShows) | **GET** /shows/recommended/{period} | Get the most recommended shows
[**getTheMostWatchedShows**](ShowsApi.md#getTheMostWatchedShows) | **GET** /shows/watched/{period} | Get the most watched shows
[**getTrendingShows**](ShowsApi.md#getTrendingShows) | **GET** /shows/trending | Get trending shows
[**resetShowProgress**](ShowsApi.md#resetShowProgress) | **POST** /shows/{id}/progress/watched/reset | Reset show progress
[**showsIdWatchingGet**](ShowsApi.md#showsIdWatchingGet) | **GET** /shows/{id}/watching | Get users watching right now
[**undoResetShowProgress**](ShowsApi.md#undoResetShowProgress) | **DELETE** /shows/{id}/progress/watched/reset | Undo reset show progress



## getASingleShow

> getASingleShow(id, opts)

Get a single show

#### &amp;#10024; Extended Info  Returns a single shows&#39;s details. If you request extended info, the &#x60;airs&#x60; object is relative to the show&#39;s country. You can use the &#x60;day&#x60;, &#x60;time&#x60;, and &#x60;timezone&#x60; to construct your own date then convert it to whatever timezone your user is in.  **Note:** When getting &#x60;full&#x60; extended info, the &#x60;status&#x60; field can have a value of &#x60;returning series&#x60; (airing right now),  &#x60;continuing&#x60; (airing right now), &#x60;in production&#x60; (airing soon), &#x60;planned&#x60; (in development), &#x60;upcoming&#x60; (in development),  &#x60;pilot&#x60;, &#x60;canceled&#x60;, or &#x60;ended&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getASingleShow(id, opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllPeopleForAShow

> getAllPeopleForAShow(id, opts)

Get all people for a show

#### &amp;#10024; Extended Info  Returns all &#x60;cast&#x60; and &#x60;crew&#x60; for a show, including the &#x60;episode_count&#x60; for which they appears. Each &#x60;cast&#x60; member will have a &#x60;characters&#x60; array and a standard &#x60;person&#x60; object.  The &#x60;crew&#x60; object will be broken up by department into &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, &#x60;editing&#x60;, and &#x60;created  by&#x60; (if there are people for those crew positions). Each of those members will have a &#x60;jobs&#x60; array and a standard &#x60;person&#x60; object.  #### Guest Stars  If you add &#x60;?extended&#x3D;guest_stars&#x60; to the URL, it will return all guest stars that appeared in at least 1 episode of the show.  **Note:** This returns a lot of data, so please only use this extended parameter if you actually need it!

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllPeopleForAShow(id, opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllShowAliases

> getAllShowAliases(id, opts)

Get all show aliases

Returns all title aliases for a show.  Includes country where name is different.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllShowAliases(id, opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllShowCertifications

> getAllShowCertifications(id, opts)

Get all show certifications

Returns all content certifications for a show, including the country.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllShowCertifications(id, opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllShowComments

> getAllShowComments(id, sort, opts)

Get all show comments

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for a show. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, most &#x60;replies&#x60;, &#x60;highest&#x60; rated, &#x60;lowest&#x60; rated, most &#x60;plays&#x60;, and highest &#x60;watched&#x60; percentage.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let sort = "newest"; // String | how to sort
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllShowComments(id, sort, opts, (error, data, response) => {
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


## getAllShowTranslations

> getAllShowTranslations(id, language, opts)

Get all show translations

Returns all translations for a show, including language and translated values for title and overview.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let language = "es"; // String | 2 character language code
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllShowTranslations(id, language, opts, (error, data, response) => {
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


## getLastEpisode

> getLastEpisode(id, opts)

Get last episode

#### &amp;#10024; Extended Info  Returns the most recently aired episode. If no episode is found, a &#x60;204&#x60; HTTP status code will be returned.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getLastEpisode(id, opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getListsContainingThisShow

> getListsContainingThisShow(id, type, sort, opts)

Get lists containing this show

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all lists that contain this show. By default, &#x60;personal&#x60; lists are returned sorted by the most &#x60;popular&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let type = "personal"; // String | Filter for a specific list type
let sort = "popular"; // String | How to sort
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getListsContainingThisShow(id, type, sort, opts, (error, data, response) => {
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


## getNextEpisode

> getNextEpisode(id, opts)

Get next episode

#### &amp;#10024; Extended Info  Returns the next scheduled to air episode. If no episode is found, a &#x60;204&#x60; HTTP status code will be returned.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getNextEpisode(id, opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPopularShows

> getPopularShows(opts)

Get popular shows

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most popular shows. Popularity is calculated using the rating percentage and the number of ratings.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getPopularShows(opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRecentlyUpdatedShowTraktIDs

> getRecentlyUpdatedShowTraktIDs(startDate, opts)

Get recently updated show Trakt IDs

#### &amp;#128196; Pagination  Returns all show Trakt IDs updated since the specified UTC date and time. We recommended storing the &#x60;X-Start-Date&#x60; header you can be efficient using this method moving forward. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page.  **Important!** The &#x60;start_date&#x60; is only accurate to the hour, for caching purposes. Please drop the minutes and seconds from your timestamp to help optimize our cached data. For example, use &#x60;2021-07-17T12:00:00Z&#x60; and not &#x60;2021-07-17T12:23:34Z&#x60;.  **Note:** The &#x60;start_date&#x60; can only be a maximum of 30 days in the past.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let startDate = "2020-11-27T00:00:00Z"; // String | Updated since this date and time.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getRecentlyUpdatedShowTraktIDs(startDate, opts, (error, data, response) => {
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
 **startDate** | **String**| Updated since this date and time. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRecentlyUpdatedShows

> getRecentlyUpdatedShows(startDate, opts)

Get recently updated shows

#### &amp;#128196; Pagination &amp;#10024; Extended Info  Returns all shows updated since the specified UTC date and time. We recommended storing the &#x60;X-Start-Date&#x60; header you can be efficient using this method moving forward. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page.  **Important!** The &#x60;start_date&#x60; is only accurate to the hour, for caching purposes. Please drop the minutes and seconds from your timestamp to help optimize our cached data. For example, use &#x60;2021-07-17T12:00:00Z&#x60; and not &#x60;2021-07-17T12:23:34Z&#x60;.  **Note:** The &#x60;start_date&#x60; can only be a maximum of 30 days in the past.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let startDate = "2020-11-27T00:00:00Z"; // String | Updated since this date and time.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getRecentlyUpdatedShows(startDate, opts, (error, data, response) => {
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
 **startDate** | **String**| Updated since this date and time. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRelatedShows

> getRelatedShows(id, opts)

Get related shows

#### &amp;#128196; Pagination &amp;#10024; Extended Info  Returns related and similar shows.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getRelatedShows(id, opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getShowCollectionProgress

> getShowCollectionProgress(id, body, opts)

Get show collection progress

#### &amp;#128274; OAuth Required  Returns collection progress for a show including details on all aired seasons and episodes. The &#x60;next_episode&#x60; will be the next episode the user should collect, if there are no upcoming episodes it will be set to &#x60;null&#x60;.  By default, any hidden seasons will be removed from the response and stats. To include these and adjust the completion stats, set the &#x60;hidden&#x60; flag to &#x60;true&#x60;.  By default, specials will be excluded from the response. Set the &#x60;specials&#x60; flag to &#x60;true&#x60; to include season 0 and adjust the stats accordingly. If you&#39;d like to include specials, but not adjust the stats, set &#x60;count_specials&#x60; to &#x60;false&#x60;.  By default, the &#x60;last_episode&#x60; and &#x60;next_episode&#x60; are calculated using the last &#x60;aired&#x60; episode the user has collected, even if they&#39;ve collected older episodes more recently. To use their last collected episode for these calculations, set the &#x60;last_activity&#x60; flag to &#x60;collected&#x60;.  **Note:** Only aired episodes are used to calculate progress. Episodes in the future or without an air date are ignored.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.ShowsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let body = "body_example"; // String | 
let opts = {
  'hidden': "false", // String | include any hidden seasons
  'specials': "false", // String | include specials as season 0
  'countSpecials': "true", // String | count specials in the overall stats (only applies if specials are included)
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getShowCollectionProgress(id, body, opts, (error, data, response) => {
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
 **body** | **String**|  | 
 **hidden** | **String**| include any hidden seasons | [optional] 
 **specials** | **String**| include specials as season 0 | [optional] 
 **countSpecials** | **String**| count specials in the overall stats (only applies if specials are included) | [optional] 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getShowRatings

> getShowRatings(id, opts)

Get show ratings

Returns rating (between 0 and 10) and distribution for a show.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getShowRatings(id, opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getShowStats

> getShowStats(id, opts)

Get show stats

Returns lots of show stats.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getShowStats(id, opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getShowStudios

> getShowStudios(id, opts)

Get show studios

Returns all studios for a show.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getShowStudios(id, opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getShowWatchedProgress

> getShowWatchedProgress(id, body, opts)

Get show watched progress

#### &amp;#128274; OAuth Required  Returns watched progress for a show including details on all aired seasons and episodes. The &#x60;next_episode&#x60; will be the next episode the user should watch, if there are no upcoming episodes it will be set to &#x60;null&#x60;. If not &#x60;null&#x60;, the &#x60;reset_at&#x60; date is when the user started re-watching the show. Your app can adjust the progress by ignoring episodes with a &#x60;last_watched_at&#x60; prior to the &#x60;reset_at&#x60;.  By default, any hidden seasons will be removed from the response and stats. To include these and adjust the completion stats, set the &#x60;hidden&#x60; flag to &#x60;true&#x60;.  By default, specials will be excluded from the response. Set the &#x60;specials&#x60; flag to &#x60;true&#x60; to include season 0 and adjust the stats accordingly. If you&#39;d like to include specials, but not adjust the stats, set &#x60;count_specials&#x60; to &#x60;false&#x60;.  By default, the &#x60;last_episode&#x60; and &#x60;next_episode&#x60; are calculated using the last &#x60;aired&#x60; episode the user has watched, even if they&#39;ve watched older episodes more recently. To use their last watched episode for these calculations, set the &#x60;last_activity&#x60; flag to &#x60;watched&#x60;.  **Note:** Only aired episodes are used to calculate progress. Episodes in the future or without an air date are ignored.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.ShowsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let body = "body_example"; // String | 
let opts = {
  'hidden': "false", // String | include any hidden seasons
  'specials': "false", // String | include specials as season 0
  'countSpecials': "true", // String | count specials in the overall stats (only applies if specials are included)
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getShowWatchedProgress(id, body, opts, (error, data, response) => {
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
 **body** | **String**|  | 
 **hidden** | **String**| include any hidden seasons | [optional] 
 **specials** | **String**| include specials as season 0 | [optional] 
 **countSpecials** | **String**| count specials in the overall stats (only applies if specials are included) | [optional] 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTheMostAnticipatedShows

> getTheMostAnticipatedShows(opts)

Get the most anticipated shows

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most anticipated shows based on the number of lists a show appears on.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getTheMostAnticipatedShows(opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTheMostCollectedShows

> getTheMostCollectedShows(period, opts)

Get the most collected shows

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most collected (unique users) shows in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let period = "weekly"; // String | Time period.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getTheMostCollectedShows(period, opts, (error, data, response) => {
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
 **period** | **String**| Time period. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTheMostPlayedShows

> getTheMostPlayedShows(period, opts)

Get the most played shows

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most played (a single user can watch multiple episodes multiple times) shows in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let period = "weekly"; // String | Time period.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getTheMostPlayedShows(period, opts, (error, data, response) => {
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
 **period** | **String**| Time period. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTheMostRecommendedShows

> getTheMostRecommendedShows(period, opts)

Get the most recommended shows

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most recommended shows in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let period = "weekly"; // String | Time period.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getTheMostRecommendedShows(period, opts, (error, data, response) => {
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
 **period** | **String**| Time period. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTheMostWatchedShows

> getTheMostWatchedShows(period, opts)

Get the most watched shows

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most watched (unique users) shows in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let period = "weekly"; // String | Time period.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getTheMostWatchedShows(period, opts, (error, data, response) => {
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
 **period** | **String**| Time period. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrendingShows

> getTrendingShows(opts)

Get trending shows

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns all shows being watched right now. Shows with the most users are returned first.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getTrendingShows(opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resetShowProgress

> resetShowProgress(id, opts)

Reset show progress

#### &amp;#128274; OAuth Required 🔥 VIP Only  Reset a show&#39;s progress when the user started re-watching the show. You can optionally specify the &#x60;reset_at&#x60; date to have it calculate progress from that specific date onwards.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.ShowsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.resetShowProgress(id, opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showsIdWatchingGet

> showsIdWatchingGet(id, opts)

Get users watching right now

#### &amp;#10024; Extended Info  Returns all users watching this show right now.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.ShowsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.showsIdWatchingGet(id, opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## undoResetShowProgress

> undoResetShowProgress(id, opts)

Undo reset show progress

#### &amp;#128274; OAuth Required 🔥 VIP Only  Undo the reset and have watched progress use all watched history for the show.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.ShowsApi();
let id = "id_example"; // String | Automatically added
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.undoResetShowProgress(id, opts, (error, data, response) => {
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
 **id** | **String**| Automatically added | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

