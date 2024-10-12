# TvApi.PlatformApi

All URIs are relative to *https://tv.api.pressassociation.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPlatform**](PlatformApi.md#getPlatform) | **GET** /platform/{platformId} | Platform Detail
[**listPlatformRegions**](PlatformApi.md#listPlatformRegions) | **GET** /platform/{platformId}/region | Platform Region Collection
[**listPlatforms**](PlatformApi.md#listPlatforms) | **GET** /platform | Platform Collection



## getPlatform

> Object getPlatform(platformId)

Platform Detail

Return the content of the selected platform.

### Example

```javascript
import TvApi from 'tv_api';
let defaultClient = TvApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TvApi.PlatformApi();
let platformId = "'d3b26caa-8c7d-5f97-9eff-40fcf1a6f8d3'"; // String | The identifier for the selected platform.
apiInstance.getPlatform(platformId, (error, data, response) => {
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
 **platformId** | **String**| The identifier for the selected platform. | [default to &#39;d3b26caa-8c7d-5f97-9eff-40fcf1a6f8d3&#39;]

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPlatformRegions

> Object listPlatformRegions(platformId, opts)

Platform Region Collection

Return a list of regions for a platform.

### Example

```javascript
import TvApi from 'tv_api';
let defaultClient = TvApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TvApi.PlatformApi();
let platformId = "'d3b26caa-8c7d-5f97-9eff-40fcf1a6f8d3'"; // String | The identifier for the selected platform.
let opts = {
  'aliases': true // Boolean | Flag to display Legacy and Provider Ids.
};
apiInstance.listPlatformRegions(platformId, opts, (error, data, response) => {
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
 **platformId** | **String**| The identifier for the selected platform. | [default to &#39;d3b26caa-8c7d-5f97-9eff-40fcf1a6f8d3&#39;]
 **aliases** | **Boolean**| Flag to display Legacy and Provider Ids. | [optional] [default to true]

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPlatforms

> Object listPlatforms(opts)

Platform Collection

Return a list of available platforms.

### Example

```javascript
import TvApi from 'tv_api';
let defaultClient = TvApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TvApi.PlatformApi();
let opts = {
  'aliases': true // Boolean | Flag to display Legacy and Provider Ids.
};
apiInstance.listPlatforms(opts, (error, data, response) => {
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
 **aliases** | **Boolean**| Flag to display Legacy and Provider Ids. | [optional] [default to true]

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

