# TimesNewswireApi.DefaultApi

All URIs are relative to *http://api.nytimes.com/svc/news/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contentJsonGet**](DefaultApi.md#contentJsonGet) | **GET** /content.json | 
[**contentSourceSectionJsonGet**](DefaultApi.md#contentSourceSectionJsonGet) | **GET** /content/{source}/{section}.json | 
[**contentSourceSectionTimePeriodJsonGet**](DefaultApi.md#contentSourceSectionTimePeriodJsonGet) | **GET** /content/{source}/{section}/{time-period}.json | 



## contentJsonGet

> ContentJsonGet200Response contentJsonGet(url)



### Example

```javascript
import TimesNewswireApi from 'times_newswire_api';
let defaultClient = TimesNewswireApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TimesNewswireApi.DefaultApi();
let url = "url_example"; // String | The complete URL of a specific news item, URL-encoded or backslash-escaped
apiInstance.contentJsonGet(url, (error, data, response) => {
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
 **url** | **String**| The complete URL of a specific news item, URL-encoded or backslash-escaped | 

### Return type

[**ContentJsonGet200Response**](ContentJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contentSourceSectionJsonGet

> ContentJsonGet200Response contentSourceSectionJsonGet(source, section, opts)



### Example

```javascript
import TimesNewswireApi from 'times_newswire_api';
let defaultClient = TimesNewswireApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TimesNewswireApi.DefaultApi();
let source = "source_example"; // String | Limits the set of items by originating source  all = items from both The New York Times and The International New York Times nyt = New York Times items only iht = International New York Times items only 
let section = "section_example"; // String | Limits the set of items by one or more sections all | One or more section names, separated by semicolons   To get all sections, specify all. To get a particular section or sections, use the section names returned by this request:  http://api.nytimes.com/svc/news/v3/content/section-list.json 
let opts = {
  'limit': 20, // Number | Limits the number of results, between 1 and 20
  'offset': 0 // Number | Sets the starting point of the result set
};
apiInstance.contentSourceSectionJsonGet(source, section, opts, (error, data, response) => {
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
 **source** | **String**| Limits the set of items by originating source  all &#x3D; items from both The New York Times and The International New York Times nyt &#x3D; New York Times items only iht &#x3D; International New York Times items only  | 
 **section** | **String**| Limits the set of items by one or more sections all | One or more section names, separated by semicolons   To get all sections, specify all. To get a particular section or sections, use the section names returned by this request:  http://api.nytimes.com/svc/news/v3/content/section-list.json  | 
 **limit** | **Number**| Limits the number of results, between 1 and 20 | [optional] [default to 20]
 **offset** | **Number**| Sets the starting point of the result set | [optional] [default to 0]

### Return type

[**ContentJsonGet200Response**](ContentJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contentSourceSectionTimePeriodJsonGet

> ContentJsonGet200Response contentSourceSectionTimePeriodJsonGet(source, section, timePeriod, opts)



### Example

```javascript
import TimesNewswireApi from 'times_newswire_api';
let defaultClient = TimesNewswireApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TimesNewswireApi.DefaultApi();
let source = "source_example"; // String | Limits the set of items by originating source  all = items from both The New York Times and The International New York Times nyt = New York Times items only iht = International New York Times items only 
let section = "section_example"; // String | Limits the set of items by one or more sections all | One or more section names, separated by semicolons   To get all sections, specify all. To get a particular section or sections, use the section names returned by this request:  http://api.nytimes.com/svc/news/v3/content/section-list.json 
let timePeriod = 56; // Number | Limits the set of items by time published, integer in number of hours
let opts = {
  'limit': 20, // Number | Limits the number of results, between 1 and 20
  'offset': 0 // Number | Sets the starting point of the result set
};
apiInstance.contentSourceSectionTimePeriodJsonGet(source, section, timePeriod, opts, (error, data, response) => {
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
 **source** | **String**| Limits the set of items by originating source  all &#x3D; items from both The New York Times and The International New York Times nyt &#x3D; New York Times items only iht &#x3D; International New York Times items only  | 
 **section** | **String**| Limits the set of items by one or more sections all | One or more section names, separated by semicolons   To get all sections, specify all. To get a particular section or sections, use the section names returned by this request:  http://api.nytimes.com/svc/news/v3/content/section-list.json  | 
 **timePeriod** | **Number**| Limits the set of items by time published, integer in number of hours | 
 **limit** | **Number**| Limits the number of results, between 1 and 20 | [optional] [default to 20]
 **offset** | **Number**| Sets the starting point of the result set | [optional] [default to 0]

### Return type

[**ContentJsonGet200Response**](ContentJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

