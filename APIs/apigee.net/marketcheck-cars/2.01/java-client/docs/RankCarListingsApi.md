# RankCarListingsApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rankCar**](RankCarListingsApi.md#rankCar) | **POST** /search/car/active/rank/listings | Compute relative rank for car listings. |
| [**searchAndRankCar**](RankCarListingsApi.md#searchAndRankCar) | **POST** /search/car/active/rank | Compute relative rank for car listings. |


<a id="rankCar"></a>
# **rankCar**
> CarRankResponse rankCar(carRankRequest, apiKey, appendApiKey)

Compute relative rank for car listings.

Computer rank for car listings based on inputs provided.Weights for ranking parameters can also be provided.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RankCarListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    RankCarListingsApi apiInstance = new RankCarListingsApi(defaultClient);
    CarRankRequest carRankRequest = new CarRankRequest(); // CarRankRequest | Inputs needed for ranking a group of car listings
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    Boolean appendApiKey = true; // Boolean | Flag on whether to include api_key in response API urls (if any)
    try {
      CarRankResponse result = apiInstance.rankCar(carRankRequest, apiKey, appendApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RankCarListingsApi#rankCar");
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
| **carRankRequest** | [**CarRankRequest**](CarRankRequest.md)| Inputs needed for ranking a group of car listings | |
| **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] |
| **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true] |

### Return type

[**CarRankResponse**](CarRankResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rank listings based on inputs provided. |  -  |
| **0** | Error |  -  |

<a id="searchAndRankCar"></a>
# **searchAndRankCar**
> CarRankResponse searchAndRankCar(carRankRequest, apiKey, appendApiKey, latitude, longitude, radius, zip, includeLease, includeFinance, leaseTerm, leaseDownPayment, leaseEmp, financeLoanTerm, financeLoanApr, financeEmp, financeDownPayment, financeDownPaymentPer, carType, carfax1Owner, carfaxCleanTitle, year, make, model, trim, vin, bodyType, bodySubtype, vehicleType, vins, taxonomyVins, ymmt, match, cylinders, transmission, doors, drivetrain, exteriorColor, interiorColor, baseExteriorColor, baseInteriorColor, engine, engineSize, engineAspiration, engineBlock, highwayMpgRange, cityMpgRange, milesRange, priceRange, msrpRange, domRange, sortBy, sortOrder, rows, start, includeNonVinListings, msaCode, facets, rangeFacets, facetSort, stats, country, plot, nodedup, dedup, owned, state, city, trimO, trimR, domActiveRange, dom180Range, excludeCertified, fuelType, dealerType, photoLinks, photoLinksCached, stockNo, lastSeenRange, firstSeenRange, firstSeenAtSourceRange, firstSeenAtMcRange, lastSeenDays, firstSeenDays, firstSeenAtSourceDays, firstSeenAtMcDays, inventoryType, page)

Compute relative rank for car listings.

Computer rank for car listings based on inputs provided.Weights for ranking parameters can also be provided.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RankCarListingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    RankCarListingsApi apiInstance = new RankCarListingsApi(defaultClient);
    CarRankRequest carRankRequest = new CarRankRequest(); // CarRankRequest | Inputs needed for ranking a group of car listings
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
    String milesRange = "1-"; // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
    String priceRange = "1-"; // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
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
    String inventoryType = "used"; // String | To filter listing on their condition. Either used or new
    BigDecimal page = new BigDecimal(78); // BigDecimal | Page number to fetch the results for the given criteria. Default is 1.
    try {
      CarRankResponse result = apiInstance.searchAndRankCar(carRankRequest, apiKey, appendApiKey, latitude, longitude, radius, zip, includeLease, includeFinance, leaseTerm, leaseDownPayment, leaseEmp, financeLoanTerm, financeLoanApr, financeEmp, financeDownPayment, financeDownPaymentPer, carType, carfax1Owner, carfaxCleanTitle, year, make, model, trim, vin, bodyType, bodySubtype, vehicleType, vins, taxonomyVins, ymmt, match, cylinders, transmission, doors, drivetrain, exteriorColor, interiorColor, baseExteriorColor, baseInteriorColor, engine, engineSize, engineAspiration, engineBlock, highwayMpgRange, cityMpgRange, milesRange, priceRange, msrpRange, domRange, sortBy, sortOrder, rows, start, includeNonVinListings, msaCode, facets, rangeFacets, facetSort, stats, country, plot, nodedup, dedup, owned, state, city, trimO, trimR, domActiveRange, dom180Range, excludeCertified, fuelType, dealerType, photoLinks, photoLinksCached, stockNo, lastSeenRange, firstSeenRange, firstSeenAtSourceRange, firstSeenAtMcRange, lastSeenDays, firstSeenDays, firstSeenAtSourceDays, firstSeenAtMcDays, inventoryType, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RankCarListingsApi#searchAndRankCar");
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
| **carRankRequest** | [**CarRankRequest**](CarRankRequest.md)| Inputs needed for ranking a group of car listings | |
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
| **milesRange** | **String**| Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] [default to 1-] |
| **priceRange** | **String**| Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] [default to 1-] |
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
| **inventoryType** | **String**| To filter listing on their condition. Either used or new | [optional] [enum: used, new] |
| **page** | **BigDecimal**| Page number to fetch the results for the given criteria. Default is 1. | [optional] |

### Return type

[**CarRankResponse**](CarRankResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rank listings based on inputs provided. |  -  |
| **0** | Error |  -  |

