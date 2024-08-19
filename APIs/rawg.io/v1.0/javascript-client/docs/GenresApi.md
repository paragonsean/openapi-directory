# RawgVideoGamesDatabaseApi.GenresApi

All URIs are relative to *https://api.rawg.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**genresList**](GenresApi.md#genresList) | **GET** /genres | Get a list of video game genres.
[**genresRead**](GenresApi.md#genresRead) | **GET** /genres/{id} | Get details of the genre.



## genresList

> GenresList200Response genresList(opts)

Get a list of video game genres.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.GenresApi();
let opts = {
  'ordering': "ordering_example", // String | Which field to use when ordering the results.
  'page': 56, // Number | A page number within the paginated result set.
  'pageSize': 56 // Number | Number of results to return per page.
};
apiInstance.genresList(opts, (error, data, response) => {
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
 **ordering** | **String**| Which field to use when ordering the results. | [optional] 
 **page** | **Number**| A page number within the paginated result set. | [optional] 
 **pageSize** | **Number**| Number of results to return per page. | [optional] 

### Return type

[**GenresList200Response**](GenresList200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## genresRead

> GenreSingle genresRead(id)

Get details of the genre.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.GenresApi();
let id = 56; // Number | A unique integer value identifying this Genre.
apiInstance.genresRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this Genre. | 

### Return type

[**GenreSingle**](GenreSingle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

