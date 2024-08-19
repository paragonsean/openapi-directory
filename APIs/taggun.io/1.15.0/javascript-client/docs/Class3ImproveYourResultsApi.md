# TaggunReceiptOcrScanningApi.Class3ImproveYourResultsApi

All URIs are relative to *https://api.taggun.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postApiAccountV1Feedback**](Class3ImproveYourResultsApi.md#postApiAccountV1Feedback) | **POST** /api/account/v1/feedback | Add manually verified receipt data to a given receipt for feedback and training purposes
[**postApiAccountV1MerchantnameAdd**](Class3ImproveYourResultsApi.md#postApiAccountV1MerchantnameAdd) | **POST** /api/account/v1/merchantname/add | Add a keyword to your account&#39;s model to predict merchant name. Changes in your account&#39;s model are updated daily.



## postApiAccountV1Feedback

> Result postApiAccountV1Feedback(apikey, opts)

Add manually verified receipt data to a given receipt for feedback and training purposes

### Example

```javascript
import TaggunReceiptOcrScanningApi from 'taggun_receipt_ocr_scanning_api';

let apiInstance = new TaggunReceiptOcrScanningApi.Class3ImproveYourResultsApi();
let apikey = "apikey_example"; // String | API authentication key.
let opts = {
  'body': new TaggunReceiptOcrScanningApi.ReceiptFeedbackAddPayload() // ReceiptFeedbackAddPayload | 
};
apiInstance.postApiAccountV1Feedback(apikey, opts, (error, data, response) => {
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
 **body** | [**ReceiptFeedbackAddPayload**](ReceiptFeedbackAddPayload.md)|  | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## postApiAccountV1MerchantnameAdd

> Result postApiAccountV1MerchantnameAdd(apikey, opts)

Add a keyword to your account&#39;s model to predict merchant name. Changes in your account&#39;s model are updated daily.

### Example

```javascript
import TaggunReceiptOcrScanningApi from 'taggun_receipt_ocr_scanning_api';

let apiInstance = new TaggunReceiptOcrScanningApi.Class3ImproveYourResultsApi();
let apikey = "apikey_example"; // String | API authentication key.
let opts = {
  'body': new TaggunReceiptOcrScanningApi.MerchantNameAddPayload() // MerchantNameAddPayload | 
};
apiInstance.postApiAccountV1MerchantnameAdd(apikey, opts, (error, data, response) => {
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
 **body** | [**MerchantNameAddPayload**](MerchantNameAddPayload.md)|  | [optional] 

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

