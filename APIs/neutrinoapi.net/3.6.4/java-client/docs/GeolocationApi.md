# GeolocationApi

All URIs are relative to *https://neutrinoapi.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**geocodeAddress**](GeolocationApi.md#geocodeAddress) | **GET** /geocode-address | Geocode Address |
| [**geocodeReverse**](GeolocationApi.md#geocodeReverse) | **GET** /geocode-reverse | Geocode Reverse |
| [**iPInfo**](GeolocationApi.md#iPInfo) | **GET** /ip-info | IP Info |


<a id="geocodeAddress"></a>
# **geocodeAddress**
> GeocodeAddressResponse geocodeAddress(address, houseNumber, street, city, county, state, postalCode, countryCode, languageCode, fuzzySearch)

Geocode Address

Geocode an address, partial address or just the name of a place

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeolocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://neutrinoapi.net");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: user-id
    ApiKeyAuth user-id = (ApiKeyAuth) defaultClient.getAuthentication("user-id");
    user-id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user-id.setApiKeyPrefix("Token");

    GeolocationApi apiInstance = new GeolocationApi(defaultClient);
    String address = "address_example"; // String | The full address, partial address or name of a place to try and locate. Comma separated address components are preferred.
    String houseNumber = "houseNumber_example"; // String | The house/building number to locate
    String street = "street_example"; // String | The street/road name to locate
    String city = "city_example"; // String | The city/town name to locate
    String county = "county_example"; // String | The county/region name to locate
    String state = "state_example"; // String | The state name to locate
    String postalCode = "postalCode_example"; // String | The postal code to locate
    String countryCode = "countryCode_example"; // String | Limit result to this country (the default is no country bias)
    String languageCode = "en"; // String | The language to display results in, available languages are: <ul> <li>de, en, es, fr, it, pt, ru, zh</li> </ul>
    Boolean fuzzySearch = false; // Boolean | If no matches are found for the given address, start performing a recursive fuzzy search until a geolocation is found. This option is recommended for processing user input or implementing auto-complete. We use a combination of approximate string matching and data cleansing to find possible location matches
    try {
      GeocodeAddressResponse result = apiInstance.geocodeAddress(address, houseNumber, street, city, county, state, postalCode, countryCode, languageCode, fuzzySearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeolocationApi#geocodeAddress");
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
| **address** | **String**| The full address, partial address or name of a place to try and locate. Comma separated address components are preferred. | [optional] |
| **houseNumber** | **String**| The house/building number to locate | [optional] |
| **street** | **String**| The street/road name to locate | [optional] |
| **city** | **String**| The city/town name to locate | [optional] |
| **county** | **String**| The county/region name to locate | [optional] |
| **state** | **String**| The state name to locate | [optional] |
| **postalCode** | **String**| The postal code to locate | [optional] |
| **countryCode** | **String**| Limit result to this country (the default is no country bias) | [optional] |
| **languageCode** | **String**| The language to display results in, available languages are: &lt;ul&gt; &lt;li&gt;de, en, es, fr, it, pt, ru, zh&lt;/li&gt; &lt;/ul&gt; | [optional] [default to en] |
| **fuzzySearch** | **Boolean**| If no matches are found for the given address, start performing a recursive fuzzy search until a geolocation is found. This option is recommended for processing user input or implementing auto-complete. We use a combination of approximate string matching and data cleansing to find possible location matches | [optional] [default to false] |

### Return type

[**GeocodeAddressResponse**](GeocodeAddressResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your API request has been rejected. Check error code for details |  -  |
| **403** | You have failed to authenticate |  -  |
| **500** | We messed up, sorry! Your request has caused a fatal exception |  -  |
| **0** | We messed up, sorry! Your request has caused an error |  -  |

<a id="geocodeReverse"></a>
# **geocodeReverse**
> GeocodeReverseResponse geocodeReverse(latitude, longitude, languageCode, zoom)

Geocode Reverse

Convert a geographic coordinate (latitude and longitude) into a real world address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeolocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://neutrinoapi.net");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: user-id
    ApiKeyAuth user-id = (ApiKeyAuth) defaultClient.getAuthentication("user-id");
    user-id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user-id.setApiKeyPrefix("Token");

    GeolocationApi apiInstance = new GeolocationApi(defaultClient);
    String latitude = "latitude_example"; // String | The location latitude in decimal degrees format
    String longitude = "longitude_example"; // String | The location longitude in decimal degrees format
    String languageCode = "en"; // String | The language to display results in, available languages are: <ul> <li>de, en, es, fr, it, pt, ru</li> </ul>
    String zoom = "address"; // String | The zoom level to respond with: <br> <ul> <li>address - the most precise address available</li> <li>street - the street level</li> <li>city - the city level</li> <li>state - the state level</li> <li>country - the country level</li> </ul>
    try {
      GeocodeReverseResponse result = apiInstance.geocodeReverse(latitude, longitude, languageCode, zoom);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeolocationApi#geocodeReverse");
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
| **latitude** | **String**| The location latitude in decimal degrees format | |
| **longitude** | **String**| The location longitude in decimal degrees format | |
| **languageCode** | **String**| The language to display results in, available languages are: &lt;ul&gt; &lt;li&gt;de, en, es, fr, it, pt, ru&lt;/li&gt; &lt;/ul&gt; | [optional] [default to en] |
| **zoom** | **String**| The zoom level to respond with: &lt;br&gt; &lt;ul&gt; &lt;li&gt;address - the most precise address available&lt;/li&gt; &lt;li&gt;street - the street level&lt;/li&gt; &lt;li&gt;city - the city level&lt;/li&gt; &lt;li&gt;state - the state level&lt;/li&gt; &lt;li&gt;country - the country level&lt;/li&gt; &lt;/ul&gt; | [optional] [default to address] |

### Return type

[**GeocodeReverseResponse**](GeocodeReverseResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your API request has been rejected. Check error code for details |  -  |
| **403** | You have failed to authenticate |  -  |
| **500** | We messed up, sorry! Your request has caused a fatal exception |  -  |
| **0** | We messed up, sorry! Your request has caused an error |  -  |

<a id="iPInfo"></a>
# **iPInfo**
> IPInfoResponse iPInfo(ip, reverseLookup)

IP Info

Get location information about an IP address and do reverse DNS (PTR) lookups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeolocationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://neutrinoapi.net");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: user-id
    ApiKeyAuth user-id = (ApiKeyAuth) defaultClient.getAuthentication("user-id");
    user-id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user-id.setApiKeyPrefix("Token");

    GeolocationApi apiInstance = new GeolocationApi(defaultClient);
    String ip = "ip_example"; // String | IPv4 or IPv6 address
    Boolean reverseLookup = false; // Boolean | Do a reverse DNS (PTR) lookup. This option can add extra delay to the request so only use it if you need it
    try {
      IPInfoResponse result = apiInstance.iPInfo(ip, reverseLookup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeolocationApi#iPInfo");
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
| **ip** | **String**| IPv4 or IPv6 address | |
| **reverseLookup** | **Boolean**| Do a reverse DNS (PTR) lookup. This option can add extra delay to the request so only use it if you need it | [optional] [default to false] |

### Return type

[**IPInfoResponse**](IPInfoResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your API request has been rejected. Check error code for details |  -  |
| **403** | You have failed to authenticate |  -  |
| **500** | We messed up, sorry! Your request has caused a fatal exception |  -  |
| **0** | We messed up, sorry! Your request has caused an error |  -  |

