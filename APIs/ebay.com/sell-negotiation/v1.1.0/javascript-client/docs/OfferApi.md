# NegotiationApi.OfferApi

All URIs are relative to *https://api.ebay.com/sell/negotiation/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findEligibleItems**](OfferApi.md#findEligibleItems) | **GET** /find_eligible_items | 
[**sendOfferToInterestedBuyers**](OfferApi.md#sendOfferToInterestedBuyers) | **POST** /send_offer_to_interested_buyers | 



## findEligibleItems

> PagedEligibleItemCollection findEligibleItems(X_EBAY_C_MARKETPLACE_ID, opts)



This method evaluates a seller&#39;s current listings and returns the set of IDs that are eligible for a seller-initiated discount offer to a buyer. A listing ID is returned only when one or more buyers have shown an &amp;quot;interest&amp;quot; in the listing. If any buyers have shown interest in a listing, the seller can initiate a &amp;quot;negotiation&amp;quot; with them by calling sendOfferToInterestedBuyers, which sends all interested buyers a message that offers the listing at a discount. For details about how to create seller offers to buyers, see Sending offers to buyers.

### Example

```javascript
import NegotiationApi from 'negotiation_api';
let defaultClient = NegotiationApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NegotiationApi.OfferApi();
let X_EBAY_C_MARKETPLACE_ID = "X_EBAY_C_MARKETPLACE_ID_example"; // String | The eBay marketplace on which you want to search for eligible listings. For a complete list of supported marketplaces, see Negotiation API requirements and restrictions.
let opts = {
  'limit': "limit_example", // String | This query parameter specifies the maximum number of items to return from the result set on a page in the paginated response. Minimum: 1 &nbsp; &nbsp;Maximum: 200 Default: 10
  'offset': "offset_example" // String | This query parameter specifies the number of results to skip in the result set before returning the first result in the paginated response. Combine offset with the limit query parameter to control the items returned in the response. For example, if you supply an offset of 0 and a limit of 10, the first page of the response contains the first 10 results from the complete list of items retrieved by the call. If offset is 10 and limit is 20, the first page of the response contains items 11-30 from the complete result set. Default: 0
};
apiInstance.findEligibleItems(X_EBAY_C_MARKETPLACE_ID, opts, (error, data, response) => {
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
 **X_EBAY_C_MARKETPLACE_ID** | **String**| The eBay marketplace on which you want to search for eligible listings. For a complete list of supported marketplaces, see Negotiation API requirements and restrictions. | 
 **limit** | **String**| This query parameter specifies the maximum number of items to return from the result set on a page in the paginated response. Minimum: 1 &amp;nbsp; &amp;nbsp;Maximum: 200 Default: 10 | [optional] 
 **offset** | **String**| This query parameter specifies the number of results to skip in the result set before returning the first result in the paginated response. Combine offset with the limit query parameter to control the items returned in the response. For example, if you supply an offset of 0 and a limit of 10, the first page of the response contains the first 10 results from the complete list of items retrieved by the call. If offset is 10 and limit is 20, the first page of the response contains items 11-30 from the complete result set. Default: 0 | [optional] 

### Return type

[**PagedEligibleItemCollection**](PagedEligibleItemCollection.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sendOfferToInterestedBuyers

> SendOfferToInterestedBuyersCollectionResponse sendOfferToInterestedBuyers(X_EBAY_C_MARKETPLACE_ID, opts)



This method sends eligible buyers offers to purchase items in a listing at a discount. When a buyer has shown interest in a listing, they become &amp;quot;eligible&amp;quot; to receive a seller-initiated offer to purchase the item(s). Sellers use findEligibleItems to get the set of listings that have interested buyers. If a listing has interested buyers, sellers can use this method (sendOfferToInterestedBuyers) to send an offer to the buyers who are interested in the listing. The offer gives buyers the ability to purchase the associated listings at a discounted price. For details about how to create seller offers to buyers, see Sending offers to buyers.

### Example

```javascript
import NegotiationApi from 'negotiation_api';
let defaultClient = NegotiationApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NegotiationApi.OfferApi();
let X_EBAY_C_MARKETPLACE_ID = "X_EBAY_C_MARKETPLACE_ID_example"; // String | The eBay marketplace on which your listings with &quot;eligible&quot; buyers appear. For a complete list of supported marketplaces, see Negotiation API requirements and restrictions.
let opts = {
  'createOffersRequest': new NegotiationApi.CreateOffersRequest() // CreateOffersRequest | Send offer to eligible items request.
};
apiInstance.sendOfferToInterestedBuyers(X_EBAY_C_MARKETPLACE_ID, opts, (error, data, response) => {
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
 **X_EBAY_C_MARKETPLACE_ID** | **String**| The eBay marketplace on which your listings with &amp;quot;eligible&amp;quot; buyers appear. For a complete list of supported marketplaces, see Negotiation API requirements and restrictions. | 
 **createOffersRequest** | [**CreateOffersRequest**](CreateOffersRequest.md)| Send offer to eligible items request. | [optional] 

### Return type

[**SendOfferToInterestedBuyersCollectionResponse**](SendOfferToInterestedBuyersCollectionResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

