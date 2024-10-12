# GeodesystemsCom443.TypeTypePointGeomagIaga2002Api

All URIs are relative to *https://geodesystems.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchTypePointGeomagIaga2002**](TypeTypePointGeomagIaga2002Api.md#searchTypePointGeomagIaga2002) | **GET** /repository/search/type/type_point_geomag_iaga2002 | Search API for &#39;IAGA 2002 Geomagnetism Data&#39; entry type



## searchTypePointGeomagIaga2002

> searchTypePointGeomagIaga2002(opts)

Search API for &#39;IAGA 2002 Geomagnetism Data&#39; entry type

API to search for entries of type IAGA 2002 Geomagnetism Data

### Example

```javascript
import GeodesystemsCom443 from 'geodesystems_com443';

let apiInstance = new GeodesystemsCom443.TypeTypePointGeomagIaga2002Api();
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
  'searchTypePointGeomagIaga2002IagaCode': "searchTypePointGeomagIaga2002IagaCode_example", // String | IAGA Code
  'searchTypePointGeomagIaga2002StationName': "searchTypePointGeomagIaga2002StationName_example", // String | Station Name
  'searchTypePointGeomagIaga2002SourceOfData': "searchTypePointGeomagIaga2002SourceOfData_example", // String | Source of data
  'searchTypePointGeomagIaga2002DigitalSampling': "searchTypePointGeomagIaga2002DigitalSampling_example", // String | Digital Sampling
  'searchTypePointGeomagIaga2002DataInterval': "searchTypePointGeomagIaga2002DataInterval_example", // String | Data Interval
  'searchTypePointGeomagIaga2002DataType': "searchTypePointGeomagIaga2002DataType_example" // String | Data Type
};
apiInstance.searchTypePointGeomagIaga2002(opts, (error, data, response) => {
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
 **searchTypePointGeomagIaga2002IagaCode** | **String**| IAGA Code | [optional] 
 **searchTypePointGeomagIaga2002StationName** | **String**| Station Name | [optional] 
 **searchTypePointGeomagIaga2002SourceOfData** | **String**| Source of data | [optional] 
 **searchTypePointGeomagIaga2002DigitalSampling** | **String**| Digital Sampling | [optional] 
 **searchTypePointGeomagIaga2002DataInterval** | **String**| Data Interval | [optional] 
 **searchTypePointGeomagIaga2002DataType** | **String**| Data Type | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

