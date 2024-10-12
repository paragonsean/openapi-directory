# GeographyApisApi

All URIs are relative to *https://api.mon-voyage-pas-cher.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAirport**](GeographyApisApi.md#getAirport) | **GET** /airports | Search airports by country / Search nearby airports / Search an airport |
| [**getAutocomplete**](GeographyApisApi.md#getAutocomplete) | **GET** /cities/findcitiesfromtext | Retrieve cities informations from a string / build an autocomplete |
| [**getCities**](GeographyApisApi.md#getCities) | **GET** /cities/findcitiesfromlatlong | Search all cities from lat/long or countrycode |
| [**getContinents**](GeographyApisApi.md#getContinents) | **GET** /continents | Search all continents or one specific continent |
| [**getCountries**](GeographyApisApi.md#getCountries) | **GET** /countries | Search all countries or one specific country |
| [**getSignificantCities**](GeographyApisApi.md#getSignificantCities) | **GET** /cities/significant | Search significant cities from lat/long or countrycode |


<a id="getAirport"></a>
# **getAirport**
> AirportsSearchResponse getAirport(language, location, radius, countrycode, topAirports)

Search airports by country / Search nearby airports / Search an airport

This webservice is providing you the ability to retrieve a list of airports matching your search criterias.&lt;br /&gt;The 3 mains search criterias are&lt;br /&gt;- by country code, this will list all airports for a given country.&lt;br /&gt;- by latitude/longitude with a radius in km. You can actually combine those 2 criterias, and search for example the closest airport in the USA of Vancoucer, Canada.&lt;br /&gt;- The last way to use the API is by searching directly with a IATA CODE in the location parameter, this will only return one result in the array of data results

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeographyApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mon-voyage-pas-cher.com");
    
    // Configure API key authorization: x-api-key
    ApiKeyAuth x-api-key = (ApiKeyAuth) defaultClient.getAuthentication("x-api-key");
    x-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //x-api-key.setApiKeyPrefix("Token");

    GeographyApisApi apiInstance = new GeographyApisApi(defaultClient);
    String language = "en"; // String | the language code of the language you want the content to be returned
    String location = "location_example"; // String | The location you want to search for. Either a latitude/longitude point or a letter airport IATA CODE ( ex. LHR ) if you want the detail for only one single airport.
    Integer radius = 100; // Integer | Radius in km for a lat/long search, will be ignore if a IATA is passed in location parameter code is passed
    String countrycode = "countrycode_example"; // String | Filter - The country ISO code 2 letters, provided by the GET /countries. If passed the results will be filtered to this country only, regardless if you passed a lat/long and a large radius
    Boolean topAirports = true; // Boolean | Filter the results to only the top and large airports airports.
    try {
      AirportsSearchResponse result = apiInstance.getAirport(language, location, radius, countrycode, topAirports);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeographyApisApi#getAirport");
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
| **language** | **String**| the language code of the language you want the content to be returned | [enum: en, fr, de, es] |
| **location** | **String**| The location you want to search for. Either a latitude/longitude point or a letter airport IATA CODE ( ex. LHR ) if you want the detail for only one single airport. | [optional] |
| **radius** | **Integer**| Radius in km for a lat/long search, will be ignore if a IATA is passed in location parameter code is passed | [optional] [default to 100] |
| **countrycode** | **String**| Filter - The country ISO code 2 letters, provided by the GET /countries. If passed the results will be filtered to this country only, regardless if you passed a lat/long and a large radius | [optional] |
| **topAirports** | **Boolean**| Filter the results to only the top and large airports airports. | [optional] |

### Return type

[**AirportsSearchResponse**](AirportsSearchResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **500** | The error message object |  -  |

<a id="getAutocomplete"></a>
# **getAutocomplete**
> CitiesResponse getAutocomplete(q, language, sort, countrycode)

Retrieve cities informations from a string / build an autocomplete

Search cities from a string parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeographyApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mon-voyage-pas-cher.com");
    
    // Configure API key authorization: x-api-key
    ApiKeyAuth x-api-key = (ApiKeyAuth) defaultClient.getAuthentication("x-api-key");
    x-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //x-api-key.setApiKeyPrefix("Token");

    GeographyApisApi apiInstance = new GeographyApisApi(defaultClient);
    String q = "q_example"; // String | the string you want to search
    String language = "en"; // String | the language code of the language you want the content to be returned
    String sort = "population,desc"; // String | The order you want the result ordered. Default is population while when entering a lat/long, you can order the results by distance from requested lat/long point
    String countrycode = "countrycode_example"; // String | if you want to limit the result to one country
    try {
      CitiesResponse result = apiInstance.getAutocomplete(q, language, sort, countrycode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeographyApisApi#getAutocomplete");
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
| **q** | **String**| the string you want to search | |
| **language** | **String**| the language code of the language you want the content to be returned | [enum: en, fr, de, es] |
| **sort** | **String**| The order you want the result ordered. Default is population while when entering a lat/long, you can order the results by distance from requested lat/long point | [default to population,desc] [enum: population,desc, population,asc, elevation,desc, elevation,asc, name,desc, name,asc, timezone,asc, timezone,desc, match_score,desc, match_score,asc] |
| **countrycode** | **String**| if you want to limit the result to one country | [optional] |

### Return type

[**CitiesResponse**](CitiesResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **500** | The error message object |  -  |

<a id="getCities"></a>
# **getCities**
> CitiesResponse getCities(language, sort, countrycode, location, radius, limit, offset)

Search all cities from lat/long or countrycode

Search cities according to given criterias. Either lat/long + radius or country code. A limit can be given but cannot exceed 50 results.&lt;br /&gt; A significant city will be defined according to the pourcent of population within a country.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeographyApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mon-voyage-pas-cher.com");
    
    // Configure API key authorization: x-api-key
    ApiKeyAuth x-api-key = (ApiKeyAuth) defaultClient.getAuthentication("x-api-key");
    x-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //x-api-key.setApiKeyPrefix("Token");

    GeographyApisApi apiInstance = new GeographyApisApi(defaultClient);
    String language = "en"; // String | the language code of the language you want the content to be returned
    String sort = "distance,desc"; // String | The order you want the result ordered. Default is population while when entering a lat/long, you can order the results by distance from requested lat/long point
    String countrycode = "countrycode_example"; // String | if you want to limit the result to one country
    String location = "location_example"; // String | The Lat/Long of the location your are seeking cities ( ex. 45.4478988,3.23456)
    Integer radius = 20; // Integer | Radius in km for a lat/long search. Default is 20km and there is no maximum, but need to be combined with limit. code is passed
    Integer limit = 20; // Integer | Limit of the result. Default is 20 rows, and maximum is 50.
    Integer offset = 0; // Integer | offset of the result set
    try {
      CitiesResponse result = apiInstance.getCities(language, sort, countrycode, location, radius, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeographyApisApi#getCities");
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
| **language** | **String**| the language code of the language you want the content to be returned | [enum: en, fr, de, es] |
| **sort** | **String**| The order you want the result ordered. Default is population while when entering a lat/long, you can order the results by distance from requested lat/long point | [default to distance,asc] [enum: distance,desc, distance,asc, population,desc, population,asc, elevation,desc, elevation,asc, name,desc, name,asc, timezone,asc, timezone,desc] |
| **countrycode** | **String**| if you want to limit the result to one country | [optional] |
| **location** | **String**| The Lat/Long of the location your are seeking cities ( ex. 45.4478988,3.23456) | [optional] |
| **radius** | **Integer**| Radius in km for a lat/long search. Default is 20km and there is no maximum, but need to be combined with limit. code is passed | [optional] [default to 20] |
| **limit** | **Integer**| Limit of the result. Default is 20 rows, and maximum is 50. | [optional] [default to 20] |
| **offset** | **Integer**| offset of the result set | [optional] [default to 0] |

### Return type

[**CitiesResponse**](CitiesResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **500** | The error message object |  -  |

<a id="getContinents"></a>
# **getContinents**
> ContinentsResponse getContinents(language, continentcode)

Search all continents or one specific continent

This webservice is providing you the ability to retrieve all informations about continents

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeographyApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mon-voyage-pas-cher.com");
    
    // Configure API key authorization: x-api-key
    ApiKeyAuth x-api-key = (ApiKeyAuth) defaultClient.getAuthentication("x-api-key");
    x-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //x-api-key.setApiKeyPrefix("Token");

    GeographyApisApi apiInstance = new GeographyApisApi(defaultClient);
    String language = "en"; // String | The language code of the language you want the content to be returned
    String continentcode = "continentcode_example"; // String | The code of the continent you want to retrieve, this parameter is not required if you want ot retrieve all continents at once
    try {
      ContinentsResponse result = apiInstance.getContinents(language, continentcode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeographyApisApi#getContinents");
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
| **language** | **String**| The language code of the language you want the content to be returned | [enum: en, fr, de, es] |
| **continentcode** | **String**| The code of the continent you want to retrieve, this parameter is not required if you want ot retrieve all continents at once | [optional] |

### Return type

[**ContinentsResponse**](ContinentsResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **500** | The error message object |  -  |

<a id="getCountries"></a>
# **getCountries**
> CountriesResponse getCountries(language, countrycode)

Search all countries or one specific country

This webservice is providing you the ability to retrieve a list of countries matching your search criterias.&lt;br /&gt;The 2 mains ways to search use this API are&lt;br /&gt;- by countrycode, it will only returns you one country&lt;br /&gt;- without the countrycode parameter which will return the full list of countries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeographyApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mon-voyage-pas-cher.com");
    
    // Configure API key authorization: x-api-key
    ApiKeyAuth x-api-key = (ApiKeyAuth) defaultClient.getAuthentication("x-api-key");
    x-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //x-api-key.setApiKeyPrefix("Token");

    GeographyApisApi apiInstance = new GeographyApisApi(defaultClient);
    String language = "en"; // String | the language code of the language you want the content to be returned
    String countrycode = "countrycode_example"; // String | The code of the country you want to retrieve
    try {
      CountriesResponse result = apiInstance.getCountries(language, countrycode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeographyApisApi#getCountries");
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
| **language** | **String**| the language code of the language you want the content to be returned | [enum: en, fr, de, es] |
| **countrycode** | **String**| The code of the country you want to retrieve | [optional] |

### Return type

[**CountriesResponse**](CountriesResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **500** | The error message object |  -  |

<a id="getSignificantCities"></a>
# **getSignificantCities**
> CitiesResponse getSignificantCities(language, sort, pourcent, countrycode, location, radius, limit, offset)

Search significant cities from lat/long or countrycode

Search cities according to given criterias. Either lat/long + radius or country code. A limit can be given but cannot exceed 50 results.&lt;br /&gt; A significant city will be defined according to the pourcent of population within a country.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeographyApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mon-voyage-pas-cher.com");
    
    // Configure API key authorization: x-api-key
    ApiKeyAuth x-api-key = (ApiKeyAuth) defaultClient.getAuthentication("x-api-key");
    x-api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //x-api-key.setApiKeyPrefix("Token");

    GeographyApisApi apiInstance = new GeographyApisApi(defaultClient);
    String language = "en"; // String | the language code of the language you want the content to be returned
    String sort = "distance,desc"; // String | The order you want the result ordered. Default is population while when entering a lat/long, you can order the results by distance from requested lat/long point
    BigDecimal pourcent = new BigDecimal("0.5"); // BigDecimal | The pourcent of population the cities need to be in order to appear in results
    String countrycode = "countrycode_example"; // String | if you want to limit the result to one country
    String location = "location_example"; // String | The Lat/Long of the location your are seeking cities ( ex. 45.4478988,3.23456)
    Integer radius = 20; // Integer | Radius in km for a lat/long search. Default is 20km and there is no maximum, but need to be combined with limit. code is passed
    Integer limit = 20; // Integer | Limit of the result. Default is 20 rows, and maximum is 50.
    Integer offset = 0; // Integer | offset of the result set
    try {
      CitiesResponse result = apiInstance.getSignificantCities(language, sort, pourcent, countrycode, location, radius, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeographyApisApi#getSignificantCities");
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
| **language** | **String**| the language code of the language you want the content to be returned | [enum: en, fr, de, es] |
| **sort** | **String**| The order you want the result ordered. Default is population while when entering a lat/long, you can order the results by distance from requested lat/long point | [default to population,desc] [enum: distance,desc, distance,asc, population,desc, population,asc, elevation,desc, elevation,asc, name,desc, name,asc, timezone,asc, timezone,desc] |
| **pourcent** | **BigDecimal**| The pourcent of population the cities need to be in order to appear in results | [optional] [default to 0.5] |
| **countrycode** | **String**| if you want to limit the result to one country | [optional] |
| **location** | **String**| The Lat/Long of the location your are seeking cities ( ex. 45.4478988,3.23456) | [optional] |
| **radius** | **Integer**| Radius in km for a lat/long search. Default is 20km and there is no maximum, but need to be combined with limit. code is passed | [optional] [default to 20] |
| **limit** | **Integer**| Limit of the result. Default is 20 rows, and maximum is 50. | [optional] [default to 20] |
| **offset** | **Integer**| offset of the result set | [optional] [default to 0] |

### Return type

[**CitiesResponse**](CitiesResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **500** | The error message object |  -  |

