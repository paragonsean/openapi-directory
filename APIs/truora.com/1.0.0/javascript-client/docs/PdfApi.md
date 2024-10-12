# ChecksApi.PdfApi

All URIs are relative to *https://api.truora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPDF**](PdfApi.md#createPDF) | **POST** /v1/checks/{check_id}/pdf | Create PDF
[**getPDF**](PdfApi.md#getPDF) | **GET** /v1/checks/{check_id}/pdf | Get PDF



## createPDF

> createPDF(checkId)

Create PDF

Creates a PDF containing the background check results.

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.PdfApi();
let checkId = "checkId_example"; // String | ID of the check
apiInstance.createPDF(checkId, (error, data, response) => {
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
 **checkId** | **String**| ID of the check | 

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPDF

> getPDF(checkId, opts)

Get PDF

Downloads the PDF in the specified language, Spanish by default.

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.PdfApi();
let checkId = "checkId_example"; // String | ID of the check
let opts = {
  'lang': "lang_example" // String | Used to specify the language for the PDF, if not specified the PDF will be downloaded in Spanish.
};
apiInstance.getPDF(checkId, opts, (error, data, response) => {
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
 **checkId** | **String**| ID of the check | 
 **lang** | **String**| Used to specify the language for the PDF, if not specified the PDF will be downloaded in Spanish. | [optional] 

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: PDF, application/json

