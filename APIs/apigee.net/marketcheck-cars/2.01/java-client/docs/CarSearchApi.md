# CarSearchApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**autoComplete**](CarSearchApi.md#autoComplete) | **GET** /search/car/auto-complete | API for auto-completion of inputs |
| [**carDealerInventoryActiveGet**](CarSearchApi.md#carDealerInventoryActiveGet) | **GET** /car/dealer/inventory/active | Get dealers active inventory |
| [**getListing**](CarSearchApi.md#getListing) | **GET** /listing/car/{id} | Listing by id |
| [**listingCarAuctionIdExtraGet**](CarSearchApi.md#listingCarAuctionIdExtraGet) | **GET** /listing/car/auction/{id}/extra | Long text Listings attributes for Listing with the given id |
| [**listingCarAuctionIdGet**](CarSearchApi.md#listingCarAuctionIdGet) | **GET** /listing/car/auction/{id} | Listing by id |
| [**listingCarAuctionIdMediaGet**](CarSearchApi.md#listingCarAuctionIdMediaGet) | **GET** /listing/car/auction/{id}/media | Listing media by id |
| [**listingCarFsboIdExtraGet**](CarSearchApi.md#listingCarFsboIdExtraGet) | **GET** /listing/car/fsbo/{id}/extra | Long text Listings attributes for Listing with the given id |
| [**listingCarFsboIdGet**](CarSearchApi.md#listingCarFsboIdGet) | **GET** /listing/car/fsbo/{id} | Listing by id |
| [**listingCarFsboIdMediaGet**](CarSearchApi.md#listingCarFsboIdMediaGet) | **GET** /listing/car/fsbo/{id}/media | Listing media by id |
| [**listingCarIdExtraGet**](CarSearchApi.md#listingCarIdExtraGet) | **GET** /listing/car/{id}/extra | Long text Listings attributes for Listing with the given id |
| [**listingCarIdMediaGet**](CarSearchApi.md#listingCarIdMediaGet) | **GET** /listing/car/{id}/media | Listing media by id |
| [**listingCarUkIdExtraGet**](CarSearchApi.md#listingCarUkIdExtraGet) | **GET** /listing/car/uk/{id}/extra | Long text Listings attributes for Listing with the given id |
| [**listingCarUkIdGet**](CarSearchApi.md#listingCarUkIdGet) | **GET** /listing/car/uk/{id} | Listing by id |
| [**listingCarUkIdMediaGet**](CarSearchApi.md#listingCarUkIdMediaGet) | **GET** /listing/car/uk/{id}/media | Listing media by id |
| [**search**](CarSearchApi.md#search) | **GET** /search/car/uk/active | Gets active car listings in UK for the given search criteria |
| [**searchCarActiveGet**](CarSearchApi.md#searchCarActiveGet) | **GET** /search/car/active | Gets active car listings for the given search criteria |
| [**searchCarAuctionActiveGet**](CarSearchApi.md#searchCarAuctionActiveGet) | **GET** /search/car/auction/active | Gets active auction car listings for the given search criteria |
| [**searchCarFsboActiveGet**](CarSearchApi.md#searchCarFsboActiveGet) | **GET** /search/car/fsbo/active | Gets active private party car listings for the given search criteria |
| [**searchCarRecentsGet**](CarSearchApi.md#searchCarRecentsGet) | **GET** /search/car/recents | Gets Recent car listings for the given search criteria |
| [**searchCarUkRecentsGet**](CarSearchApi.md#searchCarUkRecentsGet) | **GET** /search/car/uk/recents | Gets Recent UK car listings for the given search criteria |


<a id="autoComplete"></a>
# **autoComplete**
> SearchAutoCompleteResponse autoComplete(field, input, apiKey, year, make, model, trim, bodyType, bodySubtype, vehicleType, transmission, drivetrain, fuelType, exteriorColor, interiorColor, engine, engineSize, engineBlock, state, city, source, dealerId, country, carType, includeNonVinListings, ignoreCase, termCounts, sortBy, sellerType, radius, zip, inventoryCountRange, excludeDealerIds, excludeSources, inTransit, facetMinCount)

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
import org.openapitools.client.api.CarSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarSearchApi apiInstance = new CarSearchApi(defaultClient);
    String field = "ymm"; // String | Field name for which you want auto-completion
    String input = "input_example"; // String | Input entered so far
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    String year = "year_example"; // String | To filter listing on their year
    String make = "make_example"; // String | To filter listings on their make
    String model = "model_example"; // String | To filter listings on their model
    String trim = "trim_example"; // String | To filter listing on their trim
    String bodyType = "bodyType_example"; // String | To filter listing on their body type
    String bodySubtype = "bodySubtype_example"; // String | Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
    String vehicleType = "vehicleType_example"; // String | To filter listing on their vehicle type
    String transmission = "transmission_example"; // String | To filter listing on their transmission
    String drivetrain = "drivetrain_example"; // String | To filter listing on their drivetrain
    String fuelType = "fuelType_example"; // String | To filter listing on their fuel type
    String exteriorColor = "exteriorColor_example"; // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    String interiorColor = "interiorColor_example"; // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    String engine = "engine_example"; // String | To filter listing on their engine
    String engineSize = "engineSize_example"; // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    String engineBlock = "engineBlock_example"; // String | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
    String state = "state_example"; // String | To filter listing on State in which they are listed
    String city = "city_example"; // String | To filter listing on City in which they are listed
    String source = "source_example"; // String | To filter listing on their source only for widget requests
    String dealerId = "dealerId_example"; // String | Dealer id to filter the listings.
    String country = "US"; // String | To filter listing on Country in which they are listed
    String carType = "new"; // String | Car type. Allowed values are - new / used
    String includeNonVinListings = "true"; // String | Flag to indicate whether to include non vin listing terms in results or not. Default is false to avoid un-normalised terms from non vin listings out of results
    Boolean ignoreCase = true; // Boolean | Boolean variable to indicate ignore case of current input
    Boolean termCounts = false; // Boolean | Boolean variable to indicate wheather to include term counts as well in response
    String sortBy = "index"; // String | Sort the response, either by index or count(default)
    String sellerType = "sellerType_example"; // String | seller type for autocomplete
    Integer radius = 56; // Integer | Radius around the search location (Unit - Miles)
    String zip = "zip_example"; // String | To filter listing on ZIP around which they are listed
    String inventoryCountRange = "inventoryCountRange_example"; // String | Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50
    String excludeDealerIds = "excludeDealerIds_example"; // String | A list of dealer ids to exclude from result
    String excludeSources = "excludeSources_example"; // String | A list of sources to exclude from result
    String inTransit = "true"; // String | A boolean to filter in transit vehicles
    BigDecimal facetMinCount = new BigDecimal("1"); // BigDecimal | Provide minimum count value for facets
    try {
      SearchAutoCompleteResponse result = apiInstance.autoComplete(field, input, apiKey, year, make, model, trim, bodyType, bodySubtype, vehicleType, transmission, drivetrain, fuelType, exteriorColor, interiorColor, engine, engineSize, engineBlock, state, city, source, dealerId, country, carType, includeNonVinListings, ignoreCase, termCounts, sortBy, sellerType, radius, zip, inventoryCountRange, excludeDealerIds, excludeSources, inTransit, facetMinCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarSearchApi#autoComplete");
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
| **field** | **String**| Field name for which you want auto-completion | [enum: ymm, mm, make, model, trim, body_type, body_subtype, vehicle_type, transmission, drivetrain, fuel_type, exterior_color, interior_color, engine, engine_size, engine_block, state, city] |
| **input** | **String**| Input entered so far | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **year** | **String**| To filter listing on their year | [optional] |
| **make** | **String**| To filter listings on their make | [optional] |
| **model** | **String**| To filter listings on their model | [optional] |
| **trim** | **String**| To filter listing on their trim | [optional] |
| **bodyType** | **String**| To filter listing on their body type | [optional] |
| **bodySubtype** | **String**| Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] |
| **vehicleType** | **String**| To filter listing on their vehicle type | [optional] |
| **transmission** | **String**| To filter listing on their transmission | [optional] |
| **drivetrain** | **String**| To filter listing on their drivetrain | [optional] |
| **fuelType** | **String**| To filter listing on their fuel type | [optional] |
| **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] |
| **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] |
| **engine** | **String**| To filter listing on their engine | [optional] |
| **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] |
| **engineBlock** | **String**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] |
| **state** | **String**| To filter listing on State in which they are listed | [optional] |
| **city** | **String**| To filter listing on City in which they are listed | [optional] |
| **source** | **String**| To filter listing on their source only for widget requests | [optional] |
| **dealerId** | **String**| Dealer id to filter the listings. | [optional] |
| **country** | **String**| To filter listing on Country in which they are listed | [optional] [default to US] [enum: US, CA, us, ca] |
| **carType** | **String**| Car type. Allowed values are - new / used | [optional] [enum: new, used] |
| **includeNonVinListings** | **String**| Flag to indicate whether to include non vin listing terms in results or not. Default is false to avoid un-normalised terms from non vin listings out of results | [optional] [default to false] [enum: true, false] |
| **ignoreCase** | **Boolean**| Boolean variable to indicate ignore case of current input | [optional] [default to true] |
| **termCounts** | **Boolean**| Boolean variable to indicate wheather to include term counts as well in response | [optional] [default to false] |
| **sortBy** | **String**| Sort the response, either by index or count(default) | [optional] [default to index] [enum: index, count] |
| **sellerType** | **String**| seller type for autocomplete | [optional] |
| **radius** | **Integer**| Radius around the search location (Unit - Miles) | [optional] |
| **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] |
| **inventoryCountRange** | **String**| Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **excludeDealerIds** | **String**| A list of dealer ids to exclude from result | [optional] |
| **excludeSources** | **String**| A list of sources to exclude from result | [optional] |
| **inTransit** | **String**| A boolean to filter in transit vehicles | [optional] [enum: true, false] |
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

<a id="carDealerInventoryActiveGet"></a>
# **carDealerInventoryActiveGet**
> SearchResponse carDealerInventoryActiveGet(apiKey, appendApiKey, latitude, longitude, radius, zip, includeLease, includeFinance, leaseTerm, leaseDownPayment, leaseEmp, financeLoanTerm, financeLoanApr, financeEmp, financeDownPayment, financeDownPaymentPer, carType, carfax1Owner, carfaxCleanTitle, yearRange, year, make, model, trim, dealerId, vin, source, bodyType, bodySubtype, vehicleType, vins, taxonomyVins, mm, ymm, ymmt, match, cylinders, transmission, doors, drivetrain, exteriorColor, interiorColor, baseExteriorColor, baseInteriorColor, engine, engineSize, engineAspiration, engineBlock, highwayMpgRange, cityMpgRange, milesRange, priceRange, msrpRange, domRange, sortBy, sortOrder, rows, start, includeNonVinListings, msaCode, facets, rangeFacets, facetSort, stats, country, plot, nodedup, dedup, owned, state, city, dealerName, dealershipGroupName, trimO, trimR, domActiveRange, dom180Range, excludeCertified, fuelType, dealerType, photoLinks, photoLinksCached, stockNo, lastSeenRange, firstSeenRange, firstSeenAtSourceRange, firstSeenAtMcRange, lastSeenDays, firstSeenDays, firstSeenAtSourceDays, firstSeenAtMcDays, includeRelevantLinks, inventoryCountRange, inTransit, seatingCapacity, engineSizeRange, powertrainType, minPhotoLinks, minPhotoLinksCached)

Get dealers active inventory

Get dealers active inventory

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarSearchApi apiInstance = new CarSearchApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean appendApiKey = true; // Boolean | Flag on whether to include api_key in response API urls (if any)
    Double latitude = 3.4D; // Double | Latitude component of location
    Double longitude = 3.4D; // Double | Longitude component of location
    Integer radius = 56; // Integer | Radius around the search location (Unit - Miles)
    String zip = "zip_example"; // String | To filter listing on ZIP around which they are listed
    Boolean includeLease = true; // Boolean | Boolean param to search for listings that include leasing options in them
    Boolean includeFinance = true; // Boolean | Boolean param to search for listings that include finance options in them
    String leaseTerm = "leaseTerm_example"; // String | Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term=30-60
    String leaseDownPayment = "leaseDownPayment_example"; // String | Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment=30-60
    String leaseEmp = "leaseEmp_example"; // String | Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp=30-60
    String financeLoanTerm = "financeLoanTerm_example"; // String | Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term=30-60
    String financeLoanApr = "financeLoanApr_example"; // String | Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr=30-60
    String financeEmp = "financeEmp_example"; // String | Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp=30-60
    String financeDownPayment = "financeDownPayment_example"; // String | Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment=30-60
    String financeDownPaymentPer = "financeDownPaymentPer_example"; // String | Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per=30-60
    String carType = "new"; // String | Car type. Allowed values are - new / used / certified
    String carfax1Owner = "true"; // String | Indicates whether car has had only one owner or not
    String carfaxCleanTitle = "true"; // String | Indicates whether car has clean ownership records
    String yearRange = "yearRange_example"; // String | Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
    String year = "year_example"; // String | To filter listing on their year
    String make = "make_example"; // String | To filter listings on their make
    String model = "model_example"; // String | To filter listings on their model
    String trim = "trim_example"; // String | To filter listing on their trim
    String dealerId = "dealerId_example"; // String | Dealer id to filter the listings.
    String vin = "vin_example"; // String | To filter listing on their VIN
    String source = "source_example"; // String | To filter listing on their source
    String bodyType = "bodyType_example"; // String | To filter listing on their body type
    String bodySubtype = "bodySubtype_example"; // String | Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
    String vehicleType = "vehicleType_example"; // String | To filter listing on their vehicle type
    String vins = "vins_example"; // String | Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc
    String taxonomyVins = "taxonomyVins_example"; // String | Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API.
    String mm = "mm_example"; // String | Make-Model concatenated string. To help passing the results of auto-complete API on mm field, use this parameter and pass in the selected value as is
    String ymm = "ymm_example"; // String | Year-Make-Model concatenated string. To help passing the results of auto-complete API on ymm field, use this parameter and pass in the selected value as is
    String ymmt = "ymmt_example"; // String | Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe '|' character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - 'year|make||' or 'year|make|model' or '|make|model|' combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the 'vins' or 'taxonomy_vins' parameter to the search api instead the year|make|model|trim combinations.
    String match = "match_example"; // String | Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
    String cylinders = "cylinders_example"; // String | To filter listing on their cylinders
    String transmission = "transmission_example"; // String | To filter listing on their transmission
    String doors = "doors_example"; // String | Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
    String drivetrain = "drivetrain_example"; // String | To filter listing on their drivetrain
    String exteriorColor = "exteriorColor_example"; // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    String interiorColor = "interiorColor_example"; // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    String baseExteriorColor = "baseExteriorColor_example"; // String | Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
    String baseInteriorColor = "baseInteriorColor_example"; // String | Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
    String engine = "engine_example"; // String | To filter listing on their engine
    String engineSize = "engineSize_example"; // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    String engineAspiration = "engineAspiration_example"; // String | Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
    String engineBlock = "engineBlock_example"; // String | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
    String highwayMpgRange = "highwayMpgRange_example"; // String | Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String cityMpgRange = "cityMpgRange_example"; // String | City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String milesRange = "milesRange_example"; // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    String priceRange = "priceRange_example"; // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String msrpRange = "msrpRange_example"; // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String domRange = "domRange_example"; // String | Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    String sortBy = "sortBy_example"; // String | Sort by field. Default sort field is distance from the given point
    String sortOrder = "asc"; // String | Sort order - asc or desc. Default sort order is asc
    Integer rows = 10; // Integer | Number of results to return. Default is 10. Max is 50
    Integer start = 0; // Integer | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    Boolean includeNonVinListings = false; // Boolean | To include non vin listings. Default is false
    String msaCode = "msaCode_example"; // String | To filter listing on msa code in which they are listed
    String facets = "facets_example"; // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    String rangeFacets = "rangeFacets_example"; // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    String facetSort = "count"; // String | Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
    String stats = "stats_example"; // String | The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
    String country = "US"; // String | To filter listing on Country in which they are listed
    Boolean plot = true; // Boolean | If plot has value true results in around 25k coordinates with limited fields to plot respective graph
    Boolean nodedup = true; // Boolean | If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
    Boolean dedup = true; // Boolean | If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
    Boolean owned = true; // Boolean | Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
    String state = "state_example"; // String | To filter listing on State in which they are listed
    String city = "city_example"; // String | To filter listing on City in which they are listed
    String dealerName = "dealerName_example"; // String | Filter listings on dealer_name
    String dealershipGroupName = "dealershipGroupName_example"; // String | Name of the dealership group to search for
    String trimO = "trimO_example"; // String | Filter listings on web scraped trim
    String trimR = "trimR_example"; // String | Filter trim on custom possible matches
    String domActiveRange = "domActiveRange_example"; // String | Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    String dom180Range = "dom180Range_example"; // String | Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    Boolean excludeCertified = true; // Boolean | Boolean param to exclude certified cars from search results
    String fuelType = "fuelType_example"; // String | To filter listing on their fuel type
    String dealerType = "franchise"; // String | Filter based on dealer type independant or franchise
    Boolean photoLinks = true; // Boolean | A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don't have them
    Boolean photoLinksCached = true; // Boolean | A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don't have them
    String stockNo = "stockNo_example"; // String | To filter listing on their stock number on lot
    String lastSeenRange = "lastSeenRange_example"; // String | Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenRange = "firstSeenRange_example"; // String | First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenAtSourceRange = "firstSeenAtSourceRange_example"; // String | First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenAtMcRange = "firstSeenAtMcRange_example"; // String | First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String lastSeenDays = "lastSeenDays_example"; // String | Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenDays = "firstSeenDays_example"; // String | First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenAtSourceDays = "firstSeenAtSourceDays_example"; // String | First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenAtMcDays = "firstSeenAtMcDays_example"; // String | First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
    Boolean includeRelevantLinks = false; // Boolean | To include_relevant_links. Default is true
    String inventoryCountRange = "inventoryCountRange_example"; // String | Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50
    String inTransit = "true"; // String | A boolean to filter in transit vehicles
    String seatingCapacity = "seatingCapacity_example"; // String | To filter on vehicle seating capacity
    String engineSizeRange = "engineSizeRange_example"; // String | Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
    String powertrainType = "powertrainType_example"; // String | To filter on powertrain_type
    String minPhotoLinks = "minPhotoLinks_example"; // String | Filter listings based by number of photo links within given range
    String minPhotoLinksCached = "minPhotoLinksCached_example"; // String | Filter listings based by number of cached photo links within given range
    try {
      SearchResponse result = apiInstance.carDealerInventoryActiveGet(apiKey, appendApiKey, latitude, longitude, radius, zip, includeLease, includeFinance, leaseTerm, leaseDownPayment, leaseEmp, financeLoanTerm, financeLoanApr, financeEmp, financeDownPayment, financeDownPaymentPer, carType, carfax1Owner, carfaxCleanTitle, yearRange, year, make, model, trim, dealerId, vin, source, bodyType, bodySubtype, vehicleType, vins, taxonomyVins, mm, ymm, ymmt, match, cylinders, transmission, doors, drivetrain, exteriorColor, interiorColor, baseExteriorColor, baseInteriorColor, engine, engineSize, engineAspiration, engineBlock, highwayMpgRange, cityMpgRange, milesRange, priceRange, msrpRange, domRange, sortBy, sortOrder, rows, start, includeNonVinListings, msaCode, facets, rangeFacets, facetSort, stats, country, plot, nodedup, dedup, owned, state, city, dealerName, dealershipGroupName, trimO, trimR, domActiveRange, dom180Range, excludeCertified, fuelType, dealerType, photoLinks, photoLinksCached, stockNo, lastSeenRange, firstSeenRange, firstSeenAtSourceRange, firstSeenAtMcRange, lastSeenDays, firstSeenDays, firstSeenAtSourceDays, firstSeenAtMcDays, includeRelevantLinks, inventoryCountRange, inTransit, seatingCapacity, engineSizeRange, powertrainType, minPhotoLinks, minPhotoLinksCached);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarSearchApi#carDealerInventoryActiveGet");
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
| **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true] |
| **latitude** | **Double**| Latitude component of location | [optional] |
| **longitude** | **Double**| Longitude component of location | [optional] |
| **radius** | **Integer**| Radius around the search location (Unit - Miles) | [optional] |
| **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] |
| **includeLease** | **Boolean**| Boolean param to search for listings that include leasing options in them | [optional] |
| **includeFinance** | **Boolean**| Boolean param to search for listings that include finance options in them | [optional] |
| **leaseTerm** | **String**| Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60 | [optional] |
| **leaseDownPayment** | **String**| Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60 | [optional] |
| **leaseEmp** | **String**| Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60 | [optional] |
| **financeLoanTerm** | **String**| Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60 | [optional] |
| **financeLoanApr** | **String**| Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60 | [optional] |
| **financeEmp** | **String**| Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60 | [optional] |
| **financeDownPayment** | **String**| Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60 | [optional] |
| **financeDownPaymentPer** | **String**| Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60 | [optional] |
| **carType** | **String**| Car type. Allowed values are - new / used / certified | [optional] [enum: new, used, certified] |
| **carfax1Owner** | **String**| Indicates whether car has had only one owner or not | [optional] [enum: true, false] |
| **carfaxCleanTitle** | **String**| Indicates whether car has clean ownership records | [optional] [enum: true, false] |
| **yearRange** | **String**| Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021 | [optional] |
| **year** | **String**| To filter listing on their year | [optional] |
| **make** | **String**| To filter listings on their make | [optional] |
| **model** | **String**| To filter listings on their model | [optional] |
| **trim** | **String**| To filter listing on their trim | [optional] |
| **dealerId** | **String**| Dealer id to filter the listings. | [optional] |
| **vin** | **String**| To filter listing on their VIN | [optional] |
| **source** | **String**| To filter listing on their source | [optional] |
| **bodyType** | **String**| To filter listing on their body type | [optional] |
| **bodySubtype** | **String**| Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] |
| **vehicleType** | **String**| To filter listing on their vehicle type | [optional] |
| **vins** | **String**| Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc | [optional] |
| **taxonomyVins** | **String**| Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API. | [optional] |
| **mm** | **String**| Make-Model concatenated string. To help passing the results of auto-complete API on mm field, use this parameter and pass in the selected value as is | [optional] |
| **ymm** | **String**| Year-Make-Model concatenated string. To help passing the results of auto-complete API on ymm field, use this parameter and pass in the selected value as is | [optional] |
| **ymmt** | **String**| Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations. | [optional] |
| **match** | **String**| Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match | [optional] |
| **cylinders** | **String**| To filter listing on their cylinders | [optional] |
| **transmission** | **String**| To filter listing on their transmission | [optional] |
| **doors** | **String**| Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated | [optional] |
| **drivetrain** | **String**| To filter listing on their drivetrain | [optional] |
| **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] |
| **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] |
| **baseExteriorColor** | **String**| Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated | [optional] |
| **baseInteriorColor** | **String**| Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated | [optional] |
| **engine** | **String**| To filter listing on their engine | [optional] |
| **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] |
| **engineAspiration** | **String**| Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated | [optional] |
| **engineBlock** | **String**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] |
| **highwayMpgRange** | **String**| Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **cityMpgRange** | **String**| City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **milesRange** | **String**| Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **priceRange** | **String**| Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **msrpRange** | **String**| MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **domRange** | **String**| Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] |
| **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] [enum: asc, desc, ASC, DESC] |
| **rows** | **Integer**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10] |
| **start** | **Integer**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0] |
| **includeNonVinListings** | **Boolean**| To include non vin listings. Default is false | [optional] [default to false] |
| **msaCode** | **String**| To filter listing on msa code in which they are listed | [optional] |
| **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] |
| **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] |
| **facetSort** | **String**| Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param | [optional] [default to count] [enum: count, index] |
| **stats** | **String**| The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. | [optional] |
| **country** | **String**| To filter listing on Country in which they are listed | [optional] [default to US] [enum: US, CA, us, ca, all, ALL] |
| **plot** | **Boolean**| If plot has value true results in around 25k coordinates with limited fields to plot respective graph | [optional] |
| **nodedup** | **Boolean**| If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin | [optional] |
| **dedup** | **Boolean**| If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source | [optional] |
| **owned** | **Boolean**| Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself | [optional] |
| **state** | **String**| To filter listing on State in which they are listed | [optional] |
| **city** | **String**| To filter listing on City in which they are listed | [optional] |
| **dealerName** | **String**| Filter listings on dealer_name | [optional] |
| **dealershipGroupName** | **String**| Name of the dealership group to search for | [optional] |
| **trimO** | **String**| Filter listings on web scraped trim | [optional] |
| **trimR** | **String**| Filter trim on custom possible matches | [optional] |
| **domActiveRange** | **String**| Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **dom180Range** | **String**| Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **excludeCertified** | **Boolean**| Boolean param to exclude certified cars from search results | [optional] |
| **fuelType** | **String**| To filter listing on their fuel type | [optional] |
| **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] [enum: franchise, independent] |
| **photoLinks** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them | [optional] |
| **photoLinksCached** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them | [optional] |
| **stockNo** | **String**| To filter listing on their stock number on lot | [optional] |
| **lastSeenRange** | **String**| Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenRange** | **String**| First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenAtSourceRange** | **String**| First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenAtMcRange** | **String**| First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **lastSeenDays** | **String**| Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenDays** | **String**| First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenAtSourceDays** | **String**| First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenAtMcDays** | **String**| First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **includeRelevantLinks** | **Boolean**| To include_relevant_links. Default is true | [optional] [default to false] |
| **inventoryCountRange** | **String**| Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **inTransit** | **String**| A boolean to filter in transit vehicles | [optional] [enum: true, false] |
| **seatingCapacity** | **String**| To filter on vehicle seating capacity | [optional] |
| **engineSizeRange** | **String**| Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2 | [optional] |
| **powertrainType** | **String**| To filter on powertrain_type | [optional] |
| **minPhotoLinks** | **String**| Filter listings based by number of photo links within given range | [optional] |
| **minPhotoLinksCached** | **String**| Filter listings based by number of cached photo links within given range | [optional] |

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of all cars listings matching the search &amp; filter criteria |  -  |
| **0** | Error |  -  |

<a id="getListing"></a>
# **getListing**
> Listing getListing(id, apiKey, appendApiKey, includeRelevantLinks)

Listing by id

Get a particular dealer listing by its id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarSearchApi apiInstance = new CarSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean appendApiKey = true; // Boolean | Flag on whether to include api_key in response API urls (if any)
    Boolean includeRelevantLinks = false; // Boolean | To include_relevant_links. Default is true
    try {
      Listing result = apiInstance.getListing(id, apiKey, appendApiKey, includeRelevantLinks);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarSearchApi#getListing");
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
| **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true] |
| **includeRelevantLinks** | **Boolean**| To include_relevant_links. Default is true | [optional] [default to false] |

### Return type

[**Listing**](Listing.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Listing for the given id |  -  |
| **0** | Error |  -  |

<a id="listingCarAuctionIdExtraGet"></a>
# **listingCarAuctionIdExtraGet**
> ListingExtraAttributes listingCarAuctionIdExtraGet(id, apiKey)

Long text Listings attributes for Listing with the given id

Get listing options, features, seller comments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarSearchApi apiInstance = new CarSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    try {
      ListingExtraAttributes result = apiInstance.listingCarAuctionIdExtraGet(id, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarSearchApi#listingCarAuctionIdExtraGet");
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
| **200** | ListingAttributes for the given listing id |  -  |
| **0** | Error |  -  |

<a id="listingCarAuctionIdGet"></a>
# **listingCarAuctionIdGet**
> Listing listingCarAuctionIdGet(id, apiKey, appendApiKey, includeRelevantLinks)

Listing by id

Get a particular auction listing by its id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarSearchApi apiInstance = new CarSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean appendApiKey = true; // Boolean | Flag on whether to include api_key in response API urls (if any)
    Boolean includeRelevantLinks = false; // Boolean | To include_relevant_links. Default is true
    try {
      Listing result = apiInstance.listingCarAuctionIdGet(id, apiKey, appendApiKey, includeRelevantLinks);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarSearchApi#listingCarAuctionIdGet");
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
| **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true] |
| **includeRelevantLinks** | **Boolean**| To include_relevant_links. Default is true | [optional] [default to false] |

### Return type

[**Listing**](Listing.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Listing for the given id |  -  |
| **0** | Error |  -  |

<a id="listingCarAuctionIdMediaGet"></a>
# **listingCarAuctionIdMediaGet**
> ListingMedia listingCarAuctionIdMediaGet(id, apiKey, appendApiKey)

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
import org.openapitools.client.api.CarSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarSearchApi apiInstance = new CarSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean appendApiKey = true; // Boolean | Flag on whether to include api_key in response API urls (if any)
    try {
      ListingMedia result = apiInstance.listingCarAuctionIdMediaGet(id, apiKey, appendApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarSearchApi#listingCarAuctionIdMediaGet");
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
| **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true] |

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
| **200** | ListingMedia for the given listing id |  -  |
| **0** | Error |  -  |

<a id="listingCarFsboIdExtraGet"></a>
# **listingCarFsboIdExtraGet**
> ListingExtraAttributes listingCarFsboIdExtraGet(id, apiKey)

Long text Listings attributes for Listing with the given id

Get listing options, features, seller comments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarSearchApi apiInstance = new CarSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    try {
      ListingExtraAttributes result = apiInstance.listingCarFsboIdExtraGet(id, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarSearchApi#listingCarFsboIdExtraGet");
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
| **200** | ListingAttributes for the given listing id |  -  |
| **0** | Error |  -  |

<a id="listingCarFsboIdGet"></a>
# **listingCarFsboIdGet**
> Listing listingCarFsboIdGet(id, apiKey, appendApiKey, includeRelevantLinks)

Listing by id

Get a particular private party listing by its id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarSearchApi apiInstance = new CarSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean appendApiKey = true; // Boolean | Flag on whether to include api_key in response API urls (if any)
    Boolean includeRelevantLinks = false; // Boolean | To include_relevant_links. Default is true
    try {
      Listing result = apiInstance.listingCarFsboIdGet(id, apiKey, appendApiKey, includeRelevantLinks);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarSearchApi#listingCarFsboIdGet");
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
| **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true] |
| **includeRelevantLinks** | **Boolean**| To include_relevant_links. Default is true | [optional] [default to false] |

### Return type

[**Listing**](Listing.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Listing for the given id |  -  |
| **0** | Error |  -  |

<a id="listingCarFsboIdMediaGet"></a>
# **listingCarFsboIdMediaGet**
> ListingMedia listingCarFsboIdMediaGet(id, apiKey, appendApiKey)

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
import org.openapitools.client.api.CarSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarSearchApi apiInstance = new CarSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean appendApiKey = true; // Boolean | Flag on whether to include api_key in response API urls (if any)
    try {
      ListingMedia result = apiInstance.listingCarFsboIdMediaGet(id, apiKey, appendApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarSearchApi#listingCarFsboIdMediaGet");
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
| **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true] |

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
| **200** | ListingMedia for the given listing id |  -  |
| **0** | Error |  -  |

<a id="listingCarIdExtraGet"></a>
# **listingCarIdExtraGet**
> ListingExtraAttributes listingCarIdExtraGet(id, apiKey)

Long text Listings attributes for Listing with the given id

Get listing options, features, seller comments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarSearchApi apiInstance = new CarSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    try {
      ListingExtraAttributes result = apiInstance.listingCarIdExtraGet(id, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarSearchApi#listingCarIdExtraGet");
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
| **200** | ListingAttributes for the given listing id |  -  |
| **0** | Error |  -  |

<a id="listingCarIdMediaGet"></a>
# **listingCarIdMediaGet**
> ListingMedia listingCarIdMediaGet(id, apiKey, appendApiKey)

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
import org.openapitools.client.api.CarSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarSearchApi apiInstance = new CarSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean appendApiKey = true; // Boolean | Flag on whether to include api_key in response API urls (if any)
    try {
      ListingMedia result = apiInstance.listingCarIdMediaGet(id, apiKey, appendApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarSearchApi#listingCarIdMediaGet");
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
| **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true] |

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
| **200** | ListingMedia for the given listing id |  -  |
| **0** | Error |  -  |

<a id="listingCarUkIdExtraGet"></a>
# **listingCarUkIdExtraGet**
> ListingExtraAttributes listingCarUkIdExtraGet(id, apiKey)

Long text Listings attributes for Listing with the given id

Get listing options, features, seller comments

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarSearchApi apiInstance = new CarSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    try {
      ListingExtraAttributes result = apiInstance.listingCarUkIdExtraGet(id, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarSearchApi#listingCarUkIdExtraGet");
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
| **200** | ListingAttributes for the given listing id |  -  |
| **0** | Error |  -  |

<a id="listingCarUkIdGet"></a>
# **listingCarUkIdGet**
> Listing listingCarUkIdGet(id, apiKey, appendApiKey)

Listing by id

Get a particular dealer listing by its id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarSearchApi apiInstance = new CarSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean appendApiKey = true; // Boolean | Flag on whether to include api_key in response API urls (if any)
    try {
      Listing result = apiInstance.listingCarUkIdGet(id, apiKey, appendApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarSearchApi#listingCarUkIdGet");
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
| **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true] |

### Return type

[**Listing**](Listing.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Listing for the given id |  -  |
| **0** | Error |  -  |

<a id="listingCarUkIdMediaGet"></a>
# **listingCarUkIdMediaGet**
> ListingMedia listingCarUkIdMediaGet(id, apiKey, appendApiKey)

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
import org.openapitools.client.api.CarSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarSearchApi apiInstance = new CarSearchApi(defaultClient);
    String id = "id_example"; // String | Listing id to get all the listing attributes
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean appendApiKey = true; // Boolean | Flag on whether to include api_key in response API urls (if any)
    try {
      ListingMedia result = apiInstance.listingCarUkIdMediaGet(id, apiKey, appendApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarSearchApi#listingCarUkIdMediaGet");
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
| **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true] |

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
| **200** | ListingMedia for the given listing id |  -  |
| **0** | Error |  -  |

<a id="search"></a>
# **search**
> UKSearchResponse search(apiKey, appendApiKey, latitude, longitude, radius, postalCode, zip, carType, year, yearRange, make, model, variant, trim, bodyType, ymmt, transmission, doors, drivetrain, exteriorColor, interiorColor, engine, milesRange, priceRange, msrpRange, sortBy, sortOrder, rows, start, msaCode, facets, rangeFacets, facetSort, stats, country, plot, nodedup, dedup, county, state, city, fuelType, stockNo, domRange, domActiveRange, dom180Range, lastSeenRange, firstSeenRange, firstSeenAtSourceRange, firstSeenAtMcRange, lastSeenDays, firstSeenDays, firstSeenAtSourceDays, firstSeenAtMcDays, co2Emissions, insuranceGroup, vehicleRegistrationMark, vehicleRegistrationDateRange, numOwners, inventoryCountRange, source, dealerId, excludeSources, excludeDealerIds, inTransit, includeNonVinListings, cylinders, photoLinks, photoLinksCached, baseExteriorColor, baseInteriorColor, writeOffCategory, excludeWriteOffCategory, fcaStatus, seatingCapacity, vrm, powertrainType, clientFilters, boost, carLocationSellerName, carLocationStreet, carLocationCity, carLocationCounty, carLocationZip, carLocationLatitude, carLocationLongitude, priceChange, priceChangeRange, activeInventoryDateRange, engineSize, engineSizeRange, uvcId, highwayMpgRange, cityMpgRange, combinedMpgRange, owned, minPhotoLinks, minPhotoLinksCached, match, ulezCompliant)

Gets active car listings in UK for the given search criteria

Search cars for sale in UK

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarSearchApi apiInstance = new CarSearchApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean appendApiKey = false; // Boolean | Flag on whether to include api_key in response API urls (if any)
    Double latitude = 3.4D; // Double | Latitude component of location
    Double longitude = 3.4D; // Double | Longitude component of location
    Integer radius = 56; // Integer | Radius around the search location (Unit - Miles)
    String postalCode = "postalCode_example"; // String | To filter listing on postal code around which they are listed
    String zip = "zip_example"; // String | To filter listing on ZIP around which they are listed
    String carType = "new"; // String | Car type. Allowed values are - new / used
    String year = "year_example"; // String | To filter listing on their year
    String yearRange = "yearRange_example"; // String | Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
    String make = "make_example"; // String | To filter listings on their make
    String model = "model_example"; // String | To filter listings on their model
    String variant = "variant_example"; // String | To filter listing on their variant
    String trim = "trim_example"; // String | To filter listing on their trim
    String bodyType = "bodyType_example"; // String | To filter listing on their body type
    String ymmt = "ymmt_example"; // String | Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe '|' character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - 'year|make||' or 'year|make|model' or '|make|model|' combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the 'vins' or 'taxonomy_vins' parameter to the search api instead the year|make|model|trim combinations.
    String transmission = "transmission_example"; // String | To filter listing on their transmission
    String doors = "doors_example"; // String | Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
    String drivetrain = "drivetrain_example"; // String | To filter listing on their drivetrain
    String exteriorColor = "exteriorColor_example"; // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    String interiorColor = "interiorColor_example"; // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    String engine = "engine_example"; // String | To filter listing on their engine
    String milesRange = "milesRange_example"; // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    String priceRange = "priceRange_example"; // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String msrpRange = "msrpRange_example"; // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String sortBy = "sortBy_example"; // String | Sort by field. Default sort field is distance from the given point
    String sortOrder = "asc"; // String | Sort order - asc or desc. Default sort order is asc
    Integer rows = 10; // Integer | Number of results to return. Default is 10. Max is 50
    Integer start = 0; // Integer | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    String msaCode = "msaCode_example"; // String | To filter listing on msa code in which they are listed
    String facets = "facets_example"; // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    String rangeFacets = "rangeFacets_example"; // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    String facetSort = "count"; // String | Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
    String stats = "stats_example"; // String | The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
    String country = "uk"; // String | To filter listing on Country in which they are listed
    Boolean plot = true; // Boolean | If plot has value true results in around 25k coordinates with limited fields to plot respective graph
    Boolean nodedup = true; // Boolean | If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
    Boolean dedup = true; // Boolean | If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
    String county = "county_example"; // String | To filter listing on county in which they are listed
    String state = "state_example"; // String | To filter listing on State in which they are listed
    String city = "city_example"; // String | To filter listing on City in which they are listed
    String fuelType = "fuelType_example"; // String | To filter listing on their fuel type
    String stockNo = "stockNo_example"; // String | To filter listing on their stock number on lot
    String domRange = "domRange_example"; // String | Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    String domActiveRange = "domActiveRange_example"; // String | Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    String dom180Range = "dom180Range_example"; // String | Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    String lastSeenRange = "lastSeenRange_example"; // String | Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenRange = "firstSeenRange_example"; // String | First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenAtSourceRange = "firstSeenAtSourceRange_example"; // String | First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenAtMcRange = "firstSeenAtMcRange_example"; // String | First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String lastSeenDays = "lastSeenDays_example"; // String | Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenDays = "firstSeenDays_example"; // String | First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenAtSourceDays = "firstSeenAtSourceDays_example"; // String | First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenAtMcDays = "firstSeenAtMcDays_example"; // String | First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
    String co2Emissions = "co2Emissions_example"; // String | CO2 emissions
    String insuranceGroup = "insuranceGroup_example"; // String | Insurance Group
    String vehicleRegistrationMark = "vehicleRegistrationMark_example"; // String | Vehicle Registration Mark
    String vehicleRegistrationDateRange = "vehicleRegistrationDateRange_example"; // String | Vehicle registration date range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String numOwners = "numOwners_example"; // String | Number of owners. Range to be given in the format - min-max e.g. 1000-5000
    String inventoryCountRange = "inventoryCountRange_example"; // String | Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50
    String source = "source_example"; // String | To filter listing on their source only for widget requests
    String dealerId = "dealerId_example"; // String | Dealer id to filter the listings.
    String excludeSources = "excludeSources_example"; // String | A list of sources to exclude from result
    String excludeDealerIds = "excludeDealerIds_example"; // String | A list of dealer ids to exclude from result
    String inTransit = "true"; // String | A boolean to filter in transit vehicles
    Boolean includeNonVinListings = false; // Boolean | To include non vin listings. Default is false
    String cylinders = "cylinders_example"; // String | To filter listing on their cylinders
    Boolean photoLinks = true; // Boolean | A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don't have them
    Boolean photoLinksCached = true; // Boolean | A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don't have them
    String baseExteriorColor = "baseExteriorColor_example"; // String | Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
    String baseInteriorColor = "baseInteriorColor_example"; // String | Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
    String writeOffCategory = "writeOffCategory_example"; // String | write off category
    String excludeWriteOffCategory = "excludeWriteOffCategory_example"; // String | To exclude write off category
    String fcaStatus = "fcaStatus_example"; // String | To filter on fca status
    String seatingCapacity = "seatingCapacity_example"; // String | To filter on vehicle seating capacity
    String vrm = "vrm_example"; // String | To filter on vrm
    String powertrainType = "powertrainType_example"; // String | To filter on powertrain_type
    Boolean clientFilters = true; // Boolean | Flag to add explicit filters set on client level in solr
    Boolean boost = true; // Boolean | Flag to sort listings based on client filter score in solr
    String carLocationSellerName = "carLocationSellerName_example"; // String | Filter cars on seller name
    String carLocationStreet = "carLocationStreet_example"; // String | Filter cars on street name
    String carLocationCity = "carLocationCity_example"; // String | Filter cars on city
    String carLocationCounty = "carLocationCounty_example"; // String | Filter cars on county
    String carLocationZip = "carLocationZip_example"; // String | To filter listing on car ZIP around which they are listed
    Double carLocationLatitude = 3.4D; // Double | Latitude component of car location
    Double carLocationLongitude = 3.4D; // Double | Longitude component of car location
    String priceChange = "positive"; // String | Query to filter listings based on their positive and negative price change
    String priceChangeRange = "priceChangeRange_example"; // String | Price change range to filter listings with price change within given price_change_range. Range to be given in the format - min-max e.g. 10-500
    String activeInventoryDateRange = "activeInventoryDateRange_example"; // String | date range to filter listings that were active within given date range. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String engineSize = "engineSize_example"; // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    String engineSizeRange = "engineSizeRange_example"; // String | Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
    String uvcId = "uvcId_example"; // String | To filter on uvc id
    String highwayMpgRange = "highwayMpgRange_example"; // String | Highway mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String cityMpgRange = "cityMpgRange_example"; // String | City mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String combinedMpgRange = "combinedMpgRange_example"; // String | Combined mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    Boolean owned = true; // Boolean | Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
    String minPhotoLinks = "minPhotoLinks_example"; // String | Filter listings based by number of photo links within given range
    String minPhotoLinksCached = "minPhotoLinksCached_example"; // String | Filter listings based by number of cached photo links within given range
    String match = "match_example"; // String | Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
    Boolean ulezCompliant = true; // Boolean | Filter listings based on drive into ultra low emmition zone
    try {
      UKSearchResponse result = apiInstance.search(apiKey, appendApiKey, latitude, longitude, radius, postalCode, zip, carType, year, yearRange, make, model, variant, trim, bodyType, ymmt, transmission, doors, drivetrain, exteriorColor, interiorColor, engine, milesRange, priceRange, msrpRange, sortBy, sortOrder, rows, start, msaCode, facets, rangeFacets, facetSort, stats, country, plot, nodedup, dedup, county, state, city, fuelType, stockNo, domRange, domActiveRange, dom180Range, lastSeenRange, firstSeenRange, firstSeenAtSourceRange, firstSeenAtMcRange, lastSeenDays, firstSeenDays, firstSeenAtSourceDays, firstSeenAtMcDays, co2Emissions, insuranceGroup, vehicleRegistrationMark, vehicleRegistrationDateRange, numOwners, inventoryCountRange, source, dealerId, excludeSources, excludeDealerIds, inTransit, includeNonVinListings, cylinders, photoLinks, photoLinksCached, baseExteriorColor, baseInteriorColor, writeOffCategory, excludeWriteOffCategory, fcaStatus, seatingCapacity, vrm, powertrainType, clientFilters, boost, carLocationSellerName, carLocationStreet, carLocationCity, carLocationCounty, carLocationZip, carLocationLatitude, carLocationLongitude, priceChange, priceChangeRange, activeInventoryDateRange, engineSize, engineSizeRange, uvcId, highwayMpgRange, cityMpgRange, combinedMpgRange, owned, minPhotoLinks, minPhotoLinksCached, match, ulezCompliant);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarSearchApi#search");
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
| **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to false] |
| **latitude** | **Double**| Latitude component of location | [optional] |
| **longitude** | **Double**| Longitude component of location | [optional] |
| **radius** | **Integer**| Radius around the search location (Unit - Miles) | [optional] |
| **postalCode** | **String**| To filter listing on postal code around which they are listed | [optional] |
| **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] |
| **carType** | **String**| Car type. Allowed values are - new / used | [optional] [enum: new, used] |
| **year** | **String**| To filter listing on their year | [optional] |
| **yearRange** | **String**| Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021 | [optional] |
| **make** | **String**| To filter listings on their make | [optional] |
| **model** | **String**| To filter listings on their model | [optional] |
| **variant** | **String**| To filter listing on their variant | [optional] |
| **trim** | **String**| To filter listing on their trim | [optional] |
| **bodyType** | **String**| To filter listing on their body type | [optional] |
| **ymmt** | **String**| Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations. | [optional] |
| **transmission** | **String**| To filter listing on their transmission | [optional] |
| **doors** | **String**| Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated | [optional] |
| **drivetrain** | **String**| To filter listing on their drivetrain | [optional] |
| **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] |
| **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] |
| **engine** | **String**| To filter listing on their engine | [optional] |
| **milesRange** | **String**| Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **priceRange** | **String**| Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **msrpRange** | **String**| MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] |
| **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] [enum: asc, desc, ASC, DESC] |
| **rows** | **Integer**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10] |
| **start** | **Integer**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0] |
| **msaCode** | **String**| To filter listing on msa code in which they are listed | [optional] |
| **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] |
| **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] |
| **facetSort** | **String**| Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param | [optional] [default to count] [enum: count, index] |
| **stats** | **String**| The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. | [optional] |
| **country** | **String**| To filter listing on Country in which they are listed | [optional] [default to uk] [enum: uk, england, scotland, northan ireland, wales] |
| **plot** | **Boolean**| If plot has value true results in around 25k coordinates with limited fields to plot respective graph | [optional] |
| **nodedup** | **Boolean**| If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin | [optional] |
| **dedup** | **Boolean**| If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source | [optional] |
| **county** | **String**| To filter listing on county in which they are listed | [optional] |
| **state** | **String**| To filter listing on State in which they are listed | [optional] |
| **city** | **String**| To filter listing on City in which they are listed | [optional] |
| **fuelType** | **String**| To filter listing on their fuel type | [optional] |
| **stockNo** | **String**| To filter listing on their stock number on lot | [optional] |
| **domRange** | **String**| Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **domActiveRange** | **String**| Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **dom180Range** | **String**| Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **lastSeenRange** | **String**| Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenRange** | **String**| First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenAtSourceRange** | **String**| First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenAtMcRange** | **String**| First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **lastSeenDays** | **String**| Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenDays** | **String**| First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenAtSourceDays** | **String**| First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenAtMcDays** | **String**| First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **co2Emissions** | **String**| CO2 emissions | [optional] |
| **insuranceGroup** | **String**| Insurance Group | [optional] |
| **vehicleRegistrationMark** | **String**| Vehicle Registration Mark | [optional] |
| **vehicleRegistrationDateRange** | **String**| Vehicle registration date range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **numOwners** | **String**| Number of owners. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **inventoryCountRange** | **String**| Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **source** | **String**| To filter listing on their source only for widget requests | [optional] |
| **dealerId** | **String**| Dealer id to filter the listings. | [optional] |
| **excludeSources** | **String**| A list of sources to exclude from result | [optional] |
| **excludeDealerIds** | **String**| A list of dealer ids to exclude from result | [optional] |
| **inTransit** | **String**| A boolean to filter in transit vehicles | [optional] [enum: true, false] |
| **includeNonVinListings** | **Boolean**| To include non vin listings. Default is false | [optional] [default to false] |
| **cylinders** | **String**| To filter listing on their cylinders | [optional] |
| **photoLinks** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them | [optional] |
| **photoLinksCached** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them | [optional] |
| **baseExteriorColor** | **String**| Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated | [optional] |
| **baseInteriorColor** | **String**| Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated | [optional] |
| **writeOffCategory** | **String**| write off category | [optional] |
| **excludeWriteOffCategory** | **String**| To exclude write off category | [optional] |
| **fcaStatus** | **String**| To filter on fca status | [optional] |
| **seatingCapacity** | **String**| To filter on vehicle seating capacity | [optional] |
| **vrm** | **String**| To filter on vrm | [optional] |
| **powertrainType** | **String**| To filter on powertrain_type | [optional] |
| **clientFilters** | **Boolean**| Flag to add explicit filters set on client level in solr | [optional] [default to true] |
| **boost** | **Boolean**| Flag to sort listings based on client filter score in solr | [optional] [default to true] |
| **carLocationSellerName** | **String**| Filter cars on seller name | [optional] |
| **carLocationStreet** | **String**| Filter cars on street name | [optional] |
| **carLocationCity** | **String**| Filter cars on city | [optional] |
| **carLocationCounty** | **String**| Filter cars on county | [optional] |
| **carLocationZip** | **String**| To filter listing on car ZIP around which they are listed | [optional] |
| **carLocationLatitude** | **Double**| Latitude component of car location | [optional] |
| **carLocationLongitude** | **Double**| Longitude component of car location | [optional] |
| **priceChange** | **String**| Query to filter listings based on their positive and negative price change | [optional] [enum: positive, negative] |
| **priceChangeRange** | **String**| Price change range to filter listings with price change within given price_change_range. Range to be given in the format - min-max e.g. 10-500 | [optional] |
| **activeInventoryDateRange** | **String**| date range to filter listings that were active within given date range. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] |
| **engineSizeRange** | **String**| Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2 | [optional] |
| **uvcId** | **String**| To filter on uvc id | [optional] |
| **highwayMpgRange** | **String**| Highway mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **cityMpgRange** | **String**| City mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **combinedMpgRange** | **String**| Combined mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **owned** | **Boolean**| Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself | [optional] |
| **minPhotoLinks** | **String**| Filter listings based by number of photo links within given range | [optional] |
| **minPhotoLinksCached** | **String**| Filter listings based by number of cached photo links within given range | [optional] |
| **match** | **String**| Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match | [optional] |
| **ulezCompliant** | **Boolean**| Filter listings based on drive into ultra low emmition zone | [optional] |

### Return type

[**UKSearchResponse**](UKSearchResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of all cars listings matching the search &amp; filter criteria |  -  |
| **0** | Error |  -  |

<a id="searchCarActiveGet"></a>
# **searchCarActiveGet**
> SearchResponse searchCarActiveGet(apiKey, appendApiKey, latitude, longitude, radius, zip, includeLease, includeFinance, leaseTerm, leaseDownPayment, leaseEmp, financeLoanTerm, financeLoanApr, financeEmp, financeDownPayment, financeDownPaymentPer, carType, carfax1Owner, carfaxCleanTitle, yearRange, year, make, model, trim, vin, bodyType, bodySubtype, vehicleType, vins, taxonomyVins, mm, ymm, ymmt, match, cylinders, transmission, doors, drivetrain, exteriorColor, interiorColor, baseExteriorColor, baseInteriorColor, engine, engineSize, engineAspiration, engineBlock, highwayMpgRange, cityMpgRange, milesRange, priceRange, msrpRange, domRange, sortBy, sortOrder, rows, start, includeNonVinListings, msaCode, facets, rangeFacets, facetSort, stats, country, plot, nodedup, dedup, owned, source, state, city, trimO, trimR, domActiveRange, dom180Range, excludeCertified, fuelType, dealerType, photoLinks, photoLinksCached, stockNo, lastSeenRange, firstSeenRange, firstSeenAtSourceRange, firstSeenAtMcRange, lastSeenDays, firstSeenDays, firstSeenAtSourceDays, firstSeenAtMcDays, includeRelevantLinks, inventoryCountRange, dealerId, excludeDealerIds, excludeSources, inTransit, seatingCapacity, powertrainType, priceChange, priceChangeRange, activeInventoryDateRange, engineSizeRange, highValueFeatures, minPhotoLinks, minPhotoLinksCached, clientFilters)

Gets active car listings for the given search criteria

This endpoint is the meat of the API and serves many purposes. This API produces a list of currently active cars from the market for the given search criteria. The API results are limited to allow pagination upto 10000 rows.   The search API facilitates the following use cases -  1. Search Cars around a given geo-point within a given radius  2. Search cars for a specific year / make / model or combination of these  3. Search cars matching multiple year, make, model combinatins in the same search request 4. Filter results by most car specification attributes 5. Search for similar cars by VIN or Taxonomy VIN  6. Filter cars within a given price / miles / days on market (dom) range 7. Specify a sort order for the results on price / miles / dom / listed date  8. Search cars for a given City / State combination  9. Get Facets to build the search drill downs  10. Get Market averages for price/miles/dom for your search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarSearchApi apiInstance = new CarSearchApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean appendApiKey = true; // Boolean | Flag on whether to include api_key in response API urls (if any)
    Double latitude = 3.4D; // Double | Latitude component of location
    Double longitude = 3.4D; // Double | Longitude component of location
    Integer radius = 56; // Integer | Radius around the search location (Unit - Miles)
    String zip = "zip_example"; // String | To filter listing on ZIP around which they are listed
    Boolean includeLease = true; // Boolean | Boolean param to search for listings that include leasing options in them
    Boolean includeFinance = true; // Boolean | Boolean param to search for listings that include finance options in them
    String leaseTerm = "leaseTerm_example"; // String | Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term=30-60
    String leaseDownPayment = "leaseDownPayment_example"; // String | Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment=30-60
    String leaseEmp = "leaseEmp_example"; // String | Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp=30-60
    String financeLoanTerm = "financeLoanTerm_example"; // String | Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term=30-60
    String financeLoanApr = "financeLoanApr_example"; // String | Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr=30-60
    String financeEmp = "financeEmp_example"; // String | Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp=30-60
    String financeDownPayment = "financeDownPayment_example"; // String | Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment=30-60
    String financeDownPaymentPer = "financeDownPaymentPer_example"; // String | Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per=30-60
    String carType = "new"; // String | Car type. Allowed values are - new / used / certified
    String carfax1Owner = "true"; // String | Indicates whether car has had only one owner or not
    String carfaxCleanTitle = "true"; // String | Indicates whether car has clean ownership records
    String yearRange = "yearRange_example"; // String | Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
    String year = "year_example"; // String | To filter listing on their year
    String make = "make_example"; // String | To filter listings on their make
    String model = "model_example"; // String | To filter listings on their model
    String trim = "trim_example"; // String | To filter listing on their trim
    String vin = "vin_example"; // String | To filter listing on their VIN
    String bodyType = "bodyType_example"; // String | To filter listing on their body type
    String bodySubtype = "bodySubtype_example"; // String | Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
    String vehicleType = "vehicleType_example"; // String | To filter listing on their vehicle type
    String vins = "vins_example"; // String | Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc
    String taxonomyVins = "taxonomyVins_example"; // String | Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API.
    String mm = "mm_example"; // String | Make-Model concatenated string. To help passing the results of auto-complete API on mm field, use this parameter and pass in the selected value as is
    String ymm = "ymm_example"; // String | Year-Make-Model concatenated string. To help passing the results of auto-complete API on ymm field, use this parameter and pass in the selected value as is
    String ymmt = "ymmt_example"; // String | Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe '|' character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - 'year|make||' or 'year|make|model' or '|make|model|' combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the 'vins' or 'taxonomy_vins' parameter to the search api instead the year|make|model|trim combinations.
    String match = "match_example"; // String | Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
    String cylinders = "cylinders_example"; // String | To filter listing on their cylinders
    String transmission = "transmission_example"; // String | To filter listing on their transmission
    String doors = "doors_example"; // String | Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
    String drivetrain = "drivetrain_example"; // String | To filter listing on their drivetrain
    String exteriorColor = "exteriorColor_example"; // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    String interiorColor = "interiorColor_example"; // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    String baseExteriorColor = "baseExteriorColor_example"; // String | Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
    String baseInteriorColor = "baseInteriorColor_example"; // String | Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
    String engine = "engine_example"; // String | To filter listing on their engine
    String engineSize = "engineSize_example"; // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    String engineAspiration = "engineAspiration_example"; // String | Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
    String engineBlock = "engineBlock_example"; // String | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
    String highwayMpgRange = "highwayMpgRange_example"; // String | Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String cityMpgRange = "cityMpgRange_example"; // String | City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String milesRange = "milesRange_example"; // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    String priceRange = "priceRange_example"; // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String msrpRange = "msrpRange_example"; // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String domRange = "domRange_example"; // String | Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    String sortBy = "sortBy_example"; // String | Sort by field. Default sort field is distance from the given point
    String sortOrder = "asc"; // String | Sort order - asc or desc. Default sort order is asc
    Integer rows = 10; // Integer | Number of results to return. Default is 10. Max is 50
    Integer start = 0; // Integer | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    Boolean includeNonVinListings = false; // Boolean | To include non vin listings. Default is false
    String msaCode = "msaCode_example"; // String | To filter listing on msa code in which they are listed
    String facets = "facets_example"; // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    String rangeFacets = "rangeFacets_example"; // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    String facetSort = "count"; // String | Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
    String stats = "stats_example"; // String | The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
    String country = "US"; // String | To filter listing on Country in which they are listed
    Boolean plot = true; // Boolean | If plot has value true results in around 25k coordinates with limited fields to plot respective graph
    Boolean nodedup = true; // Boolean | If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
    Boolean dedup = true; // Boolean | If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
    Boolean owned = true; // Boolean | Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
    String source = "source_example"; // String | To filter listing on their source only for widget requests
    String state = "state_example"; // String | To filter listing on State in which they are listed
    String city = "city_example"; // String | To filter listing on City in which they are listed
    String trimO = "trimO_example"; // String | Filter listings on web scraped trim
    String trimR = "trimR_example"; // String | Filter trim on custom possible matches
    String domActiveRange = "domActiveRange_example"; // String | Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    String dom180Range = "dom180Range_example"; // String | Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    Boolean excludeCertified = true; // Boolean | Boolean param to exclude certified cars from search results
    String fuelType = "fuelType_example"; // String | To filter listing on their fuel type
    String dealerType = "franchise"; // String | Filter based on dealer type independant or franchise
    Boolean photoLinks = true; // Boolean | A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don't have them
    Boolean photoLinksCached = true; // Boolean | A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don't have them
    String stockNo = "stockNo_example"; // String | To filter listing on their stock number on lot
    String lastSeenRange = "lastSeenRange_example"; // String | Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenRange = "firstSeenRange_example"; // String | First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenAtSourceRange = "firstSeenAtSourceRange_example"; // String | First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenAtMcRange = "firstSeenAtMcRange_example"; // String | First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String lastSeenDays = "lastSeenDays_example"; // String | Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenDays = "firstSeenDays_example"; // String | First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenAtSourceDays = "firstSeenAtSourceDays_example"; // String | First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenAtMcDays = "firstSeenAtMcDays_example"; // String | First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
    Boolean includeRelevantLinks = false; // Boolean | To include_relevant_links. Default is true
    String inventoryCountRange = "inventoryCountRange_example"; // String | Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50
    String dealerId = "dealerId_example"; // String | Dealer id to filter the listings.
    String excludeDealerIds = "excludeDealerIds_example"; // String | A list of dealer ids to exclude from result
    String excludeSources = "excludeSources_example"; // String | A list of sources to exclude from result
    String inTransit = "true"; // String | A boolean to filter in transit vehicles
    String seatingCapacity = "seatingCapacity_example"; // String | To filter on vehicle seating capacity
    String powertrainType = "powertrainType_example"; // String | To filter on powertrain_type
    String priceChange = "positive"; // String | Query to filter listings based on their positive and negative price change
    String priceChangeRange = "priceChangeRange_example"; // String | Price change range to filter listings with price change within given price_change_range. Range to be given in the format - min-max e.g. 10-500
    String activeInventoryDateRange = "activeInventoryDateRange_example"; // String | date range to filter listings that were active within given date range. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String engineSizeRange = "engineSizeRange_example"; // String | Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
    String highValueFeatures = "highValueFeatures_example"; // String | To filter listings on their high_value_features. Results will be intersection of provided HVFs
    String minPhotoLinks = "minPhotoLinks_example"; // String | Filter listings based by number of photo links within given range
    String minPhotoLinksCached = "minPhotoLinksCached_example"; // String | Filter listings based by number of cached photo links within given range
    Boolean clientFilters = true; // Boolean | Flag to add explicit filters set on client level in solr
    try {
      SearchResponse result = apiInstance.searchCarActiveGet(apiKey, appendApiKey, latitude, longitude, radius, zip, includeLease, includeFinance, leaseTerm, leaseDownPayment, leaseEmp, financeLoanTerm, financeLoanApr, financeEmp, financeDownPayment, financeDownPaymentPer, carType, carfax1Owner, carfaxCleanTitle, yearRange, year, make, model, trim, vin, bodyType, bodySubtype, vehicleType, vins, taxonomyVins, mm, ymm, ymmt, match, cylinders, transmission, doors, drivetrain, exteriorColor, interiorColor, baseExteriorColor, baseInteriorColor, engine, engineSize, engineAspiration, engineBlock, highwayMpgRange, cityMpgRange, milesRange, priceRange, msrpRange, domRange, sortBy, sortOrder, rows, start, includeNonVinListings, msaCode, facets, rangeFacets, facetSort, stats, country, plot, nodedup, dedup, owned, source, state, city, trimO, trimR, domActiveRange, dom180Range, excludeCertified, fuelType, dealerType, photoLinks, photoLinksCached, stockNo, lastSeenRange, firstSeenRange, firstSeenAtSourceRange, firstSeenAtMcRange, lastSeenDays, firstSeenDays, firstSeenAtSourceDays, firstSeenAtMcDays, includeRelevantLinks, inventoryCountRange, dealerId, excludeDealerIds, excludeSources, inTransit, seatingCapacity, powertrainType, priceChange, priceChangeRange, activeInventoryDateRange, engineSizeRange, highValueFeatures, minPhotoLinks, minPhotoLinksCached, clientFilters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarSearchApi#searchCarActiveGet");
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
| **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true] |
| **latitude** | **Double**| Latitude component of location | [optional] |
| **longitude** | **Double**| Longitude component of location | [optional] |
| **radius** | **Integer**| Radius around the search location (Unit - Miles) | [optional] |
| **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] |
| **includeLease** | **Boolean**| Boolean param to search for listings that include leasing options in them | [optional] |
| **includeFinance** | **Boolean**| Boolean param to search for listings that include finance options in them | [optional] |
| **leaseTerm** | **String**| Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60 | [optional] |
| **leaseDownPayment** | **String**| Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60 | [optional] |
| **leaseEmp** | **String**| Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60 | [optional] |
| **financeLoanTerm** | **String**| Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60 | [optional] |
| **financeLoanApr** | **String**| Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60 | [optional] |
| **financeEmp** | **String**| Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60 | [optional] |
| **financeDownPayment** | **String**| Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60 | [optional] |
| **financeDownPaymentPer** | **String**| Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60 | [optional] |
| **carType** | **String**| Car type. Allowed values are - new / used / certified | [optional] [enum: new, used, certified] |
| **carfax1Owner** | **String**| Indicates whether car has had only one owner or not | [optional] [enum: true, false] |
| **carfaxCleanTitle** | **String**| Indicates whether car has clean ownership records | [optional] [enum: true, false] |
| **yearRange** | **String**| Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021 | [optional] |
| **year** | **String**| To filter listing on their year | [optional] |
| **make** | **String**| To filter listings on their make | [optional] |
| **model** | **String**| To filter listings on their model | [optional] |
| **trim** | **String**| To filter listing on their trim | [optional] |
| **vin** | **String**| To filter listing on their VIN | [optional] |
| **bodyType** | **String**| To filter listing on their body type | [optional] |
| **bodySubtype** | **String**| Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] |
| **vehicleType** | **String**| To filter listing on their vehicle type | [optional] |
| **vins** | **String**| Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc | [optional] |
| **taxonomyVins** | **String**| Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API. | [optional] |
| **mm** | **String**| Make-Model concatenated string. To help passing the results of auto-complete API on mm field, use this parameter and pass in the selected value as is | [optional] |
| **ymm** | **String**| Year-Make-Model concatenated string. To help passing the results of auto-complete API on ymm field, use this parameter and pass in the selected value as is | [optional] |
| **ymmt** | **String**| Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations. | [optional] |
| **match** | **String**| Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match | [optional] |
| **cylinders** | **String**| To filter listing on their cylinders | [optional] |
| **transmission** | **String**| To filter listing on their transmission | [optional] |
| **doors** | **String**| Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated | [optional] |
| **drivetrain** | **String**| To filter listing on their drivetrain | [optional] |
| **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] |
| **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] |
| **baseExteriorColor** | **String**| Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated | [optional] |
| **baseInteriorColor** | **String**| Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated | [optional] |
| **engine** | **String**| To filter listing on their engine | [optional] |
| **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] |
| **engineAspiration** | **String**| Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated | [optional] |
| **engineBlock** | **String**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] |
| **highwayMpgRange** | **String**| Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **cityMpgRange** | **String**| City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **milesRange** | **String**| Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **priceRange** | **String**| Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **msrpRange** | **String**| MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **domRange** | **String**| Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] |
| **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] [enum: asc, desc, ASC, DESC] |
| **rows** | **Integer**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10] |
| **start** | **Integer**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0] |
| **includeNonVinListings** | **Boolean**| To include non vin listings. Default is false | [optional] [default to false] |
| **msaCode** | **String**| To filter listing on msa code in which they are listed | [optional] |
| **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] |
| **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] |
| **facetSort** | **String**| Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param | [optional] [default to count] [enum: count, index] |
| **stats** | **String**| The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. | [optional] |
| **country** | **String**| To filter listing on Country in which they are listed | [optional] [default to US] [enum: US, CA, us, ca, all, ALL] |
| **plot** | **Boolean**| If plot has value true results in around 25k coordinates with limited fields to plot respective graph | [optional] |
| **nodedup** | **Boolean**| If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin | [optional] |
| **dedup** | **Boolean**| If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source | [optional] |
| **owned** | **Boolean**| Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself | [optional] |
| **source** | **String**| To filter listing on their source only for widget requests | [optional] |
| **state** | **String**| To filter listing on State in which they are listed | [optional] |
| **city** | **String**| To filter listing on City in which they are listed | [optional] |
| **trimO** | **String**| Filter listings on web scraped trim | [optional] |
| **trimR** | **String**| Filter trim on custom possible matches | [optional] |
| **domActiveRange** | **String**| Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **dom180Range** | **String**| Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **excludeCertified** | **Boolean**| Boolean param to exclude certified cars from search results | [optional] |
| **fuelType** | **String**| To filter listing on their fuel type | [optional] |
| **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] [enum: franchise, independent] |
| **photoLinks** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them | [optional] |
| **photoLinksCached** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them | [optional] |
| **stockNo** | **String**| To filter listing on their stock number on lot | [optional] |
| **lastSeenRange** | **String**| Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenRange** | **String**| First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenAtSourceRange** | **String**| First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenAtMcRange** | **String**| First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **lastSeenDays** | **String**| Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenDays** | **String**| First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenAtSourceDays** | **String**| First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenAtMcDays** | **String**| First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **includeRelevantLinks** | **Boolean**| To include_relevant_links. Default is true | [optional] [default to false] |
| **inventoryCountRange** | **String**| Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **dealerId** | **String**| Dealer id to filter the listings. | [optional] |
| **excludeDealerIds** | **String**| A list of dealer ids to exclude from result | [optional] |
| **excludeSources** | **String**| A list of sources to exclude from result | [optional] |
| **inTransit** | **String**| A boolean to filter in transit vehicles | [optional] [enum: true, false] |
| **seatingCapacity** | **String**| To filter on vehicle seating capacity | [optional] |
| **powertrainType** | **String**| To filter on powertrain_type | [optional] |
| **priceChange** | **String**| Query to filter listings based on their positive and negative price change | [optional] [enum: positive, negative] |
| **priceChangeRange** | **String**| Price change range to filter listings with price change within given price_change_range. Range to be given in the format - min-max e.g. 10-500 | [optional] |
| **activeInventoryDateRange** | **String**| date range to filter listings that were active within given date range. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **engineSizeRange** | **String**| Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2 | [optional] |
| **highValueFeatures** | **String**| To filter listings on their high_value_features. Results will be intersection of provided HVFs | [optional] |
| **minPhotoLinks** | **String**| Filter listings based by number of photo links within given range | [optional] |
| **minPhotoLinksCached** | **String**| Filter listings based by number of cached photo links within given range | [optional] |
| **clientFilters** | **Boolean**| Flag to add explicit filters set on client level in solr | [optional] [default to true] |

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of all cars listings matching the search &amp; filter criteria |  -  |
| **0** | Error |  -  |

