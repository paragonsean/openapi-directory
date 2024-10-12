# CollegeFootballDataApi.DraftApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getDraftPicks**](DraftApi.md#getDraftPicks) | **GET** /draft/picks | List of NFL Draft picks
[**getNFLPositions**](DraftApi.md#getNFLPositions) | **GET** /draft/positions | List of NFL positions
[**getNFLTeams**](DraftApi.md#getNFLTeams) | **GET** /draft/teams | List of NFL teams



## getDraftPicks

> [DraftPick] getDraftPicks(opts)

List of NFL Draft picks

List of NFL Draft picks

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.DraftApi();
let opts = {
  'year': 56, // Number | Year filter
  'nflTeam': "nflTeam_example", // String | NFL team filter
  'college': "college_example", // String | Player college filter
  'conference': "conference_example", // String | College confrence abbreviation filter
  'position': "position_example" // String | NFL position filter
};
apiInstance.getDraftPicks(opts, (error, data, response) => {
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
 **nflTeam** | **String**| NFL team filter | [optional] 
 **college** | **String**| Player college filter | [optional] 
 **conference** | **String**| College confrence abbreviation filter | [optional] 
 **position** | **String**| NFL position filter | [optional] 

### Return type

[**[DraftPick]**](DraftPick.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNFLPositions

> [DraftPosition] getNFLPositions()

List of NFL positions

List of NFL positions

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.DraftApi();
apiInstance.getNFLPositions((error, data, response) => {
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

[**[DraftPosition]**](DraftPosition.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNFLTeams

> [DraftTeam] getNFLTeams()

List of NFL teams

List of NFL teams

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.DraftApi();
apiInstance.getNFLTeams((error, data, response) => {
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

[**[DraftTeam]**](DraftTeam.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

