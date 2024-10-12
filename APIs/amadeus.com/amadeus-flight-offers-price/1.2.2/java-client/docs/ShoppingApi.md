# ShoppingApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteAirOffers**](ShoppingApi.md#quoteAirOffers) | **POST** /shopping/flight-offers/pricing | Confirm pricing of given flightOffers. |


<a id="quoteAirOffers"></a>
# **quoteAirOffers**
> SuccessPricing quoteAirOffers(xHTTPMethodOverride, priceFlightOffersBody, include, forceClass)

Confirm pricing of given flightOffers.

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
    GetPriceQuery priceFlightOffersBody = new GetPriceQuery(); // GetPriceQuery | list of criteria to confirm the price of a dedicated flight-offers
    List<String> include = Arrays.asList(); // List<String> | Sub-resources to be included:  * **credit-card-fees** to get the credit card fee applied on the booking  * **bags** to get extra bag options  * **other-services** to get services options  * **detailed-fare-rules** to get detailed fare rules options 
    Boolean forceClass = false; // Boolean | parameter to force the usage of booking class for pricing - **true**, to for pricing with the specified booking class - **false**, to get the best available price 
    try {
      SuccessPricing result = apiInstance.quoteAirOffers(xHTTPMethodOverride, priceFlightOffersBody, include, forceClass);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShoppingApi#quoteAirOffers");
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
| **priceFlightOffersBody** | [**GetPriceQuery**](GetPriceQuery.md)| list of criteria to confirm the price of a dedicated flight-offers | |
| **include** | [**List&lt;String&gt;**](String.md)| Sub-resources to be included:  * **credit-card-fees** to get the credit card fee applied on the booking  * **bags** to get extra bag options  * **other-services** to get services options  * **detailed-fare-rules** to get detailed fare rules options  | [optional] [enum: credit-card-fees, bags, other-services, detailed-fare-rules] |
| **forceClass** | **Boolean**| parameter to force the usage of booking class for pricing - **true**, to for pricing with the specified booking class - **false**, to get the best available price  | [optional] [default to false] |

### Return type

[**SuccessPricing**](SuccessPricing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.amadeus+json
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |
| **400** | code    | title                                  ------- | -------------------------------------  477     | INVALID FORMAT 2668    | PARAMETER COMBINATION INVALID/RESTRICTED 2781    | INVALID LENGTH 4926    | INVALID DATA RECEIVED 32171   | MANDATORY DATA MISSING  |  -  |
| **0** | Unexpected error |  -  |

