# ApiDocsLogoraisrCom.UploadsApi

All URIs are relative to *https://api.logoraisr.com/rest-v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**uploadsCreate**](UploadsApi.md#uploadsCreate) | **POST** /uploads/ | Upload a new image



## uploadsCreate

> FileResponse uploadsCreate(file)

Upload a new image

This POST-Method uploads a new file on the server.

### Example

```javascript
import ApiDocsLogoraisrCom from 'api_docs___logoraisr_com';
let defaultClient = ApiDocsLogoraisrCom.ApiClient.instance;
// Configure API key authorization: Token
let Token = defaultClient.authentications['Token'];
Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Token.apiKeyPrefix = 'Token';

let apiInstance = new ApiDocsLogoraisrCom.UploadsApi();
let file = "/path/to/file"; // File | File which should be uploaded. Supported file types are: JPEG and PNG
apiInstance.uploadsCreate(file, (error, data, response) => {
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
 **file** | **File**| File which should be uploaded. Supported file types are: JPEG and PNG | 

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

