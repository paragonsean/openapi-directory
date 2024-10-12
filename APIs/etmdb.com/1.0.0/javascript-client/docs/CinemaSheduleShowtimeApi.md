# EtMdbRestApiV1.CinemaSheduleShowtimeApi

All URIs are relative to *https://etmdb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cinemaSheduleShowtimeSearchRead**](CinemaSheduleShowtimeApi.md#cinemaSheduleShowtimeSearchRead) | **GET** /api/v1/cinema-shedule-showtime/search/{movie_title} | Return cinema schedule and showtime search result
[**cinemaSheduleShowtimeSearchallRead**](CinemaSheduleShowtimeApi.md#cinemaSheduleShowtimeSearchallRead) | **GET** /api/v1/cinema-shedule-showtime/searchall/{param} | Return cinema schedule and showtime search result



## cinemaSheduleShowtimeSearchRead

> cinemaSheduleShowtimeSearchRead(movieTitle)

Return cinema schedule and showtime search result

Return cinema schedule and showtime search result  ### Response Class (Status 200) * __{movie_title}__: Used as a key word to search movie cast * You can use both Amharic or English charset/font to search  For more details about cinema schedule showtime, check each cinema from the cinema list [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.CinemaSheduleShowtimeApi();
let movieTitle = "movieTitle_example"; // String | 
apiInstance.cinemaSheduleShowtimeSearchRead(movieTitle, (error, data, response) => {
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


## cinemaSheduleShowtimeSearchallRead

> cinemaSheduleShowtimeSearchallRead(param)

Return cinema schedule and showtime search result

Return cinema schedule and showtime search result  ### Response Class (Status 200) __{param}__ argument can be * movie title * cinema name * cinema hall name * showtime starting date * showtime ending date or * cinema technology  For more details about cinema schedule, check each cinema from the cinema list [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.CinemaSheduleShowtimeApi();
let param = "param_example"; // String | 
apiInstance.cinemaSheduleShowtimeSearchallRead(param, (error, data, response) => {
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

