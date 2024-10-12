# AnchoreEngineApiServer.ImportApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**importImageArchive**](ImportApi.md#importImageArchive) | **POST** /import/images | Import an anchore image tar.gz archive file. This is a deprecated API replaced by the \&quot;/imports/images\&quot; route



## importImageArchive

> [AnchoreImage] importImageArchive(archiveFile)

Import an anchore image tar.gz archive file. This is a deprecated API replaced by the \&quot;/imports/images\&quot; route

### Example

```javascript
import AnchoreEngineApiServer from 'anchore_engine_api_server';

let apiInstance = new AnchoreEngineApiServer.ImportApi();
let archiveFile = "/path/to/file"; // File | anchore image tar archive.
apiInstance.importImageArchive(archiveFile, (error, data, response) => {
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
 **archiveFile** | **File**| anchore image tar archive. | 

### Return type

[**[AnchoreImage]**](AnchoreImage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

