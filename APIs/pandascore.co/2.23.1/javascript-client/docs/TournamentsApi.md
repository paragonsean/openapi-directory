# PandaScoreRestApiForAllVideogames.TournamentsApi

All URIs are relative to *https://api.pandascore.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getTournaments**](TournamentsApi.md#getTournaments) | **GET** /tournaments | List tournaments
[**getTournamentsPast**](TournamentsApi.md#getTournamentsPast) | **GET** /tournaments/past | Get past tournaments
[**getTournamentsRunning**](TournamentsApi.md#getTournamentsRunning) | **GET** /tournaments/running | Get running tournaments
[**getTournamentsTournamentIdOrSlug**](TournamentsApi.md#getTournamentsTournamentIdOrSlug) | **GET** /tournaments/{tournament_id_or_slug} | Get a tournament
[**getTournamentsTournamentIdOrSlugBrackets**](TournamentsApi.md#getTournamentsTournamentIdOrSlugBrackets) | **GET** /tournaments/{tournament_id_or_slug}/brackets | Get a tournament&#39;s brackets
[**getTournamentsTournamentIdOrSlugMatches**](TournamentsApi.md#getTournamentsTournamentIdOrSlugMatches) | **GET** /tournaments/{tournament_id_or_slug}/matches | Get matches for tournament
[**getTournamentsTournamentIdOrSlugPlayers**](TournamentsApi.md#getTournamentsTournamentIdOrSlugPlayers) | **GET** /tournaments/{tournament_id_or_slug}/players | Get players for a tournament
[**getTournamentsTournamentIdOrSlugRosters**](TournamentsApi.md#getTournamentsTournamentIdOrSlugRosters) | **GET** /tournaments/{tournament_id_or_slug}/rosters | Get rosters for a tournament
[**getTournamentsTournamentIdOrSlugStandings**](TournamentsApi.md#getTournamentsTournamentIdOrSlugStandings) | **GET** /tournaments/{tournament_id_or_slug}/standings | Get tournament standings
[**getTournamentsTournamentIdOrSlugTeams**](TournamentsApi.md#getTournamentsTournamentIdOrSlugTeams) | **GET** /tournaments/{tournament_id_or_slug}/teams | Get teams for a tournament
[**getTournamentsUpcoming**](TournamentsApi.md#getTournamentsUpcoming) | **GET** /tournaments/upcoming | Get upcoming tournaments



## getTournaments

> [ShortTournament] getTournaments(opts)

List tournaments

List tournaments

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

let apiInstance = new PandaScoreRestApiForAllVideogames.TournamentsApi();
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverShortTournaments(), // FilterOverShortTournaments | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverShortTournaments(), // SearchOverShortTournaments | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverShortTournaments(), // RangeOverShortTournaments | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getTournaments(opts, (error, data, response) => {
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


## getTournamentsPast

> [ShortTournament] getTournamentsPast(opts)

Get past tournaments

List past tournaments

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

let apiInstance = new PandaScoreRestApiForAllVideogames.TournamentsApi();
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverShortTournaments(), // FilterOverShortTournaments | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverShortTournaments(), // SearchOverShortTournaments | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverShortTournaments(), // RangeOverShortTournaments | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getTournamentsPast(opts, (error, data, response) => {
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


## getTournamentsRunning

> [ShortTournament] getTournamentsRunning(opts)

Get running tournaments

List currently running tournaments

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

let apiInstance = new PandaScoreRestApiForAllVideogames.TournamentsApi();
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverShortTournaments(), // FilterOverShortTournaments | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverShortTournaments(), // SearchOverShortTournaments | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverShortTournaments(), // RangeOverShortTournaments | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getTournamentsRunning(opts, (error, data, response) => {
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


## getTournamentsTournamentIdOrSlug

> Tournament getTournamentsTournamentIdOrSlug(tournamentIdOrSlug)

Get a tournament

Get a single tournament by ID or by slug

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

let apiInstance = new PandaScoreRestApiForAllVideogames.TournamentsApi();
let tournamentIdOrSlug = new PandaScoreRestApiForAllVideogames.TournamentIDOrSlug(); // TournamentIDOrSlug | A tournament ID or slug
apiInstance.getTournamentsTournamentIdOrSlug(tournamentIdOrSlug, (error, data, response) => {
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
 **tournamentIdOrSlug** | [**TournamentIDOrSlug**](.md)| A tournament ID or slug | 

### Return type

[**Tournament**](Tournament.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTournamentsTournamentIdOrSlugBrackets

> [Bracket] getTournamentsTournamentIdOrSlugBrackets(tournamentIdOrSlug, opts)

Get a tournament&#39;s brackets

Get the brackets of the given tournament

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

let apiInstance = new PandaScoreRestApiForAllVideogames.TournamentsApi();
let tournamentIdOrSlug = new PandaScoreRestApiForAllVideogames.TournamentIDOrSlug(); // TournamentIDOrSlug | A tournament ID or slug
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverBrackets(), // FilterOverBrackets | Options to filter results. String fields are case sensitive
  'range': new PandaScoreRestApiForAllVideogames.RangeOverBrackets(), // RangeOverBrackets | Options to select results within ranges
  'sort': ["null"], // [String] | Options to sort results
  'search': new PandaScoreRestApiForAllVideogames.SearchOverBrackets(), // SearchOverBrackets | Options to search results
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getTournamentsTournamentIdOrSlugBrackets(tournamentIdOrSlug, opts, (error, data, response) => {
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
 **tournamentIdOrSlug** | [**TournamentIDOrSlug**](.md)| A tournament ID or slug | 
 **filter** | [**FilterOverBrackets**](.md)| Options to filter results. String fields are case sensitive | [optional] 
 **range** | [**RangeOverBrackets**](.md)| Options to select results within ranges | [optional] 
 **sort** | [**[String]**](String.md)| Options to sort results | [optional] 
 **search** | [**SearchOverBrackets**](.md)| Options to search results | [optional] 
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]

### Return type

[**[Bracket]**](Bracket.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTournamentsTournamentIdOrSlugMatches

> [Match] getTournamentsTournamentIdOrSlugMatches(tournamentIdOrSlug, opts)

Get matches for tournament

List matches for the given tournament

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

let apiInstance = new PandaScoreRestApiForAllVideogames.TournamentsApi();
let tournamentIdOrSlug = new PandaScoreRestApiForAllVideogames.TournamentIDOrSlug(); // TournamentIDOrSlug | A tournament ID or slug
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverMatches(), // FilterOverMatches | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverMatches(), // SearchOverMatches | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverMatches(), // RangeOverMatches | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getTournamentsTournamentIdOrSlugMatches(tournamentIdOrSlug, opts, (error, data, response) => {
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
 **tournamentIdOrSlug** | [**TournamentIDOrSlug**](.md)| A tournament ID or slug | 
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


## getTournamentsTournamentIdOrSlugPlayers

> [Player] getTournamentsTournamentIdOrSlugPlayers(tournamentIdOrSlug, opts)

Get players for a tournament

List players for the given tournament

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

let apiInstance = new PandaScoreRestApiForAllVideogames.TournamentsApi();
let tournamentIdOrSlug = "tournamentIdOrSlug_example"; // String | Automatically added
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverPlayers(), // FilterOverPlayers | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverPlayers(), // SearchOverPlayers | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverPlayers(), // RangeOverPlayers | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getTournamentsTournamentIdOrSlugPlayers(tournamentIdOrSlug, opts, (error, data, response) => {
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
 **tournamentIdOrSlug** | **String**| Automatically added | 
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


## getTournamentsTournamentIdOrSlugRosters

> TournamentRosters getTournamentsTournamentIdOrSlugRosters(tournamentIdOrSlug)

Get rosters for a tournament

List participants (player or team) for a given tournament.

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

let apiInstance = new PandaScoreRestApiForAllVideogames.TournamentsApi();
let tournamentIdOrSlug = new PandaScoreRestApiForAllVideogames.TournamentIDOrSlug(); // TournamentIDOrSlug | A tournament ID or slug
apiInstance.getTournamentsTournamentIdOrSlugRosters(tournamentIdOrSlug, (error, data, response) => {
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
 **tournamentIdOrSlug** | [**TournamentIDOrSlug**](.md)| A tournament ID or slug | 

### Return type

[**TournamentRosters**](TournamentRosters.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTournamentsTournamentIdOrSlugStandings

> [Standing] getTournamentsTournamentIdOrSlugStandings(tournamentIdOrSlug, opts)

Get tournament standings

Get the current standings for a given tournament

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

let apiInstance = new PandaScoreRestApiForAllVideogames.TournamentsApi();
let tournamentIdOrSlug = new PandaScoreRestApiForAllVideogames.TournamentIDOrSlug(); // TournamentIDOrSlug | A tournament ID or slug
let opts = {
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getTournamentsTournamentIdOrSlugStandings(tournamentIdOrSlug, opts, (error, data, response) => {
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
 **tournamentIdOrSlug** | [**TournamentIDOrSlug**](.md)| A tournament ID or slug | 
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]

### Return type

[**[Standing]**](Standing.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTournamentsTournamentIdOrSlugTeams

> [Team] getTournamentsTournamentIdOrSlugTeams(tournamentIdOrSlug, opts)

Get teams for a tournament

List teams for the given tournament

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

let apiInstance = new PandaScoreRestApiForAllVideogames.TournamentsApi();
let tournamentIdOrSlug = new PandaScoreRestApiForAllVideogames.TournamentIDOrSlug(); // TournamentIDOrSlug | A tournament ID or slug
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverTeams(), // FilterOverTeams | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverTeams(), // SearchOverTeams | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverTeams(), // RangeOverTeams | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getTournamentsTournamentIdOrSlugTeams(tournamentIdOrSlug, opts, (error, data, response) => {
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
 **tournamentIdOrSlug** | [**TournamentIDOrSlug**](.md)| A tournament ID or slug | 
 **filter** | [**FilterOverTeams**](.md)| Options to filter results. String fields are case sensitive | [optional] 
 **search** | [**SearchOverTeams**](.md)| Options to search results | [optional] 
 **sort** | [**[String]**](String.md)| Options to sort results | [optional] 
 **range** | [**RangeOverTeams**](.md)| Options to select results within ranges | [optional] 
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]

### Return type

[**[Team]**](Team.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTournamentsUpcoming

> [ShortTournament] getTournamentsUpcoming(opts)

Get upcoming tournaments

List upcoming tournaments

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

let apiInstance = new PandaScoreRestApiForAllVideogames.TournamentsApi();
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverShortTournaments(), // FilterOverShortTournaments | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverShortTournaments(), // SearchOverShortTournaments | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverShortTournaments(), // RangeOverShortTournaments | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getTournamentsUpcoming(opts, (error, data, response) => {
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

