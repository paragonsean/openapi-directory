# ContentDepot.ProgramsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV2ProgramsIdGet**](ProgramsApi.md#apiV2ProgramsIdGet) | **GET** /api/v2/programs/{id} | Returns the program matching the given ID.
[**apiV2ProgramsSearchGet**](ProgramsApi.md#apiV2ProgramsSearchGet) | **GET** /api/v2/programs/search | Optimized free-text search for programs using various filters.



## apiV2ProgramsIdGet

> Program apiV2ProgramsIdGet(id)

Returns the program matching the given ID.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.ProgramsApi();
let id = 789; // Number | The ID of the program to operate on.
apiInstance.apiV2ProgramsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the program to operate on. | 

### Return type

[**Program**](Program.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2ProgramsSearchGet

> [Program] apiV2ProgramsSearchGet(opts)

Optimized free-text search for programs using various filters.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.ProgramsApi();
let opts = {
  'keywords': "keywords_example", // String | Free text search that matches against the program title or description.
  'pageStart': 0, // Number | The start page of the results to return. The first item is indexed at 0.
  'pageSize': 500 // Number | The number of items to return. Must be between 0 and 500, inclusive.
};
apiInstance.apiV2ProgramsSearchGet(opts, (error, data, response) => {
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
 **keywords** | **String**| Free text search that matches against the program title or description. | [optional] 
 **pageStart** | **Number**| The start page of the results to return. The first item is indexed at 0. | [optional] [default to 0]
 **pageSize** | **Number**| The number of items to return. Must be between 0 and 500, inclusive. | [optional] [default to 500]

### Return type

[**[Program]**](Program.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

