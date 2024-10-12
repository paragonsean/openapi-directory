# EventItemApi

All URIs are relative to *https://api.ebay.com/buy/deal/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEventItems**](EventItemApi.md#getEventItems) | **GET** /event_item |  |


<a id="getEventItems"></a>
# **getEventItems**
> EventItemSearchResponse getEventItems(eventIds, X_EBAY_C_MARKETPLACE_ID, categoryIds, deliveryCountry, limit, offset)



This method returns a paginated set of event items. The result set contains all event items associated with the specified search criteria and marketplace ID. Request headers This method uses the X-EBAY-C-ENDUSERCTX request header to support revenue sharing for eBay Partner Networks and to improve the accuracy of shipping and delivery time estimations. For details see, Request headers in the Buying Integration Guide. Restrictions This method can return a maximum of 10,000 items. For a list of supported sites and other restrictions, see API Restrictions. eBay Partner Network: In order to receive a commission for your sales, you must use the URL returned in the itemAffiliateWebUrl field to forward your buyer to the ebay.com site.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventItemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/buy/deal/v1");
    
    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    EventItemApi apiInstance = new EventItemApi(defaultClient);
    String eventIds = "eventIds_example"; // String | The unique identifiers for the eBay events. Maximum Value: 1
    String X_EBAY_C_MARKETPLACE_ID = "X_EBAY_C_MARKETPLACE_ID_example"; // String | A header used to specify the eBay marketplace ID.
    String categoryIds = "categoryIds_example"; // String | The unique identifier of the eBay category for the search. Maximum Value: 1
    String deliveryCountry = "deliveryCountry_example"; // String | A filter for items that can be shipped to the specified country.
    String limit = "limit_example"; // String | The maximum number of items, from the current result set, returned on a single page. Default: 20
    String offset = "offset_example"; // String | The number of items that will be skipped in the result set. This is used with the limit field to control the pagination of the output. For example, if the offset is set to 0 and the limit is set to 10, the method will retrieve items 1 through 10 from the list of items returned. If the offset is set to 10 and the limit is set to 10, the method will retrieve items 11 through 20 from the list of items returned. Default: 0
    try {
      EventItemSearchResponse result = apiInstance.getEventItems(eventIds, X_EBAY_C_MARKETPLACE_ID, categoryIds, deliveryCountry, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventItemApi#getEventItems");
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
| **eventIds** | **String**| The unique identifiers for the eBay events. Maximum Value: 1 | |
| **X_EBAY_C_MARKETPLACE_ID** | **String**| A header used to specify the eBay marketplace ID. | |
| **categoryIds** | **String**| The unique identifier of the eBay category for the search. Maximum Value: 1 | [optional] |
| **deliveryCountry** | **String**| A filter for items that can be shipped to the specified country. | [optional] |
| **limit** | **String**| The maximum number of items, from the current result set, returned on a single page. Default: 20 | [optional] |
| **offset** | **String**| The number of items that will be skipped in the result set. This is used with the limit field to control the pagination of the output. For example, if the offset is set to 0 and the limit is set to 10, the method will retrieve items 1 through 10 from the list of items returned. If the offset is set to 10 and the limit is set to 10, the method will retrieve items 11 through 20 from the list of items returned. Default: 0 | [optional] |

### Return type

[**EventItemSearchResponse**](EventItemSearchResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

