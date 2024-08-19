# RawgVideoGamesDatabaseApi.DevelopersApi

All URIs are relative to *https://api.rawg.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**developersList**](DevelopersApi.md#developersList) | **GET** /developers | Get a list of game developers.
[**developersRead**](DevelopersApi.md#developersRead) | **GET** /developers/{id} | Get details of the developer.



## developersList

> DevelopersList200Response developersList(opts)

Get a list of game developers.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.DevelopersApi();
let opts = {
  'page': 56, // Number | A page number within the paginated result set.
  'pageSize': 56 // Number | Number of results to return per page.
};
apiInstance.developersList(opts, (error, data, response) => {
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
 **page** | **Number**| A page number within the paginated result set. | [optional] 
 **pageSize** | **Number**| Number of results to return per page. | [optional] 

### Return type

[**DevelopersList200Response**](DevelopersList200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## developersRead

> DeveloperSingle developersRead(id)

Get details of the developer.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.DevelopersApi();
let id = 56; // Number | A unique integer value identifying this Developer.
apiInstance.developersRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this Developer. | 

### Return type

[**DeveloperSingle**](DeveloperSingle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

