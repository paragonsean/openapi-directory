# SetlistFmApi.Class10CityGeoIdApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource10CityGeoIdGetCityGET**](Class10CityGeoIdApi.md#resource10CityGeoIdGetCityGET) | **GET** /1.0/city/{geoId} | Get a city by its unique geoId.



## resource10CityGeoIdGetCityGET

> JsonCity resource10CityGeoIdGetCityGET(geoId)

Get a city by its unique geoId.

Get a city by its unique geoId.

### Example

```javascript
import SetlistFmApi from 'setlist_fm_api';

let apiInstance = new SetlistFmApi.Class10CityGeoIdApi();
let geoId = "geoId_example"; // String | the city's geoId
apiInstance.resource10CityGeoIdGetCityGET(geoId, (error, data, response) => {
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
 **geoId** | **String**| the city&#39;s geoId | 

### Return type

[**JsonCity**](JsonCity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json

