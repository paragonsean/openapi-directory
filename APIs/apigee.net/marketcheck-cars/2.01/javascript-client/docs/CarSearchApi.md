# MarketcheckApis.CarSearchApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autoComplete**](CarSearchApi.md#autoComplete) | **GET** /search/car/auto-complete | API for auto-completion of inputs
[**carDealerInventoryActiveGet**](CarSearchApi.md#carDealerInventoryActiveGet) | **GET** /car/dealer/inventory/active | Get dealers active inventory
[**getListing**](CarSearchApi.md#getListing) | **GET** /listing/car/{id} | Listing by id
[**listingCarAuctionIdExtraGet**](CarSearchApi.md#listingCarAuctionIdExtraGet) | **GET** /listing/car/auction/{id}/extra | Long text Listings attributes for Listing with the given id
[**listingCarAuctionIdGet**](CarSearchApi.md#listingCarAuctionIdGet) | **GET** /listing/car/auction/{id} | Listing by id
[**listingCarAuctionIdMediaGet**](CarSearchApi.md#listingCarAuctionIdMediaGet) | **GET** /listing/car/auction/{id}/media | Listing media by id
[**listingCarFsboIdExtraGet**](CarSearchApi.md#listingCarFsboIdExtraGet) | **GET** /listing/car/fsbo/{id}/extra | Long text Listings attributes for Listing with the given id
[**listingCarFsboIdGet**](CarSearchApi.md#listingCarFsboIdGet) | **GET** /listing/car/fsbo/{id} | Listing by id
[**listingCarFsboIdMediaGet**](CarSearchApi.md#listingCarFsboIdMediaGet) | **GET** /listing/car/fsbo/{id}/media | Listing media by id
[**listingCarIdExtraGet**](CarSearchApi.md#listingCarIdExtraGet) | **GET** /listing/car/{id}/extra | Long text Listings attributes for Listing with the given id
[**listingCarIdMediaGet**](CarSearchApi.md#listingCarIdMediaGet) | **GET** /listing/car/{id}/media | Listing media by id
[**listingCarUkIdExtraGet**](CarSearchApi.md#listingCarUkIdExtraGet) | **GET** /listing/car/uk/{id}/extra | Long text Listings attributes for Listing with the given id
[**listingCarUkIdGet**](CarSearchApi.md#listingCarUkIdGet) | **GET** /listing/car/uk/{id} | Listing by id
[**listingCarUkIdMediaGet**](CarSearchApi.md#listingCarUkIdMediaGet) | **GET** /listing/car/uk/{id}/media | Listing media by id
[**search**](CarSearchApi.md#search) | **GET** /search/car/uk/active | Gets active car listings in UK for the given search criteria
[**searchCarActiveGet**](CarSearchApi.md#searchCarActiveGet) | **GET** /search/car/active | Gets active car listings for the given search criteria
[**searchCarAuctionActiveGet**](CarSearchApi.md#searchCarAuctionActiveGet) | **GET** /search/car/auction/active | Gets active auction car listings for the given search criteria
[**searchCarFsboActiveGet**](CarSearchApi.md#searchCarFsboActiveGet) | **GET** /search/car/fsbo/active | Gets active private party car listings for the given search criteria
[**searchCarRecentsGet**](CarSearchApi.md#searchCarRecentsGet) | **GET** /search/car/recents | Gets Recent car listings for the given search criteria
[**searchCarUkRecentsGet**](CarSearchApi.md#searchCarUkRecentsGet) | **GET** /search/car/uk/recents | Gets Recent UK car listings for the given search criteria



## autoComplete

> SearchAutoCompleteResponse autoComplete(field, input, opts)

API for auto-completion of inputs

Auto-complete the inputs of your end users

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarSearchApi();
let field = "field_example"; // String | Field name for which you want auto-completion
let input = "input_example"; // String | Input entered so far
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'year': "year_example", // String | To filter listing on their year
  'make': "make_example", // String | To filter listings on their make
  'model': "model_example", // String | To filter listings on their model
  'trim': "trim_example", // String | To filter listing on their trim
  'bodyType': "bodyType_example", // String | To filter listing on their body type
  'bodySubtype': "bodySubtype_example", // String | Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
  'vehicleType': "vehicleType_example", // String | To filter listing on their vehicle type
  'transmission': "transmission_example", // String | To filter listing on their transmission
  'drivetrain': "drivetrain_example", // String | To filter listing on their drivetrain
  'fuelType': "fuelType_example", // String | To filter listing on their fuel type
  'exteriorColor': "exteriorColor_example", // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
  'interiorColor': "interiorColor_example", // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
  'engine': "engine_example", // String | To filter listing on their engine
  'engineSize': "engineSize_example", // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
  'engineBlock': "engineBlock_example", // String | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
  'state': "state_example", // String | To filter listing on State in which they are listed
  'city': "city_example", // String | To filter listing on City in which they are listed
  'source': "source_example", // String | To filter listing on their source only for widget requests
  'dealerId': "dealerId_example", // String | Dealer id to filter the listings.
  'country': "'US'", // String | To filter listing on Country in which they are listed
  'carType': "carType_example", // String | Car type. Allowed values are - new / used
  'includeNonVinListings': "'false'", // String | Flag to indicate whether to include non vin listing terms in results or not. Default is false to avoid un-normalised terms from non vin listings out of results
  'ignoreCase': true, // Boolean | Boolean variable to indicate ignore case of current input
  'termCounts': false, // Boolean | Boolean variable to indicate wheather to include term counts as well in response
  'sortBy': "'index'", // String | Sort the response, either by index or count(default)
  'sellerType': "sellerType_example", // String | seller type for autocomplete
  'radius': 56, // Number | Radius around the search location (Unit - Miles)
  'zip': "zip_example", // String | To filter listing on ZIP around which they are listed
  'inventoryCountRange': "inventoryCountRange_example", // String | Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50
  'excludeDealerIds': "excludeDealerIds_example", // String | A list of dealer ids to exclude from result
  'excludeSources': "excludeSources_example", // String | A list of sources to exclude from result
  'inTransit': "inTransit_example", // String | A boolean to filter in transit vehicles
  'facetMinCount': 1 // Number | Provide minimum count value for facets
};
apiInstance.autoComplete(field, input, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **String**| Field name for which you want auto-completion | 
 **input** | **String**| Input entered so far | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **year** | **String**| To filter listing on their year | [optional] 
 **make** | **String**| To filter listings on their make | [optional] 
 **model** | **String**| To filter listings on their model | [optional] 
 **trim** | **String**| To filter listing on their trim | [optional] 
 **bodyType** | **String**| To filter listing on their body type | [optional] 
 **bodySubtype** | **String**| Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] 
 **vehicleType** | **String**| To filter listing on their vehicle type | [optional] 
 **transmission** | **String**| To filter listing on their transmission | [optional] 
 **drivetrain** | **String**| To filter listing on their drivetrain | [optional] 
 **fuelType** | **String**| To filter listing on their fuel type | [optional] 
 **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] 
 **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] 
 **engine** | **String**| To filter listing on their engine | [optional] 
 **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] 
 **engineBlock** | **String**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] 
 **state** | **String**| To filter listing on State in which they are listed | [optional] 
 **city** | **String**| To filter listing on City in which they are listed | [optional] 
 **source** | **String**| To filter listing on their source only for widget requests | [optional] 
 **dealerId** | **String**| Dealer id to filter the listings. | [optional] 
 **country** | **String**| To filter listing on Country in which they are listed | [optional] [default to &#39;US&#39;]
 **carType** | **String**| Car type. Allowed values are - new / used | [optional] 
 **includeNonVinListings** | **String**| Flag to indicate whether to include non vin listing terms in results or not. Default is false to avoid un-normalised terms from non vin listings out of results | [optional] [default to &#39;false&#39;]
 **ignoreCase** | **Boolean**| Boolean variable to indicate ignore case of current input | [optional] [default to true]
 **termCounts** | **Boolean**| Boolean variable to indicate wheather to include term counts as well in response | [optional] [default to false]
 **sortBy** | **String**| Sort the response, either by index or count(default) | [optional] [default to &#39;index&#39;]
 **sellerType** | **String**| seller type for autocomplete | [optional] 
 **radius** | **Number**| Radius around the search location (Unit - Miles) | [optional] 
 **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] 
 **inventoryCountRange** | **String**| Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **excludeDealerIds** | **String**| A list of dealer ids to exclude from result | [optional] 
 **excludeSources** | **String**| A list of sources to exclude from result | [optional] 
 **inTransit** | **String**| A boolean to filter in transit vehicles | [optional] 
 **facetMinCount** | **Number**| Provide minimum count value for facets | [optional] [default to 1]

### Return type

[**SearchAutoCompleteResponse**](SearchAutoCompleteResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## carDealerInventoryActiveGet

> SearchResponse carDealerInventoryActiveGet(opts)

Get dealers active inventory

Get dealers active inventory

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarSearchApi();
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'appendApiKey': true, // Boolean | Flag on whether to include api_key in response API urls (if any)
  'latitude': 3.4, // Number | Latitude component of location
  'longitude': 3.4, // Number | Longitude component of location
  'radius': 56, // Number | Radius around the search location (Unit - Miles)
  'zip': "zip_example", // String | To filter listing on ZIP around which they are listed
  'includeLease': true, // Boolean | Boolean param to search for listings that include leasing options in them
  'includeFinance': true, // Boolean | Boolean param to search for listings that include finance options in them
  'leaseTerm': "leaseTerm_example", // String | Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term=30-60
  'leaseDownPayment': "leaseDownPayment_example", // String | Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment=30-60
  'leaseEmp': "leaseEmp_example", // String | Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp=30-60
  'financeLoanTerm': "financeLoanTerm_example", // String | Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term=30-60
  'financeLoanApr': "financeLoanApr_example", // String | Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr=30-60
  'financeEmp': "financeEmp_example", // String | Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp=30-60
  'financeDownPayment': "financeDownPayment_example", // String | Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment=30-60
  'financeDownPaymentPer': "financeDownPaymentPer_example", // String | Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per=30-60
  'carType': "carType_example", // String | Car type. Allowed values are - new / used / certified
  'carfax1Owner': "carfax1Owner_example", // String | Indicates whether car has had only one owner or not
  'carfaxCleanTitle': "carfaxCleanTitle_example", // String | Indicates whether car has clean ownership records
  'yearRange': "yearRange_example", // String | Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
  'year': "year_example", // String | To filter listing on their year
  'make': "make_example", // String | To filter listings on their make
  'model': "model_example", // String | To filter listings on their model
  'trim': "trim_example", // String | To filter listing on their trim
  'dealerId': "dealerId_example", // String | Dealer id to filter the listings.
  'vin': "vin_example", // String | To filter listing on their VIN
  'source': "source_example", // String | To filter listing on their source
  'bodyType': "bodyType_example", // String | To filter listing on their body type
  'bodySubtype': "bodySubtype_example", // String | Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
  'vehicleType': "vehicleType_example", // String | To filter listing on their vehicle type
  'vins': "vins_example", // String | Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc
  'taxonomyVins': "taxonomyVins_example", // String | Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API.
  'mm': "mm_example", // String | Make-Model concatenated string. To help passing the results of auto-complete API on mm field, use this parameter and pass in the selected value as is
  'ymm': "ymm_example", // String | Year-Make-Model concatenated string. To help passing the results of auto-complete API on ymm field, use this parameter and pass in the selected value as is
  'ymmt': "ymmt_example", // String | Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe '|' character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - 'year|make||' or 'year|make|model' or '|make|model|' combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the 'vins' or 'taxonomy_vins' parameter to the search api instead the year|make|model|trim combinations.
  'match': "match_example", // String | Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
  'cylinders': "cylinders_example", // String | To filter listing on their cylinders
  'transmission': "transmission_example", // String | To filter listing on their transmission
  'doors': "doors_example", // String | Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
  'drivetrain': "drivetrain_example", // String | To filter listing on their drivetrain
  'exteriorColor': "exteriorColor_example", // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
  'interiorColor': "interiorColor_example", // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
  'baseExteriorColor': "baseExteriorColor_example", // String | Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
  'baseInteriorColor': "baseInteriorColor_example", // String | Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
  'engine': "engine_example", // String | To filter listing on their engine
  'engineSize': "engineSize_example", // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
  'engineAspiration': "engineAspiration_example", // String | Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
  'engineBlock': "engineBlock_example", // String | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
  'highwayMpgRange': "highwayMpgRange_example", // String | Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'cityMpgRange': "cityMpgRange_example", // String | City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'milesRange': "milesRange_example", // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
  'priceRange': "priceRange_example", // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'msrpRange': "msrpRange_example", // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'domRange': "domRange_example", // String | Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'sortBy': "sortBy_example", // String | Sort by field. Default sort field is distance from the given point
  'sortOrder': "sortOrder_example", // String | Sort order - asc or desc. Default sort order is asc
  'rows': 10, // Number | Number of results to return. Default is 10. Max is 50
  'start': 0, // Number | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
  'includeNonVinListings': false, // Boolean | To include non vin listings. Default is false
  'msaCode': "msaCode_example", // String | To filter listing on msa code in which they are listed
  'facets': "facets_example", // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
  'rangeFacets': "rangeFacets_example", // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
  'facetSort': "'count'", // String | Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
  'stats': "stats_example", // String | The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
  'country': "'US'", // String | To filter listing on Country in which they are listed
  'plot': true, // Boolean | If plot has value true results in around 25k coordinates with limited fields to plot respective graph
  'nodedup': true, // Boolean | If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
  'dedup': true, // Boolean | If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
  'owned': true, // Boolean | Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
  'state': "state_example", // String | To filter listing on State in which they are listed
  'city': "city_example", // String | To filter listing on City in which they are listed
  'dealerName': "dealerName_example", // String | Filter listings on dealer_name
  'dealershipGroupName': "dealershipGroupName_example", // String | Name of the dealership group to search for
  'trimO': "trimO_example", // String | Filter listings on web scraped trim
  'trimR': "trimR_example", // String | Filter trim on custom possible matches
  'domActiveRange': "domActiveRange_example", // String | Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'dom180Range': "dom180Range_example", // String | Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'excludeCertified': true, // Boolean | Boolean param to exclude certified cars from search results
  'fuelType': "fuelType_example", // String | To filter listing on their fuel type
  'dealerType': "dealerType_example", // String | Filter based on dealer type independant or franchise
  'photoLinks': true, // Boolean | A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don't have them
  'photoLinksCached': true, // Boolean | A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don't have them
  'stockNo': "stockNo_example", // String | To filter listing on their stock number on lot
  'lastSeenRange': "lastSeenRange_example", // String | Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenRange': "firstSeenRange_example", // String | First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenAtSourceRange': "firstSeenAtSourceRange_example", // String | First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenAtMcRange': "firstSeenAtMcRange_example", // String | First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'lastSeenDays': "lastSeenDays_example", // String | Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenDays': "firstSeenDays_example", // String | First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenAtSourceDays': "firstSeenAtSourceDays_example", // String | First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenAtMcDays': "firstSeenAtMcDays_example", // String | First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
  'includeRelevantLinks': false, // Boolean | To include_relevant_links. Default is true
  'inventoryCountRange': "inventoryCountRange_example", // String | Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50
  'inTransit': "inTransit_example", // String | A boolean to filter in transit vehicles
  'seatingCapacity': "seatingCapacity_example", // String | To filter on vehicle seating capacity
  'engineSizeRange': "engineSizeRange_example", // String | Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
  'powertrainType': "powertrainType_example", // String | To filter on powertrain_type
  'minPhotoLinks': "minPhotoLinks_example", // String | Filter listings based by number of photo links within given range
  'minPhotoLinksCached': "minPhotoLinksCached_example" // String | Filter listings based by number of cached photo links within given range
};
apiInstance.carDealerInventoryActiveGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true]
 **latitude** | **Number**| Latitude component of location | [optional] 
 **longitude** | **Number**| Longitude component of location | [optional] 
 **radius** | **Number**| Radius around the search location (Unit - Miles) | [optional] 
 **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] 
 **includeLease** | **Boolean**| Boolean param to search for listings that include leasing options in them | [optional] 
 **includeFinance** | **Boolean**| Boolean param to search for listings that include finance options in them | [optional] 
 **leaseTerm** | **String**| Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60 | [optional] 
 **leaseDownPayment** | **String**| Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60 | [optional] 
 **leaseEmp** | **String**| Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60 | [optional] 
 **financeLoanTerm** | **String**| Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60 | [optional] 
 **financeLoanApr** | **String**| Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60 | [optional] 
 **financeEmp** | **String**| Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60 | [optional] 
 **financeDownPayment** | **String**| Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60 | [optional] 
 **financeDownPaymentPer** | **String**| Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60 | [optional] 
 **carType** | **String**| Car type. Allowed values are - new / used / certified | [optional] 
 **carfax1Owner** | **String**| Indicates whether car has had only one owner or not | [optional] 
 **carfaxCleanTitle** | **String**| Indicates whether car has clean ownership records | [optional] 
 **yearRange** | **String**| Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021 | [optional] 
 **year** | **String**| To filter listing on their year | [optional] 
 **make** | **String**| To filter listings on their make | [optional] 
 **model** | **String**| To filter listings on their model | [optional] 
 **trim** | **String**| To filter listing on their trim | [optional] 
 **dealerId** | **String**| Dealer id to filter the listings. | [optional] 
 **vin** | **String**| To filter listing on their VIN | [optional] 
 **source** | **String**| To filter listing on their source | [optional] 
 **bodyType** | **String**| To filter listing on their body type | [optional] 
 **bodySubtype** | **String**| Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] 
 **vehicleType** | **String**| To filter listing on their vehicle type | [optional] 
 **vins** | **String**| Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc | [optional] 
 **taxonomyVins** | **String**| Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API. | [optional] 
 **mm** | **String**| Make-Model concatenated string. To help passing the results of auto-complete API on mm field, use this parameter and pass in the selected value as is | [optional] 
 **ymm** | **String**| Year-Make-Model concatenated string. To help passing the results of auto-complete API on ymm field, use this parameter and pass in the selected value as is | [optional] 
 **ymmt** | **String**| Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations. | [optional] 
 **match** | **String**| Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match | [optional] 
 **cylinders** | **String**| To filter listing on their cylinders | [optional] 
 **transmission** | **String**| To filter listing on their transmission | [optional] 
 **doors** | **String**| Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated | [optional] 
 **drivetrain** | **String**| To filter listing on their drivetrain | [optional] 
 **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] 
 **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] 
 **baseExteriorColor** | **String**| Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated | [optional] 
 **baseInteriorColor** | **String**| Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated | [optional] 
 **engine** | **String**| To filter listing on their engine | [optional] 
 **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] 
 **engineAspiration** | **String**| Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated | [optional] 
 **engineBlock** | **String**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] 
 **highwayMpgRange** | **String**| Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **cityMpgRange** | **String**| City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **milesRange** | **String**| Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **priceRange** | **String**| Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **msrpRange** | **String**| MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **domRange** | **String**| Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] 
 **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] 
 **rows** | **Number**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10]
 **start** | **Number**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0]
 **includeNonVinListings** | **Boolean**| To include non vin listings. Default is false | [optional] [default to false]
 **msaCode** | **String**| To filter listing on msa code in which they are listed | [optional] 
 **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] 
 **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] 
 **facetSort** | **String**| Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param | [optional] [default to &#39;count&#39;]
 **stats** | **String**| The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. | [optional] 
 **country** | **String**| To filter listing on Country in which they are listed | [optional] [default to &#39;US&#39;]
 **plot** | **Boolean**| If plot has value true results in around 25k coordinates with limited fields to plot respective graph | [optional] 
 **nodedup** | **Boolean**| If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin | [optional] 
 **dedup** | **Boolean**| If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source | [optional] 
 **owned** | **Boolean**| Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself | [optional] 
 **state** | **String**| To filter listing on State in which they are listed | [optional] 
 **city** | **String**| To filter listing on City in which they are listed | [optional] 
 **dealerName** | **String**| Filter listings on dealer_name | [optional] 
 **dealershipGroupName** | **String**| Name of the dealership group to search for | [optional] 
 **trimO** | **String**| Filter listings on web scraped trim | [optional] 
 **trimR** | **String**| Filter trim on custom possible matches | [optional] 
 **domActiveRange** | **String**| Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **dom180Range** | **String**| Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **excludeCertified** | **Boolean**| Boolean param to exclude certified cars from search results | [optional] 
 **fuelType** | **String**| To filter listing on their fuel type | [optional] 
 **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] 
 **photoLinks** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them | [optional] 
 **photoLinksCached** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them | [optional] 
 **stockNo** | **String**| To filter listing on their stock number on lot | [optional] 
 **lastSeenRange** | **String**| Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenRange** | **String**| First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenAtSourceRange** | **String**| First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenAtMcRange** | **String**| First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **lastSeenDays** | **String**| Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenDays** | **String**| First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenAtSourceDays** | **String**| First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenAtMcDays** | **String**| First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **includeRelevantLinks** | **Boolean**| To include_relevant_links. Default is true | [optional] [default to false]
 **inventoryCountRange** | **String**| Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **inTransit** | **String**| A boolean to filter in transit vehicles | [optional] 
 **seatingCapacity** | **String**| To filter on vehicle seating capacity | [optional] 
 **engineSizeRange** | **String**| Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2 | [optional] 
 **powertrainType** | **String**| To filter on powertrain_type | [optional] 
 **minPhotoLinks** | **String**| Filter listings based by number of photo links within given range | [optional] 
 **minPhotoLinksCached** | **String**| Filter listings based by number of cached photo links within given range | [optional] 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getListing

> Listing getListing(id, opts)

Listing by id

Get a particular dealer listing by its id

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarSearchApi();
let id = "id_example"; // String | Listing id to get all the listing attributes
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'appendApiKey': true, // Boolean | Flag on whether to include api_key in response API urls (if any)
  'includeRelevantLinks': false // Boolean | To include_relevant_links. Default is true
};
apiInstance.getListing(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Listing id to get all the listing attributes | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true]
 **includeRelevantLinks** | **Boolean**| To include_relevant_links. Default is true | [optional] [default to false]

### Return type

[**Listing**](Listing.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listingCarAuctionIdExtraGet

> ListingExtraAttributes listingCarAuctionIdExtraGet(id, opts)

Long text Listings attributes for Listing with the given id

Get listing options, features, seller comments

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarSearchApi();
let id = "id_example"; // String | Listing id to get all the listing attributes
let opts = {
  'apiKey': "apiKey_example" // String | The API Authentication Key. Mandatory with all API calls.
};
apiInstance.listingCarAuctionIdExtraGet(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Listing id to get all the listing attributes | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**ListingExtraAttributes**](ListingExtraAttributes.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listingCarAuctionIdGet

> Listing listingCarAuctionIdGet(id, opts)

Listing by id

Get a particular auction listing by its id

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarSearchApi();
let id = "id_example"; // String | Listing id to get all the listing attributes
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'appendApiKey': true, // Boolean | Flag on whether to include api_key in response API urls (if any)
  'includeRelevantLinks': false // Boolean | To include_relevant_links. Default is true
};
apiInstance.listingCarAuctionIdGet(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Listing id to get all the listing attributes | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true]
 **includeRelevantLinks** | **Boolean**| To include_relevant_links. Default is true | [optional] [default to false]

### Return type

[**Listing**](Listing.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listingCarAuctionIdMediaGet

> ListingMedia listingCarAuctionIdMediaGet(id, opts)

Listing media by id

Get listing media (photo, photos) by id

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarSearchApi();
let id = "id_example"; // String | Listing id to get all the listing attributes
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'appendApiKey': true // Boolean | Flag on whether to include api_key in response API urls (if any)
};
apiInstance.listingCarAuctionIdMediaGet(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Listing id to get all the listing attributes | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true]

### Return type

[**ListingMedia**](ListingMedia.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listingCarFsboIdExtraGet

> ListingExtraAttributes listingCarFsboIdExtraGet(id, opts)

Long text Listings attributes for Listing with the given id

Get listing options, features, seller comments

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarSearchApi();
let id = "id_example"; // String | Listing id to get all the listing attributes
let opts = {
  'apiKey': "apiKey_example" // String | The API Authentication Key. Mandatory with all API calls.
};
apiInstance.listingCarFsboIdExtraGet(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Listing id to get all the listing attributes | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**ListingExtraAttributes**](ListingExtraAttributes.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listingCarFsboIdGet

> Listing listingCarFsboIdGet(id, opts)

Listing by id

Get a particular private party listing by its id

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarSearchApi();
let id = "id_example"; // String | Listing id to get all the listing attributes
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'appendApiKey': true, // Boolean | Flag on whether to include api_key in response API urls (if any)
  'includeRelevantLinks': false // Boolean | To include_relevant_links. Default is true
};
apiInstance.listingCarFsboIdGet(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Listing id to get all the listing attributes | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true]
 **includeRelevantLinks** | **Boolean**| To include_relevant_links. Default is true | [optional] [default to false]

### Return type

[**Listing**](Listing.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listingCarFsboIdMediaGet

> ListingMedia listingCarFsboIdMediaGet(id, opts)

Listing media by id

Get listing media (photo, photos) by id

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarSearchApi();
let id = "id_example"; // String | Listing id to get all the listing attributes
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'appendApiKey': true // Boolean | Flag on whether to include api_key in response API urls (if any)
};
apiInstance.listingCarFsboIdMediaGet(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Listing id to get all the listing attributes | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true]

### Return type

[**ListingMedia**](ListingMedia.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listingCarIdExtraGet

> ListingExtraAttributes listingCarIdExtraGet(id, opts)

Long text Listings attributes for Listing with the given id

Get listing options, features, seller comments

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarSearchApi();
let id = "id_example"; // String | Listing id to get all the listing attributes
let opts = {
  'apiKey': "apiKey_example" // String | The API Authentication Key. Mandatory with all API calls.
};
apiInstance.listingCarIdExtraGet(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Listing id to get all the listing attributes | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**ListingExtraAttributes**](ListingExtraAttributes.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listingCarIdMediaGet

> ListingMedia listingCarIdMediaGet(id, opts)

Listing media by id

Get listing media (photo, photos) by id

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarSearchApi();
let id = "id_example"; // String | Listing id to get all the listing attributes
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'appendApiKey': true // Boolean | Flag on whether to include api_key in response API urls (if any)
};
apiInstance.listingCarIdMediaGet(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Listing id to get all the listing attributes | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true]

### Return type

[**ListingMedia**](ListingMedia.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listingCarUkIdExtraGet

> ListingExtraAttributes listingCarUkIdExtraGet(id, opts)

Long text Listings attributes for Listing with the given id

Get listing options, features, seller comments

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarSearchApi();
let id = "id_example"; // String | Listing id to get all the listing attributes
let opts = {
  'apiKey': "apiKey_example" // String | The API Authentication Key. Mandatory with all API calls.
};
apiInstance.listingCarUkIdExtraGet(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Listing id to get all the listing attributes | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**ListingExtraAttributes**](ListingExtraAttributes.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listingCarUkIdGet

> Listing listingCarUkIdGet(id, opts)

Listing by id

Get a particular dealer listing by its id

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarSearchApi();
let id = "id_example"; // String | Listing id to get all the listing attributes
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'appendApiKey': true // Boolean | Flag on whether to include api_key in response API urls (if any)
};
apiInstance.listingCarUkIdGet(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Listing id to get all the listing attributes | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true]

### Return type

[**Listing**](Listing.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listingCarUkIdMediaGet

> ListingMedia listingCarUkIdMediaGet(id, opts)

Listing media by id

Get listing media (photo, photos) by id

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarSearchApi();
let id = "id_example"; // String | Listing id to get all the listing attributes
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'appendApiKey': true // Boolean | Flag on whether to include api_key in response API urls (if any)
};
apiInstance.listingCarUkIdMediaGet(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Listing id to get all the listing attributes | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true]

### Return type

[**ListingMedia**](ListingMedia.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## search

> UKSearchResponse search(opts)

Gets active car listings in UK for the given search criteria

Search cars for sale in UK

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarSearchApi();
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'appendApiKey': false, // Boolean | Flag on whether to include api_key in response API urls (if any)
  'latitude': 3.4, // Number | Latitude component of location
  'longitude': 3.4, // Number | Longitude component of location
  'radius': 56, // Number | Radius around the search location (Unit - Miles)
  'postalCode': "postalCode_example", // String | To filter listing on postal code around which they are listed
  'zip': "zip_example", // String | To filter listing on ZIP around which they are listed
  'carType': "carType_example", // String | Car type. Allowed values are - new / used
  'year': "year_example", // String | To filter listing on their year
  'yearRange': "yearRange_example", // String | Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
  'make': "make_example", // String | To filter listings on their make
  'model': "model_example", // String | To filter listings on their model
  'variant': "variant_example", // String | To filter listing on their variant
  'trim': "trim_example", // String | To filter listing on their trim
  'bodyType': "bodyType_example", // String | To filter listing on their body type
  'ymmt': "ymmt_example", // String | Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe '|' character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - 'year|make||' or 'year|make|model' or '|make|model|' combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the 'vins' or 'taxonomy_vins' parameter to the search api instead the year|make|model|trim combinations.
  'transmission': "transmission_example", // String | To filter listing on their transmission
  'doors': "doors_example", // String | Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
  'drivetrain': "drivetrain_example", // String | To filter listing on their drivetrain
  'exteriorColor': "exteriorColor_example", // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
  'interiorColor': "interiorColor_example", // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
  'engine': "engine_example", // String | To filter listing on their engine
  'milesRange': "milesRange_example", // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
  'priceRange': "priceRange_example", // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'msrpRange': "msrpRange_example", // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'sortBy': "sortBy_example", // String | Sort by field. Default sort field is distance from the given point
  'sortOrder': "sortOrder_example", // String | Sort order - asc or desc. Default sort order is asc
  'rows': 10, // Number | Number of results to return. Default is 10. Max is 50
  'start': 0, // Number | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
  'msaCode': "msaCode_example", // String | To filter listing on msa code in which they are listed
  'facets': "facets_example", // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
  'rangeFacets': "rangeFacets_example", // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
  'facetSort': "'count'", // String | Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
  'stats': "stats_example", // String | The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
  'country': "'uk'", // String | To filter listing on Country in which they are listed
  'plot': true, // Boolean | If plot has value true results in around 25k coordinates with limited fields to plot respective graph
  'nodedup': true, // Boolean | If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
  'dedup': true, // Boolean | If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
  'county': "county_example", // String | To filter listing on county in which they are listed
  'state': "state_example", // String | To filter listing on State in which they are listed
  'city': "city_example", // String | To filter listing on City in which they are listed
  'fuelType': "fuelType_example", // String | To filter listing on their fuel type
  'stockNo': "stockNo_example", // String | To filter listing on their stock number on lot
  'domRange': "domRange_example", // String | Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'domActiveRange': "domActiveRange_example", // String | Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'dom180Range': "dom180Range_example", // String | Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'lastSeenRange': "lastSeenRange_example", // String | Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenRange': "firstSeenRange_example", // String | First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenAtSourceRange': "firstSeenAtSourceRange_example", // String | First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenAtMcRange': "firstSeenAtMcRange_example", // String | First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'lastSeenDays': "lastSeenDays_example", // String | Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenDays': "firstSeenDays_example", // String | First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenAtSourceDays': "firstSeenAtSourceDays_example", // String | First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenAtMcDays': "firstSeenAtMcDays_example", // String | First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
  'co2Emissions': "co2Emissions_example", // String | CO2 emissions
  'insuranceGroup': "insuranceGroup_example", // String | Insurance Group
  'vehicleRegistrationMark': "vehicleRegistrationMark_example", // String | Vehicle Registration Mark
  'vehicleRegistrationDateRange': "vehicleRegistrationDateRange_example", // String | Vehicle registration date range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'numOwners': "numOwners_example", // String | Number of owners. Range to be given in the format - min-max e.g. 1000-5000
  'inventoryCountRange': "inventoryCountRange_example", // String | Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50
  'source': "source_example", // String | To filter listing on their source only for widget requests
  'dealerId': "dealerId_example", // String | Dealer id to filter the listings.
  'excludeSources': "excludeSources_example", // String | A list of sources to exclude from result
  'excludeDealerIds': "excludeDealerIds_example", // String | A list of dealer ids to exclude from result
  'inTransit': "inTransit_example", // String | A boolean to filter in transit vehicles
  'includeNonVinListings': false, // Boolean | To include non vin listings. Default is false
  'cylinders': "cylinders_example", // String | To filter listing on their cylinders
  'photoLinks': true, // Boolean | A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don't have them
  'photoLinksCached': true, // Boolean | A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don't have them
  'baseExteriorColor': "baseExteriorColor_example", // String | Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
  'baseInteriorColor': "baseInteriorColor_example", // String | Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
  'writeOffCategory': "writeOffCategory_example", // String | write off category
  'excludeWriteOffCategory': "excludeWriteOffCategory_example", // String | To exclude write off category
  'fcaStatus': "fcaStatus_example", // String | To filter on fca status
  'seatingCapacity': "seatingCapacity_example", // String | To filter on vehicle seating capacity
  'vrm': "vrm_example", // String | To filter on vrm
  'powertrainType': "powertrainType_example", // String | To filter on powertrain_type
  'clientFilters': true, // Boolean | Flag to add explicit filters set on client level in solr
  'boost': true, // Boolean | Flag to sort listings based on client filter score in solr
  'carLocationSellerName': "carLocationSellerName_example", // String | Filter cars on seller name
  'carLocationStreet': "carLocationStreet_example", // String | Filter cars on street name
  'carLocationCity': "carLocationCity_example", // String | Filter cars on city
  'carLocationCounty': "carLocationCounty_example", // String | Filter cars on county
  'carLocationZip': "carLocationZip_example", // String | To filter listing on car ZIP around which they are listed
  'carLocationLatitude': 3.4, // Number | Latitude component of car location
  'carLocationLongitude': 3.4, // Number | Longitude component of car location
  'priceChange': "priceChange_example", // String | Query to filter listings based on their positive and negative price change
  'priceChangeRange': "priceChangeRange_example", // String | Price change range to filter listings with price change within given price_change_range. Range to be given in the format - min-max e.g. 10-500
  'activeInventoryDateRange': "activeInventoryDateRange_example", // String | date range to filter listings that were active within given date range. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'engineSize': "engineSize_example", // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
  'engineSizeRange': "engineSizeRange_example", // String | Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
  'uvcId': "uvcId_example", // String | To filter on uvc id
  'highwayMpgRange': "highwayMpgRange_example", // String | Highway mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'cityMpgRange': "cityMpgRange_example", // String | City mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'combinedMpgRange': "combinedMpgRange_example", // String | Combined mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'owned': true, // Boolean | Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
  'minPhotoLinks': "minPhotoLinks_example", // String | Filter listings based by number of photo links within given range
  'minPhotoLinksCached': "minPhotoLinksCached_example", // String | Filter listings based by number of cached photo links within given range
  'match': "match_example", // String | Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
  'ulezCompliant': true // Boolean | Filter listings based on drive into ultra low emmition zone
};
apiInstance.search(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to false]
 **latitude** | **Number**| Latitude component of location | [optional] 
 **longitude** | **Number**| Longitude component of location | [optional] 
 **radius** | **Number**| Radius around the search location (Unit - Miles) | [optional] 
 **postalCode** | **String**| To filter listing on postal code around which they are listed | [optional] 
 **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] 
 **carType** | **String**| Car type. Allowed values are - new / used | [optional] 
 **year** | **String**| To filter listing on their year | [optional] 
 **yearRange** | **String**| Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021 | [optional] 
 **make** | **String**| To filter listings on their make | [optional] 
 **model** | **String**| To filter listings on their model | [optional] 
 **variant** | **String**| To filter listing on their variant | [optional] 
 **trim** | **String**| To filter listing on their trim | [optional] 
 **bodyType** | **String**| To filter listing on their body type | [optional] 
 **ymmt** | **String**| Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations. | [optional] 
 **transmission** | **String**| To filter listing on their transmission | [optional] 
 **doors** | **String**| Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated | [optional] 
 **drivetrain** | **String**| To filter listing on their drivetrain | [optional] 
 **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] 
 **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] 
 **engine** | **String**| To filter listing on their engine | [optional] 
 **milesRange** | **String**| Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **priceRange** | **String**| Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **msrpRange** | **String**| MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] 
 **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] 
 **rows** | **Number**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10]
 **start** | **Number**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0]
 **msaCode** | **String**| To filter listing on msa code in which they are listed | [optional] 
 **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] 
 **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] 
 **facetSort** | **String**| Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param | [optional] [default to &#39;count&#39;]
 **stats** | **String**| The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. | [optional] 
 **country** | **String**| To filter listing on Country in which they are listed | [optional] [default to &#39;uk&#39;]
 **plot** | **Boolean**| If plot has value true results in around 25k coordinates with limited fields to plot respective graph | [optional] 
 **nodedup** | **Boolean**| If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin | [optional] 
 **dedup** | **Boolean**| If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source | [optional] 
 **county** | **String**| To filter listing on county in which they are listed | [optional] 
 **state** | **String**| To filter listing on State in which they are listed | [optional] 
 **city** | **String**| To filter listing on City in which they are listed | [optional] 
 **fuelType** | **String**| To filter listing on their fuel type | [optional] 
 **stockNo** | **String**| To filter listing on their stock number on lot | [optional] 
 **domRange** | **String**| Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **domActiveRange** | **String**| Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **dom180Range** | **String**| Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **lastSeenRange** | **String**| Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenRange** | **String**| First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenAtSourceRange** | **String**| First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenAtMcRange** | **String**| First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **lastSeenDays** | **String**| Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenDays** | **String**| First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenAtSourceDays** | **String**| First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenAtMcDays** | **String**| First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **co2Emissions** | **String**| CO2 emissions | [optional] 
 **insuranceGroup** | **String**| Insurance Group | [optional] 
 **vehicleRegistrationMark** | **String**| Vehicle Registration Mark | [optional] 
 **vehicleRegistrationDateRange** | **String**| Vehicle registration date range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **numOwners** | **String**| Number of owners. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **inventoryCountRange** | **String**| Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **source** | **String**| To filter listing on their source only for widget requests | [optional] 
 **dealerId** | **String**| Dealer id to filter the listings. | [optional] 
 **excludeSources** | **String**| A list of sources to exclude from result | [optional] 
 **excludeDealerIds** | **String**| A list of dealer ids to exclude from result | [optional] 
 **inTransit** | **String**| A boolean to filter in transit vehicles | [optional] 
 **includeNonVinListings** | **Boolean**| To include non vin listings. Default is false | [optional] [default to false]
 **cylinders** | **String**| To filter listing on their cylinders | [optional] 
 **photoLinks** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them | [optional] 
 **photoLinksCached** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them | [optional] 
 **baseExteriorColor** | **String**| Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated | [optional] 
 **baseInteriorColor** | **String**| Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated | [optional] 
 **writeOffCategory** | **String**| write off category | [optional] 
 **excludeWriteOffCategory** | **String**| To exclude write off category | [optional] 
 **fcaStatus** | **String**| To filter on fca status | [optional] 
 **seatingCapacity** | **String**| To filter on vehicle seating capacity | [optional] 
 **vrm** | **String**| To filter on vrm | [optional] 
 **powertrainType** | **String**| To filter on powertrain_type | [optional] 
 **clientFilters** | **Boolean**| Flag to add explicit filters set on client level in solr | [optional] [default to true]
 **boost** | **Boolean**| Flag to sort listings based on client filter score in solr | [optional] [default to true]
 **carLocationSellerName** | **String**| Filter cars on seller name | [optional] 
 **carLocationStreet** | **String**| Filter cars on street name | [optional] 
 **carLocationCity** | **String**| Filter cars on city | [optional] 
 **carLocationCounty** | **String**| Filter cars on county | [optional] 
 **carLocationZip** | **String**| To filter listing on car ZIP around which they are listed | [optional] 
 **carLocationLatitude** | **Number**| Latitude component of car location | [optional] 
 **carLocationLongitude** | **Number**| Longitude component of car location | [optional] 
 **priceChange** | **String**| Query to filter listings based on their positive and negative price change | [optional] 
 **priceChangeRange** | **String**| Price change range to filter listings with price change within given price_change_range. Range to be given in the format - min-max e.g. 10-500 | [optional] 
 **activeInventoryDateRange** | **String**| date range to filter listings that were active within given date range. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] 
 **engineSizeRange** | **String**| Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2 | [optional] 
 **uvcId** | **String**| To filter on uvc id | [optional] 
 **highwayMpgRange** | **String**| Highway mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **cityMpgRange** | **String**| City mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **combinedMpgRange** | **String**| Combined mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **owned** | **Boolean**| Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself | [optional] 
 **minPhotoLinks** | **String**| Filter listings based by number of photo links within given range | [optional] 
 **minPhotoLinksCached** | **String**| Filter listings based by number of cached photo links within given range | [optional] 
 **match** | **String**| Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match | [optional] 
 **ulezCompliant** | **Boolean**| Filter listings based on drive into ultra low emmition zone | [optional] 

### Return type

[**UKSearchResponse**](UKSearchResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchCarActiveGet

> SearchResponse searchCarActiveGet(opts)

Gets active car listings for the given search criteria

This endpoint is the meat of the API and serves many purposes. This API produces a list of currently active cars from the market for the given search criteria. The API results are limited to allow pagination upto 10000 rows.   The search API facilitates the following use cases -  1. Search Cars around a given geo-point within a given radius  2. Search cars for a specific year / make / model or combination of these  3. Search cars matching multiple year, make, model combinatins in the same search request 4. Filter results by most car specification attributes 5. Search for similar cars by VIN or Taxonomy VIN  6. Filter cars within a given price / miles / days on market (dom) range 7. Specify a sort order for the results on price / miles / dom / listed date  8. Search cars for a given City / State combination  9. Get Facets to build the search drill downs  10. Get Market averages for price/miles/dom for your search

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarSearchApi();
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'appendApiKey': true, // Boolean | Flag on whether to include api_key in response API urls (if any)
  'latitude': 3.4, // Number | Latitude component of location
  'longitude': 3.4, // Number | Longitude component of location
  'radius': 56, // Number | Radius around the search location (Unit - Miles)
  'zip': "zip_example", // String | To filter listing on ZIP around which they are listed
  'includeLease': true, // Boolean | Boolean param to search for listings that include leasing options in them
  'includeFinance': true, // Boolean | Boolean param to search for listings that include finance options in them
  'leaseTerm': "leaseTerm_example", // String | Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term=30-60
  'leaseDownPayment': "leaseDownPayment_example", // String | Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment=30-60
  'leaseEmp': "leaseEmp_example", // String | Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp=30-60
  'financeLoanTerm': "financeLoanTerm_example", // String | Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term=30-60
  'financeLoanApr': "financeLoanApr_example", // String | Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr=30-60
  'financeEmp': "financeEmp_example", // String | Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp=30-60
  'financeDownPayment': "financeDownPayment_example", // String | Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment=30-60
  'financeDownPaymentPer': "financeDownPaymentPer_example", // String | Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per=30-60
  'carType': "carType_example", // String | Car type. Allowed values are - new / used / certified
  'carfax1Owner': "carfax1Owner_example", // String | Indicates whether car has had only one owner or not
  'carfaxCleanTitle': "carfaxCleanTitle_example", // String | Indicates whether car has clean ownership records
  'yearRange': "yearRange_example", // String | Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
  'year': "year_example", // String | To filter listing on their year
  'make': "make_example", // String | To filter listings on their make
  'model': "model_example", // String | To filter listings on their model
  'trim': "trim_example", // String | To filter listing on their trim
  'vin': "vin_example", // String | To filter listing on their VIN
  'bodyType': "bodyType_example", // String | To filter listing on their body type
  'bodySubtype': "bodySubtype_example", // String | Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
  'vehicleType': "vehicleType_example", // String | To filter listing on their vehicle type
  'vins': "vins_example", // String | Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc
  'taxonomyVins': "taxonomyVins_example", // String | Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API.
  'mm': "mm_example", // String | Make-Model concatenated string. To help passing the results of auto-complete API on mm field, use this parameter and pass in the selected value as is
  'ymm': "ymm_example", // String | Year-Make-Model concatenated string. To help passing the results of auto-complete API on ymm field, use this parameter and pass in the selected value as is
  'ymmt': "ymmt_example", // String | Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe '|' character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - 'year|make||' or 'year|make|model' or '|make|model|' combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the 'vins' or 'taxonomy_vins' parameter to the search api instead the year|make|model|trim combinations.
  'match': "match_example", // String | Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
  'cylinders': "cylinders_example", // String | To filter listing on their cylinders
  'transmission': "transmission_example", // String | To filter listing on their transmission
  'doors': "doors_example", // String | Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
  'drivetrain': "drivetrain_example", // String | To filter listing on their drivetrain
  'exteriorColor': "exteriorColor_example", // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
  'interiorColor': "interiorColor_example", // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
  'baseExteriorColor': "baseExteriorColor_example", // String | Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
  'baseInteriorColor': "baseInteriorColor_example", // String | Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
  'engine': "engine_example", // String | To filter listing on their engine
  'engineSize': "engineSize_example", // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
  'engineAspiration': "engineAspiration_example", // String | Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
  'engineBlock': "engineBlock_example", // String | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
  'highwayMpgRange': "highwayMpgRange_example", // String | Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'cityMpgRange': "cityMpgRange_example", // String | City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'milesRange': "milesRange_example", // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
  'priceRange': "priceRange_example", // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'msrpRange': "msrpRange_example", // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'domRange': "domRange_example", // String | Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'sortBy': "sortBy_example", // String | Sort by field. Default sort field is distance from the given point
  'sortOrder': "sortOrder_example", // String | Sort order - asc or desc. Default sort order is asc
  'rows': 10, // Number | Number of results to return. Default is 10. Max is 50
  'start': 0, // Number | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
  'includeNonVinListings': false, // Boolean | To include non vin listings. Default is false
  'msaCode': "msaCode_example", // String | To filter listing on msa code in which they are listed
  'facets': "facets_example", // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
  'rangeFacets': "rangeFacets_example", // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
  'facetSort': "'count'", // String | Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
  'stats': "stats_example", // String | The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
  'country': "'US'", // String | To filter listing on Country in which they are listed
  'plot': true, // Boolean | If plot has value true results in around 25k coordinates with limited fields to plot respective graph
  'nodedup': true, // Boolean | If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
  'dedup': true, // Boolean | If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
  'owned': true, // Boolean | Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
  'source': "source_example", // String | To filter listing on their source only for widget requests
  'state': "state_example", // String | To filter listing on State in which they are listed
  'city': "city_example", // String | To filter listing on City in which they are listed
  'trimO': "trimO_example", // String | Filter listings on web scraped trim
  'trimR': "trimR_example", // String | Filter trim on custom possible matches
  'domActiveRange': "domActiveRange_example", // String | Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'dom180Range': "dom180Range_example", // String | Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'excludeCertified': true, // Boolean | Boolean param to exclude certified cars from search results
  'fuelType': "fuelType_example", // String | To filter listing on their fuel type
  'dealerType': "dealerType_example", // String | Filter based on dealer type independant or franchise
  'photoLinks': true, // Boolean | A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don't have them
  'photoLinksCached': true, // Boolean | A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don't have them
  'stockNo': "stockNo_example", // String | To filter listing on their stock number on lot
  'lastSeenRange': "lastSeenRange_example", // String | Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenRange': "firstSeenRange_example", // String | First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenAtSourceRange': "firstSeenAtSourceRange_example", // String | First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenAtMcRange': "firstSeenAtMcRange_example", // String | First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'lastSeenDays': "lastSeenDays_example", // String | Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenDays': "firstSeenDays_example", // String | First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenAtSourceDays': "firstSeenAtSourceDays_example", // String | First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenAtMcDays': "firstSeenAtMcDays_example", // String | First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
  'includeRelevantLinks': false, // Boolean | To include_relevant_links. Default is true
  'inventoryCountRange': "inventoryCountRange_example", // String | Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50
  'dealerId': "dealerId_example", // String | Dealer id to filter the listings.
  'excludeDealerIds': "excludeDealerIds_example", // String | A list of dealer ids to exclude from result
  'excludeSources': "excludeSources_example", // String | A list of sources to exclude from result
  'inTransit': "inTransit_example", // String | A boolean to filter in transit vehicles
  'seatingCapacity': "seatingCapacity_example", // String | To filter on vehicle seating capacity
  'powertrainType': "powertrainType_example", // String | To filter on powertrain_type
  'priceChange': "priceChange_example", // String | Query to filter listings based on their positive and negative price change
  'priceChangeRange': "priceChangeRange_example", // String | Price change range to filter listings with price change within given price_change_range. Range to be given in the format - min-max e.g. 10-500
  'activeInventoryDateRange': "activeInventoryDateRange_example", // String | date range to filter listings that were active within given date range. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'engineSizeRange': "engineSizeRange_example", // String | Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
  'highValueFeatures': "highValueFeatures_example", // String | To filter listings on their high_value_features. Results will be intersection of provided HVFs
  'minPhotoLinks': "minPhotoLinks_example", // String | Filter listings based by number of photo links within given range
  'minPhotoLinksCached': "minPhotoLinksCached_example", // String | Filter listings based by number of cached photo links within given range
  'clientFilters': true // Boolean | Flag to add explicit filters set on client level in solr
};
apiInstance.searchCarActiveGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true]
 **latitude** | **Number**| Latitude component of location | [optional] 
 **longitude** | **Number**| Longitude component of location | [optional] 
 **radius** | **Number**| Radius around the search location (Unit - Miles) | [optional] 
 **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] 
 **includeLease** | **Boolean**| Boolean param to search for listings that include leasing options in them | [optional] 
 **includeFinance** | **Boolean**| Boolean param to search for listings that include finance options in them | [optional] 
 **leaseTerm** | **String**| Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60 | [optional] 
 **leaseDownPayment** | **String**| Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60 | [optional] 
 **leaseEmp** | **String**| Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60 | [optional] 
 **financeLoanTerm** | **String**| Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60 | [optional] 
 **financeLoanApr** | **String**| Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60 | [optional] 
 **financeEmp** | **String**| Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60 | [optional] 
 **financeDownPayment** | **String**| Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60 | [optional] 
 **financeDownPaymentPer** | **String**| Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60 | [optional] 
 **carType** | **String**| Car type. Allowed values are - new / used / certified | [optional] 
 **carfax1Owner** | **String**| Indicates whether car has had only one owner or not | [optional] 
 **carfaxCleanTitle** | **String**| Indicates whether car has clean ownership records | [optional] 
 **yearRange** | **String**| Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021 | [optional] 
 **year** | **String**| To filter listing on their year | [optional] 
 **make** | **String**| To filter listings on their make | [optional] 
 **model** | **String**| To filter listings on their model | [optional] 
 **trim** | **String**| To filter listing on their trim | [optional] 
 **vin** | **String**| To filter listing on their VIN | [optional] 
 **bodyType** | **String**| To filter listing on their body type | [optional] 
 **bodySubtype** | **String**| Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] 
 **vehicleType** | **String**| To filter listing on their vehicle type | [optional] 
 **vins** | **String**| Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc | [optional] 
 **taxonomyVins** | **String**| Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API. | [optional] 
 **mm** | **String**| Make-Model concatenated string. To help passing the results of auto-complete API on mm field, use this parameter and pass in the selected value as is | [optional] 
 **ymm** | **String**| Year-Make-Model concatenated string. To help passing the results of auto-complete API on ymm field, use this parameter and pass in the selected value as is | [optional] 
 **ymmt** | **String**| Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations. | [optional] 
 **match** | **String**| Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match | [optional] 
 **cylinders** | **String**| To filter listing on their cylinders | [optional] 
 **transmission** | **String**| To filter listing on their transmission | [optional] 
 **doors** | **String**| Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated | [optional] 
 **drivetrain** | **String**| To filter listing on their drivetrain | [optional] 
 **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] 
 **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] 
 **baseExteriorColor** | **String**| Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated | [optional] 
 **baseInteriorColor** | **String**| Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated | [optional] 
 **engine** | **String**| To filter listing on their engine | [optional] 
 **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] 
 **engineAspiration** | **String**| Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated | [optional] 
 **engineBlock** | **String**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] 
 **highwayMpgRange** | **String**| Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **cityMpgRange** | **String**| City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **milesRange** | **String**| Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **priceRange** | **String**| Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **msrpRange** | **String**| MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **domRange** | **String**| Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] 
 **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] 
 **rows** | **Number**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10]
 **start** | **Number**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0]
 **includeNonVinListings** | **Boolean**| To include non vin listings. Default is false | [optional] [default to false]
 **msaCode** | **String**| To filter listing on msa code in which they are listed | [optional] 
 **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] 
 **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] 
 **facetSort** | **String**| Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param | [optional] [default to &#39;count&#39;]
 **stats** | **String**| The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. | [optional] 
 **country** | **String**| To filter listing on Country in which they are listed | [optional] [default to &#39;US&#39;]
 **plot** | **Boolean**| If plot has value true results in around 25k coordinates with limited fields to plot respective graph | [optional] 
 **nodedup** | **Boolean**| If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin | [optional] 
 **dedup** | **Boolean**| If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source | [optional] 
 **owned** | **Boolean**| Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself | [optional] 
 **source** | **String**| To filter listing on their source only for widget requests | [optional] 
 **state** | **String**| To filter listing on State in which they are listed | [optional] 
 **city** | **String**| To filter listing on City in which they are listed | [optional] 
 **trimO** | **String**| Filter listings on web scraped trim | [optional] 
 **trimR** | **String**| Filter trim on custom possible matches | [optional] 
 **domActiveRange** | **String**| Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **dom180Range** | **String**| Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **excludeCertified** | **Boolean**| Boolean param to exclude certified cars from search results | [optional] 
 **fuelType** | **String**| To filter listing on their fuel type | [optional] 
 **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] 
 **photoLinks** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them | [optional] 
 **photoLinksCached** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them | [optional] 
 **stockNo** | **String**| To filter listing on their stock number on lot | [optional] 
 **lastSeenRange** | **String**| Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenRange** | **String**| First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenAtSourceRange** | **String**| First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenAtMcRange** | **String**| First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **lastSeenDays** | **String**| Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenDays** | **String**| First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenAtSourceDays** | **String**| First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenAtMcDays** | **String**| First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **includeRelevantLinks** | **Boolean**| To include_relevant_links. Default is true | [optional] [default to false]
 **inventoryCountRange** | **String**| Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **dealerId** | **String**| Dealer id to filter the listings. | [optional] 
 **excludeDealerIds** | **String**| A list of dealer ids to exclude from result | [optional] 
 **excludeSources** | **String**| A list of sources to exclude from result | [optional] 
 **inTransit** | **String**| A boolean to filter in transit vehicles | [optional] 
 **seatingCapacity** | **String**| To filter on vehicle seating capacity | [optional] 
 **powertrainType** | **String**| To filter on powertrain_type | [optional] 
 **priceChange** | **String**| Query to filter listings based on their positive and negative price change | [optional] 
 **priceChangeRange** | **String**| Price change range to filter listings with price change within given price_change_range. Range to be given in the format - min-max e.g. 10-500 | [optional] 
 **activeInventoryDateRange** | **String**| date range to filter listings that were active within given date range. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **engineSizeRange** | **String**| Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2 | [optional] 
 **highValueFeatures** | **String**| To filter listings on their high_value_features. Results will be intersection of provided HVFs | [optional] 
 **minPhotoLinks** | **String**| Filter listings based by number of photo links within given range | [optional] 
 **minPhotoLinksCached** | **String**| Filter listings based by number of cached photo links within given range | [optional] 
 **clientFilters** | **Boolean**| Flag to add explicit filters set on client level in solr | [optional] [default to true]

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchCarAuctionActiveGet

> SearchResponse searchCarAuctionActiveGet(opts)

Gets active auction car listings for the given search criteria

This API produces a list of currently active auction cars from the market for the given search criteria. The API results are limited to allow pagination upto 5000 rows.   The search API facilitates the following use cases -  1. Search Cars around a given geo-point within a given radius  2. Search cars for a specific year / make / model or combination of these  3. Search cars matching multiple year, make, model combinatins in the same search request 4. Filter results by most car specification attributes 5. Search for similar cars by VIN or Taxonomy VIN  6. Filter cars within a given price / miles / days on market (dom) range 7. Specify a sort order for the results on price / miles / dom / listed date  8. Search cars for a given City / State combination  9. Get Facets to build the search drill downs  10. Get Market averages for price/miles/dom for your search

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarSearchApi();
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'appendApiKey': true, // Boolean | Flag on whether to include api_key in response API urls (if any)
  'latitude': 3.4, // Number | Latitude component of location
  'longitude': 3.4, // Number | Longitude component of location
  'radius': 56, // Number | Radius around the search location (Unit - Miles)
  'zip': "zip_example", // String | To filter listing on ZIP around which they are listed
  'includeLease': true, // Boolean | Boolean param to search for listings that include leasing options in them
  'includeFinance': true, // Boolean | Boolean param to search for listings that include finance options in them
  'leaseTerm': "leaseTerm_example", // String | Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term=30-60
  'leaseDownPayment': "leaseDownPayment_example", // String | Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment=30-60
  'leaseEmp': "leaseEmp_example", // String | Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp=30-60
  'financeLoanTerm': "financeLoanTerm_example", // String | Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term=30-60
  'financeLoanApr': "financeLoanApr_example", // String | Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr=30-60
  'financeEmp': "financeEmp_example", // String | Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp=30-60
  'financeDownPayment': "financeDownPayment_example", // String | Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment=30-60
  'financeDownPaymentPer': "financeDownPaymentPer_example", // String | Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per=30-60
  'carType': "carType_example", // String | Car type. Allowed values are - new / used / certified
  'carfax1Owner': "carfax1Owner_example", // String | Indicates whether car has had only one owner or not
  'carfaxCleanTitle': "carfaxCleanTitle_example", // String | Indicates whether car has clean ownership records
  'yearRange': "yearRange_example", // String | Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
  'year': "year_example", // String | To filter listing on their year
  'make': "make_example", // String | To filter listings on their make
  'model': "model_example", // String | To filter listings on their model
  'trim': "trim_example", // String | To filter listing on their trim
  'vin': "vin_example", // String | To filter listing on their VIN
  'bodyType': "bodyType_example", // String | To filter listing on their body type
  'bodySubtype': "bodySubtype_example", // String | Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
  'vehicleType': "vehicleType_example", // String | To filter listing on their vehicle type
  'vins': "vins_example", // String | Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc
  'taxonomyVins': "taxonomyVins_example", // String | Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API.
  'mm': "mm_example", // String | Make-Model concatenated string. To help passing the results of auto-complete API on mm field, use this parameter and pass in the selected value as is
  'ymm': "ymm_example", // String | Year-Make-Model concatenated string. To help passing the results of auto-complete API on ymm field, use this parameter and pass in the selected value as is
  'ymmt': "ymmt_example", // String | Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe '|' character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - 'year|make||' or 'year|make|model' or '|make|model|' combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the 'vins' or 'taxonomy_vins' parameter to the search api instead the year|make|model|trim combinations.
  'match': "match_example", // String | Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
  'cylinders': "cylinders_example", // String | To filter listing on their cylinders
  'transmission': "transmission_example", // String | To filter listing on their transmission
  'doors': "doors_example", // String | Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
  'drivetrain': "drivetrain_example", // String | To filter listing on their drivetrain
  'exteriorColor': "exteriorColor_example", // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
  'interiorColor': "interiorColor_example", // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
  'baseExteriorColor': "baseExteriorColor_example", // String | Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
  'baseInteriorColor': "baseInteriorColor_example", // String | Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
  'engine': "engine_example", // String | To filter listing on their engine
  'engineSize': "engineSize_example", // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
  'engineAspiration': "engineAspiration_example", // String | Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
  'engineBlock': "engineBlock_example", // String | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
  'highwayMpgRange': "highwayMpgRange_example", // String | Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'cityMpgRange': "cityMpgRange_example", // String | City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'milesRange': "milesRange_example", // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
  'priceRange': "priceRange_example", // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'msrpRange': "msrpRange_example", // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'domRange': "domRange_example", // String | Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'sortBy': "sortBy_example", // String | Sort by field. Default sort field is distance from the given point
  'sortOrder': "sortOrder_example", // String | Sort order - asc or desc. Default sort order is asc
  'rows': 10, // Number | Number of results to return. Default is 10. Max is 50
  'start': 0, // Number | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
  'includeNonVinListings': false, // Boolean | To include non vin listings. Default is false
  'msaCode': "msaCode_example", // String | To filter listing on msa code in which they are listed
  'facets': "facets_example", // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
  'rangeFacets': "rangeFacets_example", // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
  'facetSort': "'count'", // String | Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
  'stats': "stats_example", // String | The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
  'country': "'US'", // String | To filter listing on Country in which they are listed
  'plot': true, // Boolean | If plot has value true results in around 25k coordinates with limited fields to plot respective graph
  'nodedup': true, // Boolean | If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
  'dedup': true, // Boolean | If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
  'owned': true, // Boolean | Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
  'state': "state_example", // String | To filter listing on State in which they are listed
  'city': "city_example", // String | To filter listing on City in which they are listed
  'source': "source_example", // String | To filter listing on their source only for widget requests
  'dealerId': "dealerId_example", // String | Dealer id to filter the listings.
  'trimO': "trimO_example", // String | Filter listings on web scraped trim
  'trimR': "trimR_example", // String | Filter trim on custom possible matches
  'domActiveRange': "domActiveRange_example", // String | Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'dom180Range': "dom180Range_example", // String | Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'excludeCertified': true, // Boolean | Boolean param to exclude certified cars from search results
  'fuelType': "fuelType_example", // String | To filter listing on their fuel type
  'dealerType': "dealerType_example", // String | Filter based on dealer type independant or franchise
  'photoLinks': true, // Boolean | A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don't have them
  'photoLinksCached': true, // Boolean | A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don't have them
  'stockNo': "stockNo_example", // String | To filter listing on their stock number on lot
  'lastSeenRange': "lastSeenRange_example", // String | Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenRange': "firstSeenRange_example", // String | First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenAtSourceRange': "firstSeenAtSourceRange_example", // String | First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenAtMcRange': "firstSeenAtMcRange_example", // String | First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'lastSeenDays': "lastSeenDays_example", // String | Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenDays': "firstSeenDays_example", // String | First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenAtSourceDays': "firstSeenAtSourceDays_example", // String | First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenAtMcDays': "firstSeenAtMcDays_example", // String | First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
  'includeRelevantLinks': false, // Boolean | To include_relevant_links. Default is true
  'inventoryCountRange': "inventoryCountRange_example", // String | Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50
  'excludeDealerIds': "excludeDealerIds_example", // String | A list of dealer ids to exclude from result
  'excludeSources': "excludeSources_example", // String | A list of sources to exclude from result
  'inTransit': "inTransit_example", // String | A boolean to filter in transit vehicles
  'titleType': "titleType_example", // String | To filter on title type
  'seatingCapacity': "seatingCapacity_example", // String | To filter on vehicle seating capacity
  'engineSizeRange': "engineSizeRange_example", // String | Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
  'minPhotoLinks': "minPhotoLinks_example", // String | Filter listings based by number of photo links within given range
  'minPhotoLinksCached': "minPhotoLinksCached_example" // String | Filter listings based by number of cached photo links within given range
};
apiInstance.searchCarAuctionActiveGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true]
 **latitude** | **Number**| Latitude component of location | [optional] 
 **longitude** | **Number**| Longitude component of location | [optional] 
 **radius** | **Number**| Radius around the search location (Unit - Miles) | [optional] 
 **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] 
 **includeLease** | **Boolean**| Boolean param to search for listings that include leasing options in them | [optional] 
 **includeFinance** | **Boolean**| Boolean param to search for listings that include finance options in them | [optional] 
 **leaseTerm** | **String**| Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60 | [optional] 
 **leaseDownPayment** | **String**| Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60 | [optional] 
 **leaseEmp** | **String**| Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60 | [optional] 
 **financeLoanTerm** | **String**| Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60 | [optional] 
 **financeLoanApr** | **String**| Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60 | [optional] 
 **financeEmp** | **String**| Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60 | [optional] 
 **financeDownPayment** | **String**| Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60 | [optional] 
 **financeDownPaymentPer** | **String**| Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60 | [optional] 
 **carType** | **String**| Car type. Allowed values are - new / used / certified | [optional] 
 **carfax1Owner** | **String**| Indicates whether car has had only one owner or not | [optional] 
 **carfaxCleanTitle** | **String**| Indicates whether car has clean ownership records | [optional] 
 **yearRange** | **String**| Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021 | [optional] 
 **year** | **String**| To filter listing on their year | [optional] 
 **make** | **String**| To filter listings on their make | [optional] 
 **model** | **String**| To filter listings on their model | [optional] 
 **trim** | **String**| To filter listing on their trim | [optional] 
 **vin** | **String**| To filter listing on their VIN | [optional] 
 **bodyType** | **String**| To filter listing on their body type | [optional] 
 **bodySubtype** | **String**| Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] 
 **vehicleType** | **String**| To filter listing on their vehicle type | [optional] 
 **vins** | **String**| Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc | [optional] 
 **taxonomyVins** | **String**| Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API. | [optional] 
 **mm** | **String**| Make-Model concatenated string. To help passing the results of auto-complete API on mm field, use this parameter and pass in the selected value as is | [optional] 
 **ymm** | **String**| Year-Make-Model concatenated string. To help passing the results of auto-complete API on ymm field, use this parameter and pass in the selected value as is | [optional] 
 **ymmt** | **String**| Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations. | [optional] 
 **match** | **String**| Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match | [optional] 
 **cylinders** | **String**| To filter listing on their cylinders | [optional] 
 **transmission** | **String**| To filter listing on their transmission | [optional] 
 **doors** | **String**| Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated | [optional] 
 **drivetrain** | **String**| To filter listing on their drivetrain | [optional] 
 **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] 
 **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] 
 **baseExteriorColor** | **String**| Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated | [optional] 
 **baseInteriorColor** | **String**| Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated | [optional] 
 **engine** | **String**| To filter listing on their engine | [optional] 
 **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] 
 **engineAspiration** | **String**| Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated | [optional] 
 **engineBlock** | **String**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] 
 **highwayMpgRange** | **String**| Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **cityMpgRange** | **String**| City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **milesRange** | **String**| Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **priceRange** | **String**| Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **msrpRange** | **String**| MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **domRange** | **String**| Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] 
 **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] 
 **rows** | **Number**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10]
 **start** | **Number**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0]
 **includeNonVinListings** | **Boolean**| To include non vin listings. Default is false | [optional] [default to false]
 **msaCode** | **String**| To filter listing on msa code in which they are listed | [optional] 
 **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] 
 **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] 
 **facetSort** | **String**| Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param | [optional] [default to &#39;count&#39;]
 **stats** | **String**| The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. | [optional] 
 **country** | **String**| To filter listing on Country in which they are listed | [optional] [default to &#39;US&#39;]
 **plot** | **Boolean**| If plot has value true results in around 25k coordinates with limited fields to plot respective graph | [optional] 
 **nodedup** | **Boolean**| If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin | [optional] 
 **dedup** | **Boolean**| If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source | [optional] 
 **owned** | **Boolean**| Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself | [optional] 
 **state** | **String**| To filter listing on State in which they are listed | [optional] 
 **city** | **String**| To filter listing on City in which they are listed | [optional] 
 **source** | **String**| To filter listing on their source only for widget requests | [optional] 
 **dealerId** | **String**| Dealer id to filter the listings. | [optional] 
 **trimO** | **String**| Filter listings on web scraped trim | [optional] 
 **trimR** | **String**| Filter trim on custom possible matches | [optional] 
 **domActiveRange** | **String**| Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **dom180Range** | **String**| Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **excludeCertified** | **Boolean**| Boolean param to exclude certified cars from search results | [optional] 
 **fuelType** | **String**| To filter listing on their fuel type | [optional] 
 **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] 
 **photoLinks** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them | [optional] 
 **photoLinksCached** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them | [optional] 
 **stockNo** | **String**| To filter listing on their stock number on lot | [optional] 
 **lastSeenRange** | **String**| Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenRange** | **String**| First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenAtSourceRange** | **String**| First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenAtMcRange** | **String**| First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **lastSeenDays** | **String**| Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenDays** | **String**| First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenAtSourceDays** | **String**| First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenAtMcDays** | **String**| First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **includeRelevantLinks** | **Boolean**| To include_relevant_links. Default is true | [optional] [default to false]
 **inventoryCountRange** | **String**| Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **excludeDealerIds** | **String**| A list of dealer ids to exclude from result | [optional] 
 **excludeSources** | **String**| A list of sources to exclude from result | [optional] 
 **inTransit** | **String**| A boolean to filter in transit vehicles | [optional] 
 **titleType** | **String**| To filter on title type | [optional] 
 **seatingCapacity** | **String**| To filter on vehicle seating capacity | [optional] 
 **engineSizeRange** | **String**| Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2 | [optional] 
 **minPhotoLinks** | **String**| Filter listings based by number of photo links within given range | [optional] 
 **minPhotoLinksCached** | **String**| Filter listings based by number of cached photo links within given range | [optional] 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchCarFsboActiveGet

> SearchResponse searchCarFsboActiveGet(opts)

Gets active private party car listings for the given search criteria

This API produces a list of currently active FSBO cars from the market for the given search criteria. The API results are limited to allow pagination upto 5000 rows.   The search API facilitates the following use cases -  1. Search Cars around a given geo-point within a given radius  2. Search cars for a specific year / make / model or combination of these  3. Search cars matching multiple year, make, model combinatins in the same search request 4. Filter results by most car specification attributes 5. Search for similar cars by VIN or Taxonomy VIN  6. Filter cars within a given price / miles / days on market (dom) range 7. Specify a sort order for the results on price / miles / dom / listed date  8. Search cars for a given City / State combination  9. Get Facets to build the search drill downs  10. Get Market averages for price/miles/dom for your search

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarSearchApi();
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'appendApiKey': true, // Boolean | Flag on whether to include api_key in response API urls (if any)
  'latitude': 3.4, // Number | Latitude component of location
  'longitude': 3.4, // Number | Longitude component of location
  'radius': 56, // Number | Radius around the search location (Unit - Miles)
  'zip': "zip_example", // String | To filter listing on ZIP around which they are listed
  'includeLease': true, // Boolean | Boolean param to search for listings that include leasing options in them
  'includeFinance': true, // Boolean | Boolean param to search for listings that include finance options in them
  'leaseTerm': "leaseTerm_example", // String | Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term=30-60
  'leaseDownPayment': "leaseDownPayment_example", // String | Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment=30-60
  'leaseEmp': "leaseEmp_example", // String | Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp=30-60
  'financeLoanTerm': "financeLoanTerm_example", // String | Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term=30-60
  'financeLoanApr': "financeLoanApr_example", // String | Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr=30-60
  'financeEmp': "financeEmp_example", // String | Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp=30-60
  'financeDownPayment': "financeDownPayment_example", // String | Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment=30-60
  'financeDownPaymentPer': "financeDownPaymentPer_example", // String | Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per=30-60
  'carType': "carType_example", // String | Car type. Allowed values are - new / used / certified
  'carfax1Owner': "carfax1Owner_example", // String | Indicates whether car has had only one owner or not
  'carfaxCleanTitle': "carfaxCleanTitle_example", // String | Indicates whether car has clean ownership records
  'yearRange': "yearRange_example", // String | Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
  'year': "year_example", // String | To filter listing on their year
  'make': "make_example", // String | To filter listings on their make
  'model': "model_example", // String | To filter listings on their model
  'trim': "trim_example", // String | To filter listing on their trim
  'vin': "vin_example", // String | To filter listing on their VIN
  'bodyType': "bodyType_example", // String | To filter listing on their body type
  'bodySubtype': "bodySubtype_example", // String | Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
  'vehicleType': "vehicleType_example", // String | To filter listing on their vehicle type
  'vins': "vins_example", // String | Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc
  'taxonomyVins': "taxonomyVins_example", // String | Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API.
  'mm': "mm_example", // String | Make-Model concatenated string. To help passing the results of auto-complete API on mm field, use this parameter and pass in the selected value as is
  'ymm': "ymm_example", // String | Year-Make-Model concatenated string. To help passing the results of auto-complete API on ymm field, use this parameter and pass in the selected value as is
  'ymmt': "ymmt_example", // String | Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe '|' character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - 'year|make||' or 'year|make|model' or '|make|model|' combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the 'vins' or 'taxonomy_vins' parameter to the search api instead the year|make|model|trim combinations.
  'match': "match_example", // String | Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
  'cylinders': "cylinders_example", // String | To filter listing on their cylinders
  'transmission': "transmission_example", // String | To filter listing on their transmission
  'doors': "doors_example", // String | Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
  'drivetrain': "drivetrain_example", // String | To filter listing on their drivetrain
  'exteriorColor': "exteriorColor_example", // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
  'interiorColor': "interiorColor_example", // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
  'baseExteriorColor': "baseExteriorColor_example", // String | Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
  'baseInteriorColor': "baseInteriorColor_example", // String | Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
  'engine': "engine_example", // String | To filter listing on their engine
  'engineSize': "engineSize_example", // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
  'engineAspiration': "engineAspiration_example", // String | Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
  'engineBlock': "engineBlock_example", // String | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
  'highwayMpgRange': "highwayMpgRange_example", // String | Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'cityMpgRange': "cityMpgRange_example", // String | City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'milesRange': "milesRange_example", // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
  'priceRange': "priceRange_example", // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'msrpRange': "msrpRange_example", // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'domRange': "domRange_example", // String | Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'sortBy': "sortBy_example", // String | Sort by field. Default sort field is distance from the given point
  'sortOrder': "sortOrder_example", // String | Sort order - asc or desc. Default sort order is asc
  'rows': 10, // Number | Number of results to return. Default is 10. Max is 50
  'start': 0, // Number | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
  'includeNonVinListings': false, // Boolean | To include non vin listings. Default is false
  'msaCode': "msaCode_example", // String | To filter listing on msa code in which they are listed
  'facets': "facets_example", // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
  'rangeFacets': "rangeFacets_example", // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
  'facetSort': "'count'", // String | Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
  'stats': "stats_example", // String | The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
  'country': "'US'", // String | To filter listing on Country in which they are listed
  'plot': true, // Boolean | If plot has value true results in around 25k coordinates with limited fields to plot respective graph
  'nodedup': true, // Boolean | If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
  'dedup': true, // Boolean | If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
  'owned': true, // Boolean | Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
  'state': "state_example", // String | To filter listing on State in which they are listed
  'city': "city_example", // String | To filter listing on City in which they are listed
  'source': "source_example", // String | To filter listing on their source only for widget requests
  'dealerId': "dealerId_example", // String | Dealer id to filter the listings.
  'trimO': "trimO_example", // String | Filter listings on web scraped trim
  'trimR': "trimR_example", // String | Filter trim on custom possible matches
  'domActiveRange': "domActiveRange_example", // String | Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'dom180Range': "dom180Range_example", // String | Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'excludeCertified': true, // Boolean | Boolean param to exclude certified cars from search results
  'fuelType': "fuelType_example", // String | To filter listing on their fuel type
  'dealerType': "dealerType_example", // String | Filter based on dealer type independant or franchise
  'photoLinks': true, // Boolean | A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don't have them
  'photoLinksCached': true, // Boolean | A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don't have them
  'stockNo': "stockNo_example", // String | To filter listing on their stock number on lot
  'lastSeenRange': "lastSeenRange_example", // String | Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenRange': "firstSeenRange_example", // String | First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenAtSourceRange': "firstSeenAtSourceRange_example", // String | First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenAtMcRange': "firstSeenAtMcRange_example", // String | First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'lastSeenDays': "lastSeenDays_example", // String | Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenDays': "firstSeenDays_example", // String | First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenAtSourceDays': "firstSeenAtSourceDays_example", // String | First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenAtMcDays': "firstSeenAtMcDays_example", // String | First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
  'includeRelevantLinks': false, // Boolean | To include_relevant_links. Default is true
  'inventoryCountRange': "inventoryCountRange_example", // String | Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50
  'excludeDealerIds': "excludeDealerIds_example", // String | A list of dealer ids to exclude from result
  'excludeSources': "excludeSources_example", // String | A list of sources to exclude from result
  'excludeDealerListings': true, // Boolean | A list of fsbo listings to exclude from result
  'inTransit': "inTransit_example", // String | A boolean to filter in transit vehicles
  'seatingCapacity': "seatingCapacity_example", // String | To filter on vehicle seating capacity
  'engineSizeRange': "engineSizeRange_example", // String | Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
  'minPhotoLinks': "minPhotoLinks_example", // String | Filter listings based by number of photo links within given range
  'minPhotoLinksCached': "minPhotoLinksCached_example" // String | Filter listings based by number of cached photo links within given range
};
apiInstance.searchCarFsboActiveGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true]
 **latitude** | **Number**| Latitude component of location | [optional] 
 **longitude** | **Number**| Longitude component of location | [optional] 
 **radius** | **Number**| Radius around the search location (Unit - Miles) | [optional] 
 **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] 
 **includeLease** | **Boolean**| Boolean param to search for listings that include leasing options in them | [optional] 
 **includeFinance** | **Boolean**| Boolean param to search for listings that include finance options in them | [optional] 
 **leaseTerm** | **String**| Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60 | [optional] 
 **leaseDownPayment** | **String**| Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60 | [optional] 
 **leaseEmp** | **String**| Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60 | [optional] 
 **financeLoanTerm** | **String**| Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60 | [optional] 
 **financeLoanApr** | **String**| Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60 | [optional] 
 **financeEmp** | **String**| Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60 | [optional] 
 **financeDownPayment** | **String**| Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60 | [optional] 
 **financeDownPaymentPer** | **String**| Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60 | [optional] 
 **carType** | **String**| Car type. Allowed values are - new / used / certified | [optional] 
 **carfax1Owner** | **String**| Indicates whether car has had only one owner or not | [optional] 
 **carfaxCleanTitle** | **String**| Indicates whether car has clean ownership records | [optional] 
 **yearRange** | **String**| Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021 | [optional] 
 **year** | **String**| To filter listing on their year | [optional] 
 **make** | **String**| To filter listings on their make | [optional] 
 **model** | **String**| To filter listings on their model | [optional] 
 **trim** | **String**| To filter listing on their trim | [optional] 
 **vin** | **String**| To filter listing on their VIN | [optional] 
 **bodyType** | **String**| To filter listing on their body type | [optional] 
 **bodySubtype** | **String**| Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] 
 **vehicleType** | **String**| To filter listing on their vehicle type | [optional] 
 **vins** | **String**| Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc | [optional] 
 **taxonomyVins** | **String**| Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API. | [optional] 
 **mm** | **String**| Make-Model concatenated string. To help passing the results of auto-complete API on mm field, use this parameter and pass in the selected value as is | [optional] 
 **ymm** | **String**| Year-Make-Model concatenated string. To help passing the results of auto-complete API on ymm field, use this parameter and pass in the selected value as is | [optional] 
 **ymmt** | **String**| Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations. | [optional] 
 **match** | **String**| Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match | [optional] 
 **cylinders** | **String**| To filter listing on their cylinders | [optional] 
 **transmission** | **String**| To filter listing on their transmission | [optional] 
 **doors** | **String**| Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated | [optional] 
 **drivetrain** | **String**| To filter listing on their drivetrain | [optional] 
 **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] 
 **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] 
 **baseExteriorColor** | **String**| Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated | [optional] 
 **baseInteriorColor** | **String**| Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated | [optional] 
 **engine** | **String**| To filter listing on their engine | [optional] 
 **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] 
 **engineAspiration** | **String**| Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated | [optional] 
 **engineBlock** | **String**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] 
 **highwayMpgRange** | **String**| Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **cityMpgRange** | **String**| City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **milesRange** | **String**| Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **priceRange** | **String**| Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **msrpRange** | **String**| MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **domRange** | **String**| Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] 
 **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] 
 **rows** | **Number**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10]
 **start** | **Number**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0]
 **includeNonVinListings** | **Boolean**| To include non vin listings. Default is false | [optional] [default to false]
 **msaCode** | **String**| To filter listing on msa code in which they are listed | [optional] 
 **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] 
 **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] 
 **facetSort** | **String**| Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param | [optional] [default to &#39;count&#39;]
 **stats** | **String**| The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. | [optional] 
 **country** | **String**| To filter listing on Country in which they are listed | [optional] [default to &#39;US&#39;]
 **plot** | **Boolean**| If plot has value true results in around 25k coordinates with limited fields to plot respective graph | [optional] 
 **nodedup** | **Boolean**| If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin | [optional] 
 **dedup** | **Boolean**| If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source | [optional] 
 **owned** | **Boolean**| Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself | [optional] 
 **state** | **String**| To filter listing on State in which they are listed | [optional] 
 **city** | **String**| To filter listing on City in which they are listed | [optional] 
 **source** | **String**| To filter listing on their source only for widget requests | [optional] 
 **dealerId** | **String**| Dealer id to filter the listings. | [optional] 
 **trimO** | **String**| Filter listings on web scraped trim | [optional] 
 **trimR** | **String**| Filter trim on custom possible matches | [optional] 
 **domActiveRange** | **String**| Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **dom180Range** | **String**| Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **excludeCertified** | **Boolean**| Boolean param to exclude certified cars from search results | [optional] 
 **fuelType** | **String**| To filter listing on their fuel type | [optional] 
 **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] 
 **photoLinks** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them | [optional] 
 **photoLinksCached** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them | [optional] 
 **stockNo** | **String**| To filter listing on their stock number on lot | [optional] 
 **lastSeenRange** | **String**| Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenRange** | **String**| First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenAtSourceRange** | **String**| First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenAtMcRange** | **String**| First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **lastSeenDays** | **String**| Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenDays** | **String**| First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenAtSourceDays** | **String**| First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenAtMcDays** | **String**| First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **includeRelevantLinks** | **Boolean**| To include_relevant_links. Default is true | [optional] [default to false]
 **inventoryCountRange** | **String**| Inventory count range to filter listings with count of total listings in dealers inventory. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **excludeDealerIds** | **String**| A list of dealer ids to exclude from result | [optional] 
 **excludeSources** | **String**| A list of sources to exclude from result | [optional] 
 **excludeDealerListings** | **Boolean**| A list of fsbo listings to exclude from result | [optional] 
 **inTransit** | **String**| A boolean to filter in transit vehicles | [optional] 
 **seatingCapacity** | **String**| To filter on vehicle seating capacity | [optional] 
 **engineSizeRange** | **String**| Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2 | [optional] 
 **minPhotoLinks** | **String**| Filter listings based by number of photo links within given range | [optional] 
 **minPhotoLinksCached** | **String**| Filter listings based by number of cached photo links within given range | [optional] 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchCarRecentsGet

> SearchResponse searchCarRecentsGet(opts)

Gets Recent car listings for the given search criteria

This API produces a list of recently active (past 90 days) cars from the market for the given search criteria

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarSearchApi();
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'appendApiKey': true, // Boolean | Flag on whether to include api_key in response API urls (if any)
  'latitude': 3.4, // Number | Latitude component of location
  'longitude': 3.4, // Number | Longitude component of location
  'radius': 56, // Number | Radius around the search location (Unit - Miles)
  'zip': "zip_example", // String | To filter listing on ZIP around which they are listed
  'includeLease': true, // Boolean | Boolean param to search for listings that include leasing options in them
  'includeFinance': true, // Boolean | Boolean param to search for listings that include finance options in them
  'leaseTerm': "leaseTerm_example", // String | Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term=30-60
  'leaseDownPayment': "leaseDownPayment_example", // String | Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment=30-60
  'leaseEmp': "leaseEmp_example", // String | Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp=30-60
  'financeLoanTerm': "financeLoanTerm_example", // String | Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term=30-60
  'financeLoanApr': "financeLoanApr_example", // String | Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr=30-60
  'financeEmp': "financeEmp_example", // String | Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp=30-60
  'financeDownPayment': "financeDownPayment_example", // String | Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment=30-60
  'financeDownPaymentPer': "financeDownPaymentPer_example", // String | Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per=30-60
  'carType': "carType_example", // String | Car type. Allowed values are - new / used / certified
  'carfax1Owner': "carfax1Owner_example", // String | Indicates whether car has had only one owner or not
  'carfaxCleanTitle': "carfaxCleanTitle_example", // String | Indicates whether car has clean ownership records
  'yearRange': "yearRange_example", // String | Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
  'year': "year_example", // String | To filter listing on their year
  'make': "make_example", // String | To filter listings on their make
  'model': "model_example", // String | To filter listings on their model
  'trim': "trim_example", // String | To filter listing on their trim
  'dealerId': "dealerId_example", // String | Dealer id to filter the listings.
  'vin': "vin_example", // String | To filter listing on their VIN
  'source': "source_example", // String | To filter listing on their source
  'bodyType': "bodyType_example", // String | To filter listing on their body type
  'bodySubtype': "bodySubtype_example", // String | Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
  'vehicleType': "vehicleType_example", // String | To filter listing on their vehicle type
  'vins': "vins_example", // String | Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc
  'taxonomyVins': "taxonomyVins_example", // String | Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API.
  'ymmt': "ymmt_example", // String | Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe '|' character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - 'year|make||' or 'year|make|model' or '|make|model|' combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the 'vins' or 'taxonomy_vins' parameter to the search api instead the year|make|model|trim combinations.
  'match': "match_example", // String | Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
  'cylinders': "cylinders_example", // String | To filter listing on their cylinders
  'transmission': "transmission_example", // String | To filter listing on their transmission
  'doors': "doors_example", // String | Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
  'drivetrain': "drivetrain_example", // String | To filter listing on their drivetrain
  'exteriorColor': "exteriorColor_example", // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
  'interiorColor': "interiorColor_example", // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
  'baseExteriorColor': "baseExteriorColor_example", // String | Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
  'baseInteriorColor': "baseInteriorColor_example", // String | Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
  'engine': "engine_example", // String | To filter listing on their engine
  'engineSize': "engineSize_example", // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
  'engineAspiration': "engineAspiration_example", // String | Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
  'engineBlock': "engineBlock_example", // String | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
  'highwayMpgRange': "highwayMpgRange_example", // String | Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'cityMpgRange': "cityMpgRange_example", // String | City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'milesRange': "milesRange_example", // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
  'priceRange': "priceRange_example", // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'msrpRange': "msrpRange_example", // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'domRange': "domRange_example", // String | Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'lastSeenRange': "lastSeenRange_example", // String | Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenRange': "firstSeenRange_example", // String | First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenAtSourceRange': "firstSeenAtSourceRange_example", // String | First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenAtMcRange': "firstSeenAtMcRange_example", // String | First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'lastSeenDays': "lastSeenDays_example", // String | Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenDays': "firstSeenDays_example", // String | First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenAtSourceDays': "firstSeenAtSourceDays_example", // String | First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenAtMcDays': "firstSeenAtMcDays_example", // String | First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
  'sortBy': "sortBy_example", // String | Sort by field. Default sort field is distance from the given point
  'sortOrder': "sortOrder_example", // String | Sort order - asc or desc. Default sort order is asc
  'rows': 10, // Number | Number of results to return. Default is 10. Max is 50
  'start': 0, // Number | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
  'includeNonVinListings': false, // Boolean | To include non vin listings. Default is false
  'facets': "facets_example", // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
  'rangeFacets': "rangeFacets_example", // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
  'facetSort': "'count'", // String | Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
  'stats': "stats_example", // String | The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
  'country': "'US'", // String | To filter listing on Country in which they are listed
  'plot': true, // Boolean | If plot has value true results in around 25k coordinates with limited fields to plot respective graph
  'nodedup': true, // Boolean | If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
  'dedup': true, // Boolean | If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
  'owned': true, // Boolean | Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
  'state': "state_example", // String | To filter listing on State in which they are listed
  'city': "city_example", // String | To filter listing on City in which they are listed
  'msaCode': "msaCode_example", // String | To filter listing on msa code in which they are listed
  'dealerName': "dealerName_example", // String | Filter listings on dealer_name
  'dealershipGroupName': "dealershipGroupName_example", // String | Name of the dealership group to search for
  'trimO': "trimO_example", // String | Filter listings on web scraped trim
  'trimR': "trimR_example", // String | Filter trim on custom possible matches
  'domActiveRange': "domActiveRange_example", // String | Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'dom180Range': "dom180Range_example", // String | Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'excludeCertified': true, // Boolean | Boolean param to exclude certified cars from search results
  'fuelType': "fuelType_example", // String | To filter listing on their fuel type
  'dealerType': "dealerType_example", // String | Filter based on dealer type independant or franchise
  'photoLinks': true, // Boolean | A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don't have them
  'photoLinksCached': true, // Boolean | A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don't have them
  'stockNo': "stockNo_example", // String | To filter listing on their stock number on lot
  'sold': true, // Boolean | sold parameter to fetch only sold listings
  'includeRelevantLinks': false, // Boolean | To include_relevant_links. Default is true
  'expired': "expired_example", // String | Boolean falg to either fetch only the expired listings or active ones
  'excludeDealerIds': "excludeDealerIds_example", // String | A list of dealer ids to exclude from result
  'excludeSources': "excludeSources_example", // String | A list of sources to exclude from result
  'inTransit': "inTransit_example", // String | A boolean to filter in transit vehicles
  'seatingCapacity': "seatingCapacity_example", // String | To filter on vehicle seating capacity
  'activeInventoryDateRange': "activeInventoryDateRange_example", // String | date range to filter listings that were active within given date range. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'engineSizeRange': "engineSizeRange_example", // String | Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
  'priceChangeRange': "priceChangeRange_example" // String | Price change range to filter listings with price change within given price_change_range. Range to be given in the format - min-max e.g. 10-500
};
apiInstance.searchCarRecentsGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true]
 **latitude** | **Number**| Latitude component of location | [optional] 
 **longitude** | **Number**| Longitude component of location | [optional] 
 **radius** | **Number**| Radius around the search location (Unit - Miles) | [optional] 
 **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] 
 **includeLease** | **Boolean**| Boolean param to search for listings that include leasing options in them | [optional] 
 **includeFinance** | **Boolean**| Boolean param to search for listings that include finance options in them | [optional] 
 **leaseTerm** | **String**| Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60 | [optional] 
 **leaseDownPayment** | **String**| Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60 | [optional] 
 **leaseEmp** | **String**| Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60 | [optional] 
 **financeLoanTerm** | **String**| Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60 | [optional] 
 **financeLoanApr** | **String**| Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60 | [optional] 
 **financeEmp** | **String**| Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60 | [optional] 
 **financeDownPayment** | **String**| Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60 | [optional] 
 **financeDownPaymentPer** | **String**| Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60 | [optional] 
 **carType** | **String**| Car type. Allowed values are - new / used / certified | [optional] 
 **carfax1Owner** | **String**| Indicates whether car has had only one owner or not | [optional] 
 **carfaxCleanTitle** | **String**| Indicates whether car has clean ownership records | [optional] 
 **yearRange** | **String**| Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021 | [optional] 
 **year** | **String**| To filter listing on their year | [optional] 
 **make** | **String**| To filter listings on their make | [optional] 
 **model** | **String**| To filter listings on their model | [optional] 
 **trim** | **String**| To filter listing on their trim | [optional] 
 **dealerId** | **String**| Dealer id to filter the listings. | [optional] 
 **vin** | **String**| To filter listing on their VIN | [optional] 
 **source** | **String**| To filter listing on their source | [optional] 
 **bodyType** | **String**| To filter listing on their body type | [optional] 
 **bodySubtype** | **String**| Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] 
 **vehicleType** | **String**| To filter listing on their vehicle type | [optional] 
 **vins** | **String**| Comma separated list of 17 digit vins to search the matching cars for. Only 10 VINs allowed per request. If the request contains more than 10 VINs the first 10 VINs will be considered. Could be used as a More Like This or Similar Vehicles search for the given VINs. Ths vins parameter is an alternative to taxonomy_vins or ymmt parameters available with the search API. vins and taxonomy_vins parameters could be used to filter our cars with the exact build represented by the vins or taxonomy_vins whereas ymmt is a top level filter that does not filter cars by the build attributes like doors, drivetrain, cylinders, body type, body subtype, vehicle type etc | [optional] 
 **taxonomyVins** | **String**| Comma separated list of 10 letters excert from the 17 letter VIN. The 10 letters to be picked up from the 17 letter VIN are - first 8 letters and the 10th and 11th letter. E.g. For a VIN - 1FTFW1EF3EKE57182 the taxonomy vin would be - 1FTFW1EFEK  A taxonomy VIN identified a build of a car and could be used to filter our cars of a particular build. This is an alternative to the vin or ymmt parameters to the search API. | [optional] 
 **ymmt** | **String**| Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations. | [optional] 
 **match** | **String**| Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match | [optional] 
 **cylinders** | **String**| To filter listing on their cylinders | [optional] 
 **transmission** | **String**| To filter listing on their transmission | [optional] 
 **doors** | **String**| Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated | [optional] 
 **drivetrain** | **String**| To filter listing on their drivetrain | [optional] 
 **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] 
 **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] 
 **baseExteriorColor** | **String**| Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated | [optional] 
 **baseInteriorColor** | **String**| Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated | [optional] 
 **engine** | **String**| To filter listing on their engine | [optional] 
 **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] 
 **engineAspiration** | **String**| Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated | [optional] 
 **engineBlock** | **String**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] 
 **highwayMpgRange** | **String**| Highway mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **cityMpgRange** | **String**| City mileage range to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **milesRange** | **String**| Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **priceRange** | **String**| Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **msrpRange** | **String**| MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **domRange** | **String**| Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **lastSeenRange** | **String**| Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenRange** | **String**| First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenAtSourceRange** | **String**| First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenAtMcRange** | **String**| First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **lastSeenDays** | **String**| Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenDays** | **String**| First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenAtSourceDays** | **String**| First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenAtMcDays** | **String**| First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] 
 **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] 
 **rows** | **Number**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10]
 **start** | **Number**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0]
 **includeNonVinListings** | **Boolean**| To include non vin listings. Default is false | [optional] [default to false]
 **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] 
 **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] 
 **facetSort** | **String**| Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param | [optional] [default to &#39;count&#39;]
 **stats** | **String**| The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. | [optional] 
 **country** | **String**| To filter listing on Country in which they are listed | [optional] [default to &#39;US&#39;]
 **plot** | **Boolean**| If plot has value true results in around 25k coordinates with limited fields to plot respective graph | [optional] 
 **nodedup** | **Boolean**| If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin | [optional] 
 **dedup** | **Boolean**| If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source | [optional] 
 **owned** | **Boolean**| Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself | [optional] 
 **state** | **String**| To filter listing on State in which they are listed | [optional] 
 **city** | **String**| To filter listing on City in which they are listed | [optional] 
 **msaCode** | **String**| To filter listing on msa code in which they are listed | [optional] 
 **dealerName** | **String**| Filter listings on dealer_name | [optional] 
 **dealershipGroupName** | **String**| Name of the dealership group to search for | [optional] 
 **trimO** | **String**| Filter listings on web scraped trim | [optional] 
 **trimR** | **String**| Filter trim on custom possible matches | [optional] 
 **domActiveRange** | **String**| Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **dom180Range** | **String**| Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **excludeCertified** | **Boolean**| Boolean param to exclude certified cars from search results | [optional] 
 **fuelType** | **String**| To filter listing on their fuel type | [optional] 
 **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] 
 **photoLinks** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them | [optional] 
 **photoLinksCached** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them | [optional] 
 **stockNo** | **String**| To filter listing on their stock number on lot | [optional] 
 **sold** | **Boolean**| sold parameter to fetch only sold listings | [optional] 
 **includeRelevantLinks** | **Boolean**| To include_relevant_links. Default is true | [optional] [default to false]
 **expired** | **String**| Boolean falg to either fetch only the expired listings or active ones | [optional] 
 **excludeDealerIds** | **String**| A list of dealer ids to exclude from result | [optional] 
 **excludeSources** | **String**| A list of sources to exclude from result | [optional] 
 **inTransit** | **String**| A boolean to filter in transit vehicles | [optional] 
 **seatingCapacity** | **String**| To filter on vehicle seating capacity | [optional] 
 **activeInventoryDateRange** | **String**| date range to filter listings that were active within given date range. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **engineSizeRange** | **String**| Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2 | [optional] 
 **priceChangeRange** | **String**| Price change range to filter listings with price change within given price_change_range. Range to be given in the format - min-max e.g. 10-500 | [optional] 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchCarUkRecentsGet

> UKSearchResponse searchCarUkRecentsGet(opts)

Gets Recent UK car listings for the given search criteria

This API produces a list of recently active (past 90 days) cars from the market for the given search criteria

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarSearchApi();
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'appendApiKey': true, // Boolean | Flag on whether to include api_key in response API urls (if any)
  'latitude': 3.4, // Number | Latitude component of location
  'longitude': 3.4, // Number | Longitude component of location
  'radius': 56, // Number | Radius around the search location (Unit - Miles)
  'zip': "zip_example", // String | To filter listing on ZIP around which they are listed
  'includeLease': true, // Boolean | Boolean param to search for listings that include leasing options in them
  'includeFinance': true, // Boolean | Boolean param to search for listings that include finance options in them
  'leaseTerm': "leaseTerm_example", // String | Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term=30-60
  'leaseDownPayment': "leaseDownPayment_example", // String | Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment=30-60
  'leaseEmp': "leaseEmp_example", // String | Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp=30-60
  'financeLoanTerm': "financeLoanTerm_example", // String | Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term=30-60
  'financeLoanApr': "financeLoanApr_example", // String | Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr=30-60
  'financeEmp': "financeEmp_example", // String | Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp=30-60
  'financeDownPayment': "financeDownPayment_example", // String | Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment=30-60
  'financeDownPaymentPer': "financeDownPaymentPer_example", // String | Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per=30-60
  'carType': "carType_example", // String | Car type. Allowed values are - new / used / certified
  'carfax1Owner': "carfax1Owner_example", // String | Indicates whether car has had only one owner or not
  'carfaxCleanTitle': "carfaxCleanTitle_example", // String | Indicates whether car has clean ownership records
  'yearRange': "yearRange_example", // String | Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021
  'year': "year_example", // String | To filter listing on their year
  'make': "make_example", // String | To filter listings on their make
  'model': "model_example", // String | To filter listings on their model
  'trim': "trim_example", // String | To filter listing on their trim
  'dealerId': "dealerId_example", // String | Dealer id to filter the listings.
  'source': "source_example", // String | To filter listing on their source
  'bodyType': "bodyType_example", // String | To filter listing on their body type
  'bodySubtype': "bodySubtype_example", // String | Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated
  'vehicleType': "vehicleType_example", // String | To filter listing on their vehicle type
  'ymmt': "ymmt_example", // String | Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe '|' character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - 'year|make||' or 'year|make|model' or '|make|model|' combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the 'vins' or 'taxonomy_vins' parameter to the search api instead the year|make|model|trim combinations.
  'match': "match_example", // String | Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match
  'cylinders': "cylinders_example", // String | To filter listing on their cylinders
  'transmission': "transmission_example", // String | To filter listing on their transmission
  'doors': "doors_example", // String | Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated
  'drivetrain': "drivetrain_example", // String | To filter listing on their drivetrain
  'exteriorColor': "exteriorColor_example", // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
  'interiorColor': "interiorColor_example", // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
  'baseExteriorColor': "baseExteriorColor_example", // String | Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated
  'baseInteriorColor': "baseInteriorColor_example", // String | Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated
  'engine': "engine_example", // String | To filter listing on their engine
  'engineSize': "engineSize_example", // String | Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated
  'engineAspiration': "engineAspiration_example", // String | Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated
  'engineBlock': "engineBlock_example", // String | Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated
  'highwayMpgRange': "highwayMpgRange_example", // String | Highway mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'cityMpgRange': "cityMpgRange_example", // String | City mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'combinedMpgRange': "combinedMpgRange_example", // String | Combined mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'milesRange': "milesRange_example", // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
  'priceRange': "priceRange_example", // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'msrpRange': "msrpRange_example", // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'domRange': "domRange_example", // String | Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'lastSeenRange': "lastSeenRange_example", // String | Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenRange': "firstSeenRange_example", // String | First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenAtSourceRange': "firstSeenAtSourceRange_example", // String | First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenAtMcRange': "firstSeenAtMcRange_example", // String | First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'lastSeenDays': "lastSeenDays_example", // String | Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenDays': "firstSeenDays_example", // String | First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenAtSourceDays': "firstSeenAtSourceDays_example", // String | First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenAtMcDays': "firstSeenAtMcDays_example", // String | First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12
  'sortBy': "sortBy_example", // String | Sort by field. Default sort field is distance from the given point
  'sortOrder': "sortOrder_example", // String | Sort order - asc or desc. Default sort order is asc
  'rows': 10, // Number | Number of results to return. Default is 10. Max is 50
  'start': 0, // Number | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
  'includeNonVinListings': false, // Boolean | To include non vin listings. Default is false
  'facets': "facets_example", // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
  'rangeFacets': "rangeFacets_example", // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
  'facetSort': "'count'", // String | Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
  'stats': "stats_example", // String | The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
  'country': "'uk'", // String | To filter listing on Country in which they are listed
  'plot': true, // Boolean | If plot has value true results in around 25k coordinates with limited fields to plot respective graph
  'nodedup': true, // Boolean | If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin
  'dedup': true, // Boolean | If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source
  'owned': true, // Boolean | Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself
  'state': "state_example", // String | To filter listing on State in which they are listed
  'city': "city_example", // String | To filter listing on City in which they are listed
  'msaCode': "msaCode_example", // String | To filter listing on msa code in which they are listed
  'dealerName': "dealerName_example", // String | Filter listings on dealer_name
  'dealershipGroupName': "dealershipGroupName_example", // String | Name of the dealership group to search for
  'trimO': "trimO_example", // String | Filter listings on web scraped trim
  'trimR': "trimR_example", // String | Filter trim on custom possible matches
  'domActiveRange': "domActiveRange_example", // String | Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'dom180Range': "dom180Range_example", // String | Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50
  'excludeCertified': true, // Boolean | Boolean param to exclude certified cars from search results
  'fuelType': "fuelType_example", // String | To filter listing on their fuel type
  'dealerType': "dealerType_example", // String | Filter based on dealer type independant or franchise
  'photoLinks': true, // Boolean | A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don't have them
  'photoLinksCached': true, // Boolean | A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don't have them
  'stockNo': "stockNo_example", // String | To filter listing on their stock number on lot
  'sold': true, // Boolean | sold parameter to fetch only sold listings
  'includeRelevantLinks': false, // Boolean | To include_relevant_links. Default is true
  'expired': "expired_example", // String | Boolean falg to either fetch only the expired listings or active ones
  'excludeDealerIds': "excludeDealerIds_example", // String | A list of dealer ids to exclude from result
  'excludeSources': "excludeSources_example", // String | A list of sources to exclude from result
  'inTransit': "inTransit_example", // String | A boolean to filter in transit vehicles
  'seatingCapacity': "seatingCapacity_example", // String | To filter on vehicle seating capacity
  'insuranceGroup': "insuranceGroup_example", // String | Insurance Group
  'vrm': "vrm_example", // String | To filter on vrm
  'numOwners': "numOwners_example", // String | Number of owners. Range to be given in the format - min-max e.g. 1000-5000
  'variant': "variant_example", // String | To filter listing on their variant
  'postalCode': "postalCode_example", // String | To filter listing on postal code around which they are listed
  'writeOffCategory': "writeOffCategory_example", // String | write off category
  'fcaStatus': "fcaStatus_example", // String | To filter on fca status
  'activeInventoryDateRange': "activeInventoryDateRange_example", // String | date range to filter listings that were active within given date range. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'engineSizeRange': "engineSizeRange_example", // String | Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2
  'priceChangeRange': "priceChangeRange_example" // String | Price change range to filter listings with price change within given price_change_range. Range to be given in the format - min-max e.g. 10-500
};
apiInstance.searchCarUkRecentsGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **appendApiKey** | **Boolean**| Flag on whether to include api_key in response API urls (if any) | [optional] [default to true]
 **latitude** | **Number**| Latitude component of location | [optional] 
 **longitude** | **Number**| Longitude component of location | [optional] 
 **radius** | **Number**| Radius around the search location (Unit - Miles) | [optional] 
 **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] 
 **includeLease** | **Boolean**| Boolean param to search for listings that include leasing options in them | [optional] 
 **includeFinance** | **Boolean**| Boolean param to search for listings that include finance options in them | [optional] 
 **leaseTerm** | **String**| Search listings with exact lease term, or inside a range with min and max seperated by a dash like lease_term&#x3D;30-60 | [optional] 
 **leaseDownPayment** | **String**| Search listings with exact down payment in lease offers, or inside a range with min and max seperated by a dash like lease_down_payment&#x3D;30-60 | [optional] 
 **leaseEmp** | **String**| Search listings with lease offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like lease_emp&#x3D;30-60 | [optional] 
 **financeLoanTerm** | **String**| Search listings with exact finance loan term, or inside a range with min and max seperated by a dash like finance_loan_term&#x3D;30-60 | [optional] 
 **financeLoanApr** | **String**| Search listings with finance offers exactly matching loans Annual Percentage Rate, or inside a range with min and max seperated by a dash like finance_loan_apr&#x3D;30-60 | [optional] 
 **financeEmp** | **String**| Search listings with finance offers exactly matching Estimated Monthly Payment(EMI), or inside a range with min and max seperated by a dash like finance_emp&#x3D;30-60 | [optional] 
 **financeDownPayment** | **String**| Search listings with exact down payment in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment&#x3D;30-60 | [optional] 
 **financeDownPaymentPer** | **String**| Search listings with exact down payment percentage in finance offers, or inside a range with min and max seperated by a dash like finance_down_payment_per&#x3D;30-60 | [optional] 
 **carType** | **String**| Car type. Allowed values are - new / used / certified | [optional] 
 **carfax1Owner** | **String**| Indicates whether car has had only one owner or not | [optional] 
 **carfaxCleanTitle** | **String**| Indicates whether car has clean ownership records | [optional] 
 **yearRange** | **String**| Year range to filter listings with the year in the range given. Range to be given in the format - min-max e.g. 2019-2021 | [optional] 
 **year** | **String**| To filter listing on their year | [optional] 
 **make** | **String**| To filter listings on their make | [optional] 
 **model** | **String**| To filter listings on their model | [optional] 
 **trim** | **String**| To filter listing on their trim | [optional] 
 **dealerId** | **String**| Dealer id to filter the listings. | [optional] 
 **source** | **String**| To filter listing on their source | [optional] 
 **bodyType** | **String**| To filter listing on their body type | [optional] 
 **bodySubtype** | **String**| Body subtype to filter the listings on. Valid filter values are those that our Search facets API returns for unique body subtypes. You can pass in multiple body subtype values comma separated | [optional] 
 **vehicleType** | **String**| To filter listing on their vehicle type | [optional] 
 **ymmt** | **String**| Comma separated list of Year, Make, Model, Trim combinations. Each combination needs to have the year,make,model, trim values separated by a pipe &#39;|&#39; character in the form year|make|model|trim. e.g. 2010|Audi|A5,2014|Nissan|Sentra|S 6MT,|Honda|City|   You could just provide strings of the form - &#39;year|make||&#39; or &#39;year|make|model&#39; or &#39;|make|model|&#39; combinations. Individual year / make / model filters provied with the API calls will take precedence over the Year, Make, Model, Trim combinations. The Make, Model, Trim values must be valid values as per the Marketcheck Vin Decoder. If you are using a separate vin decoder then look at using the &#39;vins&#39; or &#39;taxonomy_vins&#39; parameter to the search api instead the year|make|model|trim combinations. | [optional] 
 **match** | **String**| Comma separated list of Year, Make, Model, Trim fields. For example - year,make,model,trim fields for which user wants to do an exact match | [optional] 
 **cylinders** | **String**| To filter listing on their cylinders | [optional] 
 **transmission** | **String**| To filter listing on their transmission | [optional] 
 **doors** | **String**| Doors to filter the cars on. Valid filter values are those that our Search facets API returns for unique doors. You can pass in multiple doors values comma separated | [optional] 
 **drivetrain** | **String**| To filter listing on their drivetrain | [optional] 
 **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] 
 **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] 
 **baseExteriorColor** | **String**| Base exterior color to match. Valid filter values are those that our Search facets API returns for unique base exterior colors. You can pass in multiple base interior color values comma separated | [optional] 
 **baseInteriorColor** | **String**| Base interior color to match. Valid filter values are those that our Search facets API returns for unique base interior colors. You can pass in multiple base interior color values comma separated | [optional] 
 **engine** | **String**| To filter listing on their engine | [optional] 
 **engineSize** | **String**| Engine Size to match. Valid filter values are those that our Search facets API returns for unique engine size. You can pass in multiple engine size values comma separated | [optional] 
 **engineAspiration** | **String**| Engine Aspiration to match. Valid filter values are those that our Search facets API returns for unique Engine Aspirations. You can pass in multiple Engine aspirations values comma separated | [optional] 
 **engineBlock** | **String**| Engine Block to match. Valid filter values are those that our Search facets API returns for unique Engine Block. You can pass in multiple Engine Block values comma separated | [optional] 
 **highwayMpgRange** | **String**| Highway mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **cityMpgRange** | **String**| City mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **combinedMpgRange** | **String**| Combined mileage range for UK to filter listings with the mileage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **milesRange** | **String**| Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **priceRange** | **String**| Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **msrpRange** | **String**| MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **domRange** | **String**| Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **lastSeenRange** | **String**| Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenRange** | **String**| First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenAtSourceRange** | **String**| First seen at source date range to filter listings with the first seen at source in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenAtMcRange** | **String**| First seen at MC date range to filter listings with the first seen at MC in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **lastSeenDays** | **String**| Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenDays** | **String**| First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenAtSourceDays** | **String**| First seen at source days range to filter listings with the first seen at source in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenAtMcDays** | **String**| First seen at MC days range to filter listings with the first seen at MC in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] 
 **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] 
 **rows** | **Number**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10]
 **start** | **Number**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0]
 **includeNonVinListings** | **Boolean**| To include non vin listings. Default is false | [optional] [default to false]
 **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] 
 **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] 
 **facetSort** | **String**| Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param | [optional] [default to &#39;count&#39;]
 **stats** | **String**| The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. | [optional] 
 **country** | **String**| To filter listing on Country in which they are listed | [optional] [default to &#39;uk&#39;]
 **plot** | **Boolean**| If plot has value true results in around 25k coordinates with limited fields to plot respective graph | [optional] 
 **nodedup** | **Boolean**| If nodedup is set to true then API will give results without is_searchable i.e multiple listings for single vin | [optional] 
 **dedup** | **Boolean**| If dedup is set to true then will give results with is_searchable irrespecive of dealer_id or source | [optional] 
 **owned** | **Boolean**| Used in combination with dealer_id or source, when true returns the listings actually owned by dealer himself | [optional] 
 **state** | **String**| To filter listing on State in which they are listed | [optional] 
 **city** | **String**| To filter listing on City in which they are listed | [optional] 
 **msaCode** | **String**| To filter listing on msa code in which they are listed | [optional] 
 **dealerName** | **String**| Filter listings on dealer_name | [optional] 
 **dealershipGroupName** | **String**| Name of the dealership group to search for | [optional] 
 **trimO** | **String**| Filter listings on web scraped trim | [optional] 
 **trimR** | **String**| Filter trim on custom possible matches | [optional] 
 **domActiveRange** | **String**| Active Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **dom180Range** | **String**| Last 180 Days on Market range to filter cars with the DOM within the given range. Range to be given in the format - min-max e.g. 10-50 | [optional] 
 **excludeCertified** | **Boolean**| Boolean param to exclude certified cars from search results | [optional] 
 **fuelType** | **String**| To filter listing on their fuel type | [optional] 
 **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] 
 **photoLinks** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links in search results, And discard those that don&#39;t have them | [optional] 
 **photoLinksCached** | **Boolean**| A boolean indicating whether to include only those listings that have photo_links_cached in search results, And discard those that don&#39;t have them | [optional] 
 **stockNo** | **String**| To filter listing on their stock number on lot | [optional] 
 **sold** | **Boolean**| sold parameter to fetch only sold listings | [optional] 
 **includeRelevantLinks** | **Boolean**| To include_relevant_links. Default is true | [optional] [default to false]
 **expired** | **String**| Boolean falg to either fetch only the expired listings or active ones | [optional] 
 **excludeDealerIds** | **String**| A list of dealer ids to exclude from result | [optional] 
 **excludeSources** | **String**| A list of sources to exclude from result | [optional] 
 **inTransit** | **String**| A boolean to filter in transit vehicles | [optional] 
 **seatingCapacity** | **String**| To filter on vehicle seating capacity | [optional] 
 **insuranceGroup** | **String**| Insurance Group | [optional] 
 **vrm** | **String**| To filter on vrm | [optional] 
 **numOwners** | **String**| Number of owners. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **variant** | **String**| To filter listing on their variant | [optional] 
 **postalCode** | **String**| To filter listing on postal code around which they are listed | [optional] 
 **writeOffCategory** | **String**| write off category | [optional] 
 **fcaStatus** | **String**| To filter on fca status | [optional] 
 **activeInventoryDateRange** | **String**| date range to filter listings that were active within given date range. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **engineSizeRange** | **String**| Engine size range to filter listings with engine size in the given range. Range to be given in the format - min-max e.g. 1.0-2 | [optional] 
 **priceChangeRange** | **String**| Price change range to filter listings with price change within given price_change_range. Range to be given in the format - min-max e.g. 10-500 | [optional] 

### Return type

[**UKSearchResponse**](UKSearchResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

