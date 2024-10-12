# GeoApi

All URIs are relative to *https://wft-geo-db.p.rapidapi.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**findAdminDivisionsUsingGET**](GeoApi.md#findAdminDivisionsUsingGET) | **GET** /geo/adminDivisions | Find administrative divisions |
| [**findCitiesNearAdminDivisionUsingGET**](GeoApi.md#findCitiesNearAdminDivisionUsingGET) | **GET** /geo/adminDivisions/{divisionId}/nearbyCities | Find cities near division |
| [**findCitiesNearCityUsingGET**](GeoApi.md#findCitiesNearCityUsingGET) | **GET** /geo/cities/{cityId}/nearbyCities | Find cities near city |
| [**findCitiesNearLocationUsingGET**](GeoApi.md#findCitiesNearLocationUsingGET) | **GET** /geo/locations/{locationId}/nearbyCities | Find cities near location |
| [**findCitiesUsingGET**](GeoApi.md#findCitiesUsingGET) | **GET** /geo/cities | Find cities |
| [**findDivisionsNearAdminDivisionUsingGET**](GeoApi.md#findDivisionsNearAdminDivisionUsingGET) | **GET** /geo/adminDivisions/{divisionId}/nearbyDivisions | Find divisions near division |
| [**findDivisionsNearLocationUsingGET**](GeoApi.md#findDivisionsNearLocationUsingGET) | **GET** /geo/locations/{locationId}/nearbyDivisions | Find divisions near location |
| [**findRegionCitiesUsingGET**](GeoApi.md#findRegionCitiesUsingGET) | **GET** /geo/countries/{countryId}/regions/{regionCode}/cities | Find country region cities |
| [**findRegionDivisionsUsingGET**](GeoApi.md#findRegionDivisionsUsingGET) | **GET** /geo/countries/{countryId}/regions/{regionCode}/adminDivisions | Find country region administrative divisions |
| [**getAdminDivisionUsingGET**](GeoApi.md#getAdminDivisionUsingGET) | **GET** /geo/adminDivisions/{divisionId} | Get administrative division details |
| [**getCityDateTimeUsingGET**](GeoApi.md#getCityDateTimeUsingGET) | **GET** /geo/cities/{cityId}/dateTime | Get city date-time |
| [**getCityDistanceUsingGET**](GeoApi.md#getCityDistanceUsingGET) | **GET** /geo/cities/{cityId}/distance | Get city distance |
| [**getCityLocatedInUsingGET**](GeoApi.md#getCityLocatedInUsingGET) | **GET** /geo/cities/{cityId}/locatedIn | Get city admin region |
| [**getCityTimeUsingGET**](GeoApi.md#getCityTimeUsingGET) | **GET** /geo/cities/{cityId}/time | Get city time |
| [**getCityUsingGET**](GeoApi.md#getCityUsingGET) | **GET** /geo/cities/{cityId} | Get city details |
| [**getCountriesUsingGET**](GeoApi.md#getCountriesUsingGET) | **GET** /geo/countries | Find countries |
| [**getCountryUsingGET**](GeoApi.md#getCountryUsingGET) | **GET** /geo/countries/{countryId} | Get country details |
| [**getRegionUsingGET**](GeoApi.md#getRegionUsingGET) | **GET** /geo/countries/{countryId}/regions/{regionCode} | Get region details |
| [**getRegionsUsingGET**](GeoApi.md#getRegionsUsingGET) | **GET** /geo/countries/{countryId}/regions | Find country regions |


<a id="findAdminDivisionsUsingGET"></a>
# **findAdminDivisionsUsingGET**
> PopulatedPlacesResponse findAdminDivisionsUsingGET(location, radius, distanceUnit, countryIds, excludedCountryIds, minPopulation, maxPopulation, namePrefix, namePrefixDefaultLangResults, timeZoneIds, asciiMode, hateoasMode, languageCode, limit, offset, sort, includeDeleted)

Find administrative divisions

Find administrative divisions, filtering by optional criteria. If no criteria are set, you will get back all known divisions. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    GeoApi apiInstance = new GeoApi(defaultClient);
    String location = "location_example"; // String | Only places near this location. Latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD
    Integer radius = 56; // Integer | The location radius within which to find places
    String distanceUnit = "MI"; // String | The unit of distance: MI | KM
    String countryIds = "countryIds_example"; // String | Only places in these countries (comma-delimited country codes or WikiData ids)
    String excludedCountryIds = "excludedCountryIds_example"; // String | Only places NOT in these countries (comma-delimited country codes or WikiData ids)
    Integer minPopulation = 56; // Integer | Only places having at least this population
    Integer maxPopulation = 56; // Integer | Only places having no more than this population
    String namePrefix = "namePrefix_example"; // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    Boolean namePrefixDefaultLangResults = true; // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    String timeZoneIds = "timeZoneIds_example"; // String | Only places in these time-zones (comma-delimited)
    Boolean asciiMode = false; // Boolean | Display results using ASCII characters
    Boolean hateoasMode = true; // Boolean | Include HATEOAS-style links in results
    String languageCode = "languageCode_example"; // String | Display results in this language
    Integer limit = 10; // Integer | The maximum number of results to retrieve
    Integer offset = 0; // Integer | The zero-ary offset index into the results
    String sort = "sort_example"; // String | How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD = countryCode | elevation | name | population 
    String includeDeleted = "NONE"; // String | Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
    try {
      PopulatedPlacesResponse result = apiInstance.findAdminDivisionsUsingGET(location, radius, distanceUnit, countryIds, excludedCountryIds, minPopulation, maxPopulation, namePrefix, namePrefixDefaultLangResults, timeZoneIds, asciiMode, hateoasMode, languageCode, limit, offset, sort, includeDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoApi#findAdminDivisionsUsingGET");
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
| **location** | **String**| Only places near this location. Latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD | [optional] |
| **radius** | **Integer**| The location radius within which to find places | [optional] |
| **distanceUnit** | **String**| The unit of distance: MI | KM | [optional] [default to MI] |
| **countryIds** | **String**| Only places in these countries (comma-delimited country codes or WikiData ids) | [optional] |
| **excludedCountryIds** | **String**| Only places NOT in these countries (comma-delimited country codes or WikiData ids) | [optional] |
| **minPopulation** | **Integer**| Only places having at least this population | [optional] |
| **maxPopulation** | **Integer**| Only places having no more than this population | [optional] |
| **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] |
| **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true] |
| **timeZoneIds** | **String**| Only places in these time-zones (comma-delimited) | [optional] |
| **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false] |
| **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true] |
| **languageCode** | **String**| Display results in this language | [optional] |
| **limit** | **Integer**| The maximum number of results to retrieve | [optional] [default to 10] |
| **offset** | **Integer**| The zero-ary offset index into the results | [optional] [default to 0] |
| **sort** | **String**| How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population  | [optional] |
| **includeDeleted** | **String**| Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE | [optional] [default to NONE] |

### Return type

[**PopulatedPlacesResponse**](PopulatedPlacesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of populated places |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |

<a id="findCitiesNearAdminDivisionUsingGET"></a>
# **findCitiesNearAdminDivisionUsingGET**
> PopulatedPlacesResponse findCitiesNearAdminDivisionUsingGET(divisionId, radius, distanceUnit, countryIds, excludedCountryIds, minPopulation, maxPopulation, namePrefix, namePrefixDefaultLangResults, timeZoneIds, types, asciiMode, hateoasMode, languageCode, limit, offset, sort, includeDeleted)

Find cities near division

Find cities near the given administrative division, filtering by optional criteria. If no criteria are set, you will get back all known cities. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    GeoApi apiInstance = new GeoApi(defaultClient);
    String divisionId = "divisionId_example"; // String | An admin-division id (either native 'id' or 'wikiDataId')
    Integer radius = 56; // Integer | The location radius within which to find places
    String distanceUnit = "MI"; // String | The unit of distance: MI | KM
    String countryIds = "countryIds_example"; // String | Only places in these countries (comma-delimited country codes or WikiData ids)
    String excludedCountryIds = "excludedCountryIds_example"; // String | Only places NOT in these countries (comma-delimited country codes or WikiData ids)
    Integer minPopulation = 56; // Integer | Only places having at least this population
    Integer maxPopulation = 56; // Integer | Only places having no more than this population
    String namePrefix = "namePrefix_example"; // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    Boolean namePrefixDefaultLangResults = true; // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    String timeZoneIds = "timeZoneIds_example"; // String | Only places in these time-zones (comma-delimited)
    String types = "types_example"; // String | Only places for these types (comma-delimited): CITY | ADM2
    Boolean asciiMode = false; // Boolean | Display results using ASCII characters
    Boolean hateoasMode = true; // Boolean | Include HATEOAS-style links in results
    String languageCode = "languageCode_example"; // String | Display results in this language
    Integer limit = 10; // Integer | The maximum number of results to retrieve
    Integer offset = 0; // Integer | The zero-ary offset index into the results
    String sort = "sort_example"; // String | How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD = countryCode | elevation | name | population 
    String includeDeleted = "NONE"; // String | Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
    try {
      PopulatedPlacesResponse result = apiInstance.findCitiesNearAdminDivisionUsingGET(divisionId, radius, distanceUnit, countryIds, excludedCountryIds, minPopulation, maxPopulation, namePrefix, namePrefixDefaultLangResults, timeZoneIds, types, asciiMode, hateoasMode, languageCode, limit, offset, sort, includeDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoApi#findCitiesNearAdminDivisionUsingGET");
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
| **divisionId** | **String**| An admin-division id (either native &#39;id&#39; or &#39;wikiDataId&#39;) | |
| **radius** | **Integer**| The location radius within which to find places | [optional] |
| **distanceUnit** | **String**| The unit of distance: MI | KM | [optional] [default to MI] |
| **countryIds** | **String**| Only places in these countries (comma-delimited country codes or WikiData ids) | [optional] |
| **excludedCountryIds** | **String**| Only places NOT in these countries (comma-delimited country codes or WikiData ids) | [optional] |
| **minPopulation** | **Integer**| Only places having at least this population | [optional] |
| **maxPopulation** | **Integer**| Only places having no more than this population | [optional] |
| **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] |
| **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true] |
| **timeZoneIds** | **String**| Only places in these time-zones (comma-delimited) | [optional] |
| **types** | **String**| Only places for these types (comma-delimited): CITY | ADM2 | [optional] |
| **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false] |
| **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true] |
| **languageCode** | **String**| Display results in this language | [optional] |
| **limit** | **Integer**| The maximum number of results to retrieve | [optional] [default to 10] |
| **offset** | **Integer**| The zero-ary offset index into the results | [optional] [default to 0] |
| **sort** | **String**| How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population  | [optional] |
| **includeDeleted** | **String**| Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE | [optional] [default to NONE] |

### Return type

[**PopulatedPlacesResponse**](PopulatedPlacesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of populated places |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |
| **404** | 404 - Not Found |  -  |

<a id="findCitiesNearCityUsingGET"></a>
# **findCitiesNearCityUsingGET**
> PopulatedPlacesResponse findCitiesNearCityUsingGET(cityId, radius, distanceUnit, countryIds, excludedCountryIds, minPopulation, maxPopulation, namePrefix, namePrefixDefaultLangResults, timeZoneIds, types, asciiMode, hateoasMode, languageCode, limit, offset, sort, includeDeleted)

Find cities near city

Find cities near the given origin city, filtering by optional criteria. If no criteria are set, you will get back all known cities. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    GeoApi apiInstance = new GeoApi(defaultClient);
    String cityId = "cityId_example"; // String | A city id (either native 'id' or 'wikiDataId')
    Integer radius = 56; // Integer | The location radius within which to find places
    String distanceUnit = "MI"; // String | The unit of distance: MI | KM
    String countryIds = "countryIds_example"; // String | Only places in these countries (comma-delimited country codes or WikiData ids)
    String excludedCountryIds = "excludedCountryIds_example"; // String | Only places NOT in these countries (comma-delimited country codes or WikiData ids)
    Integer minPopulation = 56; // Integer | Only places having at least this population
    Integer maxPopulation = 56; // Integer | Only places having no more than this population
    String namePrefix = "namePrefix_example"; // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    Boolean namePrefixDefaultLangResults = true; // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    String timeZoneIds = "timeZoneIds_example"; // String | Only places in these time-zones (comma-delimited)
    String types = "types_example"; // String | Only places for these types (comma-delimited): CITY | ADM2
    Boolean asciiMode = false; // Boolean | Display results using ASCII characters
    Boolean hateoasMode = true; // Boolean | Include HATEOAS-style links in results
    String languageCode = "languageCode_example"; // String | Display results in this language
    Integer limit = 10; // Integer | The maximum number of results to retrieve
    Integer offset = 0; // Integer | The zero-ary offset index into the results
    String sort = "sort_example"; // String | How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD = countryCode | elevation | name | population 
    String includeDeleted = "NONE"; // String | Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
    try {
      PopulatedPlacesResponse result = apiInstance.findCitiesNearCityUsingGET(cityId, radius, distanceUnit, countryIds, excludedCountryIds, minPopulation, maxPopulation, namePrefix, namePrefixDefaultLangResults, timeZoneIds, types, asciiMode, hateoasMode, languageCode, limit, offset, sort, includeDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoApi#findCitiesNearCityUsingGET");
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
| **cityId** | **String**| A city id (either native &#39;id&#39; or &#39;wikiDataId&#39;) | |
| **radius** | **Integer**| The location radius within which to find places | [optional] |
| **distanceUnit** | **String**| The unit of distance: MI | KM | [optional] [default to MI] |
| **countryIds** | **String**| Only places in these countries (comma-delimited country codes or WikiData ids) | [optional] |
| **excludedCountryIds** | **String**| Only places NOT in these countries (comma-delimited country codes or WikiData ids) | [optional] |
| **minPopulation** | **Integer**| Only places having at least this population | [optional] |
| **maxPopulation** | **Integer**| Only places having no more than this population | [optional] |
| **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] |
| **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true] |
| **timeZoneIds** | **String**| Only places in these time-zones (comma-delimited) | [optional] |
| **types** | **String**| Only places for these types (comma-delimited): CITY | ADM2 | [optional] |
| **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false] |
| **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true] |
| **languageCode** | **String**| Display results in this language | [optional] |
| **limit** | **Integer**| The maximum number of results to retrieve | [optional] [default to 10] |
| **offset** | **Integer**| The zero-ary offset index into the results | [optional] [default to 0] |
| **sort** | **String**| How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population  | [optional] |
| **includeDeleted** | **String**| Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE | [optional] [default to NONE] |

### Return type

[**PopulatedPlacesResponse**](PopulatedPlacesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of populated places |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |
| **404** | 404 - Not Found |  -  |

<a id="findCitiesNearLocationUsingGET"></a>
# **findCitiesNearLocationUsingGET**
> PopulatedPlacesResponse findCitiesNearLocationUsingGET(locationId, radius, distanceUnit, countryIds, excludedCountryIds, minPopulation, maxPopulation, namePrefix, namePrefixDefaultLangResults, timeZoneIds, types, asciiMode, hateoasMode, languageCode, limit, offset, sort, includeDeleted)

Find cities near location

Find cities near the given location, filtering by optional criteria. If no criteria are set, you will get back all known cities. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    GeoApi apiInstance = new GeoApi(defaultClient);
    String locationId = "locationId_example"; // String | A latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD
    Integer radius = 56; // Integer | The location radius within which to find places
    String distanceUnit = "MI"; // String | The unit of distance: MI | KM
    String countryIds = "countryIds_example"; // String | Only places in these countries (comma-delimited country codes or WikiData ids)
    String excludedCountryIds = "excludedCountryIds_example"; // String | Only places NOT in these countries (comma-delimited country codes or WikiData ids)
    Integer minPopulation = 56; // Integer | Only places having at least this population
    Integer maxPopulation = 56; // Integer | Only places having no more than this population
    String namePrefix = "namePrefix_example"; // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    Boolean namePrefixDefaultLangResults = true; // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    String timeZoneIds = "timeZoneIds_example"; // String | Only places in these time-zones (comma-delimited)
    String types = "types_example"; // String | Only places for these types (comma-delimited): CITY | ADM2
    Boolean asciiMode = false; // Boolean | Display results using ASCII characters
    Boolean hateoasMode = true; // Boolean | Include HATEOAS-style links in results
    String languageCode = "languageCode_example"; // String | Display results in this language
    Integer limit = 10; // Integer | The maximum number of results to retrieve
    Integer offset = 0; // Integer | The zero-ary offset index into the results
    String sort = "sort_example"; // String | How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD = countryCode | elevation | name | population 
    String includeDeleted = "NONE"; // String | Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
    try {
      PopulatedPlacesResponse result = apiInstance.findCitiesNearLocationUsingGET(locationId, radius, distanceUnit, countryIds, excludedCountryIds, minPopulation, maxPopulation, namePrefix, namePrefixDefaultLangResults, timeZoneIds, types, asciiMode, hateoasMode, languageCode, limit, offset, sort, includeDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoApi#findCitiesNearLocationUsingGET");
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
| **locationId** | **String**| A latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD | |
| **radius** | **Integer**| The location radius within which to find places | [optional] |
| **distanceUnit** | **String**| The unit of distance: MI | KM | [optional] [default to MI] |
| **countryIds** | **String**| Only places in these countries (comma-delimited country codes or WikiData ids) | [optional] |
| **excludedCountryIds** | **String**| Only places NOT in these countries (comma-delimited country codes or WikiData ids) | [optional] |
| **minPopulation** | **Integer**| Only places having at least this population | [optional] |
| **maxPopulation** | **Integer**| Only places having no more than this population | [optional] |
| **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] |
| **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true] |
| **timeZoneIds** | **String**| Only places in these time-zones (comma-delimited) | [optional] |
| **types** | **String**| Only places for these types (comma-delimited): CITY | ADM2 | [optional] |
| **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false] |
| **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true] |
| **languageCode** | **String**| Display results in this language | [optional] |
| **limit** | **Integer**| The maximum number of results to retrieve | [optional] [default to 10] |
| **offset** | **Integer**| The zero-ary offset index into the results | [optional] [default to 0] |
| **sort** | **String**| How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population  | [optional] |
| **includeDeleted** | **String**| Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE | [optional] [default to NONE] |

### Return type

[**PopulatedPlacesResponse**](PopulatedPlacesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of populated places |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |

<a id="findCitiesUsingGET"></a>
# **findCitiesUsingGET**
> PopulatedPlacesResponse findCitiesUsingGET(location, radius, distanceUnit, countryIds, excludedCountryIds, minPopulation, maxPopulation, namePrefix, namePrefixDefaultLangResults, timeZoneIds, types, asciiMode, hateoasMode, languageCode, limit, offset, sort, includeDeleted)

Find cities

Find cities, filtering by optional criteria. If no criteria are set, you will get back all known cities. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    GeoApi apiInstance = new GeoApi(defaultClient);
    String location = "location_example"; // String | Only places near this location. Latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD
    Integer radius = 56; // Integer | The location radius within which to find places
    String distanceUnit = "MI"; // String | The unit of distance: MI | KM
    String countryIds = "countryIds_example"; // String | Only places in these countries (comma-delimited country codes or WikiData ids)
    String excludedCountryIds = "excludedCountryIds_example"; // String | Only places NOT in these countries (comma-delimited country codes or WikiData ids)
    Integer minPopulation = 56; // Integer | Only places having at least this population
    Integer maxPopulation = 56; // Integer | Only places having no more than this population
    String namePrefix = "namePrefix_example"; // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    Boolean namePrefixDefaultLangResults = true; // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    String timeZoneIds = "timeZoneIds_example"; // String | Only places in these time-zones (comma-delimited)
    String types = "types_example"; // String | Only places for these types (comma-delimited): CITY | ADM2
    Boolean asciiMode = false; // Boolean | Display results using ASCII characters
    Boolean hateoasMode = true; // Boolean | Include HATEOAS-style links in results
    String languageCode = "languageCode_example"; // String | Display results in this language
    Integer limit = 10; // Integer | The maximum number of results to retrieve
    Integer offset = 0; // Integer | The zero-ary offset index into the results
    String sort = "sort_example"; // String | How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD = countryCode | elevation | name | population 
    String includeDeleted = "NONE"; // String | Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
    try {
      PopulatedPlacesResponse result = apiInstance.findCitiesUsingGET(location, radius, distanceUnit, countryIds, excludedCountryIds, minPopulation, maxPopulation, namePrefix, namePrefixDefaultLangResults, timeZoneIds, types, asciiMode, hateoasMode, languageCode, limit, offset, sort, includeDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoApi#findCitiesUsingGET");
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
| **location** | **String**| Only places near this location. Latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD | [optional] |
| **radius** | **Integer**| The location radius within which to find places | [optional] |
| **distanceUnit** | **String**| The unit of distance: MI | KM | [optional] [default to MI] |
| **countryIds** | **String**| Only places in these countries (comma-delimited country codes or WikiData ids) | [optional] |
| **excludedCountryIds** | **String**| Only places NOT in these countries (comma-delimited country codes or WikiData ids) | [optional] |
| **minPopulation** | **Integer**| Only places having at least this population | [optional] |
| **maxPopulation** | **Integer**| Only places having no more than this population | [optional] |
| **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] |
| **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true] |
| **timeZoneIds** | **String**| Only places in these time-zones (comma-delimited) | [optional] |
| **types** | **String**| Only places for these types (comma-delimited): CITY | ADM2 | [optional] |
| **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false] |
| **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true] |
| **languageCode** | **String**| Display results in this language | [optional] |
| **limit** | **Integer**| The maximum number of results to retrieve | [optional] [default to 10] |
| **offset** | **Integer**| The zero-ary offset index into the results | [optional] [default to 0] |
| **sort** | **String**| How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population  | [optional] |
| **includeDeleted** | **String**| Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE | [optional] [default to NONE] |

### Return type

[**PopulatedPlacesResponse**](PopulatedPlacesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of populated places |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |

<a id="findDivisionsNearAdminDivisionUsingGET"></a>
# **findDivisionsNearAdminDivisionUsingGET**
> PopulatedPlacesResponse findDivisionsNearAdminDivisionUsingGET(divisionId, radius, distanceUnit, countryIds, excludedCountryIds, minPopulation, maxPopulation, namePrefix, namePrefixDefaultLangResults, timeZoneIds, asciiMode, hateoasMode, languageCode, limit, offset, sort, includeDeleted)

Find divisions near division

Find administrative divisions near the given origin division, filtering by optional criteria. If no criteria are set, you will get back all known divisions. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    GeoApi apiInstance = new GeoApi(defaultClient);
    String divisionId = "divisionId_example"; // String | An admin-division id (either native 'id' or 'wikiDataId')
    Integer radius = 56; // Integer | The location radius within which to find places
    String distanceUnit = "MI"; // String | The unit of distance: MI | KM
    String countryIds = "countryIds_example"; // String | Only places in these countries (comma-delimited country codes or WikiData ids)
    String excludedCountryIds = "excludedCountryIds_example"; // String | Only places NOT in these countries (comma-delimited country codes or WikiData ids)
    Integer minPopulation = 56; // Integer | Only places having at least this population
    Integer maxPopulation = 56; // Integer | Only places having no more than this population
    String namePrefix = "namePrefix_example"; // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    Boolean namePrefixDefaultLangResults = true; // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    String timeZoneIds = "timeZoneIds_example"; // String | Only places in these time-zones (comma-delimited)
    Boolean asciiMode = false; // Boolean | Display results using ASCII characters
    Boolean hateoasMode = true; // Boolean | Include HATEOAS-style links in results
    String languageCode = "languageCode_example"; // String | Display results in this language
    Integer limit = 10; // Integer | The maximum number of results to retrieve
    Integer offset = 0; // Integer | The zero-ary offset index into the results
    String sort = "sort_example"; // String | How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD = countryCode | elevation | name | population 
    String includeDeleted = "NONE"; // String | Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
    try {
      PopulatedPlacesResponse result = apiInstance.findDivisionsNearAdminDivisionUsingGET(divisionId, radius, distanceUnit, countryIds, excludedCountryIds, minPopulation, maxPopulation, namePrefix, namePrefixDefaultLangResults, timeZoneIds, asciiMode, hateoasMode, languageCode, limit, offset, sort, includeDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoApi#findDivisionsNearAdminDivisionUsingGET");
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
| **divisionId** | **String**| An admin-division id (either native &#39;id&#39; or &#39;wikiDataId&#39;) | |
| **radius** | **Integer**| The location radius within which to find places | [optional] |
| **distanceUnit** | **String**| The unit of distance: MI | KM | [optional] [default to MI] |
| **countryIds** | **String**| Only places in these countries (comma-delimited country codes or WikiData ids) | [optional] |
| **excludedCountryIds** | **String**| Only places NOT in these countries (comma-delimited country codes or WikiData ids) | [optional] |
| **minPopulation** | **Integer**| Only places having at least this population | [optional] |
| **maxPopulation** | **Integer**| Only places having no more than this population | [optional] |
| **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] |
| **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true] |
| **timeZoneIds** | **String**| Only places in these time-zones (comma-delimited) | [optional] |
| **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false] |
| **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true] |
| **languageCode** | **String**| Display results in this language | [optional] |
| **limit** | **Integer**| The maximum number of results to retrieve | [optional] [default to 10] |
| **offset** | **Integer**| The zero-ary offset index into the results | [optional] [default to 0] |
| **sort** | **String**| How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population  | [optional] |
| **includeDeleted** | **String**| Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE | [optional] [default to NONE] |

### Return type

[**PopulatedPlacesResponse**](PopulatedPlacesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of populated places |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |
| **404** | 404 - Not Found |  -  |

<a id="findDivisionsNearLocationUsingGET"></a>
# **findDivisionsNearLocationUsingGET**
> PopulatedPlacesResponse findDivisionsNearLocationUsingGET(locationId, radius, distanceUnit, countryIds, excludedCountryIds, minPopulation, maxPopulation, namePrefix, namePrefixDefaultLangResults, timeZoneIds, asciiMode, hateoasMode, languageCode, limit, offset, sort, includeDeleted)

Find divisions near location

Find administrative divisions near the given location, filtering by optional criteria. If no criteria are set, you will get back all known divisions. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    GeoApi apiInstance = new GeoApi(defaultClient);
    String locationId = "locationId_example"; // String | A latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD
    Integer radius = 56; // Integer | The location radius within which to find places
    String distanceUnit = "MI"; // String | The unit of distance: MI | KM
    String countryIds = "countryIds_example"; // String | Only places in these countries (comma-delimited country codes or WikiData ids)
    String excludedCountryIds = "excludedCountryIds_example"; // String | Only places NOT in these countries (comma-delimited country codes or WikiData ids)
    Integer minPopulation = 56; // Integer | Only places having at least this population
    Integer maxPopulation = 56; // Integer | Only places having no more than this population
    String namePrefix = "namePrefix_example"; // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    Boolean namePrefixDefaultLangResults = true; // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    String timeZoneIds = "timeZoneIds_example"; // String | Only places in these time-zones (comma-delimited)
    Boolean asciiMode = false; // Boolean | Display results using ASCII characters
    Boolean hateoasMode = true; // Boolean | Include HATEOAS-style links in results
    String languageCode = "languageCode_example"; // String | Display results in this language
    Integer limit = 10; // Integer | The maximum number of results to retrieve
    Integer offset = 0; // Integer | The zero-ary offset index into the results
    String sort = "sort_example"; // String | How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD = countryCode | elevation | name | population 
    String includeDeleted = "NONE"; // String | Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
    try {
      PopulatedPlacesResponse result = apiInstance.findDivisionsNearLocationUsingGET(locationId, radius, distanceUnit, countryIds, excludedCountryIds, minPopulation, maxPopulation, namePrefix, namePrefixDefaultLangResults, timeZoneIds, asciiMode, hateoasMode, languageCode, limit, offset, sort, includeDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoApi#findDivisionsNearLocationUsingGET");
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
| **locationId** | **String**| A latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD | |
| **radius** | **Integer**| The location radius within which to find places | [optional] |
| **distanceUnit** | **String**| The unit of distance: MI | KM | [optional] [default to MI] |
| **countryIds** | **String**| Only places in these countries (comma-delimited country codes or WikiData ids) | [optional] |
| **excludedCountryIds** | **String**| Only places NOT in these countries (comma-delimited country codes or WikiData ids) | [optional] |
| **minPopulation** | **Integer**| Only places having at least this population | [optional] |
| **maxPopulation** | **Integer**| Only places having no more than this population | [optional] |
| **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] |
| **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true] |
| **timeZoneIds** | **String**| Only places in these time-zones (comma-delimited) | [optional] |
| **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false] |
| **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true] |
| **languageCode** | **String**| Display results in this language | [optional] |
| **limit** | **Integer**| The maximum number of results to retrieve | [optional] [default to 10] |
| **offset** | **Integer**| The zero-ary offset index into the results | [optional] [default to 0] |
| **sort** | **String**| How to sort places.  Format: ±SORT_FIELD,±SORT_FIELD  where SORT_FIELD &#x3D; countryCode | elevation | name | population  | [optional] |
| **includeDeleted** | **String**| Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE | [optional] [default to NONE] |

### Return type

[**PopulatedPlacesResponse**](PopulatedPlacesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of populated places |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |

<a id="findRegionCitiesUsingGET"></a>
# **findRegionCitiesUsingGET**
> PopulatedPlacesResponse findRegionCitiesUsingGET(countryId, regionCode, minPopulation, maxPopulation, namePrefix, namePrefixDefaultLangResults, timeZoneIds, types, asciiMode, hateoasMode, languageCode, limit, offset, sort, includeDeleted)

Find country region cities

Get the cities in a specific country region. The country and region info is omitted in the response. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    GeoApi apiInstance = new GeoApi(defaultClient);
    String countryId = "countryId_example"; // String | An ISO-3166 country code or WikiData id
    String regionCode = "regionCode_example"; // String | An ISO-3166 or FIPS region code
    Integer minPopulation = 56; // Integer | Only places having at least this population
    Integer maxPopulation = 56; // Integer | Only places having no more than this population
    String namePrefix = "namePrefix_example"; // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    Boolean namePrefixDefaultLangResults = true; // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    String timeZoneIds = "timeZoneIds_example"; // String | Only places in these time-zones (comma-delimited)
    String types = "types_example"; // String | Only places for these types (comma-delimited): CITY | ADM2
    Boolean asciiMode = false; // Boolean | Display results using ASCII characters
    Boolean hateoasMode = true; // Boolean | Include HATEOAS-style links in results
    String languageCode = "languageCode_example"; // String | Display results in this language
    Integer limit = 10; // Integer | The maximum number of results to retrieve
    Integer offset = 0; // Integer | The zero-ary offset index into the results
    String sort = "sort_example"; // String | How to sort place results.  'Format: ±SORT_FIELD,±SORT_FIELD'  where SORT_FIELD = elevation | name | population 
    String includeDeleted = "NONE"; // String | Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
    try {
      PopulatedPlacesResponse result = apiInstance.findRegionCitiesUsingGET(countryId, regionCode, minPopulation, maxPopulation, namePrefix, namePrefixDefaultLangResults, timeZoneIds, types, asciiMode, hateoasMode, languageCode, limit, offset, sort, includeDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoApi#findRegionCitiesUsingGET");
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
| **countryId** | **String**| An ISO-3166 country code or WikiData id | |
| **regionCode** | **String**| An ISO-3166 or FIPS region code | |
| **minPopulation** | **Integer**| Only places having at least this population | [optional] |
| **maxPopulation** | **Integer**| Only places having no more than this population | [optional] |
| **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] |
| **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true] |
| **timeZoneIds** | **String**| Only places in these time-zones (comma-delimited) | [optional] |
| **types** | **String**| Only places for these types (comma-delimited): CITY | ADM2 | [optional] |
| **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false] |
| **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true] |
| **languageCode** | **String**| Display results in this language | [optional] |
| **limit** | **Integer**| The maximum number of results to retrieve | [optional] [default to 10] |
| **offset** | **Integer**| The zero-ary offset index into the results | [optional] [default to 0] |
| **sort** | **String**| How to sort place results.  &#39;Format: ±SORT_FIELD,±SORT_FIELD&#39;  where SORT_FIELD &#x3D; elevation | name | population  | [optional] |
| **includeDeleted** | **String**| Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE | [optional] [default to NONE] |

### Return type

[**PopulatedPlacesResponse**](PopulatedPlacesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of populated places |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |
| **404** | 404 - Not Found |  -  |

<a id="findRegionDivisionsUsingGET"></a>
# **findRegionDivisionsUsingGET**
> PopulatedPlacesResponse findRegionDivisionsUsingGET(countryId, regionCode, minPopulation, maxPopulation, namePrefix, namePrefixDefaultLangResults, timeZoneIds, asciiMode, hateoasMode, languageCode, limit, offset, sort, includeDeleted)

Find country region administrative divisions

Get the administrative divisions in a specific country region. The country and region info is omitted in the response. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    GeoApi apiInstance = new GeoApi(defaultClient);
    String countryId = "countryId_example"; // String | An ISO-3166 country code or WikiData id
    String regionCode = "regionCode_example"; // String | An ISO-3166 or FIPS region code
    Integer minPopulation = 56; // Integer | Only places having at least this population
    Integer maxPopulation = 56; // Integer | Only places having no more than this population
    String namePrefix = "namePrefix_example"; // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    Boolean namePrefixDefaultLangResults = true; // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    String timeZoneIds = "timeZoneIds_example"; // String | Only places in these time-zones (comma-delimited)
    Boolean asciiMode = false; // Boolean | Display results using ASCII characters
    Boolean hateoasMode = true; // Boolean | Include HATEOAS-style links in results
    String languageCode = "languageCode_example"; // String | Display results in this language
    Integer limit = 10; // Integer | The maximum number of results to retrieve
    Integer offset = 0; // Integer | The zero-ary offset index into the results
    String sort = "sort_example"; // String | How to sort place results.  'Format: ±SORT_FIELD,±SORT_FIELD'  where SORT_FIELD = elevation | name | population 
    String includeDeleted = "NONE"; // String | Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE
    try {
      PopulatedPlacesResponse result = apiInstance.findRegionDivisionsUsingGET(countryId, regionCode, minPopulation, maxPopulation, namePrefix, namePrefixDefaultLangResults, timeZoneIds, asciiMode, hateoasMode, languageCode, limit, offset, sort, includeDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoApi#findRegionDivisionsUsingGET");
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
| **countryId** | **String**| An ISO-3166 country code or WikiData id | |
| **regionCode** | **String**| An ISO-3166 or FIPS region code | |
| **minPopulation** | **Integer**| Only places having at least this population | [optional] |
| **maxPopulation** | **Integer**| Only places having no more than this population | [optional] |
| **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] |
| **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true] |
| **timeZoneIds** | **String**| Only places in these time-zones (comma-delimited) | [optional] |
| **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false] |
| **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true] |
| **languageCode** | **String**| Display results in this language | [optional] |
| **limit** | **Integer**| The maximum number of results to retrieve | [optional] [default to 10] |
| **offset** | **Integer**| The zero-ary offset index into the results | [optional] [default to 0] |
| **sort** | **String**| How to sort place results.  &#39;Format: ±SORT_FIELD,±SORT_FIELD&#39;  where SORT_FIELD &#x3D; elevation | name | population  | [optional] |
| **includeDeleted** | **String**| Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE | [optional] [default to NONE] |

### Return type

[**PopulatedPlacesResponse**](PopulatedPlacesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of populated places |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |
| **404** | 404 - Not Found |  -  |

<a id="getAdminDivisionUsingGET"></a>
# **getAdminDivisionUsingGET**
> PopulatedPlaceResponse getAdminDivisionUsingGET(divisionId, asciiMode, languageCode)

Get administrative division details

Get the details for a specific administrative division, including location coordinates, population, and elevation above sea-level (if available). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    GeoApi apiInstance = new GeoApi(defaultClient);
    String divisionId = "divisionId_example"; // String | An admin-division id (either native 'id' or 'wikiDataId')
    Boolean asciiMode = false; // Boolean | Display results using ASCII characters
    String languageCode = "languageCode_example"; // String | Display results in this language
    try {
      PopulatedPlaceResponse result = apiInstance.getAdminDivisionUsingGET(divisionId, asciiMode, languageCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoApi#getAdminDivisionUsingGET");
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
| **divisionId** | **String**| An admin-division id (either native &#39;id&#39; or &#39;wikiDataId&#39;) | |
| **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false] |
| **languageCode** | **String**| Display results in this language | [optional] |

### Return type

[**PopulatedPlaceResponse**](PopulatedPlaceResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Populated-place details |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |
| **404** | 404 - Not Found |  -  |

<a id="getCityDateTimeUsingGET"></a>
# **getCityDateTimeUsingGET**
> DateTimeResponse getCityDateTimeUsingGET(cityId)

Get city date-time

Get city date-time

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    GeoApi apiInstance = new GeoApi(defaultClient);
    String cityId = "cityId_example"; // String | A city id (either native 'id' or 'wikiDataId')
    try {
      DateTimeResponse result = apiInstance.getCityDateTimeUsingGET(cityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoApi#getCityDateTimeUsingGET");
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
| **cityId** | **String**| A city id (either native &#39;id&#39; or &#39;wikiDataId&#39;) | |

### Return type

[**DateTimeResponse**](DateTimeResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An ISO-6801 date-time |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |
| **404** | 404 - Not Found |  -  |

<a id="getCityDistanceUsingGET"></a>
# **getCityDistanceUsingGET**
> DistanceResponse getCityDistanceUsingGET(cityId, toCityId, distanceUnit)

Get city distance

Get distance from the given city

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    GeoApi apiInstance = new GeoApi(defaultClient);
    String cityId = "cityId_example"; // String | A city id (either native 'id' or 'wikiDataId')
    String toCityId = "toCityId_example"; // String | Distance to this city
    String distanceUnit = "MI"; // String | The unit of distance: MI | KM
    try {
      DistanceResponse result = apiInstance.getCityDistanceUsingGET(cityId, toCityId, distanceUnit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoApi#getCityDistanceUsingGET");
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
| **cityId** | **String**| A city id (either native &#39;id&#39; or &#39;wikiDataId&#39;) | |
| **toCityId** | **String**| Distance to this city | |
| **distanceUnit** | **String**| The unit of distance: MI | KM | [optional] [default to MI] |

### Return type

[**DistanceResponse**](DistanceResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A decimal distance (in miles or kilometers) |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |
| **404** | 404 - Not Found |  -  |

<a id="getCityLocatedInUsingGET"></a>
# **getCityLocatedInUsingGET**
> PopulatedPlaceResponse getCityLocatedInUsingGET(cityId, asciiMode, languageCode)

Get city admin region

Get the details for the containing populated place (e.g., its county or other administrative division), including location coordinates, population, and elevation above sea-level (if available). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    GeoApi apiInstance = new GeoApi(defaultClient);
    String cityId = "cityId_example"; // String | A city id (either native 'id' or 'wikiDataId')
    Boolean asciiMode = false; // Boolean | Display results using ASCII characters
    String languageCode = "languageCode_example"; // String | Display results in this language
    try {
      PopulatedPlaceResponse result = apiInstance.getCityLocatedInUsingGET(cityId, asciiMode, languageCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoApi#getCityLocatedInUsingGET");
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
| **cityId** | **String**| A city id (either native &#39;id&#39; or &#39;wikiDataId&#39;) | |
| **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false] |
| **languageCode** | **String**| Display results in this language | [optional] |

### Return type

[**PopulatedPlaceResponse**](PopulatedPlaceResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Populated-place details |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |
| **404** | 404 - Not Found |  -  |

<a id="getCityTimeUsingGET"></a>
# **getCityTimeUsingGET**
> TimeResponse getCityTimeUsingGET(cityId)

Get city time

Get city time

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    GeoApi apiInstance = new GeoApi(defaultClient);
    String cityId = "cityId_example"; // String | A city id (either native 'id' or 'wikiDataId')
    try {
      TimeResponse result = apiInstance.getCityTimeUsingGET(cityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoApi#getCityTimeUsingGET");
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
| **cityId** | **String**| A city id (either native &#39;id&#39; or &#39;wikiDataId&#39;) | |

### Return type

[**TimeResponse**](TimeResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An ISO-8601 time response |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |
| **404** | 404 - Not Found |  -  |

<a id="getCityUsingGET"></a>
# **getCityUsingGET**
> PopulatedPlaceResponse getCityUsingGET(cityId, asciiMode, languageCode)

Get city details

Get the details for a specific city, including location coordinates, population, and elevation above sea-level (if available). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    GeoApi apiInstance = new GeoApi(defaultClient);
    String cityId = "cityId_example"; // String | A city id (either native 'id' or 'wikiDataId')
    Boolean asciiMode = false; // Boolean | Display results using ASCII characters
    String languageCode = "languageCode_example"; // String | Display results in this language
    try {
      PopulatedPlaceResponse result = apiInstance.getCityUsingGET(cityId, asciiMode, languageCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoApi#getCityUsingGET");
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
| **cityId** | **String**| A city id (either native &#39;id&#39; or &#39;wikiDataId&#39;) | |
| **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false] |
| **languageCode** | **String**| Display results in this language | [optional] |

### Return type

[**PopulatedPlaceResponse**](PopulatedPlaceResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Populated-place details |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |
| **404** | 404 - Not Found |  -  |

<a id="getCountriesUsingGET"></a>
# **getCountriesUsingGET**
> CountriesResponse getCountriesUsingGET(currencyCode, namePrefix, namePrefixDefaultLangResults, asciiMode, hateoasMode, languageCode, limit, offset, sort)

Find countries

Find countries, filtering by optional criteria. If no criteria are set, you will get back all known countries. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    GeoApi apiInstance = new GeoApi(defaultClient);
    String currencyCode = "currencyCode_example"; // String | Only countries supporting this currency
    String namePrefix = "namePrefix_example"; // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    Boolean namePrefixDefaultLangResults = true; // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    Boolean asciiMode = false; // Boolean | Display results using ASCII characters
    Boolean hateoasMode = true; // Boolean | Include HATEOAS-style links in results
    String languageCode = "languageCode_example"; // String | Display results in this language
    Integer limit = 10; // Integer | The maximum number of results to retrieve
    Integer offset = 0; // Integer | The zero-ary offset index into the results
    String sort = "sort_example"; // String | How to sort countries.  Format: ±SORT_FIELD  where SORT_FIELD = code | name
    try {
      CountriesResponse result = apiInstance.getCountriesUsingGET(currencyCode, namePrefix, namePrefixDefaultLangResults, asciiMode, hateoasMode, languageCode, limit, offset, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoApi#getCountriesUsingGET");
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
| **currencyCode** | **String**| Only countries supporting this currency | [optional] |
| **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] |
| **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true] |
| **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false] |
| **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true] |
| **languageCode** | **String**| Display results in this language | [optional] |
| **limit** | **Integer**| The maximum number of results to retrieve | [optional] [default to 10] |
| **offset** | **Integer**| The zero-ary offset index into the results | [optional] [default to 0] |
| **sort** | **String**| How to sort countries.  Format: ±SORT_FIELD  where SORT_FIELD &#x3D; code | name | [optional] |

### Return type

[**CountriesResponse**](CountriesResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of countries |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |

<a id="getCountryUsingGET"></a>
# **getCountryUsingGET**
> CountryResponse getCountryUsingGET(countryId, asciiMode, languageCode)

Get country details

Get the details for a specific country, including number of regions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    GeoApi apiInstance = new GeoApi(defaultClient);
    String countryId = "countryId_example"; // String | An ISO-3166 country code or WikiData id
    Boolean asciiMode = false; // Boolean | Display results using ASCII characters
    String languageCode = "languageCode_example"; // String | Display results in this language
    try {
      CountryResponse result = apiInstance.getCountryUsingGET(countryId, asciiMode, languageCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoApi#getCountryUsingGET");
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
| **countryId** | **String**| An ISO-3166 country code or WikiData id | |
| **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false] |
| **languageCode** | **String**| Display results in this language | [optional] |

### Return type

[**CountryResponse**](CountryResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Country detail |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |
| **404** | 404 - Not Found |  -  |

<a id="getRegionUsingGET"></a>
# **getRegionUsingGET**
> RegionResponse getRegionUsingGET(countryId, regionCode, asciiMode, languageCode)

Get region details

Get the details of a specific country region, including number of cities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    GeoApi apiInstance = new GeoApi(defaultClient);
    String countryId = "countryId_example"; // String | An ISO-3166 country code or WikiData id
    String regionCode = "regionCode_example"; // String | An ISO-3166 or FIPS region code
    Boolean asciiMode = false; // Boolean | Display results using ASCII characters
    String languageCode = "languageCode_example"; // String | Display results in this language
    try {
      RegionResponse result = apiInstance.getRegionUsingGET(countryId, regionCode, asciiMode, languageCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoApi#getRegionUsingGET");
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
| **countryId** | **String**| An ISO-3166 country code or WikiData id | |
| **regionCode** | **String**| An ISO-3166 or FIPS region code | |
| **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false] |
| **languageCode** | **String**| Display results in this language | [optional] |

### Return type

[**RegionResponse**](RegionResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Country region details |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |
| **404** | 404 - Not Found |  -  |

<a id="getRegionsUsingGET"></a>
# **getRegionsUsingGET**
> RegionsResponse getRegionsUsingGET(countryId, namePrefix, namePrefixDefaultLangResults, asciiMode, hateoasMode, languageCode, limit, offset, sort)

Find country regions

Get all regions in a specific country. These could be states, provinces, districts, or otherwise major political divisions. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wft-geo-db.p.rapidapi.com/v1");
    
    // Configure API key authorization: UserSecurity
    ApiKeyAuth UserSecurity = (ApiKeyAuth) defaultClient.getAuthentication("UserSecurity");
    UserSecurity.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //UserSecurity.setApiKeyPrefix("Token");

    GeoApi apiInstance = new GeoApi(defaultClient);
    String countryId = "countryId_example"; // String | An ISO-3166 country code or WikiData id
    String namePrefix = "namePrefix_example"; // String | Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language. 
    Boolean namePrefixDefaultLangResults = true; // Boolean | When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set. 
    Boolean asciiMode = false; // Boolean | Display results using ASCII characters
    Boolean hateoasMode = true; // Boolean | Include HATEOAS-style links in results
    String languageCode = "languageCode_example"; // String | Display results in this language
    Integer limit = 10; // Integer | The maximum number of results to retrieve
    Integer offset = 0; // Integer | The zero-ary offset index into the results
    String sort = "sort_example"; // String | How to sort regions.  Format: ±SORT_FIELD  where SORT_FIELD = fipsCode | isoCode | name
    try {
      RegionsResponse result = apiInstance.getRegionsUsingGET(countryId, namePrefix, namePrefixDefaultLangResults, asciiMode, hateoasMode, languageCode, limit, offset, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeoApi#getRegionsUsingGET");
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
| **countryId** | **String**| An ISO-3166 country code or WikiData id | |
| **namePrefix** | **String**| Only entities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.  | [optional] |
| **namePrefixDefaultLangResults** | **Boolean**| When name-prefix matching, whether or not to match on names in the default language if a non-default languageCode is set.  | [optional] [default to true] |
| **asciiMode** | **Boolean**| Display results using ASCII characters | [optional] [default to false] |
| **hateoasMode** | **Boolean**| Include HATEOAS-style links in results | [optional] [default to true] |
| **languageCode** | **String**| Display results in this language | [optional] |
| **limit** | **Integer**| The maximum number of results to retrieve | [optional] [default to 10] |
| **offset** | **Integer**| The zero-ary offset index into the results | [optional] [default to 0] |
| **sort** | **String**| How to sort regions.  Format: ±SORT_FIELD  where SORT_FIELD &#x3D; fipsCode | isoCode | name | [optional] |

### Return type

[**RegionsResponse**](RegionsResponse.md)

### Authorization

[UserSecurity](../README.md#UserSecurity)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of country regions |  -  |
| **400** | 400 - Bad Request |  -  |
| **401** | 401 - Unauthorized |  -  |
| **403** | 403 - Forbidden |  -  |
| **404** | 404 - Not Found |  -  |

