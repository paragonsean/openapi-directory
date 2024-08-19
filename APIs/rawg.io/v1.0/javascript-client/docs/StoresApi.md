# RawgVideoGamesDatabaseApi.StoresApi

All URIs are relative to *https://api.rawg.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storesList**](StoresApi.md#storesList) | **GET** /stores | Get a list of video game storefronts.
[**storesRead**](StoresApi.md#storesRead) | **GET** /stores/{id} | Get details of the store.



## storesList

> StoresList200Response storesList(opts)

Get a list of video game storefronts.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.StoresApi();
let opts = {
  'ordering': "ordering_example", // String | Which field to use when ordering the results.
  'page': 56, // Number | A page number within the paginated result set.
  'pageSize': 56 // Number | Number of results to return per page.
};
apiInstance.storesList(opts, (error, data, response) => {
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

[**StoresList200Response**](StoresList200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storesRead

> StoreSingle storesRead(id)

Get details of the store.



### Example

```javascript
import RawgVideoGamesDatabaseApi from 'rawg_video_games_database_api';

let apiInstance = new RawgVideoGamesDatabaseApi.StoresApi();
let id = 56; // Number | A unique integer value identifying this Store.
apiInstance.storesRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this Store. | 

### Return type

[**StoreSingle**](StoreSingle.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

