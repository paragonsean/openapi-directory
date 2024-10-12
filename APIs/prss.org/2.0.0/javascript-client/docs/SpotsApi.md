# ContentDepot.SpotsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV2SpotsGet**](SpotsApi.md#apiV2SpotsGet) | **GET** /api/v2/spots | Returns the spots matching the query parameters.
[**apiV2SpotsIdDelete**](SpotsApi.md#apiV2SpotsIdDelete) | **DELETE** /api/v2/spots/{id} | Deletes the spot with the given ID.
[**apiV2SpotsIdGet**](SpotsApi.md#apiV2SpotsIdGet) | **GET** /api/v2/spots/{id} | Returns the spot matching the given ID.
[**apiV2SpotsPost**](SpotsApi.md#apiV2SpotsPost) | **POST** /api/v2/spots | Creates a new spot.



## apiV2SpotsGet

> [Spot] apiV2SpotsGet(opts)

Returns the spots matching the query parameters.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.SpotsApi();
let opts = {
  'pageStart': 0, // Number | The start page of the spot to return. The first item is indexed at 0.
  'pageSize': 500, // Number | The number of items to return. Must be between 0 and 500, inclusive.
  'orderById': "orderById_example" // String | The sort order of the list of spots, based on spot ID. If unspecified, the spots are returned in random order. If using paging to iterate through the results, sort order should be specified.
};
apiInstance.apiV2SpotsGet(opts, (error, data, response) => {
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
 **pageStart** | **Number**| The start page of the spot to return. The first item is indexed at 0. | [optional] [default to 0]
 **pageSize** | **Number**| The number of items to return. Must be between 0 and 500, inclusive. | [optional] [default to 500]
 **orderById** | **String**| The sort order of the list of spots, based on spot ID. If unspecified, the spots are returned in random order. If using paging to iterate through the results, sort order should be specified. | [optional] 

### Return type

[**[Spot]**](Spot.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2SpotsIdDelete

> apiV2SpotsIdDelete(id)

Deletes the spot with the given ID.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.SpotsApi();
let id = 789; // Number | 
apiInstance.apiV2SpotsIdDelete(id, (error, data, response) => {
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


## apiV2SpotsIdGet

> Spot apiV2SpotsIdGet(id)

Returns the spot matching the given ID.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.SpotsApi();
let id = 789; // Number | 
apiInstance.apiV2SpotsIdGet(id, (error, data, response) => {
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

[**Spot**](Spot.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2SpotsPost

> Spot apiV2SpotsPost(cdDriveUri, name, notes)

Creates a new spot.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.SpotsApi();
let cdDriveUri = "cdDriveUri_example"; // String | The URI to the spot content in CD Drive. Format should be 'cddrive:id:{value}' or 'cddrive://{path}'.
let name = "name_example"; // String | The name of the spot to create/update.
let notes = "notes_example"; // String | Notes pertaining to the spot.
apiInstance.apiV2SpotsPost(cdDriveUri, name, notes, (error, data, response) => {
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
 **cdDriveUri** | **String**| The URI to the spot content in CD Drive. Format should be &#39;cddrive:id:{value}&#39; or &#39;cddrive://{path}&#39;. | 
 **name** | **String**| The name of the spot to create/update. | 
 **notes** | **String**| Notes pertaining to the spot. | 

### Return type

[**Spot**](Spot.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

