# DealApi.EventItemApi

All URIs are relative to *https://api.ebay.com/buy/deal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEventItems**](EventItemApi.md#getEventItems) | **GET** /event_item | 



## getEventItems

> EventItemSearchResponse getEventItems(eventIds, X_EBAY_C_MARKETPLACE_ID, opts)



This method returns a paginated set of event items. The result set contains all event items associated with the specified search criteria and marketplace ID. Request headers This method uses the X-EBAY-C-ENDUSERCTX request header to support revenue sharing for eBay Partner Networks and to improve the accuracy of shipping and delivery time estimations. For details see, Request headers in the Buying Integration Guide. Restrictions This method can return a maximum of 10,000 items. For a list of supported sites and other restrictions, see API Restrictions. eBay Partner Network: In order to receive a commission for your sales, you must use the URL returned in the itemAffiliateWebUrl field to forward your buyer to the ebay.com site.

### Example

```javascript
import DealApi from 'deal_api';
let defaultClient = DealApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DealApi.EventItemApi();
let eventIds = "eventIds_example"; // String | The unique identifiers for the eBay events. Maximum Value: 1
let X_EBAY_C_MARKETPLACE_ID = "X_EBAY_C_MARKETPLACE_ID_example"; // String | A header used to specify the eBay marketplace ID.
let opts = {
  'categoryIds': "categoryIds_example", // String | The unique identifier of the eBay category for the search. Maximum Value: 1
  'deliveryCountry': "deliveryCountry_example", // String | A filter for items that can be shipped to the specified country.
  'limit': "limit_example", // String | The maximum number of items, from the current result set, returned on a single page. Default: 20
  'offset': "offset_example" // String | The number of items that will be skipped in the result set. This is used with the limit field to control the pagination of the output. For example, if the offset is set to 0 and the limit is set to 10, the method will retrieve items 1 through 10 from the list of items returned. If the offset is set to 10 and the limit is set to 10, the method will retrieve items 11 through 20 from the list of items returned. Default: 0
};
apiInstance.getEventItems(eventIds, X_EBAY_C_MARKETPLACE_ID, opts, (error, data, response) => {
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
 **eventIds** | **String**| The unique identifiers for the eBay events. Maximum Value: 1 | 
 **X_EBAY_C_MARKETPLACE_ID** | **String**| A header used to specify the eBay marketplace ID. | 
 **categoryIds** | **String**| The unique identifier of the eBay category for the search. Maximum Value: 1 | [optional] 
 **deliveryCountry** | **String**| A filter for items that can be shipped to the specified country. | [optional] 
 **limit** | **String**| The maximum number of items, from the current result set, returned on a single page. Default: 20 | [optional] 
 **offset** | **String**| The number of items that will be skipped in the result set. This is used with the limit field to control the pagination of the output. For example, if the offset is set to 0 and the limit is set to 10, the method will retrieve items 1 through 10 from the list of items returned. If the offset is set to 10 and the limit is set to 10, the method will retrieve items 11 through 20 from the list of items returned. Default: 0 | [optional] 

### Return type

[**EventItemSearchResponse**](EventItemSearchResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

