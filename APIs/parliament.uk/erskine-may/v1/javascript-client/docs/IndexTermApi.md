# ErskineMayApi.IndexTermApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiIndexTermBrowseGet**](IndexTermApi.md#apiIndexTermBrowseGet) | **GET** /api/IndexTerm/browse | Returns a list of index terms by start letter.
[**apiIndexTermIndexTermIdGet**](IndexTermApi.md#apiIndexTermIndexTermIdGet) | **GET** /api/IndexTerm/{indexTermId} | Returns an index term by id.



## apiIndexTermBrowseGet

> ErskineMayIndexTermSearchResultErskineMaySearch apiIndexTermBrowseGet(opts)

Returns a list of index terms by start letter.

### Example

```javascript
import ErskineMayApi from 'erskine_may_api';

let apiInstance = new ErskineMayApi.IndexTermApi();
let opts = {
  'startLetter': "startLetter_example", // String | Index terms by start letter
  'skip': 0, // Number | The number of records to skip from the first, default is 0.
  'take': 20 // Number | The number of records to return, default is 20, maximum is 20.
};
apiInstance.apiIndexTermBrowseGet(opts, (error, data, response) => {
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
 **startLetter** | **String**| Index terms by start letter | [optional] 
 **skip** | **Number**| The number of records to skip from the first, default is 0. | [optional] [default to 0]
 **take** | **Number**| The number of records to return, default is 20, maximum is 20. | [optional] [default to 20]

### Return type

[**ErskineMayIndexTermSearchResultErskineMaySearch**](ErskineMayIndexTermSearchResultErskineMaySearch.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiIndexTermIndexTermIdGet

> ErskineMayIndexTerm apiIndexTermIndexTermIdGet(indexTermId)

Returns an index term by id.

### Example

```javascript
import ErskineMayApi from 'erskine_may_api';

let apiInstance = new ErskineMayApi.IndexTermApi();
let indexTermId = 56; // Number | Index term by if
apiInstance.apiIndexTermIndexTermIdGet(indexTermId, (error, data, response) => {
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
 **indexTermId** | **Number**| Index term by if | 

### Return type

[**ErskineMayIndexTerm**](ErskineMayIndexTerm.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

