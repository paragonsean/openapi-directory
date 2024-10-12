# GeneeaNaturalLanguageProcessing.AccountApi

All URIs are relative to *https://api.geneea.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getInfo**](AccountApi.md#getInfo) | **GET** /account | Information about current user account



## getInfo

> Object getInfo()

Information about current user account

getInfo

### Example

```javascript
import GeneeaNaturalLanguageProcessing from 'geneea_natural_language_processing';
let defaultClient = GeneeaNaturalLanguageProcessing.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new GeneeaNaturalLanguageProcessing.AccountApi();
apiInstance.getInfo((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

