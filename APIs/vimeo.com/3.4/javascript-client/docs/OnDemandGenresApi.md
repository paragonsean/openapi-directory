# Vimeo.OnDemandGenresApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addVodGenre**](OnDemandGenresApi.md#addVodGenre) | **PUT** /ondemand/pages/{ondemand_id}/genres/{genre_id} | Add a genre to an On Demand page
[**deleteVodGenre**](OnDemandGenresApi.md#deleteVodGenre) | **DELETE** /ondemand/pages/{ondemand_id}/genres/{genre_id} | Remove a genre from an On Demand page
[**getGenreVod**](OnDemandGenresApi.md#getGenreVod) | **GET** /ondemand/genres/{genre_id}/pages/{ondemand_id} | Get a specific On Demand page in a genre
[**getGenreVods**](OnDemandGenresApi.md#getGenreVods) | **GET** /ondemand/genres/{genre_id}/pages | Get all the On Demand pages in a genre
[**getVodGenre**](OnDemandGenresApi.md#getVodGenre) | **GET** /ondemand/genres/{genre_id} | Get a specific On Demand genre
[**getVodGenreByOndemandId**](OnDemandGenresApi.md#getVodGenreByOndemandId) | **GET** /ondemand/pages/{ondemand_id}/genres/{genre_id} | Check whether an On Demand page belongs to a genre
[**getVodGenres**](OnDemandGenresApi.md#getVodGenres) | **GET** /ondemand/genres | Get all On Demand genres
[**getVodGenresByOndemandId**](OnDemandGenresApi.md#getVodGenresByOndemandId) | **GET** /ondemand/pages/{ondemand_id}/genres | Get all the genres of an On Demand page



## addVodGenre

> OnDemandGenre addVodGenre(genreId, ondemandId)

Add a genre to an On Demand page

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandGenresApi();
let genreId = "animation"; // String | The ID of the genre.
let ondemandId = 61326; // Number | The ID of the On Demand.
apiInstance.addVodGenre(genreId, ondemandId, (error, data, response) => {
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
 **genreId** | **String**| The ID of the genre. | 
 **ondemandId** | **Number**| The ID of the On Demand. | 

### Return type

[**OnDemandGenre**](OnDemandGenre.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.genre+json


## deleteVodGenre

> deleteVodGenre(genreId, ondemandId)

Remove a genre from an On Demand page

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandGenresApi();
let genreId = "animation"; // String | The ID of the genre.
let ondemandId = 61326; // Number | The ID of the On Demand.
apiInstance.deleteVodGenre(genreId, ondemandId, (error, data, response) => {
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
 **genreId** | **String**| The ID of the genre. | 
 **ondemandId** | **Number**| The ID of the On Demand. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.genre+json


## getGenreVod

> OnDemandPage getGenreVod(genreId, ondemandId)

Get a specific On Demand page in a genre

Check whether a genre contains an On Demand page.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandGenresApi();
let genreId = "animation"; // String | The ID of the genre.
let ondemandId = 61326; // Number | The ID of the On Demand.
apiInstance.getGenreVod(genreId, ondemandId, (error, data, response) => {
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
 **genreId** | **String**| The ID of the genre. | 
 **ondemandId** | **Number**| The ID of the On Demand. | 

### Return type

[**OnDemandPage**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.page+json


## getGenreVods

> [OnDemandPage] getGenreVods(genreId, opts)

Get all the On Demand pages in a genre

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandGenresApi();
let genreId = "animation"; // String | The ID of the genre.
let opts = {
  'direction': "asc", // String | The sort direction of the results.
  'filter': "filter_example", // String | The attribute by which to filter the results.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'query': "Stop motion", // String | The search query to use to filter the results.
  'sort': "sort_example" // String | The way to sort the results.
};
apiInstance.getGenreVods(genreId, opts, (error, data, response) => {
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
 **genreId** | **String**| The ID of the genre. | 
 **direction** | **String**| The sort direction of the results. | [optional] 
 **filter** | **String**| The attribute by which to filter the results. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **query** | **String**| The search query to use to filter the results. | [optional] 
 **sort** | **String**| The way to sort the results. | [optional] 

### Return type

[**[OnDemandPage]**](OnDemandPage.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.page+json


## getVodGenre

> OnDemandGenre getVodGenre(genreId)

Get a specific On Demand genre

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandGenresApi();
let genreId = "animation"; // String | The ID of the genre.
apiInstance.getVodGenre(genreId, (error, data, response) => {
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
 **genreId** | **String**| The ID of the genre. | 

### Return type

[**OnDemandGenre**](OnDemandGenre.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.genre+json


## getVodGenreByOndemandId

> OnDemandGenre getVodGenreByOndemandId(genreId, ondemandId)

Check whether an On Demand page belongs to a genre

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandGenresApi();
let genreId = "animation"; // String | The ID of the genre.
let ondemandId = 61326; // Number | The ID of the On Demand.
apiInstance.getVodGenreByOndemandId(genreId, ondemandId, (error, data, response) => {
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
 **genreId** | **String**| The ID of the genre. | 
 **ondemandId** | **Number**| The ID of the On Demand. | 

### Return type

[**OnDemandGenre**](OnDemandGenre.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.genre+json


## getVodGenres

> [OnDemandGenre] getVodGenres()

Get all On Demand genres

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandGenresApi();
apiInstance.getVodGenres((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[OnDemandGenre]**](OnDemandGenre.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.genre+json


## getVodGenresByOndemandId

> [OnDemandGenre] getVodGenresByOndemandId(ondemandId)

Get all the genres of an On Demand page

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.OnDemandGenresApi();
let ondemandId = 61326; // Number | The ID of the On Demand.
apiInstance.getVodGenresByOndemandId(ondemandId, (error, data, response) => {
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
 **ondemandId** | **Number**| The ID of the On Demand. | 

### Return type

[**[OnDemandGenre]**](OnDemandGenre.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.genre+json

