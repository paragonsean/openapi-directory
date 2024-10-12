# RvSearchApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listingRvIdExtraGet**](RvSearchApi.md#listingRvIdExtraGet) | **GET** /listing/rv/{id}/extra | Long text RV Listings attributes for Listing with the given id |
| [**listingRvIdGet**](RvSearchApi.md#listingRvIdGet) | **GET** /listing/rv/{id} | RV listing by id |
| [**listingRvIdMediaGet**](RvSearchApi.md#listingRvIdMediaGet) | **GET** /listing/rv/{id}/media | Listing media by id |
| [**listingRvUkIdExtraGet**](RvSearchApi.md#listingRvUkIdExtraGet) | **GET** /listing/rv/uk/{id}/extra | Long text RV Listings attributes for Listing with the given id |
| [**listingRvUkIdGet**](RvSearchApi.md#listingRvUkIdGet) | **GET** /listing/rv/uk/{id} | RV listing by id |
| [**listingRvUkIdMediaGet**](RvSearchApi.md#listingRvUkIdMediaGet) | **GET** /listing/rv/uk/{id}/media | Listing media by id |
| [**searchRvActiveGet**](RvSearchApi.md#searchRvActiveGet) | **GET** /search/rv/active | Gets active RV listings for the given search criteria |
| [**searchRvAutoCompleteGet**](RvSearchApi.md#searchRvAutoCompleteGet) | **GET** /search/rv/auto-complete | API for auto-completion of inputs |
| [**searchRvUkActiveGet**](RvSearchApi.md#searchRvUkActiveGet) | **GET** /search/rv/uk/active | Gets active RV listings for the given search criteria |


<a id="listingRvIdExtraGet"></a>
# **listingRvIdExtraGet**
> ListingExtraAttributes listingRvIdExtraGet(id, apiKey)

Long text RV Listings attributes for Listing with the given id

Get RV listing options, features, seller comments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RvSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    RvSearchApi apiInstance = new RvSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    try {
      ListingExtraAttributes result = apiInstance.listingRvIdExtraGet(id, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RvSearchApi#listingRvIdExtraGet");
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
| **id** | **String**| Listing id to get all the listing attributes | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |

### Return type

[**ListingExtraAttributes**](ListingExtraAttributes.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | RV ListingAttributes for the given listing id |  -  |
| **0** | Error |  -  |

<a id="listingRvIdGet"></a>
# **listingRvIdGet**
> RVListing listingRvIdGet(id, apiKey)

RV listing by id

Get a particular RV listing by its id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RvSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    RvSearchApi apiInstance = new RvSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    try {
      RVListing result = apiInstance.listingRvIdGet(id, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RvSearchApi#listingRvIdGet");
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
| **id** | **String**| Listing id to get all the listing attributes | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |

### Return type

[**RVListing**](RVListing.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | RV listing for the given id |  -  |
| **0** | Error |  -  |

<a id="listingRvIdMediaGet"></a>
# **listingRvIdMediaGet**
> ListingMedia listingRvIdMediaGet(id, apiKey)

Listing media by id

Get listing media (photo, photos) by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RvSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    RvSearchApi apiInstance = new RvSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    try {
      ListingMedia result = apiInstance.listingRvIdMediaGet(id, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RvSearchApi#listingRvIdMediaGet");
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
| **id** | **String**| Listing id to get all the listing attributes | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |

### Return type

[**ListingMedia**](ListingMedia.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Listing Media for the given listing id |  -  |
| **0** | Error |  -  |

<a id="listingRvUkIdExtraGet"></a>
# **listingRvUkIdExtraGet**
> ListingExtraAttributes listingRvUkIdExtraGet(id, apiKey)

Long text RV Listings attributes for Listing with the given id

Get RV listing options, features, seller comments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RvSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    RvSearchApi apiInstance = new RvSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    try {
      ListingExtraAttributes result = apiInstance.listingRvUkIdExtraGet(id, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RvSearchApi#listingRvUkIdExtraGet");
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
| **id** | **String**| Listing id to get all the listing attributes | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |

### Return type

[**ListingExtraAttributes**](ListingExtraAttributes.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | RV ListingAttributes for the given listing id |  -  |
| **0** | Error |  -  |

<a id="listingRvUkIdGet"></a>
# **listingRvUkIdGet**
> RVListing listingRvUkIdGet(id, apiKey)

RV listing by id

Get a particular RV listing by its id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RvSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    RvSearchApi apiInstance = new RvSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    try {
      RVListing result = apiInstance.listingRvUkIdGet(id, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RvSearchApi#listingRvUkIdGet");
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
| **id** | **String**| Listing id to get all the listing attributes | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |

### Return type

[**RVListing**](RVListing.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | RV listing for the given id |  -  |
| **0** | Error |  -  |

<a id="listingRvUkIdMediaGet"></a>
# **listingRvUkIdMediaGet**
> ListingMedia listingRvUkIdMediaGet(id, apiKey)

Listing media by id

Get listing media (photo, photos) by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RvSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    RvSearchApi apiInstance = new RvSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    try {
      ListingMedia result = apiInstance.listingRvUkIdMediaGet(id, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RvSearchApi#listingRvUkIdMediaGet");
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
| **id** | **String**| Listing id to get all the listing attributes | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |

### Return type

[**ListingMedia**](ListingMedia.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Listing Media for the given listing id |  -  |
| **0** | Error |  -  |

<a id="searchRvActiveGet"></a>
# **searchRvActiveGet**
> RVSearchResponse searchRvActiveGet(apiKey, priceRange, milesRange, msrpRange, yearRange, searchText, latitude, longitude, radius, year, make, model, modelO, vin, inventoryType, stockNo, source, dealerName, dealerId, exteriorColor, interiorColor, engine, fuelType, transmission, propertyClass, state, city, zip, msaCode, sortBy, sortOrder, rows, start, facets, rangeFacets, facetSort, stats, lastSeenRange, firstSeenRange, lastSeenDays, firstSeenDays, slideouts, lengthRange, length, baseExteriorColor, baseInteriorColor, seatingCapacity, freshWaterCapacity, sleeps, cylinders, numberOfAwnings, doors, gvwr)

Gets active RV listings for the given search criteria

This endpoint provides search on RV inventory. This API produces a list of currently active RV from the market for the given search criteria. The API results are limited to allow pagination upto 5000 rows.   The search API facilitates the following use cases -  1. Search RV around a given geo-point within a given radius  2. Search RV for a specific year / make / model or combination of these  3. Search RV matching multiple year, make, model combinatins in the same search request 4. Filter results by most RV specification attributes 5. Filter RV within a given price / miles range 6. Specify a sort order for the results on price / miles / listed date  7. Search RV for a given City / State combination  8. Get Facets to build the search drill downs  9. Get Market averages for price/miles for your search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RvSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    RvSearchApi apiInstance = new RvSearchApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    String priceRange = "priceRange_example"; // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String milesRange = "milesRange_example"; // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    String msrpRange = "msrpRange_example"; // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String yearRange = "yearRange_example"; // String | Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
    String searchText = "searchText_example"; // String | To search a substring across entire document
    Double latitude = 3.4D; // Double | Latitude component of location
    Double longitude = 3.4D; // Double | Longitude component of location
    Integer radius = 56; // Integer | Radius around the search location (Unit - Miles)
    String year = "year_example"; // String | To filter listing on their year
    String make = "make_example"; // String | To filter listings on their make
    String model = "model_example"; // String | To filter listings on their model
    String modelO = "modelO_example"; // String | To filter listings on their model orig (as described on the webpage)
    String vin = "vin_example"; // String | To filter listing on their VIN
    String inventoryType = "used"; // String | To filter listing on their condition. Either used or new
    String stockNo = "stockNo_example"; // String | To filter listing on their stock number on lot
    String source = "source_example"; // String | To filter listing on their source
    String dealerName = "dealerName_example"; // String | Filter listings on dealer_name
    String dealerId = "dealerId_example"; // String | Dealer id to filter the listings.
    String exteriorColor = "exteriorColor_example"; // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    String interiorColor = "interiorColor_example"; // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    String engine = "engine_example"; // String | To filter listing on their engine
    String fuelType = "fuelType_example"; // String | To filter listing on their fuel type
    String transmission = "transmission_example"; // String | To filter listing on their transmission
    String propertyClass = "propertyClass_example"; // String | Filter RV listings on class
    String state = "state_example"; // String | To filter listing on State in which they are listed
    String city = "city_example"; // String | To filter listing on City in which they are listed
    String zip = "zip_example"; // String | To filter listing on ZIP around which they are listed
    String msaCode = "msaCode_example"; // String | To filter listing on msa code in which they are listed
    String sortBy = "sortBy_example"; // String | Sort by field. Default sort field is distance from the given point
    String sortOrder = "asc"; // String | Sort order - asc or desc. Default sort order is asc
    Integer rows = 10; // Integer | Number of results to return. Default is 10. Max is 50
    Integer start = 0; // Integer | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    String facets = "facets_example"; // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    String rangeFacets = "rangeFacets_example"; // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    String facetSort = "count"; // String | Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
    String stats = "stats_example"; // String | The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
    String lastSeenRange = "lastSeenRange_example"; // String | Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenRange = "firstSeenRange_example"; // String | First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String lastSeenDays = "lastSeenDays_example"; // String | Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenDays = "firstSeenDays_example"; // String | First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
    String slideouts = "slideouts_example"; // String | Filter RV listings on slideouts
    String lengthRange = "lengthRange_example"; // String | length range to filter listings with the length in the range given. Range to be given in the format - min-max e.g. 50-200
    String length = "length_example"; // String | Filter RV listings on length
    String baseExteriorColor = "baseExteriorColor_example"; // String | Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
    String baseInteriorColor = "baseInteriorColor_example"; // String | Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
    String seatingCapacity = "seatingCapacity_example"; // String | To filter on vehicle seating capacity
    String freshWaterCapacity = "freshWaterCapacity_example"; // String | To filter on fresh water capacity of vehicle
    String sleeps = "sleeps_example"; // String | To filter data based on sleeps
    String cylinders = "cylinders_example"; // String | To filter listing on their cylinders
    String numberOfAwnings = "numberOfAwnings_example"; // String | To filter on number_of_awnings
    String doors = "doors_example"; // String | Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
    String gvwr = "gvwr_example"; // String | To filter on the maximum total weight of your vehicle
    try {
      RVSearchResponse result = apiInstance.searchRvActiveGet(apiKey, priceRange, milesRange, msrpRange, yearRange, searchText, latitude, longitude, radius, year, make, model, modelO, vin, inventoryType, stockNo, source, dealerName, dealerId, exteriorColor, interiorColor, engine, fuelType, transmission, propertyClass, state, city, zip, msaCode, sortBy, sortOrder, rows, start, facets, rangeFacets, facetSort, stats, lastSeenRange, firstSeenRange, lastSeenDays, firstSeenDays, slideouts, lengthRange, length, baseExteriorColor, baseInteriorColor, seatingCapacity, freshWaterCapacity, sleeps, cylinders, numberOfAwnings, doors, gvwr);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RvSearchApi#searchRvActiveGet");
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
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **priceRange** | **String**| Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **milesRange** | **String**| Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **msrpRange** | **String**| MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **yearRange** | **String**| Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021 | [optional] |
| **searchText** | **String**| To search a substring across entire document | [optional] |
| **latitude** | **Double**| Latitude component of location | [optional] |
| **longitude** | **Double**| Longitude component of location | [optional] |
| **radius** | **Integer**| Radius around the search location (Unit - Miles) | [optional] |
| **year** | **String**| To filter listing on their year | [optional] |
| **make** | **String**| To filter listings on their make | [optional] |
| **model** | **String**| To filter listings on their model | [optional] |
| **modelO** | **String**| To filter listings on their model orig (as described on the webpage) | [optional] |
| **vin** | **String**| To filter listing on their VIN | [optional] |
| **inventoryType** | **String**| To filter listing on their condition. Either used or new | [optional] [enum: used, new] |
| **stockNo** | **String**| To filter listing on their stock number on lot | [optional] |
| **source** | **String**| To filter listing on their source | [optional] |
| **dealerName** | **String**| Filter listings on dealer_name | [optional] |
| **dealerId** | **String**| Dealer id to filter the listings. | [optional] |
| **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] |
| **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] |
| **engine** | **String**| To filter listing on their engine | [optional] |
| **fuelType** | **String**| To filter listing on their fuel type | [optional] |
| **transmission** | **String**| To filter listing on their transmission | [optional] |
| **propertyClass** | **String**| Filter RV listings on class | [optional] |
| **state** | **String**| To filter listing on State in which they are listed | [optional] |
| **city** | **String**| To filter listing on City in which they are listed | [optional] |
| **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] |
| **msaCode** | **String**| To filter listing on msa code in which they are listed | [optional] |
| **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] |
| **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] [enum: asc, desc, ASC, DESC] |
| **rows** | **Integer**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10] |
| **start** | **Integer**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0] |
| **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] |
| **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] |
| **facetSort** | **String**| Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param | [optional] [default to count] [enum: count, index] |
| **stats** | **String**| The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. | [optional] |
| **lastSeenRange** | **String**| Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenRange** | **String**| First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **lastSeenDays** | **String**| Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenDays** | **String**| First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **slideouts** | **String**| Filter RV listings on slideouts | [optional] |
| **lengthRange** | **String**| length range to filter listings with the length in the range given. Range to be given in the format - min-max e.g. 50-200 | [optional] |
| **length** | **String**| Filter RV listings on length | [optional] |
| **baseExteriorColor** | **String**| Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated | [optional] |
| **baseInteriorColor** | **String**| Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated | [optional] |
| **seatingCapacity** | **String**| To filter on vehicle seating capacity | [optional] |
| **freshWaterCapacity** | **String**| To filter on fresh water capacity of vehicle | [optional] |
| **sleeps** | **String**| To filter data based on sleeps | [optional] |
| **cylinders** | **String**| To filter listing on their cylinders | [optional] |
| **numberOfAwnings** | **String**| To filter on number_of_awnings | [optional] |
| **doors** | **String**| Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated | [optional] |
| **gvwr** | **String**| To filter on the maximum total weight of your vehicle | [optional] |

### Return type

[**RVSearchResponse**](RVSearchResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of all RV listings matching the search &amp; filter criteria |  -  |
| **0** | Error |  -  |

<a id="searchRvAutoCompleteGet"></a>
# **searchRvAutoCompleteGet**
> SearchAutoCompleteResponse searchRvAutoCompleteGet(field, input, apiKey, year, make, model, trim, bodyType, vehicleType, transmission, drivetrain, fuelType, color, engine, state, city, inventoryType, ignoreCase, termCounts, sortBy, sellerType, radius, zip, facetMinCount)

API for auto-completion of inputs

Auto-complete the inputs of your end users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RvSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    RvSearchApi apiInstance = new RvSearchApi(defaultClient);
    String field = "make"; // String | Field name for which you want auto-completion
    String input = "input_example"; // String | Input entered so far
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    String year = "year_example"; // String | To filter listing on their year
    String make = "make_example"; // String | To filter listings on their make
    String model = "model_example"; // String | To filter listings on their model
    String trim = "trim_example"; // String | To filter listing on their trim
    String bodyType = "bodyType_example"; // String | To filter listing on their body type
    String vehicleType = "vehicleType_example"; // String | To filter listing on their vehicle type
    String transmission = "transmission_example"; // String | To filter listing on their transmission
    String drivetrain = "drivetrain_example"; // String | To filter listing on their drivetrain
    String fuelType = "fuelType_example"; // String | To filter listing on their fuel type
    String color = "color_example"; // String | Color of the vehicle
    String engine = "engine_example"; // String | To filter listing on their engine
    String state = "state_example"; // String | To filter listing on State in which they are listed
    String city = "city_example"; // String | To filter listing on City in which they are listed
    String inventoryType = "used"; // String | To filter listing on their condition. Either used or new
    Boolean ignoreCase = true; // Boolean | Boolean variable to indicate ignore case of current input
    Boolean termCounts = false; // Boolean | Boolean variable to indicate wheather to include term counts as well in response
    String sortBy = "index"; // String | Sort the response, either by index or count(default)
    String sellerType = "sellerType_example"; // String | seller type for autocomplete
    Integer radius = 56; // Integer | Radius around the search location (Unit - Miles)
    String zip = "zip_example"; // String | To filter listing on ZIP around which they are listed
    BigDecimal facetMinCount = new BigDecimal("1"); // BigDecimal | Provide minimum count value for facets
    try {
      SearchAutoCompleteResponse result = apiInstance.searchRvAutoCompleteGet(field, input, apiKey, year, make, model, trim, bodyType, vehicleType, transmission, drivetrain, fuelType, color, engine, state, city, inventoryType, ignoreCase, termCounts, sortBy, sellerType, radius, zip, facetMinCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RvSearchApi#searchRvAutoCompleteGet");
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
| **field** | **String**| Field name for which you want auto-completion | [enum: make, model, trim, class, transmission, fuel_type, exterior_color, interior_color, engine, state, city] |
| **input** | **String**| Input entered so far | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **year** | **String**| To filter listing on their year | [optional] |
| **make** | **String**| To filter listings on their make | [optional] |
| **model** | **String**| To filter listings on their model | [optional] |
| **trim** | **String**| To filter listing on their trim | [optional] |
| **bodyType** | **String**| To filter listing on their body type | [optional] |
| **vehicleType** | **String**| To filter listing on their vehicle type | [optional] |
| **transmission** | **String**| To filter listing on their transmission | [optional] |
| **drivetrain** | **String**| To filter listing on their drivetrain | [optional] |
| **fuelType** | **String**| To filter listing on their fuel type | [optional] |
| **color** | **String**| Color of the vehicle | [optional] |
| **engine** | **String**| To filter listing on their engine | [optional] |
| **state** | **String**| To filter listing on State in which they are listed | [optional] |
| **city** | **String**| To filter listing on City in which they are listed | [optional] |
| **inventoryType** | **String**| To filter listing on their condition. Either used or new | [optional] [enum: used, new] |
| **ignoreCase** | **Boolean**| Boolean variable to indicate ignore case of current input | [optional] [default to true] |
| **termCounts** | **Boolean**| Boolean variable to indicate wheather to include term counts as well in response | [optional] [default to false] |
| **sortBy** | **String**| Sort the response, either by index or count(default) | [optional] [default to index] [enum: index, count] |
| **sellerType** | **String**| seller type for autocomplete | [optional] |
| **radius** | **Integer**| Radius around the search location (Unit - Miles) | [optional] |
| **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] |
| **facetMinCount** | **BigDecimal**| Provide minimum count value for facets | [optional] [default to 1] |

### Return type

[**SearchAutoCompleteResponse**](SearchAutoCompleteResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Unique terms available in given field for auto completion |  -  |
| **0** | Error |  -  |

<a id="searchRvUkActiveGet"></a>
# **searchRvUkActiveGet**
> UKRVSearchResponse searchRvUkActiveGet(apiKey, priceRange, milesRange, msrpRange, yearRange, searchText, latitude, longitude, radius, year, make, model, vin, source, dealerName, dealerId, exteriorColor, interiorColor, engineSize, fuelType, category, state, city, county, postalCode, zip, sortBy, sortOrder, rows, start, facets, rangeFacets, facetSort, stats, lastSeenRange, firstSeenRange, lastSeenDays, firstSeenDays, baseExteriorColor, baseInteriorColor, seatingCapacity, cylinders, doors, mtplm, subCategory, availabilityStatus, berths, inventoryType, widthRange, exteriorLengthRange, interiorLengthRange, driveType, steering, chassis, transmission)

Gets active RV listings for the given search criteria

This endpoint provides search on RV inventory. This API produces a list of currently active RV from the market for the given search criteria. The API results are limited to allow pagination upto 5000 rows.   The search API facilitates the following use cases -  1. Search RV around a given geo-point within a given radius  2. Search RV for a specific year / make / model or combination of these  3. Search RV matching multiple year, make, model combinatins in the same search request 4. Filter results by most RV specification attributes 5. Filter RV within a given price / miles range 6. Specify a sort order for the results on price / miles / listed date  7. Search RV for a given City / State combination  8. Get Facets to build the search drill downs  9. Get Market averages for price/miles for your search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RvSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    RvSearchApi apiInstance = new RvSearchApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    String priceRange = "priceRange_example"; // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String milesRange = "milesRange_example"; // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    String msrpRange = "msrpRange_example"; // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String yearRange = "yearRange_example"; // String | Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
    String searchText = "searchText_example"; // String | To search a substring across entire document
    Double latitude = 3.4D; // Double | Latitude component of location
    Double longitude = 3.4D; // Double | Longitude component of location
    Integer radius = 56; // Integer | Radius around the search location (Unit - Miles)
    String year = "year_example"; // String | To filter listing on their year
    String make = "make_example"; // String | To filter listings on their make
    String model = "model_example"; // String | To filter listings on their model
    String vin = "vin_example"; // String | To filter listing on their VIN
    String source = "source_example"; // String | To filter listing on their source
    String dealerName = "dealerName_example"; // String | Filter listings on dealer_name
    String dealerId = "dealerId_example"; // String | Dealer id to filter the listings.
    String exteriorColor = "exteriorColor_example"; // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    String interiorColor = "interiorColor_example"; // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    String engineSize = "engineSize_example"; // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    String fuelType = "fuelType_example"; // String | To filter listing on their fuel type
    String category = "category_example"; // String | Filter RV listings on category
    String state = "state_example"; // String | To filter listing on State in which they are listed
    String city = "city_example"; // String | To filter listing on City in which they are listed
    String county = "county_example"; // String | To filter listing on county in which they are listed
    String postalCode = "postalCode_example"; // String | To filter listing on postal code around which they are listed
    String zip = "zip_example"; // String | To filter listing on ZIP around which they are listed
    String sortBy = "sortBy_example"; // String | Sort by field. Default sort field is distance from the given point
    String sortOrder = "asc"; // String | Sort order - asc or desc. Default sort order is asc
    Integer rows = 10; // Integer | Number of results to return. Default is 10. Max is 50
    Integer start = 0; // Integer | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    String facets = "facets_example"; // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    String rangeFacets = "rangeFacets_example"; // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    String facetSort = "count"; // String | Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
    String stats = "stats_example"; // String | The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
    String lastSeenRange = "lastSeenRange_example"; // String | Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenRange = "firstSeenRange_example"; // String | First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String lastSeenDays = "lastSeenDays_example"; // String | Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenDays = "firstSeenDays_example"; // String | First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
    String baseExteriorColor = "baseExteriorColor_example"; // String | Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
    String baseInteriorColor = "baseInteriorColor_example"; // String | Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
    String seatingCapacity = "seatingCapacity_example"; // String | To filter on vehicle seating capacity
    String cylinders = "cylinders_example"; // String | To filter listing on their cylinders
    String doors = "doors_example"; // String | Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
    String mtplm = "mtplm_example"; // String | To filter rv on mtplm
    String subCategory = "subCategory_example"; // String | To filter rv on their sub-category
    String availabilityStatus = "availabilityStatus_example"; // String | To filter rv on their availability_status
    String berths = "berths_example"; // String | To filter rv on their berths
    String inventoryType = "used"; // String | To filter listing on their condition. Either used or new
    String widthRange = "widthRange_example"; // String | width range to filter listings on width in the range given. Range to be given in the format - min-max e.g. 4-8
    String exteriorLengthRange = "exteriorLengthRange_example"; // String | width range to filter listings on exterior_length in the range given. Range to be given in the format - min-max e.g. 4-8
    String interiorLengthRange = "interiorLengthRange_example"; // String | width range to filter listings on interior_length in the range given. Range to be given in the format - min-max e.g. 4-8
    String driveType = "driveType_example"; // String | To filter rv on their drive_type
    String steering = "steering_example"; // String | To filter rv on their steering
    String chassis = "chassis_example"; // String | To filter rv on their chassis
    String transmission = "transmission_example"; // String | To filter listing on their transmission
    try {
      UKRVSearchResponse result = apiInstance.searchRvUkActiveGet(apiKey, priceRange, milesRange, msrpRange, yearRange, searchText, latitude, longitude, radius, year, make, model, vin, source, dealerName, dealerId, exteriorColor, interiorColor, engineSize, fuelType, category, state, city, county, postalCode, zip, sortBy, sortOrder, rows, start, facets, rangeFacets, facetSort, stats, lastSeenRange, firstSeenRange, lastSeenDays, firstSeenDays, baseExteriorColor, baseInteriorColor, seatingCapacity, cylinders, doors, mtplm, subCategory, availabilityStatus, berths, inventoryType, widthRange, exteriorLengthRange, interiorLengthRange, driveType, steering, chassis, transmission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RvSearchApi#searchRvUkActiveGet");
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
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **priceRange** | **String**| Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **milesRange** | **String**| Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **msrpRange** | **String**| MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **yearRange** | **String**| Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021 | [optional] |
| **searchText** | **String**| To search a substring across entire document | [optional] |
| **latitude** | **Double**| Latitude component of location | [optional] |
| **longitude** | **Double**| Longitude component of location | [optional] |
| **radius** | **Integer**| Radius around the search location (Unit - Miles) | [optional] |
| **year** | **String**| To filter listing on their year | [optional] |
| **make** | **String**| To filter listings on their make | [optional] |
| **model** | **String**| To filter listings on their model | [optional] |
| **vin** | **String**| To filter listing on their VIN | [optional] |
| **source** | **String**| To filter listing on their source | [optional] |
| **dealerName** | **String**| Filter listings on dealer_name | [optional] |
| **dealerId** | **String**| Dealer id to filter the listings. | [optional] |
| **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] |
| **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] |
| **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] |
| **fuelType** | **String**| To filter listing on their fuel type | [optional] |
| **category** | **String**| Filter RV listings on category | [optional] |
| **state** | **String**| To filter listing on State in which they are listed | [optional] |
| **city** | **String**| To filter listing on City in which they are listed | [optional] |
| **county** | **String**| To filter listing on county in which they are listed | [optional] |
| **postalCode** | **String**| To filter listing on postal code around which they are listed | [optional] |
| **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] |
| **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] |
| **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] [enum: asc, desc, ASC, DESC] |
| **rows** | **Integer**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10] |
| **start** | **Integer**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0] |
| **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] |
| **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] |
| **facetSort** | **String**| Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param | [optional] [default to count] [enum: count, index] |
| **stats** | **String**| The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. | [optional] |
| **lastSeenRange** | **String**| Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenRange** | **String**| First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **lastSeenDays** | **String**| Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenDays** | **String**| First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **baseExteriorColor** | **String**| Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated | [optional] |
| **baseInteriorColor** | **String**| Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated | [optional] |
| **seatingCapacity** | **String**| To filter on vehicle seating capacity | [optional] |
| **cylinders** | **String**| To filter listing on their cylinders | [optional] |
| **doors** | **String**| Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated | [optional] |
| **mtplm** | **String**| To filter rv on mtplm | [optional] |
| **subCategory** | **String**| To filter rv on their sub-category | [optional] |
| **availabilityStatus** | **String**| To filter rv on their availability_status | [optional] |
| **berths** | **String**| To filter rv on their berths | [optional] |
| **inventoryType** | **String**| To filter listing on their condition. Either used or new | [optional] [enum: used, new] |
| **widthRange** | **String**| width range to filter listings on width in the range given. Range to be given in the format - min-max e.g. 4-8 | [optional] |
| **exteriorLengthRange** | **String**| width range to filter listings on exterior_length in the range given. Range to be given in the format - min-max e.g. 4-8 | [optional] |
| **interiorLengthRange** | **String**| width range to filter listings on interior_length in the range given. Range to be given in the format - min-max e.g. 4-8 | [optional] |
| **driveType** | **String**| To filter rv on their drive_type | [optional] |
| **steering** | **String**| To filter rv on their steering | [optional] |
| **chassis** | **String**| To filter rv on their chassis | [optional] |
| **transmission** | **String**| To filter listing on their transmission | [optional] |

### Return type

[**UKRVSearchResponse**](UKRVSearchResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of all RV listings matching the search &amp; filter criteria |  -  |
| **0** | Error |  -  |

