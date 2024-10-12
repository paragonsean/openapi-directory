# EtMdbRestApiV1.CinemaApi

All URIs are relative to *https://etmdb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cinemaSearchRead**](CinemaApi.md#cinemaSearchRead) | **GET** /api/v1/cinema/search/{id} | Return cinema search result



## cinemaSearchRead

> cinemaSearchRead(id)

Return cinema search result

Return cinema search result  ### Response Class (Status 200)  * __{id}__: Used as a key to search cinemas,  For more details on how cinemas are listed [see here][ref]. [ref]: https://etmdb.com/en/cinema-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.CinemaApi();
let id = "id_example"; // String | 
apiInstance.cinemaSearchRead(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

