# TvApi.AssetApi

All URIs are relative to *https://tv.api.pressassociation.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAsset**](AssetApi.md#getAsset) | **GET** /asset/{assetId} | Asset Detail
[**getAssetContributors**](AssetApi.md#getAssetContributors) | **GET** /asset/{assetId}/contributor | Asset Contributors
[**listAssets**](AssetApi.md#listAssets) | **GET** /asset | Asset Collection



## getAsset

> Object getAsset(assetId, opts)

Asset Detail

Return the content of the selected asset.

### Example

```javascript
import TvApi from 'tv_api';
let defaultClient = TvApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TvApi.AssetApi();
let assetId = "assetId_example"; // String | A asset ID filter for the schedule collection. This can be a reference to any type of asset i.e. movie, season, series or episode.
let opts = {
  'aliases': true // Boolean | Flag to display Legacy and Provider Ids.
};
apiInstance.getAsset(assetId, opts, (error, data, response) => {
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
 **assetId** | **String**| A asset ID filter for the schedule collection. This can be a reference to any type of asset i.e. movie, season, series or episode. | 
 **aliases** | **Boolean**| Flag to display Legacy and Provider Ids. | [optional] [default to true]

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAssetContributors

> Object getAssetContributors(assetId, opts)

Asset Contributors

Return the contributors of the selected asset.

### Example

```javascript
import TvApi from 'tv_api';
let defaultClient = TvApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TvApi.AssetApi();
let assetId = "assetId_example"; // String | A asset ID filter for the schedule collection. This can be a reference to any type of asset i.e. movie, season, series or episode.
let opts = {
  'aliases': true // Boolean | Flag to display Legacy and Provider Ids.
};
apiInstance.getAssetContributors(assetId, opts, (error, data, response) => {
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
 **assetId** | **String**| A asset ID filter for the schedule collection. This can be a reference to any type of asset i.e. movie, season, series or episode. | 
 **aliases** | **Boolean**| Flag to display Legacy and Provider Ids. | [optional] [default to true]

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAssets

> Object listAssets(opts)

Asset Collection

Return a collection of Assets.

### Example

```javascript
import TvApi from 'tv_api';
let defaultClient = TvApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new TvApi.AssetApi();
let opts = {
  'updatedAfter': "'2015-05-05T00:00:00.000Z'", // String | Updated After
  'limit': 100, // Number | Limit the the number of items to be returned per page. For example: 5.
  'aliases': true // Boolean | Flag to display Legacy and Provider Ids.
};
apiInstance.listAssets(opts, (error, data, response) => {
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
 **updatedAfter** | **String**| Updated After | [optional] [default to &#39;2015-05-05T00:00:00.000Z&#39;]
 **limit** | **Number**| Limit the the number of items to be returned per page. For example: 5. | [optional] [default to 100]
 **aliases** | **Boolean**| Flag to display Legacy and Provider Ids. | [optional] [default to true]

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

