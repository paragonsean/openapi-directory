# MarketcheckApis.DealerAPIApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dealerCarUkIdGet**](DealerAPIApi.md#dealerCarUkIdGet) | **GET** /dealer/car/uk/{id} | Dealer by id
[**dealerHeavyEquipmentIdGet**](DealerAPIApi.md#dealerHeavyEquipmentIdGet) | **GET** /dealer/heavy-equipment/{id} | Dealer by id
[**dealerMotorcycleIdGet**](DealerAPIApi.md#dealerMotorcycleIdGet) | **GET** /dealer/motorcycle/{id} | Dealer by id
[**dealerRvIdGet**](DealerAPIApi.md#dealerRvIdGet) | **GET** /dealer/rv/{id} | Dealer by id
[**dealerSearch**](DealerAPIApi.md#dealerSearch) | **GET** /dealers/car | Find car dealers around
[**dealersCarUkGet**](DealerAPIApi.md#dealersCarUkGet) | **GET** /dealers/car/uk | Find car dealers around
[**dealersHeavyEquipmentGet**](DealerAPIApi.md#dealersHeavyEquipmentGet) | **GET** /dealers/heavy-equipment | Find car dealers around
[**dealersMotorcycleGet**](DealerAPIApi.md#dealersMotorcycleGet) | **GET** /dealers/motorcycle | Find car dealers around
[**dealersRvGet**](DealerAPIApi.md#dealersRvGet) | **GET** /dealers/rv | Find car dealers around
[**getDealer**](DealerAPIApi.md#getDealer) | **GET** /dealer/car/{id} | Dealer by id



## dealerCarUkIdGet

> Dealer dealerCarUkIdGet(id, opts)

Dealer by id

Get a particular dealer&#39;s information by its id

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.DealerAPIApi();
let id = "id_example"; // String | Dealer id to get all the dealer info attributes
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'provider': false // Boolean | boolean param to include site providers name in response
};
apiInstance.dealerCarUkIdGet(id, opts, (error, data, response) => {
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
 **id** | **String**| Dealer id to get all the dealer info attributes | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **provider** | **Boolean**| boolean param to include site providers name in response | [optional] [default to false]

### Return type

[**Dealer**](Dealer.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dealerHeavyEquipmentIdGet

> Dealer dealerHeavyEquipmentIdGet(id, opts)

Dealer by id

Get a particular dealer&#39;s information by its id

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.DealerAPIApi();
let id = "id_example"; // String | Dealer id to get all the dealer info attributes
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'provider': false // Boolean | boolean param to include site providers name in response
};
apiInstance.dealerHeavyEquipmentIdGet(id, opts, (error, data, response) => {
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
 **id** | **String**| Dealer id to get all the dealer info attributes | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **provider** | **Boolean**| boolean param to include site providers name in response | [optional] [default to false]

### Return type

[**Dealer**](Dealer.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dealerMotorcycleIdGet

> Dealer dealerMotorcycleIdGet(id, opts)

Dealer by id

Get a particular dealer&#39;s information by its id

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.DealerAPIApi();
let id = "id_example"; // String | Dealer id to get all the dealer info attributes
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'provider': false // Boolean | boolean param to include site providers name in response
};
apiInstance.dealerMotorcycleIdGet(id, opts, (error, data, response) => {
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
 **id** | **String**| Dealer id to get all the dealer info attributes | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **provider** | **Boolean**| boolean param to include site providers name in response | [optional] [default to false]

### Return type

[**Dealer**](Dealer.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dealerRvIdGet

> Dealer dealerRvIdGet(id, opts)

Dealer by id

Get a particular dealer&#39;s information by its id

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.DealerAPIApi();
let id = "id_example"; // String | Dealer id to get all the dealer info attributes
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'provider': false // Boolean | boolean param to include site providers name in response
};
apiInstance.dealerRvIdGet(id, opts, (error, data, response) => {
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
 **id** | **String**| Dealer id to get all the dealer info attributes | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **provider** | **Boolean**| boolean param to include site providers name in response | [optional] [default to false]

### Return type

[**Dealer**](Dealer.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dealerSearch

> DealersResponse dealerSearch(opts)

Find car dealers around

The dealers API returns a list of dealers around a given point and radius.

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.DealerAPIApi();
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'latitude': 3.4, // Number | Latitude component of location
  'longitude': 3.4, // Number | Longitude component of location
  'radius': 56, // Number | Radius around the search location (Unit - Miles)
  'rows': 10, // Number | Number of results to return. Default is 10. Max is 50
  'start': 0, // Number | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
  'country': "country_example", // String | To filter listing on Country in which they are listed
  'dealerType': "dealerType_example", // String | Filter based on dealer type independant or franchise
  'city': "city_example", // String | To filter listing on City in which they are listed
  'state': "state_example", // String | To filter listing on State in which they are listed
  'listingCountRange': "listingCountRange_example", // String | To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100
  'inventoryUrl': "inventoryUrl_example", // String | inventory_url of dealer to be searched
  'zip': "zip_example", // String | To filter listing on ZIP around which they are listed
  'sortBy': "sortBy_example", // String | Sort by field. Default sort field is distance from the given point
  'sortOrder': "sortOrder_example", // String | Sort order - asc or desc. Default sort order is asc
  'provider': false, // Boolean | boolean param to include site providers name in response
  'facets': "facets_example", // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
  'rangeFacets': "rangeFacets_example" // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
};
apiInstance.dealerSearch(opts, (error, data, response) => {
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
 **latitude** | **Number**| Latitude component of location | [optional] 
 **longitude** | **Number**| Longitude component of location | [optional] 
 **radius** | **Number**| Radius around the search location (Unit - Miles) | [optional] 
 **rows** | **Number**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10]
 **start** | **Number**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0]
 **country** | **String**| To filter listing on Country in which they are listed | [optional] 
 **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] 
 **city** | **String**| To filter listing on City in which they are listed | [optional] 
 **state** | **String**| To filter listing on State in which they are listed | [optional] 
 **listingCountRange** | **String**| To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100 | [optional] 
 **inventoryUrl** | **String**| inventory_url of dealer to be searched | [optional] 
 **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] 
 **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] 
 **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] 
 **provider** | **Boolean**| boolean param to include site providers name in response | [optional] [default to false]
 **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] 
 **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] 

### Return type

[**DealersResponse**](DealersResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dealersCarUkGet

> DealersResponse dealersCarUkGet(opts)

Find car dealers around

The dealers API returns a list of dealers around a given point and radius.

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.DealerAPIApi();
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'latitude': 3.4, // Number | Latitude component of location
  'longitude': 3.4, // Number | Longitude component of location
  'radius': 56, // Number | Radius around the search location (Unit - Miles)
  'rows': 10, // Number | Number of results to return. Default is 10. Max is 50
  'start': 0, // Number | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
  'country': "country_example", // String | To filter listing on Country in which they are listed
  'dealerType': "dealerType_example", // String | Filter based on dealer type independant or franchise
  'city': "city_example", // String | To filter listing on City in which they are listed
  'county': "county_example", // String | To filter listing on county in which they are listed
  'listingCountRange': "listingCountRange_example", // String | To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100
  'inventoryUrl': "inventoryUrl_example", // String | inventory_url of dealer to be searched
  'postalCode': "postalCode_example", // String | To filter listing on postal code around which they are listed
  'sortBy': "sortBy_example", // String | Sort by field. Default sort field is distance from the given point
  'sortOrder': "sortOrder_example", // String | Sort order - asc or desc. Default sort order is asc
  'provider': false, // Boolean | boolean param to include site providers name in response
  'facets': "facets_example", // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
  'rangeFacets': "rangeFacets_example" // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
};
apiInstance.dealersCarUkGet(opts, (error, data, response) => {
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
 **latitude** | **Number**| Latitude component of location | [optional] 
 **longitude** | **Number**| Longitude component of location | [optional] 
 **radius** | **Number**| Radius around the search location (Unit - Miles) | [optional] 
 **rows** | **Number**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10]
 **start** | **Number**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0]
 **country** | **String**| To filter listing on Country in which they are listed | [optional] 
 **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] 
 **city** | **String**| To filter listing on City in which they are listed | [optional] 
 **county** | **String**| To filter listing on county in which they are listed | [optional] 
 **listingCountRange** | **String**| To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100 | [optional] 
 **inventoryUrl** | **String**| inventory_url of dealer to be searched | [optional] 
 **postalCode** | **String**| To filter listing on postal code around which they are listed | [optional] 
 **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] 
 **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] 
 **provider** | **Boolean**| boolean param to include site providers name in response | [optional] [default to false]
 **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] 
 **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] 

### Return type

[**DealersResponse**](DealersResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dealersHeavyEquipmentGet

> DealersResponse dealersHeavyEquipmentGet(opts)

Find car dealers around

The dealers API returns a list of dealers around a given point and radius.

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.DealerAPIApi();
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'latitude': 3.4, // Number | Latitude component of location
  'longitude': 3.4, // Number | Longitude component of location
  'radius': 56, // Number | Radius around the search location (Unit - Miles)
  'rows': 10, // Number | Number of results to return. Default is 10. Max is 50
  'start': 0, // Number | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
  'country': "country_example", // String | To filter listing on Country in which they are listed
  'dealerType': "dealerType_example", // String | Filter based on dealer type independant or franchise
  'city': "city_example", // String | To filter listing on City in which they are listed
  'state': "state_example", // String | To filter listing on State in which they are listed
  'listingCountRange': "listingCountRange_example", // String | To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100
  'inventoryUrl': "inventoryUrl_example", // String | inventory_url of dealer to be searched
  'zip': "zip_example", // String | To filter listing on ZIP around which they are listed
  'sortBy': "sortBy_example", // String | Sort by field. Default sort field is distance from the given point
  'sortOrder': "sortOrder_example", // String | Sort order - asc or desc. Default sort order is asc
  'provider': false, // Boolean | boolean param to include site providers name in response
  'facets': "facets_example", // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
  'rangeFacets': "rangeFacets_example" // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
};
apiInstance.dealersHeavyEquipmentGet(opts, (error, data, response) => {
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
 **latitude** | **Number**| Latitude component of location | [optional] 
 **longitude** | **Number**| Longitude component of location | [optional] 
 **radius** | **Number**| Radius around the search location (Unit - Miles) | [optional] 
 **rows** | **Number**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10]
 **start** | **Number**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0]
 **country** | **String**| To filter listing on Country in which they are listed | [optional] 
 **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] 
 **city** | **String**| To filter listing on City in which they are listed | [optional] 
 **state** | **String**| To filter listing on State in which they are listed | [optional] 
 **listingCountRange** | **String**| To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100 | [optional] 
 **inventoryUrl** | **String**| inventory_url of dealer to be searched | [optional] 
 **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] 
 **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] 
 **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] 
 **provider** | **Boolean**| boolean param to include site providers name in response | [optional] [default to false]
 **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] 
 **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] 

