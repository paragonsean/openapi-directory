# SchoolDiggerApiV1.SchoolsApi

All URIs are relative to *https://api.schooldigger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schoolsGetAllSchools**](SchoolsApi.md#schoolsGetAllSchools) | **GET** /v1/schools | Returns a list of schools
[**schoolsGetSchool10**](SchoolsApi.md#schoolsGetSchool10) | **GET** /v1/schools/{id} | Returns a detailed record for one school



## schoolsGetAllSchools

> APISchoolList schoolsGetAllSchools(st, appID, appKey, opts)

Returns a list of schools

Search the SchoolDigger database for schools. You may use any combination of criteria as query parameters.

### Example

```javascript
import SchoolDiggerApiV1 from 'school_digger_api_v1';

let apiInstance = new SchoolDiggerApiV1.SchoolsApi();
let st = "st_example"; // String | Two character state (e.g. 'CA') - required
let appID = "appID_example"; // String | Your API app id
let appKey = "appKey_example"; // String | Your API app key
let opts = {
  'q': "q_example", // String | Search term - note: will match school name or city (optional)
  'qSearchSchoolNameOnly': true, // Boolean | For parameter 'q', only search school names instead of school and city (optional)
  'districtID': "districtID_example", // String | Search for schools within this district (7 digit district id) (optional)
  'level': "level_example", // String | Search for schools at this level. Valid values: 'Elementary', 'Middle', 'High', 'Alt', 'Public', 'Private' (optional). 'Public' returns all Elementary, Middle, High and Alternative schools
  'city': "city_example", // String | Search for schools in this city (optional)
  'zip': "zip_example", // String | Search for schools in this 5-digit zip code (optional)
  'isMagnet': true, // Boolean | True = return only magnet schools, False = return only non-magnet schools (optional) (Pro, Enterprise API levels only)
  'isCharter': true, // Boolean | True = return only charter schools, False = return only non-charter schools (optional) (Pro, Enterprise API levels only)
  'isVirtual': true, // Boolean | True = return only virtual schools, False = return only non-virtual schools (optional) (Pro, Enterprise API levels only)
  'isTitleI': true, // Boolean | True = return only Title I schools, False = return only non-Title I schools (optional) (Pro, Enterprise API levels only)
  'isTitleISchoolwide': true, // Boolean | True = return only Title I school-wide schools, False = return only non-Title I school-wide schools (optional) (Pro, Enterprise API levels only)
  'nearLatitude': 3.4, // Number | Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. 44.982560) (optional) (Pro, Enterprise API levels only. Enterprise API level will flag schools that include lat/long in its attendance boundary.)
  'nearLongitude': 3.4, // Number | Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. -124.289185) (optional) (Pro, Enterprise API levels only. Enterprise API level will flag schools that include lat/long in its attendance boundary.)
  'boundaryAddress': "boundaryAddress_example", // String | Full U.S. address: flag returned schools that include this address in its attendance boundary. Example: '123 Main St. AnyTown CA 90001' (optional) (Enterprise API level only) IMPORTANT NOTE: If you have the lat/long of the address, use nearLatitude and nearLongitude instead for much faster response times
  'distanceMiles': 56, // Number | Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (Default 5 miles) (optional) (Pro, Enterprise API levels only)
  'isInBoundaryOnly': true, // Boolean | Return only the schools that include given location (nearLatitude/nearLongitude) or (boundaryAddress) in its attendance boundary (Enterprise API level only)
  'boxLatitudeNW': 3.4, // Number | Search for schools within a 'box' defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional)
  'boxLongitudeNW': 3.4, // Number | Search for schools within a 'box' defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional)
  'boxLatitudeSE': 3.4, // Number | Search for schools within a 'box' defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional)
  'boxLongitudeSE': 3.4, // Number | Search for schools within a 'box' defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional)
  'page': 56, // Number | Page number to retrieve (optional, default: 1)
  'perPage': 56, // Number | Number of schools to retrieve on a page (50 max) (optional, default: 10)
  'sortBy': "sortBy_example", // String | Sort list. Values are: schoolname, distance, rank. For descending order, precede with '-' i.e. -schoolname (optional, default: schoolname)
  'includeUnrankedSchoolsInRankSort': true // Boolean | If sortBy is 'rank', this boolean determines if schools with no rank are included in the result (optional, default: false)
};
apiInstance.schoolsGetAllSchools(st, appID, appKey, opts, (error, data, response) => {
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
 **q** | **String**| Search term - note: will match school name or city (optional) | [optional] 
 **qSearchSchoolNameOnly** | **Boolean**| For parameter &#39;q&#39;, only search school names instead of school and city (optional) | [optional] 
 **districtID** | **String**| Search for schools within this district (7 digit district id) (optional) | [optional] 
 **level** | **String**| Search for schools at this level. Valid values: &#39;Elementary&#39;, &#39;Middle&#39;, &#39;High&#39;, &#39;Alt&#39;, &#39;Public&#39;, &#39;Private&#39; (optional). &#39;Public&#39; returns all Elementary, Middle, High and Alternative schools | [optional] 
 **city** | **String**| Search for schools in this city (optional) | [optional] 
 **zip** | **String**| Search for schools in this 5-digit zip code (optional) | [optional] 
 **isMagnet** | **Boolean**| True &#x3D; return only magnet schools, False &#x3D; return only non-magnet schools (optional) (Pro, Enterprise API levels only) | [optional] 
 **isCharter** | **Boolean**| True &#x3D; return only charter schools, False &#x3D; return only non-charter schools (optional) (Pro, Enterprise API levels only) | [optional] 
 **isVirtual** | **Boolean**| True &#x3D; return only virtual schools, False &#x3D; return only non-virtual schools (optional) (Pro, Enterprise API levels only) | [optional] 
 **isTitleI** | **Boolean**| True &#x3D; return only Title I schools, False &#x3D; return only non-Title I schools (optional) (Pro, Enterprise API levels only) | [optional] 
 **isTitleISchoolwide** | **Boolean**| True &#x3D; return only Title I school-wide schools, False &#x3D; return only non-Title I school-wide schools (optional) (Pro, Enterprise API levels only) | [optional] 
 **nearLatitude** | **Number**| Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. 44.982560) (optional) (Pro, Enterprise API levels only. Enterprise API level will flag schools that include lat/long in its attendance boundary.) | [optional] 
 **nearLongitude** | **Number**| Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (e.g. -124.289185) (optional) (Pro, Enterprise API levels only. Enterprise API level will flag schools that include lat/long in its attendance boundary.) | [optional] 
 **boundaryAddress** | **String**| Full U.S. address: flag returned schools that include this address in its attendance boundary. Example: &#39;123 Main St. AnyTown CA 90001&#39; (optional) (Enterprise API level only) IMPORTANT NOTE: If you have the lat/long of the address, use nearLatitude and nearLongitude instead for much faster response times | [optional] 
 **distanceMiles** | **Number**| Search for schools within (distanceMiles) of (nearLatitude)/(nearLongitude) (Default 5 miles) (optional) (Pro, Enterprise API levels only) | [optional] 
 **isInBoundaryOnly** | **Boolean**| Return only the schools that include given location (nearLatitude/nearLongitude) or (boundaryAddress) in its attendance boundary (Enterprise API level only) | [optional] 
 **boxLatitudeNW** | **Number**| Search for schools within a &#39;box&#39; defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional) | [optional] 
 **boxLongitudeNW** | **Number**| Search for schools within a &#39;box&#39; defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional) | [optional] 
 **boxLatitudeSE** | **Number**| Search for schools within a &#39;box&#39; defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional) | [optional] 
 **boxLongitudeSE** | **Number**| Search for schools within a &#39;box&#39; defined by (boxLatitudeNW/boxLongitudeNW) to (boxLongitudeSE/boxLatitudeSE) (optional) | [optional] 
 **page** | **Number**| Page number to retrieve (optional, default: 1) | [optional] 
 **perPage** | **Number**| Number of schools to retrieve on a page (50 max) (optional, default: 10) | [optional] 
 **sortBy** | **String**| Sort list. Values are: schoolname, distance, rank. For descending order, precede with &#39;-&#39; i.e. -schoolname (optional, default: schoolname) | [optional] 
 **includeUnrankedSchoolsInRankSort** | **Boolean**| If sortBy is &#39;rank&#39;, this boolean determines if schools with no rank are included in the result (optional, default: false) | [optional] 

### Return type

[**APISchoolList**](APISchoolList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schoolsGetSchool10

> APISchool10Full schoolsGetSchool10(id, appID, appKey)

Returns a detailed record for one school

Retrieve a school record from the SchoolDigger database

### Example

```javascript
import SchoolDiggerApiV1 from 'school_digger_api_v1';

let apiInstance = new SchoolDiggerApiV1.SchoolsApi();
let id = "id_example"; // String | The 12 digit School ID (e.g. 064215006903)
let appID = "appID_example"; // String | Your API app id
let appKey = "appKey_example"; // String | Your API app key
apiInstance.schoolsGetSchool10(id, appID, appKey, (error, data, response) => {
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
 **id** | **String**| The 12 digit School ID (e.g. 064215006903) | 
 **appID** | **String**| Your API app id | 
 **appKey** | **String**| Your API app key | 

### Return type

[**APISchool10Full**](APISchool10Full.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

