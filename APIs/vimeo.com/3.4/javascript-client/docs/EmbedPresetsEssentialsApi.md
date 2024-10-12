# Vimeo.EmbedPresetsEssentialsApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**editEmbedPreset**](EmbedPresetsEssentialsApi.md#editEmbedPreset) | **PATCH** /users/{user_id}/presets/{preset_id} | Edit an embed preset
[**editEmbedPresetAlt1**](EmbedPresetsEssentialsApi.md#editEmbedPresetAlt1) | **PATCH** /me/presets/{preset_id} | Edit an embed preset
[**getEmbedPreset**](EmbedPresetsEssentialsApi.md#getEmbedPreset) | **GET** /users/{user_id}/presets/{preset_id} | Get a specific embed preset
[**getEmbedPresetAlt1**](EmbedPresetsEssentialsApi.md#getEmbedPresetAlt1) | **GET** /me/presets/{preset_id} | Get a specific embed preset
[**getEmbedPresets**](EmbedPresetsEssentialsApi.md#getEmbedPresets) | **GET** /users/{user_id}/presets | Get all the embed presets that a user has created
[**getEmbedPresetsAlt1**](EmbedPresetsEssentialsApi.md#getEmbedPresetsAlt1) | **GET** /me/presets | Get all the embed presets that a user has created



## editEmbedPreset

> Presets editEmbedPreset(presetId, userId, opts)

Edit an embed preset

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

let apiInstance = new Vimeo.EmbedPresetsEssentialsApi();
let presetId = 12345; // Number | The ID of the preset.
let userId = 152184; // Number | The ID of the user.
let opts = {
  'editEmbedPresetAlt1Request': new Vimeo.EditEmbedPresetAlt1Request() // EditEmbedPresetAlt1Request | 
};
apiInstance.editEmbedPreset(presetId, userId, opts, (error, data, response) => {
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
 **presetId** | **Number**| The ID of the preset. | 
 **userId** | **Number**| The ID of the user. | 
 **editEmbedPresetAlt1Request** | [**EditEmbedPresetAlt1Request**](EditEmbedPresetAlt1Request.md)|  | [optional] 

### Return type

[**Presets**](Presets.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.preset+json
- **Accept**: application/vnd.vimeo.preset+json


## editEmbedPresetAlt1

> Presets editEmbedPresetAlt1(presetId, opts)

Edit an embed preset

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

let apiInstance = new Vimeo.EmbedPresetsEssentialsApi();
let presetId = 12345; // Number | The ID of the preset.
let opts = {
  'editEmbedPresetAlt1Request': new Vimeo.EditEmbedPresetAlt1Request() // EditEmbedPresetAlt1Request | 
};
apiInstance.editEmbedPresetAlt1(presetId, opts, (error, data, response) => {
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
 **presetId** | **Number**| The ID of the preset. | 
 **editEmbedPresetAlt1Request** | [**EditEmbedPresetAlt1Request**](EditEmbedPresetAlt1Request.md)|  | [optional] 

### Return type

[**Presets**](Presets.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.preset+json
- **Accept**: application/vnd.vimeo.preset+json


## getEmbedPreset

> Presets getEmbedPreset(presetId, userId)

Get a specific embed preset

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

let apiInstance = new Vimeo.EmbedPresetsEssentialsApi();
let presetId = 12345; // Number | The ID of the preset.
let userId = 152184; // Number | The ID of the user.
apiInstance.getEmbedPreset(presetId, userId, (error, data, response) => {
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
 **presetId** | **Number**| The ID of the preset. | 
 **userId** | **Number**| The ID of the user. | 

### Return type

[**Presets**](Presets.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.preset+json


## getEmbedPresetAlt1

> Presets getEmbedPresetAlt1(presetId)

Get a specific embed preset

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

let apiInstance = new Vimeo.EmbedPresetsEssentialsApi();
let presetId = 12345; // Number | The ID of the preset.
apiInstance.getEmbedPresetAlt1(presetId, (error, data, response) => {
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
 **presetId** | **Number**| The ID of the preset. | 

### Return type

[**Presets**](Presets.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.preset+json


## getEmbedPresets

> [Presets] getEmbedPresets(userId, opts)

Get all the embed presets that a user has created

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

let apiInstance = new Vimeo.EmbedPresetsEssentialsApi();
let userId = 152184; // Number | The ID of the user.
let opts = {
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10 // Number | The number of items to show on each page of results, up to a maximum of 100.
};
apiInstance.getEmbedPresets(userId, opts, (error, data, response) => {
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

[**[Presets]**](Presets.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.preset+json


## getEmbedPresetsAlt1

> [Presets] getEmbedPresetsAlt1(opts)

Get all the embed presets that a user has created

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

let apiInstance = new Vimeo.EmbedPresetsEssentialsApi();
let opts = {
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10 // Number | The number of items to show on each page of results, up to a maximum of 100.
};
apiInstance.getEmbedPresetsAlt1(opts, (error, data, response) => {
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

[**[Presets]**](Presets.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.preset+json

