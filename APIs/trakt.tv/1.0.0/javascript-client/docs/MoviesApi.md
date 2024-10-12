# TraktApi.MoviesApi

All URIs are relative to *https://api.trakt.tv*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAMovie**](MoviesApi.md#getAMovie) | **GET** /movies/{id} | Get a movie
[**getAllMovieAliases**](MoviesApi.md#getAllMovieAliases) | **GET** /movies/{id}/aliases | Get all movie aliases
[**getAllMovieComments**](MoviesApi.md#getAllMovieComments) | **GET** /movies/{id}/comments/{sort} | Get all movie comments
[**getAllMovieReleases**](MoviesApi.md#getAllMovieReleases) | **GET** /movies/{id}/releases/{country} | Get all movie releases
[**getAllMovieTranslations**](MoviesApi.md#getAllMovieTranslations) | **GET** /movies/{id}/translations/{language} | Get all movie translations
[**getAllPeopleForAMovie**](MoviesApi.md#getAllPeopleForAMovie) | **GET** /movies/{id}/people | Get all people for a movie
[**getListsContainingThisMovie**](MoviesApi.md#getListsContainingThisMovie) | **GET** /movies/{id}/lists/{type}/{sort} | Get lists containing this movie
[**getMovieRatings**](MoviesApi.md#getMovieRatings) | **GET** /movies/{id}/ratings | Get movie ratings
[**getMovieStats**](MoviesApi.md#getMovieStats) | **GET** /movies/{id}/stats | Get movie stats
[**getMovieStudios**](MoviesApi.md#getMovieStudios) | **GET** /movies/{id}/studios | Get movie studios
[**getPopularMovies**](MoviesApi.md#getPopularMovies) | **GET** /movies/popular | Get popular movies
[**getRecentlyUpdatedMovieTraktIDs**](MoviesApi.md#getRecentlyUpdatedMovieTraktIDs) | **GET** /movies/updates/id/{start_date} | Get recently updated movie Trakt IDs
[**getRecentlyUpdatedMovies**](MoviesApi.md#getRecentlyUpdatedMovies) | **GET** /movies/updates/{start_date} | Get recently updated movies
[**getRelatedMovies**](MoviesApi.md#getRelatedMovies) | **GET** /movies/{id}/related | Get related movies
[**getTheMostAnticipatedMovies**](MoviesApi.md#getTheMostAnticipatedMovies) | **GET** /movies/anticipated | Get the most anticipated movies
[**getTheMostCollectedMovies**](MoviesApi.md#getTheMostCollectedMovies) | **GET** /movies/collected/{period} | Get the most Collected movies
[**getTheMostPlayedMovies**](MoviesApi.md#getTheMostPlayedMovies) | **GET** /movies/played/{period} | Get the most played movies
[**getTheMostRecommendedMovies**](MoviesApi.md#getTheMostRecommendedMovies) | **GET** /movies/recommended/{period} | Get the most recommended movies
[**getTheMostWatchedMovies**](MoviesApi.md#getTheMostWatchedMovies) | **GET** /movies/watched/{period} | Get the most watched movies
[**getTheWeekendBoxOffice**](MoviesApi.md#getTheWeekendBoxOffice) | **GET** /movies/boxoffice | Get the weekend box office
[**getTrendingMovies**](MoviesApi.md#getTrendingMovies) | **GET** /movies/trending | Get trending movies
[**getUsersWatchingRightNow**](MoviesApi.md#getUsersWatchingRightNow) | **GET** /movies/{id}/watching | Get users watching right now



## getAMovie

> getAMovie(id, opts)

Get a movie

#### &amp;#10024; Extended Info  Returns a single movie&#39;s details.  **Note:** When getting &#x60;full&#x60; extended info, the &#x60;status&#x60; field can have a value of &#x60;released&#x60;, &#x60;in production&#x60;, &#x60;post production&#x60;, &#x60;planned&#x60;, &#x60;rumored&#x60;, or &#x60;canceled&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAMovie(id, opts, (error, data, response) => {
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


## getAllMovieAliases

> getAllMovieAliases(id, opts)

Get all movie aliases

Returns all title aliases for a movie.  Includes country where name is different.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllMovieAliases(id, opts, (error, data, response) => {
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


## getAllMovieComments

> getAllMovieComments(id, sort, opts)

Get all movie comments

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all top level comments for a movie. By default, the &#x60;newest&#x60; comments are returned first. Other sorting options include &#x60;oldest&#x60;, most &#x60;likes&#x60;, most &#x60;replies&#x60;, &#x60;highest&#x60; rated, &#x60;lowest&#x60; rated, and most &#x60;plays&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
let sort = "newest"; // String | how to sort
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllMovieComments(id, sort, opts, (error, data, response) => {
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


## getAllMovieReleases

> getAllMovieReleases(id, country, opts)

Get all movie releases

Returns all releases for a movie including country, certification, release date, release type, and note. The release type can be set to &#x60;unknown&#x60;, &#x60;premiere&#x60;, &#x60;limited&#x60;, &#x60;theatrical&#x60;, &#x60;digital&#x60;, &#x60;physical&#x60;, or &#x60;tv&#x60;. The &#x60;note&#x60; might have optional info such as the film festival name for a &#x60;premiere&#x60; release or Blu-ray specs for a &#x60;physical&#x60; release. We pull this info from [TMDB](https://developers.themoviedb.org/3/movies/get-movie-release-dates).

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
let country = "us"; // String | 2 character country code
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllMovieReleases(id, country, opts, (error, data, response) => {
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
 **country** | **String**| 2 character country code | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllMovieTranslations

> getAllMovieTranslations(id, language, opts)

Get all movie translations

Returns all translations for a movie, including language and translated values for title, tagline and overview.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
let language = "es"; // String | 2 character language code
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllMovieTranslations(id, language, opts, (error, data, response) => {
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


## getAllPeopleForAMovie

> getAllPeopleForAMovie(id, opts)

Get all people for a movie

#### &amp;#10024; Extended Info  Returns all &#x60;cast&#x60; and &#x60;crew&#x60; for a movie. Each &#x60;cast&#x60; member will have a &#x60;characters&#x60; array and a standard &#x60;person&#x60; object.  The &#x60;crew&#x60; object will be broken up by department into &#x60;production&#x60;, &#x60;art&#x60;, &#x60;crew&#x60;, &#x60;costume &amp; make-up&#x60;, &#x60;directing&#x60;, &#x60;writing&#x60;, &#x60;sound&#x60;, &#x60;camera&#x60;, &#x60;visual effects&#x60;, &#x60;lighting&#x60;, and &#x60;editing&#x60; (if there are people for those crew positions). Each of those members will have a &#x60;jobs&#x60; array and a standard &#x60;person&#x60; object.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getAllPeopleForAMovie(id, opts, (error, data, response) => {
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


## getListsContainingThisMovie

> getListsContainingThisMovie(id, type, sort, opts)

Get lists containing this movie

#### &amp;#128196; Pagination &amp;#128513; Emojis  Returns all lists that contain this movie. By default, &#x60;personal&#x60; lists are returned sorted by the most &#x60;popular&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
let type = "personal"; // String | Filter for a specific list type
let sort = "popular"; // String | How to sort
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getListsContainingThisMovie(id, type, sort, opts, (error, data, response) => {
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


## getMovieRatings

> getMovieRatings(id, opts)

Get movie ratings

Returns rating (between 0 and 10) and distribution for a movie.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getMovieRatings(id, opts, (error, data, response) => {
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


## getMovieStats

> getMovieStats(id, opts)

Get movie stats

Returns lots of movie stats.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getMovieStats(id, opts, (error, data, response) => {
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


## getMovieStudios

> getMovieStudios(id, opts)

Get movie studios

Returns all studios for a movie.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getMovieStudios(id, opts, (error, data, response) => {
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


## getPopularMovies

> getPopularMovies(opts)

Get popular movies

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most popular movies. Popularity is calculated using the rating percentage and the number of ratings.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getPopularMovies(opts, (error, data, response) => {
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


## getRecentlyUpdatedMovieTraktIDs

> getRecentlyUpdatedMovieTraktIDs(startDate, opts)

Get recently updated movie Trakt IDs

#### &amp;#128196; Pagination  Returns all movie Trakt IDs updated since the specified UTC date and time. We recommended storing the &#x60;X-Start-Date&#x60; header you can be efficient using this method moving forward. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page.  **Important!** The &#x60;start_date&#x60; is only accurate to the hour, for caching purposes. Please drop the minutes and seconds from your timestamp to help optimize our cached data. For example, use &#x60;2021-07-17T12:00:00Z&#x60; and not &#x60;2021-07-17T12:23:34Z&#x60;.  **Note:** The &#x60;start_date&#x60; can only be a maximum of 30 days in the past.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let startDate = "2020-11-27T00:00:00Z"; // String | Updated since this date and time.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getRecentlyUpdatedMovieTraktIDs(startDate, opts, (error, data, response) => {
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


## getRecentlyUpdatedMovies

> getRecentlyUpdatedMovies(startDate, opts)

Get recently updated movies

#### &amp;#128196; Pagination &amp;#10024; Extended Info  Returns all movies updated since the specified UTC date and time. We recommended storing the &#x60;X-Start-Date&#x60; header you can be efficient using this method moving forward. By default, &#x60;10&#x60; results are returned. You can send a &#x60;limit&#x60; to get up to &#x60;100&#x60; results per page.  **Important!** The &#x60;start_date&#x60; is only accurate to the hour, for caching purposes. Please drop the minutes and seconds from your timestamp to help optimize our cached data. For example, use &#x60;2021-07-17T12:00:00Z&#x60; and not &#x60;2021-07-17T12:23:34Z&#x60;.  **Note:** The &#x60;start_date&#x60; can only be a maximum of 30 days in the past.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let startDate = "2020-11-27T00:00:00Z"; // String | Updated since this date and time.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getRecentlyUpdatedMovies(startDate, opts, (error, data, response) => {
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


## getRelatedMovies

> getRelatedMovies(id, opts)

Get related movies

#### &amp;#128196; Pagination &amp;#10024; Extended Info  Returns related and similar movies.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getRelatedMovies(id, opts, (error, data, response) => {
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


## getTheMostAnticipatedMovies

> getTheMostAnticipatedMovies(opts)

Get the most anticipated movies

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most anticipated movies based on the number of lists a movie appears on.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getTheMostAnticipatedMovies(opts, (error, data, response) => {
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


## getTheMostCollectedMovies

> getTheMostCollectedMovies(period, opts)

Get the most Collected movies

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most collected (unique users) movies in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let period = "weekly"; // String | Time period.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getTheMostCollectedMovies(period, opts, (error, data, response) => {
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


## getTheMostPlayedMovies

> getTheMostPlayedMovies(period, opts)

Get the most played movies

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most played (a single user can watch multiple times) movies in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let period = "weekly"; // String | Time period.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getTheMostPlayedMovies(period, opts, (error, data, response) => {
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


## getTheMostRecommendedMovies

> getTheMostRecommendedMovies(period, opts)

Get the most recommended movies

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most recommended movies in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let period = "weekly"; // String | Time period.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getTheMostRecommendedMovies(period, opts, (error, data, response) => {
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


## getTheMostWatchedMovies

> getTheMostWatchedMovies(period, opts)

Get the most watched movies

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns the most watched (unique users) movies in the specified time &#x60;period&#x60;, defaulting to &#x60;weekly&#x60;. All stats are relative to the specific time &#x60;period&#x60;.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let period = "weekly"; // String | Time period.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getTheMostWatchedMovies(period, opts, (error, data, response) => {
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


## getTheWeekendBoxOffice

> getTheWeekendBoxOffice(opts)

Get the weekend box office

#### &amp;#10024; Extended Info  Returns the top 10 grossing movies in the U.S. box office last weekend. Updated every Monday morning.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getTheWeekendBoxOffice(opts, (error, data, response) => {
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


## getTrendingMovies

> getTrendingMovies(opts)

Get trending movies

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Returns all movies being watched right now. Movies with the most users are returned first.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getTrendingMovies(opts, (error, data, response) => {
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


## getUsersWatchingRightNow

> getUsersWatchingRightNow(id, opts)

Get users watching right now

#### &amp;#10024; Extended Info  Returns all users watching this movie right now.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.MoviesApi();
let id = "tron-legacy-2010"; // String | Trakt ID, Trakt slug, or IMDB ID
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getUsersWatchingRightNow(id, opts, (error, data, response) => {
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

