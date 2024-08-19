# TaggunReceiptOcrScanningApi.Class4DeprecatedEndpointsApi

All URIs are relative to *https://api.taggun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postApiReceiptV1MatchFile**](Class4DeprecatedEndpointsApi.md#postApiReceiptV1MatchFile) | **POST** /api/receipt/v1/match/file | detect and match a receipt against keywords and metadata by uploading an image file
[**postApiReceiptV1SimpleStorage**](Class4DeprecatedEndpointsApi.md#postApiReceiptV1SimpleStorage) | **POST** /api/receipt/v1/simple/storage | transcribe a receipt in storage
[**postApiReceiptV1VerboseStorage**](Class4DeprecatedEndpointsApi.md#postApiReceiptV1VerboseStorage) | **POST** /api/receipt/v1/verbose/storage | transcribe a receipt in storage and return detailed result



## postApiReceiptV1MatchFile

> ReceiptMatchResult postApiReceiptV1MatchFile(apikey, opts)

detect and match a receipt against keywords and metadata by uploading an image file

### Example

```javascript
import TaggunReceiptOcrScanningApi from 'taggun_receipt_ocr_scanning_api';

let apiInstance = new TaggunReceiptOcrScanningApi.Class4DeprecatedEndpointsApi();
let apikey = "apikey_example"; // String | API authentication key.
let opts = {
  'file': "/path/to/file", // File | file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF
  'refresh': false, // Boolean | Set true to force re-process image transcription if the receipt is already in storage
  'incognito': false, // Boolean | Set true to avoid saving the receipt in storage
  'ipAddress': "ipAddress_example", // String | IP Address of the end user
  'primaryKeywords': ["null"], // [String] | An array of primary keywords to match
  'secondaryKeywords': ["null"], // [String] | An array of secondary keywords to match (lower confidence level than primaryKeywords)
  'stopWords': ["null"], // [String] | An array of stop words that negate the result to be UNLIKELY
  'language': "language_example" // String | Set language as a hint. Leave empty for auto detect. Supported languages: , en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh 
};
apiInstance.postApiReceiptV1MatchFile(apikey, opts, (error, data, response) => {
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
 **file** | **File**| file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF | [optional] 
 **refresh** | **Boolean**| Set true to force re-process image transcription if the receipt is already in storage | [optional] [default to false]
 **incognito** | **Boolean**| Set true to avoid saving the receipt in storage | [optional] [default to false]
 **ipAddress** | **String**| IP Address of the end user | [optional] 
 **primaryKeywords** | [**[String]**](String.md)| An array of primary keywords to match | [optional] 
 **secondaryKeywords** | [**[String]**](String.md)| An array of secondary keywords to match (lower confidence level than primaryKeywords) | [optional] 
 **stopWords** | [**[String]**](String.md)| An array of stop words that negate the result to be UNLIKELY | [optional] 
 **language** | **String**| Set language as a hint. Leave empty for auto detect. Supported languages: , en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh  | [optional] 

### Return type

[**ReceiptMatchResult**](ReceiptMatchResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: */*


## postApiReceiptV1SimpleStorage

> ReceiptResult postApiReceiptV1SimpleStorage(apikey, opts)

transcribe a receipt in storage

### Example

```javascript
import TaggunReceiptOcrScanningApi from 'taggun_receipt_ocr_scanning_api';

let apiInstance = new TaggunReceiptOcrScanningApi.Class4DeprecatedEndpointsApi();
let apikey = "apikey_example"; // String | API authentication key.
let opts = {
  'body': new TaggunReceiptOcrScanningApi.StoragePayload() // StoragePayload | 
};
apiInstance.postApiReceiptV1SimpleStorage(apikey, opts, (error, data, response) => {
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
 **body** | [**StoragePayload**](StoragePayload.md)|  | [optional] 

### Return type

[**ReceiptResult**](ReceiptResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## postApiReceiptV1VerboseStorage

> ReceiptVerboseResult postApiReceiptV1VerboseStorage(apikey, opts)

transcribe a receipt in storage and return detailed result

### Example

```javascript
import TaggunReceiptOcrScanningApi from 'taggun_receipt_ocr_scanning_api';

let apiInstance = new TaggunReceiptOcrScanningApi.Class4DeprecatedEndpointsApi();
let apikey = "apikey_example"; // String | API authentication key.
let opts = {
  'body': new TaggunReceiptOcrScanningApi.StoragePayload() // StoragePayload | 
};
apiInstance.postApiReceiptV1VerboseStorage(apikey, opts, (error, data, response) => {
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
 **body** | [**StoragePayload**](StoragePayload.md)|  | [optional] 

### Return type

[**ReceiptVerboseResult**](ReceiptVerboseResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

