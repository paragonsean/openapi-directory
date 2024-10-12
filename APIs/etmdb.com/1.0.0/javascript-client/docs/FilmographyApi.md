# EtMdbRestApiV1.FilmographyApi

All URIs are relative to *https://etmdb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filmographySearchRead**](FilmographyApi.md#filmographySearchRead) | **GET** /api/v1/filmography/search/{movie_title} | Return filmography search result
[**filmographySearchallRead**](FilmographyApi.md#filmographySearchallRead) | **GET** /api/v1/filmography/searchall/{param} | Return filmography search result



## filmographySearchRead

> filmographySearchRead(movieTitle)

Return filmography search result

Return filmography search result  ### Response Class (Status 200)  * __{movie_title}__: Used as a key word to search movies * You can use both Amharic or English charset/font to search  For more details on how filmographies are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.FilmographyApi();
let movieTitle = "movieTitle_example"; // String | 
apiInstance.filmographySearchRead(movieTitle, (error, data, response) => {
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


## filmographySearchallRead

> filmographySearchallRead(param)

Return filmography search result

Return filmography search result  ### Response Class (Status 200) __{param}__ argument can be * artist first name * artist last name * artist username * movie title or * filmography description (such as director, actor, producer, etc)  For more details on how filmographies are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.FilmographyApi();
let param = "param_example"; // String | 
apiInstance.filmographySearchallRead(param, (error, data, response) => {
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

