# Owler.FeedAPIApi

All URIs are relative to *https://api.owler.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1FeedGet**](FeedAPIApi.md#v1FeedGet) | **GET** /v1/feed | Get Feeds for given Company Ids
[**v1FeedUrlGet**](FeedAPIApi.md#v1FeedUrlGet) | **GET** /v1/feed/url | Get Feeds for given Company Websites



## v1FeedGet

> Results v1FeedGet(companyId, opts)

Get Feeds for given Company Ids

The Feeds API provides a list of feeds and individual feed information for the given Company Ids and Category. By default the API returns the latest 10 feeds available unless the limit is specified. The maximum result is restricted to 100 feeds per API request.

### Example

```javascript
import Owler from 'owler';
let defaultClient = Owler.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new Owler.FeedAPIApi();
let companyId = ["null"]; // [String] | Company Ids separated by comma (Maximum of 150 Company Ids)
let opts = {
  'format': "'json'", // String | Format of the response content - json (by default if not specified), xml
  'limit': "'10'", // String | Number of results to be displayed - 10 (by default, if not specified) to 100
  'paginationId': "'*'", // String | Pass pagination_id as blank in the first API request. The API response will return the latest feeds along with the next pagination_id which can be passed in the subsequent API request to get the next set of feeds. Repeat this process until needed or till the pagination_id returned is blank
  'category': ["null"] // [String] | Categories separated by comma. If not specified, will search against all categories
};
apiInstance.v1FeedGet(companyId, opts, (error, data, response) => {
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
 **companyId** | [**[String]**](String.md)| Company Ids separated by comma (Maximum of 150 Company Ids) | 
 **format** | **String**| Format of the response content - json (by default if not specified), xml | [optional] [default to &#39;json&#39;]
 **limit** | **String**| Number of results to be displayed - 10 (by default, if not specified) to 100 | [optional] [default to &#39;10&#39;]
 **paginationId** | **String**| Pass pagination_id as blank in the first API request. The API response will return the latest feeds along with the next pagination_id which can be passed in the subsequent API request to get the next set of feeds. Repeat this process until needed or till the pagination_id returned is blank | [optional] [default to &#39;*&#39;]
 **category** | [**[String]**](String.md)| Categories separated by comma. If not specified, will search against all categories | [optional] 

### Return type

[**Results**](Results.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## v1FeedUrlGet

> Results v1FeedUrlGet(domain, opts)

Get Feeds for given Company Websites

The Feeds API provides a list of feeds and individual feed information for the given Company Websites and Category. By default the API returns the latest 10 feeds available unless the limit is specified. The maximum result is restricted to 100 feeds per API request.

### Example

```javascript
import Owler from 'owler';
let defaultClient = Owler.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new Owler.FeedAPIApi();
let domain = ["null"]; // [String] | Company Websites separated by comma (Maximum of 10 Company Websites)
let opts = {
  'format': "'json'", // String | Format of the response content - json (by default if not specified), xml
  'limit': "'10'", // String | Number of results to be displayed - 10 (by default, if not specified) to 100
  'paginationId': "'*'", // String | Pass pagination_id as blank in the first API request. The API response will return the latest feeds along with the next pagination_id which can be passed in the subsequent API request to get the next set of feeds. Repeat this process until needed or till the pagination_id returned is blank
  'category': ["null"] // [String] | Categories separated by comma. If not specified, will search against all categories
};
apiInstance.v1FeedUrlGet(domain, opts, (error, data, response) => {
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
 **domain** | [**[String]**](String.md)| Company Websites separated by comma (Maximum of 10 Company Websites) | 
 **format** | **String**| Format of the response content - json (by default if not specified), xml | [optional] [default to &#39;json&#39;]
 **limit** | **String**| Number of results to be displayed - 10 (by default, if not specified) to 100 | [optional] [default to &#39;10&#39;]
 **paginationId** | **String**| Pass pagination_id as blank in the first API request. The API response will return the latest feeds along with the next pagination_id which can be passed in the subsequent API request to get the next set of feeds. Repeat this process until needed or till the pagination_id returned is blank | [optional] [default to &#39;*&#39;]
 **category** | [**[String]**](String.md)| Categories separated by comma. If not specified, will search against all categories | [optional] 

### Return type

[**Results**](Results.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

