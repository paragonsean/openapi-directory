# ApiDocsLogoraisrCom.ProcessesApi

All URIs are relative to *https://api.logoraisr.com/rest-v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**processesList**](ProcessesApi.md#processesList) | **GET** /processes/ | Get process list.



## processesList

> Process processesList()

Get process list.

This GET-Method lists all on logoraisr available processes.

### Example

```javascript
import ApiDocsLogoraisrCom from 'api_docs___logoraisr_com';
let defaultClient = ApiDocsLogoraisrCom.ApiClient.instance;
// Configure API key authorization: Token
let Token = defaultClient.authentications['Token'];
Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token.apiKeyPrefix = 'Token';

let apiInstance = new ApiDocsLogoraisrCom.ProcessesApi();
apiInstance.processesList((error, data, response) => {
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

[**Process**](Process.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

