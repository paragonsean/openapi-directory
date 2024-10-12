# Reverb.HandpickedApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handpickedSlugGet**](HandpickedApi.md#handpickedSlugGet) | **GET** /handpicked/{slug} | Get results from a handpicked collection



## handpickedSlugGet

> handpickedSlugGet(slug, opts)

Get results from a handpicked collection

Get results from a handpicked collection

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.HandpickedApi();
let slug = "slug_example"; // String | 
let opts = {
  'query': "query_example", // String | Search query.
  'auctionPriceMax': 3.4, // Number | Maximum current auction price
  'category': "category_example", // String | Category slug from /api/categories
  'productType': "productType_example", // String | Product type slug from /api/categories
  'conditions': ["null"], // [String] | Condition: all,new,b-stock,used,non-functioning,all-but-new,poor,fair,good,very-good,excellent,mint
  'decade': "decade_example", // String | Decade: e.g. 1970s, early 70s
  'finish': "finish_example", // String | Visual finish of the item, common for guitars
  'handmade': true, // Boolean | Handmade items only
  'itemCity': "itemCity_example", // String | City where item is located
  'itemCountry': "itemCountry_example", // String | DEPRECATED - Country code where item is located
  'itemRegion': "itemRegion_example", // String | Country code where item is located
  'itemState': "itemState_example", // String | State or region code where item is located
  'make': ["null"], // [String] | Make(s)/brand of item (e.g. Fender). Can take a single value or an array.
  'model': "model_example", // String | Model of item (e.g. Stratocaster)
  'mustNot': "mustNot_example", // String | Search term negation. If you want to exclude a term, add it here
  'priceMax': 3.4, // Number | Maximum price of search results (USD)
  'priceMin': 3.4, // Number | Minimum price of search results (USD)
  'currency': "currency_example", // String | The currency to be used for the price filters
  'yearMax': 56, // Number | Maximum year of manufacture
  'yearMin': 56, // Number | Minumum year of manufacture
  'acceptsGiftCards': true, // Boolean | If true, include only items that accept gift cards
  'preferredSeller': true, // Boolean | If true, include only items by Reverb Preferred Sellers
  'shop': "shop_example", // String | Slug of shop to search
  'shopId': "shopId_example", // String | ID of shop to search
  'listingType': "listingType_example", // String | Type of listing: auctions,offers
  'shipsTo': "shipsTo_example", // String | Limit search to items that ship to this country code
  'excludeAuctions': true, // Boolean | If true, exclude auctions
  'acceptsPaymentPlans': true, // Boolean | If true, only show items that can be purchased with a payment plan
  'watchersCountMin': 56, // Number | Minimum number of watchers (used to find popular items)
  'notIds': ["null"], // [String] | Listing ID negation. If you want to exclude a listing, add it here.
  'localPickup': true, // Boolean | Only items that offer local pickup
  'page': 1, // Number | 
  'perPage': 24, // Number | 
  'offset': 56 // Number | 
};
apiInstance.handpickedSlugGet(slug, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **String**|  | 
 **query** | **String**| Search query. | [optional] 
 **auctionPriceMax** | **Number**| Maximum current auction price | [optional] 
 **category** | **String**| Category slug from /api/categories | [optional] 
 **productType** | **String**| Product type slug from /api/categories | [optional] 
 **conditions** | [**[String]**](String.md)| Condition: all,new,b-stock,used,non-functioning,all-but-new,poor,fair,good,very-good,excellent,mint | [optional] 
 **decade** | **String**| Decade: e.g. 1970s, early 70s | [optional] 
 **finish** | **String**| Visual finish of the item, common for guitars | [optional] 
 **handmade** | **Boolean**| Handmade items only | [optional] 
 **itemCity** | **String**| City where item is located | [optional] 
 **itemCountry** | **String**| DEPRECATED - Country code where item is located | [optional] 
 **itemRegion** | **String**| Country code where item is located | [optional] 
 **itemState** | **String**| State or region code where item is located | [optional] 
 **make** | [**[String]**](String.md)| Make(s)/brand of item (e.g. Fender). Can take a single value or an array. | [optional] 
 **model** | **String**| Model of item (e.g. Stratocaster) | [optional] 
 **mustNot** | **String**| Search term negation. If you want to exclude a term, add it here | [optional] 
 **priceMax** | **Number**| Maximum price of search results (USD) | [optional] 
 **priceMin** | **Number**| Minimum price of search results (USD) | [optional] 
 **currency** | **String**| The currency to be used for the price filters | [optional] 
 **yearMax** | **Number**| Maximum year of manufacture | [optional] 
 **yearMin** | **Number**| Minumum year of manufacture | [optional] 
 **acceptsGiftCards** | **Boolean**| If true, include only items that accept gift cards | [optional] 
 **preferredSeller** | **Boolean**| If true, include only items by Reverb Preferred Sellers | [optional] 
 **shop** | **String**| Slug of shop to search | [optional] 
 **shopId** | **String**| ID of shop to search | [optional] 
 **listingType** | **String**| Type of listing: auctions,offers | [optional] 
 **shipsTo** | **String**| Limit search to items that ship to this country code | [optional] 
 **excludeAuctions** | **Boolean**| If true, exclude auctions | [optional] 
 **acceptsPaymentPlans** | **Boolean**| If true, only show items that can be purchased with a payment plan | [optional] 
 **watchersCountMin** | **Number**| Minimum number of watchers (used to find popular items) | [optional] 
 **notIds** | [**[String]**](String.md)| Listing ID negation. If you want to exclude a listing, add it here. | [optional] 
 **localPickup** | **Boolean**| Only items that offer local pickup | [optional] 
 **page** | **Number**|  | [optional] [default to 1]
 **perPage** | **Number**|  | [optional] [default to 24]
 **offset** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

