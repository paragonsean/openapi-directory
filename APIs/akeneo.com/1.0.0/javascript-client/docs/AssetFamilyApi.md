# AkeneoPimRestApi.AssetFamilyApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAssetFamilies**](AssetFamilyApi.md#getAssetFamilies) | **GET** /api/rest/v1/asset-families | Get list of asset families
[**getAssetFamilyCode**](AssetFamilyApi.md#getAssetFamilyCode) | **GET** /api/rest/v1/asset-families/{code} | Get an asset family
[**patchAssetFamilyCode**](AssetFamilyApi.md#patchAssetFamilyCode) | **PATCH** /api/rest/v1/asset-families/{code} | Update/create an asset family



## getAssetFamilies

> AssetFamilies getAssetFamilies(opts)

Get list of asset families

This endpoint allows you to get a list of asset families. Asset families are paginated.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssetFamilyApi();
let opts = {
  'searchAfter': "'cursor to the first page'" // String | Cursor when using the `search_after` pagination method type. <strong>Should never be set manually</strong>, see <a href=\"/documentation/pagination.html\">Pagination</a> section
};
apiInstance.getAssetFamilies(opts, (error, data, response) => {
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
 **searchAfter** | **String**| Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section | [optional] [default to &#39;cursor to the first page&#39;]

### Return type

[**AssetFamilies**](AssetFamilies.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, _embedded, _links, code, message


## getAssetFamilyCode

> GetAssetFamilyCode200Response getAssetFamilyCode(code)

Get an asset family

This endpoint allows you to get the information about a given asset family.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssetFamilyApi();
let code = "code_example"; // String | Code of the resource
apiInstance.getAssetFamilyCode(code, (error, data, response) => {
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
 **code** | **String**| Code of the resource | 

### Return type

[**GetAssetFamilyCode200Response**](GetAssetFamilyCode200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchAssetFamilyCode

> patchAssetFamilyCode(code, body)

Update/create an asset family

This endpoint allows you to update a given asset family. Note that if the asset family does not already exist, it creates it.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssetFamilyApi();
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.GetAssetFamilyCode200Response(); // GetAssetFamilyCode200Response | 
apiInstance.patchAssetFamilyCode(code, body, (error, data, response) => {
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
 **code** | **String**| Code of the resource | 
 **body** | [**GetAssetFamilyCode200Response**](GetAssetFamilyCode200Response.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links

