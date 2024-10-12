# ErskineMayApi.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiSearchIndexTermSearchResultsSearchTermGet**](SearchApi.md#apiSearchIndexTermSearchResultsSearchTermGet) | **GET** /api/Search/IndexTermSearchResults/{searchTerm} | Returns a list of index terms which contain the search term.
[**apiSearchParagraphReferenceGet**](SearchApi.md#apiSearchParagraphReferenceGet) | **GET** /api/Search/Paragraph/{reference} | Returns a section overview by reference.
[**apiSearchParagraphSearchResultsSearchTermGet**](SearchApi.md#apiSearchParagraphSearchResultsSearchTermGet) | **GET** /api/Search/ParagraphSearchResults/{searchTerm} | Returns a list of paragraphs which contain the search term.
[**apiSearchSectionSearchResultsSearchTermGet**](SearchApi.md#apiSearchSectionSearchResultsSearchTermGet) | **GET** /api/Search/SectionSearchResults/{searchTerm} | Returns a list of sections which contain the search term.



## apiSearchIndexTermSearchResultsSearchTermGet

> ErskineMayIndexTermSearchResultErskineMaySearch apiSearchIndexTermSearchResultsSearchTermGet(searchTerm, opts)

Returns a list of index terms which contain the search term.

### Example

```javascript
import ErskineMayApi from 'erskine_may_api';

let apiInstance = new ErskineMayApi.SearchApi();
let searchTerm = "searchTerm_example"; // String | Index terms which contain search term.
let opts = {
  'skip': 0, // Number | The number of records to skip from the first, default is 0.
  'take': 20 // Number | The number of records to return, default is 20, maximum is 20.
};
apiInstance.apiSearchIndexTermSearchResultsSearchTermGet(searchTerm, opts, (error, data, response) => {
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
 **searchTerm** | **String**| Index terms which contain search term. | 
 **skip** | **Number**| The number of records to skip from the first, default is 0. | [optional] [default to 0]
 **take** | **Number**| The number of records to return, default is 20, maximum is 20. | [optional] [default to 20]

### Return type

[**ErskineMayIndexTermSearchResultErskineMaySearch**](ErskineMayIndexTermSearchResultErskineMaySearch.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiSearchParagraphReferenceGet

> ErskineMaySectionOverview apiSearchParagraphReferenceGet(reference)

Returns a section overview by reference.

### Example

```javascript
import ErskineMayApi from 'erskine_may_api';

let apiInstance = new ErskineMayApi.SearchApi();
let reference = "reference_example"; // String | Section overview by reference.
apiInstance.apiSearchParagraphReferenceGet(reference, (error, data, response) => {
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
 **reference** | **String**| Section overview by reference. | 

### Return type

[**ErskineMaySectionOverview**](ErskineMaySectionOverview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiSearchParagraphSearchResultsSearchTermGet

> ErskineMayParagraphSearchResultErskineMaySearch apiSearchParagraphSearchResultsSearchTermGet(searchTerm, opts)

Returns a list of paragraphs which contain the search term.

### Example

```javascript
import ErskineMayApi from 'erskine_may_api';

let apiInstance = new ErskineMayApi.SearchApi();
let searchTerm = "searchTerm_example"; // String | Paragraphs which contain search term in their content.
let opts = {
  'skip': 0, // Number | The number of records to skip from the first, default is 0.
  'take': 20 // Number | The number of records to return, default is 20, maximum is 20.
};
apiInstance.apiSearchParagraphSearchResultsSearchTermGet(searchTerm, opts, (error, data, response) => {
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
 **searchTerm** | **String**| Paragraphs which contain search term in their content. | 
 **skip** | **Number**| The number of records to skip from the first, default is 0. | [optional] [default to 0]
 **take** | **Number**| The number of records to return, default is 20, maximum is 20. | [optional] [default to 20]

### Return type

[**ErskineMayParagraphSearchResultErskineMaySearch**](ErskineMayParagraphSearchResultErskineMaySearch.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiSearchSectionSearchResultsSearchTermGet

> ErskineMaySectionSearchResultErskineMaySearch apiSearchSectionSearchResultsSearchTermGet(searchTerm, opts)

Returns a list of sections which contain the search term.

### Example

```javascript
import ErskineMayApi from 'erskine_may_api';

let apiInstance = new ErskineMayApi.SearchApi();
let searchTerm = "searchTerm_example"; // String | Sections which contain search term in their title.
let opts = {
  'skip': 0, // Number | The number of records to skip from the first, default is 0.
  'take': 20 // Number | The number of records to return, default is 20, maximum is 20.
};
apiInstance.apiSearchSectionSearchResultsSearchTermGet(searchTerm, opts, (error, data, response) => {
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
 **searchTerm** | **String**| Sections which contain search term in their title. | 
 **skip** | **Number**| The number of records to skip from the first, default is 0. | [optional] [default to 0]
 **take** | **Number**| The number of records to return, default is 20, maximum is 20. | [optional] [default to 20]

### Return type

[**ErskineMaySectionSearchResultErskineMaySearch**](ErskineMaySectionSearchResultErskineMaySearch.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

