# Shotstack.ServeApi

All URIs are relative to *https://api.shotstack.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteAsset**](ServeApi.md#deleteAsset) | **DELETE** /assets/{id} | Delete Asset
[**getAsset**](ServeApi.md#getAsset) | **GET** /assets/{id} | Get Asset
[**getAssetByRenderId**](ServeApi.md#getAssetByRenderId) | **GET** /assets/render/{id} | Get Asset by Render ID



## deleteAsset

> deleteAsset(id)

Delete Asset

Delete an asset by its asset id. If a render creates multiple assets, such as thumbnail and poster images, each asset must be deleted individually by the asset id.  **base URL:** https://api.shotstack.io/serve/{version}

### Example

```javascript
import Shotstack from 'shotstack';
let defaultClient = Shotstack.ApiClient.instance;
// Configure API key authorization: DeveloperKey
let DeveloperKey = defaultClient.authentications['DeveloperKey'];
DeveloperKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DeveloperKey.apiKeyPrefix = 'Token';

let apiInstance = new Shotstack.ServeApi();
let id = "id_example"; // String | The id of the asset in UUID format
apiInstance.deleteAsset(id, (error, data, response) => {
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
 **id** | **String**| The id of the asset in UUID format | 

### Return type

null (empty response body)

### Authorization

[DeveloperKey](../README.md#DeveloperKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAsset

> AssetResponse getAsset(id)

Get Asset

The Serve API is used to interact with, and delete hosted assets including videos, images, audio files,  thumbnails and poster images. Use this endpoint to fetch an asset by asset id. Note that an asset id is unique for each asset and different from the render id.  **base URL:** https://api.shotstack.io/serve/{version}

### Example

```javascript
import Shotstack from 'shotstack';
let defaultClient = Shotstack.ApiClient.instance;
// Configure API key authorization: DeveloperKey
let DeveloperKey = defaultClient.authentications['DeveloperKey'];
DeveloperKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DeveloperKey.apiKeyPrefix = 'Token';

let apiInstance = new Shotstack.ServeApi();
let id = "id_example"; // String | The id of the asset in UUID format
apiInstance.getAsset(id, (error, data, response) => {
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
 **id** | **String**| The id of the asset in UUID format | 

### Return type

[**AssetResponse**](AssetResponse.md)

### Authorization

[DeveloperKey](../README.md#DeveloperKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAssetByRenderId

> AssetRenderResponse getAssetByRenderId(id)

Get Asset by Render ID

A render may generate more than one file, such as a video, thumbnail and poster image. When the assets are created the only known id is the render id returned by the original [render request](#render-video), status  request or webhook. This endpoint lets you look up one or more assets by the render id.  **base URL:** https://api.shotstack.io/serve/{version}

### Example

```javascript
import Shotstack from 'shotstack';
let defaultClient = Shotstack.ApiClient.instance;
// Configure API key authorization: DeveloperKey
let DeveloperKey = defaultClient.authentications['DeveloperKey'];
DeveloperKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DeveloperKey.apiKeyPrefix = 'Token';

let apiInstance = new Shotstack.ServeApi();
let id = "id_example"; // String | The render id associated with the asset in UUID format
apiInstance.getAssetByRenderId(id, (error, data, response) => {
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
 **id** | **String**| The render id associated with the asset in UUID format | 

### Return type

[**AssetRenderResponse**](AssetRenderResponse.md)

### Authorization

[DeveloperKey](../README.md#DeveloperKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

