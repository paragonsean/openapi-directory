# PersonalizedOffers.OfferDetailsApi

All URIs are relative to *https://api.mastercard.com/plo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offerdetailsGet**](OfferDetailsApi.md#offerdetailsGet) | **GET** /offerdetails | Returns Information on an Offer



## offerdetailsGet

> OfferDetailsResponse offerdetailsGet(fId, userToken, offerId)

Returns Information on an Offer

This resource returns extended information for the requested offer, typically used to display a detail view. 

### Example

```javascript
import PersonalizedOffers from 'personalized_offers';

let apiInstance = new PersonalizedOffers.OfferDetailsApi();
let fId = "999999"; // String | Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
let userToken = "mh3WonUm5xmE"; // String | Session identifier as returned by the UserToken resource.
let offerId = "c7dcfca7-cf35-36b0-9e67-d4f363d643e0"; // String | System-wide identifier for the campaign, not intended for end-user display.
apiInstance.offerdetailsGet(fId, userToken, offerId, (error, data, response) => {
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

[**OfferDetailsResponse**](OfferDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

