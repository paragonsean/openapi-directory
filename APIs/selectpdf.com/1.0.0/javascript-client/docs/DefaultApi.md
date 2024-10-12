# SelectPdfHtmlToPdfApi.DefaultApi

All URIs are relative to *https://selectpdf.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api2ConvertPost**](DefaultApi.md#api2ConvertPost) | **POST** /api2/convert | Performs a html to pdf conversion



## api2ConvertPost

> api2ConvertPost(opts)

Performs a html to pdf conversion

Converts provided HTML string or url to PDF

### Example

```javascript
import SelectPdfHtmlToPdfApi from 'select_pdf_html_to_pdf_api';

let apiInstance = new SelectPdfHtmlToPdfApi.DefaultApi();
let opts = {
  'parameters': new SelectPdfHtmlToPdfApi.ConversionParameters() // ConversionParameters | Conversion parameters
};
apiInstance.api2ConvertPost(opts, (error, data, response) => {
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
 **parameters** | [**ConversionParameters**](ConversionParameters.md)| Conversion parameters | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml
- **Accept**: Not defined

