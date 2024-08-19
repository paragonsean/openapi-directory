# TaggunReceiptOcrScanningApi.Class1GettingStartedApi

All URIs are relative to *https://api.taggun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postApiReceiptV1SimpleFile**](Class1GettingStartedApi.md#postApiReceiptV1SimpleFile) | **POST** /api/receipt/v1/simple/file | transcribe a receipt by uploading an image file
[**postApiReceiptV1VerboseFile**](Class1GettingStartedApi.md#postApiReceiptV1VerboseFile) | **POST** /api/receipt/v1/verbose/file | transcribe a receipt by uploading an image file and return detailed result



## postApiReceiptV1SimpleFile

> ReceiptResult postApiReceiptV1SimpleFile(apikey, opts)

transcribe a receipt by uploading an image file

### Example

```javascript
import TaggunReceiptOcrScanningApi from 'taggun_receipt_ocr_scanning_api';

let apiInstance = new TaggunReceiptOcrScanningApi.Class1GettingStartedApi();
let apikey = "apikey_example"; // String | API authentication key.
let opts = {
  'file': "/path/to/file", // File | file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF, HEIC
  'refresh': false, // Boolean | Set true to force re-process image transcription if the receipt is already in storage
  'incognito': false, // Boolean | Set true to avoid saving the receipt in storage
  'ipAddress': "ipAddress_example", // String | IP Address of the end user
  'near': "near_example", // String | A geo location to search for merchant. Typically in the format of city, state, country.
  'ignoreMerchantName': "ignoreMerchantName_example", // String | Ignore this merchant name if detected on the receipt. Use this field to avoid detecting the customer name as the merchant name.
  'language': "language_example", // String | Set language as a hint. Leave empty for auto detect. Supported languages: , en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh 
  'extractTime': false, // Boolean | Set true to return time if found on the receipt. Otherwise, the time is always set to 12:00:00.000.
  'subAccountId': "subAccountId_example", // String | Tag a request with sub-account ID for billing purposes
  'referenceId': "referenceId_example" // String | Tag a request with a unique reference ID for feedback and training purposes
};
apiInstance.postApiReceiptV1SimpleFile(apikey, opts, (error, data, response) => {
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
 **apikey** | **String**| API authentication key. | 
 **file** | **File**| file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF, HEIC | [optional] 
 **refresh** | **Boolean**| Set true to force re-process image transcription if the receipt is already in storage | [optional] [default to false]
 **incognito** | **Boolean**| Set true to avoid saving the receipt in storage | [optional] [default to false]
 **ipAddress** | **String**| IP Address of the end user | [optional] 
 **near** | **String**| A geo location to search for merchant. Typically in the format of city, state, country. | [optional] 
 **ignoreMerchantName** | **String**| Ignore this merchant name if detected on the receipt. Use this field to avoid detecting the customer name as the merchant name. | [optional] 
 **language** | **String**| Set language as a hint. Leave empty for auto detect. Supported languages: , en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh  | [optional] 
 **extractTime** | **Boolean**| Set true to return time if found on the receipt. Otherwise, the time is always set to 12:00:00.000. | [optional] [default to false]
 **subAccountId** | **String**| Tag a request with sub-account ID for billing purposes | [optional] 
 **referenceId** | **String**| Tag a request with a unique reference ID for feedback and training purposes | [optional] 

### Return type

[**ReceiptResult**](ReceiptResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*


## postApiReceiptV1VerboseFile

> ReceiptVerboseResult postApiReceiptV1VerboseFile(apikey, opts)

transcribe a receipt by uploading an image file and return detailed result

### Example

```javascript
import TaggunReceiptOcrScanningApi from 'taggun_receipt_ocr_scanning_api';

let apiInstance = new TaggunReceiptOcrScanningApi.Class1GettingStartedApi();
let apikey = "apikey_example"; // String | API authentication key.
let opts = {
  'file': "/path/to/file", // File | file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF, HEIC
  'refresh': false, // Boolean | Set true to force re-process image transcription if the receipt is already in storage
  'incognito': false, // Boolean | Set true to avoid saving the receipt in storage
  'ipAddress': "ipAddress_example", // String | IP Address of the end user
  'near': "near_example", // String | A geo location to search for merchant. Typically in the format of city, state, country.
  'ignoreMerchantName': "ignoreMerchantName_example", // String | Ignore this merchant name if detected on the receipt. Use this field to avoid detecting the customer name as the merchant name.
  'language': "language_example", // String | Set language as a hint. Leave empty for auto detect. Supported languages: , en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh 
  'extractTime': false, // Boolean | Set true to return time if found on the receipt. Otherwise, the time is always set to 12:00:00.000.
  'subAccountId': "subAccountId_example", // String | Tag a request with sub-account ID for billing purposes
  'referenceId': "referenceId_example" // String | Tag a request with a unique reference ID for feedback and training purposes
};
apiInstance.postApiReceiptV1VerboseFile(apikey, opts, (error, data, response) => {
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
 **apikey** | **String**| API authentication key. | 
 **file** | **File**| file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF, HEIC | [optional] 
 **refresh** | **Boolean**| Set true to force re-process image transcription if the receipt is already in storage | [optional] [default to false]
 **incognito** | **Boolean**| Set true to avoid saving the receipt in storage | [optional] [default to false]
 **ipAddress** | **String**| IP Address of the end user | [optional] 
 **near** | **String**| A geo location to search for merchant. Typically in the format of city, state, country. | [optional] 
 **ignoreMerchantName** | **String**| Ignore this merchant name if detected on the receipt. Use this field to avoid detecting the customer name as the merchant name. | [optional] 
 **language** | **String**| Set language as a hint. Leave empty for auto detect. Supported languages: , en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh  | [optional] 
 **extractTime** | **Boolean**| Set true to return time if found on the receipt. Otherwise, the time is always set to 12:00:00.000. | [optional] [default to false]
 **subAccountId** | **String**| Tag a request with sub-account ID for billing purposes | [optional] 
 **referenceId** | **String**| Tag a request with a unique reference ID for feedback and training purposes | [optional] 

### Return type

[**ReceiptVerboseResult**](ReceiptVerboseResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*

