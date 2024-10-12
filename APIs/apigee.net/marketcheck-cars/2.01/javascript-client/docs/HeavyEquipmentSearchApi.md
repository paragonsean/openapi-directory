# MarketcheckApis.HeavyEquipmentSearchApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listingHeavyEquipmentIdExtraGet**](HeavyEquipmentSearchApi.md#listingHeavyEquipmentIdExtraGet) | **GET** /listing/heavy-equipment/{id}/extra | Long text Heavy equipment Listings attributes for Listing with the given id
[**listingHeavyEquipmentIdGet**](HeavyEquipmentSearchApi.md#listingHeavyEquipmentIdGet) | **GET** /listing/heavy-equipment/{id} | Heavy equipment listing by id
[**listingHeavyEquipmentIdMediaGet**](HeavyEquipmentSearchApi.md#listingHeavyEquipmentIdMediaGet) | **GET** /listing/heavy-equipment/{id}/media | Listing media by id
[**searchHeavyEquipmentActiveGet**](HeavyEquipmentSearchApi.md#searchHeavyEquipmentActiveGet) | **GET** /search/heavy-equipment/active | Gets active heavy equipment listings for the given search criteria
[**searchHeavyEquipmentAutoCompleteGet**](HeavyEquipmentSearchApi.md#searchHeavyEquipmentAutoCompleteGet) | **GET** /search/heavy-equipment/auto-complete | API for auto-completion of inputs



## listingHeavyEquipmentIdExtraGet

> ListingExtraAttributes listingHeavyEquipmentIdExtraGet(id, opts)

Long text Heavy equipment Listings attributes for Listing with the given id

Get Heavy equipment listing options, features, seller comments

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.HeavyEquipmentSearchApi();
let id = "id_example"; // String | Listing id to get all the listing attributes
let opts = {
  'apiKey': "apiKey_example" // String | The API Authentication Key. Mandatory with all API calls.
};
apiInstance.listingHeavyEquipmentIdExtraGet(id, opts, (error, data, response) => {
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


## listingHeavyEquipmentIdGet

> HeavyEquipmentsListing listingHeavyEquipmentIdGet(id, opts)

Heavy equipment listing by id

Get a particular Heavy equipment listing by its id

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.HeavyEquipmentSearchApi();
let id = "id_example"; // String | Listing id to get all the listing attributes
let opts = {
  'apiKey': "apiKey_example" // String | The API Authentication Key. Mandatory with all API calls.
};
apiInstance.listingHeavyEquipmentIdGet(id, opts, (error, data, response) => {
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

[**HeavyEquipmentsListing**](HeavyEquipmentsListing.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listingHeavyEquipmentIdMediaGet

> ListingMedia listingHeavyEquipmentIdMediaGet(id, opts)

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

let apiInstance = new MarketcheckApis.HeavyEquipmentSearchApi();
let id = "id_example"; // String | Listing id to get all the listing attributes
let opts = {
  'apiKey': "apiKey_example" // String | The API Authentication Key. Mandatory with all API calls.
};
apiInstance.listingHeavyEquipmentIdMediaGet(id, opts, (error, data, response) => {
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

[**ListingMedia**](ListingMedia.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchHeavyEquipmentActiveGet

> HeavyEquipmentsSearchResponse searchHeavyEquipmentActiveGet(opts)

Gets active heavy equipment listings for the given search criteria

This endpoint provides search on heavy equipment inventory. This API produces a list of currently active heavy equipments from the market for the given search criteria. The API results are limited to allow pagination upto 5000 rows.   The search API facilitates the following use cases -  1. Search heavy equipments around a given geo-point within a given radius  2. Search heavy equipments for a specific year / make / model or combination of these  3. Search heavy equipments matching multiple year, make, model combinatins in the same search request 4. Filter results by most heavy equipment specification attributes 5. Filter heavy equipments within a given price / miles range 6. Specify a sort order for the results on price / miles / listed date  7. Search heavy equipments for a given City / State combination  8. Get Facets to build the search drill downs  9. Get Market averages for price/miles for your search

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.HeavyEquipmentSearchApi();
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'priceRange': "priceRange_example", // String | Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'milesRange': "milesRange_example", // String | Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000
  'msrpRange': "msrpRange_example", // String | MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'latitude': 3.4, // Number | Latitude component of location
  'longitude': 3.4, // Number | Longitude component of location
  'radius': 56, // Number | Radius around the search location (Unit - Miles)
  'searchText': "searchText_example", // String | To search a substring across entire document
  'year': "year_example", // String | To filter listing on their year
  'make': "make_example", // String | To filter listings on their make
  'model': "model_example", // String | To filter listings on their model
  'trim': "trim_example", // String | To filter listing on their trim
  'vin': "vin_example", // String | To filter listing on their VIN
  'inventoryType': "inventoryType_example", // String | To filter listing on their condition. Either used or new
  'stockNo': "stockNo_example", // String | To filter listing on their stock number on lot
  'source': "source_example", // String | To filter listing on their source
  'dealerName': "dealerName_example", // String | Filter listings on dealer_name
  'dealerId': "dealerId_example", // String | Dealer id to filter the listings.
  'exteriorColor': "exteriorColor_example", // String | Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated
  'interiorColor': "interiorColor_example", // String | Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated
  'engine': "engine_example", // String | To filter listing on their engine
  'fuelType': "fuelType_example", // String | To filter listing on their fuel type
  'transmission': "transmission_example", // String | To filter listing on their transmission
  'drivetrain': "drivetrain_example", // String | To filter listing on their drivetrain
  'bodyType': "bodyType_example", // String | To filter listing on their body type
  'category': "category_example", // String | To filter heavy equipments on their category
  'subCategory': "subCategory_example", // String | To filter heavy equipments on their sub-category
  'hoursUsedRange': "hoursUsedRange_example", // String | Hours used range to filter heavy equipments with the their usage in the range given. Range to be given in the format - min-max e.g. 1000-5000
  'state': "state_example", // String | To filter listing on State in which they are listed
  'city': "city_example", // String | To filter listing on City in which they are listed
  'zip': "zip_example", // String | To filter listing on ZIP around which they are listed
  'msaCode': "msaCode_example", // String | To filter listing on msa code in which they are listed
  'sortBy': "sortBy_example", // String | Sort by field. Default sort field is distance from the given point
  'sortOrder': "sortOrder_example", // String | Sort order - asc or desc. Default sort order is asc
  'rows': 10, // Number | Number of results to return. Default is 10. Max is 50
  'start': 0, // Number | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
  'facets': "facets_example", // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
  'rangeFacets': "rangeFacets_example", // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
  'facetSort': "'count'", // String | Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param
  'stats': "stats_example", // String | The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond.
  'lastSeenRange': "lastSeenRange_example", // String | Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'firstSeenRange': "firstSeenRange_example", // String | First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623
  'lastSeenDays': "lastSeenDays_example", // String | Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12
  'firstSeenDays': "firstSeenDays_example" // String | First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12
};
apiInstance.searchHeavyEquipmentActiveGet(opts, (error, data, response) => {
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
 **priceRange** | **String**| Price range to filter listings with the price in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **milesRange** | **String**| Miles range to filter listings with miles in the given range. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **msrpRange** | **String**| MSRP range to filter listings with the msrp in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **latitude** | **Number**| Latitude component of location | [optional] 
 **longitude** | **Number**| Longitude component of location | [optional] 
 **radius** | **Number**| Radius around the search location (Unit - Miles) | [optional] 
 **searchText** | **String**| To search a substring across entire document | [optional] 
 **year** | **String**| To filter listing on their year | [optional] 
 **make** | **String**| To filter listings on their make | [optional] 
 **model** | **String**| To filter listings on their model | [optional] 
 **trim** | **String**| To filter listing on their trim | [optional] 
 **vin** | **String**| To filter listing on their VIN | [optional] 
 **inventoryType** | **String**| To filter listing on their condition. Either used or new | [optional] 
 **stockNo** | **String**| To filter listing on their stock number on lot | [optional] 
 **source** | **String**| To filter listing on their source | [optional] 
 **dealerName** | **String**| Filter listings on dealer_name | [optional] 
 **dealerId** | **String**| Dealer id to filter the listings. | [optional] 
 **exteriorColor** | **String**| Exterior color to match. Valid filter values are those that our Search facets API returns for unique exterior colors. You can pass in multiple exterior color values comma separated | [optional] 
 **interiorColor** | **String**| Interior color to match. Valid filter values are those that our Search facets API returns for unique interior colors. You can pass in multiple interior color values comma separated | [optional] 
 **engine** | **String**| To filter listing on their engine | [optional] 
 **fuelType** | **String**| To filter listing on their fuel type | [optional] 
 **transmission** | **String**| To filter listing on their transmission | [optional] 
 **drivetrain** | **String**| To filter listing on their drivetrain | [optional] 
 **bodyType** | **String**| To filter listing on their body type | [optional] 
 **category** | **String**| To filter heavy equipments on their category | [optional] 
 **subCategory** | **String**| To filter heavy equipments on their sub-category | [optional] 
 **hoursUsedRange** | **String**| Hours used range to filter heavy equipments with the their usage in the range given. Range to be given in the format - min-max e.g. 1000-5000 | [optional] 
 **state** | **String**| To filter listing on State in which they are listed | [optional] 
 **city** | **String**| To filter listing on City in which they are listed | [optional] 
 **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] 
 **msaCode** | **String**| To filter listing on msa code in which they are listed | [optional] 
 **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] 
 **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] 
 **rows** | **Number**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10]
 **start** | **Number**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0]
 **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] 
 **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] 
 **facetSort** | **String**| Control sort order of facets with this parameter with default sort being on count, Other available sort is alphabetical sort, which can be obtained by using index as value for this param | [optional] [default to &#39;count&#39;]
 **stats** | **String**| The list of fields for which stats need to be generated based on the matching listings for the search criteria. The stats consists of mean, max, average and count of listings based on which the stats are calculated for the field. Stats could be requested in addition to the listings for the search. Please note - The API calls with the stats fields may take longer to respond. | [optional] 
 **lastSeenRange** | **String**| Last seen date range to filter listings with the last seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **firstSeenRange** | **String**| First seen date range to filter listings with the first seen in the range given. Range to be given in the format [YYYYMMDD] - min-max e.g. 20190523-20190623 | [optional] 
 **lastSeenDays** | **String**| Last seen days range to filter listings with the last seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 
 **firstSeenDays** | **String**| First seen days range to filter listings with the first seen in the range given. Range to be given in the format - min-max e.g. 25-12 | [optional] 

### Return type

[**HeavyEquipmentsSearchResponse**](HeavyEquipmentsSearchResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchHeavyEquipmentAutoCompleteGet

> SearchAutoCompleteResponse searchHeavyEquipmentAutoCompleteGet(field, input, opts)

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

let apiInstance = new MarketcheckApis.HeavyEquipmentSearchApi();
let field = "field_example"; // String | Field name for which you want auto-completion
let input = "input_example"; // String | Input entered so far
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'year': "year_example", // String | To filter listing on their year
  'make': "make_example", // String | To filter listings on their make
  'model': "model_example", // String | To filter listings on their model
  'trim': "trim_example", // String | To filter listing on their trim
  'bodyType': "bodyType_example", // String | To filter listing on their body type
  'vehicleType': "vehicleType_example", // String | To filter listing on their vehicle type
  'transmission': "transmission_example", // String | To filter listing on their transmission
  'drivetrain': "drivetrain_example", // String | To filter listing on their drivetrain
  'fuelType': "fuelType_example", // String | To filter listing on their fuel type
  'color': "color_example", // String | Color of the vehicle
  'engine': "engine_example", // String | To filter listing on their engine
  'state': "state_example", // String | To filter listing on State in which they are listed
  'city': "city_example", // String | To filter listing on City in which they are listed
  'inventoryType': "inventoryType_example", // String | To filter listing on their condition. Either used or new
  'ignoreCase': true, // Boolean | Boolean variable to indicate ignore case of current input
  'termCounts': false, // Boolean | Boolean variable to indicate wheather to include term counts as well in response
  'sortBy': "'index'", // String | Sort the response, either by index or count(default)
  'sellerType': "sellerType_example", // String | seller type for autocomplete
  'radius': 56, // Number | Radius around the search location (Unit - Miles)
  'zip': "zip_example", // String | To filter listing on ZIP around which they are listed
  'facetMinCount': 1 // Number | Provide minimum count value for facets
};
apiInstance.searchHeavyEquipmentAutoCompleteGet(field, input, opts, (error, data, response) => {
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
 **vehicleType** | **String**| To filter listing on their vehicle type | [optional] 
 **transmission** | **String**| To filter listing on their transmission | [optional] 
 **drivetrain** | **String**| To filter listing on their drivetrain | [optional] 
 **fuelType** | **String**| To filter listing on their fuel type | [optional] 
 **color** | **String**| Color of the vehicle | [optional] 
 **engine** | **String**| To filter listing on their engine | [optional] 
 **state** | **String**| To filter listing on State in which they are listed | [optional] 
 **city** | **String**| To filter listing on City in which they are listed | [optional] 
 **inventoryType** | **String**| To filter listing on their condition. Either used or new | [optional] 
 **ignoreCase** | **Boolean**| Boolean variable to indicate ignore case of current input | [optional] [default to true]
 **termCounts** | **Boolean**| Boolean variable to indicate wheather to include term counts as well in response | [optional] [default to false]
 **sortBy** | **String**| Sort the response, either by index or count(default) | [optional] [default to &#39;index&#39;]
 **sellerType** | **String**| seller type for autocomplete | [optional] 
 **radius** | **Number**| Radius around the search location (Unit - Miles) | [optional] 
 **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] 
 **facetMinCount** | **Number**| Provide minimum count value for facets | [optional] [default to 1]

### Return type

[**SearchAutoCompleteResponse**](SearchAutoCompleteResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

