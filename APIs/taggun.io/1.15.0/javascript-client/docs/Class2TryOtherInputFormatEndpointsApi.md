# TaggunReceiptOcrScanningApi.Class2TryOtherInputFormatEndpointsApi

All URIs are relative to *https://api.taggun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postApiReceiptV1SimpleEncoded**](Class2TryOtherInputFormatEndpointsApi.md#postApiReceiptV1SimpleEncoded) | **POST** /api/receipt/v1/simple/encoded | transcribe a receipt using base64 encoded image in json payload
[**postApiReceiptV1SimpleUrl**](Class2TryOtherInputFormatEndpointsApi.md#postApiReceiptV1SimpleUrl) | **POST** /api/receipt/v1/simple/url | transcribe a receipt from URL
[**postApiReceiptV1VerboseEncoded**](Class2TryOtherInputFormatEndpointsApi.md#postApiReceiptV1VerboseEncoded) | **POST** /api/receipt/v1/verbose/encoded | transcribe a receipt using base64 encoded image in json payload and return detailed result
[**postApiReceiptV1VerboseUrl**](Class2TryOtherInputFormatEndpointsApi.md#postApiReceiptV1VerboseUrl) | **POST** /api/receipt/v1/verbose/url | transcribe a receipt from URL and return detailed result



## postApiReceiptV1SimpleEncoded

> ReceiptResult postApiReceiptV1SimpleEncoded(apikey, opts)

transcribe a receipt using base64 encoded image in json payload

### Example

```javascript
import TaggunReceiptOcrScanningApi from 'taggun_receipt_ocr_scanning_api';

let apiInstance = new TaggunReceiptOcrScanningApi.Class2TryOtherInputFormatEndpointsApi();
let apikey = "apikey_example"; // String | API authentication key.
let opts = {
  'body': new TaggunReceiptOcrScanningApi.JsonPayload() // JsonPayload | 
};
apiInstance.postApiReceiptV1SimpleEncoded(apikey, opts, (error, data, response) => {
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
 **body** | [**JsonPayload**](JsonPayload.md)|  | [optional] 

### Return type

[**ReceiptResult**](ReceiptResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## postApiReceiptV1SimpleUrl

> ReceiptResult postApiReceiptV1SimpleUrl(apikey, opts)

transcribe a receipt from URL

### Example

```javascript
import TaggunReceiptOcrScanningApi from 'taggun_receipt_ocr_scanning_api';

let apiInstance = new TaggunReceiptOcrScanningApi.Class2TryOtherInputFormatEndpointsApi();
let apikey = "apikey_example"; // String | API authentication key.
let opts = {
  'body': new TaggunReceiptOcrScanningApi.UrlPayload() // UrlPayload | 
};
apiInstance.postApiReceiptV1SimpleUrl(apikey, opts, (error, data, response) => {
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
 **body** | [**UrlPayload**](UrlPayload.md)|  | [optional] 

### Return type

[**ReceiptResult**](ReceiptResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## postApiReceiptV1VerboseEncoded

> ReceiptVerboseResult postApiReceiptV1VerboseEncoded(apikey, opts)

transcribe a receipt using base64 encoded image in json payload and return detailed result

### Example

```javascript
import TaggunReceiptOcrScanningApi from 'taggun_receipt_ocr_scanning_api';

let apiInstance = new TaggunReceiptOcrScanningApi.Class2TryOtherInputFormatEndpointsApi();
let apikey = "apikey_example"; // String | API authentication key.
let opts = {
  'body': new TaggunReceiptOcrScanningApi.JsonPayload() // JsonPayload | 
};
apiInstance.postApiReceiptV1VerboseEncoded(apikey, opts, (error, data, response) => {
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
 **body** | [**JsonPayload**](JsonPayload.md)|  | [optional] 

### Return type

[**ReceiptVerboseResult**](ReceiptVerboseResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## postApiReceiptV1VerboseUrl

> ReceiptVerboseResult postApiReceiptV1VerboseUrl(apikey, opts)

transcribe a receipt from URL and return detailed result

### Example

```javascript
import TaggunReceiptOcrScanningApi from 'taggun_receipt_ocr_scanning_api';

let apiInstance = new TaggunReceiptOcrScanningApi.Class2TryOtherInputFormatEndpointsApi();
let apikey = "apikey_example"; // String | API authentication key.
let opts = {
  'body': new TaggunReceiptOcrScanningApi.UrlPayload() // UrlPayload | 
};
apiInstance.postApiReceiptV1VerboseUrl(apikey, opts, (error, data, response) => {
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
 **body** | [**UrlPayload**](UrlPayload.md)|  | [optional] 

### Return type

[**ReceiptVerboseResult**](ReceiptVerboseResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

