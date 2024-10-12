# EtMdbRestApiV1.CinemaDetailApi

All URIs are relative to *https://etmdb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cinemaDetailSearchRead**](CinemaDetailApi.md#cinemaDetailSearchRead) | **GET** /api/v1/cinema-detail/search/{cinema_name} | Return cinema details search result



## cinemaDetailSearchRead

> cinemaDetailSearchRead(cinemaName)

Return cinema details search result

Return cinema details search result  ### Response Class (Status 200)  * __{cinema_name}__: Used as a key word to search cinemas,  For more details on how cinemas are listed [see here][ref]. [ref]: https://etmdb.com/en/cinema-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.CinemaDetailApi();
let cinemaName = "cinemaName_example"; // String | 
apiInstance.cinemaDetailSearchRead(cinemaName, (error, data, response) => {
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
 **cinemaName** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

