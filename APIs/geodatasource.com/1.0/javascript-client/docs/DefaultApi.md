# GeoDataSourceLocationSearch.DefaultApi

All URIs are relative to *https://api.geodatasource.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cityGet**](DefaultApi.md#cityGet) | **GET** /city | 



## cityGet

> String cityGet(key, lng, lat, opts)



Get City name by using latitude and longitude

### Example

```javascript
import GeoDataSourceLocationSearch from 'geo_data_source_location_search';

let apiInstance = new GeoDataSourceLocationSearch.DefaultApi();
let key = "key_example"; // String | 
let lng = 3.4; // Number | 
let lat = 3.4; // Number | 
let opts = {
  'format': "format_example" // String | 
};
apiInstance.cityGet(key, lng, lat, opts, (error, data, response) => {
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
 **key** | **String**|  | 
 **lng** | **Number**|  | 
 **lat** | **Number**|  | 
 **format** | **String**|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8

