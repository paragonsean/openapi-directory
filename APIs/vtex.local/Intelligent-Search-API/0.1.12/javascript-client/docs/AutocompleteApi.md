# IntelligentSearchApi.AutocompleteApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocompleteSuggestionsGet**](AutocompleteApi.md#autocompleteSuggestionsGet) | **GET** /autocomplete_suggestions | Get list of suggested terms and attributes similar to the search term
[**topSearchesGet**](AutocompleteApi.md#topSearchesGet) | **GET** /top_searches | Get list of the 10 most searched terms



## autocompleteSuggestionsGet

> AutocompleteSearchSuggestions autocompleteSuggestionsGet(opts)

Get list of suggested terms and attributes similar to the search term

Lists the suggested terms and attributes similar to the search term.

### Example

```javascript
import IntelligentSearchApi from 'intelligent_search_api';

let apiInstance = new IntelligentSearchApi.AutocompleteApi();
let opts = {
  'query': "query_example", // String | Search term. It can contain any character.
  'locale': "en-US" // String | Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
};
apiInstance.autocompleteSuggestionsGet(opts, (error, data, response) => {
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
 **query** | **String**| Search term. It can contain any character. | [optional] 
 **locale** | **String**| Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language. | [optional] 

### Return type

[**AutocompleteSearchSuggestions**](AutocompleteSearchSuggestions.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## topSearchesGet

> TopSearches topSearchesGet(opts)

Get list of the 10 most searched terms

Lists the 10 most searched terms.

### Example

```javascript
import IntelligentSearchApi from 'intelligent_search_api';

let apiInstance = new IntelligentSearchApi.AutocompleteApi();
let opts = {
  'locale': "en-US" // String | Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
};
apiInstance.topSearchesGet(opts, (error, data, response) => {
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
 **locale** | **String**| Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language. | [optional] 

### Return type

[**TopSearches**](TopSearches.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

