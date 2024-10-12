# EasyPdfServer.DefaultApi

All URIs are relative to *https://api.easypdfserver.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**makePdfPost**](DefaultApi.md#makePdfPost) | **POST** /make-pdf | Generate a PDF from HTML or URL.



## makePdfPost

> File makePdfPost(makePdfPostRequest)

Generate a PDF from HTML or URL.

### Example

```javascript
import EasyPdfServer from 'easy_pdf_server';

let apiInstance = new EasyPdfServer.DefaultApi();
let makePdfPostRequest = new EasyPdfServer.MakePdfPostRequest(); // MakePdfPostRequest | Pass the API key from easypdfserver.com and either HTML or URL to generate your PDF.
apiInstance.makePdfPost(makePdfPostRequest, (error, data, response) => {
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
 **makePdfPostRequest** | [**MakePdfPostRequest**](MakePdfPostRequest.md)| Pass the API key from easypdfserver.com and either HTML or URL to generate your PDF. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/pdf

