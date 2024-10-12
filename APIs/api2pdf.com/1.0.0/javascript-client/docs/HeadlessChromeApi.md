# Api2PdfPdfGenerationPoweredByAwsLambda.HeadlessChromeApi

All URIs are relative to *https://v2018.api2pdf.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chromeFromHtmlPost**](HeadlessChromeApi.md#chromeFromHtmlPost) | **POST** /chrome/html | Convert raw HTML to PDF
[**chromeFromUrlGET**](HeadlessChromeApi.md#chromeFromUrlGET) | **GET** /chrome/url | Convert URL to PDF
[**chromeFromUrlPost**](HeadlessChromeApi.md#chromeFromUrlPost) | **POST** /chrome/url | Convert URL to PDF



## chromeFromHtmlPost

> ApiResponseSuccess chromeFromHtmlPost(opts)

Convert raw HTML to PDF

Convert HTML to a PDF using Headless Chrome on AWS Lambda. ### Authorize via Header of Request **Authorization: YOUR-API-KEY**

### Example

```javascript
import Api2PdfPdfGenerationPoweredByAwsLambda from 'api2_pdf_pdf_generation_powered_by_aws_lambda';
let defaultClient = Api2PdfPdfGenerationPoweredByAwsLambda.ApiClient.instance;
// Configure API key authorization: HeaderApiKey
let HeaderApiKey = defaultClient.authentications['HeaderApiKey'];
HeaderApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderApiKey.apiKeyPrefix = 'Token';

let apiInstance = new Api2PdfPdfGenerationPoweredByAwsLambda.HeadlessChromeApi();
let opts = {
  'chromeHtmlToPdfRequest': new Api2PdfPdfGenerationPoweredByAwsLambda.ChromeHtmlToPdfRequest() // ChromeHtmlToPdfRequest | A JSON object as a payload is required within the body of the request. The following attributes of the JSON object are detailed below: - `html` *(string, required)* - raw HTML to convert to PDF - `inlinePdf` *(boolean, optional)* - Open the PDF in a browser window. Default to false. - `fileName` *(string, optional)* - Specify a file name for the output PDF. Random name if not specified. - `options` *(object, optional)* - Include advanced Headless Chrome options like margins, headers, and footers. [See full list of advanced options here](https://www.api2pdf.com/documentation/advanced-options-headless-chrome/).
};
apiInstance.chromeFromHtmlPost(opts, (error, data, response) => {
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
 **chromeHtmlToPdfRequest** | [**ChromeHtmlToPdfRequest**](ChromeHtmlToPdfRequest.md)| A JSON object as a payload is required within the body of the request. The following attributes of the JSON object are detailed below: - &#x60;html&#x60; *(string, required)* - raw HTML to convert to PDF - &#x60;inlinePdf&#x60; *(boolean, optional)* - Open the PDF in a browser window. Default to false. - &#x60;fileName&#x60; *(string, optional)* - Specify a file name for the output PDF. Random name if not specified. - &#x60;options&#x60; *(object, optional)* - Include advanced Headless Chrome options like margins, headers, and footers. [See full list of advanced options here](https://www.api2pdf.com/documentation/advanced-options-headless-chrome/). | [optional] 

### Return type

[**ApiResponseSuccess**](ApiResponseSuccess.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## chromeFromUrlGET

> ApiResponseSuccess chromeFromUrlGET(url, opts)

Convert URL to PDF

Convert a URL or Web Page to PDF using Headless Chrome on AWS Lambda. This GET request is for convenience and does not support advanced options. Use the POST request for more flexibility. ### Authorize via Query String Parameter **apikey&#x3D;YOUR-API-KEY** ### Example &#x60;&#x60;&#x60; https://v2018.api2pdf.com/chrome/url?url&#x3D;{UrlToConvert}&amp;apikey&#x3D;{YourApiKey} &#x60;&#x60;&#x60; 

### Example

```javascript
import Api2PdfPdfGenerationPoweredByAwsLambda from 'api2_pdf_pdf_generation_powered_by_aws_lambda';
let defaultClient = Api2PdfPdfGenerationPoweredByAwsLambda.ApiClient.instance;
// Configure API key authorization: QueryApiKey
let QueryApiKey = defaultClient.authentications['QueryApiKey'];
QueryApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryApiKey.apiKeyPrefix = 'Token';

let apiInstance = new Api2PdfPdfGenerationPoweredByAwsLambda.HeadlessChromeApi();
let url = "url_example"; // String | Url of the page to convert to PDF. Must start with http:// or https://.
let opts = {
  'output': "output_example" // String | Specify output=json to receive a JSON output. Defaults to PDF file.
};
apiInstance.chromeFromUrlGET(url, opts, (error, data, response) => {
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
 **url** | **String**| Url of the page to convert to PDF. Must start with http:// or https://. | 
 **output** | **String**| Specify output&#x3D;json to receive a JSON output. Defaults to PDF file. | [optional] 

### Return type

[**ApiResponseSuccess**](ApiResponseSuccess.md)

### Authorization

[QueryApiKey](../README.md#QueryApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/pdf


## chromeFromUrlPost

> ApiResponseSuccess chromeFromUrlPost(opts)

Convert URL to PDF

Convert a URL or Web Page to PDF using Headless Chrome on AWS Lambda.. ### Authorize via Header of Request **Authorization: YOUR-API-KEY**

### Example

```javascript
import Api2PdfPdfGenerationPoweredByAwsLambda from 'api2_pdf_pdf_generation_powered_by_aws_lambda';
let defaultClient = Api2PdfPdfGenerationPoweredByAwsLambda.ApiClient.instance;
// Configure API key authorization: HeaderApiKey
let HeaderApiKey = defaultClient.authentications['HeaderApiKey'];
HeaderApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderApiKey.apiKeyPrefix = 'Token';

let apiInstance = new Api2PdfPdfGenerationPoweredByAwsLambda.HeadlessChromeApi();
let opts = {
  'chromeUrlToPdfRequest': new Api2PdfPdfGenerationPoweredByAwsLambda.ChromeUrlToPdfRequest() // ChromeUrlToPdfRequest | A JSON object as a payload is required within the body of the request. The following attributes of the JSON object are detailed below: - `url` *(string, required)* - Url to the web page to convert to PDF - `inlinePdf` *(boolean, optional)* - Open the PDF in a browser window. Default to false. - `fileName` *(string, optional)* - Specify a file name for the output PDF. Random name if not specified. - `options` *(object, optional)* - Include advanced Headless Chrome options like margins, headers, and footers. [See full list of advanced options here](https://www.api2pdf.com/documentation/advanced-options-headless-chrome/).
};
apiInstance.chromeFromUrlPost(opts, (error, data, response) => {
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
 **chromeUrlToPdfRequest** | [**ChromeUrlToPdfRequest**](ChromeUrlToPdfRequest.md)| A JSON object as a payload is required within the body of the request. The following attributes of the JSON object are detailed below: - &#x60;url&#x60; *(string, required)* - Url to the web page to convert to PDF - &#x60;inlinePdf&#x60; *(boolean, optional)* - Open the PDF in a browser window. Default to false. - &#x60;fileName&#x60; *(string, optional)* - Specify a file name for the output PDF. Random name if not specified. - &#x60;options&#x60; *(object, optional)* - Include advanced Headless Chrome options like margins, headers, and footers. [See full list of advanced options here](https://www.api2pdf.com/documentation/advanced-options-headless-chrome/). | [optional] 

### Return type

[**ApiResponseSuccess**](ApiResponseSuccess.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

