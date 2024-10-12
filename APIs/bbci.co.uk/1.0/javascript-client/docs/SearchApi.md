# BbcIPlayerBusinessLayer.SearchApi

All URIs are relative to *https://ibl.api.bbci.co.uk/ibl/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SearchApi.md#search) | **GET** /search | Search
[**searchSuggest**](SearchApi.md#searchSuggest) | **GET** /search-suggest | Search-suggest



## search

> Object search(q, lang, rights, availability)

Search

Search

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.SearchApi();
let q = "q_example"; // String | The term to search for.
let lang = "lang_example"; // String | The language for any applicable localised strings.
let rights = "'web'"; // String | The rights group to limit results to.
let availability = "'available'"; // String | Whether to return all, or available programmes
apiInstance.search(q, lang, rights, availability, (error, data, response) => {
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
 **q** | **String**| The term to search for. | 
 **lang** | **String**| The language for any applicable localised strings. | 
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchSuggest

> Object searchSuggest(q, lang, rights, availability)

Search-suggest

Search-suggest

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.SearchApi();
let q = "q_example"; // String | The term to search for.
let lang = "lang_example"; // String | The language for any applicable localised strings.
let rights = "'web'"; // String | The rights group to limit results to.
let availability = "'available'"; // String | Whether to return all, or available programmes
apiInstance.searchSuggest(q, lang, rights, availability, (error, data, response) => {
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
 **q** | **String**| The term to search for. | 
 **lang** | **String**| The language for any applicable localised strings. | 
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

