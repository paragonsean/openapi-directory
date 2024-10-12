# Json2VideoApi.DefaultApi

All URIs are relative to *https://api.json2video.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMovies**](DefaultApi.md#getMovies) | **GET** /movies | Get the status of your movies
[**newMovie**](DefaultApi.md#newMovie) | **POST** /movies | Create a new movie



## getMovies

> getMovies()

Get the status of your movies

Get the status any of your movies by passing your project ID in the &lt;code&gt;project&lt;/code&gt; query parameter. You can get your project ID from the response of the POST request.

### Example

```javascript
import Json2VideoApi from 'json2_video_api';

let apiInstance = new Json2VideoApi.DefaultApi();
apiInstance.getMovies((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## newMovie

> newMovie(movie)

Create a new movie

Submit a new movie rendering job.

### Example

```javascript
import Json2VideoApi from 'json2_video_api';

let apiInstance = new Json2VideoApi.DefaultApi();
let movie = new Json2VideoApi.Movie(); // Movie | 
apiInstance.newMovie(movie, (error, data, response) => {
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
 **movie** | [**Movie**](Movie.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

