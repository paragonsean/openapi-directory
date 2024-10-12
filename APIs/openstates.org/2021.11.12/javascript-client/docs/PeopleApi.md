# OpenStatesApiV3.PeopleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**peopleGeoPeopleGeoGet**](PeopleApi.md#peopleGeoPeopleGeoGet) | **GET** /people.geo | People Geo
[**peopleSearchPeopleGet**](PeopleApi.md#peopleSearchPeopleGet) | **GET** /people | People Search



## peopleGeoPeopleGeoGet

> PersonList peopleGeoPeopleGeoGet(lat, lng, opts)

People Geo

Get list of people currently representing a given location.  **Note:** Currently limited to state legislators and US Congress.  Governors &amp; mayors are not included.

### Example

```javascript
import OpenStatesApiV3 from 'open_states_api_v3';

let apiInstance = new OpenStatesApiV3.PeopleApi();
let lat = 3.4; // Number | Latitude of point.
let lng = 3.4; // Number | Longitude of point.
let opts = {
  'include': [new OpenStatesApiV3.PersonInclude()], // [PersonInclude] | Additional information to include in the response.
  'apikey': "apikey_example", // String | 
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.peopleGeoPeopleGeoGet(lat, lng, opts, (error, data, response) => {
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
 **lat** | **Number**| Latitude of point. | 
 **lng** | **Number**| Longitude of point. | 
 **include** | [**[PersonInclude]**](PersonInclude.md)| Additional information to include in the response. | [optional] 
 **apikey** | **String**|  | [optional] 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**PersonList**](PersonList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## peopleSearchPeopleGet

> PersonList peopleSearchPeopleGet(opts)

People Search

Get list of people matching selected criteria.  Must provide either **jurisdiction**, **name**, or one or more **id** parameters.

### Example

```javascript
import OpenStatesApiV3 from 'open_states_api_v3';

let apiInstance = new OpenStatesApiV3.PeopleApi();
let opts = {
  'jurisdiction': "jurisdiction_example", // String | Filter by jurisdiction name or id.
  'name': "name_example", // String | Filter by name, case-insensitive match.
  'id': ["null"], // [String] | Filter by id, can be specified multiple times for multiple people.
  'orgClassification': new OpenStatesApiV3.OrgClassification(), // OrgClassification | Filter by current role.
  'district': "district_example", // String | Filter by district name.
  'include': [new OpenStatesApiV3.PersonInclude()], // [PersonInclude] | Additional information to include in response.
  'page': 1, // Number | 
  'perPage': 10, // Number | 
  'apikey': "apikey_example", // String | 
  'xApiKey': "xApiKey_example" // String | 
};
apiInstance.peopleSearchPeopleGet(opts, (error, data, response) => {
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
 **jurisdiction** | **String**| Filter by jurisdiction name or id. | [optional] 
 **name** | **String**| Filter by name, case-insensitive match. | [optional] 
 **id** | [**[String]**](String.md)| Filter by id, can be specified multiple times for multiple people. | [optional] 
 **orgClassification** | [**OrgClassification**](.md)| Filter by current role. | [optional] 
 **district** | **String**| Filter by district name. | [optional] 
 **include** | [**[PersonInclude]**](PersonInclude.md)| Additional information to include in response. | [optional] 
 **page** | **Number**|  | [optional] [default to 1]
 **perPage** | **Number**|  | [optional] [default to 10]
 **apikey** | **String**|  | [optional] 
 **xApiKey** | **String**|  | [optional] 

### Return type

[**PersonList**](PersonList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

