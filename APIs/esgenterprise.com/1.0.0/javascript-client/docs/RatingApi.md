# EsgRatingData.RatingApi

All URIs are relative to *https://tf689y3hbj.execute-api.us-east-1.amazonaws.com/prod/authorization*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchGet**](RatingApi.md#searchGet) | **GET** /search | List all company ESG Ratings



## searchGet

> SearchGet200Response searchGet(q)

List all company ESG Ratings

### Example

```javascript
import EsgRatingData from 'esg_rating_data';
let defaultClient = EsgRatingData.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new EsgRatingData.RatingApi();
let q = "q_example"; // String | Company name or stock symbol
apiInstance.searchGet(q, (error, data, response) => {
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
 **q** | **String**| Company name or stock symbol | 

### Return type

[**SearchGet200Response**](SearchGet200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

