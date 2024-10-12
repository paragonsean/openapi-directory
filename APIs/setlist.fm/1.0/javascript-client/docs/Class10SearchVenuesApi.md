# SetlistFmApi.Class10SearchVenuesApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource10SearchVenuesGetVenuesGET**](Class10SearchVenuesApi.md#resource10SearchVenuesGetVenuesGET) | **GET** /1.0/search/venues | Search for venues.



## resource10SearchVenuesGetVenuesGET

> JsonVenues resource10SearchVenuesGetVenuesGET(opts)

Search for venues.

Search for venues.

### Example

```javascript
import SetlistFmApi from 'setlist_fm_api';

let apiInstance = new SetlistFmApi.Class10SearchVenuesApi();
let opts = {
  'cityId': "cityId_example", // String | the city's geoId
  'cityName': "cityName_example", // String | name of the city where the venue is located
  'country': "country_example", // String | the city's country
  'name': "name_example", // String | name of the venue
  'p': 1, // Number | the number of the result page you'd like to have
  'state': "state_example", // String | the city's state
  'stateCode': "stateCode_example" // String | the city's state code
};
apiInstance.resource10SearchVenuesGetVenuesGET(opts, (error, data, response) => {
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
 **cityId** | **String**| the city&#39;s geoId | [optional] 
 **cityName** | **String**| name of the city where the venue is located | [optional] 
 **country** | **String**| the city&#39;s country | [optional] 
 **name** | **String**| name of the venue | [optional] 
 **p** | **Number**| the number of the result page you&#39;d like to have | [optional] [default to 1]
 **state** | **String**| the city&#39;s state | [optional] 
 **stateCode** | **String**| the city&#39;s state code | [optional] 

### Return type

[**JsonVenues**](JsonVenues.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json

