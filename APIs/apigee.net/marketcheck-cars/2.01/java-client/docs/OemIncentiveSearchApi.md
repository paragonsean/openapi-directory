# OemIncentiveSearchApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**oemSearch**](OemIncentiveSearchApi.md#oemSearch) | **GET** /search/car/incentive/oem | Gets oem incentive listings for the given search criteria |


<a id="oemSearch"></a>
# **oemSearch**
> SearchResponse oemSearch(apiKey, offerType, year, make, model, trim, msrp, apr, monthly, monthlyPerThousand, downPayment, dueAtSigning, securityDeposit, dispositionFee, acquisitionFee, duration, dealerContribution, mileageCharge, mileageChargeLimit, cashbackAmount, cashbackTargetGroup, leaseEndPurchaseOption, netCapitalisedCost, grossCapitalisedCost, totalMonthlyPayment, zip, city, state, country, latitude, longitude, radius, searchText, lastSeenRange, firstSeenRange, sortBy, sortOrder, rows, start, facets, rangeFacets, facetSort, stats)

Gets oem incentive listings for the given search criteria

This endpoint is the meat of the API and serves many purposes. This API produces a list of currently active oem incentive from the market for the given search criteria. The API results are limited to allow pagination upto 10000 rows.   The search API facilitates the following use cases -  1. Search Cars around a given geo-point within a given radius  2. Search cars for a specific year / make / model or combination of these  3. Search cars matching multiple year, make, model combinatins in the same search request 4. Filter results by most car specification attributes 5. Search for similar cars by VIN or Taxonomy VIN  6. Filter cars within a given price / miles / days on market (dom) range 7. Specify a sort order for the results on price / miles / dom / listed date  8. Search cars for a given City / State combination  9. Get Facets to build the search drill downs  10. Get Market averages for price/miles/dom for your search

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OemIncentiveSearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://marketcheck-prod.apigee.net/v2");
    
    // Configure HTTP basic authorization: authorizeEndpoint
    HttpBasicAuth authorizeEndpoint = (HttpBasicAuth) defaultClient.getAuthentication("authorizeEndpoint");
    authorizeEndpoint.setUsername("YOUR USERNAME");
    authorizeEndpoint.setPassword("YOUR PASSWORD");

    OemIncentiveSearchApi apiInstance = new OemIncentiveSearchApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API Authentication Key. Mandatory with all API calls.
    String offerType = "lease"; // String | The type of the incentive
    String year = "year_example"; // String | To filter listing on their year
    String make = "make_example"; // String | To filter listings on their make
    String model = "model_example"; // String | To filter listings on their model
    String trim = "trim_example"; // String | To filter listing on their trim
    String msrp = "msrp_example"; // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String apr = "apr_example"; // String | APR range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
    String monthly = "monthly_example"; // String | To filter listing on Monthly payment amount, usually populated in Lease offers
    String monthlyPerThousand = "monthlyPerThousand_example"; // String | To filter listing on monthly amount to be paid by customer for every $1000 financed at the advertised APR rate
    String downPayment = "downPayment_example"; // String | To filter listing on down payment offer on car
    String dueAtSigning = "dueAtSigning_example"; // String | To filter listing on total amount due at signing, that usually includes first month payment, down payment, acquisition fee etc
    String securityDeposit = "securityDeposit_example"; // String | To filter listing on security deposit required for the offer
    String dispositionFee = "dispositionFee_example"; // String | To filter listing on disposition fee of the car
    String acquisitionFee = "acquisitionFee_example"; // String | To filter listing on acquisition fee of the car
    String duration = "duration_example"; // String | To filter listing on offer duration in months
    String dealerContribution = "dealerContribution_example"; // String | To filter listing on any contribution from dealer's side
    String mileageCharge = "mileageCharge_example"; // String | Mileage Charge Range range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 100-1000
    String mileageChargeLimit = "mileageChargeLimit_example"; // String | To filter listing on mileage charge limit the offer is valid up to under the default clauses
    String cashbackAmount = "cashbackAmount_example"; // String | To filter listing on cashback amounts listed in offer
    String cashbackTargetGroup = "cashbackTargetGroup_example"; // String | To filter listing on the demographic or any other entity for whom this cashback offer is for. Not all target groups are identified but the most common ones are tagged like Military, Grad students Current owners etc
    String leaseEndPurchaseOption = "leaseEndPurchaseOption_example"; // String | To filter listing on amount at the lease end to pay for buying the car
    String netCapitalisedCost = "netCapitalisedCost_example"; // String | To filter listing on net capitalised cost of the car
    String grossCapitalisedCost = "grossCapitalisedCost_example"; // String | To filter listing on gross capitalised cost of the car
    String totalMonthlyPayment = "totalMonthlyPayment_example"; // String | To filter listing on gross capitalised cost of the car
    String zip = "zip_example"; // String | To filter listing on ZIP around which they are listed
    String city = "city_example"; // String | To filter listing on City in which they are listed
    String state = "state_example"; // String | To filter listing on State in which they are listed
    String country = "US"; // String | To filter listing on Country in which they are listed
    Double latitude = 3.4D; // Double | Latitude component of location
    Double longitude = 3.4D; // Double | Longitude component of location
    Integer radius = 56; // Integer | Radius around the search location (Unit - Miles)
    String searchText = "searchText_example"; // String | To search a substring across entire document
    String lastSeenRange = "lastSeenRange_example"; // String | Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String firstSeenRange = "firstSeenRange_example"; // String | First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
    String sortBy = "sortBy_example"; // String | Sort by field. Default sort field is distance from the given point
    String sortOrder = "asc"; // String | Sort order - asc or desc. Default sort order is asc
    Integer rows = 10; // Integer | Number of results to return. Default is 10. Max is 50
    Integer start = 0; // Integer | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
    String facets = "facets_example"; // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
    String rangeFacets = "rangeFacets_example"; // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
    String facetSort = "count"; // String | Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
    String stats = "stats_example"; // String | The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
    try {
      SearchResponse result = apiInstance.oemSearch(apiKey, offerType, year, make, model, trim, msrp, apr, monthly, monthlyPerThousand, downPayment, dueAtSigning, securityDeposit, dispositionFee, acquisitionFee, duration, dealerContribution, mileageCharge, mileageChargeLimit, cashbackAmount, cashbackTargetGroup, leaseEndPurchaseOption, netCapitalisedCost, grossCapitalisedCost, totalMonthlyPayment, zip, city, state, country, latitude, longitude, radius, searchText, lastSeenRange, firstSeenRange, sortBy, sortOrder, rows, start, facets, rangeFacets, facetSort, stats);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OemIncentiveSearchApi#oemSearch");
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
| **offerType** | **String**| The type of the incentive | [optional] [enum: lease, finance, cash] |
| **year** | **String**| To filter listing on their year | [optional] |
| **make** | **String**| To filter listings on their make | [optional] |
| **model** | **String**| To filter listings on their model | [optional] |
| **trim** | **String**| To filter listing on their trim | [optional] |
| **msrp** | **String**| MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **apr** | **String**| APR range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] |
| **monthly** | **String**| To filter listing on Monthly payment amount, usually populated in Lease offers | [optional] |
| **monthlyPerThousand** | **String**| To filter listing on monthly amount to be paid by customer for every $1000 financed at the advertised APR rate | [optional] |
| **downPayment** | **String**| To filter listing on down payment offer on car | [optional] |
| **dueAtSigning** | **String**| To filter listing on total amount due at signing, that usually includes first month payment, down payment, acquisition fee etc | [optional] |
| **securityDeposit** | **String**| To filter listing on security deposit required for the offer | [optional] |
| **dispositionFee** | **String**| To filter listing on disposition fee of the car | [optional] |
| **acquisitionFee** | **String**| To filter listing on acquisition fee of the car | [optional] |
| **duration** | **String**| To filter listing on offer duration in months | [optional] |
| **dealerContribution** | **String**| To filter listing on any contribution from dealer&#39;s side | [optional] |
| **mileageCharge** | **String**| Mileage Charge Range range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 100-1000 | [optional] |
| **mileageChargeLimit** | **String**| To filter listing on mileage charge limit the offer is valid up to under the default clauses | [optional] |
| **cashbackAmount** | **String**| To filter listing on cashback amounts listed in offer | [optional] |
| **cashbackTargetGroup** | **String**| To filter listing on the demographic or any other entity for whom this cashback offer is for. Not all target groups are identified but the most common ones are tagged like Military, Grad students Current owners etc | [optional] |
| **leaseEndPurchaseOption** | **String**| To filter listing on amount at the lease end to pay for buying the car | [optional] |
| **netCapitalisedCost** | **String**| To filter listing on net capitalised cost of the car | [optional] |
| **grossCapitalisedCost** | **String**| To filter listing on gross capitalised cost of the car | [optional] |
| **totalMonthlyPayment** | **String**| To filter listing on gross capitalised cost of the car | [optional] |
| **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] |
| **city** | **String**| To filter listing on City in which they are listed | [optional] |
| **state** | **String**| To filter listing on State in which they are listed | [optional] |
| **country** | **String**| To filter listing on Country in which they are listed | [optional] [default to US] [enum: US, CA, us, ca] |
| **latitude** | **Double**| Latitude component of location | [optional] |
| **longitude** | **Double**| Longitude component of location | [optional] |
| **radius** | **Integer**| Radius around the search location (Unit - Miles) | [optional] |
| **searchText** | **String**| To search a substring across entire document | [optional] |
| **lastSeenRange** | **String**| Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **firstSeenRange** | **String**| First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] |
| **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] |
| **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] [enum: asc, desc, ASC, DESC] |
| **rows** | **Integer**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10] |
| **start** | **Integer**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0] |
| **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] |
| **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] |
| **facetSort** | **String**| Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param | [optional] [default to count] [enum: count, index] |
| **stats** | **String**| The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. | [optional] |

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
| **200** | List of all oem incentive listings matching the search &amp; filter criteria |  -  |
| **0** | Error |  -  |

