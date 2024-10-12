# Reverb.ListingsApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listingsAllGet**](ListingsApi.md#listingsAllGet) | **GET** /listings/all | All listings including used, handmade, and brand new
[**listingsFacetsSellerLocationGet**](ListingsApi.md#listingsFacetsSellerLocationGet) | **GET** /listings/facets/seller_location | Individual facets
[**listingsGet**](ListingsApi.md#listingsGet) | **GET** /listings | Default search of listings includes only used &amp; handmade. Add a filter to view all listings or use the /listings/all endpoint.
[**listingsIdNegotiationGet**](ListingsApi.md#listingsIdNegotiationGet) | **GET** /listings/{id}/negotiation | Returns the latest negotiation for the requesting user given a listing id
[**listingsIdOfferPost**](ListingsApi.md#listingsIdOfferPost) | **POST** /listings/{id}/offer | Make an offer to the seller of a listing
[**listingsListingIdBumpBudgetTypePost**](ListingsApi.md#listingsListingIdBumpBudgetTypePost) | **POST** /listings/{listing_id}/bump/{budget_type} | Bump a listing
[**listingsListingIdBumpGet**](ListingsApi.md#listingsListingIdBumpGet) | **GET** /listings/{listing_id}/bump | View available bump tiers and stats for a listing
[**listingsListingIdConversationsPost**](ListingsApi.md#listingsListingIdConversationsPost) | **POST** /listings/{listing_id}/conversations | Start a conversation with a seller
[**listingsListingIdImagesGet**](ListingsApi.md#listingsListingIdImagesGet) | **GET** /listings/{listing_id}/images | View the images associated with a particular listing
[**listingsListingIdImagesImageIdDelete**](ListingsApi.md#listingsListingIdImagesImageIdDelete) | **DELETE** /listings/{listing_id}/images/{image_id} | Delete an image from a listing
[**listingsListingIdSalesGet**](ListingsApi.md#listingsListingIdSalesGet) | **GET** /listings/{listing_id}/sales | See all sales that include a listing.
[**listingsPost**](ListingsApi.md#listingsPost) | **POST** /listings | Create a listing
[**listingsSlugDelete**](ListingsApi.md#listingsSlugDelete) | **DELETE** /listings/{slug} | Delete a draft listing. Cannot be used on non-drafts.
[**listingsSlugEditGet**](ListingsApi.md#listingsSlugEditGet) | **GET** /listings/{slug}/edit | Edit listing.
[**listingsSlugFlagPost**](ListingsApi.md#listingsSlugFlagPost) | **POST** /listings/{slug}/flag | Flag a listing for inappropriate content or fraud
[**listingsSlugGet**](ListingsApi.md#listingsSlugGet) | **GET** /listings/{slug} | Listing details
[**listingsSlugPut**](ListingsApi.md#listingsSlugPut) | **PUT** /listings/{slug} | Update a listing
[**listingsSlugReviewsGet**](ListingsApi.md#listingsSlugReviewsGet) | **GET** /listings/{slug}/reviews | View reviews of a listing
[**listingsSlugReviewsPost**](ListingsApi.md#listingsSlugReviewsPost) | **POST** /listings/{slug}/reviews | Create a review for a listing
[**listingsSlugSimilarListingsGet**](ListingsApi.md#listingsSlugSimilarListingsGet) | **GET** /listings/{slug}/similar_listings | Listing details



## listingsAllGet

> listingsAllGet(opts)

All listings including used, handmade, and brand new

All listings including used, handmade, and brand new

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ListingsApi();
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
apiInstance.listingsAllGet(opts, (error, data, response) => {
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


## listingsFacetsSellerLocationGet

> listingsFacetsSellerLocationGet()

Individual facets

Individual facets

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ListingsApi();
apiInstance.listingsFacetsSellerLocationGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listingsGet

> listingsGet(opts)

Default search of listings includes only used &amp; handmade. Add a filter to view all listings or use the /listings/all endpoint.

Default search of listings includes only used &amp; handmade. Add a filter to view all listings or use the /listings/all endpoint.

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ListingsApi();
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
apiInstance.listingsGet(opts, (error, data, response) => {
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


## listingsIdNegotiationGet

> listingsIdNegotiationGet(id)

Returns the latest negotiation for the requesting user given a listing id

Returns the latest negotiation for the requesting user given a listing id

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ListingsApi();
let id = "id_example"; // String | 
apiInstance.listingsIdNegotiationGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listingsIdOfferPost

> listingsIdOfferPost(id, opts)

Make an offer to the seller of a listing

Make an offer to the seller of a listing

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ListingsApi();
let id = "id_example"; // String | 
let opts = {
  'conversationsIdOfferPostRequest': new Reverb.ConversationsIdOfferPostRequest() // ConversationsIdOfferPostRequest | the content of the request
};
apiInstance.listingsIdOfferPost(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **conversationsIdOfferPostRequest** | [**ConversationsIdOfferPostRequest**](ConversationsIdOfferPostRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## listingsListingIdBumpBudgetTypePost

> listingsListingIdBumpBudgetTypePost(listingId, budgetType)

Bump a listing

Bump a listing

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ListingsApi();
let listingId = "listingId_example"; // String | 
let budgetType = "budgetType_example"; // String | 
apiInstance.listingsListingIdBumpBudgetTypePost(listingId, budgetType, (error, data, response) => {
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
 **listingId** | **String**|  | 
 **budgetType** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listingsListingIdBumpGet

> listingsListingIdBumpGet(listingId)

View available bump tiers and stats for a listing

View available bump tiers and stats for a listing

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ListingsApi();
let listingId = "listingId_example"; // String | 
apiInstance.listingsListingIdBumpGet(listingId, (error, data, response) => {
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
 **listingId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listingsListingIdConversationsPost

> listingsListingIdConversationsPost(listingId, opts)

Start a conversation with a seller

Start a conversation with a seller

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ListingsApi();
let listingId = "listingId_example"; // String | 
let opts = {
  'listingsListingIdConversationsPostRequest': new Reverb.ListingsListingIdConversationsPostRequest() // ListingsListingIdConversationsPostRequest | the content of the request
};
apiInstance.listingsListingIdConversationsPost(listingId, opts, (error, data, response) => {
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
 **listingId** | **String**|  | 
 **listingsListingIdConversationsPostRequest** | [**ListingsListingIdConversationsPostRequest**](ListingsListingIdConversationsPostRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## listingsListingIdImagesGet

> listingsListingIdImagesGet(listingId)

View the images associated with a particular listing

View the images associated with a particular listing

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ListingsApi();
let listingId = "listingId_example"; // String | 
apiInstance.listingsListingIdImagesGet(listingId, (error, data, response) => {
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
 **listingId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listingsListingIdImagesImageIdDelete

> listingsListingIdImagesImageIdDelete(listingId, imageId)

Delete an image from a listing

Delete an image from a listing

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ListingsApi();
let listingId = "listingId_example"; // String | 
let imageId = "imageId_example"; // String | 
apiInstance.listingsListingIdImagesImageIdDelete(listingId, imageId, (error, data, response) => {
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
 **listingId** | **String**|  | 
 **imageId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listingsListingIdSalesGet

> listingsListingIdSalesGet(listingId)

See all sales that include a listing.

See all sales that include a listing.

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ListingsApi();
let listingId = "listingId_example"; // String | 
apiInstance.listingsListingIdSalesGet(listingId, (error, data, response) => {
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
 **listingId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listingsPost

> listingsPost(opts)

Create a listing

Create a listing

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ListingsApi();
let opts = {
  'listingsPostRequest': new Reverb.ListingsPostRequest() // ListingsPostRequest | the content of the request
};
apiInstance.listingsPost(opts, (error, data, response) => {
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
 **listingsPostRequest** | [**ListingsPostRequest**](ListingsPostRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## listingsSlugDelete

> listingsSlugDelete(slug)

Delete a draft listing. Cannot be used on non-drafts.

Delete a draft listing. Cannot be used on non-drafts.

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ListingsApi();
let slug = "slug_example"; // String | 
apiInstance.listingsSlugDelete(slug, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listingsSlugEditGet

> listingsSlugEditGet(slug)

Edit listing.

Edit listing.

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ListingsApi();
let slug = "slug_example"; // String | 
apiInstance.listingsSlugEditGet(slug, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listingsSlugFlagPost

> listingsSlugFlagPost(slug, opts)

Flag a listing for inappropriate content or fraud

Flag a listing for inappropriate content or fraud

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ListingsApi();
let slug = "slug_example"; // String | 
let opts = {
  'listingsSlugFlagPostRequest': new Reverb.ListingsSlugFlagPostRequest() // ListingsSlugFlagPostRequest | the content of the request
};
apiInstance.listingsSlugFlagPost(slug, opts, (error, data, response) => {
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
 **listingsSlugFlagPostRequest** | [**ListingsSlugFlagPostRequest**](ListingsSlugFlagPostRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## listingsSlugGet

> listingsSlugGet(slug)

Listing details

Listing details

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ListingsApi();
let slug = "slug_example"; // String | 
apiInstance.listingsSlugGet(slug, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listingsSlugPut

> listingsSlugPut(slug, opts)

Update a listing

Update a listing

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ListingsApi();
let slug = "slug_example"; // String | 
let opts = {
  'listingsPostRequest': new Reverb.ListingsPostRequest() // ListingsPostRequest | the content of the request
};
apiInstance.listingsSlugPut(slug, opts, (error, data, response) => {
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
 **listingsPostRequest** | [**ListingsPostRequest**](ListingsPostRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## listingsSlugReviewsGet

> listingsSlugReviewsGet(slug)

View reviews of a listing

View reviews of a listing

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ListingsApi();
let slug = "slug_example"; // String | 
apiInstance.listingsSlugReviewsGet(slug, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listingsSlugReviewsPost

> listingsSlugReviewsPost(slug)

Create a review for a listing

Create a review for a listing

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.ListingsApi();
let slug = "slug_example"; // String | 
apiInstance.listingsSlugReviewsPost(slug, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listingsSlugSimilarListingsGet

> listingsSlugSimilarListingsGet(slug)

Listing details

Listing details

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ListingsApi();
let slug = "slug_example"; // String | 
apiInstance.listingsSlugSimilarListingsGet(slug, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

