# ShoppingApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**upsellAirOffers**](ShoppingApi.md#upsellAirOffers) | **POST** /shopping/flight-offers/upselling | Return a list of upsell Flight Offers based on given Flight Offers |


<a id="upsellAirOffers"></a>
# **upsellAirOffers**
> SuccessUpsell upsellAirOffers(xHTTPMethodOverride, upsellFlightOffersBody)

Return a list of upsell Flight Offers based on given Flight Offers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShoppingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    ShoppingApi apiInstance = new ShoppingApi(defaultClient);
    String xHTTPMethodOverride = "GET"; // String | the HTTP method to apply
    GetUpsellQuery upsellFlightOffersBody = new GetUpsellQuery(); // GetUpsellQuery | list of criteria to upsell a dedicated flight-offers
    try {
      SuccessUpsell result = apiInstance.upsellAirOffers(xHTTPMethodOverride, upsellFlightOffersBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShoppingApi#upsellAirOffers");
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
| **xHTTPMethodOverride** | **String**| the HTTP method to apply | [default to GET] |
| **upsellFlightOffersBody** | [**GetUpsellQuery**](GetUpsellQuery.md)| list of criteria to upsell a dedicated flight-offers | |

### Return type

[**SuccessUpsell**](SuccessUpsell.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.amadeus+json
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |
| **400** | code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 2668    | PARAMETER COMBINATION INVALID/RESTRICTED 2781    | INVALID LENGTH 4926    | INVALID DATA RECEIVED 32171   | MANDATORY DATA MISSING 39397   | UNABLE TO RETRIEVE UPSELL OFFER  |  -  |
| **0** | Unexpected error |  -  |

