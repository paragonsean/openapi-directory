# PdfBlocksApi.DefaultApi

All URIs are relative to *https://api.pdfblocks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addImageWatermarkV1**](DefaultApi.md#addImageWatermarkV1) | **POST** /v1/add_watermark/image | Add an image watermark to a PDF
[**addPasswordV1**](DefaultApi.md#addPasswordV1) | **POST** /v1/add_password | Add a password to a PDF
[**addRestrictionsV1**](DefaultApi.md#addRestrictionsV1) | **POST** /v1/add_restrictions | Add restrictions to a PDF
[**addTextWatermarkV1**](DefaultApi.md#addTextWatermarkV1) | **POST** /v1/add_watermark/text | Add a text watermark to a PDF
[**extractPagesV1**](DefaultApi.md#extractPagesV1) | **POST** /v1/extract_pages | Extract pages from a PDF
[**mergeDocumentsV1**](DefaultApi.md#mergeDocumentsV1) | **POST** /v1/merge_documents | Merge PDF documents
[**removePagesV1**](DefaultApi.md#removePagesV1) | **POST** /v1/remove_pages | Remove pages from a PDF
[**removePasswordV1**](DefaultApi.md#removePasswordV1) | **POST** /v1/remove_password | Remove the password from a PDF
[**removeRestrictionsV1**](DefaultApi.md#removeRestrictionsV1) | **POST** /v1/remove_restrictions | Remove the restrictions from a PDF
[**removeSignaturesV1**](DefaultApi.md#removeSignaturesV1) | **POST** /v1/remove_signatures | Remove the signatures from a PDF
[**reversePagesV1**](DefaultApi.md#reversePagesV1) | **POST** /v1/reverse_pages | Reverse the pages of a PDF
[**rotatePagesV1**](DefaultApi.md#rotatePagesV1) | **POST** /v1/rotate_pages | Rotate pages in a PDF



## addImageWatermarkV1

> File addImageWatermarkV1(file, image, opts)

Add an image watermark to a PDF

Add an image watermark to each page of a PDF document.

### Example

```javascript
import PdfBlocksApi from 'pdf_blocks_api';
let defaultClient = PdfBlocksApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new PdfBlocksApi.DefaultApi();
let file = "/path/to/file"; // File | The input PDF document
let image = "/path/to/file"; // File | The image to add as a watermark. The format of the image can be either PNG or JPEG.
let opts = {
  'margin': 1, // Number | The distance in inches from the border of the page to the image watermark.
  'transparency': 50 // Number | The transparency level for the image watermark from 0 (opaque) to 100 (transparent).
};
apiInstance.addImageWatermarkV1(file, image, opts, (error, data, response) => {
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
 **file** | **File**| The input PDF document | 
 **image** | **File**| The image to add as a watermark. The format of the image can be either PNG or JPEG. | 
 **margin** | **Number**| The distance in inches from the border of the page to the image watermark. | [optional] [default to 1]
 **transparency** | **Number**| The transparency level for the image watermark from 0 (opaque) to 100 (transparent). | [optional] [default to 50]

### Return type

**File**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/pdf, application/problem+json


## addPasswordV1

> File addPasswordV1(file, password, opts)

Add a password to a PDF

Protect a PDF document with a password. Encrypt the PDF document to prevent unauthorized access.

### Example

```javascript
import PdfBlocksApi from 'pdf_blocks_api';
let defaultClient = PdfBlocksApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new PdfBlocksApi.DefaultApi();
let file = "/path/to/file"; // File | The input PDF document
let password = "password_example"; // String | The password required to open the file.
let opts = {
  'encryptionAlgorithm': "'AES-128'" // String | The algorithm used to encrypt the PDF document.
};
apiInstance.addPasswordV1(file, password, opts, (error, data, response) => {
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
 **file** | **File**| The input PDF document | 
 **password** | **String**| The password required to open the file. | 
 **encryptionAlgorithm** | **String**| The algorithm used to encrypt the PDF document. | [optional] [default to &#39;AES-128&#39;]

### Return type

**File**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/pdf, application/problem+json


## addRestrictionsV1

> File addRestrictionsV1(file, ownerPassword, opts)

Add restrictions to a PDF

Add restrictions to prevent copying, printing, and modifying a PDF document.

### Example

```javascript
import PdfBlocksApi from 'pdf_blocks_api';
let defaultClient = PdfBlocksApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new PdfBlocksApi.DefaultApi();
let file = "/path/to/file"; // File | The input PDF document
let ownerPassword = "ownerPassword_example"; // String | The password required to open and change permissions of the PDF document.
let opts = {
  'allowAccessibility': true, // Boolean | If false, accessibility programs can't read the text or images of the document.
  'allowAssembleDocument': true, // Boolean | If false, the user can't assemble or manipulate the document.
  'allowChangeContent': true, // Boolean | If false, the user can't change the content of the document.
  'allowCommentAndFillForm': true, // Boolean | If false, the user can't add, edit or modify annotations or fill form fields.
  'allowCopyContent': true, // Boolean | If false, the user can't copy text and images to the clipboard.
  'allowFillForm': true, // Boolean | If false, the user can't fill forms fields.
  'allowPrint': true, // Boolean | If false, the user can't print the document.
  'allowPrintHighResolution': true, // Boolean | If false, the user can't print the document in high resolution.
  'encryptionAlgorithm': "'AES-128'", // String | The algorithm used to encrypt the PDF document.
  'userPassword': "userPassword_example" // String | The password required to open the PDF document. If the `user_password` is not set, the user will be able to open the document without a password.
};
apiInstance.addRestrictionsV1(file, ownerPassword, opts, (error, data, response) => {
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
 **file** | **File**| The input PDF document | 
 **ownerPassword** | **String**| The password required to open and change permissions of the PDF document. | 
 **allowAccessibility** | **Boolean**| If false, accessibility programs can&#39;t read the text or images of the document. | [optional] [default to true]
 **allowAssembleDocument** | **Boolean**| If false, the user can&#39;t assemble or manipulate the document. | [optional] [default to true]
 **allowChangeContent** | **Boolean**| If false, the user can&#39;t change the content of the document. | [optional] [default to true]
 **allowCommentAndFillForm** | **Boolean**| If false, the user can&#39;t add, edit or modify annotations or fill form fields. | [optional] [default to true]
 **allowCopyContent** | **Boolean**| If false, the user can&#39;t copy text and images to the clipboard. | [optional] [default to true]
 **allowFillForm** | **Boolean**| If false, the user can&#39;t fill forms fields. | [optional] [default to true]
 **allowPrint** | **Boolean**| If false, the user can&#39;t print the document. | [optional] [default to true]
 **allowPrintHighResolution** | **Boolean**| If false, the user can&#39;t print the document in high resolution. | [optional] [default to true]
 **encryptionAlgorithm** | **String**| The algorithm used to encrypt the PDF document. | [optional] [default to &#39;AES-128&#39;]
 **userPassword** | **String**| The password required to open the PDF document. If the &#x60;user_password&#x60; is not set, the user will be able to open the document without a password. | [optional] 

### Return type

**File**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/pdf, application/problem+json


## addTextWatermarkV1

> File addTextWatermarkV1(file, line1, opts)

Add a text watermark to a PDF

Add a text watermark to each page of a PDF document. Choose from several watermark templates.

### Example

```javascript
import PdfBlocksApi from 'pdf_blocks_api';
let defaultClient = PdfBlocksApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new PdfBlocksApi.DefaultApi();
let file = "/path/to/file"; // File | The input PDF document
let line1 = "line1_example"; // String | The first line of text of the watermark.
let opts = {
  'color': "'Gray'", // String | The color of the text watermark.
  'line2': "line2_example", // String | The second line of text of the watermark.
  'line3': "line3_example", // String | The third line of text of the watermark.
  'margin': 1, // Number | The distance in inches from the border of the page to the text watermark.
  'template': 1001, // Number | The [id of the text watermark template](https://www.pdfblocks.com/docs/api/v1/text-watermark-templates.pdf).
  'transparency': 75 // Number | The transparency level for the text watermark from 0 (opaque) to 100 (transparent).
};
apiInstance.addTextWatermarkV1(file, line1, opts, (error, data, response) => {
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
 **file** | **File**| The input PDF document | 
 **line1** | **String**| The first line of text of the watermark. | 
 **color** | **String**| The color of the text watermark. | [optional] [default to &#39;Gray&#39;]
 **line2** | **String**| The second line of text of the watermark. | [optional] 
 **line3** | **String**| The third line of text of the watermark. | [optional] 
 **margin** | **Number**| The distance in inches from the border of the page to the text watermark. | [optional] [default to 1]
 **template** | **Number**| The [id of the text watermark template](https://www.pdfblocks.com/docs/api/v1/text-watermark-templates.pdf). | [optional] [default to 1001]
 **transparency** | **Number**| The transparency level for the text watermark from 0 (opaque) to 100 (transparent). | [optional] [default to 75]

### Return type

**File**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/pdf, application/problem+json


## extractPagesV1

> File extractPagesV1(file, opts)

Extract pages from a PDF

Extract one or more pages from a PDF document.

### Example

```javascript
import PdfBlocksApi from 'pdf_blocks_api';
let defaultClient = PdfBlocksApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new PdfBlocksApi.DefaultApi();
let file = "/path/to/file"; // File | The input PDF document
let opts = {
  'firstPage': 56, // Number | The first page of the range to extract. If empty, it defaults to the first page of the PDF document.
  'lastPage': 56 // Number | The last page of the range to extract. If empty, it defaults to the last page of the PDF document.
};
apiInstance.extractPagesV1(file, opts, (error, data, response) => {
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
 **file** | **File**| The input PDF document | 
 **firstPage** | **Number**| The first page of the range to extract. If empty, it defaults to the first page of the PDF document. | [optional] 
 **lastPage** | **Number**| The last page of the range to extract. If empty, it defaults to the last page of the PDF document. | [optional] 

### Return type

**File**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/pdf, application/problem+json


## mergeDocumentsV1

> File mergeDocumentsV1(opts)

Merge PDF documents

Combine multiple PDF documents into a single PDF document.

### Example

```javascript
import PdfBlocksApi from 'pdf_blocks_api';
let defaultClient = PdfBlocksApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new PdfBlocksApi.DefaultApi();
let opts = {
  'file': ["null"] // [File] | The array of PDF documents. PDF documents will be merged in the same order they are inserted into this array.
};
apiInstance.mergeDocumentsV1(opts, (error, data, response) => {
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
 **file** | **[File]**| The array of PDF documents. PDF documents will be merged in the same order they are inserted into this array. | [optional] 

### Return type

**File**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/pdf, application/problem+json


## removePagesV1

> File removePagesV1(file, opts)

Remove pages from a PDF

Remove one or more pages from a PDF document.

### Example

```javascript
import PdfBlocksApi from 'pdf_blocks_api';
let defaultClient = PdfBlocksApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new PdfBlocksApi.DefaultApi();
let file = "/path/to/file"; // File | The input PDF document
let opts = {
  'firstPage': 56, // Number | The first page of the range to remove from the PDF document. If empty, it defaults to the first page of the document.
  'lastPage': 56 // Number | The last page of the range to remove from the PDF document. If empty, it defaults to the last page of the document.
};
apiInstance.removePagesV1(file, opts, (error, data, response) => {
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
 **file** | **File**| The input PDF document | 
 **firstPage** | **Number**| The first page of the range to remove from the PDF document. If empty, it defaults to the first page of the document. | [optional] 
 **lastPage** | **Number**| The last page of the range to remove from the PDF document. If empty, it defaults to the last page of the document. | [optional] 

### Return type

**File**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/pdf, application/problem+json


## removePasswordV1

> File removePasswordV1(file, password)

Remove the password from a PDF

Remove the password from an encrypted PDF document. The PDF document will no longer require a password to open.

### Example

```javascript
import PdfBlocksApi from 'pdf_blocks_api';
let defaultClient = PdfBlocksApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new PdfBlocksApi.DefaultApi();
let file = "/path/to/file"; // File | The input PDF document
let password = "password_example"; // String | The password required to open the file.
apiInstance.removePasswordV1(file, password, (error, data, response) => {
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
 **file** | **File**| The input PDF document | 
 **password** | **String**| The password required to open the file. | 

### Return type

**File**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/pdf, application/problem+json


## removeRestrictionsV1

> File removeRestrictionsV1(file)

Remove the restrictions from a PDF

Remove all the restrictions from a PDF document.

### Example

```javascript
import PdfBlocksApi from 'pdf_blocks_api';
let defaultClient = PdfBlocksApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new PdfBlocksApi.DefaultApi();
let file = "/path/to/file"; // File | The input PDF document
apiInstance.removeRestrictionsV1(file, (error, data, response) => {
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
 **file** | **File**| The input PDF document | 

### Return type

**File**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/pdf, application/problem+json


## removeSignaturesV1

> File removeSignaturesV1(file)

Remove the signatures from a PDF

Remove the cryptographic signatures and timestamps from a PDF document.

### Example

```javascript
import PdfBlocksApi from 'pdf_blocks_api';
let defaultClient = PdfBlocksApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new PdfBlocksApi.DefaultApi();
let file = "/path/to/file"; // File | The input PDF document
apiInstance.removeSignaturesV1(file, (error, data, response) => {
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
 **file** | **File**| The input PDF document | 

### Return type

**File**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/pdf, application/problem+json


## reversePagesV1

> File reversePagesV1(file)

Reverse the pages of a PDF

Reverse the order of the pages of a PDF document.

### Example

```javascript
import PdfBlocksApi from 'pdf_blocks_api';
let defaultClient = PdfBlocksApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new PdfBlocksApi.DefaultApi();
let file = "/path/to/file"; // File | The input PDF document
apiInstance.reversePagesV1(file, (error, data, response) => {
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
 **file** | **File**| The input PDF document | 

### Return type

**File**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/pdf, application/problem+json


## rotatePagesV1

> File rotatePagesV1(angle, file, opts)

Rotate pages in a PDF

Rotate one or more pages in a PDF document.

### Example

```javascript
import PdfBlocksApi from 'pdf_blocks_api';
let defaultClient = PdfBlocksApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new PdfBlocksApi.DefaultApi();
let angle = 56; // Number | The angle of rotation of the pages. Positive angles rotate the pages clockwise. Negative angles rotate the pages counter-clockwise.
let file = "/path/to/file"; // File | The input PDF document
let opts = {
  'firstPage': 56, // Number | The first page of the range to rotate in the PDF document. If empty, it defaults to the first page of the document.
  'lastPage': 56 // Number | The last page of the range to rotate in the PDF document. If empty, it defaults to the last page of the document.
};
apiInstance.rotatePagesV1(angle, file, opts, (error, data, response) => {
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
 **angle** | **Number**| The angle of rotation of the pages. Positive angles rotate the pages clockwise. Negative angles rotate the pages counter-clockwise. | 
 **file** | **File**| The input PDF document | 
 **firstPage** | **Number**| The first page of the range to rotate in the PDF document. If empty, it defaults to the first page of the document. | [optional] 
 **lastPage** | **Number**| The last page of the range to rotate in the PDF document. If empty, it defaults to the last page of the document. | [optional] 

### Return type

**File**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/pdf, application/problem+json