<a id="searchCarAuctionActiveGet"></a>
# **searchCarAuctionActiveGet**
> SearchResponse searchCarAuctionActiveGet(apiKey, appendApiKey, latitude, longitude, radius, zip, includeLease, includeFinance, leaseTerm, leaseDownPayment, leaseEmp, financeLoanTerm, financeLoanApr, financeEmp, financeDownPayment, financeDownPaymentPer, carType, carfax1Owner, carfaxCleanTitle, yearRange, year, make, model, trim, vin, bodyType, bodySubtype, vehicleType, vins, taxonomyVins, mm, ymm, ymmt, match, cylinders, transmission, doors, drivetrain, exteriorColor, interiorColor, baseExteriorColor, baseInteriorColor, engine, engineSize, engineAspiration, engineBlock, highwayMpgRange, cityMpgRange, milesRange, priceRange, msrpRange, domRange, sortBy, sortOrder, rows, start, includeNonVinListings, msaCode, facets, rangeFacets, facetSort, stats, country, plot, nodedup, dedup, owned, state, city, source, dealerId, trimO, trimR, domActiveRange, dom180Range, excludeCertified, fuelType, dealerType, photoLinks, photoLinksCached, stockNo, lastSeenRange, firstSeenRange, firstSeenAtSourceRange, firstSeenAtMcRange, lastSeenDays, firstSeenDays, firstSeenAtSourceDays, firstSeenAtMcDays, includeRelevantLinks, inventoryCountRange, excludeDealerIds, excludeSources, inTransit, titleType, seatingCapacity, engineSizeRange, minPhotoLinks, minPhotoLinksCached)

