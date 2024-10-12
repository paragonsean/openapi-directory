# CollegeFootballDataApi.MetricsApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getGamePPA**](MetricsApi.md#getGamePPA) | **GET** /ppa/games | Team Predicated Points Added (PPA/EPA) by game
[**getPlayerGamePPA**](MetricsApi.md#getPlayerGamePPA) | **GET** /ppa/players/games | Player Predicated Points Added (PPA/EPA) broken down by game
[**getPlayerSeasonPPA**](MetricsApi.md#getPlayerSeasonPPA) | **GET** /ppa/players/season | Player Predicated Points Added (PPA/EPA) broken down by season
[**getPredictedPoints**](MetricsApi.md#getPredictedPoints) | **GET** /ppa/predicted | Predicted Points (i.e. Expected Points or EP)
[**getPregameWinProbabilities**](MetricsApi.md#getPregameWinProbabilities) | **GET** /metrics/wp/pregame | Pregame win probability data
[**getTeamPPA**](MetricsApi.md#getTeamPPA) | **GET** /ppa/teams | Predicted Points Added (PPA/EPA) data by team
[**getWinProbabilityData**](MetricsApi.md#getWinProbabilityData) | **GET** /metrics/wp | Win probability chart data



## getGamePPA

> [GamePPA] getGamePPA(year, opts)

Team Predicated Points Added (PPA/EPA) by game

Predicted Points Added (PPA) by game

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.MetricsApi();
let year = 56; // Number | Year filter
let opts = {
  'week': 56, // Number | Week filter
  'team': "team_example", // String | Team filter
  'conference': "conference_example", // String | Conference filter
  'excludeGarbageTime': true, // Boolean | Filter to remove garbage time plays from calculations
  'seasonType': "'regular'" // String | Season type filter (regular or postseason)
};
apiInstance.getGamePPA(year, opts, (error, data, response) => {
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
 **week** | **Number**| Week filter | [optional] 
 **team** | **String**| Team filter | [optional] 
 **conference** | **String**| Conference filter | [optional] 
 **excludeGarbageTime** | **Boolean**| Filter to remove garbage time plays from calculations | [optional] 
 **seasonType** | **String**| Season type filter (regular or postseason) | [optional] [default to &#39;regular&#39;]

### Return type

[**[GamePPA]**](GamePPA.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPlayerGamePPA

> [PlayerGamePPA] getPlayerGamePPA(opts)

Player Predicated Points Added (PPA/EPA) broken down by game

Predicted Points Added (PPA) by player game

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.MetricsApi();
let opts = {
  'year': 56, // Number | Year filter
  'week': 56, // Number | Week filter
  'team': "team_example", // String | Team filter
  'position': "position_example", // String | Position abbreviation filter
  'playerId': 56, // Number | Player id filter
  'threshold': "threshold_example", // String | Minimum play threshold filter
  'excludeGarbageTime': true, // Boolean | Filter to remove garbage time plays from calculations
  'seasonType': "'regular'" // String | Season type filter (regular or postseason)
};
apiInstance.getPlayerGamePPA(opts, (error, data, response) => {
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
 **position** | **String**| Position abbreviation filter | [optional] 
 **playerId** | **Number**| Player id filter | [optional] 
 **threshold** | **String**| Minimum play threshold filter | [optional] 
 **excludeGarbageTime** | **Boolean**| Filter to remove garbage time plays from calculations | [optional] 
 **seasonType** | **String**| Season type filter (regular or postseason) | [optional] [default to &#39;regular&#39;]

### Return type

[**[PlayerGamePPA]**](PlayerGamePPA.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPlayerSeasonPPA

> [PlayerSeasonPPA] getPlayerSeasonPPA(opts)

Player Predicated Points Added (PPA/EPA) broken down by season

Predicted Points Added (PPA) by player season

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.MetricsApi();
let opts = {
  'year': 56, // Number | Year filter
  'team': "team_example", // String | Team filter
  'conference': "conference_example", // String | Conference abbreviation filter
  'position': "position_example", // String | Position abbreviation filter
  'playerId': 56, // Number | Player id filter
  'threshold': "threshold_example", // String | Minimum play threshold filter
  'excludeGarbageTime': true // Boolean | Filter to remove garbage time plays from calculations
};
apiInstance.getPlayerSeasonPPA(opts, (error, data, response) => {
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
 **team** | **String**| Team filter | [optional] 
 **conference** | **String**| Conference abbreviation filter | [optional] 
 **position** | **String**| Position abbreviation filter | [optional] 
 **playerId** | **Number**| Player id filter | [optional] 
 **threshold** | **String**| Minimum play threshold filter | [optional] 
 **excludeGarbageTime** | **Boolean**| Filter to remove garbage time plays from calculations | [optional] 

### Return type

[**[PlayerSeasonPPA]**](PlayerSeasonPPA.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPredictedPoints

> [PredictedPoints] getPredictedPoints(down, distance)

Predicted Points (i.e. Expected Points or EP)

Predicted Points

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.MetricsApi();
let down = 56; // Number | Down filter
let distance = 56; // Number | Distance filter
apiInstance.getPredictedPoints(down, distance, (error, data, response) => {
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
 **down** | **Number**| Down filter | 
 **distance** | **Number**| Distance filter | 

### Return type

[**[PredictedPoints]**](PredictedPoints.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPregameWinProbabilities

> [PregameWP] getPregameWinProbabilities(opts)

Pregame win probability data

Pregame win probabilities

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.MetricsApi();
let opts = {
  'year': 56, // Number | Year filter
  'week': 56, // Number | Week filter
  'team': "team_example", // String | Team filter
  'seasonType': "seasonType_example" // String | regular or postseason
};
apiInstance.getPregameWinProbabilities(opts, (error, data, response) => {
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
 **seasonType** | **String**| regular or postseason | [optional] 

### Return type

[**[PregameWP]**](PregameWP.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTeamPPA

> [TeamPPA] getTeamPPA(opts)

Predicted Points Added (PPA/EPA) data by team

Predicted Points Added (PPA)

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.MetricsApi();
let opts = {
  'year': 56, // Number | Year filter (required if team not specified)
  'team': "team_example", // String | Team filter (required if year not specified)
  'conference': "conference_example", // String | Conference filter
  'excludeGarbageTime': true // Boolean | Filter to remove garbage time plays from calculations
};
apiInstance.getTeamPPA(opts, (error, data, response) => {
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
 **year** | **Number**| Year filter (required if team not specified) | [optional] 
 **team** | **String**| Team filter (required if year not specified) | [optional] 
 **conference** | **String**| Conference filter | [optional] 
 **excludeGarbageTime** | **Boolean**| Filter to remove garbage time plays from calculations | [optional] 

### Return type

[**[TeamPPA]**](TeamPPA.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWinProbabilityData

> [PlayWP] getWinProbabilityData(gameId)

Win probability chart data

Win probability data

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.MetricsApi();
let gameId = 56; // Number | Game id filter
apiInstance.getWinProbabilityData(gameId, (error, data, response) => {
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
 **gameId** | **Number**| Game id filter | 

### Return type

[**[PlayWP]**](PlayWP.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

