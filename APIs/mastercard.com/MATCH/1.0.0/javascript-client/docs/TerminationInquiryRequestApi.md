# MatchApi.TerminationInquiryRequestApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fraudMerchantV3TerminationInquiryPost**](TerminationInquiryRequestApi.md#fraudMerchantV3TerminationInquiryPost) | **POST** /fraud/merchant/v3/termination-inquiry | Returns information on merchants that have been terminated and merchants that have inquired upon. Provides the acquiring bank with information, such as, if a Merchant or individual has been terminated by another acquirer already, the reason for termination, the history of fraudulent or risky business practices that led to that termination and the inquiry that was made already on the Merchant or individual by own or another acquiring bank (if opted).



## fraudMerchantV3TerminationInquiryPost

> TerminationInquirySchema fraudMerchantV3TerminationInquiryPost(pageOffset, pageLength, terminationInquiryRequest)

Returns information on merchants that have been terminated and merchants that have inquired upon. Provides the acquiring bank with information, such as, if a Merchant or individual has been terminated by another acquirer already, the reason for termination, the history of fraudulent or risky business practices that led to that termination and the inquiry that was made already on the Merchant or individual by own or another acquiring bank (if opted).

Returns information on merchants that have been terminated and merchants which have been inquired upon. MATCH can provide the acquiring bank with information, such as, if a Merchant or individual has been terminated by another acquirer already, the reason for termination, the history of fraudulent or risky business practices that led to that termination and the inquiry that was made already on the Merchant or individual by own or another acquiring bank (If opted) 

### Example

```javascript
import MatchApi from 'match_api';

let apiInstance = new MatchApi.TerminationInquiryRequestApi();
let pageOffset = 0; // Number | The zero-based offset to start at. The actual start position is this value +1. An offset of 10 starts at item 11. Combined with the PageLength option this allows pagination to be supported through the service requests.
let pageLength = 10; // Number | The maximum number of items to retrieve within the current \"page\" of results.
let terminationInquiryRequest = new MatchApi.TerminationInquiryRequestSchema(); // TerminationInquiryRequestSchema | Body of the Termination Inquiry Request
apiInstance.fraudMerchantV3TerminationInquiryPost(pageOffset, pageLength, terminationInquiryRequest, (error, data, response) => {
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
 **pageOffset** | **Number**| The zero-based offset to start at. The actual start position is this value +1. An offset of 10 starts at item 11. Combined with the PageLength option this allows pagination to be supported through the service requests. | 
 **pageLength** | **Number**| The maximum number of items to retrieve within the current \&quot;page\&quot; of results. | 
 **terminationInquiryRequest** | [**TerminationInquiryRequestSchema**](TerminationInquiryRequestSchema.md)| Body of the Termination Inquiry Request | 

### Return type

[**TerminationInquirySchema**](TerminationInquirySchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

