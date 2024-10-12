# EtMdbRestApiV1.CinemaScheduleApi

All URIs are relative to *https://etmdb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cinemaScheduleSearchRead**](CinemaScheduleApi.md#cinemaScheduleSearchRead) | **GET** /api/v1/cinema-schedule/search/{movie_title} | Return cinema schedule search result
[**cinemaScheduleSearchallRead**](CinemaScheduleApi.md#cinemaScheduleSearchallRead) | **GET** /api/v1/cinema-schedule/searchall/{param} | Return cinema schedule search result



## cinemaScheduleSearchRead

> cinemaScheduleSearchRead(movieTitle)

Return cinema schedule search result

Return cinema schedule search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search movie cast * You can use both Amharic or English charset/font to search  For more details about cinema schedule, check each cinema from the cinema list [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.CinemaScheduleApi();
let movieTitle = "movieTitle_example"; // String | 
apiInstance.cinemaScheduleSearchRead(movieTitle, (error, data, response) => {
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
 **movieTitle** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## cinemaScheduleSearchallRead

> cinemaScheduleSearchallRead(param)

Return cinema schedule search result

Return cinema schedule search result  ### Response Class (Status 200) __{param}__ argument can be * movie title * cinema name * cinema hall name or * cinema technology  For more details about cinema schedule, check each cinema from the cinema list [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.CinemaScheduleApi();
let param = "param_example"; // String | 
apiInstance.cinemaScheduleSearchallRead(param, (error, data, response) => {
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

