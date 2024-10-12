# NegotiableQuotePricesUpdatedApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**negotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPost**](NegotiableQuotePricesUpdatedApi.md#negotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPost) | **POST** /V1/negotiableQuote/pricesUpdated | negotiableQuote/pricesUpdated |


<a id="negotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPost"></a>
# **negotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPost**
> Boolean negotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPost(negotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPostRequest)

negotiableQuote/pricesUpdated

Refreshes item prices, taxes, discounts, cart rules in the negotiable quote as per the latest changes in the catalog / shared catalog and in the price rules. Depending on the negotiable quote state and totals, all or just some of quote numbers will be recalculated. &#39;Update Prices&#39; parameter forces refresh on any quote that is not locked for admin user, including the quotes with a negotiated price. The request can be applied to one or more quotes at the same time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegotiableQuotePricesUpdatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    NegotiableQuotePricesUpdatedApi apiInstance = new NegotiableQuotePricesUpdatedApi(defaultClient);
    NegotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPostRequest negotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPostRequest = new NegotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPostRequest(); // NegotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPostRequest | 
    try {
      Boolean result = apiInstance.negotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPost(negotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegotiableQuotePricesUpdatedApi#negotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPost");
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
| **negotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPostRequest** | [**NegotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPostRequest**](NegotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPostRequest.md)|  | [optional] |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

