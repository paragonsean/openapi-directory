# InfermedicaApi.SuggestApi

All URIs are relative to *https://api.infermedica.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSuggestions**](SuggestApi.md#getSuggestions) | **POST** /suggest | Query diagnostic engine for related symptoms



## getSuggestions

> [SuggestResult] getSuggestions(body, opts)

Query diagnostic engine for related symptoms

Suggests possible symptoms based on provided patient information.

### Example

```javascript
import InfermedicaApi from 'infermedica_api';

let apiInstance = new InfermedicaApi.SuggestApi();
let body = new InfermedicaApi.SuggestRequest(); // SuggestRequest | 
let opts = {
  'maxResults': 8 // Number | maximum number of results
};
apiInstance.getSuggestions(body, opts, (error, data, response) => {
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
 **body** | [**SuggestRequest**](SuggestRequest.md)|  | 
 **maxResults** | **Number**| maximum number of results | [optional] [default to 8]

### Return type

[**[SuggestResult]**](SuggestResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

