# CollegeFootballDataApi.PlaysApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLivePlays**](PlaysApi.md#getLivePlays) | **GET** /live/plays | Live metrics and PBP (Patreon only)
[**getPlayStatTypes**](PlaysApi.md#getPlayStatTypes) | **GET** /play/stat/types | Types of player play stats
[**getPlayStats**](PlaysApi.md#getPlayStats) | **GET** /play/stats | Play stats by play
[**getPlayTypes**](PlaysApi.md#getPlayTypes) | **GET** /play/types | Play types
[**getPlays**](PlaysApi.md#getPlays) | **GET** /plays | Play by play data



## getLivePlays

> LivePlayByPlay getLivePlays(id)

Live metrics and PBP (Patreon only)

Get live metrics and PBP

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.PlaysApi();
let id = 56; // Number | Game id
apiInstance.getLivePlays(id, (error, data, response) => {
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
 **id** | **Number**| Game id | 

### Return type

[**LivePlayByPlay**](LivePlayByPlay.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPlayStatTypes

> [PlayStatType] getPlayStatTypes()

Types of player play stats

Type of play stats

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.PlaysApi();
apiInstance.getPlayStatTypes((error, data, response) => {
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

[**[PlayStatType]**](PlayStatType.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPlayStats

> [PlayStat] getPlayStats(opts)

Play stats by play

Gets player stats associated by play (limit 1000)

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.PlaysApi();
let opts = {
  'year': 56, // Number | Year filter
  'week': 56, // Number | Week filter
  'team': "team_example", // String | Team filter
  'gameId': 56, // Number | gameId filter (from /games endpoint)
  'athleteId': 56, // Number | athleteId filter (from /roster endpoint)
  'statTypeId': 56, // Number | statTypeId filter (from /play/stat/types endpoint)
  'seasonType': "seasonType_example", // String | regular, postseason, or both
  'conference': "conference_example" // String | conference abbreviation filter
};
apiInstance.getPlayStats(opts, (error, data, response) => {
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
 **year** | **Number**| Year filter | [optional] 
 **week** | **Number**| Week filter | [optional] 
 **team** | **String**| Team filter | [optional] 
 **gameId** | **Number**| gameId filter (from /games endpoint) | [optional] 
 **athleteId** | **Number**| athleteId filter (from /roster endpoint) | [optional] 
 **statTypeId** | **Number**| statTypeId filter (from /play/stat/types endpoint) | [optional] 
 **seasonType** | **String**| regular, postseason, or both | [optional] 
 **conference** | **String**| conference abbreviation filter | [optional] 

### Return type

[**[PlayStat]**](PlayStat.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPlayTypes

> [PlayType] getPlayTypes()

Play types

Types of plays

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.PlaysApi();
apiInstance.getPlayTypes((error, data, response) => {
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

[**[PlayType]**](PlayType.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPlays

> [Play] getPlays(year, week, opts)

Play by play data

Get play data and results

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.PlaysApi();
let year = 56; // Number | Year filter
let week = 56; // Number | Week filter (required if team, offense, or defense, not specified)
let opts = {
  'seasonType': "'regular'", // String | Season type filter
  'team': "team_example", // String | Team filter
  'offense': "offense_example", // String | Offensive team filter
  'defense': "defense_example", // String | Defensive team filter
  'conference': "conference_example", // String | Conference filter
  'offenseConference': "offenseConference_example", // String | Offensive conference filter
  'defenseConference': "defenseConference_example", // String | Defensive conference filter
  'playType': 56, // Number | Play type filter
  'classification': "classification_example" // String | Division classification filter (fbs/fcs/ii/iii)
};
apiInstance.getPlays(year, week, opts, (error, data, response) => {
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
 **year** | **Number**| Year filter | 
 **week** | **Number**| Week filter (required if team, offense, or defense, not specified) | 
 **seasonType** | **String**| Season type filter | [optional] [default to &#39;regular&#39;]
 **team** | **String**| Team filter | [optional] 
 **offense** | **String**| Offensive team filter | [optional] 
 **defense** | **String**| Defensive team filter | [optional] 
 **conference** | **String**| Conference filter | [optional] 
 **offenseConference** | **String**| Offensive conference filter | [optional] 
 **defenseConference** | **String**| Defensive conference filter | [optional] 
 **playType** | **Number**| Play type filter | [optional] 
 **classification** | **String**| Division classification filter (fbs/fcs/ii/iii) | [optional] 

### Return type

[**[Play]**](Play.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

