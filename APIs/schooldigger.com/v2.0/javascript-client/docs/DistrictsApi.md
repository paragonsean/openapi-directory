# SchoolDiggerApiV20.DistrictsApi

All URIs are relative to *https://api.schooldigger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**districtsGetAllDistricts2**](DistrictsApi.md#districtsGetAllDistricts2) | **GET** /v2.0/districts | Returns a list of districts
[**districtsGetDistrict2**](DistrictsApi.md#districtsGetDistrict2) | **GET** /v2.0/districts/{id} | Returns a detailed record for one district



## districtsGetAllDistricts2

> APIDistrictList2 districtsGetAllDistricts2(st, appID, appKey, opts)

Returns a list of districts

Search the SchoolDigger database for districts. You may use any combination of criteria as query parameters.

### Example

```javascript
import SchoolDiggerApiV20 from 'school_digger_api_v2_0';

let apiInstance = new SchoolDiggerApiV20.DistrictsApi();
let st = "st_example"; // String | Two character state (e.g. 'CA') - required
let appID = "appID_example"; // String | Your API app id
let appKey = "appKey_example"; // String | Your API app key
let opts = {
  'q': "q_example", // String | Search term - note: will match district name or city (optional)
  'city': "city_example", // String | Search for districts in this city (optional)
  'zip': "zip_example", // String | Search for districts in this 5-digit zip code (optional)
  'nearLatitude': 3.4, // Number | Search for districts within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. 44.982560) (optional) (Pro, Enterprise API levels only. Enterprise API level will flag districts that include lat/long in its attendance boundary.)
  'nearLongitude': 3.4, // Number | Search for districts within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. -124.289185) (optional) (Pro, Enterprise API levels only. Enterprise API level will flag districts that include lat/long in its attendance boundary.)
  'boundaryAddress': "boundaryAddress_example", // String | Full U.S. address: flag returned districts that include this address in its attendance boundary. Example: '123 Main St. AnyTown CA 90001' (optional) (Enterprise API level only)
  'distanceMiles': 56, // Number | Search for districts within (distanceMiles) of (nearLatitude)/(nearLongitude) (Default 50 miles) (optional) (Pro, Enterprise API levels only)
  'isInBoundaryOnly': true, // Boolean | Return only the districts that include given location (nearLatitude/nearLongitude) or (boundaryAddress) in its attendance boundary (Enterprise API level only)
  'boxLatitudeNW': 3.4, // Number | Search for districts within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional)
  'boxLongitudeNW': 3.4, // Number | Search for districts within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional)
  'boxLatitudeSE': 3.4, // Number | Search for districts within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional)
  'boxLongitudeSE': 3.4, // Number | Search for districts within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional)
  'page': 56, // Number | Page number to retrieve (optional, default: 1)
  'perPage': 56, // Number | Number of districts to retrieve on a page (50 max) (optional, default: 10)
  'sortBy': "sortBy_example", // String | Sort list. Values are: districtname, distance, rank. For descending order, precede with '-' i.e. -districtname (optional, default: districtname)
  'includeUnrankedDistrictsInRankSort': true // Boolean | If sortBy is 'rank', this boolean determines if districts with no rank are included in the result (optional, default: false)
};
apiInstance.districtsGetAllDistricts2(st, appID, appKey, opts, (error, data, response) => {
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
 **st** | **String**| Two character state (e.g. &#39;CA&#39;) - required | 
 **appID** | **String**| Your API app id | 
 **appKey** | **String**| Your API app key | 
 **q** | **String**| Search term - note: will match district name or city (optional) | [optional] 
 **city** | **String**| Search for districts in this city (optional) | [optional] 
 **zip** | **String**| Search for districts in this 5-digit zip code (optional) | [optional] 
 **nearLatitude** | **Number**| Search for districts within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. 44.982560) (optional) (Pro, Enterprise API levels only. Enterprise API level will flag districts that include lat/long in its attendance boundary.) | [optional] 
 **nearLongitude** | **Number**| Search for districts within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. -124.289185) (optional) (Pro, Enterprise API levels only. Enterprise API level will flag districts that include lat/long in its attendance boundary.) | [optional] 
 **boundaryAddress** | **String**| Full U.S. address: flag returned districts that include this address in its attendance boundary. Example: &#39;123 Main St. AnyTown CA 90001&#39; (optional) (Enterprise API level only) | [optional] 
 **distanceMiles** | **Number**| Search for districts within (distanceMiles) of (nearLatitude)/(nearLongitude) (Default 50 miles) (optional) (Pro, Enterprise API levels only) | [optional] 
 **isInBoundaryOnly** | **Boolean**| Return only the districts that include given location (nearLatitude/nearLongitude) or (boundaryAddress) in its attendance boundary (Enterprise API level only) | [optional] 
 **boxLatitudeNW** | **Number**| Search for districts within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional) | [optional] 
 **boxLongitudeNW** | **Number**| Search for districts within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional) | [optional] 
 **boxLatitudeSE** | **Number**| Search for districts within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional) | [optional] 
 **boxLongitudeSE** | **Number**| Search for districts within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional) | [optional] 
 **page** | **Number**| Page number to retrieve (optional, default: 1) | [optional] 
 **perPage** | **Number**| Number of districts to retrieve on a page (50 max) (optional, default: 10) | [optional] 
 **sortBy** | **String**| Sort list. Values are: districtname, distance, rank. For descending order, precede with &#39;-&#39; i.e. -districtname (optional, default: districtname) | [optional] 
 **includeUnrankedDistrictsInRankSort** | **Boolean**| If sortBy is &#39;rank&#39;, this boolean determines if districts with no rank are included in the result (optional, default: false) | [optional] 

### Return type

[**APIDistrictList2**](APIDistrictList2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## districtsGetDistrict2

> APIDistrict12 districtsGetDistrict2(id, appID, appKey)

Returns a detailed record for one district

Retrieve a single district record from the SchoolDigger database

### Example

```javascript
import SchoolDiggerApiV20 from 'school_digger_api_v2_0';

let apiInstance = new SchoolDiggerApiV20.DistrictsApi();
let id = "id_example"; // String | The 7 digit District ID (e.g. 0642150)
let appID = "appID_example"; // String | Your API app id
let appKey = "appKey_example"; // String | Your API app key
apiInstance.districtsGetDistrict2(id, appID, appKey, (error, data, response) => {
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
 **id** | **String**| The 7 digit District ID (e.g. 0642150) | 
 **appID** | **String**| Your API app id | 
 **appKey** | **String**| Your API app key | 

### Return type

[**APIDistrict12**](APIDistrict12.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