### Return type

[**DealersResponse**](DealersResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dealersMotorcycleGet

> DealersResponse dealersMotorcycleGet(opts)

Find car dealers around

The dealers API returns a list of dealers around a given point and radius.

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.DealerAPIApi();
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'latitude': 3.4, // Number | Latitude component of location
  'longitude': 3.4, // Number | Longitude component of location
  'radius': 56, // Number | Radius around the search location (Unit - Miles)
  'rows': 10, // Number | Number of results to return. Default is 10. Max is 50
  'start': 0, // Number | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
  'country': "country_example", // String | To filter listing on Country in which they are listed
  'dealerType': "dealerType_example", // String | Filter based on dealer type independant or franchise
  'city': "city_example", // String | To filter listing on City in which they are listed
  'state': "state_example", // String | To filter listing on State in which they are listed
  'listingCountRange': "listingCountRange_example", // String | To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100
  'inventoryUrl': "inventoryUrl_example", // String | inventory_url of dealer to be searched
  'zip': "zip_example", // String | To filter listing on ZIP around which they are listed
  'sortBy': "sortBy_example", // String | Sort by field. Default sort field is distance from the given point
  'sortOrder': "sortOrder_example", // String | Sort order - asc or desc. Default sort order is asc
  'provider': false, // Boolean | boolean param to include site providers name in response
  'facets': "facets_example", // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
  'rangeFacets': "rangeFacets_example" // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
};
apiInstance.dealersMotorcycleGet(opts, (error, data, response) => {
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
 **latitude** | **Number**| Latitude component of location | [optional] 
 **longitude** | **Number**| Longitude component of location | [optional] 
 **radius** | **Number**| Radius around the search location (Unit - Miles) | [optional] 
 **rows** | **Number**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10]
 **start** | **Number**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0]
 **country** | **String**| To filter listing on Country in which they are listed | [optional] 
 **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] 
 **city** | **String**| To filter listing on City in which they are listed | [optional] 
 **state** | **String**| To filter listing on State in which they are listed | [optional] 
 **listingCountRange** | **String**| To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100 | [optional] 
 **inventoryUrl** | **String**| inventory_url of dealer to be searched | [optional] 
 **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] 
 **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] 
 **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] 
 **provider** | **Boolean**| boolean param to include site providers name in response | [optional] [default to false]
 **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] 
 **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] 

