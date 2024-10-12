# PandaScoreRestApiForAllVideogames.LivesApi

All URIs are relative to *https://api.pandascore.co*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getLives_0**](LivesApi.md#getLives_0) | **GET** /lives | List lives matches



## getLives_0

> [Live] getLives_0(opts)

List lives matches

List currently running live matches, available from pandascore with live websocket data.

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

let apiInstance = new PandaScoreRestApiForAllVideogames.LivesApi();
let opts = {
  'page': new PandaScoreRestApiForAllVideogames.GetAdditionsPageParameter(), // GetAdditionsPageParameter | Pagination in the form of `page=2` or `page[size]=30&amp;page[number]=2`
  'perPage': 5 // Number | Equivalent to `page[size]`
};
apiInstance.getLives_0(opts, (error, data, response) => {
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
 **page** | [**GetAdditionsPageParameter**](.md)| Pagination in the form of &#x60;page&#x3D;2&#x60; or &#x60;page[size]&#x3D;30&amp;amp;page[number]&#x3D;2&#x60; | [optional] 
 **perPage** | **Number**| Equivalent to &#x60;page[size]&#x60; | [optional] [default to 50]

### Return type

[**[Live]**](Live.md)

### Authorization

[BearerToken](../README.md#BearerToken), [QueryToken](../README.md#QueryToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

