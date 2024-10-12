# Reverb.MyApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**myAccountGet**](MyApi.md#myAccountGet) | **GET** /my/account | Get account details
[**myAccountPut**](MyApi.md#myAccountPut) | **PUT** /my/account | Update account details
[**myAddressesAddressIdDelete**](MyApi.md#myAddressesAddressIdDelete) | **DELETE** /my/addresses/{address_id} | Delete an existing address in your address book
[**myAddressesAddressIdPut**](MyApi.md#myAddressesAddressIdPut) | **PUT** /my/addresses/{address_id} | Update an existing address in your address book
[**myAddressesGet**](MyApi.md#myAddressesGet) | **GET** /my/addresses | See all addresses in your address book
[**myAddressesPost**](MyApi.md#myAddressesPost) | **POST** /my/addresses | Create a new address in your address book
[**myConversationsConversationIdMessagesPost**](MyApi.md#myConversationsConversationIdMessagesPost) | **POST** /my/conversations/{conversation_id}/messages | Send a message
[**myConversationsGet**](MyApi.md#myConversationsGet) | **GET** /my/conversations | Get a list of your conversations
[**myConversationsIdGet**](MyApi.md#myConversationsIdGet) | **GET** /my/conversations/{id} | Display conversation details with messages in natural time order (oldest to newest)
[**myConversationsIdPut**](MyApi.md#myConversationsIdPut) | **PUT** /my/conversations/{id} | Mark a conversation read/unread
[**myConversationsPost**](MyApi.md#myConversationsPost) | **POST** /my/conversations | Start a conversation
[**myCountsGet**](MyApi.md#myCountsGet) | **GET** /my/counts | Get your actionable status counts
[**myCuratedSetProductProductIdDelete**](MyApi.md#myCuratedSetProductProductIdDelete) | **DELETE** /my/curated_set/product/{product_id} | 
[**myCuratedSetProductProductIdPost**](MyApi.md#myCuratedSetProductProductIdPost) | **POST** /my/curated_set/product/{product_id} | 
[**myFeedCustomizeGet**](MyApi.md#myFeedCustomizeGet) | **GET** /my/feed/customize | get your feed customization options
[**myFeedGet**](MyApi.md#myFeedGet) | **GET** /my/feed | Get listings from your feed
[**myFeedGridGet**](MyApi.md#myFeedGridGet) | **GET** /my/feed/grid | get your feed
[**myFeedbackReceivedGet**](MyApi.md#myFeedbackReceivedGet) | **GET** /my/feedback/received | List of received feedback
[**myFeedbackSentGet**](MyApi.md#myFeedbackSentGet) | **GET** /my/feedback/sent | List of sent feedback
[**myFollowsArticlesGet**](MyApi.md#myFollowsArticlesGet) | **GET** /my/follows/articles | Returns a user&#39;s ArticleCategoryFollows
[**myFollowsArticlesPost**](MyApi.md#myFollowsArticlesPost) | **POST** /my/follows/articles | Set a user&#39;s ArticleCategoryFollows
[**myFollowsBrandsSlugDelete**](MyApi.md#myFollowsBrandsSlugDelete) | **DELETE** /my/follows/brands/{slug} | Unfollow a brand
[**myFollowsBrandsSlugGet**](MyApi.md#myFollowsBrandsSlugGet) | **GET** /my/follows/brands/{slug} | Follow status for a brand
[**myFollowsBrandsSlugPost**](MyApi.md#myFollowsBrandsSlugPost) | **POST** /my/follows/brands/{slug} | Follow a brand
[**myFollowsCategoriesCategorySubcategoryDelete**](MyApi.md#myFollowsCategoriesCategorySubcategoryDelete) | **DELETE** /my/follows/categories/{category}/{subcategory} | Unfollow a subcategory
[**myFollowsCategoriesCategorySubcategoryGet**](MyApi.md#myFollowsCategoriesCategorySubcategoryGet) | **GET** /my/follows/categories/{category}/{subcategory} | Follow status for a subcategory
[**myFollowsCategoriesCategorySubcategoryPost**](MyApi.md#myFollowsCategoriesCategorySubcategoryPost) | **POST** /my/follows/categories/{category}/{subcategory} | Follow a subcategory
[**myFollowsCategoriesIdentifierDelete**](MyApi.md#myFollowsCategoriesIdentifierDelete) | **DELETE** /my/follows/categories/{identifier} | Unfollow a category
[**myFollowsCategoriesIdentifierGet**](MyApi.md#myFollowsCategoriesIdentifierGet) | **GET** /my/follows/categories/{identifier} | Follow status for a category
[**myFollowsCategoriesIdentifierPost**](MyApi.md#myFollowsCategoriesIdentifierPost) | **POST** /my/follows/categories/{identifier} | Follow a category
[**myFollowsCategoriesUuidPost**](MyApi.md#myFollowsCategoriesUuidPost) | **POST** /my/follows/categories/{uuid} | Follow a category
[**myFollowsCollectionsSlugDelete**](MyApi.md#myFollowsCollectionsSlugDelete) | **DELETE** /my/follows/collections/{slug} | Unfollow a collection
[**myFollowsCollectionsSlugGet**](MyApi.md#myFollowsCollectionsSlugGet) | **GET** /my/follows/collections/{slug} | Follow status for a collection
[**myFollowsCollectionsSlugPost**](MyApi.md#myFollowsCollectionsSlugPost) | **POST** /my/follows/collections/{slug} | Follow a collection
[**myFollowsFollowIdAlertDelete**](MyApi.md#myFollowsFollowIdAlertDelete) | **DELETE** /my/follows/{follow_id}/alert | 
[**myFollowsFollowIdAlertPost**](MyApi.md#myFollowsFollowIdAlertPost) | **POST** /my/follows/{follow_id}/alert | 
[**myFollowsFollowIdDelete**](MyApi.md#myFollowsFollowIdDelete) | **DELETE** /my/follows/{follow_id} | Delete a follow
[**myFollowsGet**](MyApi.md#myFollowsGet) | **GET** /my/follows | See what the user is following
[**myFollowsHandpickedSlugDelete**](MyApi.md#myFollowsHandpickedSlugDelete) | **DELETE** /my/follows/handpicked/{slug} | Unfollow a handpicked collection
[**myFollowsHandpickedSlugGet**](MyApi.md#myFollowsHandpickedSlugGet) | **GET** /my/follows/handpicked/{slug} | Follow status for a handpicked collection
[**myFollowsHandpickedSlugPost**](MyApi.md#myFollowsHandpickedSlugPost) | **POST** /my/follows/handpicked/{slug} | Follow a handpicked collection
[**myFollowsSearchGet**](MyApi.md#myFollowsSearchGet) | **GET** /my/follows/search | Follow status for a search
[**myFollowsSearchPost**](MyApi.md#myFollowsSearchPost) | **POST** /my/follows/search | Follow a search
[**myFollowsShopsSlugDelete**](MyApi.md#myFollowsShopsSlugDelete) | **DELETE** /my/follows/shops/{slug} | Unfollow a shop
[**myFollowsShopsSlugGet**](MyApi.md#myFollowsShopsSlugGet) | **GET** /my/follows/shops/{slug} | Follow status for a shop
[**myFollowsShopsSlugPost**](MyApi.md#myFollowsShopsSlugPost) | **POST** /my/follows/shops/{slug} | Follow a shop
[**myListingsDraftsGet**](MyApi.md#myListingsDraftsGet) | **GET** /my/listings/drafts | Retrieve a list your draft listings
[**myListingsGet**](MyApi.md#myListingsGet) | **GET** /my/listings | Retrieve a list of live listings for the seller. To search all listings specify state&#x3D;all
[**myListingsNegotiationsGet**](MyApi.md#myListingsNegotiationsGet) | **GET** /my/listings/negotiations | Get a list of active negotiations as a seller
[**myListingsSlugStateEndPut**](MyApi.md#myListingsSlugStateEndPut) | **PUT** /my/listings/{slug}/state/end | End a listing
[**myListsGet**](MyApi.md#myListsGet) | **GET** /my/lists | Get a list of your lists (wishlist, watch list, etc)
[**myNegotiationsBuyingGet**](MyApi.md#myNegotiationsBuyingGet) | **GET** /my/negotiations/buying | Get a list of active negotiations as a buyer
[**myNegotiationsIdAcceptPost**](MyApi.md#myNegotiationsIdAcceptPost) | **POST** /my/negotiations/{id}/accept | Accept an offer
[**myNegotiationsIdCounterPost**](MyApi.md#myNegotiationsIdCounterPost) | **POST** /my/negotiations/{id}/counter | Counter an offer
[**myNegotiationsIdDeclinePost**](MyApi.md#myNegotiationsIdDeclinePost) | **POST** /my/negotiations/{id}/decline | Decline an offer
[**myNegotiationsIdGet**](MyApi.md#myNegotiationsIdGet) | **GET** /my/negotiations/{id} | Get offer details
[**myOrdersAwaitingFeedbackGet**](MyApi.md#myOrdersAwaitingFeedbackGet) | **GET** /my/orders/awaiting_feedback | List of orders that need feedback
[**myOrdersBuyingAllGet**](MyApi.md#myOrdersBuyingAllGet) | **GET** /my/orders/buying/all | Returns all orders, newest first.
[**myOrdersBuyingByUuidUuidGet**](MyApi.md#myOrdersBuyingByUuidUuidGet) | **GET** /my/orders/buying/by_uuid/{uuid} | 
[**myOrdersBuyingIdGet**](MyApi.md#myOrdersBuyingIdGet) | **GET** /my/orders/buying/{id} | Returns order details for a buyer
[**myOrdersBuyingIdMarkReceivedPost**](MyApi.md#myOrdersBuyingIdMarkReceivedPost) | **POST** /my/orders/buying/{id}/mark_received | Marks an order as received by the buyer
[**myOrdersBuyingUnpaidGet**](MyApi.md#myOrdersBuyingUnpaidGet) | **GET** /my/orders/buying/unpaid | Returns unpaid orders, newest first.
[**myOrdersSellingAllGet**](MyApi.md#myOrdersSellingAllGet) | **GET** /my/orders/selling/all | Get all seller orders, newest first.
[**myOrdersSellingAwaitingShipmentGet**](MyApi.md#myOrdersSellingAwaitingShipmentGet) | **GET** /my/orders/selling/awaiting_shipment | Get unpaid seller orders, newest first.
[**myOrdersSellingBuyerHistoryBuyerIdGet**](MyApi.md#myOrdersSellingBuyerHistoryBuyerIdGet) | **GET** /my/orders/selling/buyer_history/{buyer_id} | See previous orders from buyer
[**myOrdersSellingByUuidUuidGet**](MyApi.md#myOrdersSellingByUuidUuidGet) | **GET** /my/orders/selling/by_uuid/{uuid} | 
[**myOrdersSellingIdGet**](MyApi.md#myOrdersSellingIdGet) | **GET** /my/orders/selling/{id} | Returns order details for a seller
[**myOrdersSellingIdMarkPickedUpPost**](MyApi.md#myOrdersSellingIdMarkPickedUpPost) | **POST** /my/orders/selling/{id}/mark_picked_up | Marks an order as picked up
[**myOrdersSellingIdShipPost**](MyApi.md#myOrdersSellingIdShipPost) | **POST** /my/orders/selling/{id}/ship | Marks an order as shipped
[**myOrdersSellingOrderIdRefundRequestsPost**](MyApi.md#myOrdersSellingOrderIdRefundRequestsPost) | **POST** /my/orders/selling/{order_id}/refund_requests | Initiate a refund for a sold order
[**myOrdersSellingUnpaidGet**](MyApi.md#myOrdersSellingUnpaidGet) | **GET** /my/orders/selling/unpaid | Get unpaid seller orders, newest first.
[**myPaymentsSellingGet**](MyApi.md#myPaymentsSellingGet) | **GET** /my/payments/selling | Get payments
[**myPaymentsSellingIdGet**](MyApi.md#myPaymentsSellingIdGet) | **GET** /my/payments/selling/{id} | Get payment
[**myPayoutsGet**](MyApi.md#myPayoutsGet) | **GET** /my/payouts | Get a list of payouts
[**myPayoutsIdLineItemsGet**](MyApi.md#myPayoutsIdLineItemsGet) | **GET** /my/payouts/{id}/line_items | Read the line items of a payout
[**myRefundRequestsSellingGet**](MyApi.md#myRefundRequestsSellingGet) | **GET** /my/refund_requests/selling | Get a list of refund requests as a seller
[**myRefundRequestsSellingIdPut**](MyApi.md#myRefundRequestsSellingIdPut) | **PUT** /my/refund_requests/selling/{id} | Update a refund request for a sold order
[**myViewedListingsGet**](MyApi.md#myViewedListingsGet) | **GET** /my/viewed_listings | Get a list of your recently viewed listings.
[**myWishlistGet**](MyApi.md#myWishlistGet) | **GET** /my/wishlist | Get a list of wishlisted items
[**myWishlistIdDelete**](MyApi.md#myWishlistIdDelete) | **DELETE** /my/wishlist/{id} | Remove a listing from your wishlist
[**myWishlistIdPut**](MyApi.md#myWishlistIdPut) | **PUT** /my/wishlist/{id} | Add a listing to your wishlist



## myAccountGet

> myAccountGet()

Get account details

Get account details

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myAccountGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myAccountPut

> myAccountPut(opts)

Update account details

Update account details

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let opts = {
  'myAccountPutRequest': new Reverb.MyAccountPutRequest() // MyAccountPutRequest | the content of the request
};
apiInstance.myAccountPut(opts, (error, data, response) => {
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
 **myAccountPutRequest** | [**MyAccountPutRequest**](MyAccountPutRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## myAddressesAddressIdDelete

> myAddressesAddressIdDelete(addressId)

Delete an existing address in your address book

Delete an existing address in your address book

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let addressId = "addressId_example"; // String | 
apiInstance.myAddressesAddressIdDelete(addressId, (error, data, response) => {
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
 **addressId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myAddressesAddressIdPut

> myAddressesAddressIdPut(addressId)

Update an existing address in your address book

Update an existing address in your address book

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let addressId = "addressId_example"; // String | 
apiInstance.myAddressesAddressIdPut(addressId, (error, data, response) => {
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
 **addressId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myAddressesGet

> myAddressesGet()

See all addresses in your address book

See all addresses in your address book

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myAddressesGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myAddressesPost

> myAddressesPost()

Create a new address in your address book

Create a new address in your address book

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myAddressesPost((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myConversationsConversationIdMessagesPost

> myConversationsConversationIdMessagesPost(conversationId, opts)

Send a message

Send a message

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let conversationId = "conversationId_example"; // String | 
let opts = {
  'listingsListingIdConversationsPostRequest': new Reverb.ListingsListingIdConversationsPostRequest() // ListingsListingIdConversationsPostRequest | the content of the request
};
apiInstance.myConversationsConversationIdMessagesPost(conversationId, opts, (error, data, response) => {
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
 **conversationId** | **String**|  | 
 **listingsListingIdConversationsPostRequest** | [**ListingsListingIdConversationsPostRequest**](ListingsListingIdConversationsPostRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## myConversationsGet

> myConversationsGet(opts)

Get a list of your conversations

Get a list of your conversations

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let opts = {
  'search': "search_example", // String | Query string to search conversations by
  'unreadOnly': true, // Boolean | Show unread conversations only
  'page': 1, // Number | 
  'perPage': 24, // Number | 
  'offset': 56 // Number | 
};
apiInstance.myConversationsGet(opts, (error, data, response) => {
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
 **search** | **String**| Query string to search conversations by | [optional] 
 **unreadOnly** | **Boolean**| Show unread conversations only | [optional] 
 **page** | **Number**|  | [optional] [default to 1]
 **perPage** | **Number**|  | [optional] [default to 24]
 **offset** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myConversationsIdGet

> myConversationsIdGet(id)

Display conversation details with messages in natural time order (oldest to newest)

Display conversation details with messages in natural time order (oldest to newest)

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let id = "id_example"; // String | 
apiInstance.myConversationsIdGet(id, (error, data, response) => {
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


## myConversationsIdPut

> myConversationsIdPut(id, opts)

Mark a conversation read/unread

Mark a conversation read/unread

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let id = "id_example"; // String | 
let opts = {
  'myConversationsIdPutRequest': new Reverb.MyConversationsIdPutRequest() // MyConversationsIdPutRequest | the content of the request
};
apiInstance.myConversationsIdPut(id, opts, (error, data, response) => {
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
 **myConversationsIdPutRequest** | [**MyConversationsIdPutRequest**](MyConversationsIdPutRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## myConversationsPost

> myConversationsPost(opts)

Start a conversation

Start a conversation

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let opts = {
  'myConversationsPostRequest': new Reverb.MyConversationsPostRequest() // MyConversationsPostRequest | the content of the request
};
apiInstance.myConversationsPost(opts, (error, data, response) => {
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
 **myConversationsPostRequest** | [**MyConversationsPostRequest**](MyConversationsPostRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## myCountsGet

> myCountsGet()

Get your actionable status counts

Get your actionable status counts

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myCountsGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myCuratedSetProductProductIdDelete

> myCuratedSetProductProductIdDelete(productId)



### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.MyApi();
let productId = "productId_example"; // String | 
apiInstance.myCuratedSetProductProductIdDelete(productId, (error, data, response) => {
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
 **productId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myCuratedSetProductProductIdPost

> myCuratedSetProductProductIdPost(productId)



### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.MyApi();
let productId = "productId_example"; // String | 
apiInstance.myCuratedSetProductProductIdPost(productId, (error, data, response) => {
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
 **productId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myFeedCustomizeGet

> myFeedCustomizeGet()

get your feed customization options

get your feed customization options

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myFeedCustomizeGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myFeedGet

> myFeedGet()

Get listings from your feed

Get listings from your feed

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myFeedGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myFeedGridGet

> myFeedGridGet()

get your feed

get your feed

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myFeedGridGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myFeedbackReceivedGet

> myFeedbackReceivedGet()

List of received feedback

List of received feedback

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myFeedbackReceivedGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myFeedbackSentGet

> myFeedbackSentGet()

List of sent feedback

List of sent feedback

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myFeedbackSentGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myFollowsArticlesGet

> myFollowsArticlesGet()

Returns a user&#39;s ArticleCategoryFollows

Returns a user&#39;s ArticleCategoryFollows

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myFollowsArticlesGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myFollowsArticlesPost

> myFollowsArticlesPost(opts)

Set a user&#39;s ArticleCategoryFollows

Set a user&#39;s ArticleCategoryFollows

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let opts = {
  'myFollowsArticlesPostRequest': new Reverb.MyFollowsArticlesPostRequest() // MyFollowsArticlesPostRequest | the content of the request
};
apiInstance.myFollowsArticlesPost(opts, (error, data, response) => {
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
 **myFollowsArticlesPostRequest** | [**MyFollowsArticlesPostRequest**](MyFollowsArticlesPostRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## myFollowsBrandsSlugDelete

> myFollowsBrandsSlugDelete(slug)

Unfollow a brand

Unfollow a brand

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let slug = "slug_example"; // String | 
apiInstance.myFollowsBrandsSlugDelete(slug, (error, data, response) => {
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


## myFollowsBrandsSlugGet

> myFollowsBrandsSlugGet(slug)

Follow status for a brand

Follow status for a brand

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let slug = "slug_example"; // String | 
apiInstance.myFollowsBrandsSlugGet(slug, (error, data, response) => {
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


## myFollowsBrandsSlugPost

> myFollowsBrandsSlugPost(slug)

Follow a brand

Follow a brand

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let slug = "slug_example"; // String | 
apiInstance.myFollowsBrandsSlugPost(slug, (error, data, response) => {
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


## myFollowsCategoriesCategorySubcategoryDelete

> myFollowsCategoriesCategorySubcategoryDelete(category, subcategory)

Unfollow a subcategory

Unfollow a subcategory

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let category = "category_example"; // String | 
let subcategory = "subcategory_example"; // String | 
apiInstance.myFollowsCategoriesCategorySubcategoryDelete(category, subcategory, (error, data, response) => {
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
 **category** | **String**|  | 
 **subcategory** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myFollowsCategoriesCategorySubcategoryGet

> myFollowsCategoriesCategorySubcategoryGet(category, subcategory)

Follow status for a subcategory

Follow status for a subcategory

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let category = "category_example"; // String | 
let subcategory = "subcategory_example"; // String | 
apiInstance.myFollowsCategoriesCategorySubcategoryGet(category, subcategory, (error, data, response) => {
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
 **category** | **String**|  | 
 **subcategory** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myFollowsCategoriesCategorySubcategoryPost

> myFollowsCategoriesCategorySubcategoryPost(category, subcategory)

Follow a subcategory

Follow a subcategory

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let category = "category_example"; // String | 
let subcategory = "subcategory_example"; // String | 
apiInstance.myFollowsCategoriesCategorySubcategoryPost(category, subcategory, (error, data, response) => {
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
 **category** | **String**|  | 
 **subcategory** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myFollowsCategoriesIdentifierDelete

> myFollowsCategoriesIdentifierDelete(identifier)

Unfollow a category

Unfollow a category

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let identifier = "identifier_example"; // String | 
apiInstance.myFollowsCategoriesIdentifierDelete(identifier, (error, data, response) => {
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
 **identifier** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myFollowsCategoriesIdentifierGet

> myFollowsCategoriesIdentifierGet(identifier)

Follow status for a category

Follow status for a category

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let identifier = "identifier_example"; // String | 
apiInstance.myFollowsCategoriesIdentifierGet(identifier, (error, data, response) => {
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
 **identifier** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myFollowsCategoriesIdentifierPost

> myFollowsCategoriesIdentifierPost(identifier)

Follow a category

Follow a category

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let identifier = "identifier_example"; // String | 
apiInstance.myFollowsCategoriesIdentifierPost(identifier, (error, data, response) => {
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
 **identifier** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myFollowsCategoriesUuidPost

> myFollowsCategoriesUuidPost(uuid)

Follow a category

Follow a category

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let uuid = "uuid_example"; // String | 
apiInstance.myFollowsCategoriesUuidPost(uuid, (error, data, response) => {
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
 **uuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myFollowsCollectionsSlugDelete

> myFollowsCollectionsSlugDelete(slug)

Unfollow a collection

Unfollow a collection

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let slug = "slug_example"; // String | 
apiInstance.myFollowsCollectionsSlugDelete(slug, (error, data, response) => {
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


## myFollowsCollectionsSlugGet

> myFollowsCollectionsSlugGet(slug)

Follow status for a collection

Follow status for a collection

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let slug = "slug_example"; // String | 
apiInstance.myFollowsCollectionsSlugGet(slug, (error, data, response) => {
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


## myFollowsCollectionsSlugPost

> myFollowsCollectionsSlugPost(slug)

Follow a collection

Follow a collection

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let slug = "slug_example"; // String | 
apiInstance.myFollowsCollectionsSlugPost(slug, (error, data, response) => {
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


## myFollowsFollowIdAlertDelete

> myFollowsFollowIdAlertDelete(followId)



### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.MyApi();
let followId = "followId_example"; // String | 
apiInstance.myFollowsFollowIdAlertDelete(followId, (error, data, response) => {
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
 **followId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myFollowsFollowIdAlertPost

> myFollowsFollowIdAlertPost(followId)



### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.MyApi();
let followId = "followId_example"; // String | 
apiInstance.myFollowsFollowIdAlertPost(followId, (error, data, response) => {
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
 **followId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myFollowsFollowIdDelete

> myFollowsFollowIdDelete(followId)

Delete a follow

Delete a follow

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let followId = "followId_example"; // String | 
apiInstance.myFollowsFollowIdDelete(followId, (error, data, response) => {
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
 **followId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myFollowsGet

> myFollowsGet()

See what the user is following

See what the user is following

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myFollowsGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myFollowsHandpickedSlugDelete

> myFollowsHandpickedSlugDelete(slug)

Unfollow a handpicked collection

Unfollow a handpicked collection

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let slug = "slug_example"; // String | 
apiInstance.myFollowsHandpickedSlugDelete(slug, (error, data, response) => {
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


## myFollowsHandpickedSlugGet

> myFollowsHandpickedSlugGet(slug)

Follow status for a handpicked collection

Follow status for a handpicked collection

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let slug = "slug_example"; // String | 
apiInstance.myFollowsHandpickedSlugGet(slug, (error, data, response) => {
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


## myFollowsHandpickedSlugPost

> myFollowsHandpickedSlugPost(slug)

Follow a handpicked collection

Follow a handpicked collection

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let slug = "slug_example"; // String | 
apiInstance.myFollowsHandpickedSlugPost(slug, (error, data, response) => {
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


## myFollowsSearchGet

> myFollowsSearchGet()

Follow status for a search

Follow status for a search

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myFollowsSearchGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myFollowsSearchPost

> myFollowsSearchPost(opts)

Follow a search

Follow a search

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let opts = {
  'myFollowsSearchPostRequest': new Reverb.MyFollowsSearchPostRequest() // MyFollowsSearchPostRequest | the content of the request
};
apiInstance.myFollowsSearchPost(opts, (error, data, response) => {
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
 **myFollowsSearchPostRequest** | [**MyFollowsSearchPostRequest**](MyFollowsSearchPostRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## myFollowsShopsSlugDelete

> myFollowsShopsSlugDelete(slug)

Unfollow a shop

Unfollow a shop

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let slug = "slug_example"; // String | 
apiInstance.myFollowsShopsSlugDelete(slug, (error, data, response) => {
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


## myFollowsShopsSlugGet

> myFollowsShopsSlugGet(slug)

Follow status for a shop

Follow status for a shop

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let slug = "slug_example"; // String | 
apiInstance.myFollowsShopsSlugGet(slug, (error, data, response) => {
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


## myFollowsShopsSlugPost

> myFollowsShopsSlugPost(slug)

Follow a shop

Follow a shop

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let slug = "slug_example"; // String | 
apiInstance.myFollowsShopsSlugPost(slug, (error, data, response) => {
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


## myListingsDraftsGet

> myListingsDraftsGet(opts)

Retrieve a list your draft listings

Retrieve a list your draft listings

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
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
  'localPickup': true // Boolean | Only items that offer local pickup
};
apiInstance.myListingsDraftsGet(opts, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myListingsGet

> myListingsGet(opts)

Retrieve a list of live listings for the seller. To search all listings specify state&#x3D;all

Retrieve a list of live listings for the seller. To search all listings specify state&#x3D;all

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
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
  'state': "'live'", // String | Available: [\"all\", \"draft\", \"ended\", \"live\", \"ordered\", \"sold_out\", \"suspended\", \"seller_unavailable\"]. Defaults to 'live'
  'sku': "sku_example" // String | Find a listing by sku
};
apiInstance.myListingsGet(opts, (error, data, response) => {
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
 **state** | **String**| Available: [\&quot;all\&quot;, \&quot;draft\&quot;, \&quot;ended\&quot;, \&quot;live\&quot;, \&quot;ordered\&quot;, \&quot;sold_out\&quot;, \&quot;suspended\&quot;, \&quot;seller_unavailable\&quot;]. Defaults to &#39;live&#39; | [optional] [default to &#39;live&#39;]
 **sku** | **String**| Find a listing by sku | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myListingsNegotiationsGet

> myListingsNegotiationsGet(opts)

Get a list of active negotiations as a seller

Get a list of active negotiations as a seller

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let opts = {
  'page': 1, // Number | 
  'perPage': 24, // Number | 
  'offset': 56 // Number | 
};
apiInstance.myListingsNegotiationsGet(opts, (error, data, response) => {
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
 **page** | **Number**|  | [optional] [default to 1]
 **perPage** | **Number**|  | [optional] [default to 24]
 **offset** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myListingsSlugStateEndPut

> myListingsSlugStateEndPut(slug, opts)

End a listing

End a listing

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let slug = "slug_example"; // String | 
let opts = {
  'myListingsSlugStateEndPutRequest': new Reverb.MyListingsSlugStateEndPutRequest() // MyListingsSlugStateEndPutRequest | the content of the request
};
apiInstance.myListingsSlugStateEndPut(slug, opts, (error, data, response) => {
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
 **myListingsSlugStateEndPutRequest** | [**MyListingsSlugStateEndPutRequest**](MyListingsSlugStateEndPutRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## myListsGet

> myListsGet()

Get a list of your lists (wishlist, watch list, etc)

Get a list of your lists (wishlist, watch list, etc)

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myListsGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myNegotiationsBuyingGet

> myNegotiationsBuyingGet(opts)

Get a list of active negotiations as a buyer

Get a list of active negotiations as a buyer

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let opts = {
  'page': 1, // Number | 
  'perPage': 24, // Number | 
  'offset': 56 // Number | 
};
apiInstance.myNegotiationsBuyingGet(opts, (error, data, response) => {
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
 **page** | **Number**|  | [optional] [default to 1]
 **perPage** | **Number**|  | [optional] [default to 24]
 **offset** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myNegotiationsIdAcceptPost

> myNegotiationsIdAcceptPost(id, opts)

Accept an offer

Accept an offer

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let id = "id_example"; // String | 
let opts = {
  'myNegotiationsIdAcceptPostRequest': new Reverb.MyNegotiationsIdAcceptPostRequest() // MyNegotiationsIdAcceptPostRequest | the content of the request
};
apiInstance.myNegotiationsIdAcceptPost(id, opts, (error, data, response) => {
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
 **myNegotiationsIdAcceptPostRequest** | [**MyNegotiationsIdAcceptPostRequest**](MyNegotiationsIdAcceptPostRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## myNegotiationsIdCounterPost

> myNegotiationsIdCounterPost(id, opts)

Counter an offer

Counter an offer

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let id = "id_example"; // String | 
let opts = {
  'conversationsConversationIdOfferPostRequest': new Reverb.ConversationsConversationIdOfferPostRequest() // ConversationsConversationIdOfferPostRequest | the content of the request
};
apiInstance.myNegotiationsIdCounterPost(id, opts, (error, data, response) => {
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
 **conversationsConversationIdOfferPostRequest** | [**ConversationsConversationIdOfferPostRequest**](ConversationsConversationIdOfferPostRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## myNegotiationsIdDeclinePost

> myNegotiationsIdDeclinePost(id)

Decline an offer

Decline an offer

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let id = "id_example"; // String | 
apiInstance.myNegotiationsIdDeclinePost(id, (error, data, response) => {
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


## myNegotiationsIdGet

> myNegotiationsIdGet(id)

Get offer details

Get offer details

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let id = "id_example"; // String | 
apiInstance.myNegotiationsIdGet(id, (error, data, response) => {
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


## myOrdersAwaitingFeedbackGet

> myOrdersAwaitingFeedbackGet()

List of orders that need feedback

List of orders that need feedback

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myOrdersAwaitingFeedbackGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myOrdersBuyingAllGet

> myOrdersBuyingAllGet()

Returns all orders, newest first.

Returns all orders, newest first.

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myOrdersBuyingAllGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myOrdersBuyingByUuidUuidGet

> myOrdersBuyingByUuidUuidGet(uuid)



### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.MyApi();
let uuid = "uuid_example"; // String | 
apiInstance.myOrdersBuyingByUuidUuidGet(uuid, (error, data, response) => {
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
 **uuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myOrdersBuyingIdGet

> myOrdersBuyingIdGet(id)

Returns order details for a buyer

Returns order details for a buyer

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let id = "id_example"; // String | 
apiInstance.myOrdersBuyingIdGet(id, (error, data, response) => {
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


## myOrdersBuyingIdMarkReceivedPost

> myOrdersBuyingIdMarkReceivedPost(id)

Marks an order as received by the buyer

Marks an order as received by the buyer

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let id = "id_example"; // String | 
apiInstance.myOrdersBuyingIdMarkReceivedPost(id, (error, data, response) => {
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


## myOrdersBuyingUnpaidGet

> myOrdersBuyingUnpaidGet()

Returns unpaid orders, newest first.

Returns unpaid orders, newest first.

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myOrdersBuyingUnpaidGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myOrdersSellingAllGet

> myOrdersSellingAllGet()

Get all seller orders, newest first.

Get all seller orders, newest first.

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myOrdersSellingAllGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myOrdersSellingAwaitingShipmentGet

> myOrdersSellingAwaitingShipmentGet()

Get unpaid seller orders, newest first.

Get unpaid seller orders, newest first.

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myOrdersSellingAwaitingShipmentGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myOrdersSellingBuyerHistoryBuyerIdGet

> myOrdersSellingBuyerHistoryBuyerIdGet(buyerId)

See previous orders from buyer

See previous orders from buyer

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let buyerId = "buyerId_example"; // String | 
apiInstance.myOrdersSellingBuyerHistoryBuyerIdGet(buyerId, (error, data, response) => {
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
 **buyerId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myOrdersSellingByUuidUuidGet

> myOrdersSellingByUuidUuidGet(uuid)



### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.MyApi();
let uuid = "uuid_example"; // String | 
apiInstance.myOrdersSellingByUuidUuidGet(uuid, (error, data, response) => {
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
 **uuid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myOrdersSellingIdGet

> myOrdersSellingIdGet(id)

Returns order details for a seller

Returns order details for a seller

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let id = "id_example"; // String | 
apiInstance.myOrdersSellingIdGet(id, (error, data, response) => {
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


## myOrdersSellingIdMarkPickedUpPost

> myOrdersSellingIdMarkPickedUpPost(id, opts)

Marks an order as picked up

Marks an order as picked up

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let id = "id_example"; // String | 
let opts = {
  'myOrdersSellingIdMarkPickedUpPostRequest': new Reverb.MyOrdersSellingIdMarkPickedUpPostRequest() // MyOrdersSellingIdMarkPickedUpPostRequest | the content of the request
};
apiInstance.myOrdersSellingIdMarkPickedUpPost(id, opts, (error, data, response) => {
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
 **myOrdersSellingIdMarkPickedUpPostRequest** | [**MyOrdersSellingIdMarkPickedUpPostRequest**](MyOrdersSellingIdMarkPickedUpPostRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## myOrdersSellingIdShipPost

> myOrdersSellingIdShipPost(id, opts)

Marks an order as shipped

Marks an order as shipped

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let id = "id_example"; // String | 
let opts = {
  'myOrdersSellingIdShipPostRequest': new Reverb.MyOrdersSellingIdShipPostRequest() // MyOrdersSellingIdShipPostRequest | the content of the request
};
apiInstance.myOrdersSellingIdShipPost(id, opts, (error, data, response) => {
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
 **myOrdersSellingIdShipPostRequest** | [**MyOrdersSellingIdShipPostRequest**](MyOrdersSellingIdShipPostRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## myOrdersSellingOrderIdRefundRequestsPost

> myOrdersSellingOrderIdRefundRequestsPost(orderId)

Initiate a refund for a sold order

Initiate a refund for a sold order

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let orderId = "orderId_example"; // String | 
apiInstance.myOrdersSellingOrderIdRefundRequestsPost(orderId, (error, data, response) => {
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
 **orderId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myOrdersSellingUnpaidGet

> myOrdersSellingUnpaidGet()

Get unpaid seller orders, newest first.

Get unpaid seller orders, newest first.

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myOrdersSellingUnpaidGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myPaymentsSellingGet

> myPaymentsSellingGet(opts)

Get payments

Get payments

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let opts = {
  'page': 1, // Number | 
  'perPage': 24, // Number | 
  'offset': 56, // Number | 
  'createdStartDate': "createdStartDate_example", // String | Filter by date created in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00
  'createdEndDate': "createdEndDate_example", // String | Filter by date created in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00
  'updatedStartDate': "updatedStartDate_example", // String | Filter by date modified in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00
  'updatedEndDate': "updatedEndDate_example", // String | Filter by date modified in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00
  'orderId': "orderId_example" // String | Look up payments by order id
};
apiInstance.myPaymentsSellingGet(opts, (error, data, response) => {
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
 **page** | **Number**|  | [optional] [default to 1]
 **perPage** | **Number**|  | [optional] [default to 24]
 **offset** | **Number**|  | [optional] 
 **createdStartDate** | **String**| Filter by date created in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00 | [optional] 
 **createdEndDate** | **String**| Filter by date created in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00 | [optional] 
 **updatedStartDate** | **String**| Filter by date modified in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00 | [optional] 
 **updatedEndDate** | **String**| Filter by date modified in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00 | [optional] 
 **orderId** | **String**| Look up payments by order id | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myPaymentsSellingIdGet

> myPaymentsSellingIdGet(id)

Get payment

Get payment

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let id = "id_example"; // String | 
apiInstance.myPaymentsSellingIdGet(id, (error, data, response) => {
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


## myPayoutsGet

> myPayoutsGet()

Get a list of payouts

Get a list of payouts

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myPayoutsGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myPayoutsIdLineItemsGet

> myPayoutsIdLineItemsGet(id)

Read the line items of a payout

Read the line items of a payout

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let id = "id_example"; // String | 
apiInstance.myPayoutsIdLineItemsGet(id, (error, data, response) => {
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


## myRefundRequestsSellingGet

> myRefundRequestsSellingGet()

Get a list of refund requests as a seller

Get a list of refund requests as a seller

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myRefundRequestsSellingGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myRefundRequestsSellingIdPut

> myRefundRequestsSellingIdPut(id)

Update a refund request for a sold order

Update a refund request for a sold order

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let id = "id_example"; // String | 
apiInstance.myRefundRequestsSellingIdPut(id, (error, data, response) => {
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


## myViewedListingsGet

> myViewedListingsGet()

Get a list of your recently viewed listings.

Get a list of your recently viewed listings.

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myViewedListingsGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myWishlistGet

> myWishlistGet()

Get a list of wishlisted items

Get a list of wishlisted items

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
apiInstance.myWishlistGet((error, data, response) => {
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

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## myWishlistIdDelete

> myWishlistIdDelete(id)

Remove a listing from your wishlist

Remove a listing from your wishlist

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let id = "id_example"; // String | 
apiInstance.myWishlistIdDelete(id, (error, data, response) => {
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


## myWishlistIdPut

> myWishlistIdPut(id)

Add a listing to your wishlist

Add a listing to your wishlist

### Example

```javascript
import Reverb from 'reverb';
let defaultClient = Reverb.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Reverb.MyApi();
let id = "id_example"; // String | 
apiInstance.myWishlistIdPut(id, (error, data, response) => {
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

