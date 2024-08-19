# PersonalizedOffers.ActivateStatementCreditOfferApi

All URIs are relative to *https://api.mastercard.com/plo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activatestatementcreditofferPost**](ActivateStatementCreditOfferApi.md#activatestatementcreditofferPost) | **POST** /activatestatementcreditoffer | Make Statement Credit Offer Available Redeemable



## activatestatementcreditofferPost

> ActivateOfferResponse activatestatementcreditofferPost(fId, userToken, offerId)

Make Statement Credit Offer Available Redeemable

This resource is used to make a statement credit offer available for redemption. 

### Example

```javascript
import PersonalizedOffers from 'personalized_offers';

let apiInstance = new PersonalizedOffers.ActivateStatementCreditOfferApi();
let fId = "999999"; // String | Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
let userToken = "userToken_example"; // String | Session identifier as returned by the UserToken resource.
let offerId = "c7dcfca7-cf35-36b0-9e67-d4f363d643e0"; // String | System-wide identifier for the campaign, not intended for end-user display.
apiInstance.activatestatementcreditofferPost(fId, userToken, offerId, (error, data, response) => {
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
 **fId** | **String**| Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation. | 
 **userToken** | **String**| Session identifier as returned by the UserToken resource. | 
 **offerId** | **String**| System-wide identifier for the campaign, not intended for end-user display. | 

### Return type

[**ActivateOfferResponse**](ActivateOfferResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

