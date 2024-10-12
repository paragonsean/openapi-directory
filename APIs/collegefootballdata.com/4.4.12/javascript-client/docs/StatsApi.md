# CollegeFootballDataApi.StatsApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAdvancedTeamGameStats**](StatsApi.md#getAdvancedTeamGameStats) | **GET** /stats/game/advanced | Advanced team metrics by game
[**getAdvancedTeamSeasonStats**](StatsApi.md#getAdvancedTeamSeasonStats) | **GET** /stats/season/advanced | Advanced team metrics by season
[**getStatCategories**](StatsApi.md#getStatCategories) | **GET** /stats/categories | Team stat categories
[**getTeamSeasonStats**](StatsApi.md#getTeamSeasonStats) | **GET** /stats/season | Team statistics by season



## getAdvancedTeamGameStats

> [AdvancedGameStat] getAdvancedTeamGameStats(opts)

Advanced team metrics by game

Advanced team game stats

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.StatsApi();
let opts = {
  'year': 56, // Number | Year filter (required if no team specified)
  'week': 56, // Number | Week filter
  'team': "team_example", // String | Team filter (required if no year specified)
  'opponent': "opponent_example", // String | Opponent filter
  'excludeGarbageTime': true, // Boolean | Filter to remove garbage time plays from calculations
  'seasonType': "seasonType_example" // String | Season type filter (regular, postseason, or both)
};
apiInstance.getAdvancedTeamGameStats(opts, (error, data, response) => {
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
 **year** | **Number**| Year filter (required if no team specified) | [optional] 
 **week** | **Number**| Week filter | [optional] 
 **team** | **String**| Team filter (required if no year specified) | [optional] 
 **opponent** | **String**| Opponent filter | [optional] 
 **excludeGarbageTime** | **Boolean**| Filter to remove garbage time plays from calculations | [optional] 
 **seasonType** | **String**| Season type filter (regular, postseason, or both) | [optional] 

### Return type

[**[AdvancedGameStat]**](AdvancedGameStat.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAdvancedTeamSeasonStats

> [AdvancedSeasonStat] getAdvancedTeamSeasonStats(opts)

Advanced team metrics by season

Advanced team season stats

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.StatsApi();
let opts = {
  'year': 56, // Number | Year filter (required if no team specified)
  'team': "team_example", // String | Team filter (required if no year specified)
  'excludeGarbageTime': true, // Boolean | Filter to remove garbage time plays from calculations
  'startWeek': 56, // Number | Starting week filter
  'endWeek': 56 // Number | Starting week filter
};
apiInstance.getAdvancedTeamSeasonStats(opts, (error, data, response) => {
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
 **year** | **Number**| Year filter (required if no team specified) | [optional] 
 **team** | **String**| Team filter (required if no year specified) | [optional] 
 **excludeGarbageTime** | **Boolean**| Filter to remove garbage time plays from calculations | [optional] 
 **startWeek** | **Number**| Starting week filter | [optional] 
 **endWeek** | **Number**| Starting week filter | [optional] 

### Return type

[**[AdvancedSeasonStat]**](AdvancedSeasonStat.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getStatCategories

> [String] getStatCategories()

Team stat categories

Stat category list

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.StatsApi();
apiInstance.getStatCategories((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamSeasonStats

> [TeamSeasonStat] getTeamSeasonStats(opts)

Team statistics by season

Team season stats

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.StatsApi();
let opts = {
  'year': 56, // Number | Year filter (required if no team specified)
  'team': "team_example", // String | Team filter (required if no year specified)
  'conference': "conference_example", // String | Conference abbreviation filter
  'startWeek': 56, // Number | Starting week filter
  'endWeek': 56 // Number | Starting week filter
};
apiInstance.getTeamSeasonStats(opts, (error, data, response) => {
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
 **year** | **Number**| Year filter (required if no team specified) | [optional] 
 **team** | **String**| Team filter (required if no year specified) | [optional] 
 **conference** | **String**| Conference abbreviation filter | [optional] 
 **startWeek** | **Number**| Starting week filter | [optional] 
 **endWeek** | **Number**| Starting week filter | [optional] 

### Return type

[**[TeamSeasonStat]**](TeamSeasonStat.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

