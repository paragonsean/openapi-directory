# UebermapsApiEndpoints.CommentsApi

All URIs are relative to *http://uebermaps.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commentsIdDelete**](CommentsApi.md#commentsIdDelete) | **DELETE** /comments/{id} | Delete comment
[**commentsIdPatch**](CommentsApi.md#commentsIdPatch) | **PATCH** /comments/{id} | Update comment
[**mapsIdCommentsGet**](CommentsApi.md#mapsIdCommentsGet) | **GET** /maps/{id}/comments | List comments for a given map
[**mapsIdCommentsPost**](CommentsApi.md#mapsIdCommentsPost) | **POST** /maps/{id}/comments | Create map comment
[**spotsIdCommentsGet**](CommentsApi.md#spotsIdCommentsGet) | **GET** /spots/{id}/comments | List comments for a given spot
[**spotsIdCommentsPost**](CommentsApi.md#spotsIdCommentsPost) | **POST** /spots/{id}/comments | Create spot comment



## commentsIdDelete

> Comment commentsIdDelete(id)

Delete comment

Delete comment.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.CommentsApi();
let id = 56; // Number | Comment id
apiInstance.commentsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| Comment id | 

### Return type

[**Comment**](Comment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## commentsIdPatch

> Comment commentsIdPatch(id, opts)

Update comment

Update comment. Wrap comment parameters in [comment].

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.CommentsApi();
let id = 56; // Number | Comment id
let opts = {
  'comment': new UebermapsApiEndpoints.CommentEditable() // CommentEditable | Comment attributes
};
apiInstance.commentsIdPatch(id, opts, (error, data, response) => {
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
 **id** | **Number**| Comment id | 
 **comment** | [**CommentEditable**](CommentEditable.md)| Comment attributes | [optional] 

### Return type

[**Comment**](Comment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mapsIdCommentsGet

> [Comment] mapsIdCommentsGet(id)

List comments for a given map

List comments for a given map.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.CommentsApi();
let id = 56; // Number | Id of map
apiInstance.mapsIdCommentsGet(id, (error, data, response) => {
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
 **id** | **Number**| Id of map | 

### Return type

[**[Comment]**](Comment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mapsIdCommentsPost

> Comment mapsIdCommentsPost(id, opts)

Create map comment

Create map comment. Wrap comment parameters in [comment].

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.CommentsApi();
let id = 56; // Number | map id
let opts = {
  'comment': new UebermapsApiEndpoints.CommentEditable() // CommentEditable | comment attributes
};
apiInstance.mapsIdCommentsPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| map id | 
 **comment** | [**CommentEditable**](CommentEditable.md)| comment attributes | [optional] 

### Return type

[**Comment**](Comment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## spotsIdCommentsGet

> [Comment] spotsIdCommentsGet(id)

List comments for a given spot

List comments for a given spot.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.CommentsApi();
let id = 56; // Number | Id of spot
apiInstance.spotsIdCommentsGet(id, (error, data, response) => {
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
 **id** | **Number**| Id of spot | 

### Return type

[**[Comment]**](Comment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## spotsIdCommentsPost

> Comment spotsIdCommentsPost(id, opts)

Create spot comment

Create spot comment. Wrap comment parameters in [comment].

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.CommentsApi();
let id = 56; // Number | spot id
let opts = {
  'comment': new UebermapsApiEndpoints.CommentEditable() // CommentEditable | comment attributes
};
apiInstance.spotsIdCommentsPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| spot id | 
 **comment** | [**CommentEditable**](CommentEditable.md)| comment attributes | [optional] 

### Return type

[**Comment**](Comment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

