# PandaScoreRestApiForAllVideogames.SeriesApi

All URIs are relative to *https://api.pandascore.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSeries**](SeriesApi.md#getSeries) | **GET** /series | List series
[**getSeriesPast**](SeriesApi.md#getSeriesPast) | **GET** /series/past | Get past series
[**getSeriesRunning**](SeriesApi.md#getSeriesRunning) | **GET** /series/running | Get running series
[**getSeriesSerieIdOrSlug**](SeriesApi.md#getSeriesSerieIdOrSlug) | **GET** /series/{serie_id_or_slug} | Get a serie
[**getSeriesSerieIdOrSlugMatches**](SeriesApi.md#getSeriesSerieIdOrSlugMatches) | **GET** /series/{serie_id_or_slug}/matches | Get matches for a serie
[**getSeriesSerieIdOrSlugMatchesPast**](SeriesApi.md#getSeriesSerieIdOrSlugMatchesPast) | **GET** /series/{serie_id_or_slug}/matches/past | Get past matches for serie
[**getSeriesSerieIdOrSlugMatchesRunning**](SeriesApi.md#getSeriesSerieIdOrSlugMatchesRunning) | **GET** /series/{serie_id_or_slug}/matches/running | Get running matches for serie
[**getSeriesSerieIdOrSlugMatchesUpcoming**](SeriesApi.md#getSeriesSerieIdOrSlugMatchesUpcoming) | **GET** /series/{serie_id_or_slug}/matches/upcoming | Get upcoming matches for serie
[**getSeriesSerieIdOrSlugPlayers**](SeriesApi.md#getSeriesSerieIdOrSlugPlayers) | **GET** /series/{serie_id_or_slug}/players | Get players for a serie
[**getSeriesSerieIdOrSlugTournaments**](SeriesApi.md#getSeriesSerieIdOrSlugTournaments) | **GET** /series/{serie_id_or_slug}/tournaments | Get tournaments for a serie
[**getSeriesUpcoming**](SeriesApi.md#getSeriesUpcoming) | **GET** /series/upcoming | Get upcoming series



## getSeries

> [Serie] getSeries(opts)

List series

List series

### Example

```javascript
import PandaScoreRestApiForAllVideogames from 'panda_score_rest_api_for_all_videogames';
let defaultClient = PandaScoreRestApiForAllVideogames.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"
// Configure API key authorization: QueryToken
let QueryToken = defaultClient.authentications['QueryToken'];
QueryToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryToken.apiKeyPrefix = 'Token';

let apiInstance = new PandaScoreRestApiForAllVideogames.SeriesApi();
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverSeries(), // FilterOverSeries | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverSeries(), // SearchOverSeries | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverSeries(), // RangeOverSeries | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getSeries(opts, (error, data, response) => {
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
 **filter** | [**FilterOverSeries**](.md)| Options to filter results. String fields are case sensitive | [optional] 
 **search** | [**SearchOverSeries**](.md)| Options to search results | [optional] 
 **sort** | [**[String]**](String.md)| Options to sort results | [optional] 
 **range** | [**RangeOverSeries**](.md)| Options to select results within ranges | [optional] 
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]

### Return type

[**[Serie]**](Serie.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSeriesPast

> [Serie] getSeriesPast(opts)

Get past series

List past series

### Example

```javascript
import PandaScoreRestApiForAllVideogames from 'panda_score_rest_api_for_all_videogames';
let defaultClient = PandaScoreRestApiForAllVideogames.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"
// Configure API key authorization: QueryToken
let QueryToken = defaultClient.authentications['QueryToken'];
QueryToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryToken.apiKeyPrefix = 'Token';

let apiInstance = new PandaScoreRestApiForAllVideogames.SeriesApi();
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverSeries(), // FilterOverSeries | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverSeries(), // SearchOverSeries | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverSeries(), // RangeOverSeries | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getSeriesPast(opts, (error, data, response) => {
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
 **filter** | [**FilterOverSeries**](.md)| Options to filter results. String fields are case sensitive | [optional] 
 **search** | [**SearchOverSeries**](.md)| Options to search results | [optional] 
 **sort** | [**[String]**](String.md)| Options to sort results | [optional] 
 **range** | [**RangeOverSeries**](.md)| Options to select results within ranges | [optional] 
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]

### Return type

[**[Serie]**](Serie.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSeriesRunning

> [Serie] getSeriesRunning(opts)

Get running series

List currently running series

### Example

```javascript
import PandaScoreRestApiForAllVideogames from 'panda_score_rest_api_for_all_videogames';
let defaultClient = PandaScoreRestApiForAllVideogames.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"
// Configure API key authorization: QueryToken
let QueryToken = defaultClient.authentications['QueryToken'];
QueryToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryToken.apiKeyPrefix = 'Token';

let apiInstance = new PandaScoreRestApiForAllVideogames.SeriesApi();
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverSeries(), // FilterOverSeries | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverSeries(), // SearchOverSeries | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverSeries(), // RangeOverSeries | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getSeriesRunning(opts, (error, data, response) => {
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
 **filter** | [**FilterOverSeries**](.md)| Options to filter results. String fields are case sensitive | [optional] 
 **search** | [**SearchOverSeries**](.md)| Options to search results | [optional] 
 **sort** | [**[String]**](String.md)| Options to sort results | [optional] 
 **range** | [**RangeOverSeries**](.md)| Options to select results within ranges | [optional] 
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]

### Return type

[**[Serie]**](Serie.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSeriesSerieIdOrSlug

> Serie getSeriesSerieIdOrSlug(serieIdOrSlug)

Get a serie

Get a single serie by ID or by slug

### Example

```javascript
import PandaScoreRestApiForAllVideogames from 'panda_score_rest_api_for_all_videogames';
let defaultClient = PandaScoreRestApiForAllVideogames.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"
// Configure API key authorization: QueryToken
let QueryToken = defaultClient.authentications['QueryToken'];
QueryToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryToken.apiKeyPrefix = 'Token';

let apiInstance = new PandaScoreRestApiForAllVideogames.SeriesApi();
let serieIdOrSlug = new PandaScoreRestApiForAllVideogames.SerieIDOrSlug(); // SerieIDOrSlug | A serie ID or slug
apiInstance.getSeriesSerieIdOrSlug(serieIdOrSlug, (error, data, response) => {
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
 **serieIdOrSlug** | [**SerieIDOrSlug**](.md)| A serie ID or slug | 

### Return type

[**Serie**](Serie.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSeriesSerieIdOrSlugMatches

> [Match] getSeriesSerieIdOrSlugMatches(serieIdOrSlug, opts)

Get matches for a serie

List matches of the given serie

### Example

```javascript
import PandaScoreRestApiForAllVideogames from 'panda_score_rest_api_for_all_videogames';
let defaultClient = PandaScoreRestApiForAllVideogames.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"
// Configure API key authorization: QueryToken
let QueryToken = defaultClient.authentications['QueryToken'];
QueryToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryToken.apiKeyPrefix = 'Token';

let apiInstance = new PandaScoreRestApiForAllVideogames.SeriesApi();
let serieIdOrSlug = new PandaScoreRestApiForAllVideogames.SerieIDOrSlug(); // SerieIDOrSlug | A serie ID or slug
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverMatches(), // FilterOverMatches | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverMatches(), // SearchOverMatches | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverMatches(), // RangeOverMatches | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getSeriesSerieIdOrSlugMatches(serieIdOrSlug, opts, (error, data, response) => {
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
 **serieIdOrSlug** | [**SerieIDOrSlug**](.md)| A serie ID or slug | 
 **filter** | [**FilterOverMatches**](.md)| Options to filter results. String fields are case sensitive | [optional] 
 **search** | [**SearchOverMatches**](.md)| Options to search results | [optional] 
 **sort** | [**[String]**](String.md)| Options to sort results | [optional] 
 **range** | [**RangeOverMatches**](.md)| Options to select results within ranges | [optional] 
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]

### Return type

[**[Match]**](Match.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSeriesSerieIdOrSlugMatchesPast

> [Match] getSeriesSerieIdOrSlugMatchesPast(serieIdOrSlug, opts)

Get past matches for serie

List past matches for the given serie

### Example

```javascript
import PandaScoreRestApiForAllVideogames from 'panda_score_rest_api_for_all_videogames';
let defaultClient = PandaScoreRestApiForAllVideogames.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"
// Configure API key authorization: QueryToken
let QueryToken = defaultClient.authentications['QueryToken'];
QueryToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryToken.apiKeyPrefix = 'Token';

let apiInstance = new PandaScoreRestApiForAllVideogames.SeriesApi();
let serieIdOrSlug = new PandaScoreRestApiForAllVideogames.SerieIDOrSlug(); // SerieIDOrSlug | A serie ID or slug
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverMatches(), // FilterOverMatches | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverMatches(), // SearchOverMatches | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverMatches(), // RangeOverMatches | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getSeriesSerieIdOrSlugMatchesPast(serieIdOrSlug, opts, (error, data, response) => {
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
 **serieIdOrSlug** | [**SerieIDOrSlug**](.md)| A serie ID or slug | 
 **filter** | [**FilterOverMatches**](.md)| Options to filter results. String fields are case sensitive | [optional] 
 **search** | [**SearchOverMatches**](.md)| Options to search results | [optional] 
 **sort** | [**[String]**](String.md)| Options to sort results | [optional] 
 **range** | [**RangeOverMatches**](.md)| Options to select results within ranges | [optional] 
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]

### Return type

[**[Match]**](Match.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSeriesSerieIdOrSlugMatchesRunning

> [Match] getSeriesSerieIdOrSlugMatchesRunning(serieIdOrSlug, opts)

Get running matches for serie

List currently running matches for the given serie

### Example

```javascript
import PandaScoreRestApiForAllVideogames from 'panda_score_rest_api_for_all_videogames';
let defaultClient = PandaScoreRestApiForAllVideogames.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"
// Configure API key authorization: QueryToken
let QueryToken = defaultClient.authentications['QueryToken'];
QueryToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryToken.apiKeyPrefix = 'Token';

let apiInstance = new PandaScoreRestApiForAllVideogames.SeriesApi();
let serieIdOrSlug = new PandaScoreRestApiForAllVideogames.SerieIDOrSlug(); // SerieIDOrSlug | A serie ID or slug
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverMatches(), // FilterOverMatches | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverMatches(), // SearchOverMatches | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverMatches(), // RangeOverMatches | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getSeriesSerieIdOrSlugMatchesRunning(serieIdOrSlug, opts, (error, data, response) => {
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
 **serieIdOrSlug** | [**SerieIDOrSlug**](.md)| A serie ID or slug | 
 **filter** | [**FilterOverMatches**](.md)| Options to filter results. String fields are case sensitive | [optional] 
 **search** | [**SearchOverMatches**](.md)| Options to search results | [optional] 
 **sort** | [**[String]**](String.md)| Options to sort results | [optional] 
 **range** | [**RangeOverMatches**](.md)| Options to select results within ranges | [optional] 
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]

### Return type

[**[Match]**](Match.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSeriesSerieIdOrSlugMatchesUpcoming

> [Match] getSeriesSerieIdOrSlugMatchesUpcoming(serieIdOrSlug, opts)

Get upcoming matches for serie

List upcoming matches for the given serie

### Example

```javascript
import PandaScoreRestApiForAllVideogames from 'panda_score_rest_api_for_all_videogames';
let defaultClient = PandaScoreRestApiForAllVideogames.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"
// Configure API key authorization: QueryToken
let QueryToken = defaultClient.authentications['QueryToken'];
QueryToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryToken.apiKeyPrefix = 'Token';

let apiInstance = new PandaScoreRestApiForAllVideogames.SeriesApi();
let serieIdOrSlug = new PandaScoreRestApiForAllVideogames.SerieIDOrSlug(); // SerieIDOrSlug | A serie ID or slug
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverMatches(), // FilterOverMatches | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverMatches(), // SearchOverMatches | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverMatches(), // RangeOverMatches | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getSeriesSerieIdOrSlugMatchesUpcoming(serieIdOrSlug, opts, (error, data, response) => {
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
 **serieIdOrSlug** | [**SerieIDOrSlug**](.md)| A serie ID or slug | 
 **filter** | [**FilterOverMatches**](.md)| Options to filter results. String fields are case sensitive | [optional] 
 **search** | [**SearchOverMatches**](.md)| Options to search results | [optional] 
 **sort** | [**[String]**](String.md)| Options to sort results | [optional] 
 **range** | [**RangeOverMatches**](.md)| Options to select results within ranges | [optional] 
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]

### Return type

[**[Match]**](Match.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSeriesSerieIdOrSlugPlayers

> [Player] getSeriesSerieIdOrSlugPlayers(serieIdOrSlug, opts)

Get players for a serie

List players for the given serie

### Example

```javascript
import PandaScoreRestApiForAllVideogames from 'panda_score_rest_api_for_all_videogames';
let defaultClient = PandaScoreRestApiForAllVideogames.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"
// Configure API key authorization: QueryToken
let QueryToken = defaultClient.authentications['QueryToken'];
QueryToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryToken.apiKeyPrefix = 'Token';

let apiInstance = new PandaScoreRestApiForAllVideogames.SeriesApi();
let serieIdOrSlug = "serieIdOrSlug_example"; // String | Automatically added
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverPlayers(), // FilterOverPlayers | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverPlayers(), // SearchOverPlayers | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverPlayers(), // RangeOverPlayers | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getSeriesSerieIdOrSlugPlayers(serieIdOrSlug, opts, (error, data, response) => {
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
 **serieIdOrSlug** | **String**| Automatically added | 
 **filter** | [**FilterOverPlayers**](.md)| Options to filter results. String fields are case sensitive | [optional] 
 **search** | [**SearchOverPlayers**](.md)| Options to search results | [optional] 
 **sort** | [**[String]**](String.md)| Options to sort results | [optional] 
 **range** | [**RangeOverPlayers**](.md)| Options to select results within ranges | [optional] 
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]

### Return type

[**[Player]**](Player.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSeriesSerieIdOrSlugTournaments

> [ShortTournament] getSeriesSerieIdOrSlugTournaments(serieIdOrSlug, opts)

Get tournaments for a serie

List tournaments of the given serie

### Example

```javascript
import PandaScoreRestApiForAllVideogames from 'panda_score_rest_api_for_all_videogames';
let defaultClient = PandaScoreRestApiForAllVideogames.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"
// Configure API key authorization: QueryToken
let QueryToken = defaultClient.authentications['QueryToken'];
QueryToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryToken.apiKeyPrefix = 'Token';

let apiInstance = new PandaScoreRestApiForAllVideogames.SeriesApi();
let serieIdOrSlug = new PandaScoreRestApiForAllVideogames.SerieIDOrSlug(); // SerieIDOrSlug | A serie ID or slug
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverShortTournaments(), // FilterOverShortTournaments | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverShortTournaments(), // SearchOverShortTournaments | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverShortTournaments(), // RangeOverShortTournaments | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getSeriesSerieIdOrSlugTournaments(serieIdOrSlug, opts, (error, data, response) => {
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
 **serieIdOrSlug** | [**SerieIDOrSlug**](.md)| A serie ID or slug | 
 **filter** | [**FilterOverShortTournaments**](.md)| Options to filter results. String fields are case sensitive | [optional] 
 **search** | [**SearchOverShortTournaments**](.md)| Options to search results | [optional] 
 **sort** | [**[String]**](String.md)| Options to sort results | [optional] 
 **range** | [**RangeOverShortTournaments**](.md)| Options to select results within ranges | [optional] 
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]

### Return type

[**[ShortTournament]**](ShortTournament.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSeriesUpcoming

> [Serie] getSeriesUpcoming(opts)

Get upcoming series

List upcoming series

### Example

```javascript
import PandaScoreRestApiForAllVideogames from 'panda_score_rest_api_for_all_videogames';
let defaultClient = PandaScoreRestApiForAllVideogames.ApiClient.instance;
// Configure Bearer access token for authorization: BearerToken
let BearerToken = defaultClient.authentications['BearerToken'];
BearerToken.accessToken = "YOUR ACCESS TOKEN"
// Configure API key authorization: QueryToken
let QueryToken = defaultClient.authentications['QueryToken'];
QueryToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryToken.apiKeyPrefix = 'Token';

let apiInstance = new PandaScoreRestApiForAllVideogames.SeriesApi();
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverSeries(), // FilterOverSeries | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverSeries(), // SearchOverSeries | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverSeries(), // RangeOverSeries | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getSeriesUpcoming(opts, (error, data, response) => {
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
 **filter** | [**FilterOverSeries**](.md)| Options to filter results. String fields are case sensitive | [optional] 
 **search** | [**SearchOverSeries**](.md)| Options to search results | [optional] 
 **sort** | [**[String]**](String.md)| Options to sort results | [optional] 
 **range** | [**RangeOverSeries**](.md)| Options to select results within ranges | [optional] 
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]

### Return type

[**[Serie]**](Serie.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

