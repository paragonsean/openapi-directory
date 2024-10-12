# ShoppingApi

All URIs are relative to *https://test.api.amadeus.com/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMultiHotelOffers**](ShoppingApi.md#getMultiHotelOffers) | **GET** /shopping/hotel-offers | getMultiHotelOffers |
| [**getOfferPricing**](ShoppingApi.md#getOfferPricing) | **GET** /shopping/hotel-offers/{offerId} | getOfferPricing |


<a id="getMultiHotelOffers"></a>
# **getMultiHotelOffers**
> MultiResponse getMultiHotelOffers(hotelIds, adults, checkInDate, checkOutDate, countryOfResidence, roomQuantity, priceRange, currency, paymentPolicy, boardType, includeClosed, bestRateOnly, lang)

getMultiHotelOffers

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
    defaultClient.setBasePath("https://test.api.amadeus.com/v3");

    ShoppingApi apiInstance = new ShoppingApi(defaultClient);
    List<String> hotelIds = Arrays.asList(); // List<String> | Amadeus property codes on 8 chars. Mandatory parameter for a search by predefined list of hotels.
    Integer adults = 1; // Integer | Number of adult guests (1-9) per room.
    LocalDate checkInDate = LocalDate.parse("2023-11-22"); // LocalDate | Check-in date of the stay (hotel local date). Format YYYY-MM-DD. The lowest accepted value is the present date (no dates in the past). If not present, the default value will be today's date in the GMT time zone.
    LocalDate checkOutDate = LocalDate.now(); // LocalDate | Check-out date of the stay (hotel local date). Format YYYY-MM-DD. The lowest accepted value is checkInDate+1. If not present, it will default to checkInDate +1.
    String countryOfResidence = "countryOfResidence_example"; // String | Code of the country of residence of the traveler expressed using ISO 3166-1 format.
    Integer roomQuantity = 1; // Integer | Number of rooms requested (1-9).
    String priceRange = "priceRange_example"; // String | Filter hotel offers by price per night interval (ex: 200-300 or -300 or 100). It is mandatory to include a currency when this field is set.
    String currency = "currency_example"; // String | Use this parameter to request a specific currency. ISO currency code (http://www.iso.org/iso/home/standards/currency_codes.htm). If a hotel does not support the requested currency, the prices for the hotel will be returned in the local currency of the hotel.
    String paymentPolicy = "GUARANTEE"; // String | Filter the response based on a specific payment type. NONE means all types (default).
    String boardType = "ROOM_ONLY"; // String | Filter response based on available meals:         * ROOM_ONLY = Room Only         * BREAKFAST = Breakfast         * HALF_BOARD = Diner & Breakfast (only for Aggregators)         * FULL_BOARD = Full Board (only for Aggregators)         * ALL_INCLUSIVE = All Inclusive (only for Aggregators)
    Boolean includeClosed = true; // Boolean | Show all properties (include sold out) or available only. For sold out properties, please check availability on other dates.
    Boolean bestRateOnly = true; // Boolean | Used to return only the cheapest offer per hotel or all available offers.
    String lang = "lang_example"; // String | Requested language of descriptive texts.  Examples: FR , fr , fr-FR. If a language is not available the text will be returned in english. ISO language code (https://www.iso.org/iso-639-language-codes.html).
    try {
      MultiResponse result = apiInstance.getMultiHotelOffers(hotelIds, adults, checkInDate, checkOutDate, countryOfResidence, roomQuantity, priceRange, currency, paymentPolicy, boardType, includeClosed, bestRateOnly, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShoppingApi#getMultiHotelOffers");
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
| **hotelIds** | [**List&lt;String&gt;**](String.md)| Amadeus property codes on 8 chars. Mandatory parameter for a search by predefined list of hotels. | |
| **adults** | **Integer**| Number of adult guests (1-9) per room. | [optional] [default to 1] |
| **checkInDate** | **LocalDate**| Check-in date of the stay (hotel local date). Format YYYY-MM-DD. The lowest accepted value is the present date (no dates in the past). If not present, the default value will be today&#39;s date in the GMT time zone. | [optional] |
| **checkOutDate** | **LocalDate**| Check-out date of the stay (hotel local date). Format YYYY-MM-DD. The lowest accepted value is checkInDate+1. If not present, it will default to checkInDate +1. | [optional] |
| **countryOfResidence** | **String**| Code of the country of residence of the traveler expressed using ISO 3166-1 format. | [optional] |
| **roomQuantity** | **Integer**| Number of rooms requested (1-9). | [optional] [default to 1] |
| **priceRange** | **String**| Filter hotel offers by price per night interval (ex: 200-300 or -300 or 100). It is mandatory to include a currency when this field is set. | [optional] |
| **currency** | **String**| Use this parameter to request a specific currency. ISO currency code (http://www.iso.org/iso/home/standards/currency_codes.htm). If a hotel does not support the requested currency, the prices for the hotel will be returned in the local currency of the hotel. | [optional] |
| **paymentPolicy** | **String**| Filter the response based on a specific payment type. NONE means all types (default). | [optional] [default to NONE] [enum: GUARANTEE, DEPOSIT, NONE] |
| **boardType** | **String**| Filter response based on available meals:         * ROOM_ONLY &#x3D; Room Only         * BREAKFAST &#x3D; Breakfast         * HALF_BOARD &#x3D; Diner &amp; Breakfast (only for Aggregators)         * FULL_BOARD &#x3D; Full Board (only for Aggregators)         * ALL_INCLUSIVE &#x3D; All Inclusive (only for Aggregators) | [optional] [enum: ROOM_ONLY, BREAKFAST, HALF_BOARD, FULL_BOARD, ALL_INCLUSIVE] |
| **includeClosed** | **Boolean**| Show all properties (include sold out) or available only. For sold out properties, please check availability on other dates. | [optional] |
| **bestRateOnly** | **Boolean**| Used to return only the cheapest offer per hotel or all available offers. | [optional] [default to true] |
| **lang** | **String**| Requested language of descriptive texts.  Examples: FR , fr , fr-FR. If a language is not available the text will be returned in english. ISO language code (https://www.iso.org/iso-639-language-codes.html). | [optional] |

### Return type

[**MultiResponse**](MultiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad request:  | Code | Title  | |-----|-----| | 23   | PASSENGER TYPE NOT SUPPORTED   | | 61 | INVALID CURRENCY CODE| | 137 | INVALID ADULTS OCCUPANCY REQUESTED| | 145 | DURATION PERIOD OR DATES INCORRECT| | 195 | SERVICE RESTRICTION| | 249 | INVALID RATE CODE| | 377 | MAX STAY DURATION IS EXCEEDED| | 381 | INVALID CHECK-IN DATE| | 382 | INVALID CHECK-OUT DATE| | 383 | INVALID CITY CODE| | 392 | INVALID HOTEL CODE| | 397 | INVALID NUMBER OF ADULTS| | 400 | INVALID PROPERTY CODE| | 404 | CHECK_OUT DATE MUST BE FURTHER IN THE FUTURE THAN CHECK-IN DATE| | 424 | NO HOTELS FOUND WHICH MATCH THIS INPUT| | 431 | CHECK-OUT DATE IS TOO FAR IN THE FUTURE THAN CHECK-IN DATE| | 424 | NO HOTELS FOUND WHICH MATCH THIS INPUT| | 431 | CHECK-OUT DATE IS TOO FAR IN THE FUTURE| | 450 | INVALID PROVIDER RESPONSE| | 451 | INVALID CREDENTIALS| | 562 | RESTRICTED ACCESS FOR THE REQUESTED RATES AND CHAINS| | 784 | PROVIDER TIME OUT| | 790 | RATE SECURITY NOT LOADED|  |  -  |
| **500** | Internal server error. |  -  |

<a id="getOfferPricing"></a>
# **getOfferPricing**
> PricingResponse getOfferPricing(offerId, lang)

getOfferPricing

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
    defaultClient.setBasePath("https://test.api.amadeus.com/v3");

    ShoppingApi apiInstance = new ShoppingApi(defaultClient);
    String offerId = "TSXOJ6LFQ2"; // String | Unique identifier of an offer. Either the GDS booking code or the aggregator offerId with a limited lifetime.
    String lang = "lang_example"; // String | Requested language of descriptive texts.  Examples: FR , fr , fr-FR. If a language is not available the text will be returned in english. ISO language code (https://www.iso.org/iso-639-language-codes.html).
    try {
      PricingResponse result = apiInstance.getOfferPricing(offerId, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShoppingApi#getOfferPricing");
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
| **offerId** | **String**| Unique identifier of an offer. Either the GDS booking code or the aggregator offerId with a limited lifetime. | |
| **lang** | **String**| Requested language of descriptive texts.  Examples: FR , fr , fr-FR. If a language is not available the text will be returned in english. ISO language code (https://www.iso.org/iso-639-language-codes.html). | [optional] |

### Return type

[**PricingResponse**](PricingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request: code| title ------- | ------------------------------------- 23 | PASSENGER TYPE NOT SUPPORTED 61 |INVALID CURRENCY CODE 137 | INVALID ADULTS OCCUPANCY REQUESTED 145 | DURATION PERIOD OR DATES INCORRECT 195 | SERVICE RESTRICTION 249 | INVALID RATE CODE 377 | MAX STAY DURATION IS EXCEEDED 381 | INVALID CHECK-IN DATE 382 | INVALID CHECK-OUT DATE 383 | INVALID CITY CODE 392 | INVALID HOTEL CODE 397 | INVALID NUMBER OF ADULTS 400 | INVALID PROPERTY CODE 402 | INVALID ROOM TYPE 404 | CHECK_OUT DATE MUST BE FURTHER IN THE FUTURE THAN CHECK-IN DATE 424 | NO HOTELS FOUND WHICH MATCH THIS INPUT 431 | CHECK-OUT DATE IS TOO FAR IN THE FUTURE 450 | INVALID PROVIDER RESPONSE 451 | INVALID CREDENTIAL 562 | RESTRICTED ACCESS FOR THE REQUESTED RATES AND CHAINS 784 | PROVIDER TIME OUT 790 | NO PROPERTIES FOUND WITHIN THIS RADIUS 795 | NO SIMILAR NAME FOUND, PLEASE ENLARGE YOUR SEARCH CRITERIA 842 | RATE SECURITY NOT LOADED |  -  |
| **404** | Hotel or offer not found |  -  |
| **500** | Internal server error. |  -  |

