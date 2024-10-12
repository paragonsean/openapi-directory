# CollegeFootballDataApi.CoachesApi

All URIs are relative to *https://api.collegefootballdata.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCoaches**](CoachesApi.md#getCoaches) | **GET** /coaches | Coaching records and history



## getCoaches

> [Coach] getCoaches(opts)

Coaching records and history

Coaching history

### Example

```javascript
import CollegeFootballDataApi from 'college_football_data_api';
let defaultClient = CollegeFootballDataApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CollegeFootballDataApi.CoachesApi();
let opts = {
  'firstName': "firstName_example", // String | First name filter
  'lastName': "lastName_example", // String | Last name filter
  'team': "team_example", // String | Team name filter
  'year': 56, // Number | Year filter
  'minYear': 56, // Number | Minimum year filter (inclusive)
  'maxYear': 56 // Number | Maximum year filter (inclusive)
};
apiInstance.getCoaches(opts, (error, data, response) => {
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
 **firstName** | **String**| First name filter | [optional] 
 **lastName** | **String**| Last name filter | [optional] 
 **team** | **String**| Team name filter | [optional] 
 **year** | **Number**| Year filter | [optional] 
 **minYear** | **Number**| Minimum year filter (inclusive) | [optional] 
 **maxYear** | **Number**| Maximum year filter (inclusive) | [optional] 

### Return type

[**[Coach]**](Coach.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

