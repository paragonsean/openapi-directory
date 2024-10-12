# BbcNitroApi.RawApi

All URIs are relative to *https://programmes.api.bbc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRawAncestors**](RawApi.md#getRawAncestors) | **GET** /v1/episodes/{pid}/ancestors/ | Get raw ancestors
[**getRawBrand**](RawApi.md#getRawBrand) | **GET** /v1/brands/{pid} | Get raw brand
[**getRawBrandFranchises**](RawApi.md#getRawBrandFranchises) | **GET** /v1/brands/{pid}/franchises/ | Get raw brand franchise
[**getRawEpisode**](RawApi.md#getRawEpisode) | **GET** /v1/episodes/{pid} | Get raw episode
[**getRawFormats**](RawApi.md#getRawFormats) | **GET** /v1/episodes/{pid}/formats/ | Get raw formats
[**getRawGenreGroups**](RawApi.md#getRawGenreGroups) | **GET** /v1/episodes/{pid}/genre_groups/ | Get raw genre groups
[**getRawImage**](RawApi.md#getRawImage) | **GET** /v1/images/{pid} | Get raw image
[**getRawMasterbrand**](RawApi.md#getRawMasterbrand) | **GET** /v1/master_brands/{mbid} | Get raw masterbrand
[**getRawPromotion**](RawApi.md#getRawPromotion) | **GET** /v1/promotions/{pid} | Get raw promotion



## getRawAncestors

> Nitro getRawAncestors(pid)

Get raw ancestors

Get raw ancestors

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.RawApi();
let pid = "pid_example"; // String | 
apiInstance.getRawAncestors(pid, (error, data, response) => {
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
 **pid** | **String**|  | 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getRawBrand

> Nitro getRawBrand(pid)

Get raw brand

Get raw brand

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.RawApi();
let pid = "pid_example"; // String | 
apiInstance.getRawBrand(pid, (error, data, response) => {
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
 **pid** | **String**|  | 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getRawBrandFranchises

> Nitro getRawBrandFranchises(pid)

Get raw brand franchise

Get raw brand franchises

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.RawApi();
let pid = "pid_example"; // String | 
apiInstance.getRawBrandFranchises(pid, (error, data, response) => {
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
 **pid** | **String**|  | 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getRawEpisode

> Nitro getRawEpisode(pid)

Get raw episode

Get raw episode

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.RawApi();
let pid = "pid_example"; // String | 
apiInstance.getRawEpisode(pid, (error, data, response) => {
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
 **pid** | **String**|  | 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getRawFormats

> Nitro getRawFormats(pid)

Get raw formats

Get raw formats

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.RawApi();
let pid = "pid_example"; // String | 
apiInstance.getRawFormats(pid, (error, data, response) => {
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
 **pid** | **String**|  | 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getRawGenreGroups

> Nitro getRawGenreGroups(pid)

Get raw genre groups

Get raw genre groups

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.RawApi();
let pid = "pid_example"; // String | 
apiInstance.getRawGenreGroups(pid, (error, data, response) => {
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
 **pid** | **String**|  | 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getRawImage

> Nitro getRawImage(pid)

Get raw image

Get raw image

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.RawApi();
let pid = "pid_example"; // String | 
apiInstance.getRawImage(pid, (error, data, response) => {
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
 **pid** | **String**|  | 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getRawMasterbrand

> Nitro getRawMasterbrand(mbid)

Get raw masterbrand

Get raw masterbrand

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.RawApi();
let mbid = "mbid_example"; // String | 
apiInstance.getRawMasterbrand(mbid, (error, data, response) => {
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
 **mbid** | **String**|  | 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getRawPromotion

> Nitro getRawPromotion(pid)

Get raw promotion

Get raw promotion

### Example

```javascript
import BbcNitroApi from 'bbc_nitro_api';
let defaultClient = BbcNitroApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new BbcNitroApi.RawApi();
let pid = "pid_example"; // String | 
apiInstance.getRawPromotion(pid, (error, data, response) => {
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
 **pid** | **String**|  | 

### Return type

[**Nitro**](Nitro.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

