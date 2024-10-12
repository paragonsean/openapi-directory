# JellyfinApi.MoviesApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMovieRecommendations**](MoviesApi.md#getMovieRecommendations) | **GET** /Movies/Recommendations | Gets movie recommendations.



## getMovieRecommendations

> [RecommendationDto] getMovieRecommendations(opts)

Gets movie recommendations.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.MoviesApi();
let opts = {
  'userId': "userId_example", // String | Optional. Filter by user id, and attach user data.
  'parentId': "parentId_example", // String | Specify this to localize the search to a specific item or folder. Omit to use the root.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. The fields to return.
  'categoryLimit': 5, // Number | The max number of categories to return.
  'itemLimit': 8 // Number | The max number of items to return per category.
};
apiInstance.getMovieRecommendations(opts, (error, data, response) => {
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
 **userId** | **String**| Optional. Filter by user id, and attach user data. | [optional] 
 **parentId** | **String**| Specify this to localize the search to a specific item or folder. Omit to use the root. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. The fields to return. | [optional] 
 **categoryLimit** | **Number**| The max number of categories to return. | [optional] [default to 5]
 **itemLimit** | **Number**| The max number of items to return per category. | [optional] [default to 8]

### Return type

[**[RecommendationDto]**](RecommendationDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase

