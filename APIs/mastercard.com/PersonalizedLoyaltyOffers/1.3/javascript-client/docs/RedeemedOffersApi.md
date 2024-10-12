# PersonalizedOffers.RedeemedOffersApi

All URIs are relative to *https://api.mastercard.com/plo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**redeemedoffersGet**](RedeemedOffersApi.md#redeemedoffersGet) | **GET** /redeemedoffers | Returns Redeemed Offers



## redeemedoffersGet

> RedeemedOffersResponse redeemedoffersGet(fId, userToken, opts)

Returns Redeemed Offers

This resource returns offers that have been fulfilled by the user. 

### Example

```javascript
import PersonalizedOffers from 'personalized_offers';

let apiInstance = new PersonalizedOffers.RedeemedOffersApi();
let fId = "999999"; // String | Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
let userToken = "userToken_example"; // String | Session identifier as returned by the UserToken resource.
let opts = {
  'lang': "en_US", // String | When utilized with a multi-lingual implementation, may be the tongue and country of the user in ISO 639-1, underscore, ISO 3166-1 alpha-2 format.
  'pageNumber': 1, // Number | Segment of offers to return.
  'itemsPerPage': 1 // Number | Segment size of offer to be returned. Default is 25.
};
apiInstance.redeemedoffersGet(fId, userToken, opts, (error, data, response) => {
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
 **lang** | **String**| When utilized with a multi-lingual implementation, may be the tongue and country of the user in ISO 639-1, underscore, ISO 3166-1 alpha-2 format. | [optional] 
 **pageNumber** | **Number**| Segment of offers to return. | [optional] 
 **itemsPerPage** | **Number**| Segment size of offer to be returned. Default is 25. | [optional] 

### Return type

[**RedeemedOffersResponse**](RedeemedOffersResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

