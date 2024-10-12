# ListingsApi

All URIs are relative to *https://api.reverb.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listingsAllGet**](ListingsApi.md#listingsAllGet) | **GET** /listings/all | All listings including used, handmade, and brand new |
| [**listingsFacetsSellerLocationGet**](ListingsApi.md#listingsFacetsSellerLocationGet) | **GET** /listings/facets/seller_location | Individual facets |
| [**listingsGet**](ListingsApi.md#listingsGet) | **GET** /listings | Default search of listings includes only used &amp; handmade. Add a filter to view all listings or use the /listings/all endpoint. |
| [**listingsIdNegotiationGet**](ListingsApi.md#listingsIdNegotiationGet) | **GET** /listings/{id}/negotiation | Returns the latest negotiation for the requesting user given a listing id |
| [**listingsIdOfferPost**](ListingsApi.md#listingsIdOfferPost) | **POST** /listings/{id}/offer | Make an offer to the seller of a listing |
| [**listingsListingIdBumpBudgetTypePost**](ListingsApi.md#listingsListingIdBumpBudgetTypePost) | **POST** /listings/{listing_id}/bump/{budget_type} | Bump a listing |
| [**listingsListingIdBumpGet**](ListingsApi.md#listingsListingIdBumpGet) | **GET** /listings/{listing_id}/bump | View available bump tiers and stats for a listing |
| [**listingsListingIdConversationsPost**](ListingsApi.md#listingsListingIdConversationsPost) | **POST** /listings/{listing_id}/conversations | Start a conversation with a seller |
| [**listingsListingIdImagesGet**](ListingsApi.md#listingsListingIdImagesGet) | **GET** /listings/{listing_id}/images | View the images associated with a particular listing |
| [**listingsListingIdImagesImageIdDelete**](ListingsApi.md#listingsListingIdImagesImageIdDelete) | **DELETE** /listings/{listing_id}/images/{image_id} | Delete an image from a listing |
| [**listingsListingIdSalesGet**](ListingsApi.md#listingsListingIdSalesGet) | **GET** /listings/{listing_id}/sales | See all sales that include a listing. |
| [**listingsPost**](ListingsApi.md#listingsPost) | **POST** /listings | Create a listing |
| [**listingsSlugDelete**](ListingsApi.md#listingsSlugDelete) | **DELETE** /listings/{slug} | Delete a draft listing. Cannot be used on non-drafts. |
| [**listingsSlugEditGet**](ListingsApi.md#listingsSlugEditGet) | **GET** /listings/{slug}/edit | Edit listing. |
| [**listingsSlugFlagPost**](ListingsApi.md#listingsSlugFlagPost) | **POST** /listings/{slug}/flag | Flag a listing for inappropriate content or fraud |
| [**listingsSlugGet**](ListingsApi.md#listingsSlugGet) | **GET** /listings/{slug} | Listing details |
| [**listingsSlugPut**](ListingsApi.md#listingsSlugPut) | **PUT** /listings/{slug} | Update a listing |
| [**listingsSlugReviewsGet**](ListingsApi.md#listingsSlugReviewsGet) | **GET** /listings/{slug}/reviews | View reviews of a listing |
| [**listingsSlugReviewsPost**](ListingsApi.md#listingsSlugReviewsPost) | **POST** /listings/{slug}/reviews | Create a review for a listing |
| [**listingsSlugSimilarListingsGet**](ListingsApi.md#listingsSlugSimilarListingsGet) | **GET** /listings/{slug}/similar_listings | Listing details |


<a id="listingsAllGet"></a>
# **listingsAllGet**
> listingsAllGet(query, auctionPriceMax, category, productType, conditions, decade, finish, handmade, itemCity, itemCountry, itemRegion, itemState, make, model, mustNot, priceMax, priceMin, currency, yearMax, yearMin, acceptsGiftCards, preferredSeller, shop, shopId, listingType, shipsTo, excludeAuctions, acceptsPaymentPlans, watchersCountMin, notIds, localPickup, page, perPage, offset)

All listings including used, handmade, and brand new

All listings including used, handmade, and brand new

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ListingsApi apiInstance = new ListingsApi(defaultClient);
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
    Integer page = 1; // Integer | 
    Integer perPage = 24; // Integer | 
    Integer offset = 56; // Integer | 
    try {
      apiInstance.listingsAllGet(query, auctionPriceMax, category, productType, conditions, decade, finish, handmade, itemCity, itemCountry, itemRegion, itemState, make, model, mustNot, priceMax, priceMin, currency, yearMax, yearMin, acceptsGiftCards, preferredSeller, shop, shopId, listingType, shipsTo, excludeAuctions, acceptsPaymentPlans, watchersCountMin, notIds, localPickup, page, perPage, offset);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingsApi#listingsAllGet");
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
| **page** | **Integer**|  | [optional] [default to 1] |
| **perPage** | **Integer**|  | [optional] [default to 24] |
| **offset** | **Integer**|  | [optional] |

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

<a id="listingsFacetsSellerLocationGet"></a>
# **listingsFacetsSellerLocationGet**
> listingsFacetsSellerLocationGet()

Individual facets

Individual facets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ListingsApi apiInstance = new ListingsApi(defaultClient);
    try {
      apiInstance.listingsFacetsSellerLocationGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingsApi#listingsFacetsSellerLocationGet");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="listingsGet"></a>
# **listingsGet**
> listingsGet(query, auctionPriceMax, category, productType, conditions, decade, finish, handmade, itemCity, itemCountry, itemRegion, itemState, make, model, mustNot, priceMax, priceMin, currency, yearMax, yearMin, acceptsGiftCards, preferredSeller, shop, shopId, listingType, shipsTo, excludeAuctions, acceptsPaymentPlans, watchersCountMin, notIds, localPickup, page, perPage, offset)

Default search of listings includes only used &amp; handmade. Add a filter to view all listings or use the /listings/all endpoint.

Default search of listings includes only used &amp; handmade. Add a filter to view all listings or use the /listings/all endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ListingsApi apiInstance = new ListingsApi(defaultClient);
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
    Integer page = 1; // Integer | 
    Integer perPage = 24; // Integer | 
    Integer offset = 56; // Integer | 
    try {
      apiInstance.listingsGet(query, auctionPriceMax, category, productType, conditions, decade, finish, handmade, itemCity, itemCountry, itemRegion, itemState, make, model, mustNot, priceMax, priceMin, currency, yearMax, yearMin, acceptsGiftCards, preferredSeller, shop, shopId, listingType, shipsTo, excludeAuctions, acceptsPaymentPlans, watchersCountMin, notIds, localPickup, page, perPage, offset);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingsApi#listingsGet");
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
| **page** | **Integer**|  | [optional] [default to 1] |
| **perPage** | **Integer**|  | [optional] [default to 24] |
| **offset** | **Integer**|  | [optional] |

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

<a id="listingsIdNegotiationGet"></a>
# **listingsIdNegotiationGet**
> listingsIdNegotiationGet(id)

Returns the latest negotiation for the requesting user given a listing id

Returns the latest negotiation for the requesting user given a listing id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ListingsApi apiInstance = new ListingsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.listingsIdNegotiationGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingsApi#listingsIdNegotiationGet");
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

<a id="listingsIdOfferPost"></a>
# **listingsIdOfferPost**
> listingsIdOfferPost(id, conversationsIdOfferPostRequest)

Make an offer to the seller of a listing

Make an offer to the seller of a listing

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ListingsApi apiInstance = new ListingsApi(defaultClient);
    String id = "id_example"; // String | 
    ConversationsIdOfferPostRequest conversationsIdOfferPostRequest = new ConversationsIdOfferPostRequest(); // ConversationsIdOfferPostRequest | the content of the request
    try {
      apiInstance.listingsIdOfferPost(id, conversationsIdOfferPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingsApi#listingsIdOfferPost");
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
| **conversationsIdOfferPostRequest** | [**ConversationsIdOfferPostRequest**](ConversationsIdOfferPostRequest.md)| the content of the request | [optional] |

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

<a id="listingsListingIdBumpBudgetTypePost"></a>
# **listingsListingIdBumpBudgetTypePost**
> listingsListingIdBumpBudgetTypePost(listingId, budgetType)

Bump a listing

Bump a listing

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ListingsApi apiInstance = new ListingsApi(defaultClient);
    String listingId = "listingId_example"; // String | 
    String budgetType = "budgetType_example"; // String | 
    try {
      apiInstance.listingsListingIdBumpBudgetTypePost(listingId, budgetType);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingsApi#listingsListingIdBumpBudgetTypePost");
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
| **listingId** | **String**|  | |
| **budgetType** | **String**|  | |

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

<a id="listingsListingIdBumpGet"></a>
# **listingsListingIdBumpGet**
> listingsListingIdBumpGet(listingId)

View available bump tiers and stats for a listing

View available bump tiers and stats for a listing

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ListingsApi apiInstance = new ListingsApi(defaultClient);
    String listingId = "listingId_example"; // String | 
    try {
      apiInstance.listingsListingIdBumpGet(listingId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingsApi#listingsListingIdBumpGet");
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
| **listingId** | **String**|  | |

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

<a id="listingsListingIdConversationsPost"></a>
# **listingsListingIdConversationsPost**
> listingsListingIdConversationsPost(listingId, listingsListingIdConversationsPostRequest)

Start a conversation with a seller

Start a conversation with a seller

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ListingsApi apiInstance = new ListingsApi(defaultClient);
    String listingId = "listingId_example"; // String | 
    ListingsListingIdConversationsPostRequest listingsListingIdConversationsPostRequest = new ListingsListingIdConversationsPostRequest(); // ListingsListingIdConversationsPostRequest | the content of the request
    try {
      apiInstance.listingsListingIdConversationsPost(listingId, listingsListingIdConversationsPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingsApi#listingsListingIdConversationsPost");
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
| **listingId** | **String**|  | |
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

<a id="listingsListingIdImagesGet"></a>
# **listingsListingIdImagesGet**
> listingsListingIdImagesGet(listingId)

View the images associated with a particular listing

View the images associated with a particular listing

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ListingsApi apiInstance = new ListingsApi(defaultClient);
    String listingId = "listingId_example"; // String | 
    try {
      apiInstance.listingsListingIdImagesGet(listingId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingsApi#listingsListingIdImagesGet");
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
| **listingId** | **String**|  | |

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

<a id="listingsListingIdImagesImageIdDelete"></a>
# **listingsListingIdImagesImageIdDelete**
> listingsListingIdImagesImageIdDelete(listingId, imageId)

Delete an image from a listing

Delete an image from a listing

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ListingsApi apiInstance = new ListingsApi(defaultClient);
    String listingId = "listingId_example"; // String | 
    String imageId = "imageId_example"; // String | 
    try {
      apiInstance.listingsListingIdImagesImageIdDelete(listingId, imageId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingsApi#listingsListingIdImagesImageIdDelete");
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
| **listingId** | **String**|  | |
| **imageId** | **String**|  | |

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

<a id="listingsListingIdSalesGet"></a>
# **listingsListingIdSalesGet**
> listingsListingIdSalesGet(listingId)

See all sales that include a listing.

See all sales that include a listing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ListingsApi apiInstance = new ListingsApi(defaultClient);
    String listingId = "listingId_example"; // String | 
    try {
      apiInstance.listingsListingIdSalesGet(listingId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingsApi#listingsListingIdSalesGet");
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
| **listingId** | **String**|  | |

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

<a id="listingsPost"></a>
# **listingsPost**
> listingsPost(listingsPostRequest)

Create a listing

Create a listing

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ListingsApi apiInstance = new ListingsApi(defaultClient);
    ListingsPostRequest listingsPostRequest = new ListingsPostRequest(); // ListingsPostRequest | the content of the request
    try {
      apiInstance.listingsPost(listingsPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingsApi#listingsPost");
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
| **listingsPostRequest** | [**ListingsPostRequest**](ListingsPostRequest.md)| the content of the request | [optional] |

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

<a id="listingsSlugDelete"></a>
# **listingsSlugDelete**
> listingsSlugDelete(slug)

Delete a draft listing. Cannot be used on non-drafts.

Delete a draft listing. Cannot be used on non-drafts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ListingsApi apiInstance = new ListingsApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.listingsSlugDelete(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingsApi#listingsSlugDelete");
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

<a id="listingsSlugEditGet"></a>
# **listingsSlugEditGet**
> listingsSlugEditGet(slug)

Edit listing.

Edit listing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ListingsApi apiInstance = new ListingsApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.listingsSlugEditGet(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingsApi#listingsSlugEditGet");
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

<a id="listingsSlugFlagPost"></a>
# **listingsSlugFlagPost**
> listingsSlugFlagPost(slug, listingsSlugFlagPostRequest)

Flag a listing for inappropriate content or fraud

Flag a listing for inappropriate content or fraud

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ListingsApi apiInstance = new ListingsApi(defaultClient);
    String slug = "slug_example"; // String | 
    ListingsSlugFlagPostRequest listingsSlugFlagPostRequest = new ListingsSlugFlagPostRequest(); // ListingsSlugFlagPostRequest | the content of the request
    try {
      apiInstance.listingsSlugFlagPost(slug, listingsSlugFlagPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingsApi#listingsSlugFlagPost");
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
| **listingsSlugFlagPostRequest** | [**ListingsSlugFlagPostRequest**](ListingsSlugFlagPostRequest.md)| the content of the request | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="listingsSlugGet"></a>
# **listingsSlugGet**
> listingsSlugGet(slug)

Listing details

Listing details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ListingsApi apiInstance = new ListingsApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.listingsSlugGet(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingsApi#listingsSlugGet");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="listingsSlugPut"></a>
# **listingsSlugPut**
> listingsSlugPut(slug, listingsPostRequest)

Update a listing

Update a listing

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ListingsApi apiInstance = new ListingsApi(defaultClient);
    String slug = "slug_example"; // String | 
    ListingsPostRequest listingsPostRequest = new ListingsPostRequest(); // ListingsPostRequest | the content of the request
    try {
      apiInstance.listingsSlugPut(slug, listingsPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingsApi#listingsSlugPut");
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
| **listingsPostRequest** | [**ListingsPostRequest**](ListingsPostRequest.md)| the content of the request | [optional] |

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

<a id="listingsSlugReviewsGet"></a>
# **listingsSlugReviewsGet**
> listingsSlugReviewsGet(slug)

View reviews of a listing

View reviews of a listing

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ListingsApi apiInstance = new ListingsApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.listingsSlugReviewsGet(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingsApi#listingsSlugReviewsGet");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="listingsSlugReviewsPost"></a>
# **listingsSlugReviewsPost**
> listingsSlugReviewsPost(slug)

Create a review for a listing

Create a review for a listing

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ListingsApi apiInstance = new ListingsApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.listingsSlugReviewsPost(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingsApi#listingsSlugReviewsPost");
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

<a id="listingsSlugSimilarListingsGet"></a>
# **listingsSlugSimilarListingsGet**
> listingsSlugSimilarListingsGet(slug)

Listing details

Listing details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ListingsApi apiInstance = new ListingsApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.listingsSlugSimilarListingsGet(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingsApi#listingsSlugSimilarListingsGet");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