Gets active auction car listings for the given search criteria

This API produces a list of currently active auction cars from the market for the given search criteria. The API results are limited to allow pagination upto 5000 rows.   The search API facilitates the following use cases -  1. Search Cars around a given geo-point within a given radius  2. Search cars for a specific year / make / model or combination of these  3. Search cars matching multiple year, make, model combinatins in the same search request 4. Filter results by most car specification attributes 5. Search for similar cars by VIN or Taxonomy VIN  6. Filter cars within a given price / miles / days on market (dom) range 7. Specify a sort order for the results on price / miles / dom / listed date  8. Search cars for a given City / State combination  9. Get Facets to build the search drill downs  10. Get Market averages for price/miles/dom for your search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarSearchApi apiInstance = new CarSearchApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean appendApiKey = true; // Boolean | Flag on whether to include api_key in response API urls (if any)
    Double latitude = 3.4D; // Double | Latitude component of location
    Double longitude = 3.4D; // Double | Longitude component of location
    Integer radius = 56; // Integer | Radius around the search location (Unit - Miles)
    String zip = "zip_example"; // String | To filter listing on ZIP around which they are listed
    Boolean includeLease = true; // Boolean | Boolean param to search for listings that include leasing options in them
    Boolean includeFinance = true; // Boolean | Boolean param to search for listings that include finance options in them
    String leaseTerm = "leaseTerm_example"; // String | Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term=30-60
    String leaseDownPayment = "leaseDownPayment_example"; // String | Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment=30-60
    String leaseEmp = "leaseEmp_example"; // String | Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp=30-60
    String financeLoanTerm = "financeLoanTerm_example"; // String | Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term=30-60
    String financeLoanApr = "financeLoanApr_example"; // String | Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr=30-60
    String financeEmp = "financeEmp_example"; // String | Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp=30-60
    String financeDownPayment = "financeDownPayment_example"; // String | Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment=30-60
    String financeDownPaymentPer = "financeDownPaymentPer_example"; // String | Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per=30-60
    String carType = "new"; // String | Car type. Allowed values are - new / used / certified
    String carfax1Owner = "true"; // String | Indicates whether car has had only one owner or not
    String carfaxCleanTitle = "true"; // String | Indicates whether car has clean ownership records
    String yearRange = "yearRange_example"; // String | Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
    String year = "year_example"; // String | To filter listing on their year
    String make = "make_example"; // String | To filter listings on their make
    String model = "model_example"; // String | To filter listings on their model
    String trim = "trim_example"; // String | To filter listing on their trim
    String vin = "vin_example"; // String | To filter listing on their VIN
    String bodyType = "bodyType_example"; // String | To filter listing on their body type
    String bodySubtype = "bodySubtype_example"; // String | Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
    String vehicleType = "vehicleType_example"; // String | To filter listing on their vehicle type
    String vins = "vins_example"; // String | Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc
    String taxonomyVins = "taxonomyVins_example"; // String | Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API.
    String mm = "mm_example"; // String | Make-Model concatenated string. To help passing the results of auto-complete API on mm field, use this parameter and pass in the selected value as is
    String ymm = "ymm_example"; // String | Year-Make-Model concatenated string. To help passing the results of auto-complete API on ymm field, use this parameter and pass in the selected value as is
    String ymmt = "ymmt_example"; // String | Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe '|' character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - 'year|make||' or 'year|make|model' or '|make|model|' combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the 'vins' or 'taxonomy_vins' parameter to the search api instead the year|make|model|trim combinations.
    String match = "match_example"; // String | Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
    String cylinders = "cylinders_example"; // String | To filter listing on their cylinders
    String transmission = "transmission_example"; // String | To filter listing on their transmission
    String doors = "doors_example"; // String | Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
    String drivetrain = "drivetrain_example"; // String | To filter listing on their drivetrain
    String exteriorColor = "exteriorColor_example"; // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    String interiorColor = "interiorColor_example"; // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    String baseExteriorColor = "baseExteriorColor_example"; // String | Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
    String baseInteriorColor = "baseInteriorColor_example"; // String | Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
    String engine = "engine_example"; // String | To filter listing on their engine
    String engineSize = "engineSize_example"; // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    String engineAspiration = "engineAspiration_example"; // String | Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
    String engineBlock = "engineBlock_example"; // String | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
    String highwayMpgRange = "highwayMpgRange_example"; // String | Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String cityMpgRange = "cityMpgRange_example"; // String | City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String milesRange = "milesRange_example"; // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    String priceRange = "priceRange_example"; // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String msrpRange = "msrpRange_example"; // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String domRange = "domRange_example"; // String | Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    String sortBy = "sortBy_example"; // String | Sort by field. Default sort field is distance from the given point
    String sortOrder = "asc"; // String | Sort order - asc or desc. Default sort order is asc
    Integer rows = 10; // Integer | Number of results to return. Default is 10. Max is 50
    Integer start = 0; // Integer | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    Boolean includeNonVinListings = false; // Boolean | To include non vin listings. Default is false
    String msaCode = "msaCode_example"; // String | To filter listing on msa code in which they are listed
    String facets = "facets_example"; // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    String rangeFacets = "rangeFacets_example"; // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    String facetSort = "count"; // String | Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
    String stats = "stats_example"; // String | The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
    String country = "US"; // String | To filter listing on Country in which they are listed
    Boolean plot = true; // Boolean | If plot has value true results in around 25k coordinates with limited fields to plot respective graph
    Boolean nodedup = true; // Boolean | If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
    Boolean dedup = true; // Boolean | If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
    Boolean owned = true; // Boolean | Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
    String state = "state_example"; // String | To filter listing on State in which they are listed
    String city = "city_example"; // String | To filter listing on City in which they are listed
    String source = "source_example"; // String | To filter listing on their source only for widget requests
    String dealerId = "dealerId_example"; // String | Dealer id to filter the listings.
    String trimO = "trimO_example"; // String | Filter listings on web scraped trim
    String trimR = "trimR_example"; // String | Filter trim on custom possible matches
    String domActiveRange = "domActiveRange_example"; // String | Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    String dom180Range = "dom180Range_example"; // String | Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    Boolean excludeCertified = true; // Boolean | Boolean param to exclude certified cars from search results
    String fuelType = "fuelType_example"; // String | To filter listing on their fuel type
    String dealerType = "franchise"; // String | Filter based on dealer type independant or franchise
    Boolean photoLinks = true; // Boolean | A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don't have them
    Boolean photoLinksCached = true; // Boolean | A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don't have them
    String stockNo = "stockNo_example"; // String | To filter listing on their stock number on lot
    String lastSeenRange = "lastSeenRange_example"; // String | Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenRange = "firstSeenRange_example"; // String | First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenAtSourceRange = "firstSeenAtSourceRange_example"; // String | First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenAtMcRange = "firstSeenAtMcRange_example"; // String | First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String lastSeenDays = "lastSeenDays_example"; // String | Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenDays = "firstSeenDays_example"; // String | First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenAtSourceDays = "firstSeenAtSourceDays_example"; // String | First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenAtMcDays = "firstSeenAtMcDays_example"; // String | First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
    Boolean includeRelevantLinks = false; // Boolean | To include_relevant_links. Default is true
    String inventoryCountRange = "inventoryCountRange_example"; // String | Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50
    String excludeDealerIds = "excludeDealerIds_example"; // String | A list of dealer ids to exclude from result
    String excludeSources = "excludeSources_example"; // String | A list of sources to exclude from result
    String inTransit = "true"; // String | A boolean to filter in transit vehicles
    String titleType = "clean"; // String | To filter on title type
    String seatingCapacity = "seatingCapacity_example"; // String | To filter on vehicle seating capacity
    String engineSizeRange = "engineSizeRange_example"; // String | Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
    String minPhotoLinks = "minPhotoLinks_example"; // String | Filter listings based by number of photo links within given range
    String minPhotoLinksCached = "minPhotoLinksCached_example"; // String | Filter listings based by number of cached photo links within given range
    try {
      SearchResponse result = apiInstance.searchCarAuctionActiveGet(apiKey, appendApiKey, latitude, longitude, radius, zip, includeLease, includeFinance, leaseTerm, leaseDownPayment, leaseEmp, financeLoanTerm, financeLoanApr, financeEmp, financeDownPayment, financeDownPaymentPer, carType, carfax1Owner, carfaxCleanTitle, yearRange, year, make, model, trim, vin, bodyType, bodySubtype, vehicleType, vins, taxonomyVins, mm, ymm, ymmt, match, cylinders, transmission, doors, drivetrain, exteriorColor, interiorColor, baseExteriorColor, baseInteriorColor, engine, engineSize, engineAspiration, engineBlock, highwayMpgRange, cityMpgRange, milesRange, priceRange, msrpRange, domRange, sortBy, sortOrder, rows, start, includeNonVinListings, msaCode, facets, rangeFacets, facetSort, stats, country, plot, nodedup, dedup, owned, state, city, source, dealerId, trimO, trimR, domActiveRange, dom180Range, excludeCertified, fuelType, dealerType, photoLinks, photoLinksCached, stockNo, lastSeenRange, firstSeenRange, firstSeenAtSourceRange, firstSeenAtMcRange, lastSeenDays, firstSeenDays, firstSeenAtSourceDays, firstSeenAtMcDays, includeRelevantLinks, inventoryCountRange, excludeDealerIds, excludeSources, inTransit, titleType, seatingCapacity, engineSizeRange, minPhotoLinks, minPhotoLinksCached);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarSearchApi#searchCarAuctionActiveGet");
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
| **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true] |
| **latitude** | **Double**| Latitude component of location | [optional] |
| **longitude** | **Double**| Longitude component of location | [optional] |
| **radius** | **Integer**| Radius around the search location (Unit - Miles) | [optional] |
| **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] |
| **includeLease** | **Boolean**| Boolean param to search for listings that include leasing options in them | [optional] |
| **includeFinance** | **Boolean**| Boolean param to search for listings that include finance options in them | [optional] |
| **leaseTerm** | **String**| Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60 | [optional] |
| **leaseDownPayment** | **String**| Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60 | [optional] |
| **leaseEmp** | **String**| Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60 | [optional] |
| **financeLoanTerm** | **String**| Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60 | [optional] |
| **financeLoanApr** | **String**| Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60 | [optional] |
| **financeEmp** | **String**| Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60 | [optional] |
| **financeDownPayment** | **String**| Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60 | [optional] |
| **financeDownPaymentPer** | **String**| Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60 | [optional] |
| **carType** | **String**| Car type. Allowed values are - new / used / certified | [optional] [enum: new, used, certified] |
| **carfax1Owner** | **String**| Indicates whether car has had only one owner or not | [optional] [enum: true, false] |
| **carfaxCleanTitle** | **String**| Indicates whether car has clean ownership records | [optional] [enum: true, false] |
| **yearRange** | **String**| Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021 | [optional] |
| **year** | **String**| To filter listing on their year | [optional] |
| **make** | **String**| To filter listings on their make | [optional] |
| **model** | **String**| To filter listings on their model | [optional] |
| **trim** | **String**| To filter listing on their trim | [optional] |
| **vin** | **String**| To filter listing on their VIN | [optional] |
| **bodyType** | **String**| To filter listing on their body type | [optional] |
| **bodySubtype** | **String**| Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] |
| **vehicleType** | **String**| To filter listing on their vehicle type | [optional] |
| **vins** | **String**| Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc | [optional] |
| **taxonomyVins** | **String**| Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API. | [optional] |
| **mm** | **String**| Make-Model concatenated string. To help passing the results of auto-complete API on mm field, use this parameter and pass in the selected value as is | [optional] |
| **ymm** | **String**| Year-Make-Model concatenated string. To help passing the results of auto-complete API on ymm field, use this parameter and pass in the selected value as is | [optional] |
| **ymmt** | **String**| Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations. | [optional] |
| **match** | **String**| Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match | [optional] |
| **cylinders** | **String**| To filter listing on their cylinders | [optional] |
| **transmission** | **String**| To filter listing on their transmission | [optional] |
| **doors** | **String**| Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated | [optional] |
| **drivetrain** | **String**| To filter listing on their drivetrain | [optional] |
| **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] |
| **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] |
| **baseExteriorColor** | **String**| Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated | [optional] |
| **baseInteriorColor** | **String**| Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated | [optional] |
| **engine** | **String**| To filter listing on their engine | [optional] |
| **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] |
| **engineAspiration** | **String**| Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated | [optional] |
| **engineBlock** | **String**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] |
| **highwayMpgRange** | **String**| Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **cityMpgRange** | **String**| City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **milesRange** | **String**| Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **priceRange** | **String**| Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **msrpRange** | **String**| MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **domRange** | **String**| Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] |
| **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] [enum: asc, desc, ASC, DESC] |
| **rows** | **Integer**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10] |
| **start** | **Integer**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0] |
| **includeNonVinListings** | **Boolean**| To include non vin listings. Default is false | [optional] [default to false] |
| **msaCode** | **String**| To filter listing on msa code in which they are listed | [optional] |
| **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] |
| **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] |
| **facetSort** | **String**| Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param | [optional] [default to count] [enum: count, index] |
| **stats** | **String**| The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. | [optional] |
| **country** | **String**| To filter listing on Country in which they are listed | [optional] [default to US] [enum: US, CA, us, ca, all, ALL] |
| **plot** | **Boolean**| If plot has value true results in around 25k coordinates with limited fields to plot respective graph | [optional] |
| **nodedup** | **Boolean**| If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin | [optional] |
| **dedup** | **Boolean**| If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source | [optional] |
| **owned** | **Boolean**| Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself | [optional] |
| **state** | **String**| To filter listing on State in which they are listed | [optional] |
| **city** | **String**| To filter listing on City in which they are listed | [optional] |
| **source** | **String**| To filter listing on their source only for widget requests | [optional] |
| **dealerId** | **String**| Dealer id to filter the listings. | [optional] |
| **trimO** | **String**| Filter listings on web scraped trim | [optional] |
| **trimR** | **String**| Filter trim on custom possible matches | [optional] |
| **domActiveRange** | **String**| Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **dom180Range** | **String**| Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **excludeCertified** | **Boolean**| Boolean param to exclude certified cars from search results | [optional] |
| **fuelType** | **String**| To filter listing on their fuel type | [optional] |
| **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] [enum: franchise, independent] |
| **photoLinks** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them | [optional] |
| **photoLinksCached** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them | [optional] |
| **stockNo** | **String**| To filter listing on their stock number on lot | [optional] |
| **lastSeenRange** | **String**| Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenRange** | **String**| First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenAtSourceRange** | **String**| First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenAtMcRange** | **String**| First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **lastSeenDays** | **String**| Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenDays** | **String**| First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenAtSourceDays** | **String**| First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenAtMcDays** | **String**| First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **includeRelevantLinks** | **Boolean**| To include_relevant_links. Default is true | [optional] [default to false] |
| **inventoryCountRange** | **String**| Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **excludeDealerIds** | **String**| A list of dealer ids to exclude from result | [optional] |
| **excludeSources** | **String**| A list of sources to exclude from result | [optional] |
| **inTransit** | **String**| A boolean to filter in transit vehicles | [optional] [enum: true, false] |
| **titleType** | **String**| To filter on title type | [optional] [enum: clean, salvage] |
| **seatingCapacity** | **String**| To filter on vehicle seating capacity | [optional] |
| **engineSizeRange** | **String**| Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2 | [optional] |
| **minPhotoLinks** | **String**| Filter listings based by number of photo links within given range | [optional] |
| **minPhotoLinksCached** | **String**| Filter listings based by number of cached photo links within given range | [optional] |

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of all auction cars listings matching the search &amp; filter criteria |  -  |
| **0** | Error |  -  |

