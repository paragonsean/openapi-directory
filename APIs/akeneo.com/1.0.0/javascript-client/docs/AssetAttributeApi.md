# AkeneoPimRestApi.AssetAttributeApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAssetFamiliesCodeAttributes**](AssetAttributeApi.md#getAssetFamiliesCodeAttributes) | **GET** /api/rest/v1/asset-families/{asset_family_code}/attributes | Get the list of attributes of a given asset family
[**getAssetFamilyAttributesCode**](AssetAttributeApi.md#getAssetFamilyAttributesCode) | **GET** /api/rest/v1/asset-families/{asset_family_code}/attributes/{code} | Get an attribute of a given asset family
[**patchAssetFamilyAttributesCode**](AssetAttributeApi.md#patchAssetFamilyAttributesCode) | **PATCH** /api/rest/v1/asset-families/{asset_family_code}/attributes/{code} | Update/create an attribute of a given asset family



## getAssetFamiliesCodeAttributes

> [GetAssetFamiliesCodeAttributes200ResponseInner] getAssetFamiliesCodeAttributes(assetFamilyCode)

Get the list of attributes of a given asset family

This endpoint allows you to get the list of attributes of a given asset family.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssetAttributeApi();
let assetFamilyCode = "assetFamilyCode_example"; // String | Code of the asset family
apiInstance.getAssetFamiliesCodeAttributes(assetFamilyCode, (error, data, response) => {
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

### Return type

[**[GetAssetFamiliesCodeAttributes200ResponseInner]**](GetAssetFamiliesCodeAttributes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## getAssetFamilyAttributesCode

> GetAssetFamiliesCodeAttributes200ResponseInner getAssetFamilyAttributesCode(assetFamilyCode, code)

Get an attribute of a given asset family

This endpoint allows you to get the information about a given attribute for a given asset family.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssetAttributeApi();
let assetFamilyCode = "assetFamilyCode_example"; // String | Code of the asset family
let code = "code_example"; // String | Code of the resource
apiInstance.getAssetFamilyAttributesCode(assetFamilyCode, code, (error, data, response) => {
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

[**GetAssetFamiliesCodeAttributes200ResponseInner**](GetAssetFamiliesCodeAttributes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchAssetFamilyAttributesCode

> patchAssetFamilyAttributesCode(assetFamilyCode, code, body)

Update/create an attribute of a given asset family

This endpoint allows you to update a given attribute for a given asset family. Note that if the attribute does not already exist for the given asset family, it creates it.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssetAttributeApi();
let assetFamilyCode = "assetFamilyCode_example"; // String | Code of the asset family
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.GetAssetFamiliesCodeAttributes200ResponseInner(); // GetAssetFamiliesCodeAttributes200ResponseInner | 
apiInstance.patchAssetFamilyAttributesCode(assetFamilyCode, code, body, (error, data, response) => {
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
 **body** | [**GetAssetFamiliesCodeAttributes200ResponseInner**](GetAssetFamiliesCodeAttributes200ResponseInner.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links

