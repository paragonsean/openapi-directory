# ContentDepot.PiecesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV2PiecesGet**](PiecesApi.md#apiV2PiecesGet) | **GET** /api/v2/pieces | Returns the pieces matching the query parameters.
[**apiV2PiecesIdDelete**](PiecesApi.md#apiV2PiecesIdDelete) | **DELETE** /api/v2/pieces/{id} | Deletes the piece with the given ID.
[**apiV2PiecesIdGet**](PiecesApi.md#apiV2PiecesIdGet) | **GET** /api/v2/pieces/{id} | Returns the piece matching the given ID.
[**apiV2PiecesPost**](PiecesApi.md#apiV2PiecesPost) | **POST** /api/v2/pieces | Create a new piece.



## apiV2PiecesGet

> [Piece] apiV2PiecesGet(episodeId)

Returns the pieces matching the query parameters.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.PiecesApi();
let episodeId = 789; // Number | The ID of the episode that owns the piece.
apiInstance.apiV2PiecesGet(episodeId, (error, data, response) => {
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
 **episodeId** | **Number**| The ID of the episode that owns the piece. | 

### Return type

[**[Piece]**](Piece.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2PiecesIdDelete

> apiV2PiecesIdDelete(id)

Deletes the piece with the given ID.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.PiecesApi();
let id = 789; // Number | 
apiInstance.apiV2PiecesIdDelete(id, (error, data, response) => {
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
- **Accept**: Not defined


## apiV2PiecesIdGet

> Piece apiV2PiecesIdGet(id)

Returns the piece matching the given ID.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.PiecesApi();
let id = 789; // Number | 
apiInstance.apiV2PiecesIdGet(id, (error, data, response) => {
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

[**Piece**](Piece.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2PiecesPost

> Piece apiV2PiecesPost(opts)

Create a new piece.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.PiecesApi();
let opts = {
  'piece': new ContentDepot.Piece() // Piece | 
};
apiInstance.apiV2PiecesPost(opts, (error, data, response) => {
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
 **piece** | [**Piece**](Piece.md)|  | [optional] 

### Return type

[**Piece**](Piece.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

