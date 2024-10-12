# OffersApi

All URIs are relative to *https://api.lufthansa.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**allFares**](OffersApi.md#allFares) | **GET** /offers/fares/allfares | All Fares |
| [**bestFares**](OffersApi.md#bestFares) | **GET** /offers/fares/bestfares | Best Fares |
| [**deepLinks**](OffersApi.md#deepLinks) | **GET** /offers/fares/deeplink | Deep Links |
| [**fares**](OffersApi.md#fares) | **GET** /offers/fares/fares | Fares |
| [**faresSubscriptions**](OffersApi.md#faresSubscriptions) | **GET** /offers/fares/subscriptions | Fares Subscriptions |
| [**lHDeepLinksFFP**](OffersApi.md#lHDeepLinksFFP) | **GET** /offers/fares/deeplink/ffp | LH Deep Links - FFP |
| [**lHDeepLinksITCO**](OffersApi.md#lHDeepLinksITCO) | **GET** /offers/fares/deeplink/itco | LH Deep Links - ITCO |
| [**lowestFares**](OffersApi.md#lowestFares) | **GET** /offers/fares/lowestfares | Lowest Fares |
| [**oNDRoute**](OffersApi.md#oNDRoute) | **GET** /offers/ond/route/{origin}/{destination} | OND Route |
| [**oNDStatus**](OffersApi.md#oNDStatus) | **GET** /offers/ond/status | OND Status |
| [**topOND**](OffersApi.md#topOND) | **GET** /offers/ond/top | Top OND |


<a id="allFares"></a>
# **allFares**
> String allFares(catalogues, origin, destination, travelDate, returnDate, cabinClass, travelers, fareFamily, trackingid, accept)

All Fares

Retrieves all available fares for a specific Origin &amp; Destination pair on a given date. Available fares are: One-way and Return for 4U. Return only for OS

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
    String catalogues = "catalogues_example"; // String | Specifies in which catalogue the fares need to be searched (e.g.'4U;OS').
    String origin = "origin_example"; // String | Enter journey origin (e.g 'FRA').
    String destination = "destination_example"; // String | Enter journey destination (e.g 'MAD').
    String travelDate = "travelDate_example"; // String | Enter journey travel-date (e.g 2016-10-20)
    String returnDate = "returnDate_example"; // String | Enter journey return-date (e.g 2016-10-31)'.
    String cabinClass = "economy"; // String | Enter the required cabin class (e.g econonmy, business etc.). (Acceptable values are: \"\", \"economy\", \"premium economy\", \"business\", \"first\")
    String travelers = "travelers_example"; // String | Specifies the type and number of travelers (e.g. '(adult=2;child=2;infant=1)') For LH only (adult=1) possible.
    String fareFamily = "smart"; // String | Mandatory for 4U. Specifies, which fares to be returned, such as basic, smart, best, smartflex, bestflex . (Acceptable values are: \"\", \"basic\", \"smart\", \"best\", \"smartflex\", \"bestflex\")
    String trackingid = "trackingid_example"; // String | Austrian Airlines only - specify the web tracking id to be used in OS Deep link.
    String accept = "application/json"; // String | Mandatory http header:  application/xml or application/json
    try {
      String result = apiInstance.allFares(catalogues, origin, destination, travelDate, returnDate, cabinClass, travelers, fareFamily, trackingid, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OffersApi#allFares");
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
| **catalogues** | **String**| Specifies in which catalogue the fares need to be searched (e.g.&#39;4U;OS&#39;). | |
| **origin** | **String**| Enter journey origin (e.g &#39;FRA&#39;). | |
| **destination** | **String**| Enter journey destination (e.g &#39;MAD&#39;). | |
| **travelDate** | **String**| Enter journey travel-date (e.g 2016-10-20) | |
| **returnDate** | **String**| Enter journey return-date (e.g 2016-10-31)&#39;. | [optional] |
| **cabinClass** | **String**| Enter the required cabin class (e.g econonmy, business etc.). (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;) | [optional] [default to economy] |
| **travelers** | **String**| Specifies the type and number of travelers (e.g. &#39;(adult&#x3D;2;child&#x3D;2;infant&#x3D;1)&#39;) For LH only (adult&#x3D;1) possible. | [optional] |
| **fareFamily** | **String**| Mandatory for 4U. Specifies, which fares to be returned, such as basic, smart, best, smartflex, bestflex . (Acceptable values are: \&quot;\&quot;, \&quot;basic\&quot;, \&quot;smart\&quot;, \&quot;best\&quot;, \&quot;smartflex\&quot;, \&quot;bestflex\&quot;) | [optional] [default to smart] |
| **trackingid** | **String**| Austrian Airlines only - specify the web tracking id to be used in OS Deep link. | [optional] |
| **accept** | **String**| Mandatory http header:  application/xml or application/json | [optional] [default to application/json] |

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

<a id="bestFares"></a>
# **bestFares**
> String bestFares(catalogues, origin, destination, travelDate, tripDuration, range, accept, cabinClass, country, trackingid, fareFamily)

Best Fares

Retrieve best fares for the requested journey across multiple days or multiple months.

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
    String catalogues = "catalogues_example"; // String | Search fares from these carriers' catalogues (e.g. '4U;OS;LH')
    String origin = "origin_example"; // String | Journey origin. 3-letter IATA airport code (e.g. 'FRA')
    String destination = "destination_example"; // String | Journey destination. 3-letter IATA airport code (e.g. 'MAD')
    String travelDate = "travelDate_example"; // String | Journey travel-date (YYYY-MM-DD)
    String tripDuration = "tripDuration_example"; // String | Trip duration in days (e.g. '7')
    String range = "range_example"; // String | Fare range: 'byday' or 'bymonth' (Acceptable values are: \"byday\", \"bymonth\")
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    String cabinClass = "cabinClass_example"; // String | Cabin class: 'economy', 'premium_economy', 'business', 'first' (Acceptable values are: \"\", \"economy\", \"premium_economy\", \"business\", \"first\")
    String country = "country_example"; // String | Country code of requestor. 2-letter ISO 3166-1 country code (e.g. 'de')
    String trackingid = "trackingid_example"; // String | Austrian Airlines only - specify the web tracking id to be used in OS Deep link.
    String fareFamily = "fareFamily_example"; // String | Fare family: basic, smart, best, smartflex, bestflex - Germanwings only (Acceptable values are: \"\", \"basic\", \"smart\", \"best\", \"smartflex\", \"bestflex\")
    try {
      String result = apiInstance.bestFares(catalogues, origin, destination, travelDate, tripDuration, range, accept, cabinClass, country, trackingid, fareFamily);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OffersApi#bestFares");
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
| **catalogues** | **String**| Search fares from these carriers&#39; catalogues (e.g. &#39;4U;OS;LH&#39;) | |
| **origin** | **String**| Journey origin. 3-letter IATA airport code (e.g. &#39;FRA&#39;) | |
| **destination** | **String**| Journey destination. 3-letter IATA airport code (e.g. &#39;MAD&#39;) | |
| **travelDate** | **String**| Journey travel-date (YYYY-MM-DD) | |
| **tripDuration** | **String**| Trip duration in days (e.g. &#39;7&#39;) | |
| **range** | **String**| Fare range: &#39;byday&#39; or &#39;bymonth&#39; (Acceptable values are: \&quot;byday\&quot;, \&quot;bymonth\&quot;) | |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **cabinClass** | **String**| Cabin class: &#39;economy&#39;, &#39;premium_economy&#39;, &#39;business&#39;, &#39;first&#39; (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium_economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;) | [optional] |
| **country** | **String**| Country code of requestor. 2-letter ISO 3166-1 country code (e.g. &#39;de&#39;) | [optional] |
| **trackingid** | **String**| Austrian Airlines only - specify the web tracking id to be used in OS Deep link. | [optional] |
| **fareFamily** | **String**| Fare family: basic, smart, best, smartflex, bestflex - Germanwings only (Acceptable values are: \&quot;\&quot;, \&quot;basic\&quot;, \&quot;smart\&quot;, \&quot;best\&quot;, \&quot;smartflex\&quot;, \&quot;bestflex\&quot;) | [optional] |

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

<a id="deepLinks"></a>
# **deepLinks**
> String deepLinks(catalogues, trackingid, country, lang, accept, origin, originName, destination, destinationName, travelDate, returnDate, cabinClass, outboundSegments, returnSegments, travelers, fare, netFare, fareCurrency, partnerid, encryptionKey)

Deep Links

Returns valid deep links for the provided input parameters

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
    String catalogues = "catalogues_example"; // String | Carrier for which the deep link will be created (e.g. 'LH')
    String trackingid = "trackingid_example"; // String | Deep link tracking ID
    String country = "country_example"; // String | 2-letter ISO 3166-1 country code
    String lang = "lang_example"; // String | 2-letter ISO 3166-1 language code
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    String origin = "origin_example"; // String | Journey origin. 3-letter IATA airport or city code (e.g. 'FRA')
    String originName = "originName_example"; // String | Journey origin airport or city name (e.g. 'frankfurt')
    String destination = "destination_example"; // String | Journey destination. 3-letter IATA airport or city code (e.g. 'MAD')
    String destinationName = "destinationName_example"; // String | Journey destination airport or city name (e.g. 'madrid')
    String travelDate = "travelDate_example"; // String | Journey travel-date (YYYY-MM-DD)
    String returnDate = "returnDate_example"; // String | Journey return-date (YYYY-MM-DD)
    String cabinClass = "cabinClass_example"; // String | Cabin class: 'economy', 'premium_economy', 'business', 'first' (Acceptable values are: \"\", \"economy\", \"premium_economy\", \"business\", \"first\")
    String outboundSegments = "outboundSegments_example"; // String | Outbound flight segments in the sequence of travel (e.g. 'LH096;LH480')
    String returnSegments = "returnSegments_example"; // String | Flight segments in the sequence of travel (e.g. 'LH7465;LH431')
    String travelers = "travelers_example"; // String | Type and number of travelers (e.g. '(adult=2;child=2;infant=1)')
    String fare = "fare_example"; // String | Travel fare (e.g. '1341.45')
    String netFare = "netFare_example"; // String | Travel net fare. Total fare less taxes and charges (e.g. '1140')
    String fareCurrency = "fareCurrency_example"; // String | Fare currency (e.g. 'EUR')
    String partnerid = "partnerid_example"; // String | Deep link partner id (e.g. '1247')
    String encryptionKey = "encryptionKey_example"; // String | Deep link encryption-key
    try {
      String result = apiInstance.deepLinks(catalogues, trackingid, country, lang, accept, origin, originName, destination, destinationName, travelDate, returnDate, cabinClass, outboundSegments, returnSegments, travelers, fare, netFare, fareCurrency, partnerid, encryptionKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OffersApi#deepLinks");
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
| **catalogues** | **String**| Carrier for which the deep link will be created (e.g. &#39;LH&#39;) | |
| **trackingid** | **String**| Deep link tracking ID | |
| **country** | **String**| 2-letter ISO 3166-1 country code | |
| **lang** | **String**| 2-letter ISO 3166-1 language code | |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **origin** | **String**| Journey origin. 3-letter IATA airport or city code (e.g. &#39;FRA&#39;) | [optional] |
| **originName** | **String**| Journey origin airport or city name (e.g. &#39;frankfurt&#39;) | [optional] |
| **destination** | **String**| Journey destination. 3-letter IATA airport or city code (e.g. &#39;MAD&#39;) | [optional] |
| **destinationName** | **String**| Journey destination airport or city name (e.g. &#39;madrid&#39;) | [optional] |
| **travelDate** | **String**| Journey travel-date (YYYY-MM-DD) | [optional] |
| **returnDate** | **String**| Journey return-date (YYYY-MM-DD) | [optional] |
| **cabinClass** | **String**| Cabin class: &#39;economy&#39;, &#39;premium_economy&#39;, &#39;business&#39;, &#39;first&#39; (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium_economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;) | [optional] |
| **outboundSegments** | **String**| Outbound flight segments in the sequence of travel (e.g. &#39;LH096;LH480&#39;) | [optional] |
| **returnSegments** | **String**| Flight segments in the sequence of travel (e.g. &#39;LH7465;LH431&#39;) | [optional] |
| **travelers** | **String**| Type and number of travelers (e.g. &#39;(adult&#x3D;2;child&#x3D;2;infant&#x3D;1)&#39;) | [optional] |
| **fare** | **String**| Travel fare (e.g. &#39;1341.45&#39;) | [optional] |
| **netFare** | **String**| Travel net fare. Total fare less taxes and charges (e.g. &#39;1140&#39;) | [optional] |
| **fareCurrency** | **String**| Fare currency (e.g. &#39;EUR&#39;) | [optional] |
| **partnerid** | **String**| Deep link partner id (e.g. &#39;1247&#39;) | [optional] |
| **encryptionKey** | **String**| Deep link encryption-key | [optional] |

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

<a id="fares"></a>
# **fares**
> String fares(catalogues, segments, carriers, accept, travelers, fareTypes)

Fares

Retrieve all available fares per fare family for a specific Origin &amp; Destination on a given date

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
    String catalogues = "catalogues_example"; // String | Search fares from these carriers' catalogues - currently active for Germanwings only  (4U)
    String segments = "segments_example"; // String | Journey details  e.g. (origin=TXL;destination=CGN;travel-date=2016-12-15;return-date=2016-12-20;cabin=Economy)
    String carriers = "carriers_example"; // String | Include fares for these carriers e.g. ('4U;LH')
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    String travelers = "travelers_example"; // String | Type and number of travelers e.g. (adult=1;child=1;infant=1)
    String fareTypes = "basic"; // String | Fares family: basic,smart, best, smartflex, bestflex - Germanwings only (Acceptable values are: \"\", \"basic\", \"smart\", \"best\", \"smartflex\", \"bestflex\")
    try {
      String result = apiInstance.fares(catalogues, segments, carriers, accept, travelers, fareTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OffersApi#fares");
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
| **catalogues** | **String**| Search fares from these carriers&#39; catalogues - currently active for Germanwings only  (4U) | |
| **segments** | **String**| Journey details  e.g. (origin&#x3D;TXL;destination&#x3D;CGN;travel-date&#x3D;2016-12-15;return-date&#x3D;2016-12-20;cabin&#x3D;Economy) | |
| **carriers** | **String**| Include fares for these carriers e.g. (&#39;4U;LH&#39;) | |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **travelers** | **String**| Type and number of travelers e.g. (adult&#x3D;1;child&#x3D;1;infant&#x3D;1) | [optional] |
| **fareTypes** | **String**| Fares family: basic,smart, best, smartflex, bestflex - Germanwings only (Acceptable values are: \&quot;\&quot;, \&quot;basic\&quot;, \&quot;smart\&quot;, \&quot;best\&quot;, \&quot;smartflex\&quot;, \&quot;bestflex\&quot;) | [optional] [default to basic] |

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

<a id="faresSubscriptions"></a>
# **faresSubscriptions**
> String faresSubscriptions(origin, destination, cabinClass, tripDuration, email, lang, accept, country, trackingid)

Fares Subscriptions

Create a subscription for best price O&amp;D. Receive regular updates on lowest fares

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
    String origin = "origin_example"; // String | Journey origin. 3-leter IATA airport code (e.g. 'FRA')
    String destination = "destination_example"; // String | Journey destination. 3-letter IATA airport code (e.g. 'MAD')
    String cabinClass = "cabinClass_example"; // String | Cabin class: 'economy', 'premium_economy', 'business', 'first' (Acceptable values are: \"\", \"economy\", \"premium_economy\", \"business\", \"first\")
    String tripDuration = "tripDuration_example"; // String | Trip duration in days (e.g. '7')
    String email = "email_example"; // String | Email Address')
    String lang = "lang_example"; // String | 2-letter ISO 3166-1 language code
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    String country = "country_example"; // String | 2-letter ISO 3166-1 country code
    String trackingid = "trackingid_example"; // String | Tracking parameter
    try {
      String result = apiInstance.faresSubscriptions(origin, destination, cabinClass, tripDuration, email, lang, accept, country, trackingid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OffersApi#faresSubscriptions");
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
| **origin** | **String**| Journey origin. 3-leter IATA airport code (e.g. &#39;FRA&#39;) | |
| **destination** | **String**| Journey destination. 3-letter IATA airport code (e.g. &#39;MAD&#39;) | |
| **cabinClass** | **String**| Cabin class: &#39;economy&#39;, &#39;premium_economy&#39;, &#39;business&#39;, &#39;first&#39; (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium_economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;) | |
| **tripDuration** | **String**| Trip duration in days (e.g. &#39;7&#39;) | |
| **email** | **String**| Email Address&#39;) | |
| **lang** | **String**| 2-letter ISO 3166-1 language code | |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **country** | **String**| 2-letter ISO 3166-1 country code | [optional] |
| **trackingid** | **String**| Tracking parameter | [optional] |

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

<a id="lHDeepLinksFFP"></a>
# **lHDeepLinksFFP**
> String lHDeepLinksFFP(catalogues, origin, destination, travelDate, trackingid, country, lang, accept, returnDate, cabinClass, travelers, partnerid, encryptionKey)

LH Deep Links - FFP

Returns valid LH deep links (FFP - links to flight selection screen on LH.COM)

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
    String catalogues = "catalogues_example"; // String | Carrier for which the deep link will be created (e.g. 'LH')
    String origin = "origin_example"; // String | Journey origin. 3-letter IATA airport or city code (e.g. 'FRA')
    String destination = "destination_example"; // String | Journey destination. 3-letter IATA airport or city code (e.g. 'MAD')
    String travelDate = "travelDate_example"; // String | Journey travel-date (YYYY-MM-DD)
    String trackingid = "trackingid_example"; // String | Deep link tracking ID
    String country = "country_example"; // String | 2-letter ISO 3166-1 country code
    String lang = "lang_example"; // String | 2-letter ISO 3166-1 language code
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    String returnDate = "returnDate_example"; // String | Journey return-date (YYYY-MM-DD)
    String cabinClass = "cabinClass_example"; // String | Cabin class: 'economy', 'premium_economy', 'business', 'first' (Acceptable values are: \"\", \"economy\", \"premium_economy\", \"business\", \"first\")
    String travelers = "travelers_example"; // String | Type and number of travelers (e.g. '(adult=2;child=2;infant=1)')
    String partnerid = "partnerid_example"; // String | Deep link partner id (e.g. '1247')
    String encryptionKey = "encryptionKey_example"; // String | Deep link encryption-key
    try {
      String result = apiInstance.lHDeepLinksFFP(catalogues, origin, destination, travelDate, trackingid, country, lang, accept, returnDate, cabinClass, travelers, partnerid, encryptionKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OffersApi#lHDeepLinksFFP");
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
| **catalogues** | **String**| Carrier for which the deep link will be created (e.g. &#39;LH&#39;) | |
| **origin** | **String**| Journey origin. 3-letter IATA airport or city code (e.g. &#39;FRA&#39;) | |
| **destination** | **String**| Journey destination. 3-letter IATA airport or city code (e.g. &#39;MAD&#39;) | |
| **travelDate** | **String**| Journey travel-date (YYYY-MM-DD) | |
| **trackingid** | **String**| Deep link tracking ID | |
| **country** | **String**| 2-letter ISO 3166-1 country code | |
| **lang** | **String**| 2-letter ISO 3166-1 language code | |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **returnDate** | **String**| Journey return-date (YYYY-MM-DD) | [optional] |
| **cabinClass** | **String**| Cabin class: &#39;economy&#39;, &#39;premium_economy&#39;, &#39;business&#39;, &#39;first&#39; (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium_economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;) | [optional] |
| **travelers** | **String**| Type and number of travelers (e.g. &#39;(adult&#x3D;2;child&#x3D;2;infant&#x3D;1)&#39;) | [optional] |
| **partnerid** | **String**| Deep link partner id (e.g. &#39;1247&#39;) | [optional] |
| **encryptionKey** | **String**| Deep link encryption-key | [optional] |

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

<a id="lHDeepLinksITCO"></a>
# **lHDeepLinksITCO**
> String lHDeepLinksITCO(catalogues, origin, destination, travelDate, outboundSegments, fare, fareCurrency, trackingid, country, lang, accept, returnDate, cabinClass, returnSegments, travelers, netFare, partnerid, encryptionKey)

LH Deep Links - ITCO

Returns valid LH deep links (ITCO - links to shopping cart on LH.COM)

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
    String catalogues = "catalogues_example"; // String | Carrier for which the deep link will be created (e.g. 'LH')
    String origin = "origin_example"; // String | Journey origin. 3-letter IATA airport or city code (e.g. 'FRA')
    String destination = "destination_example"; // String | Journey destination. 3-letter IATA airport or city code (e.g. 'MAD')
    String travelDate = "travelDate_example"; // String | Journey travel-date (YYYY-MM-DD)
    String outboundSegments = "outboundSegments_example"; // String | Outbound flight segments in the sequence of travel (e.g. 'LH096;LH480')
    String fare = "fare_example"; // String | Travel fare (e.g. '1341.45')
    String fareCurrency = "fareCurrency_example"; // String | Fare currency (e.g. 'EUR')
    String trackingid = "trackingid_example"; // String | Deep link tracking ID
    String country = "country_example"; // String | 2-letter ISO 3166-1 country code
    String lang = "lang_example"; // String | 2-letter ISO 3166-1 language code
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    String returnDate = "returnDate_example"; // String | Journey return-date (YYYY-MM-DD)
    String cabinClass = "cabinClass_example"; // String | Cabin class: 'economy', 'premium_economy', 'business', 'first' (Acceptable values are: \"\", \"economy\", \"premium_economy\", \"business\", \"first\")
    String returnSegments = "returnSegments_example"; // String | Flight segments in the sequence of travel (e.g. 'LH7465;LH431')
    String travelers = "travelers_example"; // String | Type and number of travelers (e.g. '(adult=2;child=2;infant=1)')
    String netFare = "netFare_example"; // String | Travel net fare. Total fare less taxes and charges (e.g. '1140')
    String partnerid = "partnerid_example"; // String | Deep link partner id (e.g. '1247')
    String encryptionKey = "encryptionKey_example"; // String | Deep link encryption-key
    try {
      String result = apiInstance.lHDeepLinksITCO(catalogues, origin, destination, travelDate, outboundSegments, fare, fareCurrency, trackingid, country, lang, accept, returnDate, cabinClass, returnSegments, travelers, netFare, partnerid, encryptionKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OffersApi#lHDeepLinksITCO");
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
| **catalogues** | **String**| Carrier for which the deep link will be created (e.g. &#39;LH&#39;) | |
| **origin** | **String**| Journey origin. 3-letter IATA airport or city code (e.g. &#39;FRA&#39;) | |
| **destination** | **String**| Journey destination. 3-letter IATA airport or city code (e.g. &#39;MAD&#39;) | |
| **travelDate** | **String**| Journey travel-date (YYYY-MM-DD) | |
| **outboundSegments** | **String**| Outbound flight segments in the sequence of travel (e.g. &#39;LH096;LH480&#39;) | |
| **fare** | **String**| Travel fare (e.g. &#39;1341.45&#39;) | |
| **fareCurrency** | **String**| Fare currency (e.g. &#39;EUR&#39;) | |
| **trackingid** | **String**| Deep link tracking ID | |
| **country** | **String**| 2-letter ISO 3166-1 country code | |
| **lang** | **String**| 2-letter ISO 3166-1 language code | |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **returnDate** | **String**| Journey return-date (YYYY-MM-DD) | [optional] |
| **cabinClass** | **String**| Cabin class: &#39;economy&#39;, &#39;premium_economy&#39;, &#39;business&#39;, &#39;first&#39; (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium_economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;) | [optional] |
| **returnSegments** | **String**| Flight segments in the sequence of travel (e.g. &#39;LH7465;LH431&#39;) | [optional] |
| **travelers** | **String**| Type and number of travelers (e.g. &#39;(adult&#x3D;2;child&#x3D;2;infant&#x3D;1)&#39;) | [optional] |
| **netFare** | **String**| Travel net fare. Total fare less taxes and charges (e.g. &#39;1140&#39;) | [optional] |
| **partnerid** | **String**| Deep link partner id (e.g. &#39;1247&#39;) | [optional] |
| **encryptionKey** | **String**| Deep link encryption-key | [optional] |

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

<a id="lowestFares"></a>
# **lowestFares**
> String lowestFares(catalogues, origin, destination, travelDate, accept, returnDate, cabinClass, travelers, fareFamily, country)

Lowest Fares

Retrieve lowest fare for a specific Origin &amp; Destination pair on a given date. Available fares are: One-way and Return for 4U. Return only for OS &amp; LH

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
    String catalogues = "catalogues_example"; // String | Search fares from these carriers' catalogues e.g. '4U;OS;LH'
    String origin = "origin_example"; // String | Journey origin. 3-letter IATA aiport code e.g. 'FRA'
    String destination = "destination_example"; // String | Journey destination. 3-letter IATA airport code e.g. 'MAD'
    String travelDate = "travelDate_example"; // String | Journey travel-date YYYY-MM-DD
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    String returnDate = "returnDate_example"; // String | Journey return-date - mandatory for OS and LH searches YYYY-MM-DD
    String cabinClass = "cabinClass_example"; // String | Cabin class: 'economy', 'premium_economy', 'business', 'first' (Acceptable values are: \"\", \"economy\", \"premium_economy\", \"business\", \"first\")
    String travelers = "travelers_example"; // String | Type and number of travelers e.g. '(adult=2;child=2;infant=1)'. For LH only (adult=1) possible
    String fareFamily = "basic"; // String | Fare family: basic, smart, best, smartflex, bestflex - Germanwings only (Acceptable values are: \"\", \"basic\", \"smart\", \"best\", \"smartflex\", \"bestflex\")
    String country = "country_example"; // String | Country code of requestor. 2-letter ISO 3166-1 country code (e.g. 'de')
    try {
      String result = apiInstance.lowestFares(catalogues, origin, destination, travelDate, accept, returnDate, cabinClass, travelers, fareFamily, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OffersApi#lowestFares");
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
| **catalogues** | **String**| Search fares from these carriers&#39; catalogues e.g. &#39;4U;OS;LH&#39; | |
| **origin** | **String**| Journey origin. 3-letter IATA aiport code e.g. &#39;FRA&#39; | |
| **destination** | **String**| Journey destination. 3-letter IATA airport code e.g. &#39;MAD&#39; | |
| **travelDate** | **String**| Journey travel-date YYYY-MM-DD | |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **returnDate** | **String**| Journey return-date - mandatory for OS and LH searches YYYY-MM-DD | [optional] |
| **cabinClass** | **String**| Cabin class: &#39;economy&#39;, &#39;premium_economy&#39;, &#39;business&#39;, &#39;first&#39; (Acceptable values are: \&quot;\&quot;, \&quot;economy\&quot;, \&quot;premium_economy\&quot;, \&quot;business\&quot;, \&quot;first\&quot;) | [optional] |
| **travelers** | **String**| Type and number of travelers e.g. &#39;(adult&#x3D;2;child&#x3D;2;infant&#x3D;1)&#39;. For LH only (adult&#x3D;1) possible | [optional] |
| **fareFamily** | **String**| Fare family: basic, smart, best, smartflex, bestflex - Germanwings only (Acceptable values are: \&quot;\&quot;, \&quot;basic\&quot;, \&quot;smart\&quot;, \&quot;best\&quot;, \&quot;smartflex\&quot;, \&quot;bestflex\&quot;) | [optional] [default to basic] |
| **country** | **String**| Country code of requestor. 2-letter ISO 3166-1 country code (e.g. &#39;de&#39;) | [optional] |

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

<a id="oNDRoute"></a>
# **oNDRoute**
> String oNDRoute(origin, destination, accept, catalogues, limit, offset)

OND Route

Returns LH route origin &amp; destination information

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
    String origin = "origin_example"; // String | Enter either the orgin city or orgin country code (e.g 'FRA' or 'DE'). Enter '*' for all
    String destination = "destination_example"; // String | Enter either the destination city or country code (e.g 'MAD' or 'ES'). Enter '*' for all
    String accept = "accept_example"; // String | Mandatory http header:  application/xml or application/json
    String catalogues = "LH"; // String | Carrier for which the OND will be retrieved (e.g. 'LH')
    String limit = "limit_example"; // String | Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    String offset = "offset_example"; // String | Number of records skipped. Defaults to 0
    try {
      String result = apiInstance.oNDRoute(origin, destination, accept, catalogues, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OffersApi#oNDRoute");
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
| **origin** | **String**| Enter either the orgin city or orgin country code (e.g &#39;FRA&#39; or &#39;DE&#39;). Enter &#39;*&#39; for all | |
| **destination** | **String**| Enter either the destination city or country code (e.g &#39;MAD&#39; or &#39;ES&#39;). Enter &#39;*&#39; for all | |
| **accept** | **String**| Mandatory http header:  application/xml or application/json | |
| **catalogues** | **String**| Carrier for which the OND will be retrieved (e.g. &#39;LH&#39;) | [optional] [default to LH] |
| **limit** | **String**| Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken) | [optional] |
| **offset** | **String**| Number of records skipped. Defaults to 0 | [optional] |

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

<a id="oNDStatus"></a>
# **oNDStatus**
> String oNDStatus(accept, catalogues, newRoutes, oldRoutes)

OND Status

Returns LH network route status information. Search for recently added or retired routes

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
    String accept = "accept_example"; // String | Mandatory http header:  application/xml or application/json
    String catalogues = "LH"; // String | Carrier for which the OND will be retrieved (e.g. 'LH')
    String newRoutes = "newRoutes_example"; // String | Enter if newly added routes should be returned in the response. (Acceptable values are: \"\", \"true\", \"false\")
    String oldRoutes = "oldRoutes_example"; // String | Enter if old (deleted) routes should be returned in the response. (Acceptable values are: \"\", \"true\", \"false\")
    try {
      String result = apiInstance.oNDStatus(accept, catalogues, newRoutes, oldRoutes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OffersApi#oNDStatus");
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
| **accept** | **String**| Mandatory http header:  application/xml or application/json | |
| **catalogues** | **String**| Carrier for which the OND will be retrieved (e.g. &#39;LH&#39;) | [optional] [default to LH] |
| **newRoutes** | **String**| Enter if newly added routes should be returned in the response. (Acceptable values are: \&quot;\&quot;, \&quot;true\&quot;, \&quot;false\&quot;) | [optional] |
| **oldRoutes** | **String**| Enter if old (deleted) routes should be returned in the response. (Acceptable values are: \&quot;\&quot;, \&quot;true\&quot;, \&quot;false\&quot;) | [optional] |

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

<a id="topOND"></a>
# **topOND**
> String topOND(accept, catalogues, origin)

Top OND

Returns LH Top routes per country or across all countries

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
    String accept = "accept_example"; // String | Mandatory http header:  application/xml or application/json
    String catalogues = "LH"; // String | Carrier for which the OND will be retrieved (e.g. 'LH')
    String origin = "origin_example"; // String | Enter the origin country code (e.g. 'DE'). Leave empty to search Top OND across all countries
    try {
      String result = apiInstance.topOND(accept, catalogues, origin);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OffersApi#topOND");
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
| **accept** | **String**| Mandatory http header:  application/xml or application/json | |
| **catalogues** | **String**| Carrier for which the OND will be retrieved (e.g. &#39;LH&#39;) | [optional] [default to LH] |
| **origin** | **String**| Enter the origin country code (e.g. &#39;DE&#39;). Leave empty to search Top OND across all countries | [optional] |

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