<a id="searchCarFsboActiveGet"></a>
# **searchCarFsboActiveGet**
> SearchResponse searchCarFsboActiveGet(apiKey, appendApiKey, latitude, longitude, radius, zip, includeLease, includeFinance, leaseTerm, leaseDownPayment, leaseEmp, financeLoanTerm, financeLoanApr, financeEmp, financeDownPayment, financeDownPaymentPer, carType, carfax1Owner, carfaxCleanTitle, yearRange, year, make, model, trim, vin, bodyType, bodySubtype, vehicleType, vins, taxonomyVins, mm, ymm, ymmt, match, cylinders, transmission, doors, drivetrain, exteriorColor, interiorColor, baseExteriorColor, baseInteriorColor, engine, engineSize, engineAspiration, engineBlock, highwayMpgRange, cityMpgRange, milesRange, priceRange, msrpRange, domRange, sortBy, sortOrder, rows, start, includeNonVinListings, msaCode, facets, rangeFacets, facetSort, stats, country, plot, nodedup, dedup, owned, state, city, source, dealerId, trimO, trimR, domActiveRange, dom180Range, excludeCertified, fuelType, dealerType, photoLinks, photoLinksCached, stockNo, lastSeenRange, firstSeenRange, firstSeenAtSourceRange, firstSeenAtMcRange, lastSeenDays, firstSeenDays, firstSeenAtSourceDays, firstSeenAtMcDays, includeRelevantLinks, inventoryCountRange, excludeDealerIds, excludeSources, excludeDealerListings, inTransit, seatingCapacity, engineSizeRange, minPhotoLinks, minPhotoLinksCached)

