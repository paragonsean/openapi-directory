# ReferenceDataApi

All URIs are relative to *https://api.lufthansa.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**referencesAircraftByAircraftCodeGet**](ReferenceDataApi.md#referencesAircraftByAircraftCodeGet) | **GET** /references/aircraft/{aircraftCode} | Aircraft |
| [**referencesAirlinesByAirlineCodeGet**](ReferenceDataApi.md#referencesAirlinesByAirlineCodeGet) | **GET** /references/airlines/{airlineCode} | Airlines |
| [**referencesAirportsByAirportCodeGet**](ReferenceDataApi.md#referencesAirportsByAirportCodeGet) | **GET** /references/airports/{airportCode} | Airports |
| [**referencesAirportsNearestByLatitudeAndLongitudeGet**](ReferenceDataApi.md#referencesAirportsNearestByLatitudeAndLongitudeGet) | **GET** /references/airports/nearest/{latitude},{longitude} | Nearest Airports |
| [**referencesCitiesByCityCodeGet**](ReferenceDataApi.md#referencesCitiesByCityCodeGet) | **GET** /references/cities/{cityCode} | Cities |
| [**referencesCountriesByCountryCodeGet**](ReferenceDataApi.md#referencesCountriesByCountryCodeGet) | **GET** /references/countries/{countryCode} | Countries |


<a id="referencesAircraftByAircraftCodeGet"></a>
# **referencesAircraftByAircraftCodeGet**
> Object referencesAircraftByAircraftCodeGet(accept, aircraftCode, limit, offset)

Aircraft

List all aircraft types or one specific aircraft type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lufthansa.com/v1");
    
    // Configure OAuth2 access token for authorization: auth
    OAuth auth = (OAuth) defaultClient.getAuthentication("auth");
    auth.setAccessToken("YOUR ACCESS TOKEN");

    ReferenceDataApi apiInstance = new ReferenceDataApi(defaultClient);
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    String aircraftCode = "33P"; // String | 3-character IATA aircraft code
    String limit = "20"; // String | Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    String offset = "0"; // String | Number of records skipped. Defaults to 0
    try {
      Object result = apiInstance.referencesAircraftByAircraftCodeGet(accept, aircraftCode, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceDataApi#referencesAircraftByAircraftCodeGet");
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
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **aircraftCode** | **String**| 3-character IATA aircraft code | [default to 33P] |
| **limit** | **String**| Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken) | [optional] [default to 20] |
| **offset** | **String**| Number of records skipped. Defaults to 0 | [optional] [default to 0] |

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

<a id="referencesAirlinesByAirlineCodeGet"></a>
# **referencesAirlinesByAirlineCodeGet**
> Object referencesAirlinesByAirlineCodeGet(accept, airlineCode, limit, offset)

Airlines

List all airlines or one specific airline.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lufthansa.com/v1");
    
    // Configure OAuth2 access token for authorization: auth
    OAuth auth = (OAuth) defaultClient.getAuthentication("auth");
    auth.setAccessToken("YOUR ACCESS TOKEN");

    ReferenceDataApi apiInstance = new ReferenceDataApi(defaultClient);
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    String airlineCode = "LH"; // String | 2-character IATA airline/carrier code
    String limit = "20"; // String | Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    String offset = "0"; // String | Number of records skipped. Defaults to 0
    try {
      Object result = apiInstance.referencesAirlinesByAirlineCodeGet(accept, airlineCode, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceDataApi#referencesAirlinesByAirlineCodeGet");
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
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **airlineCode** | **String**| 2-character IATA airline/carrier code | [default to LH] |
| **limit** | **String**| Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken) | [optional] [default to 20] |
| **offset** | **String**| Number of records skipped. Defaults to 0 | [optional] [default to 0] |

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

<a id="referencesAirportsByAirportCodeGet"></a>
# **referencesAirportsByAirportCodeGet**
> AirportResponse referencesAirportsByAirportCodeGet(accept, airportCode, lang, limit, offset, lhoperated)

Airports

List all airports or one specific airport. All airports response is very large. It is possible to request the response in a specific language.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lufthansa.com/v1");
    
    // Configure OAuth2 access token for authorization: auth
    OAuth auth = (OAuth) defaultClient.getAuthentication("auth");
    auth.setAccessToken("YOUR ACCESS TOKEN");

    ReferenceDataApi apiInstance = new ReferenceDataApi(defaultClient);
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    String airportCode = "TXL"; // String | 3-letter IATA airport code
    String lang = "lang_example"; // String | 2-letter ISO 3166-1 language code
    String limit = "20"; // String | Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    String offset = "0"; // String | Number of records skipped. Defaults to 0
    Boolean lhoperated = true; // Boolean | Restrict the results to locations with flights operated by LH (false=0, true=1)
    try {
      AirportResponse result = apiInstance.referencesAirportsByAirportCodeGet(accept, airportCode, lang, limit, offset, lhoperated);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceDataApi#referencesAirportsByAirportCodeGet");
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
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **airportCode** | **String**| 3-letter IATA airport code | [default to TXL] |
| **lang** | **String**| 2-letter ISO 3166-1 language code | [optional] |
| **limit** | **String**| Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken) | [optional] [default to 20] |
| **offset** | **String**| Number of records skipped. Defaults to 0 | [optional] [default to 0] |
| **lhoperated** | **Boolean**| Restrict the results to locations with flights operated by LH (false&#x3D;0, true&#x3D;1) | [optional] |

### Return type

[**AirportResponse**](AirportResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="referencesAirportsNearestByLatitudeAndLongitudeGet"></a>
# **referencesAirportsNearestByLatitudeAndLongitudeGet**
> Object referencesAirportsNearestByLatitudeAndLongitudeGet(latitude, longitude, accept, lang)

Nearest Airports

List the 5 closest airports to the given latitude and longitude, irrespective of the radius of the reference point.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lufthansa.com/v1");
    
    // Configure OAuth2 access token for authorization: auth
    OAuth auth = (OAuth) defaultClient.getAuthentication("auth");
    auth.setAccessToken("YOUR ACCESS TOKEN");

    ReferenceDataApi apiInstance = new ReferenceDataApi(defaultClient);
    Integer latitude = 56; // Integer | Latitude in decimal format to at most 3 decimal places
    Integer longitude = 56; // Integer | Longitude in decimal format to at most 3 decimal places
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    String lang = "lang_example"; // String | 2 letter ISO 3166-1 language code
    try {
      Object result = apiInstance.referencesAirportsNearestByLatitudeAndLongitudeGet(latitude, longitude, accept, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceDataApi#referencesAirportsNearestByLatitudeAndLongitudeGet");
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
| **latitude** | **Integer**| Latitude in decimal format to at most 3 decimal places | |
| **longitude** | **Integer**| Longitude in decimal format to at most 3 decimal places | |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **lang** | **String**| 2 letter ISO 3166-1 language code | [optional] |

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

<a id="referencesCitiesByCityCodeGet"></a>
# **referencesCitiesByCityCodeGet**
> Object referencesCitiesByCityCodeGet(accept, cityCode, lang, limit, offset)

Cities

List all cities or one specific city. It is possible to request the response in a specific language.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lufthansa.com/v1");
    
    // Configure OAuth2 access token for authorization: auth
    OAuth auth = (OAuth) defaultClient.getAuthentication("auth");
    auth.setAccessToken("YOUR ACCESS TOKEN");

    ReferenceDataApi apiInstance = new ReferenceDataApi(defaultClient);
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    String cityCode = "BER"; // String | 3-letter IATA city code
    String lang = "lang_example"; // String | 2 letter ISO 3166-1 language code
    String limit = "20"; // String | Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    String offset = "0"; // String | Number of records skipped. Defaults to 0
    try {
      Object result = apiInstance.referencesCitiesByCityCodeGet(accept, cityCode, lang, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceDataApi#referencesCitiesByCityCodeGet");
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
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **cityCode** | **String**| 3-letter IATA city code | [default to BER] |
| **lang** | **String**| 2 letter ISO 3166-1 language code | [optional] |
| **limit** | **String**| Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken) | [optional] [default to 20] |
| **offset** | **String**| Number of records skipped. Defaults to 0 | [optional] [default to 0] |

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

<a id="referencesCountriesByCountryCodeGet"></a>
# **referencesCountriesByCountryCodeGet**
> Object referencesCountriesByCountryCodeGet(accept, countryCode, lang, limit, offset)

Countries

List all countries or one specific country. It is possible to request the response in a specific language.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lufthansa.com/v1");
    
    // Configure OAuth2 access token for authorization: auth
    OAuth auth = (OAuth) defaultClient.getAuthentication("auth");
    auth.setAccessToken("YOUR ACCESS TOKEN");

    ReferenceDataApi apiInstance = new ReferenceDataApi(defaultClient);
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    String countryCode = "DK"; // String | 2-letter ISO 3166-1 country code
    String lang = "lang_example"; // String | 2 letter ISO 3166-1 language code
    String limit = "20"; // String | Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    String offset = "0"; // String | Number of records skipped. Defaults to 0
    try {
      Object result = apiInstance.referencesCountriesByCountryCodeGet(accept, countryCode, lang, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceDataApi#referencesCountriesByCountryCodeGet");
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
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |
| **countryCode** | **String**| 2-letter ISO 3166-1 country code | [default to DK] |
| **lang** | **String**| 2 letter ISO 3166-1 language code | [optional] |
| **limit** | **String**| Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken) | [optional] [default to 20] |
| **offset** | **String**| Number of records skipped. Defaults to 0 | [optional] [default to 0] |

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

