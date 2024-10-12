# TraktApi.SeasonsApi

All URIs are relative to *https://api.trakt.tv*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllPeopleForASeason**](SeasonsApi.md#getAllPeopleForASeason) | **GET** /shows/{id}/seasons/{season}/people | Get all people for a season
[**getAllSeasonComments**](SeasonsApi.md#getAllSeasonComments) | **GET** /shows/{id}/seasons/{season}/comments/{sort} | Get all season comments
[**getAllSeasonTranslations**](SeasonsApi.md#getAllSeasonTranslations) | **GET** /shows/{id}/seasons/{season}/translations/{language} | Get all season translations
[**getAllSeasonsForAShow**](SeasonsApi.md#getAllSeasonsForAShow) | **GET** /shows/{id}/seasons | Get all seasons for a show
[**getListsContainingThisSeason**](SeasonsApi.md#getListsContainingThisSeason) | **GET** /shows/{id}/seasons/{season}/lists/{type}/{sort} | Get lists containing this season
[**getSeasonRatings**](SeasonsApi.md#getSeasonRatings) | **GET** /shows/{id}/seasons/{season}/ratings | Get season ratings
[**getSeasonStats**](SeasonsApi.md#getSeasonStats) | **GET** /shows/{id}/seasons/{season}/stats | Get season stats
[**getSingleSeasonForAShow**](SeasonsApi.md#getSingleSeasonForAShow) | **GET** /shows/{id}/seasons/{season} | Get single season for a show
[**showsIdSeasonsSeasonWatchingGet**](SeasonsApi.md#showsIdSeasonsSeasonWatchingGet) | **GET** /shows/{id}/seasons/{season}/watching | Get users watching right now



## getAllPeopleForASeason

> getAllPeopleForASeason(id, season, opts)

Get all people for a season

#### &amp;#10024; Extended Info  Returns all &#x60;cast&#x60; and &#x60;crew&#x60; for a season, including the &#x60;episode_count&#x60; for which they appear. Each &#x60;cast&#x60; member will have a &#x60;characters&#x60; array and a standard &#x60;person&#x60; object.  The &#x60;crew&#x60; object will be broken up by department into &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, and &#x60;editing&#x60; (if there are people for those crew positions).. Each of those members will have a &#x60;jobs&#x60; array and a standard &#x60;person&#x60; object.  #### Guest Stars  If you add &#x60;?extended&#x3D;guest_stars&#x60; to the URL, it will return all guest stars that appeared in at least 1 episode of the season.  **Note:** This returns a lot of data, so please only use this extended parameter if you actually need it!

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.SeasonsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let season = 1; // Number | season number
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllPeopleForASeason(id, season, opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllSeasonComments

> getAllSeasonComments(id, season, sort, opts)

Get all season comments

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for a season. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, most &#x60;replies&#x60;, &#x60;highest&#x60; rated, &#x60;lowest&#x60; rated, most &#x60;plays&#x60;, and highest &#x60;watched&#x60; percentage.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.SeasonsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let season = 1; // Number | season number
let sort = "newest"; // String | how to sort
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllSeasonComments(id, season, sort, opts, (error, data, response) => {
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


## getAllSeasonTranslations

> getAllSeasonTranslations(id, season, language, opts)

Get all season translations

Returns all translations for an season, including language and translated values for title and overview.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.SeasonsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let season = 1; // Number | season number
let language = "es"; // String | 2 character language code
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllSeasonTranslations(id, season, language, opts, (error, data, response) => {
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


## getAllSeasonsForAShow

> getAllSeasonsForAShow(id, opts)

Get all seasons for a show

#### &amp;#10024; Extended Info  Returns all seasons for a show including the number of episodes in each season.  #### Episodes  If you add &#x60;?extended&#x3D;episodes&#x60; to the URL, it will return all episodes for all seasons.  **Note:** This returns a lot of data, so please only use this extended parameter if you actually need it!

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.SeasonsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllSeasonsForAShow(id, opts, (error, data, response) => {
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


## getListsContainingThisSeason

> getListsContainingThisSeason(id, season, type, sort, opts)

Get lists containing this season

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all lists that contain this season. By default, &#x60;personal&#x60; lists are returned sorted by the most &#x60;popular&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.SeasonsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let season = 1; // Number | season number
let type = "personal"; // String | Filter for a specific list type
let sort = "popular"; // String | How to sort
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getListsContainingThisSeason(id, season, type, sort, opts, (error, data, response) => {
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


## getSeasonRatings

> getSeasonRatings(id, season, opts)

Get season ratings

Returns rating (between 0 and 10) and distribution for a season.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.SeasonsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let season = 1; // Number | season number
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getSeasonRatings(id, season, opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSeasonStats

> getSeasonStats(id, season, opts)

Get season stats

Returns lots of season stats.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.SeasonsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let season = 1; // Number | season number
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getSeasonStats(id, season, opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSingleSeasonForAShow

> getSingleSeasonForAShow(id, season, opts)

Get single season for a show

#### &amp;#10024; Extended Info  Returns all episodes for a specific season of a show.  #### Translations  If you&#39;d like to included translated episode titles and overviews in the response, include the &#x60;translations&#x60; parameter in the URL. Include all languages by setting the parameter to &#x60;all&#x60; or use a specific 2 digit country language code to further limit it.  **Note:** This returns a lot of data, so please only use this parameter if you actually need it!

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.SeasonsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let season = 1; // Number | season number
let opts = {
  'translations': "es", // String | include episode translations
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getSingleSeasonForAShow(id, season, opts, (error, data, response) => {
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
 **translations** | **String**| include episode translations | [optional] 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showsIdSeasonsSeasonWatchingGet

> showsIdSeasonsSeasonWatchingGet(id, season, opts)

Get users watching right now

#### &amp;#10024; Extended Info  Returns all users watching this season right now.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.SeasonsApi();
let id = "game-of-thrones"; // String | Trakt ID, Trakt slug, or IMDB ID
let season = 1; // Number | season number
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.showsIdSeasonsSeasonWatchingGet(id, season, opts, (error, data, response) => {
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
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

