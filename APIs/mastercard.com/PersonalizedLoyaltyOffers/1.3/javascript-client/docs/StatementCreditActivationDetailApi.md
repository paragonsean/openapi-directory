# PersonalizedOffers.StatementCreditActivationDetailApi

All URIs are relative to *https://api.mastercard.com/plo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statementcreditactivationdetailGet**](StatementCreditActivationDetailApi.md#statementcreditactivationdetailGet) | **GET** /statementcreditactivationdetail | Returns Information About Redeemable Postpaid Credit Offer



## statementcreditactivationdetailGet

> StatementCreditActivationResponse statementcreditactivationdetailGet(fId, userToken, activationId)

Returns Information About Redeemable Postpaid Credit Offer

This resource returns extended information about the specified activated postpaid credit offer. 

### Example

```javascript
import PersonalizedOffers from 'personalized_offers';

let apiInstance = new PersonalizedOffers.StatementCreditActivationDetailApi();
let fId = "999999"; // String | Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
let userToken = "userToken_example"; // String | Session identifier as returned by the UserToken resource.
let activationId = "TRU_1000136"; // String | Distinct identifier for the offer being available for redemption by the user as returned by Activate Statement Credit Offer or Redeemed Offers, not intended for end-user display.
apiInstance.statementcreditactivationdetailGet(fId, userToken, activationId, (error, data, response) => {
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
 **activationId** | **String**| Distinct identifier for the offer being available for redemption by the user as returned by Activate Statement Credit Offer or Redeemed Offers, not intended for end-user display. | 

### Return type

[**StatementCreditActivationResponse**](StatementCreditActivationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

