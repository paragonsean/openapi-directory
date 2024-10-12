# BcLaws.SearchApi

All URIs are relative to *http://www.bclaws.ca/civix*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchAspectIdFullsearchGet**](SearchApi.md#searchAspectIdFullsearchGet) | **GET** /search/{aspectId}/fullsearch | A listing of metadata available for the specified aspect and search term from the BCLaws legislative repository



## searchAspectIdFullsearchGet

> searchAspectIdFullsearchGet(aspectId, q, s, e, nFrag, lFrag)

A listing of metadata available for the specified aspect and search term from the BCLaws legislative repository

### Example

```javascript
import BcLaws from 'bc_laws';

let apiInstance = new BcLaws.SearchApi();
let aspectId = "'complete'"; // String | The identifier of the 'aspect' (content group) to search
let q = "'water'"; // String | query term
let s = "'0'"; // String | first hit (start index)
let e = 20; // Number | last hit (end index)
let nFrag = 5; // Number | number of fragment snippets to return (< 10)
let lFrag = 100; // Number | length of fragment snippets (< 200)
apiInstance.searchAspectIdFullsearchGet(aspectId, q, s, e, nFrag, lFrag, (error, data, response) => {
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
 **aspectId** | **String**| The identifier of the &#39;aspect&#39; (content group) to search | [default to &#39;complete&#39;]
 **q** | **String**| query term | [default to &#39;water&#39;]
 **s** | **String**| first hit (start index) | [default to &#39;0&#39;]
 **e** | **Number**| last hit (end index) | [default to 20]
 **nFrag** | **Number**| number of fragment snippets to return (&lt; 10) | [default to 5]
 **lFrag** | **Number**| length of fragment snippets (&lt; 200) | [default to 100]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

