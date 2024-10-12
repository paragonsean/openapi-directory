# MyApi

All URIs are relative to *https://api.reverb.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**myAccountGet**](MyApi.md#myAccountGet) | **GET** /my/account | Get account details |
| [**myAccountPut**](MyApi.md#myAccountPut) | **PUT** /my/account | Update account details |
| [**myAddressesAddressIdDelete**](MyApi.md#myAddressesAddressIdDelete) | **DELETE** /my/addresses/{address_id} | Delete an existing address in your address book |
| [**myAddressesAddressIdPut**](MyApi.md#myAddressesAddressIdPut) | **PUT** /my/addresses/{address_id} | Update an existing address in your address book |
| [**myAddressesGet**](MyApi.md#myAddressesGet) | **GET** /my/addresses | See all addresses in your address book |
| [**myAddressesPost**](MyApi.md#myAddressesPost) | **POST** /my/addresses | Create a new address in your address book |
| [**myConversationsConversationIdMessagesPost**](MyApi.md#myConversationsConversationIdMessagesPost) | **POST** /my/conversations/{conversation_id}/messages | Send a message |
| [**myConversationsGet**](MyApi.md#myConversationsGet) | **GET** /my/conversations | Get a list of your conversations |
| [**myConversationsIdGet**](MyApi.md#myConversationsIdGet) | **GET** /my/conversations/{id} | Display conversation details with messages in natural time order (oldest to newest) |
| [**myConversationsIdPut**](MyApi.md#myConversationsIdPut) | **PUT** /my/conversations/{id} | Mark a conversation read/unread |
| [**myConversationsPost**](MyApi.md#myConversationsPost) | **POST** /my/conversations | Start a conversation |
| [**myCountsGet**](MyApi.md#myCountsGet) | **GET** /my/counts | Get your actionable status counts |
| [**myCuratedSetProductProductIdDelete**](MyApi.md#myCuratedSetProductProductIdDelete) | **DELETE** /my/curated_set/product/{product_id} |  |
| [**myCuratedSetProductProductIdPost**](MyApi.md#myCuratedSetProductProductIdPost) | **POST** /my/curated_set/product/{product_id} |  |
| [**myFeedCustomizeGet**](MyApi.md#myFeedCustomizeGet) | **GET** /my/feed/customize | get your feed customization options |
| [**myFeedGet**](MyApi.md#myFeedGet) | **GET** /my/feed | Get listings from your feed |
| [**myFeedGridGet**](MyApi.md#myFeedGridGet) | **GET** /my/feed/grid | get your feed |
| [**myFeedbackReceivedGet**](MyApi.md#myFeedbackReceivedGet) | **GET** /my/feedback/received | List of received feedback |
| [**myFeedbackSentGet**](MyApi.md#myFeedbackSentGet) | **GET** /my/feedback/sent | List of sent feedback |
| [**myFollowsArticlesGet**](MyApi.md#myFollowsArticlesGet) | **GET** /my/follows/articles | Returns a user&#39;s ArticleCategoryFollows |
| [**myFollowsArticlesPost**](MyApi.md#myFollowsArticlesPost) | **POST** /my/follows/articles | Set a user&#39;s ArticleCategoryFollows |
| [**myFollowsBrandsSlugDelete**](MyApi.md#myFollowsBrandsSlugDelete) | **DELETE** /my/follows/brands/{slug} | Unfollow a brand |
| [**myFollowsBrandsSlugGet**](MyApi.md#myFollowsBrandsSlugGet) | **GET** /my/follows/brands/{slug} | Follow status for a brand |
| [**myFollowsBrandsSlugPost**](MyApi.md#myFollowsBrandsSlugPost) | **POST** /my/follows/brands/{slug} | Follow a brand |
| [**myFollowsCategoriesCategorySubcategoryDelete**](MyApi.md#myFollowsCategoriesCategorySubcategoryDelete) | **DELETE** /my/follows/categories/{category}/{subcategory} | Unfollow a subcategory |
| [**myFollowsCategoriesCategorySubcategoryGet**](MyApi.md#myFollowsCategoriesCategorySubcategoryGet) | **GET** /my/follows/categories/{category}/{subcategory} | Follow status for a subcategory |
| [**myFollowsCategoriesCategorySubcategoryPost**](MyApi.md#myFollowsCategoriesCategorySubcategoryPost) | **POST** /my/follows/categories/{category}/{subcategory} | Follow a subcategory |
| [**myFollowsCategoriesIdentifierDelete**](MyApi.md#myFollowsCategoriesIdentifierDelete) | **DELETE** /my/follows/categories/{identifier} | Unfollow a category |
| [**myFollowsCategoriesIdentifierGet**](MyApi.md#myFollowsCategoriesIdentifierGet) | **GET** /my/follows/categories/{identifier} | Follow status for a category |
| [**myFollowsCategoriesIdentifierPost**](MyApi.md#myFollowsCategoriesIdentifierPost) | **POST** /my/follows/categories/{identifier} | Follow a category |
| [**myFollowsCategoriesUuidPost**](MyApi.md#myFollowsCategoriesUuidPost) | **POST** /my/follows/categories/{uuid} | Follow a category |
| [**myFollowsCollectionsSlugDelete**](MyApi.md#myFollowsCollectionsSlugDelete) | **DELETE** /my/follows/collections/{slug} | Unfollow a collection |
| [**myFollowsCollectionsSlugGet**](MyApi.md#myFollowsCollectionsSlugGet) | **GET** /my/follows/collections/{slug} | Follow status for a collection |
| [**myFollowsCollectionsSlugPost**](MyApi.md#myFollowsCollectionsSlugPost) | **POST** /my/follows/collections/{slug} | Follow a collection |
| [**myFollowsFollowIdAlertDelete**](MyApi.md#myFollowsFollowIdAlertDelete) | **DELETE** /my/follows/{follow_id}/alert |  |
| [**myFollowsFollowIdAlertPost**](MyApi.md#myFollowsFollowIdAlertPost) | **POST** /my/follows/{follow_id}/alert |  |
| [**myFollowsFollowIdDelete**](MyApi.md#myFollowsFollowIdDelete) | **DELETE** /my/follows/{follow_id} | Delete a follow |
| [**myFollowsGet**](MyApi.md#myFollowsGet) | **GET** /my/follows | See what the user is following |
| [**myFollowsHandpickedSlugDelete**](MyApi.md#myFollowsHandpickedSlugDelete) | **DELETE** /my/follows/handpicked/{slug} | Unfollow a handpicked collection |
| [**myFollowsHandpickedSlugGet**](MyApi.md#myFollowsHandpickedSlugGet) | **GET** /my/follows/handpicked/{slug} | Follow status for a handpicked collection |
| [**myFollowsHandpickedSlugPost**](MyApi.md#myFollowsHandpickedSlugPost) | **POST** /my/follows/handpicked/{slug} | Follow a handpicked collection |
| [**myFollowsSearchGet**](MyApi.md#myFollowsSearchGet) | **GET** /my/follows/search | Follow status for a search |
| [**myFollowsSearchPost**](MyApi.md#myFollowsSearchPost) | **POST** /my/follows/search | Follow a search |
| [**myFollowsShopsSlugDelete**](MyApi.md#myFollowsShopsSlugDelete) | **DELETE** /my/follows/shops/{slug} | Unfollow a shop |
| [**myFollowsShopsSlugGet**](MyApi.md#myFollowsShopsSlugGet) | **GET** /my/follows/shops/{slug} | Follow status for a shop |
| [**myFollowsShopsSlugPost**](MyApi.md#myFollowsShopsSlugPost) | **POST** /my/follows/shops/{slug} | Follow a shop |
| [**myListingsDraftsGet**](MyApi.md#myListingsDraftsGet) | **GET** /my/listings/drafts | Retrieve a list your draft listings |
| [**myListingsGet**](MyApi.md#myListingsGet) | **GET** /my/listings | Retrieve a list of live listings for the seller. To search all listings specify state&#x3D;all |
| [**myListingsNegotiationsGet**](MyApi.md#myListingsNegotiationsGet) | **GET** /my/listings/negotiations | Get a list of active negotiations as a seller |
| [**myListingsSlugStateEndPut**](MyApi.md#myListingsSlugStateEndPut) | **PUT** /my/listings/{slug}/state/end | End a listing |
| [**myListsGet**](MyApi.md#myListsGet) | **GET** /my/lists | Get a list of your lists (wishlist, watch list, etc) |
| [**myNegotiationsBuyingGet**](MyApi.md#myNegotiationsBuyingGet) | **GET** /my/negotiations/buying | Get a list of active negotiations as a buyer |
| [**myNegotiationsIdAcceptPost**](MyApi.md#myNegotiationsIdAcceptPost) | **POST** /my/negotiations/{id}/accept | Accept an offer |
| [**myNegotiationsIdCounterPost**](MyApi.md#myNegotiationsIdCounterPost) | **POST** /my/negotiations/{id}/counter | Counter an offer |
| [**myNegotiationsIdDeclinePost**](MyApi.md#myNegotiationsIdDeclinePost) | **POST** /my/negotiations/{id}/decline | Decline an offer |
| [**myNegotiationsIdGet**](MyApi.md#myNegotiationsIdGet) | **GET** /my/negotiations/{id} | Get offer details |
| [**myOrdersAwaitingFeedbackGet**](MyApi.md#myOrdersAwaitingFeedbackGet) | **GET** /my/orders/awaiting_feedback | List of orders that need feedback |
| [**myOrdersBuyingAllGet**](MyApi.md#myOrdersBuyingAllGet) | **GET** /my/orders/buying/all | Returns all orders, newest first. |
| [**myOrdersBuyingByUuidUuidGet**](MyApi.md#myOrdersBuyingByUuidUuidGet) | **GET** /my/orders/buying/by_uuid/{uuid} |  |
| [**myOrdersBuyingIdGet**](MyApi.md#myOrdersBuyingIdGet) | **GET** /my/orders/buying/{id} | Returns order details for a buyer |
| [**myOrdersBuyingIdMarkReceivedPost**](MyApi.md#myOrdersBuyingIdMarkReceivedPost) | **POST** /my/orders/buying/{id}/mark_received | Marks an order as received by the buyer |
| [**myOrdersBuyingUnpaidGet**](MyApi.md#myOrdersBuyingUnpaidGet) | **GET** /my/orders/buying/unpaid | Returns unpaid orders, newest first. |
| [**myOrdersSellingAllGet**](MyApi.md#myOrdersSellingAllGet) | **GET** /my/orders/selling/all | Get all seller orders, newest first. |
| [**myOrdersSellingAwaitingShipmentGet**](MyApi.md#myOrdersSellingAwaitingShipmentGet) | **GET** /my/orders/selling/awaiting_shipment | Get unpaid seller orders, newest first. |
| [**myOrdersSellingBuyerHistoryBuyerIdGet**](MyApi.md#myOrdersSellingBuyerHistoryBuyerIdGet) | **GET** /my/orders/selling/buyer_history/{buyer_id} | See previous orders from buyer |
| [**myOrdersSellingByUuidUuidGet**](MyApi.md#myOrdersSellingByUuidUuidGet) | **GET** /my/orders/selling/by_uuid/{uuid} |  |
| [**myOrdersSellingIdGet**](MyApi.md#myOrdersSellingIdGet) | **GET** /my/orders/selling/{id} | Returns order details for a seller |
| [**myOrdersSellingIdMarkPickedUpPost**](MyApi.md#myOrdersSellingIdMarkPickedUpPost) | **POST** /my/orders/selling/{id}/mark_picked_up | Marks an order as picked up |
| [**myOrdersSellingIdShipPost**](MyApi.md#myOrdersSellingIdShipPost) | **POST** /my/orders/selling/{id}/ship | Marks an order as shipped |
| [**myOrdersSellingOrderIdRefundRequestsPost**](MyApi.md#myOrdersSellingOrderIdRefundRequestsPost) | **POST** /my/orders/selling/{order_id}/refund_requests | Initiate a refund for a sold order |
| [**myOrdersSellingUnpaidGet**](MyApi.md#myOrdersSellingUnpaidGet) | **GET** /my/orders/selling/unpaid | Get unpaid seller orders, newest first. |
| [**myPaymentsSellingGet**](MyApi.md#myPaymentsSellingGet) | **GET** /my/payments/selling | Get payments |
| [**myPaymentsSellingIdGet**](MyApi.md#myPaymentsSellingIdGet) | **GET** /my/payments/selling/{id} | Get payment |
| [**myPayoutsGet**](MyApi.md#myPayoutsGet) | **GET** /my/payouts | Get a list of payouts |
| [**myPayoutsIdLineItemsGet**](MyApi.md#myPayoutsIdLineItemsGet) | **GET** /my/payouts/{id}/line_items | Read the line items of a payout |
| [**myRefundRequestsSellingGet**](MyApi.md#myRefundRequestsSellingGet) | **GET** /my/refund_requests/selling | Get a list of refund requests as a seller |
| [**myRefundRequestsSellingIdPut**](MyApi.md#myRefundRequestsSellingIdPut) | **PUT** /my/refund_requests/selling/{id} | Update a refund request for a sold order |
| [**myViewedListingsGet**](MyApi.md#myViewedListingsGet) | **GET** /my/viewed_listings | Get a list of your recently viewed listings. |
| [**myWishlistGet**](MyApi.md#myWishlistGet) | **GET** /my/wishlist | Get a list of wishlisted items |
| [**myWishlistIdDelete**](MyApi.md#myWishlistIdDelete) | **DELETE** /my/wishlist/{id} | Remove a listing from your wishlist |
| [**myWishlistIdPut**](MyApi.md#myWishlistIdPut) | **PUT** /my/wishlist/{id} | Add a listing to your wishlist |


<a id="myAccountGet"></a>
# **myAccountGet**
> myAccountGet()

Get account details

Get account details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myAccountGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myAccountGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myAccountPut"></a>
# **myAccountPut**
> myAccountPut(myAccountPutRequest)

Update account details

Update account details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    MyAccountPutRequest myAccountPutRequest = new MyAccountPutRequest(); // MyAccountPutRequest | the content of the request
    try {
      apiInstance.myAccountPut(myAccountPutRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myAccountPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **myAccountPutRequest** | [**MyAccountPutRequest**](MyAccountPutRequest.md)| the content of the request | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myAddressesAddressIdDelete"></a>
# **myAddressesAddressIdDelete**
> myAddressesAddressIdDelete(addressId)

Delete an existing address in your address book

Delete an existing address in your address book

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String addressId = "addressId_example"; // String | 
    try {
      apiInstance.myAddressesAddressIdDelete(addressId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myAddressesAddressIdDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **addressId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myAddressesAddressIdPut"></a>
# **myAddressesAddressIdPut**
> myAddressesAddressIdPut(addressId)

Update an existing address in your address book

Update an existing address in your address book

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String addressId = "addressId_example"; // String | 
    try {
      apiInstance.myAddressesAddressIdPut(addressId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myAddressesAddressIdPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **addressId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myAddressesGet"></a>
# **myAddressesGet**
> myAddressesGet()

See all addresses in your address book

See all addresses in your address book

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myAddressesGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myAddressesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myAddressesPost"></a>
# **myAddressesPost**
> myAddressesPost()

Create a new address in your address book

Create a new address in your address book

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myAddressesPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myAddressesPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myConversationsConversationIdMessagesPost"></a>
# **myConversationsConversationIdMessagesPost**
> myConversationsConversationIdMessagesPost(conversationId, listingsListingIdConversationsPostRequest)

Send a message

Send a message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String conversationId = "conversationId_example"; // String | 
    ListingsListingIdConversationsPostRequest listingsListingIdConversationsPostRequest = new ListingsListingIdConversationsPostRequest(); // ListingsListingIdConversationsPostRequest | the content of the request
    try {
      apiInstance.myConversationsConversationIdMessagesPost(conversationId, listingsListingIdConversationsPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myConversationsConversationIdMessagesPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **conversationId** | **String**|  | |
| **listingsListingIdConversationsPostRequest** | [**ListingsListingIdConversationsPostRequest**](ListingsListingIdConversationsPostRequest.md)| the content of the request | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myConversationsGet"></a>
# **myConversationsGet**
> myConversationsGet(search, unreadOnly, page, perPage, offset)

Get a list of your conversations

Get a list of your conversations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String search = "search_example"; // String | Query string to search conversations by
    Boolean unreadOnly = true; // Boolean | Show unread conversations only
    Integer page = 1; // Integer | 
    Integer perPage = 24; // Integer | 
    Integer offset = 56; // Integer | 
    try {
      apiInstance.myConversationsGet(search, unreadOnly, page, perPage, offset);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myConversationsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **search** | **String**| Query string to search conversations by | [optional] |
| **unreadOnly** | **Boolean**| Show unread conversations only | [optional] |
| **page** | **Integer**|  | [optional] [default to 1] |
| **perPage** | **Integer**|  | [optional] [default to 24] |
| **offset** | **Integer**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myConversationsIdGet"></a>
# **myConversationsIdGet**
> myConversationsIdGet(id)

Display conversation details with messages in natural time order (oldest to newest)

Display conversation details with messages in natural time order (oldest to newest)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.myConversationsIdGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myConversationsIdGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myConversationsIdPut"></a>
# **myConversationsIdPut**
> myConversationsIdPut(id, myConversationsIdPutRequest)

Mark a conversation read/unread

Mark a conversation read/unread

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String id = "id_example"; // String | 
    MyConversationsIdPutRequest myConversationsIdPutRequest = new MyConversationsIdPutRequest(); // MyConversationsIdPutRequest | the content of the request
    try {
      apiInstance.myConversationsIdPut(id, myConversationsIdPutRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myConversationsIdPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **myConversationsIdPutRequest** | [**MyConversationsIdPutRequest**](MyConversationsIdPutRequest.md)| the content of the request | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myConversationsPost"></a>
# **myConversationsPost**
> myConversationsPost(myConversationsPostRequest)

Start a conversation

Start a conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    MyConversationsPostRequest myConversationsPostRequest = new MyConversationsPostRequest(); // MyConversationsPostRequest | the content of the request
    try {
      apiInstance.myConversationsPost(myConversationsPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myConversationsPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **myConversationsPostRequest** | [**MyConversationsPostRequest**](MyConversationsPostRequest.md)| the content of the request | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myCountsGet"></a>
# **myCountsGet**
> myCountsGet()

Get your actionable status counts

Get your actionable status counts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myCountsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myCountsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myCuratedSetProductProductIdDelete"></a>
# **myCuratedSetProductProductIdDelete**
> myCuratedSetProductProductIdDelete(productId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    MyApi apiInstance = new MyApi(defaultClient);
    String productId = "productId_example"; // String | 
    try {
      apiInstance.myCuratedSetProductProductIdDelete(productId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myCuratedSetProductProductIdDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myCuratedSetProductProductIdPost"></a>
# **myCuratedSetProductProductIdPost**
> myCuratedSetProductProductIdPost(productId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    MyApi apiInstance = new MyApi(defaultClient);
    String productId = "productId_example"; // String | 
    try {
      apiInstance.myCuratedSetProductProductIdPost(productId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myCuratedSetProductProductIdPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFeedCustomizeGet"></a>
# **myFeedCustomizeGet**
> myFeedCustomizeGet()

get your feed customization options

get your feed customization options

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myFeedCustomizeGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFeedCustomizeGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFeedGet"></a>
# **myFeedGet**
> myFeedGet()

Get listings from your feed

Get listings from your feed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myFeedGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFeedGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFeedGridGet"></a>
# **myFeedGridGet**
> myFeedGridGet()

get your feed

get your feed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myFeedGridGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFeedGridGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFeedbackReceivedGet"></a>
# **myFeedbackReceivedGet**
> myFeedbackReceivedGet()

List of received feedback

List of received feedback

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myFeedbackReceivedGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFeedbackReceivedGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFeedbackSentGet"></a>
# **myFeedbackSentGet**
> myFeedbackSentGet()

List of sent feedback

List of sent feedback

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myFeedbackSentGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFeedbackSentGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsArticlesGet"></a>
# **myFollowsArticlesGet**
> myFollowsArticlesGet()

Returns a user&#39;s ArticleCategoryFollows

Returns a user&#39;s ArticleCategoryFollows

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myFollowsArticlesGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsArticlesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsArticlesPost"></a>
# **myFollowsArticlesPost**
> myFollowsArticlesPost(myFollowsArticlesPostRequest)

Set a user&#39;s ArticleCategoryFollows

Set a user&#39;s ArticleCategoryFollows

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    MyFollowsArticlesPostRequest myFollowsArticlesPostRequest = new MyFollowsArticlesPostRequest(); // MyFollowsArticlesPostRequest | the content of the request
    try {
      apiInstance.myFollowsArticlesPost(myFollowsArticlesPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsArticlesPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **myFollowsArticlesPostRequest** | [**MyFollowsArticlesPostRequest**](MyFollowsArticlesPostRequest.md)| the content of the request | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsBrandsSlugDelete"></a>
# **myFollowsBrandsSlugDelete**
> myFollowsBrandsSlugDelete(slug)

Unfollow a brand

Unfollow a brand

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.myFollowsBrandsSlugDelete(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsBrandsSlugDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **slug** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsBrandsSlugGet"></a>
# **myFollowsBrandsSlugGet**
> myFollowsBrandsSlugGet(slug)

Follow status for a brand

Follow status for a brand

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.myFollowsBrandsSlugGet(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsBrandsSlugGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **slug** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsBrandsSlugPost"></a>
# **myFollowsBrandsSlugPost**
> myFollowsBrandsSlugPost(slug)

Follow a brand

Follow a brand

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.myFollowsBrandsSlugPost(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsBrandsSlugPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **slug** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsCategoriesCategorySubcategoryDelete"></a>
# **myFollowsCategoriesCategorySubcategoryDelete**
> myFollowsCategoriesCategorySubcategoryDelete(category, subcategory)

Unfollow a subcategory

Unfollow a subcategory

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String category = "category_example"; // String | 
    String subcategory = "subcategory_example"; // String | 
    try {
      apiInstance.myFollowsCategoriesCategorySubcategoryDelete(category, subcategory);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsCategoriesCategorySubcategoryDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **category** | **String**|  | |
| **subcategory** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsCategoriesCategorySubcategoryGet"></a>
# **myFollowsCategoriesCategorySubcategoryGet**
> myFollowsCategoriesCategorySubcategoryGet(category, subcategory)

Follow status for a subcategory

Follow status for a subcategory

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String category = "category_example"; // String | 
    String subcategory = "subcategory_example"; // String | 
    try {
      apiInstance.myFollowsCategoriesCategorySubcategoryGet(category, subcategory);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsCategoriesCategorySubcategoryGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **category** | **String**|  | |
| **subcategory** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsCategoriesCategorySubcategoryPost"></a>
# **myFollowsCategoriesCategorySubcategoryPost**
> myFollowsCategoriesCategorySubcategoryPost(category, subcategory)

Follow a subcategory

Follow a subcategory

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String category = "category_example"; // String | 
    String subcategory = "subcategory_example"; // String | 
    try {
      apiInstance.myFollowsCategoriesCategorySubcategoryPost(category, subcategory);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsCategoriesCategorySubcategoryPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **category** | **String**|  | |
| **subcategory** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsCategoriesIdentifierDelete"></a>
# **myFollowsCategoriesIdentifierDelete**
> myFollowsCategoriesIdentifierDelete(identifier)

Unfollow a category

Unfollow a category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String identifier = "identifier_example"; // String | 
    try {
      apiInstance.myFollowsCategoriesIdentifierDelete(identifier);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsCategoriesIdentifierDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **identifier** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsCategoriesIdentifierGet"></a>
# **myFollowsCategoriesIdentifierGet**
> myFollowsCategoriesIdentifierGet(identifier)

Follow status for a category

Follow status for a category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String identifier = "identifier_example"; // String | 
    try {
      apiInstance.myFollowsCategoriesIdentifierGet(identifier);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsCategoriesIdentifierGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **identifier** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsCategoriesIdentifierPost"></a>
# **myFollowsCategoriesIdentifierPost**
> myFollowsCategoriesIdentifierPost(identifier)

Follow a category

Follow a category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String identifier = "identifier_example"; // String | 
    try {
      apiInstance.myFollowsCategoriesIdentifierPost(identifier);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsCategoriesIdentifierPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **identifier** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsCategoriesUuidPost"></a>
# **myFollowsCategoriesUuidPost**
> myFollowsCategoriesUuidPost(uuid)

Follow a category

Follow a category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String uuid = "uuid_example"; // String | 
    try {
      apiInstance.myFollowsCategoriesUuidPost(uuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsCategoriesUuidPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **uuid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsCollectionsSlugDelete"></a>
# **myFollowsCollectionsSlugDelete**
> myFollowsCollectionsSlugDelete(slug)

Unfollow a collection

Unfollow a collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.myFollowsCollectionsSlugDelete(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsCollectionsSlugDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **slug** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsCollectionsSlugGet"></a>
# **myFollowsCollectionsSlugGet**
> myFollowsCollectionsSlugGet(slug)

Follow status for a collection

Follow status for a collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.myFollowsCollectionsSlugGet(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsCollectionsSlugGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **slug** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsCollectionsSlugPost"></a>
# **myFollowsCollectionsSlugPost**
> myFollowsCollectionsSlugPost(slug)

Follow a collection

Follow a collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.myFollowsCollectionsSlugPost(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsCollectionsSlugPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **slug** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsFollowIdAlertDelete"></a>
# **myFollowsFollowIdAlertDelete**
> myFollowsFollowIdAlertDelete(followId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    MyApi apiInstance = new MyApi(defaultClient);
    String followId = "followId_example"; // String | 
    try {
      apiInstance.myFollowsFollowIdAlertDelete(followId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsFollowIdAlertDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **followId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsFollowIdAlertPost"></a>
# **myFollowsFollowIdAlertPost**
> myFollowsFollowIdAlertPost(followId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    MyApi apiInstance = new MyApi(defaultClient);
    String followId = "followId_example"; // String | 
    try {
      apiInstance.myFollowsFollowIdAlertPost(followId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsFollowIdAlertPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **followId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsFollowIdDelete"></a>
# **myFollowsFollowIdDelete**
> myFollowsFollowIdDelete(followId)

Delete a follow

Delete a follow

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String followId = "followId_example"; // String | 
    try {
      apiInstance.myFollowsFollowIdDelete(followId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsFollowIdDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **followId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsGet"></a>
# **myFollowsGet**
> myFollowsGet()

See what the user is following

See what the user is following

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myFollowsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsHandpickedSlugDelete"></a>
# **myFollowsHandpickedSlugDelete**
> myFollowsHandpickedSlugDelete(slug)

Unfollow a handpicked collection

Unfollow a handpicked collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.myFollowsHandpickedSlugDelete(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsHandpickedSlugDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **slug** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsHandpickedSlugGet"></a>
# **myFollowsHandpickedSlugGet**
> myFollowsHandpickedSlugGet(slug)

Follow status for a handpicked collection

Follow status for a handpicked collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.myFollowsHandpickedSlugGet(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsHandpickedSlugGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **slug** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsHandpickedSlugPost"></a>
# **myFollowsHandpickedSlugPost**
> myFollowsHandpickedSlugPost(slug)

Follow a handpicked collection

Follow a handpicked collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.myFollowsHandpickedSlugPost(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsHandpickedSlugPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **slug** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsSearchGet"></a>
# **myFollowsSearchGet**
> myFollowsSearchGet()

Follow status for a search

Follow status for a search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myFollowsSearchGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsSearchGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsSearchPost"></a>
# **myFollowsSearchPost**
> myFollowsSearchPost(myFollowsSearchPostRequest)

Follow a search

Follow a search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    MyFollowsSearchPostRequest myFollowsSearchPostRequest = new MyFollowsSearchPostRequest(); // MyFollowsSearchPostRequest | the content of the request
    try {
      apiInstance.myFollowsSearchPost(myFollowsSearchPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsSearchPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **myFollowsSearchPostRequest** | [**MyFollowsSearchPostRequest**](MyFollowsSearchPostRequest.md)| the content of the request | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsShopsSlugDelete"></a>
# **myFollowsShopsSlugDelete**
> myFollowsShopsSlugDelete(slug)

Unfollow a shop

Unfollow a shop

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.myFollowsShopsSlugDelete(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsShopsSlugDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **slug** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsShopsSlugGet"></a>
# **myFollowsShopsSlugGet**
> myFollowsShopsSlugGet(slug)

Follow status for a shop

Follow status for a shop

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.myFollowsShopsSlugGet(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsShopsSlugGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **slug** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myFollowsShopsSlugPost"></a>
# **myFollowsShopsSlugPost**
> myFollowsShopsSlugPost(slug)

Follow a shop

Follow a shop

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.myFollowsShopsSlugPost(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myFollowsShopsSlugPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **slug** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myListingsDraftsGet"></a>
# **myListingsDraftsGet**
> myListingsDraftsGet(query, auctionPriceMax, category, productType, conditions, decade, finish, handmade, itemCity, itemCountry, itemRegion, itemState, make, model, mustNot, priceMax, priceMin, currency, yearMax, yearMin, acceptsGiftCards, preferredSeller, shop, shopId, listingType, shipsTo, excludeAuctions, acceptsPaymentPlans, watchersCountMin, notIds, localPickup)

Retrieve a list your draft listings

Retrieve a list your draft listings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String query = "query_example"; // String | Search query.
    Float auctionPriceMax = 3.4F; // Float | Maximum current auction price
    String category = "category_example"; // String | Category slug from /api/categories
    String productType = "productType_example"; // String | Product type slug from /api/categories
    List<String> conditions = Arrays.asList(); // List<String> | Condition: all,new,b-stock,used,non-functioning,all-but-new,poor,fair,good,very-good,excellent,mint
    String decade = "decade_example"; // String | Decade: e.g. 1970s, early 70s
    String finish = "finish_example"; // String | Visual finish of the item, common for guitars
    Boolean handmade = true; // Boolean | Handmade items only
    String itemCity = "itemCity_example"; // String | City where item is located
    String itemCountry = "itemCountry_example"; // String | DEPRECATED - Country code where item is located
    String itemRegion = "itemRegion_example"; // String | Country code where item is located
    String itemState = "itemState_example"; // String | State or region code where item is located
    List<String> make = Arrays.asList(); // List<String> | Make(s)/brand of item (e.g. Fender). Can take a single value or an array.
    String model = "model_example"; // String | Model of item (e.g. Stratocaster)
    String mustNot = "mustNot_example"; // String | Search term negation. If you want to exclude a term, add it here
    Float priceMax = 3.4F; // Float | Maximum price of search results (USD)
    Float priceMin = 3.4F; // Float | Minimum price of search results (USD)
    String currency = "currency_example"; // String | The currency to be used for the price filters
    Integer yearMax = 56; // Integer | Maximum year of manufacture
    Integer yearMin = 56; // Integer | Minumum year of manufacture
    Boolean acceptsGiftCards = true; // Boolean | If true, include only items that accept gift cards
    Boolean preferredSeller = true; // Boolean | If true, include only items by Reverb Preferred Sellers
    String shop = "shop_example"; // String | Slug of shop to search
    String shopId = "shopId_example"; // String | ID of shop to search
    String listingType = "listingType_example"; // String | Type of listing: auctions,offers
    String shipsTo = "shipsTo_example"; // String | Limit search to items that ship to this country code
    Boolean excludeAuctions = true; // Boolean | If true, exclude auctions
    Boolean acceptsPaymentPlans = true; // Boolean | If true, only show items that can be purchased with a payment plan
    Integer watchersCountMin = 56; // Integer | Minimum number of watchers (used to find popular items)
    List<String> notIds = Arrays.asList(); // List<String> | Listing ID negation. If you want to exclude a listing, add it here.
    Boolean localPickup = true; // Boolean | Only items that offer local pickup
    try {
      apiInstance.myListingsDraftsGet(query, auctionPriceMax, category, productType, conditions, decade, finish, handmade, itemCity, itemCountry, itemRegion, itemState, make, model, mustNot, priceMax, priceMin, currency, yearMax, yearMin, acceptsGiftCards, preferredSeller, shop, shopId, listingType, shipsTo, excludeAuctions, acceptsPaymentPlans, watchersCountMin, notIds, localPickup);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myListingsDraftsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **query** | **String**| Search query. | [optional] |
| **auctionPriceMax** | **Float**| Maximum current auction price | [optional] |
| **category** | **String**| Category slug from /api/categories | [optional] |
| **productType** | **String**| Product type slug from /api/categories | [optional] |
| **conditions** | [**List&lt;String&gt;**](String.md)| Condition: all,new,b-stock,used,non-functioning,all-but-new,poor,fair,good,very-good,excellent,mint | [optional] |
| **decade** | **String**| Decade: e.g. 1970s, early 70s | [optional] |
| **finish** | **String**| Visual finish of the item, common for guitars | [optional] |
| **handmade** | **Boolean**| Handmade items only | [optional] |
| **itemCity** | **String**| City where item is located | [optional] |
| **itemCountry** | **String**| DEPRECATED - Country code where item is located | [optional] |
| **itemRegion** | **String**| Country code where item is located | [optional] |
| **itemState** | **String**| State or region code where item is located | [optional] |
| **make** | [**List&lt;String&gt;**](String.md)| Make(s)/brand of item (e.g. Fender). Can take a single value or an array. | [optional] |
| **model** | **String**| Model of item (e.g. Stratocaster) | [optional] |
| **mustNot** | **String**| Search term negation. If you want to exclude a term, add it here | [optional] |
| **priceMax** | **Float**| Maximum price of search results (USD) | [optional] |
| **priceMin** | **Float**| Minimum price of search results (USD) | [optional] |
| **currency** | **String**| The currency to be used for the price filters | [optional] |
| **yearMax** | **Integer**| Maximum year of manufacture | [optional] |
| **yearMin** | **Integer**| Minumum year of manufacture | [optional] |
| **acceptsGiftCards** | **Boolean**| If true, include only items that accept gift cards | [optional] |
| **preferredSeller** | **Boolean**| If true, include only items by Reverb Preferred Sellers | [optional] |
| **shop** | **String**| Slug of shop to search | [optional] |
| **shopId** | **String**| ID of shop to search | [optional] |
| **listingType** | **String**| Type of listing: auctions,offers | [optional] |
| **shipsTo** | **String**| Limit search to items that ship to this country code | [optional] |
| **excludeAuctions** | **Boolean**| If true, exclude auctions | [optional] |
| **acceptsPaymentPlans** | **Boolean**| If true, only show items that can be purchased with a payment plan | [optional] |
| **watchersCountMin** | **Integer**| Minimum number of watchers (used to find popular items) | [optional] |
| **notIds** | [**List&lt;String&gt;**](String.md)| Listing ID negation. If you want to exclude a listing, add it here. | [optional] |
| **localPickup** | **Boolean**| Only items that offer local pickup | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myListingsGet"></a>
# **myListingsGet**
> myListingsGet(query, auctionPriceMax, category, productType, conditions, decade, finish, handmade, itemCity, itemCountry, itemRegion, itemState, make, model, mustNot, priceMax, priceMin, currency, yearMax, yearMin, acceptsGiftCards, preferredSeller, shop, shopId, listingType, shipsTo, excludeAuctions, acceptsPaymentPlans, watchersCountMin, notIds, localPickup, state, sku)

Retrieve a list of live listings for the seller. To search all listings specify state&#x3D;all

Retrieve a list of live listings for the seller. To search all listings specify state&#x3D;all

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String query = "query_example"; // String | Search query.
    Float auctionPriceMax = 3.4F; // Float | Maximum current auction price
    String category = "category_example"; // String | Category slug from /api/categories
    String productType = "productType_example"; // String | Product type slug from /api/categories
    List<String> conditions = Arrays.asList(); // List<String> | Condition: all,new,b-stock,used,non-functioning,all-but-new,poor,fair,good,very-good,excellent,mint
    String decade = "decade_example"; // String | Decade: e.g. 1970s, early 70s
    String finish = "finish_example"; // String | Visual finish of the item, common for guitars
    Boolean handmade = true; // Boolean | Handmade items only
    String itemCity = "itemCity_example"; // String | City where item is located
    String itemCountry = "itemCountry_example"; // String | DEPRECATED - Country code where item is located
    String itemRegion = "itemRegion_example"; // String | Country code where item is located
    String itemState = "itemState_example"; // String | State or region code where item is located
    List<String> make = Arrays.asList(); // List<String> | Make(s)/brand of item (e.g. Fender). Can take a single value or an array.
    String model = "model_example"; // String | Model of item (e.g. Stratocaster)
    String mustNot = "mustNot_example"; // String | Search term negation. If you want to exclude a term, add it here
    Float priceMax = 3.4F; // Float | Maximum price of search results (USD)
    Float priceMin = 3.4F; // Float | Minimum price of search results (USD)
    String currency = "currency_example"; // String | The currency to be used for the price filters
    Integer yearMax = 56; // Integer | Maximum year of manufacture
    Integer yearMin = 56; // Integer | Minumum year of manufacture
    Boolean acceptsGiftCards = true; // Boolean | If true, include only items that accept gift cards
    Boolean preferredSeller = true; // Boolean | If true, include only items by Reverb Preferred Sellers
    String shop = "shop_example"; // String | Slug of shop to search
    String shopId = "shopId_example"; // String | ID of shop to search
    String listingType = "listingType_example"; // String | Type of listing: auctions,offers
    String shipsTo = "shipsTo_example"; // String | Limit search to items that ship to this country code
    Boolean excludeAuctions = true; // Boolean | If true, exclude auctions
    Boolean acceptsPaymentPlans = true; // Boolean | If true, only show items that can be purchased with a payment plan
    Integer watchersCountMin = 56; // Integer | Minimum number of watchers (used to find popular items)
    List<String> notIds = Arrays.asList(); // List<String> | Listing ID negation. If you want to exclude a listing, add it here.
    Boolean localPickup = true; // Boolean | Only items that offer local pickup
    String state = "live"; // String | Available: [\"all\", \"draft\", \"ended\", \"live\", \"ordered\", \"sold_out\", \"suspended\", \"seller_unavailable\"]. Defaults to 'live'
    String sku = "sku_example"; // String | Find a listing by sku
    try {
      apiInstance.myListingsGet(query, auctionPriceMax, category, productType, conditions, decade, finish, handmade, itemCity, itemCountry, itemRegion, itemState, make, model, mustNot, priceMax, priceMin, currency, yearMax, yearMin, acceptsGiftCards, preferredSeller, shop, shopId, listingType, shipsTo, excludeAuctions, acceptsPaymentPlans, watchersCountMin, notIds, localPickup, state, sku);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myListingsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **query** | **String**| Search query. | [optional] |
| **auctionPriceMax** | **Float**| Maximum current auction price | [optional] |
| **category** | **String**| Category slug from /api/categories | [optional] |
| **productType** | **String**| Product type slug from /api/categories | [optional] |
| **conditions** | [**List&lt;String&gt;**](String.md)| Condition: all,new,b-stock,used,non-functioning,all-but-new,poor,fair,good,very-good,excellent,mint | [optional] |
| **decade** | **String**| Decade: e.g. 1970s, early 70s | [optional] |
| **finish** | **String**| Visual finish of the item, common for guitars | [optional] |
| **handmade** | **Boolean**| Handmade items only | [optional] |
| **itemCity** | **String**| City where item is located | [optional] |
| **itemCountry** | **String**| DEPRECATED - Country code where item is located | [optional] |
| **itemRegion** | **String**| Country code where item is located | [optional] |
| **itemState** | **String**| State or region code where item is located | [optional] |
| **make** | [**List&lt;String&gt;**](String.md)| Make(s)/brand of item (e.g. Fender). Can take a single value or an array. | [optional] |
| **model** | **String**| Model of item (e.g. Stratocaster) | [optional] |
| **mustNot** | **String**| Search term negation. If you want to exclude a term, add it here | [optional] |
| **priceMax** | **Float**| Maximum price of search results (USD) | [optional] |
| **priceMin** | **Float**| Minimum price of search results (USD) | [optional] |
| **currency** | **String**| The currency to be used for the price filters | [optional] |
| **yearMax** | **Integer**| Maximum year of manufacture | [optional] |
| **yearMin** | **Integer**| Minumum year of manufacture | [optional] |
| **acceptsGiftCards** | **Boolean**| If true, include only items that accept gift cards | [optional] |
| **preferredSeller** | **Boolean**| If true, include only items by Reverb Preferred Sellers | [optional] |
| **shop** | **String**| Slug of shop to search | [optional] |
| **shopId** | **String**| ID of shop to search | [optional] |
| **listingType** | **String**| Type of listing: auctions,offers | [optional] |
| **shipsTo** | **String**| Limit search to items that ship to this country code | [optional] |
| **excludeAuctions** | **Boolean**| If true, exclude auctions | [optional] |
| **acceptsPaymentPlans** | **Boolean**| If true, only show items that can be purchased with a payment plan | [optional] |
| **watchersCountMin** | **Integer**| Minimum number of watchers (used to find popular items) | [optional] |
| **notIds** | [**List&lt;String&gt;**](String.md)| Listing ID negation. If you want to exclude a listing, add it here. | [optional] |
| **localPickup** | **Boolean**| Only items that offer local pickup | [optional] |
| **state** | **String**| Available: [\&quot;all\&quot;, \&quot;draft\&quot;, \&quot;ended\&quot;, \&quot;live\&quot;, \&quot;ordered\&quot;, \&quot;sold_out\&quot;, \&quot;suspended\&quot;, \&quot;seller_unavailable\&quot;]. Defaults to &#39;live&#39; | [optional] [default to live] |
| **sku** | **String**| Find a listing by sku | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myListingsNegotiationsGet"></a>
# **myListingsNegotiationsGet**
> myListingsNegotiationsGet(page, perPage, offset)

Get a list of active negotiations as a seller

Get a list of active negotiations as a seller

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    Integer page = 1; // Integer | 
    Integer perPage = 24; // Integer | 
    Integer offset = 56; // Integer | 
    try {
      apiInstance.myListingsNegotiationsGet(page, perPage, offset);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myListingsNegotiationsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**|  | [optional] [default to 1] |
| **perPage** | **Integer**|  | [optional] [default to 24] |
| **offset** | **Integer**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myListingsSlugStateEndPut"></a>
# **myListingsSlugStateEndPut**
> myListingsSlugStateEndPut(slug, myListingsSlugStateEndPutRequest)

End a listing

End a listing

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String slug = "slug_example"; // String | 
    MyListingsSlugStateEndPutRequest myListingsSlugStateEndPutRequest = new MyListingsSlugStateEndPutRequest(); // MyListingsSlugStateEndPutRequest | the content of the request
    try {
      apiInstance.myListingsSlugStateEndPut(slug, myListingsSlugStateEndPutRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myListingsSlugStateEndPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **slug** | **String**|  | |
| **myListingsSlugStateEndPutRequest** | [**MyListingsSlugStateEndPutRequest**](MyListingsSlugStateEndPutRequest.md)| the content of the request | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myListsGet"></a>
# **myListsGet**
> myListsGet()

Get a list of your lists (wishlist, watch list, etc)

Get a list of your lists (wishlist, watch list, etc)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myListsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myListsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myNegotiationsBuyingGet"></a>
# **myNegotiationsBuyingGet**
> myNegotiationsBuyingGet(page, perPage, offset)

Get a list of active negotiations as a buyer

Get a list of active negotiations as a buyer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    Integer page = 1; // Integer | 
    Integer perPage = 24; // Integer | 
    Integer offset = 56; // Integer | 
    try {
      apiInstance.myNegotiationsBuyingGet(page, perPage, offset);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myNegotiationsBuyingGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**|  | [optional] [default to 1] |
| **perPage** | **Integer**|  | [optional] [default to 24] |
| **offset** | **Integer**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myNegotiationsIdAcceptPost"></a>
# **myNegotiationsIdAcceptPost**
> myNegotiationsIdAcceptPost(id, myNegotiationsIdAcceptPostRequest)

Accept an offer

Accept an offer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String id = "id_example"; // String | 
    MyNegotiationsIdAcceptPostRequest myNegotiationsIdAcceptPostRequest = new MyNegotiationsIdAcceptPostRequest(); // MyNegotiationsIdAcceptPostRequest | the content of the request
    try {
      apiInstance.myNegotiationsIdAcceptPost(id, myNegotiationsIdAcceptPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myNegotiationsIdAcceptPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **myNegotiationsIdAcceptPostRequest** | [**MyNegotiationsIdAcceptPostRequest**](MyNegotiationsIdAcceptPostRequest.md)| the content of the request | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myNegotiationsIdCounterPost"></a>
# **myNegotiationsIdCounterPost**
> myNegotiationsIdCounterPost(id, conversationsConversationIdOfferPostRequest)

Counter an offer

Counter an offer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String id = "id_example"; // String | 
    ConversationsConversationIdOfferPostRequest conversationsConversationIdOfferPostRequest = new ConversationsConversationIdOfferPostRequest(); // ConversationsConversationIdOfferPostRequest | the content of the request
    try {
      apiInstance.myNegotiationsIdCounterPost(id, conversationsConversationIdOfferPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myNegotiationsIdCounterPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **conversationsConversationIdOfferPostRequest** | [**ConversationsConversationIdOfferPostRequest**](ConversationsConversationIdOfferPostRequest.md)| the content of the request | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myNegotiationsIdDeclinePost"></a>
# **myNegotiationsIdDeclinePost**
> myNegotiationsIdDeclinePost(id)

Decline an offer

Decline an offer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.myNegotiationsIdDeclinePost(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myNegotiationsIdDeclinePost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myNegotiationsIdGet"></a>
# **myNegotiationsIdGet**
> myNegotiationsIdGet(id)

Get offer details

Get offer details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.myNegotiationsIdGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myNegotiationsIdGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myOrdersAwaitingFeedbackGet"></a>
# **myOrdersAwaitingFeedbackGet**
> myOrdersAwaitingFeedbackGet()

List of orders that need feedback

List of orders that need feedback

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myOrdersAwaitingFeedbackGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myOrdersAwaitingFeedbackGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myOrdersBuyingAllGet"></a>
# **myOrdersBuyingAllGet**
> myOrdersBuyingAllGet()

Returns all orders, newest first.

Returns all orders, newest first.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myOrdersBuyingAllGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myOrdersBuyingAllGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myOrdersBuyingByUuidUuidGet"></a>
# **myOrdersBuyingByUuidUuidGet**
> myOrdersBuyingByUuidUuidGet(uuid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    MyApi apiInstance = new MyApi(defaultClient);
    String uuid = "uuid_example"; // String | 
    try {
      apiInstance.myOrdersBuyingByUuidUuidGet(uuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myOrdersBuyingByUuidUuidGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **uuid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myOrdersBuyingIdGet"></a>
# **myOrdersBuyingIdGet**
> myOrdersBuyingIdGet(id)

Returns order details for a buyer

Returns order details for a buyer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.myOrdersBuyingIdGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myOrdersBuyingIdGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myOrdersBuyingIdMarkReceivedPost"></a>
# **myOrdersBuyingIdMarkReceivedPost**
> myOrdersBuyingIdMarkReceivedPost(id)

Marks an order as received by the buyer

Marks an order as received by the buyer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.myOrdersBuyingIdMarkReceivedPost(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myOrdersBuyingIdMarkReceivedPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myOrdersBuyingUnpaidGet"></a>
# **myOrdersBuyingUnpaidGet**
> myOrdersBuyingUnpaidGet()

Returns unpaid orders, newest first.

Returns unpaid orders, newest first.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myOrdersBuyingUnpaidGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myOrdersBuyingUnpaidGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myOrdersSellingAllGet"></a>
# **myOrdersSellingAllGet**
> myOrdersSellingAllGet()

Get all seller orders, newest first.

Get all seller orders, newest first.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myOrdersSellingAllGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myOrdersSellingAllGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myOrdersSellingAwaitingShipmentGet"></a>
# **myOrdersSellingAwaitingShipmentGet**
> myOrdersSellingAwaitingShipmentGet()

Get unpaid seller orders, newest first.

Get unpaid seller orders, newest first.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myOrdersSellingAwaitingShipmentGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myOrdersSellingAwaitingShipmentGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myOrdersSellingBuyerHistoryBuyerIdGet"></a>
# **myOrdersSellingBuyerHistoryBuyerIdGet**
> myOrdersSellingBuyerHistoryBuyerIdGet(buyerId)

See previous orders from buyer

See previous orders from buyer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String buyerId = "buyerId_example"; // String | 
    try {
      apiInstance.myOrdersSellingBuyerHistoryBuyerIdGet(buyerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myOrdersSellingBuyerHistoryBuyerIdGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **buyerId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myOrdersSellingByUuidUuidGet"></a>
# **myOrdersSellingByUuidUuidGet**
> myOrdersSellingByUuidUuidGet(uuid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    MyApi apiInstance = new MyApi(defaultClient);
    String uuid = "uuid_example"; // String | 
    try {
      apiInstance.myOrdersSellingByUuidUuidGet(uuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myOrdersSellingByUuidUuidGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **uuid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myOrdersSellingIdGet"></a>
# **myOrdersSellingIdGet**
> myOrdersSellingIdGet(id)

Returns order details for a seller

Returns order details for a seller

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.myOrdersSellingIdGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myOrdersSellingIdGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myOrdersSellingIdMarkPickedUpPost"></a>
# **myOrdersSellingIdMarkPickedUpPost**
> myOrdersSellingIdMarkPickedUpPost(id, myOrdersSellingIdMarkPickedUpPostRequest)

Marks an order as picked up

Marks an order as picked up

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String id = "id_example"; // String | 
    MyOrdersSellingIdMarkPickedUpPostRequest myOrdersSellingIdMarkPickedUpPostRequest = new MyOrdersSellingIdMarkPickedUpPostRequest(); // MyOrdersSellingIdMarkPickedUpPostRequest | the content of the request
    try {
      apiInstance.myOrdersSellingIdMarkPickedUpPost(id, myOrdersSellingIdMarkPickedUpPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myOrdersSellingIdMarkPickedUpPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **myOrdersSellingIdMarkPickedUpPostRequest** | [**MyOrdersSellingIdMarkPickedUpPostRequest**](MyOrdersSellingIdMarkPickedUpPostRequest.md)| the content of the request | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myOrdersSellingIdShipPost"></a>
# **myOrdersSellingIdShipPost**
> myOrdersSellingIdShipPost(id, myOrdersSellingIdShipPostRequest)

Marks an order as shipped

Marks an order as shipped

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String id = "id_example"; // String | 
    MyOrdersSellingIdShipPostRequest myOrdersSellingIdShipPostRequest = new MyOrdersSellingIdShipPostRequest(); // MyOrdersSellingIdShipPostRequest | the content of the request
    try {
      apiInstance.myOrdersSellingIdShipPost(id, myOrdersSellingIdShipPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myOrdersSellingIdShipPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |
| **myOrdersSellingIdShipPostRequest** | [**MyOrdersSellingIdShipPostRequest**](MyOrdersSellingIdShipPostRequest.md)| the content of the request | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myOrdersSellingOrderIdRefundRequestsPost"></a>
# **myOrdersSellingOrderIdRefundRequestsPost**
> myOrdersSellingOrderIdRefundRequestsPost(orderId)

Initiate a refund for a sold order

Initiate a refund for a sold order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String orderId = "orderId_example"; // String | 
    try {
      apiInstance.myOrdersSellingOrderIdRefundRequestsPost(orderId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myOrdersSellingOrderIdRefundRequestsPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **orderId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myOrdersSellingUnpaidGet"></a>
# **myOrdersSellingUnpaidGet**
> myOrdersSellingUnpaidGet()

Get unpaid seller orders, newest first.

Get unpaid seller orders, newest first.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myOrdersSellingUnpaidGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myOrdersSellingUnpaidGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myPaymentsSellingGet"></a>
# **myPaymentsSellingGet**
> myPaymentsSellingGet(page, perPage, offset, createdStartDate, createdEndDate, updatedStartDate, updatedEndDate, orderId)

Get payments

Get payments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    Integer page = 1; // Integer | 
    Integer perPage = 24; // Integer | 
    Integer offset = 56; // Integer | 
    String createdStartDate = "createdStartDate_example"; // String | Filter by date created in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00
    String createdEndDate = "createdEndDate_example"; // String | Filter by date created in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00
    String updatedStartDate = "updatedStartDate_example"; // String | Filter by date modified in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00
    String updatedEndDate = "updatedEndDate_example"; // String | Filter by date modified in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00
    String orderId = "orderId_example"; // String | Look up payments by order id
    try {
      apiInstance.myPaymentsSellingGet(page, perPage, offset, createdStartDate, createdEndDate, updatedStartDate, updatedEndDate, orderId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myPaymentsSellingGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**|  | [optional] [default to 1] |
| **perPage** | **Integer**|  | [optional] [default to 24] |
| **offset** | **Integer**|  | [optional] |
| **createdStartDate** | **String**| Filter by date created in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00 | [optional] |
| **createdEndDate** | **String**| Filter by date created in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00 | [optional] |
| **updatedStartDate** | **String**| Filter by date modified in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00 | [optional] |
| **updatedEndDate** | **String**| Filter by date modified in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00 | [optional] |
| **orderId** | **String**| Look up payments by order id | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myPaymentsSellingIdGet"></a>
# **myPaymentsSellingIdGet**
> myPaymentsSellingIdGet(id)

Get payment

Get payment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.myPaymentsSellingIdGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myPaymentsSellingIdGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myPayoutsGet"></a>
# **myPayoutsGet**
> myPayoutsGet()

Get a list of payouts

Get a list of payouts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myPayoutsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myPayoutsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myPayoutsIdLineItemsGet"></a>
# **myPayoutsIdLineItemsGet**
> myPayoutsIdLineItemsGet(id)

Read the line items of a payout

Read the line items of a payout

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.myPayoutsIdLineItemsGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myPayoutsIdLineItemsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myRefundRequestsSellingGet"></a>
# **myRefundRequestsSellingGet**
> myRefundRequestsSellingGet()

Get a list of refund requests as a seller

Get a list of refund requests as a seller

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myRefundRequestsSellingGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myRefundRequestsSellingGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myRefundRequestsSellingIdPut"></a>
# **myRefundRequestsSellingIdPut**
> myRefundRequestsSellingIdPut(id)

Update a refund request for a sold order

Update a refund request for a sold order

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.myRefundRequestsSellingIdPut(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myRefundRequestsSellingIdPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myViewedListingsGet"></a>
# **myViewedListingsGet**
> myViewedListingsGet()

Get a list of your recently viewed listings.

Get a list of your recently viewed listings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myViewedListingsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myViewedListingsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myWishlistGet"></a>
# **myWishlistGet**
> myWishlistGet()

Get a list of wishlisted items

Get a list of wishlisted items

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    try {
      apiInstance.myWishlistGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myWishlistGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myWishlistIdDelete"></a>
# **myWishlistIdDelete**
> myWishlistIdDelete(id)

Remove a listing from your wishlist

Remove a listing from your wishlist

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.myWishlistIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myWishlistIdDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="myWishlistIdPut"></a>
# **myWishlistIdPut**
> myWishlistIdPut(id)

Add a listing to your wishlist

Add a listing to your wishlist

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    MyApi apiInstance = new MyApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.myWishlistIdPut(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyApi#myWishlistIdPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

