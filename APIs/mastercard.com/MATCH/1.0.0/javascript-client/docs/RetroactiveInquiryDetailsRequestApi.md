# MatchApi.RetroactiveInquiryDetailsRequestApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fraudMerchantV3RetroRetroInquiryDetailsPost**](RetroactiveInquiryDetailsRequestApi.md#fraudMerchantV3RetroRetroInquiryDetailsPost) | **POST** /fraud/merchant/v3/retro/retro-inquiry-details | Returns detailed information about Merchants, URLs and up to five principal owners, that have been terminated by an acquiring bank after the inquiry was made.  This MATCH resource assists acquirer&#39;s ability to consider the merchants terminated after the inquiry was made. If an initial inquiry does not result in a possible match, it is still possible that the merchant listing could appear sometime in the next 360 days. This may occur when another acquirer enters the merchant into the MATCH database. The system will automatically continue to search the MATCH system for 360 days. To view these notifications, acquirers must use the Retroactive Inquiry Summary service. This resource can be used to obtain detailed information, such as, if a Merchant or individual has been terminated by another acquirer after an inquiry was made, the reason for termination, and the history of fraudulent or risky business practices that led to that termination.



## fraudMerchantV3RetroRetroInquiryDetailsPost

> RetroInquiryResponseSchema fraudMerchantV3RetroRetroInquiryDetailsPost(acquirerId, retroInquiryRequest)

Returns detailed information about Merchants, URLs and up to five principal owners, that have been terminated by an acquiring bank after the inquiry was made.  This MATCH resource assists acquirer&#39;s ability to consider the merchants terminated after the inquiry was made. If an initial inquiry does not result in a possible match, it is still possible that the merchant listing could appear sometime in the next 360 days. This may occur when another acquirer enters the merchant into the MATCH database. The system will automatically continue to search the MATCH system for 360 days. To view these notifications, acquirers must use the Retroactive Inquiry Summary service. This resource can be used to obtain detailed information, such as, if a Merchant or individual has been terminated by another acquirer after an inquiry was made, the reason for termination, and the history of fraudulent or risky business practices that led to that termination.

Returns detailed information about Merchants, URLs and up to five principal owners, that have been terminated by an acquiring bank after the inquiry was made.  This MATCH resource assists acquirer&#39;s ability to consider the merchants terminated after the inquiry was made. If an initial inquiry does not result in a possible match, it is still possible that the merchant listing could appear sometime in the next 360 days. This may occur when another acquirer enters the merchant into the MATCH database. The system will automatically continue to search the MATCH system for 360 days. To view these notifications, acquirers must use the Retroactive Inquiry Summary service. This resource can be used to obtain detailed information, such as, if a Merchant or individual has been terminated by another acquirer after an inquiry was made, the reason for termination, and the history of fraudulent or risky business practices that led to that termination. 

### Example

```javascript
import MatchApi from 'match_api';

let apiInstance = new MatchApi.RetroactiveInquiryDetailsRequestApi();
let acquirerId = "acquirerId_example"; // String | The Member ICA number which is used to validate that the application has permission to hit the MATCH database. This number must be obtained from a participating MATCH acquiring bank or entity before a developer can access the MATCH resource.
let retroInquiryRequest = new MatchApi.RetroInquiryRequestSchema(); // RetroInquiryRequestSchema | The retro inquiry request object
apiInstance.fraudMerchantV3RetroRetroInquiryDetailsPost(acquirerId, retroInquiryRequest, (error, data, response) => {
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
 **acquirerId** | **String**| The Member ICA number which is used to validate that the application has permission to hit the MATCH database. This number must be obtained from a participating MATCH acquiring bank or entity before a developer can access the MATCH resource. | 
 **retroInquiryRequest** | [**RetroInquiryRequestSchema**](RetroInquiryRequestSchema.md)| The retro inquiry request object | 

### Return type

[**RetroInquiryResponseSchema**](RetroInquiryResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

