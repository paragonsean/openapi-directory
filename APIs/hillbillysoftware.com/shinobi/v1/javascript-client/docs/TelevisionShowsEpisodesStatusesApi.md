# Shinobiapi.TelevisionShowsEpisodesStatusesApi

All URIs are relative to *https://api.hillbillysoftware.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addTVShowPost**](TelevisionShowsEpisodesStatusesApi.md#addTVShowPost) | **POST** /AddTVShow | Add new show to database
[**episodesByIDGet**](TelevisionShowsEpisodesStatusesApi.md#episodesByIDGet) | **GET** /Episodes/ByID/{AccessToken}/{ID} | Gets all episodes for selected ID
[**episodesBySeasonGet**](TelevisionShowsEpisodesStatusesApi.md#episodesBySeasonGet) | **GET** /Episodes/BySeason/{AccessToken}/{ID}/{Season} | Gets list of episodes for specified imdbID and Season number
[**episodesGet**](TelevisionShowsEpisodesStatusesApi.md#episodesGet) | **GET** /Episodes/ByShowName/{AccessToken}/{Showname} | Gets all episodes for selected show
[**episodesLastAvailableSeasonGet**](TelevisionShowsEpisodesStatusesApi.md#episodesLastAvailableSeasonGet) | **GET** /Episodes/LatestSeason/{AccessToken}/{ID} | Returns last available season number in database, based on passed imdbID
[**episodesLastAvailableSeasonbyNameGet**](TelevisionShowsEpisodesStatusesApi.md#episodesLastAvailableSeasonbyNameGet) | **GET** /Episodes/LatestSeason/Show/{AccessToken}/{Name} | Gets latest season number based on show name
[**episodesSeasonCountGet**](TelevisionShowsEpisodesStatusesApi.md#episodesSeasonCountGet) | **GET** /Episodes/SeasonCount/{AccessToken}/{ID} | Returns number of available seasons and episodes
[**showStatusGet**](TelevisionShowsEpisodesStatusesApi.md#showStatusGet) | **GET** /Status/{AccessToken}/{Query} | Returns status of queried show (query can be IMDB, TVDB, or showname)
[**tVShowByNameGet**](TelevisionShowsEpisodesStatusesApi.md#tVShowByNameGet) | **GET** /TV/ByName/{AccessToken}/{Query} | Returns results based on query, result set limited to 5 records
[**tVShowIDGet**](TelevisionShowsEpisodesStatusesApi.md#tVShowIDGet) | **GET** /TV/ByID/{accesstoken}/{imdbID} | Returns TVShow information based on IMDBid



## addTVShowPost

> PostResult addTVShowPost(value)

Add new show to database

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.TelevisionShowsEpisodesStatusesApi();
let value = new Shinobiapi.TVInformationPost(); // TVInformationPost | 
apiInstance.addTVShowPost(value, (error, data, response) => {
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
 **value** | [**TVInformationPost**](TVInformationPost.md)|  | 

### Return type

[**PostResult**](PostResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## episodesByIDGet

> [Episode] episodesByIDGet(accessToken, ID)

Gets all episodes for selected ID

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.TelevisionShowsEpisodesStatusesApi();
let accessToken = "accessToken_example"; // String | 
let ID = "ID_example"; // String | imdbID
apiInstance.episodesByIDGet(accessToken, ID, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **ID** | **String**| imdbID | 

### Return type

[**[Episode]**](Episode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## episodesBySeasonGet

> [Episode] episodesBySeasonGet(accessToken, ID, season)

Gets list of episodes for specified imdbID and Season number

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.TelevisionShowsEpisodesStatusesApi();
let accessToken = "accessToken_example"; // String | 
let ID = "ID_example"; // String | imdbID
let season = "season_example"; // String | Season number
apiInstance.episodesBySeasonGet(accessToken, ID, season, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **ID** | **String**| imdbID | 
 **season** | **String**| Season number | 

### Return type

[**[Episode]**](Episode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## episodesGet

> [Episode] episodesGet(accessToken, showname)

Gets all episodes for selected show

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.TelevisionShowsEpisodesStatusesApi();
let accessToken = "accessToken_example"; // String | 
let showname = "showname_example"; // String | 
apiInstance.episodesGet(accessToken, showname, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **showname** | **String**|  | 

### Return type

[**[Episode]**](Episode.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## episodesLastAvailableSeasonGet

> LastAvailableSeason episodesLastAvailableSeasonGet(accessToken, ID)

Returns last available season number in database, based on passed imdbID

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.TelevisionShowsEpisodesStatusesApi();
let accessToken = "accessToken_example"; // String | 
let ID = "ID_example"; // String | imdbID
apiInstance.episodesLastAvailableSeasonGet(accessToken, ID, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **ID** | **String**| imdbID | 

### Return type

[**LastAvailableSeason**](LastAvailableSeason.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## episodesLastAvailableSeasonbyNameGet

> LastAvailableSeason episodesLastAvailableSeasonbyNameGet(accessToken, name)

Gets latest season number based on show name

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.TelevisionShowsEpisodesStatusesApi();
let accessToken = "accessToken_example"; // String | 
let name = "name_example"; // String | 
apiInstance.episodesLastAvailableSeasonbyNameGet(accessToken, name, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **name** | **String**|  | 

### Return type

[**LastAvailableSeason**](LastAvailableSeason.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## episodesSeasonCountGet

> TVShowSeasons episodesSeasonCountGet(accessToken, ID)

Returns number of available seasons and episodes

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.TelevisionShowsEpisodesStatusesApi();
let accessToken = "accessToken_example"; // String | 
let ID = "ID_example"; // String | imdbID
apiInstance.episodesSeasonCountGet(accessToken, ID, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **ID** | **String**| imdbID | 

### Return type

[**TVShowSeasons**](TVShowSeasons.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## showStatusGet

> [ShowStatus] showStatusGet(accessToken, query)

Returns status of queried show (query can be IMDB, TVDB, or showname)

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.TelevisionShowsEpisodesStatusesApi();
let accessToken = "accessToken_example"; // String | 
let query = "query_example"; // String | Query can be IMDB, TVDB, or Show name
apiInstance.showStatusGet(accessToken, query, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **query** | **String**| Query can be IMDB, TVDB, or Show name | 

### Return type

[**[ShowStatus]**](ShowStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## tVShowByNameGet

> [TVInformation] tVShowByNameGet(accessToken, query)

Returns results based on query, result set limited to 5 records

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.TelevisionShowsEpisodesStatusesApi();
let accessToken = "accessToken_example"; // String | 
let query = "query_example"; // String | 
apiInstance.tVShowByNameGet(accessToken, query, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **query** | **String**|  | 

### Return type

[**[TVInformation]**](TVInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## tVShowIDGet

> TVInformation tVShowIDGet(accesstoken, id, imdbID)

Returns TVShow information based on IMDBid

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.TelevisionShowsEpisodesStatusesApi();
let accesstoken = "accesstoken_example"; // String | 
let id = "id_example"; // String | imdbID of show you want info on
let imdbID = "imdbID_example"; // String | 
apiInstance.tVShowIDGet(accesstoken, id, imdbID, (error, data, response) => {
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
 **accesstoken** | **String**|  | 
 **id** | **String**| imdbID of show you want info on | 
 **imdbID** | **String**|  | 

### Return type

[**TVInformation**](TVInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

