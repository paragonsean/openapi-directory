# GeodesystemsCom443.TypeDbCoIndicatorsApi

All URIs are relative to *https://geodesystems.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchDbCoIndicators**](TypeDbCoIndicatorsApi.md#searchDbCoIndicators) | **GET** /repository/search/type/db_co_indicators | Search API for &#39;Colorado Health Indicators&#39; entry type



## searchDbCoIndicators

> searchDbCoIndicators(opts)

Search API for &#39;Colorado Health Indicators&#39; entry type

API to search for entries of type Colorado Health Indicators

### Example

```javascript
import GeodesystemsCom443 from 'geodesystems_com443';

let apiInstance = new GeodesystemsCom443.TypeDbCoIndicatorsApi();
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
  'searchDbDbCoIndicatorsGeoName': "searchDbDbCoIndicatorsGeoName_example", // String | County
  'searchDbDbCoIndicatorsDomain': "searchDbDbCoIndicatorsDomain_example", // String | Domain
  'searchDbDbCoIndicatorsSubdomain': "searchDbDbCoIndicatorsSubdomain_example", // String | Subdomain
  'searchDbDbCoIndicatorsIndicatorName': "searchDbDbCoIndicatorsIndicatorName_example", // String | Indicator
  'searchDbDbCoIndicatorsDescription': "searchDbDbCoIndicatorsDescription_example", // String | Description
  'searchDbDbCoIndicatorsMeasure': 3.4, // Number | Measure
  'searchDbDbCoIndicatorsLocation': "searchDbDbCoIndicatorsLocation_example" // String | Location
};
apiInstance.searchDbCoIndicators(opts, (error, data, response) => {
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
 **searchDbDbCoIndicatorsGeoName** | **String**| County | [optional] 
 **searchDbDbCoIndicatorsDomain** | **String**| Domain | [optional] 
 **searchDbDbCoIndicatorsSubdomain** | **String**| Subdomain | [optional] 
 **searchDbDbCoIndicatorsIndicatorName** | **String**| Indicator | [optional] 
 **searchDbDbCoIndicatorsDescription** | **String**| Description | [optional] 
 **searchDbDbCoIndicatorsMeasure** | **Number**| Measure | [optional] 
 **searchDbDbCoIndicatorsLocation** | **String**| Location | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

