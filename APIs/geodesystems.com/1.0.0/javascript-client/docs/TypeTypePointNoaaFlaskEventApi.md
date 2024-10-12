# GeodesystemsCom443.TypeTypePointNoaaFlaskEventApi

All URIs are relative to *https://geodesystems.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchTypePointNoaaFlaskEvent**](TypeTypePointNoaaFlaskEventApi.md#searchTypePointNoaaFlaskEvent) | **GET** /repository/search/type/type_point_noaa_flask_event | Search API for &#39;NOAA Flask Event Measurements&#39; entry type



## searchTypePointNoaaFlaskEvent

> searchTypePointNoaaFlaskEvent(opts)

Search API for &#39;NOAA Flask Event Measurements&#39; entry type

API to search for entries of type NOAA Flask Event Measurements

### Example

```javascript
import GeodesystemsCom443 from 'geodesystems_com443';

let apiInstance = new GeodesystemsCom443.TypeTypePointNoaaFlaskEventApi();
let opts = {
  'text': "text_example", // String | Search text
  'name': "name_example", // String | Search name
  'description': "description_example", // String | Search description
  'fromdate': new Date("2013-10-20T19:20:30+01:00"), // Date | From date
  'todate': new Date("2013-10-20T19:20:30+01:00"), // Date | To date
  'createdateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Archive create date from
  'createdateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Archive create date to
  'changedateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Archive change date from
  'changedateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Archive change date to
  'group': "group_example", // String | Parent entry
  'filesuffix': "filesuffix_example", // String | File suffix
  'maxlatitude': 3.4, // Number | Northern bounds of search
  'minlongitude': 3.4, // Number | Western bounds of search
  'minlatitude': 3.4, // Number | Southern bounds of search
  'maxlongitude': 3.4, // Number | Eastern bounds of search
  'max': 56, // Number | Max number of results
  'skip': 56, // Number | Number to skip
  'searchTypePointNoaaFlaskEventSiteId': "searchTypePointNoaaFlaskEventSiteId_example", // String | Site ID
  'searchTypePointNoaaFlaskEventParameter': "searchTypePointNoaaFlaskEventParameter_example", // String | Parameter
  'searchTypePointNoaaFlaskEventProject': "searchTypePointNoaaFlaskEventProject_example", // String | Project
  'searchTypePointNoaaFlaskEventLabIdNumber': "searchTypePointNoaaFlaskEventLabIdNumber_example", // String | Lab ID Number
  'searchTypePointNoaaFlaskEventMeasurementGroup': "searchTypePointNoaaFlaskEventMeasurementGroup_example" // String | Measurement Group
};
apiInstance.searchTypePointNoaaFlaskEvent(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **String**| Search text | [optional] 
 **name** | **String**| Search name | [optional] 
 **description** | **String**| Search description | [optional] 
 **fromdate** | **Date**| From date | [optional] 
 **todate** | **Date**| To date | [optional] 
 **createdateFrom** | **Date**| Archive create date from | [optional] 
 **createdateTo** | **Date**| Archive create date to | [optional] 
 **changedateFrom** | **Date**| Archive change date from | [optional] 
 **changedateTo** | **Date**| Archive change date to | [optional] 
 **group** | **String**| Parent entry | [optional] 
 **filesuffix** | **String**| File suffix | [optional] 
 **maxlatitude** | **Number**| Northern bounds of search | [optional] 
 **minlongitude** | **Number**| Western bounds of search | [optional] 
 **minlatitude** | **Number**| Southern bounds of search | [optional] 
 **maxlongitude** | **Number**| Eastern bounds of search | [optional] 
 **max** | **Number**| Max number of results | [optional] 
 **skip** | **Number**| Number to skip | [optional] 
 **searchTypePointNoaaFlaskEventSiteId** | **String**| Site ID | [optional] 
 **searchTypePointNoaaFlaskEventParameter** | **String**| Parameter | [optional] 
 **searchTypePointNoaaFlaskEventProject** | **String**| Project | [optional] 
 **searchTypePointNoaaFlaskEventLabIdNumber** | **String**| Lab ID Number | [optional] 
 **searchTypePointNoaaFlaskEventMeasurementGroup** | **String**| Measurement Group | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

