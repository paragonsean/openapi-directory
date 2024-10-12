# HeavyEquipmentSearchApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listingHeavyEquipmentIdExtraGet**](HeavyEquipmentSearchApi.md#listingHeavyEquipmentIdExtraGet) | **GET** /listing/heavy-equipment/{id}/extra | Long text Heavy equipment Listings attributes for Listing with the given id |
| [**listingHeavyEquipmentIdGet**](HeavyEquipmentSearchApi.md#listingHeavyEquipmentIdGet) | **GET** /listing/heavy-equipment/{id} | Heavy equipment listing by id |
| [**listingHeavyEquipmentIdMediaGet**](HeavyEquipmentSearchApi.md#listingHeavyEquipmentIdMediaGet) | **GET** /listing/heavy-equipment/{id}/media | Listing media by id |
| [**searchHeavyEquipmentActiveGet**](HeavyEquipmentSearchApi.md#searchHeavyEquipmentActiveGet) | **GET** /search/heavy-equipment/active | Gets active heavy equipment listings for the given search criteria |
| [**searchHeavyEquipmentAutoCompleteGet**](HeavyEquipmentSearchApi.md#searchHeavyEquipmentAutoCompleteGet) | **GET** /search/heavy-equipment/auto-complete | API for auto-completion of inputs |


<a id="listingHeavyEquipmentIdExtraGet"></a>
# **listingHeavyEquipmentIdExtraGet**
> ListingExtraAttributes listingHeavyEquipmentIdExtraGet(id, apiKey)

Long text Heavy equipment Listings attributes for Listing with the given id

Get Heavy equipment listing options, features, seller comments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HeavyEquipmentSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    HeavyEquipmentSearchApi apiInstance = new HeavyEquipmentSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    try {
      ListingExtraAttributes result = apiInstance.listingHeavyEquipmentIdExtraGet(id, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HeavyEquipmentSearchApi#listingHeavyEquipmentIdExtraGet");
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
| **200** | Heavy equipment ListingAttributes for the given listing id |  -  |
| **0** | Error |  -  |

<a id="listingHeavyEquipmentIdGet"></a>
# **listingHeavyEquipmentIdGet**
> HeavyEquipmentsListing listingHeavyEquipmentIdGet(id, apiKey)

Heavy equipment listing by id

Get a particular Heavy equipment listing by its id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HeavyEquipmentSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    HeavyEquipmentSearchApi apiInstance = new HeavyEquipmentSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    try {
      HeavyEquipmentsListing result = apiInstance.listingHeavyEquipmentIdGet(id, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HeavyEquipmentSearchApi#listingHeavyEquipmentIdGet");
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

[**HeavyEquipmentsListing**](HeavyEquipmentsListing.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Heavy equipment listing for the given id |  -  |
| **0** | Error |  -  |

<a id="listingHeavyEquipmentIdMediaGet"></a>
# **listingHeavyEquipmentIdMediaGet**
> ListingMedia listingHeavyEquipmentIdMediaGet(id, apiKey)

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
import org.openapitools.client.api.HeavyEquipmentSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    HeavyEquipmentSearchApi apiInstance = new HeavyEquipmentSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    try {
      ListingMedia result = apiInstance.listingHeavyEquipmentIdMediaGet(id, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HeavyEquipmentSearchApi#listingHeavyEquipmentIdMediaGet");
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

<a id="searchHeavyEquipmentActiveGet"></a>
# **searchHeavyEquipmentActiveGet**
> HeavyEquipmentsSearchResponse searchHeavyEquipmentActiveGet(apiKey, priceRange, milesRange, msrpRange, latitude, longitude, radius, searchText, year, make, model, trim, vin, inventoryType, stockNo, source, dealerName, dealerId, exteriorColor, interiorColor, engine, fuelType, transmission, drivetrain, bodyType, category, subCategory, hoursUsedRange, state, city, zip, msaCode, sortBy, sortOrder, rows, start, facets, rangeFacets, facetSort, stats, lastSeenRange, firstSeenRange, lastSeenDays, firstSeenDays)

Gets active heavy equipment listings for the given search criteria

This endpoint provides search on heavy equipment inventory. This API produces a list of currently active heavy equipments from the market for the given search criteria. The API results are limited to allow pagination upto 5000 rows.   The search API facilitates the following use cases -  1. Search heavy equipments around a given geo-point within a given radius  2. Search heavy equipments for a specific year / make / model or combination of these  3. Search heavy equipments matching multiple year, make, model combinatins in the same search request 4. Filter results by most heavy equipment specification attributes 5. Filter heavy equipments within a given price / miles range 6. Specify a sort order for the results on price / miles / listed date  7. Search heavy equipments for a given City / State combination  8. Get Facets to build the search drill downs  9. Get Market averages for price/miles for your search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HeavyEquipmentSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    HeavyEquipmentSearchApi apiInstance = new HeavyEquipmentSearchApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    String priceRange = "priceRange_example"; // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String milesRange = "milesRange_example"; // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    String msrpRange = "msrpRange_example"; // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    Double latitude = 3.4D; // Double | Latitude component of location
    Double longitude = 3.4D; // Double | Longitude component of location
    Integer radius = 56; // Integer | Radius around the search location (Unit - Miles)
    String searchText = "searchText_example"; // String | To search a substring across entire document
    String year = "year_example"; // String | To filter listing on their year
    String make = "make_example"; // String | To filter listings on their make
    String model = "model_example"; // String | To filter listings on their model
    String trim = "trim_example"; // String | To filter listing on their trim
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
    String drivetrain = "drivetrain_example"; // String | To filter listing on their drivetrain
    String bodyType = "bodyType_example"; // String | To filter listing on their body type
    String category = "category_example"; // String | To filter heavy equipments on their category
    String subCategory = "subCategory_example"; // String | To filter heavy equipments on their sub-category
    String hoursUsedRange = "hoursUsedRange_example"; // String | Hours used range to filter heavy equipments with the their usage in the range given. Range to be given in the format - min-max e.g. 1000-5000
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
    try {
      HeavyEquipmentsSearchResponse result = apiInstance.searchHeavyEquipmentActiveGet(apiKey, priceRange, milesRange, msrpRange, latitude, longitude, radius, searchText, year, make, model, trim, vin, inventoryType, stockNo, source, dealerName, dealerId, exteriorColor, interiorColor, engine, fuelType, transmission, drivetrain, bodyType, category, subCategory, hoursUsedRange, state, city, zip, msaCode, sortBy, sortOrder, rows, start, facets, rangeFacets, facetSort, stats, lastSeenRange, firstSeenRange, lastSeenDays, firstSeenDays);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HeavyEquipmentSearchApi#searchHeavyEquipmentActiveGet");
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
| **latitude** | **Double**| Latitude component of location | [optional] |
| **longitude** | **Double**| Longitude component of location | [optional] |
| **radius** | **Integer**| Radius around the search location (Unit - Miles) | [optional] |
| **searchText** | **String**| To search a substring across entire document | [optional] |
| **year** | **String**| To filter listing on their year | [optional] |
| **make** | **String**| To filter listings on their make | [optional] |
| **model** | **String**| To filter listings on their model | [optional] |
| **trim** | **String**| To filter listing on their trim | [optional] |
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
| **drivetrain** | **String**| To filter listing on their drivetrain | [optional] |
| **bodyType** | **String**| To filter listing on their body type | [optional] |
| **category** | **String**| To filter heavy equipments on their category | [optional] |
| **subCategory** | **String**| To filter heavy equipments on their sub-category | [optional] |
| **hoursUsedRange** | **String**| Hours used range to filter heavy equipments with the their usage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
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

### Return type

[**HeavyEquipmentsSearchResponse**](HeavyEquipmentsSearchResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of all heavy equipment listings matching the search &amp; filter criteria |  -  |
| **0** | Error |  -  |

<a id="searchHeavyEquipmentAutoCompleteGet"></a>
# **searchHeavyEquipmentAutoCompleteGet**
> SearchAutoCompleteResponse searchHeavyEquipmentAutoCompleteGet(field, input, apiKey, year, make, model, trim, bodyType, vehicleType, transmission, drivetrain, fuelType, color, engine, state, city, inventoryType, ignoreCase, termCounts, sortBy, sellerType, radius, zip, facetMinCount)

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
import org.openapitools.client.api.HeavyEquipmentSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    HeavyEquipmentSearchApi apiInstance = new HeavyEquipmentSearchApi(defaultClient);
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
      SearchAutoCompleteResponse result = apiInstance.searchHeavyEquipmentAutoCompleteGet(field, input, apiKey, year, make, model, trim, bodyType, vehicleType, transmission, drivetrain, fuelType, color, engine, state, city, inventoryType, ignoreCase, termCounts, sortBy, sellerType, radius, zip, facetMinCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HeavyEquipmentSearchApi#searchHeavyEquipmentAutoCompleteGet");
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
| **field** | **String**| Field name for which you want auto-completion | [enum: make, model, trim, body_type, transmission, drivetrain, fuel_type, exterior_color, interior_color, engine, category, sub_category, state, city] |
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