Gets active private party car listings for the given search criteria

This API produces a list of currently active FSBO cars from the market for the given search criteria. The API results are limited to allow pagination upto 5000 rows.   The search API facilitates the following use cases -  1. Search Cars around a given geo-point within a given radius  2. Search cars for a specific year / make / model or combination of these  3. Search cars matching multiple year, make, model combinatins in the same search request 4. Filter results by most car specification attributes 5. Search for similar cars by VIN or Taxonomy VIN  6. Filter cars within a given price / miles / days on market (dom) range 7. Specify a sort order for the results on price / miles / dom / listed date  8. Search cars for a given City / State combination  9. Get Facets to build the search drill downs  10. Get Market averages for price/miles/dom for your search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarSearchApi apiInstance = new CarSearchApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean appendApiKey = true; // Boolean | Flag on whether to include api_key in response API urls (if any)
    Double latitude = 3.4D; // Double | Latitude component of location
    Double longitude = 3.4D; // Double | Longitude component of location
    Integer radius = 56; // Integer | Radius around the search location (Unit - Miles)
    String zip = "zip_example"; // String | To filter listing on ZIP around which they are listed
    Boolean includeLease = true; // Boolean | Boolean param to search for listings that include leasing options in them
    Boolean includeFinance = true; // Boolean | Boolean param to search for listings that include finance options in them
    String leaseTerm = "leaseTerm_example"; // String | Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term=30-60
    String leaseDownPayment = "leaseDownPayment_example"; // String | Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment=30-60
    String leaseEmp = "leaseEmp_example"; // String | Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp=30-60
    String financeLoanTerm = "financeLoanTerm_example"; // String | Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term=30-60
    String financeLoanApr = "financeLoanApr_example"; // String | Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr=30-60
    String financeEmp = "financeEmp_example"; // String | Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp=30-60
    String financeDownPayment = "financeDownPayment_example"; // String | Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment=30-60
    String financeDownPaymentPer = "financeDownPaymentPer_example"; // String | Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per=30-60
    String carType = "new"; // String | Car type. Allowed values are - new / used / certified
    String carfax1Owner = "true"; // String | Indicates whether car has had only one owner or not
    String carfaxCleanTitle = "true"; // String | Indicates whether car has clean ownership records
    String yearRange = "yearRange_example"; // String | Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
    String year = "year_example"; // String | To filter listing on their year
    String make = "make_example"; // String | To filter listings on their make
    String model = "model_example"; // String | To filter listings on their model
    String trim = "trim_example"; // String | To filter listing on their trim
    String vin = "vin_example"; // String | To filter listing on their VIN
    String bodyType = "bodyType_example"; // String | To filter listing on their body type
    String bodySubtype = "bodySubtype_example"; // String | Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
    String vehicleType = "vehicleType_example"; // String | To filter listing on their vehicle type
    String vins = "vins_example"; // String | Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc
    String taxonomyVins = "taxonomyVins_example"; // String | Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API.
    String mm = "mm_example"; // String | Make-Model concatenated string. To help passing the results of auto-complete API on mm field, use this parameter and pass in the selected value as is
    String ymm = "ymm_example"; // String | Year-Make-Model concatenated string. To help passing the results of auto-complete API on ymm field, use this parameter and pass in the selected value as is
    String ymmt = "ymmt_example"; // String | Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe '|' character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - 'year|make||' or 'year|make|model' or '|make|model|' combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the 'vins' or 'taxonomy_vins' parameter to the search api instead the year|make|model|trim combinations.
    String match = "match_example"; // String | Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
    String cylinders = "cylinders_example"; // String | To filter listing on their cylinders
    String transmission = "transmission_example"; // String | To filter listing on their transmission
    String doors = "doors_example"; // String | Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
    String drivetrain = "drivetrain_example"; // String | To filter listing on their drivetrain
    String exteriorColor = "exteriorColor_example"; // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    String interiorColor = "interiorColor_example"; // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    String baseExteriorColor = "baseExteriorColor_example"; // String | Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
    String baseInteriorColor = "baseInteriorColor_example"; // String | Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
    String engine = "engine_example"; // String | To filter listing on their engine
    String engineSize = "engineSize_example"; // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    String engineAspiration = "engineAspiration_example"; // String | Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
    String engineBlock = "engineBlock_example"; // String | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
    String highwayMpgRange = "highwayMpgRange_example"; // String | Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String cityMpgRange = "cityMpgRange_example"; // String | City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String milesRange = "milesRange_example"; // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    String priceRange = "priceRange_example"; // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String msrpRange = "msrpRange_example"; // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String domRange = "domRange_example"; // String | Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    String sortBy = "sortBy_example"; // String | Sort by field. Default sort field is distance from the given point
    String sortOrder = "asc"; // String | Sort order - asc or desc. Default sort order is asc
    Integer rows = 10; // Integer | Number of results to return. Default is 10. Max is 50
    Integer start = 0; // Integer | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    Boolean includeNonVinListings = false; // Boolean | To include non vin listings. Default is false
    String msaCode = "msaCode_example"; // String | To filter listing on msa code in which they are listed
    String facets = "facets_example"; // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    String rangeFacets = "rangeFacets_example"; // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    String facetSort = "count"; // String | Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
    String stats = "stats_example"; // String | The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
    String country = "US"; // String | To filter listing on Country in which they are listed
    Boolean plot = true; // Boolean | If plot has value true results in around 25k coordinates with limited fields to plot respective graph
    Boolean nodedup = true; // Boolean | If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
    Boolean dedup = true; // Boolean | If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
    Boolean owned = true; // Boolean | Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
    String state = "state_example"; // String | To filter listing on State in which they are listed
    String city = "city_example"; // String | To filter listing on City in which they are listed
    String source = "source_example"; // String | To filter listing on their source only for widget requests
    String dealerId = "dealerId_example"; // String | Dealer id to filter the listings.
    String trimO = "trimO_example"; // String | Filter listings on web scraped trim
    String trimR = "trimR_example"; // String | Filter trim on custom possible matches
    String domActiveRange = "domActiveRange_example"; // String | Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    String dom180Range = "dom180Range_example"; // String | Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    Boolean excludeCertified = true; // Boolean | Boolean param to exclude certified cars from search results
    String fuelType = "fuelType_example"; // String | To filter listing on their fuel type
    String dealerType = "franchise"; // String | Filter based on dealer type independant or franchise
    Boolean photoLinks = true; // Boolean | A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don't have them
    Boolean photoLinksCached = true; // Boolean | A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don't have them
    String stockNo = "stockNo_example"; // String | To filter listing on their stock number on lot
    String lastSeenRange = "lastSeenRange_example"; // String | Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenRange = "firstSeenRange_example"; // String | First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenAtSourceRange = "firstSeenAtSourceRange_example"; // String | First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenAtMcRange = "firstSeenAtMcRange_example"; // String | First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String lastSeenDays = "lastSeenDays_example"; // String | Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenDays = "firstSeenDays_example"; // String | First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenAtSourceDays = "firstSeenAtSourceDays_example"; // String | First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenAtMcDays = "firstSeenAtMcDays_example"; // String | First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
    Boolean includeRelevantLinks = false; // Boolean | To include_relevant_links. Default is true
    String inventoryCountRange = "inventoryCountRange_example"; // String | Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50
    String excludeDealerIds = "excludeDealerIds_example"; // String | A list of dealer ids to exclude from result
    String excludeSources = "excludeSources_example"; // String | A list of sources to exclude from result
    Boolean excludeDealerListings = true; // Boolean | A list of fsbo listings to exclude from result
    String inTransit = "true"; // String | A boolean to filter in transit vehicles
    String seatingCapacity = "seatingCapacity_example"; // String | To filter on vehicle seating capacity
    String engineSizeRange = "engineSizeRange_example"; // String | Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
    String minPhotoLinks = "minPhotoLinks_example"; // String | Filter listings based by number of photo links within given range
    String minPhotoLinksCached = "minPhotoLinksCached_example"; // String | Filter listings based by number of cached photo links within given range
    try {
      SearchResponse result = apiInstance.searchCarFsboActiveGet(apiKey, appendApiKey, latitude, longitude, radius, zip, includeLease, includeFinance, leaseTerm, leaseDownPayment, leaseEmp, financeLoanTerm, financeLoanApr, financeEmp, financeDownPayment, financeDownPaymentPer, carType, carfax1Owner, carfaxCleanTitle, yearRange, year, make, model, trim, vin, bodyType, bodySubtype, vehicleType, vins, taxonomyVins, mm, ymm, ymmt, match, cylinders, transmission, doors, drivetrain, exteriorColor, interiorColor, baseExteriorColor, baseInteriorColor, engine, engineSize, engineAspiration, engineBlock, highwayMpgRange, cityMpgRange, milesRange, priceRange, msrpRange, domRange, sortBy, sortOrder, rows, start, includeNonVinListings, msaCode, facets, rangeFacets, facetSort, stats, country, plot, nodedup, dedup, owned, state, city, source, dealerId, trimO, trimR, domActiveRange, dom180Range, excludeCertified, fuelType, dealerType, photoLinks, photoLinksCached, stockNo, lastSeenRange, firstSeenRange, firstSeenAtSourceRange, firstSeenAtMcRange, lastSeenDays, firstSeenDays, firstSeenAtSourceDays, firstSeenAtMcDays, includeRelevantLinks, inventoryCountRange, excludeDealerIds, excludeSources, excludeDealerListings, inTransit, seatingCapacity, engineSizeRange, minPhotoLinks, minPhotoLinksCached);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarSearchApi#searchCarFsboActiveGet");
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
| **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true] |
| **latitude** | **Double**| Latitude component of location | [optional] |
| **longitude** | **Double**| Longitude component of location | [optional] |
| **radius** | **Integer**| Radius around the search location (Unit - Miles) | [optional] |
| **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] |
| **includeLease** | **Boolean**| Boolean param to search for listings that include leasing options in them | [optional] |
| **includeFinance** | **Boolean**| Boolean param to search for listings that include finance options in them | [optional] |
| **leaseTerm** | **String**| Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60 | [optional] |
| **leaseDownPayment** | **String**| Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60 | [optional] |
| **leaseEmp** | **String**| Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60 | [optional] |
| **financeLoanTerm** | **String**| Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60 | [optional] |
| **financeLoanApr** | **String**| Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60 | [optional] |
| **financeEmp** | **String**| Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60 | [optional] |
| **financeDownPayment** | **String**| Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60 | [optional] |
| **financeDownPaymentPer** | **String**| Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60 | [optional] |
| **carType** | **String**| Car type. Allowed values are - new / used / certified | [optional] [enum: new, used, certified] |
| **carfax1Owner** | **String**| Indicates whether car has had only one owner or not | [optional] [enum: true, false] |
| **carfaxCleanTitle** | **String**| Indicates whether car has clean ownership records | [optional] [enum: true, false] |
| **yearRange** | **String**| Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021 | [optional] |
| **year** | **String**| To filter listing on their year | [optional] |
| **make** | **String**| To filter listings on their make | [optional] |
| **model** | **String**| To filter listings on their model | [optional] |
| **trim** | **String**| To filter listing on their trim | [optional] |
| **vin** | **String**| To filter listing on their VIN | [optional] |
| **bodyType** | **String**| To filter listing on their body type | [optional] |
| **bodySubtype** | **String**| Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] |
| **vehicleType** | **String**| To filter listing on their vehicle type | [optional] |
| **vins** | **String**| Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc | [optional] |
| **taxonomyVins** | **String**| Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API. | [optional] |
| **mm** | **String**| Make-Model concatenated string. To help passing the results of auto-complete API on mm field, use this parameter and pass in the selected value as is | [optional] |
| **ymm** | **String**| Year-Make-Model concatenated string. To help passing the results of auto-complete API on ymm field, use this parameter and pass in the selected value as is | [optional] |
| **ymmt** | **String**| Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations. | [optional] |
| **match** | **String**| Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match | [optional] |
| **cylinders** | **String**| To filter listing on their cylinders | [optional] |
| **transmission** | **String**| To filter listing on their transmission | [optional] |
| **doors** | **String**| Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated | [optional] |
| **drivetrain** | **String**| To filter listing on their drivetrain | [optional] |
| **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] |
| **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] |
| **baseExteriorColor** | **String**| Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated | [optional] |
| **baseInteriorColor** | **String**| Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated | [optional] |
| **engine** | **String**| To filter listing on their engine | [optional] |
| **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] |
| **engineAspiration** | **String**| Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated | [optional] |
| **engineBlock** | **String**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] |
| **highwayMpgRange** | **String**| Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **cityMpgRange** | **String**| City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **milesRange** | **String**| Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **priceRange** | **String**| Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **msrpRange** | **String**| MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **domRange** | **String**| Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] |
| **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] [enum: asc, desc, ASC, DESC] |
| **rows** | **Integer**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10] |
| **start** | **Integer**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0] |
| **includeNonVinListings** | **Boolean**| To include non vin listings. Default is false | [optional] [default to false] |
| **msaCode** | **String**| To filter listing on msa code in which they are listed | [optional] |
| **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] |
| **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] |
| **facetSort** | **String**| Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param | [optional] [default to count] [enum: count, index] |
| **stats** | **String**| The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. | [optional] |
| **country** | **String**| To filter listing on Country in which they are listed | [optional] [default to US] [enum: US, CA, us, ca, all, ALL] |
| **plot** | **Boolean**| If plot has value true results in around 25k coordinates with limited fields to plot respective graph | [optional] |
| **nodedup** | **Boolean**| If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin | [optional] |
| **dedup** | **Boolean**| If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source | [optional] |
| **owned** | **Boolean**| Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself | [optional] |
| **state** | **String**| To filter listing on State in which they are listed | [optional] |
| **city** | **String**| To filter listing on City in which they are listed | [optional] |
| **source** | **String**| To filter listing on their source only for widget requests | [optional] |
| **dealerId** | **String**| Dealer id to filter the listings. | [optional] |
| **trimO** | **String**| Filter listings on web scraped trim | [optional] |
| **trimR** | **String**| Filter trim on custom possible matches | [optional] |
| **domActiveRange** | **String**| Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **dom180Range** | **String**| Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **excludeCertified** | **Boolean**| Boolean param to exclude certified cars from search results | [optional] |
| **fuelType** | **String**| To filter listing on their fuel type | [optional] |
| **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] [enum: franchise, independent] |
| **photoLinks** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them | [optional] |
| **photoLinksCached** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them | [optional] |
| **stockNo** | **String**| To filter listing on their stock number on lot | [optional] |
| **lastSeenRange** | **String**| Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenRange** | **String**| First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenAtSourceRange** | **String**| First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenAtMcRange** | **String**| First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **lastSeenDays** | **String**| Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenDays** | **String**| First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenAtSourceDays** | **String**| First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenAtMcDays** | **String**| First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **includeRelevantLinks** | **Boolean**| To include_relevant_links. Default is true | [optional] [default to false] |
| **inventoryCountRange** | **String**| Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **excludeDealerIds** | **String**| A list of dealer ids to exclude from result | [optional] |
| **excludeSources** | **String**| A list of sources to exclude from result | [optional] |
| **excludeDealerListings** | **Boolean**| A list of fsbo listings to exclude from result | [optional] |
| **inTransit** | **String**| A boolean to filter in transit vehicles | [optional] [enum: true, false] |
| **seatingCapacity** | **String**| To filter on vehicle seating capacity | [optional] |
| **engineSizeRange** | **String**| Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2 | [optional] |
| **minPhotoLinks** | **String**| Filter listings based by number of photo links within given range | [optional] |
| **minPhotoLinksCached** | **String**| Filter listings based by number of cached photo links within given range | [optional] |

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of all FSBO cars listings matching the search &amp; filter criteria |  -  |
| **0** | Error |  -  |

