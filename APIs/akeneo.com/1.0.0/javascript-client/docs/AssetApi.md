# AkeneoPimRestApi.AssetApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteAssetsCode**](AssetApi.md#deleteAssetsCode) | **DELETE** /api/rest/v1/asset-families/{asset_family_code}/assets/{code} | Delete an asset
[**getAssets**](AssetApi.md#getAssets) | **GET** /api/rest/v1/asset-families/{asset_family_code}/assets | Get the list of the assets of a given asset family
[**getAssetsCode**](AssetApi.md#getAssetsCode) | **GET** /api/rest/v1/asset-families/{asset_family_code}/assets/{code} | Get an asset of a given asset family
[**patchAssetCode**](AssetApi.md#patchAssetCode) | **PATCH** /api/rest/v1/asset-families/{asset_family_code}/assets/{code} | Update/create an asset
[**patchAssets**](AssetApi.md#patchAssets) | **PATCH** /api/rest/v1/asset-families/{asset_family_code}/assets | Update/create several assets



## deleteAssetsCode

> deleteAssetsCode(assetFamilyCode, code)

Delete an asset

This endpoint allows you to delete a given asset. This endpoint is case sensitive on the asset family code.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssetApi();
let assetFamilyCode = "assetFamilyCode_example"; // String | Code of the asset family
let code = "code_example"; // String | Code of the resource
apiInstance.deleteAssetsCode(assetFamilyCode, code, (error, data, response) => {
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
 **assetFamilyCode** | **String**| Code of the asset family | 
 **code** | **String**| Code of the resource | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## getAssets

> Asset getAssets(assetFamilyCode, opts)

Get the list of the assets of a given asset family

This endpoint allows you to get a list of assets of a given asset family. Assets are paginated. This endpoint is case sensitive on the asset family code.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssetApi();
let assetFamilyCode = "assetFamilyCode_example"; // String | Code of the asset family
let opts = {
  'search': "search_example", // String | Filter assets, for more details see the <a href=\"/documentation/filter.html#filter-assets\">Asset filters</a> section
  'channel': "channel_example", // String | Filter asset values to return scopable asset attributes for the given channel as well as the non localizable/non scopable asset attributes, for more details see the <a href=\"/documentation/filter.html#asset-values-by-channel\">Filter asset values by channel</a> section
  'locales': "locales_example", // String | Filter asset values to return localizable attributes for the given locales as well as the non localizable/non scopable asset attributes, for more details see the <a href=\"/documentation/filter.html#asset-values-by-locale\">Filter asset values by locale</a> section
  'searchAfter': "'cursor to the first page'" // String | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section
};
apiInstance.getAssets(assetFamilyCode, opts, (error, data, response) => {
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
 **assetFamilyCode** | **String**| Code of the asset family | 
 **search** | **String**| Filter assets, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-assets\&quot;&gt;Asset filters&lt;/a&gt; section | [optional] 
 **channel** | **String**| Filter asset values to return scopable asset attributes for the given channel as well as the non localizable/non scopable asset attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#asset-values-by-channel\&quot;&gt;Filter asset values by channel&lt;/a&gt; section | [optional] 
 **locales** | **String**| Filter asset values to return localizable attributes for the given locales as well as the non localizable/non scopable asset attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#asset-values-by-locale\&quot;&gt;Filter asset values by locale&lt;/a&gt; section | [optional] 
 **searchAfter** | **String**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to &#39;cursor to the first page&#39;]

### Return type

[**Asset**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, _embedded, _links, code, message


## getAssetsCode

> PatchAssetsRequestInner getAssetsCode(assetFamilyCode, code)

Get an asset of a given asset family

This endpoint allows you to get the information about a given asset for a given asset family. This endpoint is case sensitive on the asset family code.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssetApi();
let assetFamilyCode = "assetFamilyCode_example"; // String | Code of the asset family
let code = "code_example"; // String | Code of the resource
apiInstance.getAssetsCode(assetFamilyCode, code, (error, data, response) => {
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
 **assetFamilyCode** | **String**| Code of the asset family | 
 **code** | **String**| Code of the resource | 

### Return type

[**PatchAssetsRequestInner**](PatchAssetsRequestInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchAssetCode

> patchAssetCode(assetFamilyCode, code, body)

Update/create an asset

This endpoint allows you to update a given asset of a given asset family. Learn more about the &lt;a href&#x3D;\&quot;/documentation/update.html#patch-asset-attribute-values\&quot;&gt;Update behavior&lt;/a&gt;. Note that if the asset does not already exist for the given asset family, it creates it. This endpoint is case sensitive on the asset family code.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssetApi();
let assetFamilyCode = "assetFamilyCode_example"; // String | Code of the asset family
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.PatchAssetsRequestInner(); // PatchAssetsRequestInner | 
apiInstance.patchAssetCode(assetFamilyCode, code, body, (error, data, response) => {
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
 **assetFamilyCode** | **String**| Code of the asset family | 
 **code** | **String**| Code of the resource | 
 **body** | [**PatchAssetsRequestInner**](PatchAssetsRequestInner.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links


## patchAssets

> [PatchAssets200ResponseInner] patchAssets(assetFamilyCode, body)

Update/create several assets

This endpoint allows you to update and/or create several assets of one given asset family at once. Learn more about the &lt;a href&#x3D;\&quot;/documentation/update.html#patch-asset-attribute-values\&quot;&gt;Update behavior&lt;/a&gt;. Note that if the asset does not already exist for the given asset family, it creates it. This endpoint is case sensitive on the asset family code.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssetApi();
let assetFamilyCode = "assetFamilyCode_example"; // String | Code of the asset family
let body = [new AkeneoPimRestApi.PatchAssetsRequestInner()]; // [PatchAssetsRequestInner] | 
apiInstance.patchAssets(assetFamilyCode, body, (error, data, response) => {
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
 **assetFamilyCode** | **String**| Code of the asset family | 
 **body** | [**[PatchAssetsRequestInner]**](PatchAssetsRequestInner.md)|  | 

### Return type

[**[PatchAssets200ResponseInner]**](PatchAssets200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message

