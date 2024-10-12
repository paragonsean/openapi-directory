# Shinobiapi.MiscellaneousConversionOtherUtilitiesApi

All URIs are relative to *https://api.hillbillysoftware.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getIMDBidGetAsync**](MiscellaneousConversionOtherUtilitiesApi.md#getIMDBidGetAsync) | **GET** /GetIMDBid/ByID/{AccessToken}/{Query} | Gets list of avaiable IMDB ids from Movies and TV Show databases, you can use those to query other end points that need ID&#39;s



## getIMDBidGetAsync

> [ImdbID] getIMDBidGetAsync(accessToken, query)

Gets list of avaiable IMDB ids from Movies and TV Show databases, you can use those to query other end points that need ID&#39;s

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.MiscellaneousConversionOtherUtilitiesApi();
let accessToken = "accessToken_example"; // String | 
let query = "query_example"; // String | 
apiInstance.getIMDBidGetAsync(accessToken, query, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **query** | **String**|  | 

### Return type

[**[ImdbID]**](ImdbID.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