<a id="searchCarRecentsGet"></a>
# **searchCarRecentsGet**
> SearchResponse searchCarRecentsGet(apiKey, appendApiKey, latitude, longitude, radius, zip, includeLease, includeFinance, leaseTerm, leaseDownPayment, leaseEmp, financeLoanTerm, financeLoanApr, financeEmp, financeDownPayment, financeDownPaymentPer, carType, carfax1Owner, carfaxCleanTitle, yearRange, year, make, model, trim, dealerId, vin, source, bodyType, bodySubtype, vehicleType, vins, taxonomyVins, ymmt, match, cylinders, transmission, doors, drivetrain, exteriorColor, interiorColor, baseExteriorColor, baseInteriorColor, engine, engineSize, engineAspiration, engineBlock, highwayMpgRange, cityMpgRange, milesRange, priceRange, msrpRange, domRange, lastSeenRange, firstSeenRange, firstSeenAtSourceRange, firstSeenAtMcRange, lastSeenDays, firstSeenDays, firstSeenAtSourceDays, firstSeenAtMcDays, sortBy, sortOrder, rows, start, includeNonVinListings, facets, rangeFacets, facetSort, stats, country, plot, nodedup, dedup, owned, state, city, msaCode, dealerName, dealershipGroupName, trimO, trimR, domActiveRange, dom180Range, excludeCertified, fuelType, dealerType, photoLinks, photoLinksCached, stockNo, sold, includeRelevantLinks, expired, excludeDealerIds, excludeSources, inTransit, seatingCapacity, activeInventoryDateRange, engineSizeRange, priceChangeRange)

