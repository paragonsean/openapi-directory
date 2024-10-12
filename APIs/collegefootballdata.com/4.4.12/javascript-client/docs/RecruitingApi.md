# CollegeFootballDataApi.RecruitingApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRecruitingGroups**](RecruitingApi.md#getRecruitingGroups) | **GET** /recruiting/groups | Recruit position group ratings
[**getRecruitingPlayers**](RecruitingApi.md#getRecruitingPlayers) | **GET** /recruiting/players | Player recruiting ratings and rankings
[**getRecruitingTeams**](RecruitingApi.md#getRecruitingTeams) | **GET** /recruiting/teams | Team recruiting rankings and ratings



## getRecruitingGroups

> [PositionGroupRecruitingRating] getRecruitingGroups(opts)

Recruit position group ratings

Gets a list of aggregated statistics by team and position grouping

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.RecruitingApi();
let opts = {
  'startYear': 56, // Number | Starting year
  'endYear': 56, // Number | Ending year
  'team': "team_example", // String | Team filter
  'conference': "conference_example" // String | conference filter
};
apiInstance.getRecruitingGroups(opts, (error, data, response) => {
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
 **startYear** | **Number**| Starting year | [optional] 
 **endYear** | **Number**| Ending year | [optional] 
 **team** | **String**| Team filter | [optional] 
 **conference** | **String**| conference filter | [optional] 

### Return type

[**[PositionGroupRecruitingRating]**](PositionGroupRecruitingRating.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRecruitingPlayers

> [Recruit] getRecruitingPlayers(opts)

Player recruiting ratings and rankings

Get player recruiting rankings and data. Requires either a year or team to be specified.

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.RecruitingApi();
let opts = {
  'year': 56, // Number | Recruiting class year (required if team no specified)
  'classification': "'HighSchool'", // String | Type of recruit (HighSchool, JUCO, PrepSchool)
  'position': "position_example", // String | Position abbreviation filter
  'state': "state_example", // String | State or province abbreviation filter
  'team': "team_example" // String | Committed team filter (required if year not specified)
};
apiInstance.getRecruitingPlayers(opts, (error, data, response) => {
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
 **year** | **Number**| Recruiting class year (required if team no specified) | [optional] 
 **classification** | **String**| Type of recruit (HighSchool, JUCO, PrepSchool) | [optional] [default to &#39;HighSchool&#39;]
 **position** | **String**| Position abbreviation filter | [optional] 
 **state** | **String**| State or province abbreviation filter | [optional] 
 **team** | **String**| Committed team filter (required if year not specified) | [optional] 

### Return type

[**[Recruit]**](Recruit.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRecruitingTeams

> [TeamRecruitingRank] getRecruitingTeams(opts)

Team recruiting rankings and ratings

Team recruiting rankings

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.RecruitingApi();
let opts = {
  'year': 56, // Number | Recruiting class year
  'team': "team_example" // String | Team filter
};
apiInstance.getRecruitingTeams(opts, (error, data, response) => {
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
 **year** | **Number**| Recruiting class year | [optional] 
 **team** | **String**| Team filter | [optional] 

### Return type

[**[TeamRecruitingRank]**](TeamRecruitingRank.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

