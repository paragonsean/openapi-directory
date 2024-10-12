# PdfBrokerIoApi.PdfApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPdfGet**](PdfApi.md#apiPdfGet) | **GET** /api/pdf | Basic method to verify api is up and running
[**apiPdfPdfconcatPost**](PdfApi.md#apiPdfPdfconcatPost) | **POST** /api/pdf/pdfconcat | Concatenate multiple pdf files into single pdf file..
[**apiPdfPdftoimagePost**](PdfApi.md#apiPdfPdftoimagePost) | **POST** /api/pdf/pdftoimage | Generate an image of to provided pdf file
[**apiPdfPdfwritestringPost**](PdfApi.md#apiPdfPdfwritestringPost) | **POST** /api/pdf/pdfwritestring | Write text on a page in a pdf document.
[**apiPdfWkhtmltopdfPost**](PdfApi.md#apiPdfWkhtmltopdfPost) | **POST** /api/pdf/wkhtmltopdf | Generate pdf file from url using the excellent tool wkhtmltopdf.
[**apiPdfXslfoPost**](PdfApi.md#apiPdfXslfoPost) | **POST** /api/pdf/xslfo | Create pdf-file from complete XSL-FO document.
[**apiPdfXslfowithtransformPost**](PdfApi.md#apiPdfXslfowithtransformPost) | **POST** /api/pdf/xslfowithtransform | Create pdf-file from transforming xml document with Xsl-Fo transform document.



## apiPdfGet

> apiPdfGet()

Basic method to verify api is up and running

### Example

```javascript
import PdfBrokerIoApi from 'pdf_broker_io_api';
let defaultClient = PdfBrokerIoApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PdfBrokerIoApi.PdfApi();
apiInstance.apiPdfGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPdfPdfconcatPost

> PdfResponseDto apiPdfPdfconcatPost(opts)

Concatenate multiple pdf files into single pdf file..

### Example

```javascript
import PdfBrokerIoApi from 'pdf_broker_io_api';
let defaultClient = PdfBrokerIoApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PdfBrokerIoApi.PdfApi();
let opts = {
  'pdfConcatenationRequestDto': {
  "pdfDocumentsAsBase64String": [
    "<Encode your pdf documents as Base64 encoded string>",
    "<Encode your pdf documents as Base64 encoded string>"
  ]
} // PdfConcatenationRequestDto | PdfConcat Request. Add two or more pdf files and concatenate pages into single pdf document.
};
apiInstance.apiPdfPdfconcatPost(opts, (error, data, response) => {
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
 **pdfConcatenationRequestDto** | [**PdfConcatenationRequestDto**](PdfConcatenationRequestDto.md)| PdfConcat Request. Add two or more pdf files and concatenate pages into single pdf document. | [optional] 

### Return type

[**PdfResponseDto**](PdfResponseDto.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json, application/pdf


## apiPdfPdftoimagePost

> ImageResponseDto apiPdfPdftoimagePost(opts)

Generate an image of to provided pdf file

### Example

```javascript
import PdfBrokerIoApi from 'pdf_broker_io_api';
let defaultClient = PdfBrokerIoApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PdfBrokerIoApi.PdfApi();
let opts = {
  'pdfToImageRequestDto': {
  "pdfFileBase64String": "<Encode your existing PDF document as Base64 encoded string>",
  "options": {
    "pageNumber": 1,
    "imageFormat": "image/jpeg",
    "horizontalResolution": 96.0,
    "verticalResolution": 96.0,
    "width": 0,
    "height": 0,
    "transparent": false,
    "jpegQuality": 90,
    "pngCompressionLevel": 6
  }
} // PdfToImageRequestDto | PdfToImage Request. Create an image of a page in an existing pdf document.
};
apiInstance.apiPdfPdftoimagePost(opts, (error, data, response) => {
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
 **pdfToImageRequestDto** | [**PdfToImageRequestDto**](PdfToImageRequestDto.md)| PdfToImage Request. Create an image of a page in an existing pdf document. | [optional] 

### Return type

[**ImageResponseDto**](ImageResponseDto.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json, image/gif, image/jpeg, image/png


## apiPdfPdfwritestringPost

> PdfResponseDto apiPdfPdfwritestringPost(opts)

Write text on a page in a pdf document.

### Example

```javascript
import PdfBrokerIoApi from 'pdf_broker_io_api';
let defaultClient = PdfBrokerIoApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PdfBrokerIoApi.PdfApi();
let opts = {
  'pdfWriteStringRequestDto': {
  "pdfFileBase64String": "<Encode your existing PDF document as Base64 encoded string>",
  "options": {
    "text": "This is test string",
    "textColor": {
      "r": 33,
      "g": 34,
      "b": 35
    },
    "font": {
      "name": "Arial",
      "size": 24.0,
      "style": 1
    },
    "pageNumber": 3,
    "xPosition": 40.0,
    "yPosition": -200.0,
    "xOrigin": 1,
    "yOrigin": 2
  },
  "fontFileBase64String": "<Attach your own TrueTypeFont file if necessary to style text, encoded as Base64 encoded string>"
} // PdfWriteStringRequestDto | PdfWriteString Request. Write string on page in pdf document
};
apiInstance.apiPdfPdfwritestringPost(opts, (error, data, response) => {
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
 **pdfWriteStringRequestDto** | [**PdfWriteStringRequestDto**](PdfWriteStringRequestDto.md)| PdfWriteString Request. Write string on page in pdf document | [optional] 

### Return type

[**PdfResponseDto**](PdfResponseDto.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json, application/pdf


## apiPdfWkhtmltopdfPost

> PdfResponseDto apiPdfWkhtmltopdfPost(opts)

Generate pdf file from url using the excellent tool wkhtmltopdf.

### Example

```javascript
import PdfBrokerIoApi from 'pdf_broker_io_api';
let defaultClient = PdfBrokerIoApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PdfBrokerIoApi.PdfApi();
let opts = {
  'wkHtmlToPdfRequestDto': {
  "url": "https://www.pdfbroker.io",
  "htmlBase64String": null,
  "wkHtmlToPdfArguments": {
    "grayscale": "",
    "viewport-size": "1280x1024"
  },
  "resources": null
} // WkHtmlToPdfRequestDto | WkHtmlToPdf Request. Generate pdf from html, either from url or base64 encoded html string
};
apiInstance.apiPdfWkhtmltopdfPost(opts, (error, data, response) => {
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
 **wkHtmlToPdfRequestDto** | [**WkHtmlToPdfRequestDto**](WkHtmlToPdfRequestDto.md)| WkHtmlToPdf Request. Generate pdf from html, either from url or base64 encoded html string | [optional] 

### Return type

[**PdfResponseDto**](PdfResponseDto.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/pdf


## apiPdfXslfoPost

> PdfResponseDto apiPdfXslfoPost(opts)

Create pdf-file from complete XSL-FO document.

### Example

```javascript
import PdfBrokerIoApi from 'pdf_broker_io_api';
let defaultClient = PdfBrokerIoApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PdfBrokerIoApi.PdfApi();
let opts = {
  'foRequestDto': {
  "foDocumentBase64String": "<Encode your XSL-FO document as Base64 encoded string>",
  "resources": {
    "<Use file name as key, i.e 'logo.png', which is set as src on fo:external-graphic elements>": "<Convert your images to Base64 encoded string>"
  },
  "metadata": {
    "title": "Pdf title metadata can be set with metadata object",
    "author": null,
    "subject": null,
    "keywords": [
      "pdf",
      "api"
    ],
    "enableAdd": true,
    "enableCopy": true,
    "enableModify": true,
    "enablePrinting": true,
    "ownerPassword": null,
    "userPassword": null
  }
} // FoRequestDto | XSL-FO Request, the basic XSL-FO request. Post your XSL-FO document and digital resources, either as 'multipart/form-data' or 'application/json'
};
apiInstance.apiPdfXslfoPost(opts, (error, data, response) => {
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
 **foRequestDto** | [**FoRequestDto**](FoRequestDto.md)| XSL-FO Request, the basic XSL-FO request. Post your XSL-FO document and digital resources, either as &#39;multipart/form-data&#39; or &#39;application/json&#39; | [optional] 

### Return type

[**PdfResponseDto**](PdfResponseDto.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json, application/pdf


## apiPdfXslfowithtransformPost

> PdfResponseDto apiPdfXslfowithtransformPost(opts)

Create pdf-file from transforming xml document with Xsl-Fo transform document.

### Example

```javascript
import PdfBrokerIoApi from 'pdf_broker_io_api';
let defaultClient = PdfBrokerIoApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PdfBrokerIoApi.PdfApi();
let opts = {
  'foTransformRequestDto': {
  "xmlDataDocumentBase64String": "<This is the document which contains your data that the XSL-FO transform will be applied on. Send as Base64 encoded string>",
  "foDocumentBase64String": "<Encode your XSL-FO transform document as Base64 encoded string>",
  "resources": {
    "<Use file name as key, i.e 'logo.png', which is set as src on fo:external-graphic elements>": "<Convert your images to Base64 encoded string>"
  },
  "metadata": null
} // FoTransformRequestDto | XSL-FO Transform Request. The XSL-FO is transformed on the supplied xml data document. Post your XSL-FO transform document and xml data document aloing with your digital resources, either as 'multipart/form-data' or 'application/json'
};
apiInstance.apiPdfXslfowithtransformPost(opts, (error, data, response) => {
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
 **foTransformRequestDto** | [**FoTransformRequestDto**](FoTransformRequestDto.md)| XSL-FO Transform Request. The XSL-FO is transformed on the supplied xml data document. Post your XSL-FO transform document and xml data document aloing with your digital resources, either as &#39;multipart/form-data&#39; or &#39;application/json&#39; | [optional] 

### Return type

[**PdfResponseDto**](PdfResponseDto.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json, application/pdf

