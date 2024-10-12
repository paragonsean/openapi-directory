# ShortenRestApiDocumentation.ClickApi

All URIs are relative to *https://api.shorten.rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getClicks**](ClickApi.md#getClicks) | **GET** /clicks | Get clicks



## getClicks

> GetClicksModel getClicks(opts)

Get clicks

Retrieve the raw click data for your account. Clicks are retrieved by creation date in descending order.    If there are more results than the limit for the request the response will return you a value in lastId property you can specify it in the continueFrom query parameter to get the next batch of records.

### Example

```javascript
import ShortenRestApiDocumentation from 'shorten_rest_api_documentation';
let defaultClient = ShortenRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ShortenRestApiDocumentation.ClickApi();
let opts = {
  'continueFrom': "1588788835614657618", // String | An ID returned by a previous query to continue clicks retrieval (see lastId in response)
  'limit': 100 // Number | Number of results to return per request
};
apiInstance.getClicks(opts, (error, data, response) => {
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
 **continueFrom** | **String**| An ID returned by a previous query to continue clicks retrieval (see lastId in response) | [optional] 
 **limit** | **Number**| Number of results to return per request | [optional] [default to 1000]

### Return type

[**GetClicksModel**](GetClicksModel.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

