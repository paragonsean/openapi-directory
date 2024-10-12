# Api2PdfPdfGenerationPoweredByAwsLambda.MergeCombinePdfsApi

All URIs are relative to *https://v2018.api2pdf.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mergePost**](MergeCombinePdfsApi.md#mergePost) | **POST** /merge | Merge multiple PDFs together



## mergePost

> ApiResponseSuccess mergePost(opts)

Merge multiple PDFs together

Merge two or more PDFs together on AWS Lambda. ### Authorize via Header of Request **Authorization: YOUR-API-KEY**

### Example

```javascript
import Api2PdfPdfGenerationPoweredByAwsLambda from 'api2_pdf_pdf_generation_powered_by_aws_lambda';
let defaultClient = Api2PdfPdfGenerationPoweredByAwsLambda.ApiClient.instance;
// Configure API key authorization: HeaderApiKey
let HeaderApiKey = defaultClient.authentications['HeaderApiKey'];
HeaderApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//HeaderApiKey.apiKeyPrefix = 'Token';

let apiInstance = new Api2PdfPdfGenerationPoweredByAwsLambda.MergeCombinePdfsApi();
let opts = {
  'mergeRequest': new Api2PdfPdfGenerationPoweredByAwsLambda.MergeRequest() // MergeRequest | A JSON object as a payload is required within the body of the request. The following attributes of the JSON object are detailed below: - `urls` *(array of urls, required)* - A JSON array of direct URLs to PDFs. Api2Pdf will consume the PDF files in the list and then merge them all together.. - `inlinePdf` *(boolean, optional)* - Open the PDF in a browser window. Default to false. - `fileName` *(string, optional)* - Specify a file name for the output PDF. Random name if not specified. 
};
apiInstance.mergePost(opts, (error, data, response) => {
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
 **mergeRequest** | [**MergeRequest**](MergeRequest.md)| A JSON object as a payload is required within the body of the request. The following attributes of the JSON object are detailed below: - &#x60;urls&#x60; *(array of urls, required)* - A JSON array of direct URLs to PDFs. Api2Pdf will consume the PDF files in the list and then merge them all together.. - &#x60;inlinePdf&#x60; *(boolean, optional)* - Open the PDF in a browser window. Default to false. - &#x60;fileName&#x60; *(string, optional)* - Specify a file name for the output PDF. Random name if not specified.  | [optional] 

### Return type

[**ApiResponseSuccess**](ApiResponseSuccess.md)

### Authorization

[HeaderApiKey](../README.md#HeaderApiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

