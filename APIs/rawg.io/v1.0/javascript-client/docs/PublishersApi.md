# RawgVideoGamesDatabaseApi.PublishersApi

All URIs are relative to *https://api.rawg.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publishersList**](PublishersApi.md#publishersList) | **GET** /publishers | Get a list of video game publishers.
[**publishersRead**](PublishersApi.md#publishersRead) | **GET** /publishers/{id} | Get details of the publisher.



## publishersList

> PublishersList200Response publishersList(opts)

Get a list of video game publishers.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.PublishersApi();
let opts = {
  'page': 56, // Number | A page number within the paginated result set.
  'pageSize': 56 // Number | Number of results to return per page.
};
apiInstance.publishersList(opts, (error, data, response) => {
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

[**PublishersList200Response**](PublishersList200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publishersRead

> PublisherSingle publishersRead(id)

Get details of the publisher.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.PublishersApi();
let id = 56; // Number | A unique integer value identifying this Publisher.
apiInstance.publishersRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this Publisher. | 

### Return type

[**PublisherSingle**](PublisherSingle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

