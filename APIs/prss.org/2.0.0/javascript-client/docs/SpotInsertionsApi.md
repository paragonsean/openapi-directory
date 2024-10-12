# ContentDepot.SpotInsertionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV2SpotinsertionsGet**](SpotInsertionsApi.md#apiV2SpotinsertionsGet) | **GET** /api/v2/spotinsertions | Returns the spot insertions matching the query parameters.
[**apiV2SpotinsertionsIdDelete**](SpotInsertionsApi.md#apiV2SpotinsertionsIdDelete) | **DELETE** /api/v2/spotinsertions/{id} | Deletes the spot insertion with the given ID.
[**apiV2SpotinsertionsIdGet**](SpotInsertionsApi.md#apiV2SpotinsertionsIdGet) | **GET** /api/v2/spotinsertions/{id} | Returns the spot insertion matching the given ID.
[**apiV2SpotinsertionsPost**](SpotInsertionsApi.md#apiV2SpotinsertionsPost) | **POST** /api/v2/spotinsertions | Creates a new spot insertion.



## apiV2SpotinsertionsGet

> [SpotInsertion] apiV2SpotinsertionsGet(opts)

Returns the spot insertions matching the query parameters.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.SpotInsertionsApi();
let opts = {
  'pageStart': 0, // Number | The start page of the results to return. The first item is indexed at 0.
  'pageSize': 500, // Number | The number of items to return. Must be between 0 and 500, inclusive.
  'orderById': "orderById_example" // String | The sort order of the list of spot insertions, based on ID. If unspecified, the spot insertions are returned in random order. If using paging to iterate through the results, sort order should be specified.
};
apiInstance.apiV2SpotinsertionsGet(opts, (error, data, response) => {
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
 **pageStart** | **Number**| The start page of the results to return. The first item is indexed at 0. | [optional] [default to 0]
 **pageSize** | **Number**| The number of items to return. Must be between 0 and 500, inclusive. | [optional] [default to 500]
 **orderById** | **String**| The sort order of the list of spot insertions, based on ID. If unspecified, the spot insertions are returned in random order. If using paging to iterate through the results, sort order should be specified. | [optional] 

### Return type

[**[SpotInsertion]**](SpotInsertion.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2SpotinsertionsIdDelete

> apiV2SpotinsertionsIdDelete(id)

Deletes the spot insertion with the given ID.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.SpotInsertionsApi();
let id = 789; // Number | 
apiInstance.apiV2SpotinsertionsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2SpotinsertionsIdGet

> SpotInsertion apiV2SpotinsertionsIdGet(id)

Returns the spot insertion matching the given ID.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.SpotInsertionsApi();
let id = 789; // Number | 
apiInstance.apiV2SpotinsertionsIdGet(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

[**SpotInsertion**](SpotInsertion.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2SpotinsertionsPost

> SpotInsertion apiV2SpotinsertionsPost(opts)

Creates a new spot insertion.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.SpotInsertionsApi();
let opts = {
  'spotInsertion': new ContentDepot.SpotInsertion() // SpotInsertion | 
};
apiInstance.apiV2SpotinsertionsPost(opts, (error, data, response) => {
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
 **spotInsertion** | [**SpotInsertion**](SpotInsertion.md)|  | [optional] 

### Return type

[**SpotInsertion**](SpotInsertion.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

