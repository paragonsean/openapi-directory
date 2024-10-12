# GeodesystemsCom443.TypePropertydbApi

All URIs are relative to *https://geodesystems.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchPropertydb**](TypePropertydbApi.md#searchPropertydb) | **GET** /repository/search/type/propertydb | Search API for &#39;Property Database&#39; entry type



## searchPropertydb

> searchPropertydb(opts)

Search API for &#39;Property Database&#39; entry type

API to search for entries of type Property Database

### Example

```javascript
import GeodesystemsCom443 from 'geodesystems_com443';

let apiInstance = new GeodesystemsCom443.TypePropertydbApi();
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
  'searchDbPropertydbPropertyId': "searchDbPropertydbPropertyId_example", // String | Property ID
  'searchDbPropertydbOwner': "searchDbPropertydbOwner_example", // String | Owner
  'searchDbPropertydbAddress': "searchDbPropertydbAddress_example", // String | Address
  'searchDbPropertydbCity': "searchDbPropertydbCity_example", // String | City
  'searchDbPropertydbState': "searchDbPropertydbState_example", // String | State
  'searchDbPropertydbValue': 56, // Number | Property Value
  'searchDbPropertydbBuildingType': "searchDbPropertydbBuildingType_example", // String | Building Type
  'searchDbPropertydbHouseSize': 56, // Number | Building Sq Ft
  'searchDbPropertydbLotSqft': 56, // Number | Lot Size Sq Ft
  'searchDbPropertydbLotAcres': 3.4, // Number | Lot Size Acres
  'searchDbPropertydbPriceSqft': 3.4, // Number | $-sqft
  'searchDbPropertydbLocation': "searchDbPropertydbLocation_example" // String | Location
};
apiInstance.searchPropertydb(opts, (error, data, response) => {
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
 **searchDbPropertydbPropertyId** | **String**| Property ID | [optional] 
 **searchDbPropertydbOwner** | **String**| Owner | [optional] 
 **searchDbPropertydbAddress** | **String**| Address | [optional] 
 **searchDbPropertydbCity** | **String**| City | [optional] 
 **searchDbPropertydbState** | **String**| State | [optional] 
 **searchDbPropertydbValue** | **Number**| Property Value | [optional] 
 **searchDbPropertydbBuildingType** | **String**| Building Type | [optional] 
 **searchDbPropertydbHouseSize** | **Number**| Building Sq Ft | [optional] 
 **searchDbPropertydbLotSqft** | **Number**| Lot Size Sq Ft | [optional] 
 **searchDbPropertydbLotAcres** | **Number**| Lot Size Acres | [optional] 
 **searchDbPropertydbPriceSqft** | **Number**| $-sqft | [optional] 
 **searchDbPropertydbLocation** | **String**| Location | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

