# IsbNdbApi.SearchApi

All URIs are relative to *https://api.isbndb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchGet**](SearchApi.md#searchGet) | **GET** /search | Search all ISBNDB databases



## searchGet

> searchGet(opts)

Search all ISBNDB databases

Uses a free query string compatible with ElasticSearch 6 to search in any of the ISBNDB&#39;s databases

### Example

```javascript
import IsbNdbApi from 'isb_ndb_api';
let defaultClient = IsbNdbApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new IsbNdbApi.SearchApi();
let opts = {
  'q': "q_example" // String | A query string compatible with ElasticSearch 6
};
apiInstance.searchGet(opts, (error, data, response) => {
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
 **q** | **String**| A query string compatible with ElasticSearch 6 | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

