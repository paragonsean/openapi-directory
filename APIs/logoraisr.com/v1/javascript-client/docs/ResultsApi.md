# ApiDocsLogoraisrCom.ResultsApi

All URIs are relative to *https://api.logoraisr.com/rest-v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resultsRead**](ResultsApi.md#resultsRead) | **GET** /results/{result_file_id}/ | Get the result from image processing



## resultsRead

> ResultResponse resultsRead(resultFileId)

Get the result from image processing

This GET-Method returns the URL where the result can downloaded from.

### Example

```javascript
import ApiDocsLogoraisrCom from 'api_docs___logoraisr_com';
let defaultClient = ApiDocsLogoraisrCom.ApiClient.instance;
// Configure API key authorization: Token
let Token = defaultClient.authentications['Token'];
Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token.apiKeyPrefix = 'Token';

let apiInstance = new ApiDocsLogoraisrCom.ResultsApi();
let resultFileId = "resultFileId_example"; // String | Id of the result_file for which the result_file_url is generated.
apiInstance.resultsRead(resultFileId, (error, data, response) => {
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
 **resultFileId** | **String**| Id of the result_file for which the result_file_url is generated. | 

### Return type

[**ResultResponse**](ResultResponse.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

