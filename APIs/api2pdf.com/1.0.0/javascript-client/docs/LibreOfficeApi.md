# Api2PdfPdfGenerationPoweredByAwsLambda.LibreOfficeApi

All URIs are relative to *https://v2018.api2pdf.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**libreConvertPost**](LibreOfficeApi.md#libreConvertPost) | **POST** /libreoffice/convert | Convert office document or image to PDF



## libreConvertPost

> ApiResponseSuccess libreConvertPost(opts)

Convert office document or image to PDF

Convert an office document (Word, Excel, Powerpoint) or an image (jpg, gif, png) to a PDF using LibreOffice on AWS Lambda. ### Authorize via Header of Request **Authorization: YOUR-API-KEY**

### Example

```javascript
import Api2PdfPdfGenerationPoweredByAwsLambda from 'api2_pdf_pdf_generation_powered_by_aws_lambda';
let defaultClient = Api2PdfPdfGenerationPoweredByAwsLambda.ApiClient.instance;
// Configure API key authorization: HeaderApiKey
let HeaderApiKey = defaultClient.authentications['HeaderApiKey'];
HeaderApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderApiKey.apiKeyPrefix = 'Token';

let apiInstance = new Api2PdfPdfGenerationPoweredByAwsLambda.LibreOfficeApi();
let opts = {
  'libreOfficeConvertRequest': new Api2PdfPdfGenerationPoweredByAwsLambda.LibreOfficeConvertRequest() // LibreOfficeConvertRequest | A JSON object as a payload is required within the body of the request. The following attributes of the JSON object are detailed below: - `url` *(string, required)* - A direct URL to the file. Api2Pdf will consume the file at that URL and then convert it. - `inlinePdf` *(boolean, optional)* - Open the PDF in a browser window. Default to false. - `fileName` *(string, optional)* - Specify a file name for the output PDF. Random name if not specified. 
};
apiInstance.libreConvertPost(opts, (error, data, response) => {
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
 **libreOfficeConvertRequest** | [**LibreOfficeConvertRequest**](LibreOfficeConvertRequest.md)| A JSON object as a payload is required within the body of the request. The following attributes of the JSON object are detailed below: - &#x60;url&#x60; *(string, required)* - A direct URL to the file. Api2Pdf will consume the file at that URL and then convert it. - &#x60;inlinePdf&#x60; *(boolean, optional)* - Open the PDF in a browser window. Default to false. - &#x60;fileName&#x60; *(string, optional)* - Specify a file name for the output PDF. Random name if not specified.  | [optional] 

### Return type

[**ApiResponseSuccess**](ApiResponseSuccess.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

