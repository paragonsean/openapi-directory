# Api2PdfPdfGenerationPoweredByAwsLambda.ZXINGZebraCrossingBarCodesApi

All URIs are relative to *https://v2018.api2pdf.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zebraGET**](ZXINGZebraCrossingBarCodesApi.md#zebraGET) | **GET** /zebra | Generate bar codes and QR codes with ZXING.



## zebraGET

> File zebraGET(format, value, opts)

Generate bar codes and QR codes with ZXING.

See full list of options and documentation [here](https://www.api2pdf.com/documentation/advanced-options-zxing-zebra-crossing-barcodes/) ### Authorize via Query String Parameter **apikey&#x3D;YOUR-API-KEY** ### Example &#x60;&#x60;&#x60; https://v2018.api2pdf.com/zebra?format&#x3D;{format}&amp;apikey&#x3D;{YourApiKey}&amp;value&#x3D;{YourText} &#x60;&#x60;&#x60; 

### Example

```javascript
import Api2PdfPdfGenerationPoweredByAwsLambda from 'api2_pdf_pdf_generation_powered_by_aws_lambda';
let defaultClient = Api2PdfPdfGenerationPoweredByAwsLambda.ApiClient.instance;
// Configure API key authorization: QueryApiKey
let QueryApiKey = defaultClient.authentications['QueryApiKey'];
QueryApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//QueryApiKey.apiKeyPrefix = 'Token';

let apiInstance = new Api2PdfPdfGenerationPoweredByAwsLambda.ZXINGZebraCrossingBarCodesApi();
let format = "format_example"; // String | Most common is CODE_39 or QR_CODE
let value = "value_example"; // String | Specify the text value you want to convert
let opts = {
  'showlabel': true, // Boolean | Show label of text below barcode
  'height': 56, // Number | Height of the barcode generated image
  'width': 56 // Number | Width of the barcode generated image
};
apiInstance.zebraGET(format, value, opts, (error, data, response) => {
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
 **format** | **String**| Most common is CODE_39 or QR_CODE | 
 **value** | **String**| Specify the text value you want to convert | 
 **showlabel** | **Boolean**| Show label of text below barcode | [optional] 
 **height** | **Number**| Height of the barcode generated image | [optional] 
 **width** | **Number**| Width of the barcode generated image | [optional] 

### Return type

**File**

### Authorization

[QueryApiKey](../README.md#QueryApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/png

