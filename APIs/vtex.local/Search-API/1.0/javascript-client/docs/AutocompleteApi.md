# LegacySearchApi.AutocompleteApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autoComplete**](AutocompleteApi.md#autoComplete) | **GET** /buscaautocomplete | Product Search Autocomplete



## autoComplete

> TheRootSchema autoComplete(contentType, accept, productNameContains)

Product Search Autocomplete

Retrieves product&#39;s information related to the searched string.  &#x60;{{searchString}} is the part of string the user is looking for.  E.g.: &#x60;ref&#x60; | &#x60;refrig&#x60; | &#x60;refrigerator&#x60;

### Example

```javascript
import LegacySearchApi from 'legacy_search_api';
let defaultClient = LegacySearchApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new LegacySearchApi.AutocompleteApi();
let contentType = "application/json"; // String | Type of the content being sent
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
let productNameContains = "jeans"; // String | Part of the string that will be searched.
apiInstance.autoComplete(contentType, accept, productNameContains, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent | 
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | 
 **productNameContains** | **String**| Part of the string that will be searched. | 

### Return type

[**TheRootSchema**](TheRootSchema.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

