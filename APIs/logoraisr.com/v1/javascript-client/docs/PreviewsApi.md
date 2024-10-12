# ApiDocsLogoraisrCom.PreviewsApi

All URIs are relative to *https://api.logoraisr.com/rest-v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**previewsRead**](PreviewsApi.md#previewsRead) | **GET** /previews/{file_id}/ | Get preview image of uploaded file



## previewsRead

> PreviewResponse previewsRead(fileId)

Get preview image of uploaded file

This GET-Method returns the URL where the preview image of uploaded file can downloaded from.

### Example

```javascript
import ApiDocsLogoraisrCom from 'api_docs___logoraisr_com';
let defaultClient = ApiDocsLogoraisrCom.ApiClient.instance;
// Configure API key authorization: Token
let Token = defaultClient.authentications['Token'];
Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token.apiKeyPrefix = 'Token';

let apiInstance = new ApiDocsLogoraisrCom.PreviewsApi();
let fileId = "fileId_example"; // String | Id of the file for which the preview_img_url is generated.
apiInstance.previewsRead(fileId, (error, data, response) => {
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
 **fileId** | **String**| Id of the file for which the preview_img_url is generated. | 

### Return type

[**PreviewResponse**](PreviewResponse.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

