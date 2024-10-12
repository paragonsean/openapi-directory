# BookingServicesApi

All URIs are relative to *https://viatorapi.viator.com/service*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bookingAvailability**](BookingServicesApi.md#bookingAvailability) | **POST** /booking/availability | /booking/availability |
| [**bookingAvailabilityDates**](BookingServicesApi.md#bookingAvailabilityDates) | **GET** /booking/availability/dates | /booking/availability/dates |
| [**bookingAvailabilityTourgrades**](BookingServicesApi.md#bookingAvailabilityTourgrades) | **POST** /booking/availability/tourgrades | /booking/availability/tourgrades |
| [**bookingAvailabilityTourgradesPricingmatrix**](BookingServicesApi.md#bookingAvailabilityTourgradesPricingmatrix) | **POST** /booking/availability/tourgrades/pricingmatrix | /booking/availability/tourgrades/pricingmatrix |
| [**bookingBook**](BookingServicesApi.md#bookingBook) | **POST** /booking/book | /booking/book |
| [**bookingCalculateprice**](BookingServicesApi.md#bookingCalculateprice) | **POST** /booking/calculateprice | /booking/calculateprice |
| [**bookingHotels**](BookingServicesApi.md#bookingHotels) | **GET** /booking/hotels | /booking/hotels |
| [**bookingMybookings**](BookingServicesApi.md#bookingMybookings) | **GET** /booking/mybookings | /booking/mybookings |
| [**bookingPastbooking**](BookingServicesApi.md#bookingPastbooking) | **GET** /booking/pastbooking | /booking/pastbooking |
| [**bookingPricingmatrix**](BookingServicesApi.md#bookingPricingmatrix) | **POST** /booking/pricingmatrix | /booking/pricingmatrix |
| [**bookingStatus**](BookingServicesApi.md#bookingStatus) | **POST** /booking/status | /booking/status |
| [**bookingStatusItems**](BookingServicesApi.md#bookingStatusItems) | **POST** /booking/status/items | /booking/status/items |
| [**bookingVoucher**](BookingServicesApi.md#bookingVoucher) | **GET** /booking/voucher | /booking/voucher |
| [**cancelBooking**](BookingServicesApi.md#cancelBooking) | **POST** /bookings/{booking-reference}/cancel | /bookings/{booking-reference}/cancel |
| [**cancelBookingQuote**](BookingServicesApi.md#cancelBookingQuote) | **GET** /bookings/{booking-reference}/cancel-quote | /bookings/{booking-reference}/cancel-quote |
| [**cancellationReasons**](BookingServicesApi.md#cancellationReasons) | **GET** /bookings/cancel-reasons | /bookings/cancel-reasons |


<a id="bookingAvailability"></a>
# **bookingAvailability**
> BookingAvailability200Response bookingAvailability(acceptLanguage, bookingAvailabilityRequest)

/booking/availability

Get the tour-grade with the lowest price that is available for a product on each day of the specified month  This service: - returns  - useful when displaying a calendar of available tours - For more information, see: [Availability services](#section/Key-concepts/Availability-services) - **Notes:**    - [/booking/availability/dates](#operation/bookingAvailabilityDates) provides all availability in one call and is more suitable for calendars, etc.    - Availability data is limited to a period of **12 months** into the future from the present time on the production server and **6 months** on the sandbox server.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    BookingServicesApi apiInstance = new BookingServicesApi(defaultClient);
    String acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    BookingAvailabilityRequest bookingAvailabilityRequest = new BookingAvailabilityRequest(); // BookingAvailabilityRequest | 
    try {
      BookingAvailability200Response result = apiInstance.bookingAvailability(acceptLanguage, bookingAvailabilityRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingServicesApi#bookingAvailability");
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
| **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | |
| **bookingAvailabilityRequest** | [**BookingAvailabilityRequest**](BookingAvailabilityRequest.md)|  | [optional] |

### Return type

[**BookingAvailability200Response**](BookingAvailability200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="bookingAvailabilityDates"></a>
# **bookingAvailabilityDates**
> BookingAvailabilityDates200Response bookingAvailabilityDates(acceptLanguage, productCode)

/booking/availability/dates

Get dates on which a product is available  This service: - retrieves all available dates for a product, excluding days it does not operate and blocked-out dates - returns a multi-dimensional array of year-month -&amp;gt; days that have any availabile tour grade or traveler mix - useful to present the user with a list of dates for selection on which *this* product is available for booking - **Notes**:     - The user&#39;s desired traveler mix may not be eligible for booking; these details can be displayed when you retrieve its list of tour grades   - Availability data is limited to a period of **12 months** into the future from the present time on the production server and **6 months** on the sandbox server.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    BookingServicesApi apiInstance = new BookingServicesApi(defaultClient);
    String acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    String productCode = "2280AAHT"; // String | **unique alphanumeric identifier** of the product
    try {
      BookingAvailabilityDates200Response result = apiInstance.bookingAvailabilityDates(acceptLanguage, productCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingServicesApi#bookingAvailabilityDates");
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
| **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | |
| **productCode** | **String**| **unique alphanumeric identifier** of the product | [optional] |

### Return type

[**BookingAvailabilityDates200Response**](BookingAvailabilityDates200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="bookingAvailabilityTourgrades"></a>
# **bookingAvailabilityTourgrades**
> BookingAvailabilityTourgrades200Response bookingAvailabilityTourgrades(acceptLanguage, bookingAvailabilityTourgradesRequest)

/booking/availability/tourgrades

Get the tour grades of a product that are currently available  This service reports: - all tour grades for the specified product, on the specified day, that are available for the specified age bands - the pricing breakdown and the total depending on the travel date and traveler mix  **Note**: Availability data is limited to a period of **12 months** into the future from the present time on the production server and **6 months** on the sandbox server.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    BookingServicesApi apiInstance = new BookingServicesApi(defaultClient);
    String acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    BookingAvailabilityTourgradesRequest bookingAvailabilityTourgradesRequest = new BookingAvailabilityTourgradesRequest(); // BookingAvailabilityTourgradesRequest | 
    try {
      BookingAvailabilityTourgrades200Response result = apiInstance.bookingAvailabilityTourgrades(acceptLanguage, bookingAvailabilityTourgradesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingServicesApi#bookingAvailabilityTourgrades");
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
| **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | |
| **bookingAvailabilityTourgradesRequest** | [**BookingAvailabilityTourgradesRequest**](BookingAvailabilityTourgradesRequest.md)|  | [optional] |

### Return type

[**BookingAvailabilityTourgrades200Response**](BookingAvailabilityTourgrades200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="bookingAvailabilityTourgradesPricingmatrix"></a>
# **bookingAvailabilityTourgradesPricingmatrix**
> BookingAvailabilityTourgradesPricingmatrix200Response bookingAvailabilityTourgradesPricingmatrix(acceptLanguage, bookingAvailabilityTourgradesPricingmatrixRequest)

/booking/availability/tourgrades/pricingmatrix

Get a pricing matrix that includes availability and tour-grades for a product  Given a month, this service returns days with available tour grades only (i.e., days which have at least one tourgrade available), and the pricing matrix for that tour grade for that day.  - **Note**: Availability data is limited to a period of **12 months** into the future from the present time on the production server and **6 months** on the sandbox server.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    BookingServicesApi apiInstance = new BookingServicesApi(defaultClient);
    String acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    BookingAvailabilityTourgradesPricingmatrixRequest bookingAvailabilityTourgradesPricingmatrixRequest = new BookingAvailabilityTourgradesPricingmatrixRequest(); // BookingAvailabilityTourgradesPricingmatrixRequest | 
    try {
      BookingAvailabilityTourgradesPricingmatrix200Response result = apiInstance.bookingAvailabilityTourgradesPricingmatrix(acceptLanguage, bookingAvailabilityTourgradesPricingmatrixRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingServicesApi#bookingAvailabilityTourgradesPricingmatrix");
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
| **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | |
| **bookingAvailabilityTourgradesPricingmatrixRequest** | [**BookingAvailabilityTourgradesPricingmatrixRequest**](BookingAvailabilityTourgradesPricingmatrixRequest.md)|  | [optional] |

### Return type

[**BookingAvailabilityTourgradesPricingmatrix200Response**](BookingAvailabilityTourgradesPricingmatrix200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="bookingBook"></a>
# **bookingBook**
> BookingBook200Response bookingBook(acceptLanguage, bookingBookRequest)

/booking/book

Make a booking  For more information, see:     - [Cancellation policy](#section/Key-concepts/Cancellation-policy)   - [Booking concepts](#section/Key-concepts/Booking-concepts)   - [Booking process flow](#section/Common-workflows-and-data-validation/Booking-process-flow)   - [Making a booking](#section/Common-workflows-and-data-validation/Making-a-booking)   - [Supplier communications](#section/Key-concepts/Supplier-communications) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    BookingServicesApi apiInstance = new BookingServicesApi(defaultClient);
    String acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    BookingBookRequest bookingBookRequest = new BookingBookRequest(); // BookingBookRequest | 
    try {
      BookingBook200Response result = apiInstance.bookingBook(acceptLanguage, bookingBookRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingServicesApi#bookingBook");
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
| **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | |
| **bookingBookRequest** | [**BookingBookRequest**](BookingBookRequest.md)|  | [optional] |

### Return type

[**BookingBook200Response**](BookingBook200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="bookingCalculateprice"></a>
# **bookingCalculateprice**
> BookingCalculateprice200Response bookingCalculateprice(acceptLanguage, bookingCalculatepriceRequest)

/booking/calculateprice

Confirm the price of a tour / activity prior to booking  For more information, see: [Calculating prices](#section/Common-workflows-and-data-validation/Calculating-prices)    - **Note**: Availability and pricing data is limited to a period of **six months** into the future from the present time 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    BookingServicesApi apiInstance = new BookingServicesApi(defaultClient);
    String acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    BookingCalculatepriceRequest bookingCalculatepriceRequest = new BookingCalculatepriceRequest(); // BookingCalculatepriceRequest | 
    try {
      BookingCalculateprice200Response result = apiInstance.bookingCalculateprice(acceptLanguage, bookingCalculatepriceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingServicesApi#bookingCalculateprice");
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
| **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | |
| **bookingCalculatepriceRequest** | [**BookingCalculatepriceRequest**](BookingCalculatepriceRequest.md)|  | [optional] |

### Return type

[**BookingCalculateprice200Response**](BookingCalculateprice200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="bookingHotels"></a>
# **bookingHotels**
> BookingHotels200Response bookingHotels(acceptLanguage, productCode, destId)

/booking/hotels

Get hotel pick-ups Lists the hotel pickups available for either a product or a destination 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    BookingServicesApi apiInstance = new BookingServicesApi(defaultClient);
    String acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    String productCode = "2280AAHT"; // String | **unique alphanumeric identifier** of the product
    Integer destId = 123; // Integer | **unique numeric identifier** of the destination
    try {
      BookingHotels200Response result = apiInstance.bookingHotels(acceptLanguage, productCode, destId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingServicesApi#bookingHotels");
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
| **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | |
| **productCode** | **String**| **unique alphanumeric identifier** of the product | [optional] |
| **destId** | **Integer**| **unique numeric identifier** of the destination | [optional] |

### Return type

[**BookingHotels200Response**](BookingHotels200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="bookingMybookings"></a>
# **bookingMybookings**
> BookingMybookings200Response bookingMybookings(acceptLanguage, voucherKey, email, itineraryOrItemId)

/booking/mybookings

Get a user&#39;s bookings with travel dates in the future.   This service can also be used to check the status of a booking.   **Provide either:**  - A &#x60;voucherKey&#x60;, **or...**  - An email address (&#x60;email&#x60;) and a booking reference (&#x60;itineraryOrItemId&#x60;) ([Booking Reference](#section/Key-concepts/Booking-references)) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    BookingServicesApi apiInstance = new BookingServicesApi(defaultClient);
    String acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    String voucherKey = "3299307:93c7f36a56b18ba1068787ba7fb7988da5c8ad08db77604110141ff21498603e:600033670"; // String | **voucher key** for the booking
    String email = "apitest@viator.com"; // String | **email address** of the booker for the booking
    String itineraryOrItemId = "700179574"; // String | The booking reference number of the item - **Note**: For more information, see [Booking references](#section/Key-concepts/Booking-references) 
    try {
      BookingMybookings200Response result = apiInstance.bookingMybookings(acceptLanguage, voucherKey, email, itineraryOrItemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingServicesApi#bookingMybookings");
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
| **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | |
| **voucherKey** | **String**| **voucher key** for the booking | [optional] |
| **email** | **String**| **email address** of the booker for the booking | [optional] |
| **itineraryOrItemId** | **String**| The booking reference number of the item - **Note**: For more information, see [Booking references](#section/Key-concepts/Booking-references)  | [optional] |

### Return type

[**BookingMybookings200Response**](BookingMybookings200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="bookingPastbooking"></a>
# **bookingPastbooking**
> BookingPastbooking200Response bookingPastbooking(acceptLanguage, voucherKey, email, itemId)

/booking/pastbooking

Get the details of a single specific past booking based on the &#x60;voucherKey&#x60; or &#x60;itemId&#x60; and email address sent in the request.  **Note**: this service will only return past bookings that were made with the same API key that was used to make the booking  **Sample query parameters**: - email&#x3D;apitest@viator.com&amp;amp;itemId&#x3D;580669678  **or** - voucherKey&#x3D;1005851866:4af44c13ecf3f1a7d3f9ef2fc00c2257e08fa42ae20f877f3039ff9b52aba24e:580669678  **email** - The email address passed must match the email address associated with the booking  **Departure details**  - Departure details such as the &#x60;departurePoint&#x60;, &#x60;departurePointAddress&#x60; and &#x60;departurePointDirections&#x60; is included in the response.  - These fields may contain HTML escape characters such as &amp;amp;amp; and special characters that are escaped by a backslash. Ensure that these fields are parsed after receiving the response as it will cause your JSON to be invalid.  For more information, see: [Reviewing bookings](#section/Common-workflows-and-data-validation/Reviewing-bookings) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    BookingServicesApi apiInstance = new BookingServicesApi(defaultClient);
    String acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    String voucherKey = "1005851866:4af44c13ecf3f1a7d3f9ef2fc00c2257e08fa42ae20f877f3039ff9b52aba24e:580669678"; // String | **specifier** of past booking type (use *one* of: `itemId` (booking reference) *and* `'voucherKey'` *or* `'email'`)
    String email = "apitest@viator.com"; // String | **email address** by which to search for past bookings
    String itemId = "580669678"; // String | Search for a booking with this **unique booking-reference number**. See [Booking references](#section/Key-concepts/Booking-references) for more information. 
    try {
      BookingPastbooking200Response result = apiInstance.bookingPastbooking(acceptLanguage, voucherKey, email, itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingServicesApi#bookingPastbooking");
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
| **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | |
| **voucherKey** | **String**| **specifier** of past booking type (use *one* of: &#x60;itemId&#x60; (booking reference) *and* &#x60;&#39;voucherKey&#39;&#x60; *or* &#x60;&#39;email&#39;&#x60;) | [optional] |
| **email** | **String**| **email address** by which to search for past bookings | [optional] |
| **itemId** | **String**| Search for a booking with this **unique booking-reference number**. See [Booking references](#section/Key-concepts/Booking-references) for more information.  | [optional] |

### Return type

[**BookingPastbooking200Response**](BookingPastbooking200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="bookingPricingmatrix"></a>
# **bookingPricingmatrix**
> BookingPricingmatrix200Response bookingPricingmatrix(acceptLanguage, bookingPricingmatrixRequest)

/booking/pricingmatrix

Get the pricing matrix for tour-grades, product age bands and pax mixes  For more information, see: [Get the tour-grade pricing matrix](#section/Common-workflows-and-data-validation/Get-the-tour-grade-pricing-matrix) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    BookingServicesApi apiInstance = new BookingServicesApi(defaultClient);
    String acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    BookingPricingmatrixRequest bookingPricingmatrixRequest = new BookingPricingmatrixRequest(); // BookingPricingmatrixRequest | 
    try {
      BookingPricingmatrix200Response result = apiInstance.bookingPricingmatrix(acceptLanguage, bookingPricingmatrixRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingServicesApi#bookingPricingmatrix");
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
| **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | |
| **bookingPricingmatrixRequest** | [**BookingPricingmatrixRequest**](BookingPricingmatrixRequest.md)|  | [optional] |

### Return type

[**BookingPricingmatrix200Response**](BookingPricingmatrix200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="bookingStatus"></a>
# **bookingStatus**
> BookingStatus200Response bookingStatus(acceptLanguage, bookingStatusRequest)

/booking/status

Get the booking status for multiple items based on different criteria  This service:  - is ideally be used in software for bulk updates of pending bookings - returns a maximum of 1000 bookings (narrow your search if you expect a greater number of results) - will return &amp;lt;u&amp;gt;both&amp;lt;/u&amp;gt; live &amp;lt;u&amp;gt;and&amp;lt;/u&amp;gt; test bookings - rate limited to &amp;lt;u&amp;gt;one request every 30 minutes&amp;lt;/u&amp;gt; - For more information, see: [Get the bookiing status for multiple items](#section/Common-workflows-and-data-validation/Get-the-booking-status-for-multiple-items)  **Exceeding the rate limit** - You will receive the following error message if you exceed the rate limit allowed for this service. Set &#x60;test&#x60; to &#x60;true&#x60; to bypass this limit: &#x60;&#x60;&#x60;javascript {     \&quot;data\&quot;: null     \&quot;vmid\&quot;: 221002     \&quot;errorMessage\&quot;: [\&quot;Access allowed every 30 minutes\&quot;]     \&quot;errorType\&quot;: \&quot;EXCEPTION\&quot;     \&quot;dateStamp\&quot;: \&quot;2013-03-26T10:28:51+0000\&quot;     \&quot;errorReference\&quot;: 55315512721712161381352771     \&quot;errorMessageText\&quot;: [\&quot;Access allowed every 30 minutes\&quot;]     \&quot;success\&quot;: false     \&quot;totalCount\&quot;: 1     \&quot;errorName\&quot;: \&quot;PollingDeniedException\&quot;   } &#x60;&#x60;&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    BookingServicesApi apiInstance = new BookingServicesApi(defaultClient);
    String acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    BookingStatusRequest bookingStatusRequest = new BookingStatusRequest(); // BookingStatusRequest | 
    try {
      BookingStatus200Response result = apiInstance.bookingStatus(acceptLanguage, bookingStatusRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingServicesApi#bookingStatus");
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
| **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | |
| **bookingStatusRequest** | [**BookingStatusRequest**](BookingStatusRequest.md)|  | [optional] |

### Return type

[**BookingStatus200Response**](BookingStatus200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="bookingStatusItems"></a>
# **bookingStatusItems**
> BookingStatusItems200Response bookingStatusItems(acceptLanguage, bookingStatusItemsRequest)

/booking/status/items

Get brief booking statuses  This service is similar to [/booking/status](#operation/bookingStatus) in that it: - retrieves the booking status for multiple items based on different criteria - has the same request parameters as [/booking/status](#operation/bookingStatus)  However, it differs in that it returns a multi-item array of booking items with less detail than what would be received from [/booking/status](#operation/bookingStatus). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    BookingServicesApi apiInstance = new BookingServicesApi(defaultClient);
    String acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    BookingStatusItemsRequest bookingStatusItemsRequest = new BookingStatusItemsRequest(); // BookingStatusItemsRequest | 
    try {
      BookingStatusItems200Response result = apiInstance.bookingStatusItems(acceptLanguage, bookingStatusItemsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingServicesApi#bookingStatusItems");
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
| **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | |
| **bookingStatusItemsRequest** | [**BookingStatusItemsRequest**](BookingStatusItemsRequest.md)|  | [optional] |

### Return type

[**BookingStatusItems200Response**](BookingStatusItems200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="bookingVoucher"></a>
# **bookingVoucher**
> BookingVoucher200Response bookingVoucher(acceptLanguage, leadLastName, itemId, embeddedResources, voucherKey, fullHTML, mobileVoucher)

/booking/voucher

Get voucher details - Use this service to retrieve the voucher details of a booked item. - The data returned is HTML-formatted and can be wrapped in a header and/or footer.  **Sample query parameters** - leadLastName&#x3D;Simpson test&amp;amp;itemId&#x3D;580669678  **or**  - voucherKey&#x3D;1005851866:4af44c13ecf3f1a7d3f9ef2fc00c2257e08fa42ae20f877f3039ff9b52aba24e:580669678&amp;amp;fullHTML&#x3D;true&amp;amp;mobileVoucher&#x3D;true 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    BookingServicesApi apiInstance = new BookingServicesApi(defaultClient);
    String acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    String leadLastName = "Simpson"; // String | **surname** of *this* lead traveler
    Integer itemId = 600033670; // Integer | Booking-reference number generated by Viator    - **Note**: For more information, see: [Booking references](#section/Key-concepts/Booking-references) 
    Boolean embeddedResources = false; // Boolean | ignore (Viator only)
    String voucherKey = "3299307:93c7f36a56b18ba1068787ba7fb7988da5c8ad08db77604110141ff21498603e:600033670"; // String | **identifier** for the voucher - **note**: use &lt;u&gt;either&lt;/u&gt; `voucherKey` &lt;u&gt;or&lt;/u&gt; the three separate parameters - if `voucherKey` is provided as well as the other parameters, then `voucherKey` overrides the other paramaters - `voucherKey` is obtained from [/booking/mybookings](#operation/bookingMybookings) or in the response from [/booking/book](#operation/bookingBook) when you make a booking 
    Boolean fullHTML = true; // Boolean | **specifier**: - set to `true` if you wish to retrieve the full HTML-formatted voucher - set to `false` if you want the div fragment (optional) 
    Boolean mobileVoucher = true; // Boolean | **specifier**:  - if set to `true`, the service returns the mobile (cut down) HTML-formatted voucher - if `false` the full voucher HTML is returned (ignoring `fullHTML`) - default: `true`  - this field should only be enabled for products that have a `voucherOption` of `'VOUCHER_E'` - do not enable `mobileVouchers` for paper vouchers (`voucherOption` of `'VOUCHER_PAPER_ONLY'`) as no barcode is returned - the voucher information is available in the response from [/product](#operation/product), [/booking/book](#operation/bookingBook), [/booking/pastbooking](#operation/bookingPastbooking), [/booking/mybookings](#operation/bookingMybookings) (it is also displayed under the 'Redemption Info' heading in this service) 
    try {
      BookingVoucher200Response result = apiInstance.bookingVoucher(acceptLanguage, leadLastName, itemId, embeddedResources, voucherKey, fullHTML, mobileVoucher);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingServicesApi#bookingVoucher");
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
| **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | |
| **leadLastName** | **String**| **surname** of *this* lead traveler | [optional] |
| **itemId** | **Integer**| Booking-reference number generated by Viator    - **Note**: For more information, see: [Booking references](#section/Key-concepts/Booking-references)  | [optional] |
| **embeddedResources** | **Boolean**| ignore (Viator only) | [optional] |
| **voucherKey** | **String**| **identifier** for the voucher - **note**: use &amp;lt;u&amp;gt;either&amp;lt;/u&amp;gt; &#x60;voucherKey&#x60; &amp;lt;u&amp;gt;or&amp;lt;/u&amp;gt; the three separate parameters - if &#x60;voucherKey&#x60; is provided as well as the other parameters, then &#x60;voucherKey&#x60; overrides the other paramaters - &#x60;voucherKey&#x60; is obtained from [/booking/mybookings](#operation/bookingMybookings) or in the response from [/booking/book](#operation/bookingBook) when you make a booking  | [optional] |
| **fullHTML** | **Boolean**| **specifier**: - set to &#x60;true&#x60; if you wish to retrieve the full HTML-formatted voucher - set to &#x60;false&#x60; if you want the div fragment (optional)  | [optional] |
| **mobileVoucher** | **Boolean**| **specifier**:  - if set to &#x60;true&#x60;, the service returns the mobile (cut down) HTML-formatted voucher - if &#x60;false&#x60; the full voucher HTML is returned (ignoring &#x60;fullHTML&#x60;) - default: &#x60;true&#x60;  - this field should only be enabled for products that have a &#x60;voucherOption&#x60; of &#x60;&#39;VOUCHER_E&#39;&#x60; - do not enable &#x60;mobileVouchers&#x60; for paper vouchers (&#x60;voucherOption&#x60; of &#x60;&#39;VOUCHER_PAPER_ONLY&#39;&#x60;) as no barcode is returned - the voucher information is available in the response from [/product](#operation/product), [/booking/book](#operation/bookingBook), [/booking/pastbooking](#operation/bookingPastbooking), [/booking/mybookings](#operation/bookingMybookings) (it is also displayed under the &#39;Redemption Info&#39; heading in this service)  | [optional] |

### Return type

[**BookingVoucher200Response**](BookingVoucher200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="cancelBooking"></a>
# **cancelBooking**
> CancelBookingResponse cancelBooking(bookingReference, acceptLanguage, cancellationRequest)

/bookings/{booking-reference}/cancel

Submits a cancellation request for the specified booking  For information on how to use this service, see: [Cancellation API workflow](#section/Common-workflows-and-data-validation/Cancellation-API-workflow)  **Note**:     * This service &amp;lt;u&amp;gt;requires&amp;lt;/u&amp;gt; [exp-api-key](#section/Authentication/exp-api-key) to be included as a header parameter. Please speak to your account manager if you have not yet been issued an exp-api-key.   * The base URL for the server for this endpoint is different from the older endpoints described in this document. Use &#x60;https://api.sandbox.viator.com/partner/bookings/{booking-reference}/cancel&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    BookingServicesApi apiInstance = new BookingServicesApi(defaultClient);
    String bookingReference = "bookingReference_example"; // String | The ID of the booking
    String acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    CancellationRequest cancellationRequest = new CancellationRequest(); // CancellationRequest | 
    try {
      CancelBookingResponse result = apiInstance.cancelBooking(bookingReference, acceptLanguage, cancellationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingServicesApi#cancelBooking");
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
| **bookingReference** | **String**| The ID of the booking | |
| **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | |
| **cancellationRequest** | [**CancellationRequest**](CancellationRequest.md)|  | [optional] |

### Return type

[**CancelBookingResponse**](CancelBookingResponse.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |
| **406** | Not Acceptable |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="cancelBookingQuote"></a>
# **cancelBookingQuote**
> CancelBookingQuoteResponse cancelBookingQuote(bookingReference)

/bookings/{booking-reference}/cancel-quote

Retrieves a quote for the cancellation of a booking  For information on how to use this service, see: [Cancellation API workflow](#section/Common-workflows-and-data-validation/Cancellation-API-workflow)  **Note**:     * This service &amp;lt;u&amp;gt;requires&amp;lt;/u&amp;gt; [exp-api-key](#section/Authentication/exp-api-key) to be included as a header parameter. Please speak to your account manager if you have not yet been issued an exp-api-key.   * The base URL for the server for this endpoint is different from the older endpoints described in this document. Use &#x60;https://api.sandbox.viator.com/partner/bookings/{booking-reference}/cancel-quote&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    BookingServicesApi apiInstance = new BookingServicesApi(defaultClient);
    String bookingReference = "bookingReference_example"; // String | Unique numeric identifier of the booking for which to retrieve a cancellation quote
    try {
      CancelBookingQuoteResponse result = apiInstance.cancelBookingQuote(bookingReference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingServicesApi#cancelBookingQuote");
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
| **bookingReference** | **String**| Unique numeric identifier of the booking for which to retrieve a cancellation quote | |

### Return type

[**CancelBookingQuoteResponse**](CancelBookingQuoteResponse.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **406** | Not Acceptable |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

<a id="cancellationReasons"></a>
# **cancellationReasons**
> List&lt;CancellationReasonsResponse&gt; cancellationReasons(acceptLanguage)

/bookings/cancel-reasons

Retrieves a dictionary of unique identification codes (&#x60;cancellationReasonCode&#x60;) and their associated natural-language descriptions (&#x60;cancellationReasonText&#x60;).  For information on how to use this service, see: [Cancellation API workflow](#section/Common-workflows-and-data-validation/Cancellation-API-workflow)  **Note**:     * This service &amp;lt;u&amp;gt;requires&amp;lt;/u&amp;gt; [exp-api-key](#section/Authentication/exp-api-key) to be included as a header parameter. Please speak to your account manager if you have not yet been issued an exp-api-key.   * The base URL for the server for this endpoint is different from the older endpoints described in this document. Use &#x60;https://api.sandbox.viator.com/partner/cancel-reasons&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookingServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    BookingServicesApi apiInstance = new BookingServicesApi(defaultClient);
    String acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    try {
      List<CancellationReasonsResponse> result = apiInstance.cancellationReasons(acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookingServicesApi#cancellationReasons");
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
| **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | |

### Return type

[**List&lt;CancellationReasonsResponse&gt;**](CancellationReasonsResponse.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **406** | Not Acceptable |  -  |
| **500** | Internal Server Error |  -  |
| **503** | Service Unavailable |  -  |

