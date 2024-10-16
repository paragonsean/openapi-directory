# OffersApi

All URIs are relative to *https://api.lufthansa.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**offersLoungesByLocationGet**](OffersApi.md#offersLoungesByLocationGet) | **GET** /offers/lounges/{location} | Lounges |
| [**offersSeatmapsDestinationDateCabinClassByFlightNumberAndOriginGet**](OffersApi.md#offersSeatmapsDestinationDateCabinClassByFlightNumberAndOriginGet) | **GET** /offers/seatmaps/{flightNumber}/{origin}/{destination}/{date}/{cabinClass} | Seat Maps |


<a id="offersLoungesByLocationGet"></a>
# **offersLoungesByLocationGet**
> Object offersLoungesByLocationGet(location, accept, cabinClass, tierCode, lang)

Lounges

Lounge information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OffersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lufthansa.com/v1");
    
    // Configure OAuth2 access token for authorization: auth
    OAuth auth = (OAuth) defaultClient.getAuthentication("auth");
    auth.setAccessToken("YOUR ACCESS TOKEN");

    OffersApi apiInstance = new OffersApi(defaultClient);
    String location = "location_example"; // String | 3-leter IATA airport or city code (e.g. 'ZRH')
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    String cabinClass = "cabinClass_example"; // String | Cabin class: 'M', 'E', 'C', 'F' (Acceptable values are: \"\", \"M\", \"E\", \"C\", \"F\")
    String tierCode = "tierCode_example"; // String | Frequent flyer level ('FTL', 'SGC', 'SEN', 'HON') (Acceptable values are: \"\", \"FTL\", \"SGC\", \"SEN\", \"HON\")
    String lang = "lang_example"; // String | Language code.
    try {
      Object result = apiInstance.offersLoungesByLocationGet(location, accept, cabinClass, tierCode, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OffersApi#offersLoungesByLocationGet");
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
| **location** | **String**| 3-leter IATA airport or city code (e.g. &#39;ZRH&#39;) | |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **cabinClass** | **String**| Cabin class: &#39;M&#39;, &#39;E&#39;, &#39;C&#39;, &#39;F&#39; (Acceptable values are: \&quot;\&quot;, \&quot;M\&quot;, \&quot;E\&quot;, \&quot;C\&quot;, \&quot;F\&quot;) | [optional] |
| **tierCode** | **String**| Frequent flyer level (&#39;FTL&#39;, &#39;SGC&#39;, &#39;SEN&#39;, &#39;HON&#39;) (Acceptable values are: \&quot;\&quot;, \&quot;FTL\&quot;, \&quot;SGC\&quot;, \&quot;SEN\&quot;, \&quot;HON\&quot;) | [optional] |
| **lang** | **String**| Language code. | [optional] |

### Return type

**Object**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="offersSeatmapsDestinationDateCabinClassByFlightNumberAndOriginGet"></a>
# **offersSeatmapsDestinationDateCabinClassByFlightNumberAndOriginGet**
> Object offersSeatmapsDestinationDateCabinClassByFlightNumberAndOriginGet(flightNumber, origin, destination, date, cabinClass, accept)

Seat Maps

Cabin layout and seat characteristics.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OffersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lufthansa.com/v1");
    
    // Configure OAuth2 access token for authorization: auth
    OAuth auth = (OAuth) defaultClient.getAuthentication("auth");
    auth.setAccessToken("YOUR ACCESS TOKEN");

    OffersApi apiInstance = new OffersApi(defaultClient);
    String flightNumber = "flightNumber_example"; // String | Flight number including carrier code and any suffix (e.g. 'LH2037')
    String origin = "origin_example"; // String | Departure airport. 3-letter IATA airport code (e.g. 'TXL')
    String destination = "destination_example"; // String | Destination airport. 3-letter IATA airport code (e.g. 'MUC')
    String date = "date_example"; // String | Departure date (YYYY-MM-DD)
    String cabinClass = "cabinClass_example"; // String | Cabin class: 'M', 'E', 'C', 'F'. Some flights have fewer classes (Acceptable values are: \"M\", \"E\", \"C\", \"F\")
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    try {
      Object result = apiInstance.offersSeatmapsDestinationDateCabinClassByFlightNumberAndOriginGet(flightNumber, origin, destination, date, cabinClass, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OffersApi#offersSeatmapsDestinationDateCabinClassByFlightNumberAndOriginGet");
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
| **flightNumber** | **String**| Flight number including carrier code and any suffix (e.g. &#39;LH2037&#39;) | |
| **origin** | **String**| Departure airport. 3-letter IATA airport code (e.g. &#39;TXL&#39;) | |
| **destination** | **String**| Destination airport. 3-letter IATA airport code (e.g. &#39;MUC&#39;) | |
| **date** | **String**| Departure date (YYYY-MM-DD) | |
| **cabinClass** | **String**| Cabin class: &#39;M&#39;, &#39;E&#39;, &#39;C&#39;, &#39;F&#39;. Some flights have fewer classes (Acceptable values are: \&quot;M\&quot;, \&quot;E\&quot;, \&quot;C\&quot;, \&quot;F\&quot;) | |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |

### Return type

**Object**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

