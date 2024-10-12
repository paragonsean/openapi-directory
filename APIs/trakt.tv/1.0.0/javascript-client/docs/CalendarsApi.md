# TraktApi.CalendarsApi

All URIs are relative to *https://api.trakt.tv*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calendarsAllDvdStartDateDaysGet**](CalendarsApi.md#calendarsAllDvdStartDateDaysGet) | **GET** /calendars/all/dvd/{start_date}/{days} | Get DVD releases
[**calendarsAllMoviesStartDateDaysGet**](CalendarsApi.md#calendarsAllMoviesStartDateDaysGet) | **GET** /calendars/all/movies/{start_date}/{days} | Get movies
[**calendarsAllShowsNewStartDateDaysGet**](CalendarsApi.md#calendarsAllShowsNewStartDateDaysGet) | **GET** /calendars/all/shows/new/{start_date}/{days} | Get new shows
[**calendarsAllShowsPremieresStartDateDaysGet**](CalendarsApi.md#calendarsAllShowsPremieresStartDateDaysGet) | **GET** /calendars/all/shows/premieres/{start_date}/{days} | Get season premieres
[**calendarsAllShowsStartDateDaysGet**](CalendarsApi.md#calendarsAllShowsStartDateDaysGet) | **GET** /calendars/all/shows/{start_date}/{days} | Get shows
[**getDVDReleases**](CalendarsApi.md#getDVDReleases) | **GET** /calendars/my/dvd/{start_date}/{days} | Get DVD releases
[**getMovies**](CalendarsApi.md#getMovies) | **GET** /calendars/my/movies/{start_date}/{days} | Get movies
[**getNewShows**](CalendarsApi.md#getNewShows) | **GET** /calendars/my/shows/new/{start_date}/{days} | Get new shows
[**getSeasonPremieres**](CalendarsApi.md#getSeasonPremieres) | **GET** /calendars/my/shows/premieres/{start_date}/{days} | Get season premieres
[**getShows**](CalendarsApi.md#getShows) | **GET** /calendars/my/shows/{start_date}/{days} | Get shows



## calendarsAllDvdStartDateDaysGet

> calendarsAllDvdStartDateDaysGet(startDate, days, opts)

Get DVD releases

#### &amp;#10024; Extended Info &amp;#127898; Filters  Returns all movies with a DVD release date during the time period specified.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.CalendarsApi();
let startDate = "2014-09-01"; // String | Start the calendar on this date.
let days = 7; // Number | Number of days to display.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.calendarsAllDvdStartDateDaysGet(startDate, days, opts, (error, data, response) => {
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
 **startDate** | **String**| Start the calendar on this date. | 
 **days** | **Number**| Number of days to display. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## calendarsAllMoviesStartDateDaysGet

> calendarsAllMoviesStartDateDaysGet(startDate, days, opts)

Get movies

#### &amp;#10024; Extended Info &amp;#127898; Filters  Returns all movies with a release date during the time period specified.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.CalendarsApi();
let startDate = "2014-09-01"; // String | Start the calendar on this date.
let days = 7; // Number | Number of days to display.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.calendarsAllMoviesStartDateDaysGet(startDate, days, opts, (error, data, response) => {
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
 **startDate** | **String**| Start the calendar on this date. | 
 **days** | **Number**| Number of days to display. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## calendarsAllShowsNewStartDateDaysGet

> calendarsAllShowsNewStartDateDaysGet(startDate, days, opts)

Get new shows

#### &amp;#10024; Extended Info &amp;#127898; Filters  Returns all new show premieres (season 1, episode 1) airing during the time period specified.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.CalendarsApi();
let startDate = "2014-09-01"; // String | Start the calendar on this date.
let days = 7; // Number | Number of days to display.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.calendarsAllShowsNewStartDateDaysGet(startDate, days, opts, (error, data, response) => {
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
 **startDate** | **String**| Start the calendar on this date. | 
 **days** | **Number**| Number of days to display. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## calendarsAllShowsPremieresStartDateDaysGet

> calendarsAllShowsPremieresStartDateDaysGet(startDate, days, opts)

Get season premieres

#### &amp;#10024; Extended Info &amp;#127898; Filters  Returns all show premieres (any season, episode 1) airing during the time period specified.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.CalendarsApi();
let startDate = "2014-09-01"; // String | Start the calendar on this date.
let days = 7; // Number | Number of days to display.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.calendarsAllShowsPremieresStartDateDaysGet(startDate, days, opts, (error, data, response) => {
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
 **startDate** | **String**| Start the calendar on this date. | 
 **days** | **Number**| Number of days to display. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## calendarsAllShowsStartDateDaysGet

> calendarsAllShowsStartDateDaysGet(startDate, days, opts)

Get shows

#### &amp;#10024; Extended Info &amp;#127898; Filters  Returns all shows airing during the time period specified.

### Example

```javascript
import TraktApi from 'trakt_api';

let apiInstance = new TraktApi.CalendarsApi();
let startDate = "2014-09-01"; // String | Start the calendar on this date.
let days = 7; // Number | Number of days to display.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.calendarsAllShowsStartDateDaysGet(startDate, days, opts, (error, data, response) => {
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
 **startDate** | **String**| Start the calendar on this date. | 
 **days** | **Number**| Number of days to display. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDVDReleases

> getDVDReleases(startDate, days, opts)

Get DVD releases

#### &amp;#128274; OAuth Required &amp;#10024; Extended Info &amp;#127898; Filters  Returns all movies with a DVD release date during the time period specified.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.CalendarsApi();
let startDate = "2014-09-01"; // String | Start the calendar on this date.
let days = 7; // Number | Number of days to display.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getDVDReleases(startDate, days, opts, (error, data, response) => {
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
 **startDate** | **String**| Start the calendar on this date. | 
 **days** | **Number**| Number of days to display. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMovies

> getMovies(startDate, days, opts)

Get movies

#### &amp;#128274; OAuth Required &amp;#10024; Extended Info &amp;#127898; Filters  Returns all movies with a release date during the time period specified.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.CalendarsApi();
let startDate = "2014-09-01"; // String | Start the calendar on this date.
let days = 7; // Number | Number of days to display.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getMovies(startDate, days, opts, (error, data, response) => {
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
 **startDate** | **String**| Start the calendar on this date. | 
 **days** | **Number**| Number of days to display. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNewShows

> getNewShows(startDate, days, opts)

Get new shows

#### &amp;#128274; OAuth Required &amp;#10024; Extended Info &amp;#127898; Filters  Returns all new show premieres (season 1, episode 1) airing during the time period specified.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.CalendarsApi();
let startDate = "2014-09-01"; // String | Start the calendar on this date.
let days = 7; // Number | Number of days to display.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getNewShows(startDate, days, opts, (error, data, response) => {
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
 **startDate** | **String**| Start the calendar on this date. | 
 **days** | **Number**| Number of days to display. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSeasonPremieres

> getSeasonPremieres(startDate, days, opts)

Get season premieres

#### &amp;#128274; OAuth Required &amp;#10024; Extended Info &amp;#127898; Filters  Returns all show premieres (any season, episode 1) airing during the time period specified.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.CalendarsApi();
let startDate = "2014-09-01"; // String | Start the calendar on this date.
let days = 7; // Number | Number of days to display.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getSeasonPremieres(startDate, days, opts, (error, data, response) => {
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
 **startDate** | **String**| Start the calendar on this date. | 
 **days** | **Number**| Number of days to display. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getShows

> getShows(startDate, days, opts)

Get shows

#### &amp;#128274; OAuth Required &amp;#10024; Extended Info &amp;#127898; Filters  Returns all shows airing during the time period specified.

### Example

```javascript
import TraktApi from 'trakt_api';
let defaultClient = TraktApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TraktApi.CalendarsApi();
let startDate = "2014-09-01"; // String | Start the calendar on this date.
let days = 7; // Number | Number of days to display.
let opts = {
  'traktApiVersion': "2", // String | e.g. 2
  'traktApiKey': "[client_id]" // String | e.g. [client_id]
};
apiInstance.getShows(startDate, days, opts, (error, data, response) => {
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
 **startDate** | **String**| Start the calendar on this date. | 
 **days** | **Number**| Number of days to display. | 
 **traktApiVersion** | **String**| e.g. 2 | [optional] 
 **traktApiKey** | **String**| e.g. [client_id] | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

