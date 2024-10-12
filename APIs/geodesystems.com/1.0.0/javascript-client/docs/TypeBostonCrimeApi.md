# GeodesystemsCom443.TypeBostonCrimeApi

All URIs are relative to *https://geodesystems.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchBostonCrime**](TypeBostonCrimeApi.md#searchBostonCrime) | **GET** /repository/search/type/boston_crime | Search API for &#39;Boston Crime&#39; entry type



## searchBostonCrime

> searchBostonCrime(opts)

Search API for &#39;Boston Crime&#39; entry type

API to search for entries of type Boston Crime

### Example

```javascript
import GeodesystemsCom443 from 'geodesystems_com443';

let apiInstance = new GeodesystemsCom443.TypeBostonCrimeApi();
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
  'searchDbBostonCrimeOffense': "searchDbBostonCrimeOffense_example", // String | Offense
  'searchDbBostonCrimeOffenseCodeGroup': "searchDbBostonCrimeOffenseCodeGroup_example", // String | Offense Code Group
  'searchDbBostonCrimeOffenseDescription': "searchDbBostonCrimeOffenseDescription_example", // String | Offense Description
  'searchDbBostonCrimeDistrict': "searchDbBostonCrimeDistrict_example", // String | District
  'searchDbBostonCrimeReportingArea': "searchDbBostonCrimeReportingArea_example", // String | Reporting Area
  'searchDbBostonCrimeShooting': "searchDbBostonCrimeShooting_example", // String | Shooting
  'searchDbBostonCrimeYear': 3.4, // Number | Year
  'searchDbBostonCrimeMonth': 3.4, // Number | Month
  'searchDbBostonCrimeDayOfWeek': "searchDbBostonCrimeDayOfWeek_example", // String | Day Of Week
  'searchDbBostonCrimeHour': 3.4, // Number | Hour
  'searchDbBostonCrimeStreet': "searchDbBostonCrimeStreet_example", // String | Street
  'searchDbBostonCrimeLocation': "searchDbBostonCrimeLocation_example" // String | Location
};
apiInstance.searchBostonCrime(opts, (error, data, response) => {
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
 **searchDbBostonCrimeOffense** | **String**| Offense | [optional] 
 **searchDbBostonCrimeOffenseCodeGroup** | **String**| Offense Code Group | [optional] 
 **searchDbBostonCrimeOffenseDescription** | **String**| Offense Description | [optional] 
 **searchDbBostonCrimeDistrict** | **String**| District | [optional] 
 **searchDbBostonCrimeReportingArea** | **String**| Reporting Area | [optional] 
 **searchDbBostonCrimeShooting** | **String**| Shooting | [optional] 
 **searchDbBostonCrimeYear** | **Number**| Year | [optional] 
 **searchDbBostonCrimeMonth** | **Number**| Month | [optional] 
 **searchDbBostonCrimeDayOfWeek** | **String**| Day Of Week | [optional] 
 **searchDbBostonCrimeHour** | **Number**| Hour | [optional] 
 **searchDbBostonCrimeStreet** | **String**| Street | [optional] 
 **searchDbBostonCrimeLocation** | **String**| Location | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

