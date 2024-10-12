# Shinobiapi.MagnetsMagnetHashesOfMoviesTelevisionShowsApi

All URIs are relative to *https://api.hillbillysoftware.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**magnetsByDateGetAsync**](MagnetsMagnetHashesOfMoviesTelevisionShowsApi.md#magnetsByDateGetAsync) | **GET** /Magnets/ByDate/{AccessToken}/{Date} | Gets available magnet hashes on passed date (yyyy-mm-dd).  Feature not available on free plan, please donate to be able to use this feature.
[**magnetsByimdbIDGetAsync**](MagnetsMagnetHashesOfMoviesTelevisionShowsApi.md#magnetsByimdbIDGetAsync) | **GET** /Magnets/ByIMDB/{AccessToken}/{imdbID} | Returns list of magnet hashes for passed IMDBID.  Feature not available on free plan, please donate to be able to use this feature.
[**magnetsMovieByIDGetAsync**](MagnetsMagnetHashesOfMoviesTelevisionShowsApi.md#magnetsMovieByIDGetAsync) | **GET** /Magnets/Search/{AccessToken}/{Query} | Try and find magnet links for queried movie.  Feature not available on free plan, please donate to be able to use this feature
[**tVShowsearchGet**](MagnetsMagnetHashesOfMoviesTelevisionShowsApi.md#tVShowsearchGet) | **GET** /Magnets/TVShow/{AccessToken}/{TVShow} | Returns results based on query, Feature not available on free plan, please donate to be able to use this feature.



## magnetsByDateGetAsync

> [Magnets] magnetsByDateGetAsync(accessToken, date)

Gets available magnet hashes on passed date (yyyy-mm-dd).  Feature not available on free plan, please donate to be able to use this feature.

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.MagnetsMagnetHashesOfMoviesTelevisionShowsApi();
let accessToken = "accessToken_example"; // String | 
let date = "date_example"; // String | 
apiInstance.magnetsByDateGetAsync(accessToken, date, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **date** | **String**|  | 

### Return type

[**[Magnets]**](Magnets.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## magnetsByimdbIDGetAsync

> [Magnets] magnetsByimdbIDGetAsync(accessToken, imdbID)

Returns list of magnet hashes for passed IMDBID.  Feature not available on free plan, please donate to be able to use this feature.

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.MagnetsMagnetHashesOfMoviesTelevisionShowsApi();
let accessToken = "accessToken_example"; // String | 
let imdbID = "imdbID_example"; // String | ID with or without tt prefix
apiInstance.magnetsByimdbIDGetAsync(accessToken, imdbID, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **imdbID** | **String**| ID with or without tt prefix | 

### Return type

[**[Magnets]**](Magnets.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## magnetsMovieByIDGetAsync

> [Magnets] magnetsMovieByIDGetAsync(accessToken, query)

Try and find magnet links for queried movie.  Feature not available on free plan, please donate to be able to use this feature

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.MagnetsMagnetHashesOfMoviesTelevisionShowsApi();
let accessToken = "accessToken_example"; // String | 
let query = "query_example"; // String | Name or part of name of movie or tv show
apiInstance.magnetsMovieByIDGetAsync(accessToken, query, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **query** | **String**| Name or part of name of movie or tv show | 

### Return type

[**[Magnets]**](Magnets.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## tVShowsearchGet

> [Magnets] tVShowsearchGet(accessToken, tVShow)

Returns results based on query, Feature not available on free plan, please donate to be able to use this feature.

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.MagnetsMagnetHashesOfMoviesTelevisionShowsApi();
let accessToken = "accessToken_example"; // String | 
let tVShow = "tVShow_example"; // String | 
apiInstance.tVShowsearchGet(accessToken, tVShow, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **tVShow** | **String**|  | 

### Return type

[**[Magnets]**](Magnets.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

