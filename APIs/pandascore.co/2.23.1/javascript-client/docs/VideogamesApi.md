# PandaScoreRestApiForAllVideogames.VideogamesApi

All URIs are relative to *https://api.pandascore.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getVideogames**](VideogamesApi.md#getVideogames) | **GET** /videogames | List videogames
[**getVideogamesVideogameIdOrSlug**](VideogamesApi.md#getVideogamesVideogameIdOrSlug) | **GET** /videogames/{videogame_id_or_slug} | Get a videogame
[**getVideogamesVideogameIdOrSlugLeagues**](VideogamesApi.md#getVideogamesVideogameIdOrSlugLeagues) | **GET** /videogames/{videogame_id_or_slug}/leagues | 
[**getVideogamesVideogameIdOrSlugSeries**](VideogamesApi.md#getVideogamesVideogameIdOrSlugSeries) | **GET** /videogames/{videogame_id_or_slug}/series | List series for a videogame
[**getVideogamesVideogameIdOrSlugTournaments**](VideogamesApi.md#getVideogamesVideogameIdOrSlugTournaments) | **GET** /videogames/{videogame_id_or_slug}/tournaments | Get tournaments for a videogame
[**getVideogamesVideogameIdOrSlugVersions**](VideogamesApi.md#getVideogamesVideogameIdOrSlugVersions) | **GET** /videogames/{videogame_id_or_slug}/versions | List videogame versions



## getVideogames

> [Videogame] getVideogames(opts)

List videogames

List videogames

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

let apiInstance = new PandaScoreRestApiForAllVideogames.VideogamesApi();
let opts = {
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getVideogames(opts, (error, data, response) => {
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
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]

### Return type

[**[Videogame]**](Videogame.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVideogamesVideogameIdOrSlug

> Videogame getVideogamesVideogameIdOrSlug(videogameIdOrSlug)

Get a videogame

Get a single videogame by ID or by slug

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

let apiInstance = new PandaScoreRestApiForAllVideogames.VideogamesApi();
let videogameIdOrSlug = new PandaScoreRestApiForAllVideogames.VideogameIDOrSlug(); // VideogameIDOrSlug | A videogame ID or slug
apiInstance.getVideogamesVideogameIdOrSlug(videogameIdOrSlug, (error, data, response) => {
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
 **videogameIdOrSlug** | [**VideogameIDOrSlug**](.md)| A videogame ID or slug | 

### Return type

[**Videogame**](Videogame.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVideogamesVideogameIdOrSlugLeagues

> [League] getVideogamesVideogameIdOrSlugLeagues(videogameIdOrSlug, opts)



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

let apiInstance = new PandaScoreRestApiForAllVideogames.VideogamesApi();
let videogameIdOrSlug = new PandaScoreRestApiForAllVideogames.VideogameIDOrSlug(); // VideogameIDOrSlug | A videogame ID or slug
let opts = {
  'search': new PandaScoreRestApiForAllVideogames.SearchOverLeagues(), // SearchOverLeagues | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverLeagues(), // RangeOverLeagues | Options to select results within ranges
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverLeagues(), // FilterOverLeagues | Options to filter results. String fields are case sensitive
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getVideogamesVideogameIdOrSlugLeagues(videogameIdOrSlug, opts, (error, data, response) => {
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
 **videogameIdOrSlug** | [**VideogameIDOrSlug**](.md)| A videogame ID or slug | 
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


## getVideogamesVideogameIdOrSlugSeries

> [Serie] getVideogamesVideogameIdOrSlugSeries(videogameIdOrSlug, opts)

List series for a videogame

List series for the given videogame

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

let apiInstance = new PandaScoreRestApiForAllVideogames.VideogamesApi();
let videogameIdOrSlug = new PandaScoreRestApiForAllVideogames.VideogameIDOrSlug(); // VideogameIDOrSlug | A videogame ID or slug
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverSeries(), // FilterOverSeries | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverSeries(), // SearchOverSeries | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverSeries(), // RangeOverSeries | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getVideogamesVideogameIdOrSlugSeries(videogameIdOrSlug, opts, (error, data, response) => {
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
 **videogameIdOrSlug** | [**VideogameIDOrSlug**](.md)| A videogame ID or slug | 
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


## getVideogamesVideogameIdOrSlugTournaments

> [ShortTournament] getVideogamesVideogameIdOrSlugTournaments(videogameIdOrSlug, opts)

Get tournaments for a videogame

List tournaments of the given videogame

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

let apiInstance = new PandaScoreRestApiForAllVideogames.VideogamesApi();
let videogameIdOrSlug = new PandaScoreRestApiForAllVideogames.VideogameIDOrSlug(); // VideogameIDOrSlug | A videogame ID or slug
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverShortTournaments(), // FilterOverShortTournaments | Options to filter results. String fields are case sensitive
  'range': new PandaScoreRestApiForAllVideogames.RangeOverShortTournaments(), // RangeOverShortTournaments | Options to select results within ranges
  'sort': ["null"], // [String] | Options to sort results
  'search': new PandaScoreRestApiForAllVideogames.SearchOverShortTournaments(), // SearchOverShortTournaments | Options to search results
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getVideogamesVideogameIdOrSlugTournaments(videogameIdOrSlug, opts, (error, data, response) => {
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
 **videogameIdOrSlug** | [**VideogameIDOrSlug**](.md)| A videogame ID or slug | 
 **filter** | [**FilterOverShortTournaments**](.md)| Options to filter results. String fields are case sensitive | [optional] 
 **range** | [**RangeOverShortTournaments**](.md)| Options to select results within ranges | [optional] 
 **sort** | [**[String]**](String.md)| Options to sort results | [optional] 
 **search** | [**SearchOverShortTournaments**](.md)| Options to search results | [optional] 
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]

### Return type

[**[ShortTournament]**](ShortTournament.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVideogamesVideogameIdOrSlugVersions

> [ShortVideogameVersion] getVideogamesVideogameIdOrSlugVersions(videogameIdOrSlug, opts)

List videogame versions

List available versions for a given videogame

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

let apiInstance = new PandaScoreRestApiForAllVideogames.VideogamesApi();
let videogameIdOrSlug = new PandaScoreRestApiForAllVideogames.VideogameIDOrSlug(); // VideogameIDOrSlug | A videogame ID or slug
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverShortVideogameVersions(), // FilterOverShortVideogameVersions | Options to filter results. String fields are case sensitive
  'range': new PandaScoreRestApiForAllVideogames.RangeOverShortVideogameVersions(), // RangeOverShortVideogameVersions | Options to select results within ranges
  'sort': ["null"], // [String] | Options to sort results
  'search': new PandaScoreRestApiForAllVideogames.SearchOverShortVideogameVersions(), // SearchOverShortVideogameVersions | Options to search results
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getVideogamesVideogameIdOrSlugVersions(videogameIdOrSlug, opts, (error, data, response) => {
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
 **videogameIdOrSlug** | [**VideogameIDOrSlug**](.md)| A videogame ID or slug | 
 **filter** | [**FilterOverShortVideogameVersions**](.md)| Options to filter results. String fields are case sensitive | [optional] 
 **range** | [**RangeOverShortVideogameVersions**](.md)| Options to select results within ranges | [optional] 
 **sort** | [**[String]**](String.md)| Options to sort results | [optional] 
 **search** | [**SearchOverShortVideogameVersions**](.md)| Options to search results | [optional] 
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]

### Return type

[**[ShortVideogameVersion]**](ShortVideogameVersion.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

