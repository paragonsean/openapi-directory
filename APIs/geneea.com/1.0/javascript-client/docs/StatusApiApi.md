# GeneeaNaturalLanguageProcessing.StatusApiApi

All URIs are relative to *https://api.geneea.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status**](StatusApiApi.md#status) | **GET** /status | Gets status of the Interpretor service



## status

> String status()

Gets status of the Interpretor service

status

### Example

```javascript
import GeneeaNaturalLanguageProcessing from 'geneea_natural_language_processing';
let defaultClient = GeneeaNaturalLanguageProcessing.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new GeneeaNaturalLanguageProcessing.StatusApiApi();
apiInstance.status((error, data, response) => {
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

**String**

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json

