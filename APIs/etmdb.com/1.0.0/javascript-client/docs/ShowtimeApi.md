# EtMdbRestApiV1.ShowtimeApi

All URIs are relative to *https://etmdb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**showtimeSearchallRead**](ShowtimeApi.md#showtimeSearchallRead) | **GET** /api/v1/showtime/searchall/{param} | Return showtime search result



## showtimeSearchallRead

> showtimeSearchallRead(param)

Return showtime search result

Return showtime search result  ### Response Class (Status 200) __{param}__ argument can be * show time or * day of the week [Mon&#x3D;1, Tue&#x3D;2, Wed&#x3D;3, Thu&#x3D;4, Fri&#x3D;5, Sat&#x3D;6, Sun&#x3D;7]  For more details about showtime, check each cinema from the cinema list [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.ShowtimeApi();
let param = "param_example"; // String | 
apiInstance.showtimeSearchallRead(param, (error, data, response) => {
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
 **param** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

