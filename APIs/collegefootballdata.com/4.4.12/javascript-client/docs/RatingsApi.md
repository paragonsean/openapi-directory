# CollegeFootballDataApi.RatingsApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getConferenceSPRatings**](RatingsApi.md#getConferenceSPRatings) | **GET** /ratings/sp/conferences | Historical SP+ ratings by conference
[**getEloRatings**](RatingsApi.md#getEloRatings) | **GET** /ratings/elo | Historical Elo ratings
[**getSPRatings**](RatingsApi.md#getSPRatings) | **GET** /ratings/sp | Historical SP+ ratings
[**getSRSRatings**](RatingsApi.md#getSRSRatings) | **GET** /ratings/srs | Historical SRS ratings



## getConferenceSPRatings

> [ConferenceSPRating] getConferenceSPRatings(opts)

Historical SP+ ratings by conference

Get average SP+ historical rating data by conference

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.RatingsApi();
let opts = {
  'year': 56, // Number | Season filter
  'conference': "conference_example" // String | Conference abbreviation filter
};
apiInstance.getConferenceSPRatings(opts, (error, data, response) => {
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
 **year** | **Number**| Season filter | [optional] 
 **conference** | **String**| Conference abbreviation filter | [optional] 

### Return type

[**[ConferenceSPRating]**](ConferenceSPRating.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEloRatings

> [TeamEloRating] getEloRatings(opts)

Historical Elo ratings

Elo rating data

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.RatingsApi();
let opts = {
  'year': 56, // Number | Season filter
  'week': 56, // Number | Maximum week filter
  'team': "team_example", // String | Team filter
  'conference': "conference_example" // String | Conference filter
};
apiInstance.getEloRatings(opts, (error, data, response) => {
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
 **year** | **Number**| Season filter | [optional] 
 **week** | **Number**| Maximum week filter | [optional] 
 **team** | **String**| Team filter | [optional] 
 **conference** | **String**| Conference filter | [optional] 

### Return type

[**[TeamEloRating]**](TeamEloRating.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSPRatings

> [TeamSPRating] getSPRatings(opts)

Historical SP+ ratings

SP+ rating data

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.RatingsApi();
let opts = {
  'year': 56, // Number | Season filter (required if team not specified)
  'team': "team_example" // String | Team filter (required if year not specified)
};
apiInstance.getSPRatings(opts, (error, data, response) => {
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
 **year** | **Number**| Season filter (required if team not specified) | [optional] 
 **team** | **String**| Team filter (required if year not specified) | [optional] 

### Return type

[**[TeamSPRating]**](TeamSPRating.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSRSRatings

> [TeamSRSRating] getSRSRatings(opts)

Historical SRS ratings

SRS rating data (requires either a year or team specified)

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.RatingsApi();
let opts = {
  'year': 56, // Number | Season filter (required if team not specified)
  'team': "team_example", // String | Team filter (required if year not specified)
  'conference': "conference_example" // String | Conference filter
};
apiInstance.getSRSRatings(opts, (error, data, response) => {
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
 **year** | **Number**| Season filter (required if team not specified) | [optional] 
 **team** | **String**| Team filter (required if year not specified) | [optional] 
 **conference** | **String**| Conference filter | [optional] 

### Return type

[**[TeamSRSRating]**](TeamSRSRating.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

