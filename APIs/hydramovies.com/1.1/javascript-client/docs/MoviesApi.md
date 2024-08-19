# HydraMovies.MoviesApi

All URIs are relative to *https://hydramovies.com/api-v2/%3Fsource&#x3D;http:/hydramovies.com/api-v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currentMovieDataCsvGet**](MoviesApi.md#currentMovieDataCsvGet) | **GET** /current-Movie-Data.csv&amp;imdb_id&#x3D;{IMDBid} | getMovieByIMDBid
[**currentMovieDataCsvGet2**](MoviesApi.md#currentMovieDataCsvGet2) | **GET** /current-Movie-Data.csv&amp;movie_year&#x3D;{MovieYear} | getMovieByYear



## currentMovieDataCsvGet

> currentMovieDataCsvGet(iMDBid)

getMovieByIMDBid

Returns a movie using the films unique IMDB identifier

### Example

```javascript
import HydraMovies from 'hydra_movies';

let apiInstance = new HydraMovies.MoviesApi();
let iMDBid = "iMDBid_example"; // String | IMDB ID of the movie to return
apiInstance.currentMovieDataCsvGet(iMDBid, (error, data, response) => {
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
 **iMDBid** | **String**| IMDB ID of the movie to return | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## currentMovieDataCsvGet2

> currentMovieDataCsvGet2(movieYear)

getMovieByYear

Returns a movie based on the year of its release

### Example

```javascript
import HydraMovies from 'hydra_movies';

let apiInstance = new HydraMovies.MoviesApi();
let movieYear = "movieYear_example"; // String | Release year of the movies to return
apiInstance.currentMovieDataCsvGet2(movieYear, (error, data, response) => {
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
 **movieYear** | **String**| Release year of the movies to return | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

