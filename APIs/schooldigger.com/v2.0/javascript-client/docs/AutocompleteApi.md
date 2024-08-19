# SchoolDiggerApiV20.AutocompleteApi

All URIs are relative to *https://api.schooldigger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocompleteGetSchools**](AutocompleteApi.md#autocompleteGetSchools) | **GET** /v2.0/autocomplete/schools | Returns a simple and quick list of schools for use in a client-typed autocomplete



## autocompleteGetSchools

> APIAutocompleteSchoolResult autocompleteGetSchools(appID, appKey, opts)

Returns a simple and quick list of schools for use in a client-typed autocomplete

### Example

```javascript
import SchoolDiggerApiV20 from 'school_digger_api_v2_0';

let apiInstance = new SchoolDiggerApiV20.AutocompleteApi();
let appID = "appID_example"; // String | Your API app id
let appKey = "appKey_example"; // String | Your API app key
let opts = {
  'q': "q_example", // String | Search term for autocomplete (e.g. 'Lincol') (required)
  'qSearchCityStateName': true, // Boolean | Extend the search term to include city and state (e.g. 'Lincoln el paso' matches Lincoln Middle School in El Paso) (optional)
  'st': "st_example", // String | Two character state (e.g. 'CA') (optional -- leave blank to search entire U.S.)
  'level': "level_example", // String | Search for schools at this level only. Valid values: 'Elementary', 'Middle', 'High', 'Alt', 'Private' (optional - leave blank to search for all schools)
  'boxLatitudeNW': 3.4, // Number | Search within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.)
  'boxLongitudeNW': 3.4, // Number | Search within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.)
  'boxLatitudeSE': 3.4, // Number | Search within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.)
  'boxLongitudeSE': 3.4, // Number | Search within a 'box' defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.)
  'returnCount': 56 // Number | Number of schools to return. Valid values: 1-20. (default: 10)
};
apiInstance.autocompleteGetSchools(appID, appKey, opts, (error, data, response) => {
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
 **appID** | **String**| Your API app id | 
 **appKey** | **String**| Your API app key | 
 **q** | **String**| Search term for autocomplete (e.g. &#39;Lincol&#39;) (required) | [optional] 
 **qSearchCityStateName** | **Boolean**| Extend the search term to include city and state (e.g. &#39;Lincoln el paso&#39; matches Lincoln Middle School in El Paso) (optional) | [optional] 
 **st** | **String**| Two character state (e.g. &#39;CA&#39;) (optional -- leave blank to search entire U.S.) | [optional] 
 **level** | **String**| Search for schools at this level only. Valid values: &#39;Elementary&#39;, &#39;Middle&#39;, &#39;High&#39;, &#39;Alt&#39;, &#39;Private&#39; (optional - leave blank to search for all schools) | [optional] 
 **boxLatitudeNW** | **Number**| Search within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.) | [optional] 
 **boxLongitudeNW** | **Number**| Search within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.) | [optional] 
 **boxLatitudeSE** | **Number**| Search within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.) | [optional] 
 **boxLongitudeSE** | **Number**| Search within a &#39;box&#39; defined by (BoxLatitudeNW/BoxLongitudeNW) to (BoxLongitudeSE/BoxLatitudeSE) (optional. Pro, Enterprise API levels only.) | [optional] 
 **returnCount** | **Number**| Number of schools to return. Valid values: 1-20. (default: 10) | [optional] 

### Return type

[**APIAutocompleteSchoolResult**](APIAutocompleteSchoolResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

