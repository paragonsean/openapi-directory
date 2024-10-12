# TimesTagsApi.DefaultApi

All URIs are relative to *http://api.nytimes.com/svc/suggest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timestagsGet**](DefaultApi.md#timestagsGet) | **GET** /timestags | 



## timestagsGet

> [[String]] timestagsGet(query, opts)



### Example

```javascript
import TimesTagsApi from 'times_tags_api';
let defaultClient = TimesTagsApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TimesTagsApi.DefaultApi();
let query = "query_example"; // String | Your search query
let opts = {
  'filter': "filter_example", // String | If you do not specify a value for filter (see the Optional Parameters), your query will be matched to tags in all four Times dictionaries: subject, geographic location, organization and person. To use more than one, separate with commas. 
  'max': 10 // Number | Sets the maximum number of results
};
apiInstance.timestagsGet(query, opts, (error, data, response) => {
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
 **query** | **String**| Your search query | 
 **filter** | **String**| If you do not specify a value for filter (see the Optional Parameters), your query will be matched to tags in all four Times dictionaries: subject, geographic location, organization and person. To use more than one, separate with commas.  | [optional] 
 **max** | **Number**| Sets the maximum number of results | [optional] [default to 10]

### Return type

**[[String]]**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