### Return type

[**DealersResponse**](DealersResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dealersRvGet

> DealersResponse dealersRvGet(opts)

Find car dealers around

The dealers API returns a list of dealers around a given point and radius.

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.DealerAPIApi();
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'latitude': 3.4, // Number | Latitude component of location
  'longitude': 3.4, // Number | Longitude component of location
  'radius': 56, // Number | Radius around the search location (Unit - Miles)
  'rows': 10, // Number | Number of results to return. Default is 10. Max is 50
  'start': 0, // Number | Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows
  'country': "country_example", // String | To filter listing on Country in which they are listed
  'dealerType': "dealerType_example", // String | Filter based on dealer type independant or franchise
  'city': "city_example", // String | To filter listing on City in which they are listed
  'state': "state_example", // String | To filter listing on State in which they are listed
  'listingCountRange': "listingCountRange_example", // String | To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100
  'inventoryUrl': "inventoryUrl_example", // String | inventory_url of dealer to be searched
  'zip': "zip_example", // String | To filter listing on ZIP around which they are listed
  'sortBy': "sortBy_example", // String | Sort by field. Default sort field is distance from the given point
  'sortOrder': "sortOrder_example", // String | Sort order - asc or desc. Default sort order is asc
  'provider': false, // Boolean | boolean param to include site providers name in response
  'facets': "facets_example", // String | The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond.
  'rangeFacets': "rangeFacets_example" // String | The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond.
};
apiInstance.dealersRvGet(opts, (error, data, response) => {
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
 **latitude** | **Number**| Latitude component of location | [optional] 
 **longitude** | **Number**| Longitude component of location | [optional] 
 **radius** | **Number**| Radius around the search location (Unit - Miles) | [optional] 
 **rows** | **Number**| Number of results to return. Default is 10. Max is 50 | [optional] [default to 10]
 **start** | **Number**| Page number to fetch the results for the given criteria. Default is 0. Pagination is allowed only till first 10000 results for the search and sort criteria. The page value can be only between 1 to 10000/rows | [optional] [default to 0]
 **country** | **String**| To filter listing on Country in which they are listed | [optional] 
 **dealerType** | **String**| Filter based on dealer type independant or franchise | [optional] 
 **city** | **String**| To filter listing on City in which they are listed | [optional] 
 **state** | **String**| To filter listing on State in which they are listed | [optional] 
 **listingCountRange** | **String**| To filter dealers based on their inventory size. Range can be given in the format - min-max e.g. 50-100 | [optional] 
 **inventoryUrl** | **String**| inventory_url of dealer to be searched | [optional] 
 **zip** | **String**| To filter listing on ZIP around which they are listed | [optional] 
 **sortBy** | **String**| Sort by field. Default sort field is distance from the given point | [optional] 
 **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] 
 **provider** | **Boolean**| boolean param to include site providers name in response | [optional] [default to false]
 **facets** | **String**| The comma separated list of fields for which facets are requested. Facets could be requested in addition to the listings for the search. Please note - The API calls with lots of facet fields may take longer to respond. | [optional] 
 **rangeFacets** | **String**| The comma separated list of numeric fields for which range facets are requested. Range facets could be requested in addition to the listings for the search. Please note - The API calls with lots of range facet fields may take longer to respond. | [optional] 

### Return type

[**DealersResponse**](DealersResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDealer

> Dealer getDealer(id, opts)

Dealer by id

Get a particular dealer&#39;s information by its id

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.DealerAPIApi();
let id = "id_example"; // String | Dealer id to get all the dealer info attributes
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'provider': false // Boolean | boolean param to include site providers name in response
};
apiInstance.getDealer(id, opts, (error, data, response) => {
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
 **id** | **String**| Dealer id to get all the dealer info attributes | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **provider** | **Boolean**| boolean param to include site providers name in response | [optional] [default to false]

### Return type

[**Dealer**](Dealer.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