Gets Recent car listings for the given search criteria

This API produces a list of recently active (past 90 days) cars from the market for the given search criteria

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarSearchApi apiInstance = new CarSearchApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean appendApiKey = true; // Boolean | Flag on whether to include api_key in response API urls (if any)
    Double latitude = 3.4D; // Double | Latitude component of location
    Double longitude = 3.4D; // Double | Longitude component of location
    Integer radius = 56; // Integer | Radius around the search location (Unit - Miles)
    String zip = "zip_example"; // String | To filter listing on ZIP around which they are listed
    Boolean includeLease = true; // Boolean | Boolean param to search for listings that include leasing options in them
    Boolean includeFinance = true; // Boolean | Boolean param to search for listings that include finance options in them
    String leaseTerm = "leaseTerm_example"; // String | Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term=30-60
    String leaseDownPayment = "leaseDownPayment_example"; // String | Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment=30-60
    String leaseEmp = "leaseEmp_example"; // String | Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp=30-60
    String financeLoanTerm = "financeLoanTerm_example"; // String | Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term=30-60
    String financeLoanApr = "financeLoanApr_example"; // String | Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr=30-60
    String financeEmp = "financeEmp_example"; // String | Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp=30-60
    String financeDownPayment = "financeDownPayment_example"; // String | Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment=30-60
    String financeDownPaymentPer = "financeDownPaymentPer_example"; // String | Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per=30-60
    String carType = "new"; // String | Car type. Allowed values are - new / used / certified
    String carfax1Owner = "true"; // String | Indicates whether car has had only one owner or not
    String carfaxCleanTitle = "true"; // String | Indicates whether car has clean ownership records
    String yearRange = "yearRange_example"; // String | Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
    String year = "year_example"; // String | To filter listing on their year
    String make = "make_example"; // String | To filter listings on their make
    String model = "model_example"; // String | To filter listings on their model
    String trim = "trim_example"; // String | To filter listing on their trim
    String dealerId = "dealerId_example"; // String | Dealer id to filter the listings.
    String vin = "vin_example"; // String | To filter listing on their VIN
    String source = "source_example"; // String | To filter listing on their source
    String bodyType = "bodyType_example"; // String | To filter listing on their body type
    String bodySubtype = "bodySubtype_example"; // String | Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
    String vehicleType = "vehicleType_example"; // String | To filter listing on their vehicle type
    String vins = "vins_example"; // String | Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc
    String taxonomyVins = "taxonomyVins_example"; // String | Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API.
    String ymmt = "ymmt_example"; // String | Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe '|' character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - 'year|make||' or 'year|make|model' or '|make|model|' combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the 'vins' or 'taxonomy_vins' parameter to the search api instead the year|make|model|trim combinations.
    String match = "match_example"; // String | Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
    String cylinders = "cylinders_example"; // String | To filter listing on their cylinders
    String transmission = "transmission_example"; // String | To filter listing on their transmission
    String doors = "doors_example"; // String | Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
    String drivetrain = "drivetrain_example"; // String | To filter listing on their drivetrain
    String exteriorColor = "exteriorColor_example"; // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    String interiorColor = "interiorColor_example"; // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    String baseExteriorColor = "baseExteriorColor_example"; // String | Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
    String baseInteriorColor = "baseInteriorColor_example"; // String | Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
    String engine = "engine_example"; // String | To filter listing on their engine
    String engineSize = "engineSize_example"; // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    String engineAspiration = "engineAspiration_example"; // String | Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
    String engineBlock = "engineBlock_example"; // String | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
    String highwayMpgRange = "highwayMpgRange_example"; // String | Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String cityMpgRange = "cityMpgRange_example"; // String | City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String milesRange = "milesRange_example"; // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    String priceRange = "priceRange_example"; // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String msrpRange = "msrpRange_example"; // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String domRange = "domRange_example"; // String | Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    String lastSeenRange = "lastSeenRange_example"; // String | Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenRange = "firstSeenRange_example"; // String | First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenAtSourceRange = "firstSeenAtSourceRange_example"; // String | First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenAtMcRange = "firstSeenAtMcRange_example"; // String | First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String lastSeenDays = "lastSeenDays_example"; // String | Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenDays = "firstSeenDays_example"; // String | First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenAtSourceDays = "firstSeenAtSourceDays_example"; // String | First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenAtMcDays = "firstSeenAtMcDays_example"; // String | First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
    String sortBy = "sortBy_example"; // String | Sort by field. Default sort field is distance from the given point
    String sortOrder = "asc"; // String | Sort order - asc or desc. Default sort order is asc
    Integer rows = 10; // Integer | Number of results to return. Default is 10. Max is 50
    Integer start = 0; // Integer | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    Boolean includeNonVinListings = false; // Boolean | To include non vin listings. Default is false
    String facets = "facets_example"; // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    String rangeFacets = "rangeFacets_example"; // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    String facetSort = "count"; // String | Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
    String stats = "stats_example"; // String | The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
    String country = "US"; // String | To filter listing on Country in which they are listed
    Boolean plot = true; // Boolean | If plot has value true results in around 25k coordinates with limited fields to plot respective graph
    Boolean nodedup = true; // Boolean | If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
    Boolean dedup = true; // Boolean | If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
    Boolean owned = true; // Boolean | Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
    String state = "state_example"; // String | To filter listing on State in which they are listed
    String city = "city_example"; // String | To filter listing on City in which they are listed
    String msaCode = "msaCode_example"; // String | To filter listing on msa code in which they are listed
    String dealerName = "dealerName_example"; // String | Filter listings on dealer_name
    String dealershipGroupName = "dealershipGroupName_example"; // String | Name of the dealership group to search for
    String trimO = "trimO_example"; // String | Filter listings on web scraped trim
    String trimR = "trimR_example"; // String | Filter trim on custom possible matches
    String domActiveRange = "domActiveRange_example"; // String | Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    String dom180Range = "dom180Range_example"; // String | Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    Boolean excludeCertified = true; // Boolean | Boolean param to exclude certified cars from search results
    String fuelType = "fuelType_example"; // String | To filter listing on their fuel type
    String dealerType = "franchise"; // String | Filter based on dealer type independant or franchise
    Boolean photoLinks = true; // Boolean | A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don't have them
    Boolean photoLinksCached = true; // Boolean | A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don't have them
    String stockNo = "stockNo_example"; // String | To filter listing on their stock number on lot
    Boolean sold = true; // Boolean | sold parameter to fetch only sold listings
    Boolean includeRelevantLinks = false; // Boolean | To include_relevant_links. Default is true
    String expired = "true"; // String | Boolean falg to either fetch only the expired listings or active ones
    String excludeDealerIds = "excludeDealerIds_example"; // String | A list of dealer ids to exclude from result
    String excludeSources = "excludeSources_example"; // String | A list of sources to exclude from result
    String inTransit = "true"; // String | A boolean to filter in transit vehicles
    String seatingCapacity = "seatingCapacity_example"; // String | To filter on vehicle seating capacity
    String activeInventoryDateRange = "activeInventoryDateRange_example"; // String | date range to filter listings that were active within given date range. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String engineSizeRange = "engineSizeRange_example"; // String | Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
    String priceChangeRange = "priceChangeRange_example"; // String | Price change range to filter listings with price change within given price_change_range. Range to be given in the format - min-max e.g. 10-500
    try {
      SearchResponse result = apiInstance.searchCarRecentsGet(apiKey, appendApiKey, latitude, longitude, radius, zip, includeLease, includeFinance, leaseTerm, leaseDownPayment, leaseEmp, financeLoanTerm, financeLoanApr, financeEmp, financeDownPayment, financeDownPaymentPer, carType, carfax1Owner, carfaxCleanTitle, yearRange, year, make, model, trim, dealerId, vin, source, bodyType, bodySubtype, vehicleType, vins, taxonomyVins, ymmt, match, cylinders, transmission, doors, drivetrain, exteriorColor, interiorColor, baseExteriorColor, baseInteriorColor, engine, engineSize, engineAspiration, engineBlock, highwayMpgRange, cityMpgRange, milesRange, priceRange, msrpRange, domRange, lastSeenRange, firstSeenRange, firstSeenAtSourceRange, firstSeenAtMcRange, lastSeenDays, firstSeenDays, firstSeenAtSourceDays, firstSeenAtMcDays, sortBy, sortOrder, rows, start, includeNonVinListings, facets, rangeFacets, facetSort, stats, country, plot, nodedup, dedup, owned, state, city, msaCode, dealerName, dealershipGroupName, trimO, trimR, domActiveRange, dom180Range, excludeCertified, fuelType, dealerType, photoLinks, photoLinksCached, stockNo, sold, includeRelevantLinks, expired, excludeDealerIds, excludeSources, inTransit, seatingCapacity, activeInventoryDateRange, engineSizeRange, priceChangeRange);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarSearchApi#searchCarRecentsGet");
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
| **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true] |
| **latitude** | **Double**| Latitude component of location | [optional] |
| **longitude** | **Double**| Longitude component of location | [optional] |
| **radius** | **Integer**| Radius around the search location (Unit - Miles) | [optional] |
| **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] |
| **includeLease** | **Boolean**| Boolean param to search for listings that include leasing options in them | [optional] |
| **includeFinance** | **Boolean**| Boolean param to search for listings that include finance options in them | [optional] |
| **leaseTerm** | **String**| Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60 | [optional] |
| **leaseDownPayment** | **String**| Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60 | [optional] |
| **leaseEmp** | **String**| Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60 | [optional] |
| **financeLoanTerm** | **String**| Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60 | [optional] |
| **financeLoanApr** | **String**| Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60 | [optional] |
| **financeEmp** | **String**| Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60 | [optional] |
| **financeDownPayment** | **String**| Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60 | [optional] |
| **financeDownPaymentPer** | **String**| Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60 | [optional] |
| **carType** | **String**| Car type. Allowed values are - new / used / certified | [optional] [enum: new, used, certified] |
| **carfax1Owner** | **String**| Indicates whether car has had only one owner or not | [optional] [enum: true, false] |
| **carfaxCleanTitle** | **String**| Indicates whether car has clean ownership records | [optional] [enum: true, false] |
| **yearRange** | **String**| Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021 | [optional] |
| **year** | **String**| To filter listing on their year | [optional] |
| **make** | **String**| To filter listings on their make | [optional] |
| **model** | **String**| To filter listings on their model | [optional] |
| **trim** | **String**| To filter listing on their trim | [optional] |
| **dealerId** | **String**| Dealer id to filter the listings. | [optional] |
| **vin** | **String**| To filter listing on their VIN | [optional] |
| **source** | **String**| To filter listing on their source | [optional] |
| **bodyType** | **String**| To filter listing on their body type | [optional] |
| **bodySubtype** | **String**| Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] |
| **vehicleType** | **String**| To filter listing on their vehicle type | [optional] |
| **vins** | **String**| Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc | [optional] |
| **taxonomyVins** | **String**| Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API. | [optional] |
| **ymmt** | **String**| Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations. | [optional] |
| **match** | **String**| Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match | [optional] |
| **cylinders** | **String**| To filter listing on their cylinders | [optional] |
| **transmission** | **String**| To filter listing on their transmission | [optional] |
| **doors** | **String**| Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated | [optional] |
| **drivetrain** | **String**| To filter listing on their drivetrain | [optional] |
| **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] |
| **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] |
| **baseExteriorColor** | **String**| Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated | [optional] |
| **baseInteriorColor** | **String**| Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated | [optional] |
| **engine** | **String**| To filter listing on their engine | [optional] |
| **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] |
| **engineAspiration** | **String**| Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated | [optional] |
| **engineBlock** | **String**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] |
| **highwayMpgRange** | **String**| Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **cityMpgRange** | **String**| City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **milesRange** | **String**| Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **priceRange** | **String**| Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **msrpRange** | **String**| MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **domRange** | **String**| Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **lastSeenRange** | **String**| Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenRange** | **String**| First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenAtSourceRange** | **String**| First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenAtMcRange** | **String**| First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **lastSeenDays** | **String**| Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenDays** | **String**| First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenAtSourceDays** | **String**| First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenAtMcDays** | **String**| First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] |
| **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] [enum: asc, desc, ASC, DESC] |
| **rows** | **Integer**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10] |
| **start** | **Integer**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0] |
| **includeNonVinListings** | **Boolean**| To include non vin listings. Default is false | [optional] [default to false] |
| **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] |
| **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] |
| **facetSort** | **String**| Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param | [optional] [default to count] [enum: count, index] |
| **stats** | **String**| The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. | [optional] |
| **country** | **String**| To filter listing on Country in which they are listed | [optional] [default to US] [enum: US, CA, us, ca, all, ALL] |
| **plot** | **Boolean**| If plot has value true results in around 25k coordinates with limited fields to plot respective graph | [optional] |
| **nodedup** | **Boolean**| If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin | [optional] |
| **dedup** | **Boolean**| If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source | [optional] |
| **owned** | **Boolean**| Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself | [optional] |
| **state** | **String**| To filter listing on State in which they are listed | [optional] |
| **city** | **String**| To filter listing on City in which they are listed | [optional] |
| **msaCode** | **String**| To filter listing on msa code in which they are listed | [optional] |
| **dealerName** | **String**| Filter listings on dealer_name | [optional] |
| **dealershipGroupName** | **String**| Name of the dealership group to search for | [optional] |
| **trimO** | **String**| Filter listings on web scraped trim | [optional] |
| **trimR** | **String**| Filter trim on custom possible matches | [optional] |
| **domActiveRange** | **String**| Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **dom180Range** | **String**| Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **excludeCertified** | **Boolean**| Boolean param to exclude certified cars from search results | [optional] |
| **fuelType** | **String**| To filter listing on their fuel type | [optional] |
| **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] [enum: franchise, independent] |
| **photoLinks** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them | [optional] |
| **photoLinksCached** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them | [optional] |
| **stockNo** | **String**| To filter listing on their stock number on lot | [optional] |
| **sold** | **Boolean**| sold parameter to fetch only sold listings | [optional] |
| **includeRelevantLinks** | **Boolean**| To include_relevant_links. Default is true | [optional] [default to false] |
| **expired** | **String**| Boolean falg to either fetch only the expired listings or active ones | [optional] [enum: true, false] |
| **excludeDealerIds** | **String**| A list of dealer ids to exclude from result | [optional] |
| **excludeSources** | **String**| A list of sources to exclude from result | [optional] |
| **inTransit** | **String**| A boolean to filter in transit vehicles | [optional] [enum: true, false] |
| **seatingCapacity** | **String**| To filter on vehicle seating capacity | [optional] |
| **activeInventoryDateRange** | **String**| date range to filter listings that were active within given date range. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **engineSizeRange** | **String**| Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2 | [optional] |
| **priceChangeRange** | **String**| Price change range to filter listings with price change within given price_change_range. Range to be given in the format - min-max e.g. 10-500 | [optional] |

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of all cars listings matching the search &amp; filter criteria |  -  |
| **0** | Error |  -  |

