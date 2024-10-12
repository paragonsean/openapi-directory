# LinQr.MultipleQRCodesApi

All URIs are relative to *https://run.byvalue.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**qrCodeBatchBatchQrcodePost**](MultipleQRCodesApi.md#qrCodeBatchBatchQrcodePost) | **POST** /batch/qrcode | QR Code Batch



## qrCodeBatchBatchQrcodePost

> File qrCodeBatchBatchQrcodePost(autoQRCodeBatch)

QR Code Batch

This endpoint allows you to generate an archive containing multiple QR Codes with a single request. The endpoint response is the archive containing the generated image files and &#x60;items.json&#x60; file which is a record of the specifications of each of the files in the archive.

### Example

```javascript
import LinQr from 'lin_qr';
let defaultClient = LinQr.ApiClient.instance;
// Configure API key authorization: Byvalue
let Byvalue = defaultClient.authentications['Byvalue'];
Byvalue.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Byvalue.apiKeyPrefix = 'Token';
// Configure API key authorization: RapidAPI
let RapidAPI = defaultClient.authentications['RapidAPI'];
RapidAPI.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RapidAPI.apiKeyPrefix = 'Token';

let apiInstance = new LinQr.MultipleQRCodesApi();
let autoQRCodeBatch = new LinQr.AutoQRCodeBatch(); // AutoQRCodeBatch | 
apiInstance.qrCodeBatchBatchQrcodePost(autoQRCodeBatch, (error, data, response) => {
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
 **autoQRCodeBatch** | [**AutoQRCodeBatch**](AutoQRCodeBatch.md)|  | 

### Return type

**File**

### Authorization

[Byvalue](../README.md#Byvalue), [RapidAPI](../README.md#RapidAPI)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/gzip, application/zip, application/json, text/plain

