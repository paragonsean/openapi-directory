# UuidGenerationApi.UUIDParsingApi

All URIs are relative to *https://api.fungenerators.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**uuidPost**](UUIDParsingApi.md#uuidPost) | **POST** /uuid | 



## uuidPost

> uuidPost(uuidstr)



Parse a UUID string and return its version and check whether it is valid.

### Example

```javascript
import UuidGenerationApi from 'uuid_generation_api';
let defaultClient = UuidGenerationApi.ApiClient.instance;
// Configure API key authorization: X-Fungenerators-Api-Secret
let X-Fungenerators-Api-Secret = defaultClient.authentications['X-Fungenerators-Api-Secret'];
X-Fungenerators-Api-Secret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Fungenerators-Api-Secret.apiKeyPrefix = 'Token';

let apiInstance = new UuidGenerationApi.UUIDParsingApi();
let uuidstr = "uuidstr_example"; // String | UUID String to parse
apiInstance.uuidPost(uuidstr, (error, data, response) => {
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
 **uuidstr** | **String**| UUID String to parse | 

### Return type

null (empty response body)

### Authorization

[X-Fungenerators-Api-Secret](../README.md#X-Fungenerators-Api-Secret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

