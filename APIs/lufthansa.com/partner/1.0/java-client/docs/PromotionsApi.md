# PromotionsApi

All URIs are relative to *https://api.lufthansa.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**priceOffers**](PromotionsApi.md#priceOffers) | **GET** /promotions/priceoffers/flights/ond/{origin}/{destination} | Price Offers |


<a id="priceOffers"></a>
# **priceOffers**
> String priceOffers(origin, destination, departureDate, returnDate, service)

Price Offers

Retrieve a best price offer given an origin and destination.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromotionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lufthansa.com/v1");
    
    // Configure OAuth2 access token for authorization: auth
    OAuth auth = (OAuth) defaultClient.getAuthentication("auth");
    auth.setAccessToken("YOUR ACCESS TOKEN");

    PromotionsApi apiInstance = new PromotionsApi(defaultClient);
    String origin = "origin_example"; // String | Departure city. 3-letter IATA city code
    String destination = "destination_example"; // String | Destination city. 3-letter IATA city code
    String departureDate = "departureDate_example"; // String | Departure date in local time (YYYY-MM-DD)
    String returnDate = "returnDate_example"; // String | Return date in local time (YYYY-MM-DD)
    String service = "amadeusBestPrice"; // String | Optional parameter.
    try {
      String result = apiInstance.priceOffers(origin, destination, departureDate, returnDate, service);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromotionsApi#priceOffers");
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
| **origin** | **String**| Departure city. 3-letter IATA city code | |
| **destination** | **String**| Destination city. 3-letter IATA city code | |
| **departureDate** | **String**| Departure date in local time (YYYY-MM-DD) | |
| **returnDate** | **String**| Return date in local time (YYYY-MM-DD) | |
| **service** | **String**| Optional parameter. | [optional] [default to amadeusBestPrice] |

### Return type

**String**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

