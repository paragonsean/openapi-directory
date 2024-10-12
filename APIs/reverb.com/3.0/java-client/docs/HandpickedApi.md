# HandpickedApi

All URIs are relative to *https://api.reverb.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**handpickedSlugGet**](HandpickedApi.md#handpickedSlugGet) | **GET** /handpicked/{slug} | Get results from a handpicked collection |


<a id="handpickedSlugGet"></a>
# **handpickedSlugGet**
> handpickedSlugGet(slug, query, auctionPriceMax, category, productType, conditions, decade, finish, handmade, itemCity, itemCountry, itemRegion, itemState, make, model, mustNot, priceMax, priceMin, currency, yearMax, yearMin, acceptsGiftCards, preferredSeller, shop, shopId, listingType, shipsTo, excludeAuctions, acceptsPaymentPlans, watchersCountMin, notIds, localPickup, page, perPage, offset)

Get results from a handpicked collection

Get results from a handpicked collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HandpickedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    HandpickedApi apiInstance = new HandpickedApi(defaultClient);
    String slug = "slug_example"; // String | 
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
      apiInstance.handpickedSlugGet(slug, query, auctionPriceMax, category, productType, conditions, decade, finish, handmade, itemCity, itemCountry, itemRegion, itemState, make, model, mustNot, priceMax, priceMin, currency, yearMax, yearMin, acceptsGiftCards, preferredSeller, shop, shopId, listingType, shipsTo, excludeAuctions, acceptsPaymentPlans, watchersCountMin, notIds, localPickup, page, perPage, offset);
    } catch (ApiException e) {
      System.err.println("Exception when calling HandpickedApi#handpickedSlugGet");
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

