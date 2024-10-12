# DracoonApi.UploadsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelFileUploadByToken**](UploadsApi.md#cancelFileUploadByToken) | **DELETE** /v4/uploads/{token} | Cancel file upload
[**completeFileUploadByToken**](UploadsApi.md#completeFileUploadByToken) | **PUT** /v4/uploads/{token} | Complete file upload
[**uploadFileByTokenAsMultipart1**](UploadsApi.md#uploadFileByTokenAsMultipart1) | **POST** /v4/uploads/{token} | Upload file



## cancelFileUploadByToken

> cancelFileUploadByToken(token)

Cancel file upload

### Description: Cancel file upload.  ### Precondition: Valid upload token.  ### Postcondition: Upload canceled, token invalidated and all already transfered chunks removed.  ### Further Information: It is recommended to notify the API about cancelled uploads if possible.

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.UploadsApi();
let token = "token_example"; // String | Upload token
apiInstance.cancelFileUploadByToken(token, (error, data, response) => {
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
 **token** | **String**| Upload token | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## completeFileUploadByToken

> Node completeFileUploadByToken(token, opts)

Complete file upload

### Description: Finish uploading a file.  ### Precondition: Valid upload token.  ### Postcondition: File created.  ### Further Information: The provided file name might be changed in accordance with the resolution strategy:  * **autorename**: changes the file name and adds a number to avoid conflicts. * **overwrite**: deletes any old file with the same file name. * **fail**: returns an error; in this case, another &#x60;PUT&#x60; request with a different file name may be sent.  Please ensure that all chunks have been transferred correctly before finishing the upload.  Download share id (if exists) gets changed if: - node with the same name exists in the target container - &#x60;resolutionStrategy&#x60; is &#x60;overwrite&#x60; - &#x60;keepShareLinks&#x60; is &#x60;true&#x60;

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.UploadsApi();
let token = "token_example"; // String | Upload token
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'completeUploadRequest': new DracoonApi.CompleteUploadRequest() // CompleteUploadRequest | 
};
apiInstance.completeFileUploadByToken(token, opts, (error, data, response) => {
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
 **token** | **String**| Upload token | 
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **completeUploadRequest** | [**CompleteUploadRequest**](CompleteUploadRequest.md)|  | [optional] 

### Return type

[**Node**](Node.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## uploadFileByTokenAsMultipart1

> ChunkUploadResponse uploadFileByTokenAsMultipart1(token, file, opts)

Upload file

### Description:   Upload a (chunk of a) file.  ### Precondition: Valid upload token.  ### Postcondition: Chunk uploaded.  ### Further Information: Range requests are supported.    Following &#x60;Content-Types&#x60; are supported by this API: * &#x60;multipart/form-data&#x60; * provided &#x60;Content-Type&#x60;  For both file upload types set the correct &#x60;Content-Type&#x60; header and body.    ### Examples:    * &#x60;multipart/form-data&#x60; &#x60;&#x60;&#x60; POST /api/v4/uploads/{token} HTTP/1.1  Header: ... Content-Type: multipart/form-data; boundary&#x3D;----WebKitFormBoundary7MA4YWxkTrZu0gW ...  Body: ------WebKitFormBoundary7MA4YWxkTrZu0gW Content-Disposition: form-data; name&#x3D;\&quot;file\&quot;; filename&#x3D;\&quot;file.txt\&quot; Content-Type: text/plain  Content of file.txt ------WebKitFormBoundary7MA4YWxkTrZu0gW-- &#x60;&#x60;&#x60;  * any other &#x60;Content-Type&#x60;  &#x60;&#x60;&#x60; POST /api/v4/uploads/{token} HTTP/1.1  Header: ... Content-Type: { ... } ...  Body: raw content &#x60;&#x60;&#x60; 

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.UploadsApi();
let token = "token_example"; // String | Upload token
let file = "/path/to/file"; // File | File
let opts = {
  'contentRange': "contentRange_example" // String | Content-Range   e.g. `bytes 0-999/3980`
};
apiInstance.uploadFileByTokenAsMultipart1(token, file, opts, (error, data, response) => {
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
 **token** | **String**| Upload token | 
 **file** | **File**| File | 
 **contentRange** | **String**| Content-Range   e.g. &#x60;bytes 0-999/3980&#x60; | [optional] 

### Return type

[**ChunkUploadResponse**](ChunkUploadResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

