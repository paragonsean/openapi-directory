# UkParliamentSearchService.QueryApi

All URIs are relative to *https://api.parliament.uk/search*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queryExtensionGet**](QueryApi.md#queryExtensionGet) | **GET** /query.{extension} | Search results
[**queryGet**](QueryApi.md#queryGet) | **GET** /query | Search results



## queryExtensionGet

> queryExtensionGet(extension, q, opts)

Search results

### Example

```javascript
import UkParliamentSearchService from 'uk_parliament_search_service';

let apiInstance = new UkParliamentSearchService.QueryApi();
let extension = "extension_example"; // String | extension
let q = "q_example"; // String | 
let opts = {
  'start': 3.4, // Number | 
  'count': 3.4, // Number | 
  'subdomains': "subdomains_example", // String | 
  'inUrlPrefixes': "inUrlPrefixes_example" // String | 
};
apiInstance.queryExtensionGet(extension, q, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension** | **String**| extension | 
 **q** | **String**|  | 
 **start** | **Number**|  | [optional] 
 **count** | **Number**|  | [optional] 
 **subdomains** | **String**|  | [optional] 
 **inUrlPrefixes** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/atom+xml, application/json, application/rss+xml, text/html


## queryGet

> queryGet(q, opts)

Search results

### Example

```javascript
import UkParliamentSearchService from 'uk_parliament_search_service';

let apiInstance = new UkParliamentSearchService.QueryApi();
let q = "q_example"; // String | 
let opts = {
  'start': 3.4, // Number | 
  'count': 3.4, // Number | 
  'subdomains': "subdomains_example", // String | 
  'inUrlPrefixes': "inUrlPrefixes_example" // String | 
};
apiInstance.queryGet(q, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **String**|  | 
 **start** | **Number**|  | [optional] 
 **count** | **Number**|  | [optional] 
 **subdomains** | **String**|  | [optional] 
 **inUrlPrefixes** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/atom+xml, application/json, application/rss+xml, text/html

