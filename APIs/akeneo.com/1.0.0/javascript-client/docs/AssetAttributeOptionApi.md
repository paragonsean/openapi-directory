# AkeneoPimRestApi.AssetAttributeOptionApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAssetAttributesAttributeCodeOptionsCode**](AssetAttributeOptionApi.md#getAssetAttributesAttributeCodeOptionsCode) | **GET** /api/rest/v1/asset-families/{asset_family_code}/attributes/{attribute_code}/options/{code} | Get an attribute option for a given attribute of a given asset family
[**getAssetFamilyAttributesAttributeCodeOptions**](AssetAttributeOptionApi.md#getAssetFamilyAttributesAttributeCodeOptions) | **GET** /api/rest/v1/asset-families/{asset_family_code}/attributes/{attribute_code}/options | Get a list of attribute options of a given attribute for a given asset family
[**patchAssetAttributesAttributeCodeOptionsCode**](AssetAttributeOptionApi.md#patchAssetAttributesAttributeCodeOptionsCode) | **PATCH** /api/rest/v1/asset-families/{asset_family_code}/attributes/{attribute_code}/options/{code} | Update/create an asset attribute option for a given asset family



## getAssetAttributesAttributeCodeOptionsCode

> GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner getAssetAttributesAttributeCodeOptionsCode(assetFamilyCode, attributeCode, code)

Get an attribute option for a given attribute of a given asset family

This endpoint allows you to get the information about a given asset attribute option.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssetAttributeOptionApi();
let assetFamilyCode = "assetFamilyCode_example"; // String | Code of the asset family
let attributeCode = "attributeCode_example"; // String | Code of the attribute
let code = "code_example"; // String | Code of the resource
apiInstance.getAssetAttributesAttributeCodeOptionsCode(assetFamilyCode, attributeCode, code, (error, data, response) => {
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
 **attributeCode** | **String**| Code of the attribute | 
 **code** | **String**| Code of the resource | 

### Return type

[**GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner**](GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## getAssetFamilyAttributesAttributeCodeOptions

> [GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner] getAssetFamilyAttributesAttributeCodeOptions(assetFamilyCode, attributeCode)

Get a list of attribute options of a given attribute for a given asset family

This endpoint allows you to get a list of attribute options for a given asset family.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssetAttributeOptionApi();
let assetFamilyCode = "assetFamilyCode_example"; // String | Code of the asset family
let attributeCode = "attributeCode_example"; // String | Code of the attribute
apiInstance.getAssetFamilyAttributesAttributeCodeOptions(assetFamilyCode, attributeCode, (error, data, response) => {
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
 **attributeCode** | **String**| Code of the attribute | 

### Return type

[**[GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner]**](GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## patchAssetAttributesAttributeCodeOptionsCode

> patchAssetAttributesAttributeCodeOptionsCode(assetFamilyCode, attributeCode, code, body)

Update/create an asset attribute option for a given asset family

This endpoint allows you to update a given option for a given attribute and a given asset family. Learn more about the &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if the option does not already exist for the given attribute of the given asset family, it creates it.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.AssetAttributeOptionApi();
let assetFamilyCode = "assetFamilyCode_example"; // String | Code of the asset family
let attributeCode = "attributeCode_example"; // String | Code of the attribute
let code = "code_example"; // String | Code of the resource
let body = new AkeneoPimRestApi.GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner(); // GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner | 
apiInstance.patchAssetAttributesAttributeCodeOptionsCode(assetFamilyCode, attributeCode, code, body, (error, data, response) => {
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
 **attributeCode** | **String**| Code of the attribute | 
 **code** | **String**| Code of the resource | 
 **body** | [**GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner**](GetAssetFamilyAttributesAttributeCodeOptions200ResponseInner.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links

