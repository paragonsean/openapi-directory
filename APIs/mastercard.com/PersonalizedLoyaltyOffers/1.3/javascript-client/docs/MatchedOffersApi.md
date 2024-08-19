# PersonalizedOffers.MatchedOffersApi

All URIs are relative to *https://api.mastercard.com/plo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**matchedoffersGet**](MatchedOffersApi.md#matchedoffersGet) | **GET** /matchedoffers | Returns Matched Offers



## matchedoffersGet

> MatchedOffersResponse matchedoffersGet(fId, userToken, opts)

Returns Matched Offers

This resource returns offers that are available to the user and conform to the search criteria (if specified). 

### Example

```javascript
import PersonalizedOffers from 'personalized_offers';

let apiInstance = new PersonalizedOffers.MatchedOffersApi();
let fId = "999999"; // String | Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
let userToken = "userToken_example"; // String | Session identifier as returned by the UserToken resource.
let opts = {
  'lang': "en_US", // String | When utilized with a multi-lingual implementation, may be the tongue and country of the user in ISO 639-1, underscore, ISO 3166-1 alpha-2 format.
  'merchantName': "Example.com", // String | Fuzzy term to search retailers with offers for the user. In general, searching of Matched Offers is not advised as users generally have a modest selection of highly relevant promotions.
  'category': "DEPARTMENTSTORE", // String | Offer Categories.
  'offerType': "POSTPAIDCREDIT", // String | The kind of deal. POSTPAIDCREDIT- Statement Credit Offer, which is a discount that is automatically applied to the card linked to the user and utilized to make the purchase.
  'pageNumber': 1, // Number | Segment of offers to return.
  'itemsPerPage': 1 // Number | Segment size of offer to be returned. Default is 25.
};
apiInstance.matchedoffersGet(fId, userToken, opts, (error, data, response) => {
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
 **merchantName** | **String**| Fuzzy term to search retailers with offers for the user. In general, searching of Matched Offers is not advised as users generally have a modest selection of highly relevant promotions. | [optional] 
 **category** | **String**| Offer Categories. | [optional] 
 **offerType** | **String**| The kind of deal. POSTPAIDCREDIT- Statement Credit Offer, which is a discount that is automatically applied to the card linked to the user and utilized to make the purchase. | [optional] 
 **pageNumber** | **Number**| Segment of offers to return. | [optional] 
 **itemsPerPage** | **Number**| Segment size of offer to be returned. Default is 25. | [optional] 

### Return type

[**MatchedOffersResponse**](MatchedOffersResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

