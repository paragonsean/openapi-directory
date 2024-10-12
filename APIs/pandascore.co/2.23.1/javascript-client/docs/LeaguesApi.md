# PandaScoreRestApiForAllVideogames.LeaguesApi

All URIs are relative to *https://api.pandascore.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLeagues**](LeaguesApi.md#getLeagues) | **GET** /leagues | List leagues
[**getLeaguesLeagueIdOrSlug**](LeaguesApi.md#getLeaguesLeagueIdOrSlug) | **GET** /leagues/{league_id_or_slug} | Get a league
[**getLeaguesLeagueIdOrSlugMatches**](LeaguesApi.md#getLeaguesLeagueIdOrSlugMatches) | **GET** /leagues/{league_id_or_slug}/matches | Get matches for a league
[**getLeaguesLeagueIdOrSlugMatchesPast**](LeaguesApi.md#getLeaguesLeagueIdOrSlugMatchesPast) | **GET** /leagues/{league_id_or_slug}/matches/past | Get past matches for league
[**getLeaguesLeagueIdOrSlugMatchesRunning**](LeaguesApi.md#getLeaguesLeagueIdOrSlugMatchesRunning) | **GET** /leagues/{league_id_or_slug}/matches/running | Get running matches for league
[**getLeaguesLeagueIdOrSlugMatchesUpcoming**](LeaguesApi.md#getLeaguesLeagueIdOrSlugMatchesUpcoming) | **GET** /leagues/{league_id_or_slug}/matches/upcoming | Get upcoming matches for league
[**getLeaguesLeagueIdOrSlugSeries**](LeaguesApi.md#getLeaguesLeagueIdOrSlugSeries) | **GET** /leagues/{league_id_or_slug}/series | List series of a league
[**getLeaguesLeagueIdOrSlugTournaments**](LeaguesApi.md#getLeaguesLeagueIdOrSlugTournaments) | **GET** /leagues/{league_id_or_slug}/tournaments | Get tournaments for a league



## getLeagues

> [League] getLeagues(opts)

List leagues

List leagues

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

let apiInstance = new PandaScoreRestApiForAllVideogames.LeaguesApi();
let opts = {
  'search': new PandaScoreRestApiForAllVideogames.SearchOverLeagues(), // SearchOverLeagues | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverLeagues(), // RangeOverLeagues | Options to select results within ranges
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverLeagues(), // FilterOverLeagues | Options to filter results. String fields are case sensitive
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getLeagues(opts, (error, data, response) => {
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
 **search** | [**SearchOverLeagues**](.md)| Options to search results | [optional] 
 **sort** | [**[String]**](String.md)| Options to sort results | [optional] 
 **range** | [**RangeOverLeagues**](.md)| Options to select results within ranges | [optional] 
 **filter** | [**FilterOverLeagues**](.md)| Options to filter results. String fields are case sensitive | [optional] 
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]

### Return type

[**[League]**](League.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLeaguesLeagueIdOrSlug

> League getLeaguesLeagueIdOrSlug(leagueIdOrSlug)

Get a league

Get a single league by ID or by slug

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

let apiInstance = new PandaScoreRestApiForAllVideogames.LeaguesApi();
let leagueIdOrSlug = new PandaScoreRestApiForAllVideogames.LeagueIDOrSlug(); // LeagueIDOrSlug | A league ID or slug
apiInstance.getLeaguesLeagueIdOrSlug(leagueIdOrSlug, (error, data, response) => {
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
 **leagueIdOrSlug** | [**LeagueIDOrSlug**](.md)| A league ID or slug | 

### Return type

[**League**](League.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLeaguesLeagueIdOrSlugMatches

> [Match] getLeaguesLeagueIdOrSlugMatches(leagueIdOrSlug, opts)

Get matches for a league

List matches of the given league

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

let apiInstance = new PandaScoreRestApiForAllVideogames.LeaguesApi();
let leagueIdOrSlug = new PandaScoreRestApiForAllVideogames.LeagueIDOrSlug(); // LeagueIDOrSlug | A league ID or slug
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverMatches(), // FilterOverMatches | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverMatches(), // SearchOverMatches | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverMatches(), // RangeOverMatches | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getLeaguesLeagueIdOrSlugMatches(leagueIdOrSlug, opts, (error, data, response) => {
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
 **leagueIdOrSlug** | [**LeagueIDOrSlug**](.md)| A league ID or slug | 
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


## getLeaguesLeagueIdOrSlugMatchesPast

> [Match] getLeaguesLeagueIdOrSlugMatchesPast(leagueIdOrSlug, opts)

Get past matches for league

List past matches for the given league

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

let apiInstance = new PandaScoreRestApiForAllVideogames.LeaguesApi();
let leagueIdOrSlug = new PandaScoreRestApiForAllVideogames.LeagueIDOrSlug(); // LeagueIDOrSlug | A league ID or slug
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverMatches(), // FilterOverMatches | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverMatches(), // SearchOverMatches | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverMatches(), // RangeOverMatches | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getLeaguesLeagueIdOrSlugMatchesPast(leagueIdOrSlug, opts, (error, data, response) => {
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
 **leagueIdOrSlug** | [**LeagueIDOrSlug**](.md)| A league ID or slug | 
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


## getLeaguesLeagueIdOrSlugMatchesRunning

> [Match] getLeaguesLeagueIdOrSlugMatchesRunning(leagueIdOrSlug, opts)

Get running matches for league

List currently running matches for the given league

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

let apiInstance = new PandaScoreRestApiForAllVideogames.LeaguesApi();
let leagueIdOrSlug = new PandaScoreRestApiForAllVideogames.LeagueIDOrSlug(); // LeagueIDOrSlug | A league ID or slug
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverMatches(), // FilterOverMatches | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverMatches(), // SearchOverMatches | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverMatches(), // RangeOverMatches | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getLeaguesLeagueIdOrSlugMatchesRunning(leagueIdOrSlug, opts, (error, data, response) => {
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
 **leagueIdOrSlug** | [**LeagueIDOrSlug**](.md)| A league ID or slug | 
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


## getLeaguesLeagueIdOrSlugMatchesUpcoming

> [Match] getLeaguesLeagueIdOrSlugMatchesUpcoming(leagueIdOrSlug, opts)

Get upcoming matches for league

List upcoming matches for the given league

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

let apiInstance = new PandaScoreRestApiForAllVideogames.LeaguesApi();
let leagueIdOrSlug = new PandaScoreRestApiForAllVideogames.LeagueIDOrSlug(); // LeagueIDOrSlug | A league ID or slug
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverMatches(), // FilterOverMatches | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverMatches(), // SearchOverMatches | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverMatches(), // RangeOverMatches | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getLeaguesLeagueIdOrSlugMatchesUpcoming(leagueIdOrSlug, opts, (error, data, response) => {
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
 **leagueIdOrSlug** | [**LeagueIDOrSlug**](.md)| A league ID or slug | 
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


## getLeaguesLeagueIdOrSlugSeries

> [Serie] getLeaguesLeagueIdOrSlugSeries(leagueIdOrSlug, opts)

List series of a league

List series for the given league

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

let apiInstance = new PandaScoreRestApiForAllVideogames.LeaguesApi();
let leagueIdOrSlug = new PandaScoreRestApiForAllVideogames.LeagueIDOrSlug(); // LeagueIDOrSlug | A league ID or slug
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverSeries(), // FilterOverSeries | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverSeries(), // SearchOverSeries | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverSeries(), // RangeOverSeries | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getLeaguesLeagueIdOrSlugSeries(leagueIdOrSlug, opts, (error, data, response) => {
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
 **leagueIdOrSlug** | [**LeagueIDOrSlug**](.md)| A league ID or slug | 
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


## getLeaguesLeagueIdOrSlugTournaments

> [ShortTournament] getLeaguesLeagueIdOrSlugTournaments(leagueIdOrSlug, opts)

Get tournaments for a league

List tournaments of the given league

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

let apiInstance = new PandaScoreRestApiForAllVideogames.LeaguesApi();
let leagueIdOrSlug = new PandaScoreRestApiForAllVideogames.LeagueIDOrSlug(); // LeagueIDOrSlug | A league ID or slug
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverShortTournaments(), // FilterOverShortTournaments | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverShortTournaments(), // SearchOverShortTournaments | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverShortTournaments(), // RangeOverShortTournaments | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getLeaguesLeagueIdOrSlugTournaments(leagueIdOrSlug, opts, (error, data, response) => {
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
 **leagueIdOrSlug** | [**LeagueIDOrSlug**](.md)| A league ID or slug | 
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

