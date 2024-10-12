# ForemApiV1.DisplayAdsApi

All URIs are relative to *https://dev.to/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiDisplayAdsGet**](DisplayAdsApi.md#apiDisplayAdsGet) | **GET** /api/display_ads | display ads
[**apiDisplayAdsIdGet**](DisplayAdsApi.md#apiDisplayAdsIdGet) | **GET** /api/display_ads/{id} | display ad
[**apiDisplayAdsIdPut**](DisplayAdsApi.md#apiDisplayAdsIdPut) | **PUT** /api/display_ads/{id} | display ads
[**apiDisplayAdsIdUnpublishPut**](DisplayAdsApi.md#apiDisplayAdsIdUnpublishPut) | **PUT** /api/display_ads/{id}/unpublish | unpublish
[**apiDisplayAdsPost**](DisplayAdsApi.md#apiDisplayAdsPost) | **POST** /api/display_ads | display ads



## apiDisplayAdsGet

> [DisplayAd] apiDisplayAdsGet()

display ads

This endpoint allows the client to retrieve a list of all display ads.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.DisplayAdsApi();
apiInstance.apiDisplayAdsGet((error, data, response) => {
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

[**[DisplayAd]**](DisplayAd.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiDisplayAdsIdGet

> apiDisplayAdsIdGet(id)

display ad

This endpoint allows the client to retrieve a single display ad, via its id.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.DisplayAdsApi();
let id = 123; // Number | The ID of the display ad.
apiInstance.apiDisplayAdsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the display ad. | 

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiDisplayAdsIdPut

> [DisplayAd] apiDisplayAdsIdPut(id, opts)

display ads

This endpoint allows the client to update the attributes of a single display ad, via its id.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.DisplayAdsApi();
let id = 123; // Number | The ID of the display ad.
let opts = {
  'displayAd': [new ForemApiV1.DisplayAd()] // [DisplayAd] | 
};
apiInstance.apiDisplayAdsIdPut(id, opts, (error, data, response) => {
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
 **id** | **Number**| The ID of the display ad. | 
 **displayAd** | [**[DisplayAd]**](DisplayAd.md)|  | [optional] 

### Return type

[**[DisplayAd]**](DisplayAd.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiDisplayAdsIdUnpublishPut

> apiDisplayAdsIdUnpublishPut(id)

unpublish

This endpoint allows the client to remove a display ad from rotation by un-publishing it.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.DisplayAdsApi();
let id = 123; // Number | The ID of the display ad to unpublish.
apiInstance.apiDisplayAdsIdUnpublishPut(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the display ad to unpublish. | 

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiDisplayAdsPost

> [DisplayAd] apiDisplayAdsPost(opts)

display ads

This endpoint allows the client to create a new display ad.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';
let defaultClient = ForemApiV1.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ForemApiV1.DisplayAdsApi();
let opts = {
  'displayAd': [new ForemApiV1.DisplayAd()] // [DisplayAd] | 
};
apiInstance.apiDisplayAdsPost(opts, (error, data, response) => {
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
 **displayAd** | [**[DisplayAd]**](DisplayAd.md)|  | [optional] 

### Return type

[**[DisplayAd]**](DisplayAd.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

