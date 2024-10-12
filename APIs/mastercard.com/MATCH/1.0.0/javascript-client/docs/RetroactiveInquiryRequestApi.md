# MatchApi.RetroactiveInquiryRequestApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fraudMerchantV3RetroRetroListPost**](RetroactiveInquiryRequestApi.md#fraudMerchantV3RetroRetroListPost) | **POST** /fraud/merchant/v3/retro/retro-list | Returns the summary of Retro matches for the given Acquirer Id. This resource will return the summary of Retroactive Inquiry matches for the given Acquirer ID/ICA. If an initial inquiry does not result in a possible match, it is still possible that the merchant listing could appear sometime in the next 360 days. This may occur when another acquirer enters the merchant into the MATCH database. The system will automatically continue to search the MATCH system for 360 days. To view these notifications, acquirers must use the Retroactive Inquiry service.



## fraudMerchantV3RetroRetroListPost

> RetroResponseSchema fraudMerchantV3RetroRetroListPost(retroRequest)

Returns the summary of Retro matches for the given Acquirer Id. This resource will return the summary of Retroactive Inquiry matches for the given Acquirer ID/ICA. If an initial inquiry does not result in a possible match, it is still possible that the merchant listing could appear sometime in the next 360 days. This may occur when another acquirer enters the merchant into the MATCH database. The system will automatically continue to search the MATCH system for 360 days. To view these notifications, acquirers must use the Retroactive Inquiry service.

Returns the summary of Retro matches for the given Acquirer Id. This resource will return the summary of Retroactive Inquiry matches for the given Acquirer ID/ICA. If an initial inquiry does not result in a possible match, it is still possible that the merchant listing could appear sometime in the next 360 days. This may occur when another acquirer enters the merchant into the MATCH database. The system will automatically continue to search the MATCH system for 360 days. To view these notifications, acquirers must use the Retroactive Inquiry service. 

### Example

```javascript
import MatchApi from 'match_api';

let apiInstance = new MatchApi.RetroactiveInquiryRequestApi();
let retroRequest = new MatchApi.RetroRequestSchema(); // RetroRequestSchema | The retro request object
apiInstance.fraudMerchantV3RetroRetroListPost(retroRequest, (error, data, response) => {
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
 **retroRequest** | [**RetroRequestSchema**](RetroRequestSchema.md)| The retro request object | 

### Return type

[**RetroResponseSchema**](RetroResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

