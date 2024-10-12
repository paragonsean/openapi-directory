# ListingApi.ItemDraftApi

All URIs are relative to *https://api.ebay.com/sell/listing/v1_beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createItemDraft**](ItemDraftApi.md#createItemDraft) | **POST** /item_draft/ | 



## createItemDraft

> ItemDraftResponse createItemDraft(X_EBAY_C_MARKETPLACE_ID, opts)



This call gives Partners the ability to create an eBay draft of a item for their seller using information from their site. This lets the Partner increase the exposure of items on their site and leverage the eBay user listing experience seamlessly. This experience provides guidance on pricing, aspects, etc. and recommendations that help create a listing that is complete and improves the exposure of the listing in search results. After the listing draft is created, the seller logs into their eBay account and uses the listing experience to finish the listing and publish the item on eBay.

### Example

```javascript
import ListingApi from 'listing_api';
let defaultClient = ListingApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: api_auth
let api_auth = defaultClient.authentications['api_auth'];
api_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ListingApi.ItemDraftApi();
let X_EBAY_C_MARKETPLACE_ID = "X_EBAY_C_MARKETPLACE_ID_example"; // String | Use this header to specify an eBay marketplace ID. For a list of supported sites, see API Restrictions in the Listing API overview.
let opts = {
  'contentLanguage': "contentLanguage_example", // String | Use this header to specify the natural language of the seller. For details, see Content-Language in HTTP request headers. Required: For EBAY_CA in French. (Content-Language = fr-CA)
  'itemDraft': new ListingApi.ItemDraft() // ItemDraft | 
};
apiInstance.createItemDraft(X_EBAY_C_MARKETPLACE_ID, opts, (error, data, response) => {
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
 **X_EBAY_C_MARKETPLACE_ID** | **String**| Use this header to specify an eBay marketplace ID. For a list of supported sites, see API Restrictions in the Listing API overview. | 
 **contentLanguage** | **String**| Use this header to specify the natural language of the seller. For details, see Content-Language in HTTP request headers. Required: For EBAY_CA in French. (Content-Language &#x3D; fr-CA) | [optional] 
 **itemDraft** | [**ItemDraft**](ItemDraft.md)|  | [optional] 

### Return type

[**ItemDraftResponse**](ItemDraftResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

