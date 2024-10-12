# SetlistFmApi.Class10SearchCitiesApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource10SearchCitiesGetCitiesGET**](Class10SearchCitiesApi.md#resource10SearchCitiesGetCitiesGET) | **GET** /1.0/search/cities | Search for a city.



## resource10SearchCitiesGetCitiesGET

> JsonCities resource10SearchCitiesGetCitiesGET(opts)

Search for a city.

Search for a city.

### Example

```javascript
import SetlistFmApi from 'setlist_fm_api';

let apiInstance = new SetlistFmApi.Class10SearchCitiesApi();
let opts = {
  'country': "country_example", // String | the city's country
  'name': "name_example", // String | name of the city
  'p': 1, // Number | the number of the result page you'd like to have
  'state': "state_example", // String | state the city lies in
  'stateCode': "stateCode_example" // String | state code the city lies in
};
apiInstance.resource10SearchCitiesGetCitiesGET(opts, (error, data, response) => {
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
 **country** | **String**| the city&#39;s country | [optional] 
 **name** | **String**| name of the city | [optional] 
 **p** | **Number**| the number of the result page you&#39;d like to have | [optional] [default to 1]
 **state** | **String**| state the city lies in | [optional] 
 **stateCode** | **String**| state code the city lies in | [optional] 

### Return type

[**JsonCities**](JsonCities.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json