<a id="searchCarUkRecentsGet"></a>
# **searchCarUkRecentsGet**
> UKSearchResponse searchCarUkRecentsGet(apiKey, appendApiKey, latitude, longitude, radius, zip, includeLease, includeFinance, leaseTerm, leaseDownPayment, leaseEmp, financeLoanTerm, financeLoanApr, financeEmp, financeDownPayment, financeDownPaymentPer, carType, carfax1Owner, carfaxCleanTitle, yearRange, year, make, model, trim, dealerId, source, bodyType, bodySubtype, vehicleType, ymmt, match, cylinders, transmission, doors, drivetrain, exteriorColor, interiorColor, baseExteriorColor, baseInteriorColor, engine, engineSize, engineAspiration, engineBlock, highwayMpgRange, cityMpgRange, combinedMpgRange, milesRange, priceRange, msrpRange, domRange, lastSeenRange, firstSeenRange, firstSeenAtSourceRange, firstSeenAtMcRange, lastSeenDays, firstSeenDays, firstSeenAtSourceDays, firstSeenAtMcDays, sortBy, sortOrder, rows, start, includeNonVinListings, facets, rangeFacets, facetSort, stats, country, plot, nodedup, dedup, owned, state, city, msaCode, dealerName, dealershipGroupName, trimO, trimR, domActiveRange, dom180Range, excludeCertified, fuelType, dealerType, photoLinks, photoLinksCached, stockNo, sold, includeRelevantLinks, expired, excludeDealerIds, excludeSources, inTransit, seatingCapacity, insuranceGroup, vrm, numOwners, variant, postalCode, writeOffCategory, fcaStatus, activeInventoryDateRange, engineSizeRange, priceChangeRange)

Gets Recent UK car listings for the given search criteria

This API produces a list of recently active (past 90 days) cars from the market for the given search criteria

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CarSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    CarSearchApi apiInstance = new CarSearchApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean appendApiKey = true; // Boolean | Flag on whether to include api_key in response API urls (if any)
    Double latitude = 3.4D; // Double | Latitude component of location
    Double longitude = 3.4D; // Double | Longitude component of location
    Integer radius = 56; // Integer | Radius around the search location (Unit - Miles)
    String zip = "zip_example"; // String | To filter listing on ZIP around which they are listed
    Boolean includeLease = true; // Boolean | Boolean param to search for listings that include leasing options in them
    Boolean includeFinance = true; // Boolean | Boolean param to search for listings that include finance options in them
    String leaseTerm = "leaseTerm_example"; // String | Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term=30-60
    String leaseDownPayment = "leaseDownPayment_example"; // String | Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment=30-60
    String leaseEmp = "leaseEmp_example"; // String | Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp=30-60
    String financeLoanTerm = "financeLoanTerm_example"; // String | Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term=30-60
    String financeLoanApr = "financeLoanApr_example"; // String | Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr=30-60
    String financeEmp = "financeEmp_example"; // String | Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp=30-60
    String financeDownPayment = "financeDownPayment_example"; // String | Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment=30-60
    String financeDownPaymentPer = "financeDownPaymentPer_example"; // String | Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per=30-60
    String carType = "new"; // String | Car type. Allowed values are - new / used / certified
    String carfax1Owner = "true"; // String | Indicates whether car has had only one owner or not
    String carfaxCleanTitle = "true"; // String | Indicates whether car has clean ownership records
    String yearRange = "yearRange_example"; // String | Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
    String year = "year_example"; // String | To filter listing on their year
    String make = "make_example"; // String | To filter listings on their make
    String model = "model_example"; // String | To filter listings on their model
    String trim = "trim_example"; // String | To filter listing on their trim
    String dealerId = "dealerId_example"; // String | Dealer id to filter the listings.
    String source = "source_example"; // String | To filter listing on their source
    String bodyType = "bodyType_example"; // String | To filter listing on their body type
    String bodySubtype = "bodySubtype_example"; // String | Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
    String vehicleType = "vehicleType_example"; // String | To filter listing on their vehicle type
    String ymmt = "ymmt_example"; // String | Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe '|' character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - 'year|make||' or 'year|make|model' or '|make|model|' combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the 'vins' or 'taxonomy_vins' parameter to the search api instead the year|make|model|trim combinations.
    String match = "match_example"; // String | Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
    String cylinders = "cylinders_example"; // String | To filter listing on their cylinders
    String transmission = "transmission_example"; // String | To filter listing on their transmission
    String doors = "doors_example"; // String | Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
    String drivetrain = "drivetrain_example"; // String | To filter listing on their drivetrain
    String exteriorColor = "exteriorColor_example"; // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
    String interiorColor = "interiorColor_example"; // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
    String baseExteriorColor = "baseExteriorColor_example"; // String | Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
    String baseInteriorColor = "baseInteriorColor_example"; // String | Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
    String engine = "engine_example"; // String | To filter listing on their engine
    String engineSize = "engineSize_example"; // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
    String engineAspiration = "engineAspiration_example"; // String | Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
    String engineBlock = "engineBlock_example"; // String | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
    String highwayMpgRange = "highwayMpgRange_example"; // String | Highway mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String cityMpgRange = "cityMpgRange_example"; // String | City mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String combinedMpgRange = "combinedMpgRange_example"; // String | Combined mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String milesRange = "milesRange_example"; // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    String priceRange = "priceRange_example"; // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String msrpRange = "msrpRange_example"; // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String domRange = "domRange_example"; // String | Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    String lastSeenRange = "lastSeenRange_example"; // String | Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenRange = "firstSeenRange_example"; // String | First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenAtSourceRange = "firstSeenAtSourceRange_example"; // String | First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenAtMcRange = "firstSeenAtMcRange_example"; // String | First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String lastSeenDays = "lastSeenDays_example"; // String | Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenDays = "firstSeenDays_example"; // String | First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenAtSourceDays = "firstSeenAtSourceDays_example"; // String | First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
    String firstSeenAtMcDays = "firstSeenAtMcDays_example"; // String | First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
    String sortBy = "sortBy_example"; // String | Sort by field. Default sort field is distance from the given point
    String sortOrder = "asc"; // String | Sort order - asc or desc. Default sort order is asc
    Integer rows = 10; // Integer | Number of results to return. Default is 10. Max is 50
    Integer start = 0; // Integer | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    Boolean includeNonVinListings = false; // Boolean | To include non vin listings. Default is false
    String facets = "facets_example"; // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    String rangeFacets = "rangeFacets_example"; // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    String facetSort = "count"; // String | Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
    String stats = "stats_example"; // String | The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
    String country = "uk"; // String | To filter listing on Country in which they are listed
    Boolean plot = true; // Boolean | If plot has value true results in around 25k coordinates with limited fields to plot respective graph
    Boolean nodedup = true; // Boolean | If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
    Boolean dedup = true; // Boolean | If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
    Boolean owned = true; // Boolean | Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
    String state = "state_example"; // String | To filter listing on State in which they are listed
    String city = "city_example"; // String | To filter listing on City in which they are listed
    String msaCode = "msaCode_example"; // String | To filter listing on msa code in which they are listed
    String dealerName = "dealerName_example"; // String | Filter listings on dealer_name
    String dealershipGroupName = "dealershipGroupName_example"; // String | Name of the dealership group to search for
    String trimO = "trimO_example"; // String | Filter listings on web scraped trim
    String trimR = "trimR_example"; // String | Filter trim on custom possible matches
    String domActiveRange = "domActiveRange_example"; // String | Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    String dom180Range = "dom180Range_example"; // String | Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
    Boolean excludeCertified = true; // Boolean | Boolean param to exclude certified cars from search results
    String fuelType = "fuelType_example"; // String | To filter listing on their fuel type
    String dealerType = "franchise"; // String | Filter based on dealer type independant or franchise
    Boolean photoLinks = true; // Boolean | A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don't have them
    Boolean photoLinksCached = true; // Boolean | A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don't have them
    String stockNo = "stockNo_example"; // String | To filter listing on their stock number on lot
    Boolean sold = true; // Boolean | sold parameter to fetch only sold listings
    Boolean includeRelevantLinks = false; // Boolean | To include_relevant_links. Default is true
    String expired = "true"; // String | Boolean falg to either fetch only the expired listings or active ones
    String excludeDealerIds = "excludeDealerIds_example"; // String | A list of dealer ids to exclude from result
    String excludeSources = "excludeSources_example"; // String | A list of sources to exclude from result
    String inTransit = "true"; // String | A boolean to filter in transit vehicles
    String seatingCapacity = "seatingCapacity_example"; // String | To filter on vehicle seating capacity
    String insuranceGroup = "insuranceGroup_example"; // String | Insurance Group
    String vrm = "vrm_example"; // String | To filter on vrm
    String numOwners = "numOwners_example"; // String | Number of owners. Range to be given in the format - min-max e.g. 1000-5000
    String variant = "variant_example"; // String | To filter listing on their variant
    String postalCode = "postalCode_example"; // String | To filter listing on postal code around which they are listed
    String writeOffCategory = "writeOffCategory_example"; // String | write off category
    String fcaStatus = "fcaStatus_example"; // String | To filter on fca status
    String activeInventoryDateRange = "activeInventoryDateRange_example"; // String | date range to filter listings that were active within given date range. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String engineSizeRange = "engineSizeRange_example"; // String | Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
    String priceChangeRange = "priceChangeRange_example"; // String | Price change range to filter listings with price change within given price_change_range. Range to be given in the format - min-max e.g. 10-500
    try {
      UKSearchResponse result = apiInstance.searchCarUkRecentsGet(apiKey, appendApiKey, latitude, longitude, radius, zip, includeLease, includeFinance, leaseTerm, leaseDownPayment, leaseEmp, financeLoanTerm, financeLoanApr, financeEmp, financeDownPayment, financeDownPaymentPer, carType, carfax1Owner, carfaxCleanTitle, yearRange, year, make, model, trim, dealerId, source, bodyType, bodySubtype, vehicleType, ymmt, match, cylinders, transmission, doors, drivetrain, exteriorColor, interiorColor, baseExteriorColor, baseInteriorColor, engine, engineSize, engineAspiration, engineBlock, highwayMpgRange, cityMpgRange, combinedMpgRange, milesRange, priceRange, msrpRange, domRange, lastSeenRange, firstSeenRange, firstSeenAtSourceRange, firstSeenAtMcRange, lastSeenDays, firstSeenDays, firstSeenAtSourceDays, firstSeenAtMcDays, sortBy, sortOrder, rows, start, includeNonVinListings, facets, rangeFacets, facetSort, stats, country, plot, nodedup, dedup, owned, state, city, msaCode, dealerName, dealershipGroupName, trimO, trimR, domActiveRange, dom180Range, excludeCertified, fuelType, dealerType, photoLinks, photoLinksCached, stockNo, sold, includeRelevantLinks, expired, excludeDealerIds, excludeSources, inTransit, seatingCapacity, insuranceGroup, vrm, numOwners, variant, postalCode, writeOffCategory, fcaStatus, activeInventoryDateRange, engineSizeRange, priceChangeRange);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CarSearchApi#searchCarUkRecentsGet");
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
| **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true] |
| **latitude** | **Double**| Latitude component of location | [optional] |
| **longitude** | **Double**| Longitude component of location | [optional] |
| **radius** | **Integer**| Radius around the search location (Unit - Miles) | [optional] |
| **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] |
| **includeLease** | **Boolean**| Boolean param to search for listings that include leasing options in them | [optional] |
| **includeFinance** | **Boolean**| Boolean param to search for listings that include finance options in them | [optional] |
| **leaseTerm** | **String**| Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60 | [optional] |
| **leaseDownPayment** | **String**| Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60 | [optional] |
| **leaseEmp** | **String**| Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60 | [optional] |
| **financeLoanTerm** | **String**| Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60 | [optional] |
| **financeLoanApr** | **String**| Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60 | [optional] |
| **financeEmp** | **String**| Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60 | [optional] |
| **financeDownPayment** | **String**| Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60 | [optional] |
| **financeDownPaymentPer** | **String**| Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60 | [optional] |
| **carType** | **String**| Car type. Allowed values are - new / used / certified | [optional] [enum: new, used, certified] |
| **carfax1Owner** | **String**| Indicates whether car has had only one owner or not | [optional] [enum: true, false] |
| **carfaxCleanTitle** | **String**| Indicates whether car has clean ownership records | [optional] [enum: true, false] |
| **yearRange** | **String**| Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021 | [optional] |
| **year** | **String**| To filter listing on their year | [optional] |
| **make** | **String**| To filter listings on their make | [optional] |
| **model** | **String**| To filter listings on their model | [optional] |
| **trim** | **String**| To filter listing on their trim | [optional] |
| **dealerId** | **String**| Dealer id to filter the listings. | [optional] |
| **source** | **String**| To filter listing on their source | [optional] |
| **bodyType** | **String**| To filter listing on their body type | [optional] |
| **bodySubtype** | **String**| Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] |
| **vehicleType** | **String**| To filter listing on their vehicle type | [optional] |
| **ymmt** | **String**| Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations. | [optional] |
| **match** | **String**| Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match | [optional] |
| **cylinders** | **String**| To filter listing on their cylinders | [optional] |
| **transmission** | **String**| To filter listing on their transmission | [optional] |
| **doors** | **String**| Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated | [optional] |
| **drivetrain** | **String**| To filter listing on their drivetrain | [optional] |
| **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] |
| **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] |
| **baseExteriorColor** | **String**| Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated | [optional] |
| **baseInteriorColor** | **String**| Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated | [optional] |
| **engine** | **String**| To filter listing on their engine | [optional] |
| **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] |
| **engineAspiration** | **String**| Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated | [optional] |
| **engineBlock** | **String**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] |
| **highwayMpgRange** | **String**| Highway mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **cityMpgRange** | **String**| City mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **combinedMpgRange** | **String**| Combined mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **milesRange** | **String**| Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **priceRange** | **String**| Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **msrpRange** | **String**| MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **domRange** | **String**| Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **lastSeenRange** | **String**| Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenRange** | **String**| First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenAtSourceRange** | **String**| First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenAtMcRange** | **String**| First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **lastSeenDays** | **String**| Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenDays** | **String**| First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenAtSourceDays** | **String**| First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **firstSeenAtMcDays** | **String**| First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] |
| **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] |
| **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] [enum: asc, desc, ASC, DESC] |
| **rows** | **Integer**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10] |
| **start** | **Integer**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0] |
| **includeNonVinListings** | **Boolean**| To include non vin listings. Default is false | [optional] [default to false] |
| **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] |
| **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] |
| **facetSort** | **String**| Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param | [optional] [default to count] [enum: count, index] |
| **stats** | **String**| The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. | [optional] |
| **country** | **String**| To filter listing on Country in which they are listed | [optional] [default to uk] [enum: uk, england, scotland, northan ireland, wales] |
| **plot** | **Boolean**| If plot has value true results in around 25k coordinates with limited fields to plot respective graph | [optional] |
| **nodedup** | **Boolean**| If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin | [optional] |
| **dedup** | **Boolean**| If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source | [optional] |
| **owned** | **Boolean**| Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself | [optional] |
| **state** | **String**| To filter listing on State in which they are listed | [optional] |
| **city** | **String**| To filter listing on City in which they are listed | [optional] |
| **msaCode** | **String**| To filter listing on msa code in which they are listed | [optional] |
| **dealerName** | **String**| Filter listings on dealer_name | [optional] |
| **dealershipGroupName** | **String**| Name of the dealership group to search for | [optional] |
| **trimO** | **String**| Filter listings on web scraped trim | [optional] |
| **trimR** | **String**| Filter trim on custom possible matches | [optional] |
| **domActiveRange** | **String**| Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **dom180Range** | **String**| Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] |
| **excludeCertified** | **Boolean**| Boolean param to exclude certified cars from search results | [optional] |
| **fuelType** | **String**| To filter listing on their fuel type | [optional] |
| **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] [enum: franchise, independent] |
| **photoLinks** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them | [optional] |
| **photoLinksCached** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them | [optional] |
| **stockNo** | **String**| To filter listing on their stock number on lot | [optional] |
| **sold** | **Boolean**| sold parameter to fetch only sold listings | [optional] |
| **includeRelevantLinks** | **Boolean**| To include_relevant_links. Default is true | [optional] [default to false] |
| **expired** | **String**| Boolean falg to either fetch only the expired listings or active ones | [optional] [enum: true, false] |
| **excludeDealerIds** | **String**| A list of dealer ids to exclude from result | [optional] |
| **excludeSources** | **String**| A list of sources to exclude from result | [optional] |
| **inTransit** | **String**| A boolean to filter in transit vehicles | [optional] [enum: true, false] |
| **seatingCapacity** | **String**| To filter on vehicle seating capacity | [optional] |
| **insuranceGroup** | **String**| Insurance Group | [optional] |
| **vrm** | **String**| To filter on vrm | [optional] |
| **numOwners** | **String**| Number of owners. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **variant** | **String**| To filter listing on their variant | [optional] |
| **postalCode** | **String**| To filter listing on postal code around which they are listed | [optional] |
| **writeOffCategory** | **String**| write off category | [optional] |
| **fcaStatus** | **String**| To filter on fca status | [optional] |
| **activeInventoryDateRange** | **String**| date range to filter listings that were active within given date range. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **engineSizeRange** | **String**| Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2 | [optional] |
| **priceChangeRange** | **String**| Price change range to filter listings with price change within given price_change_range. Range to be given in the format - min-max e.g. 10-500 | [optional] |

### Return type

[**UKSearchResponse**](UKSearchResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of all cars listings matching the search &amp; filter criteria |  -  |
| **0** | Error |  -  |

