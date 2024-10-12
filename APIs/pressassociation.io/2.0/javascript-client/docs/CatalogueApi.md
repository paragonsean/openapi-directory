# TvApi.CatalogueApi

All URIs are relative to *https://tv.api.pressassociation.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCatalogue**](CatalogueApi.md#getCatalogue) | **GET** /catalogue/{catalogueId} | Catalogue Detail
[**getCatalogueAsset**](CatalogueApi.md#getCatalogueAsset) | **GET** /catalogue/{catalogueId}/asset | Catalogue Asset Collection
[**getCatalogueAssetDetail**](CatalogueApi.md#getCatalogueAssetDetail) | **GET** /catalogue/{catalogueId}/asset/{assetId} | Catalogue Asset Detail
[**listCatalogues**](CatalogueApi.md#listCatalogues) | **GET** /catalogue | Catalogue Collection



## getCatalogue

> Object getCatalogue(catalogueId)

Catalogue Detail

Return the content of the selected catalogue.

### Example

```javascript
import TvApi from 'tv_api';
let defaultClient = TvApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TvApi.CatalogueApi();
let catalogueId = "catalogueId_example"; // String | The identifier for the selected catalogue.
apiInstance.getCatalogue(catalogueId, (error, data, response) => {
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
 **catalogueId** | **String**| The identifier for the selected catalogue. | 

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCatalogueAsset

> Object getCatalogueAsset(catalogueId, opts)

Catalogue Asset Collection

Return the content of the selected catalogue.

### Example

```javascript
import TvApi from 'tv_api';
let defaultClient = TvApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TvApi.CatalogueApi();
let catalogueId = "catalogueId_example"; // String | The identifier for the selected catalogue.
let opts = {
  'title': "title_example", // String | The query string for a title search
  'start': "'2015-05-05T00:00:00'", // String | The Start Date for the catalogue date range.
  'end': "'2015-05-06T00:00:00'", // String | The End Date for the catalogue date range.
  'updatedAfter': "'2015-05-06T00:00:00'", // String | Retrieve items only that have been updated after this point.
  'limit': 500, // Number | Restrict number of returned items Min = 1, Max = 500.
  'aliases': true // Boolean | Flag to display Legacy and Provider Ids.
};
apiInstance.getCatalogueAsset(catalogueId, opts, (error, data, response) => {
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
 **catalogueId** | **String**| The identifier for the selected catalogue. | 
 **title** | **String**| The query string for a title search | [optional] 
 **start** | **String**| The Start Date for the catalogue date range. | [optional] [default to &#39;2015-05-05T00:00:00&#39;]
 **end** | **String**| The End Date for the catalogue date range. | [optional] [default to &#39;2015-05-06T00:00:00&#39;]
 **updatedAfter** | **String**| Retrieve items only that have been updated after this point. | [optional] [default to &#39;2015-05-06T00:00:00&#39;]
 **limit** | **Number**| Restrict number of returned items Min &#x3D; 1, Max &#x3D; 500. | [optional] [default to 500]
 **aliases** | **Boolean**| Flag to display Legacy and Provider Ids. | [optional] [default to true]

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCatalogueAssetDetail

> Object getCatalogueAssetDetail(catalogueId, assetId)

Catalogue Asset Detail

Return the content of the selected catalogue asset.

### Example

```javascript
import TvApi from 'tv_api';
let defaultClient = TvApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TvApi.CatalogueApi();
let catalogueId = "catalogueId_example"; // String | The identifier for the selected catalogue.
let assetId = "assetId_example"; // String | The identifier for the selected catalogue asset.
apiInstance.getCatalogueAssetDetail(catalogueId, assetId, (error, data, response) => {
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
 **catalogueId** | **String**| The identifier for the selected catalogue. | 
 **assetId** | **String**| The identifier for the selected catalogue asset. | 

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCatalogues

> Object listCatalogues()

Catalogue Collection

Return a collection of Catalogues.

### Example

```javascript
import TvApi from 'tv_api';
let defaultClient = TvApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TvApi.CatalogueApi();
apiInstance.listCatalogues((error, data, response) => {
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

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

