# DebianCodeSearch.SearchApi

All URIs are relative to *https://codesearch.debian.net/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **GET** /search | Searches through source code
[**searchperpackage**](SearchApi.md#searchperpackage) | **GET** /searchperpackage | Like /search, but aggregates per package



## search

> [SearchResult] search(query, opts)

Searches through source code

Performs a search through the full Debian Code Search corpus, blocking until all results are available (might take a few seconds depending on the search query).  Search results are ordered by their ranking (best results come first).

### Example

```javascript
import DebianCodeSearch from 'debian_code_search';
let defaultClient = DebianCodeSearch.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new DebianCodeSearch.SearchApi();
let query = "query_example"; // String | The search query, for example `who knows...` (literal) or `who knows\\.\\.\\.` (regular expression). See https://codesearch.debian.net/faq for more details about which keywords are supported. The regular expression flavor is RE2, see https://github.com/google/re2/blob/master/doc/syntax.txt
let opts = {
  'matchMode': "'regexp'" // String | Whether the query is to be interpreted as a literal (`literal`) instead of as an RE2 regular expression (`regexp`). Literal searches are faster and do not require escaping special characters, regular expression searches are more powerful.
};
apiInstance.search(query, opts, (error, data, response) => {
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
 **query** | **String**| The search query, for example &#x60;who knows...&#x60; (literal) or &#x60;who knows\\.\\.\\.&#x60; (regular expression). See https://codesearch.debian.net/faq for more details about which keywords are supported. The regular expression flavor is RE2, see https://github.com/google/re2/blob/master/doc/syntax.txt | 
 **matchMode** | **String**| Whether the query is to be interpreted as a literal (&#x60;literal&#x60;) instead of as an RE2 regular expression (&#x60;regexp&#x60;). Literal searches are faster and do not require escaping special characters, regular expression searches are more powerful. | [optional] [default to &#39;regexp&#39;]

### Return type

[**[SearchResult]**](SearchResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchperpackage

> [PackageSearchResult] searchperpackage(query, opts)

Like /search, but aggregates per package

The search results are currently sorted arbitrarily, but we intend to sort them by ranking eventually: https://github.com/Debian/dcs/blob/51338e934eb7ee18d00c5c18531c0790a83cb698/cmd/dcs-web/querymanager.go#L719

### Example

```javascript
import DebianCodeSearch from 'debian_code_search';
let defaultClient = DebianCodeSearch.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new DebianCodeSearch.SearchApi();
let query = "query_example"; // String | The search query, for example `who knows...` (literal) or `who knows\\.\\.\\.` (regular expression). See https://codesearch.debian.net/faq for more details about which keywords are supported. The regular expression flavor is RE2, see https://github.com/google/re2/blob/master/doc/syntax.txt
let opts = {
  'matchMode': "'regexp'" // String | Whether the query is to be interpreted as a literal (`literal`) instead of as an RE2 regular expression (`regexp`). Literal searches are faster and do not require escaping special characters, regular expression searches are more powerful.
};
apiInstance.searchperpackage(query, opts, (error, data, response) => {
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
 **query** | **String**| The search query, for example &#x60;who knows...&#x60; (literal) or &#x60;who knows\\.\\.\\.&#x60; (regular expression). See https://codesearch.debian.net/faq for more details about which keywords are supported. The regular expression flavor is RE2, see https://github.com/google/re2/blob/master/doc/syntax.txt | 
 **matchMode** | **String**| Whether the query is to be interpreted as a literal (&#x60;literal&#x60;) instead of as an RE2 regular expression (&#x60;regexp&#x60;). Literal searches are faster and do not require escaping special characters, regular expression searches are more powerful. | [optional] [default to &#39;regexp&#39;]

### Return type

[**[PackageSearchResult]**](PackageSearchResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

