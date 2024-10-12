# PandaScoreRestApiForAllVideogames.TeamsApi

All URIs are relative to *https://api.pandascore.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getTeams**](TeamsApi.md#getTeams) | **GET** /teams | List teams
[**getTeamsTeamIdOrSlug**](TeamsApi.md#getTeamsTeamIdOrSlug) | **GET** /teams/{team_id_or_slug} | Get a team
[**getTeamsTeamIdOrSlugLeagues**](TeamsApi.md#getTeamsTeamIdOrSlugLeagues) | **GET** /teams/{team_id_or_slug}/leagues | Get leagues for a team
[**getTeamsTeamIdOrSlugMatches**](TeamsApi.md#getTeamsTeamIdOrSlugMatches) | **GET** /teams/{team_id_or_slug}/matches | Get matches for team
[**getTeamsTeamIdOrSlugSeries**](TeamsApi.md#getTeamsTeamIdOrSlugSeries) | **GET** /teams/{team_id_or_slug}/series | Get series for a team
[**getTeamsTeamIdOrSlugTournaments**](TeamsApi.md#getTeamsTeamIdOrSlugTournaments) | **GET** /teams/{team_id_or_slug}/tournaments | Get tournaments for a team



## getTeams

> [Team] getTeams(opts)

List teams

List teams

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

let apiInstance = new PandaScoreRestApiForAllVideogames.TeamsApi();
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverTeams(), // FilterOverTeams | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverTeams(), // SearchOverTeams | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverTeams(), // RangeOverTeams | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getTeams(opts, (error, data, response) => {
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


## getTeamsTeamIdOrSlug

> Team getTeamsTeamIdOrSlug(teamIdOrSlug)

Get a team

Get a single team by ID or by slug

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

let apiInstance = new PandaScoreRestApiForAllVideogames.TeamsApi();
let teamIdOrSlug = new PandaScoreRestApiForAllVideogames.TeamIDOrSlug(); // TeamIDOrSlug | A team ID or slug
apiInstance.getTeamsTeamIdOrSlug(teamIdOrSlug, (error, data, response) => {
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
 **teamIdOrSlug** | [**TeamIDOrSlug**](.md)| A team ID or slug | 

### Return type

[**Team**](Team.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamsTeamIdOrSlugLeagues

> [League] getTeamsTeamIdOrSlugLeagues(teamIdOrSlug, opts)

Get leagues for a team

List leagues in which the given team was part of

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

let apiInstance = new PandaScoreRestApiForAllVideogames.TeamsApi();
let teamIdOrSlug = new PandaScoreRestApiForAllVideogames.TeamIDOrSlug(); // TeamIDOrSlug | A team ID or slug
let opts = {
  'search': new PandaScoreRestApiForAllVideogames.SearchOverLeagues(), // SearchOverLeagues | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverLeagues(), // RangeOverLeagues | Options to select results within ranges
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverLeagues(), // FilterOverLeagues | Options to filter results. String fields are case sensitive
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getTeamsTeamIdOrSlugLeagues(teamIdOrSlug, opts, (error, data, response) => {
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
 **teamIdOrSlug** | [**TeamIDOrSlug**](.md)| A team ID or slug | 
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


## getTeamsTeamIdOrSlugMatches

> [Match] getTeamsTeamIdOrSlugMatches(teamIdOrSlug, opts)

Get matches for team

List matches for the given team

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

let apiInstance = new PandaScoreRestApiForAllVideogames.TeamsApi();
let teamIdOrSlug = new PandaScoreRestApiForAllVideogames.TeamIDOrSlug(); // TeamIDOrSlug | A team ID or slug
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverMatches(), // FilterOverMatches | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverMatches(), // SearchOverMatches | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverMatches(), // RangeOverMatches | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getTeamsTeamIdOrSlugMatches(teamIdOrSlug, opts, (error, data, response) => {
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
 **teamIdOrSlug** | [**TeamIDOrSlug**](.md)| A team ID or slug | 
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


## getTeamsTeamIdOrSlugSeries

> [Serie] getTeamsTeamIdOrSlugSeries(teamIdOrSlug, opts)

Get series for a team

List series in which the given team was part of

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

let apiInstance = new PandaScoreRestApiForAllVideogames.TeamsApi();
let teamIdOrSlug = new PandaScoreRestApiForAllVideogames.TeamIDOrSlug(); // TeamIDOrSlug | A team ID or slug
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverSeries(), // FilterOverSeries | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverSeries(), // SearchOverSeries | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverSeries(), // RangeOverSeries | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getTeamsTeamIdOrSlugSeries(teamIdOrSlug, opts, (error, data, response) => {
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
 **teamIdOrSlug** | [**TeamIDOrSlug**](.md)| A team ID or slug | 
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


## getTeamsTeamIdOrSlugTournaments

> [ShortTournament] getTeamsTeamIdOrSlugTournaments(teamIdOrSlug, opts)

Get tournaments for a team

List tournaments in which the given team was part of

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

let apiInstance = new PandaScoreRestApiForAllVideogames.TeamsApi();
let teamIdOrSlug = new PandaScoreRestApiForAllVideogames.TeamIDOrSlug(); // TeamIDOrSlug | A team ID or slug
let opts = {
  'filter': new PandaScoreRestApiForAllVideogames.FilterOverShortTournaments(), // FilterOverShortTournaments | Options to filter results. String fields are case sensitive
  'search': new PandaScoreRestApiForAllVideogames.SearchOverShortTournaments(), // SearchOverShortTournaments | Options to search results
  'sort': ["null"], // [String] | Options to sort results
  'range': new PandaScoreRestApiForAllVideogames.RangeOverShortTournaments(), // RangeOverShortTournaments | Options to select results within ranges
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getTeamsTeamIdOrSlugTournaments(teamIdOrSlug, opts, (error, data, response) => {
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
 **teamIdOrSlug** | [**TeamIDOrSlug**](.md)| A team ID or slug | 
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

