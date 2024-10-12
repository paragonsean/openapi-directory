# GeodesystemsCom443.TypeGazeteerCountiesApi

All URIs are relative to *https://geodesystems.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchGazeteerCounties**](TypeGazeteerCountiesApi.md#searchGazeteerCounties) | **GET** /repository/search/type/gazeteer_counties | Search API for &#39;Census Gazeteer Counties&#39; entry type



## searchGazeteerCounties

> searchGazeteerCounties(opts)

Search API for &#39;Census Gazeteer Counties&#39; entry type

API to search for entries of type Census Gazeteer Counties

### Example

```javascript
import GeodesystemsCom443 from 'geodesystems_com443';

let apiInstance = new GeodesystemsCom443.TypeGazeteerCountiesApi();
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
  'searchDbGazeteerCountiesStateAbbreviation': "searchDbGazeteerCountiesStateAbbreviation_example", // String | State Abbreviation
  'searchDbGazeteerCountiesStateFips': "searchDbGazeteerCountiesStateFips_example", // String | State Fips
  'searchDbGazeteerCountiesCountyFips': "searchDbGazeteerCountiesCountyFips_example", // String | County Fips
  'searchDbGazeteerCountiesFullCountyFips': "searchDbGazeteerCountiesFullCountyFips_example", // String | Full County Fips
  'searchDbGazeteerCountiesCountyName': "searchDbGazeteerCountiesCountyName_example", // String | County Name
  'searchDbGazeteerCountiesAreaLand': 3.4, // Number | Area Land
  'searchDbGazeteerCountiesAreaWater': 3.4, // Number | Area Water
  'searchDbGazeteerCountiesLocation': "searchDbGazeteerCountiesLocation_example" // String | Location
};
apiInstance.searchGazeteerCounties(opts, (error, data, response) => {
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
 **searchDbGazeteerCountiesStateAbbreviation** | **String**| State Abbreviation | [optional] 
 **searchDbGazeteerCountiesStateFips** | **String**| State Fips | [optional] 
 **searchDbGazeteerCountiesCountyFips** | **String**| County Fips | [optional] 
 **searchDbGazeteerCountiesFullCountyFips** | **String**| Full County Fips | [optional] 
 **searchDbGazeteerCountiesCountyName** | **String**| County Name | [optional] 
 **searchDbGazeteerCountiesAreaLand** | **Number**| Area Land | [optional] 
 **searchDbGazeteerCountiesAreaWater** | **Number**| Area Water | [optional] 
 **searchDbGazeteerCountiesLocation** | **String**| Location | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

