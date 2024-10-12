# Vimeo.UsersPicturesApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPicture**](UsersPicturesApi.md#createPicture) | **POST** /users/{user_id}/pictures | Add a user picture
[**createPictureAlt1**](UsersPicturesApi.md#createPictureAlt1) | **POST** /me/pictures | Add a user picture
[**deletePicture**](UsersPicturesApi.md#deletePicture) | **DELETE** /users/{user_id}/pictures/{portraitset_id} | Delete a user picture
[**deletePictureAlt1**](UsersPicturesApi.md#deletePictureAlt1) | **DELETE** /me/pictures/{portraitset_id} | Delete a user picture
[**editPicture**](UsersPicturesApi.md#editPicture) | **PATCH** /users/{user_id}/pictures/{portraitset_id} | Edit a user picture
[**editPictureAlt1**](UsersPicturesApi.md#editPictureAlt1) | **PATCH** /me/pictures/{portraitset_id} | Edit a user picture
[**getPicture**](UsersPicturesApi.md#getPicture) | **GET** /users/{user_id}/pictures/{portraitset_id} | Get a specific user picture
[**getPictureAlt1**](UsersPicturesApi.md#getPictureAlt1) | **GET** /me/pictures/{portraitset_id} | Get a specific user picture
[**getPictures**](UsersPicturesApi.md#getPictures) | **GET** /users/{user_id}/pictures | Get all the pictures that belong to a user
[**getPicturesAlt1**](UsersPicturesApi.md#getPicturesAlt1) | **GET** /me/pictures | Get all the pictures that belong to a user



## createPicture

> Picture createPicture(userId)

Add a user picture

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

let apiInstance = new Vimeo.UsersPicturesApi();
let userId = 152184; // Number | The ID of the user.
apiInstance.createPicture(userId, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user. | 

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json


## createPictureAlt1

> Picture createPictureAlt1()

Add a user picture

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

let apiInstance = new Vimeo.UsersPicturesApi();
apiInstance.createPictureAlt1((error, data, response) => {
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

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json


## deletePicture

> deletePicture(portraitsetId, userId)

Delete a user picture

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

let apiInstance = new Vimeo.UsersPicturesApi();
let portraitsetId = 12345; // Number | The ID of the picture.
let userId = 152184; // Number | The ID of the user.
apiInstance.deletePicture(portraitsetId, userId, (error, data, response) => {
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
 **portraitsetId** | **Number**| The ID of the picture. | 
 **userId** | **Number**| The ID of the user. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deletePictureAlt1

> deletePictureAlt1(portraitsetId)

Delete a user picture

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

let apiInstance = new Vimeo.UsersPicturesApi();
let portraitsetId = 12345; // Number | The ID of the picture.
apiInstance.deletePictureAlt1(portraitsetId, (error, data, response) => {
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
 **portraitsetId** | **Number**| The ID of the picture. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## editPicture

> Picture editPicture(portraitsetId, userId, opts)

Edit a user picture

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

let apiInstance = new Vimeo.UsersPicturesApi();
let portraitsetId = 12345; // Number | The ID of the picture.
let userId = 152184; // Number | The ID of the user.
let opts = {
  'editPictureAlt1Request': new Vimeo.EditPictureAlt1Request() // EditPictureAlt1Request | 
};
apiInstance.editPicture(portraitsetId, userId, opts, (error, data, response) => {
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
 **portraitsetId** | **Number**| The ID of the picture. | 
 **userId** | **Number**| The ID of the user. | 
 **editPictureAlt1Request** | [**EditPictureAlt1Request**](EditPictureAlt1Request.md)|  | [optional] 

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.picture+json
- **Accept**: application/vnd.vimeo.picture+json


## editPictureAlt1

> Picture editPictureAlt1(portraitsetId, opts)

Edit a user picture

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

let apiInstance = new Vimeo.UsersPicturesApi();
let portraitsetId = 12345; // Number | The ID of the picture.
let opts = {
  'editPictureAlt1Request': new Vimeo.EditPictureAlt1Request() // EditPictureAlt1Request | 
};
apiInstance.editPictureAlt1(portraitsetId, opts, (error, data, response) => {
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
 **portraitsetId** | **Number**| The ID of the picture. | 
 **editPictureAlt1Request** | [**EditPictureAlt1Request**](EditPictureAlt1Request.md)|  | [optional] 

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.picture+json
- **Accept**: application/vnd.vimeo.picture+json


## getPicture

> Picture getPicture(portraitsetId, userId)

Get a specific user picture

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

let apiInstance = new Vimeo.UsersPicturesApi();
let portraitsetId = 12345; // Number | The ID of the picture.
let userId = 152184; // Number | The ID of the user.
apiInstance.getPicture(portraitsetId, userId, (error, data, response) => {
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
 **portraitsetId** | **Number**| The ID of the picture. | 
 **userId** | **Number**| The ID of the user. | 

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json


## getPictureAlt1

> Picture getPictureAlt1(portraitsetId)

Get a specific user picture

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

let apiInstance = new Vimeo.UsersPicturesApi();
let portraitsetId = 12345; // Number | The ID of the picture.
apiInstance.getPictureAlt1(portraitsetId, (error, data, response) => {
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
 **portraitsetId** | **Number**| The ID of the picture. | 

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json


## getPictures

> [Picture] getPictures(userId, opts)

Get all the pictures that belong to a user

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

let apiInstance = new Vimeo.UsersPicturesApi();
let userId = 152184; // Number | The ID of the user.
let opts = {
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10 // Number | The number of items to show on each page of results, up to a maximum of 100.
};
apiInstance.getPictures(userId, opts, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user. | 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 

### Return type

[**[Picture]**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json


## getPicturesAlt1

> [Picture] getPicturesAlt1(opts)

Get all the pictures that belong to a user

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

let apiInstance = new Vimeo.UsersPicturesApi();
let opts = {
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10 // Number | The number of items to show on each page of results, up to a maximum of 100.
};
apiInstance.getPicturesAlt1(opts, (error, data, response) => {
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
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 

### Return type

[**[Picture]**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json

