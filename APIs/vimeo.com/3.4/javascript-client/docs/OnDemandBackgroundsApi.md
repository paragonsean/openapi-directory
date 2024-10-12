# Vimeo.OnDemandBackgroundsApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createVodBackground**](OnDemandBackgroundsApi.md#createVodBackground) | **POST** /ondemand/pages/{ondemand_id}/backgrounds | Add a background to an On Demand page
[**deleteVodBackground**](OnDemandBackgroundsApi.md#deleteVodBackground) | **DELETE** /ondemand/pages/{ondemand_id}/backgrounds/{background_id} | Remove a background from an On Demand page
[**editVodBackground**](OnDemandBackgroundsApi.md#editVodBackground) | **PATCH** /ondemand/pages/{ondemand_id}/backgrounds/{background_id} | Edit a background of an On Demand page
[**getVodBackground**](OnDemandBackgroundsApi.md#getVodBackground) | **GET** /ondemand/pages/{ondemand_id}/backgrounds/{background_id} | Get a specific background of an On Demand page
[**getVodBackgrounds**](OnDemandBackgroundsApi.md#getVodBackgrounds) | **GET** /ondemand/pages/{ondemand_id}/backgrounds | Get all the backgrounds of an On Demand page



## createVodBackground

> Picture createVodBackground(ondemandId)

Add a background to an On Demand page

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

let apiInstance = new Vimeo.OnDemandBackgroundsApi();
let ondemandId = 61326; // Number | The ID of the On Demand.
apiInstance.createVodBackground(ondemandId, (error, data, response) => {
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

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json


## deleteVodBackground

> Picture deleteVodBackground(backgroundId, ondemandId)

Remove a background from an On Demand page

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

let apiInstance = new Vimeo.OnDemandBackgroundsApi();
let backgroundId = 12345; // Number | The ID of the background.
let ondemandId = 61326; // Number | The ID of the On Demand.
apiInstance.deleteVodBackground(backgroundId, ondemandId, (error, data, response) => {
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
 **backgroundId** | **Number**| The ID of the background. | 
 **ondemandId** | **Number**| The ID of the On Demand. | 

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json


## editVodBackground

> Picture editVodBackground(backgroundId, ondemandId, opts)

Edit a background of an On Demand page

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

let apiInstance = new Vimeo.OnDemandBackgroundsApi();
let backgroundId = 12345; // Number | The ID of the background.
let ondemandId = 61326; // Number | The ID of the On Demand.
let opts = {
  'editVodBackgroundRequest': new Vimeo.EditVodBackgroundRequest() // EditVodBackgroundRequest | 
};
apiInstance.editVodBackground(backgroundId, ondemandId, opts, (error, data, response) => {
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
 **backgroundId** | **Number**| The ID of the background. | 
 **ondemandId** | **Number**| The ID of the On Demand. | 
 **editVodBackgroundRequest** | [**EditVodBackgroundRequest**](EditVodBackgroundRequest.md)|  | [optional] 

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.picture+json
- **Accept**: application/vnd.vimeo.picture+json


## getVodBackground

> Picture getVodBackground(backgroundId, ondemandId)

Get a specific background of an On Demand page

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

let apiInstance = new Vimeo.OnDemandBackgroundsApi();
let backgroundId = 12345; // Number | The ID of the background.
let ondemandId = 61326; // Number | The ID of the On Demand.
apiInstance.getVodBackground(backgroundId, ondemandId, (error, data, response) => {
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
 **backgroundId** | **Number**| The ID of the background. | 
 **ondemandId** | **Number**| The ID of the On Demand. | 

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json


## getVodBackgrounds

> [Picture] getVodBackgrounds(ondemandId, opts)

Get all the backgrounds of an On Demand page

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

let apiInstance = new Vimeo.OnDemandBackgroundsApi();
let ondemandId = 61326; // Number | The ID of the On Demand.
let opts = {
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10 // Number | The number of items to show on each page of results, up to a maximum of 100.
};
apiInstance.getVodBackgrounds(ondemandId, opts, (error, data, response) => {
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
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 

### Return type

[**[Picture]**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json

