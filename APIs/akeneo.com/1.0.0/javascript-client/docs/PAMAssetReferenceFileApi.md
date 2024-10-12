# AkeneoPimRestApi.PAMAssetReferenceFileApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getReferenceFilesChannelCodeLocaleCodeDownload**](PAMAssetReferenceFileApi.md#getReferenceFilesChannelCodeLocaleCodeDownload) | **GET** /api/rest/v1/assets/{asset_code}/reference-files/{locale_code}/download | Download a reference file
[**getReferenceFilesLocaleCode**](PAMAssetReferenceFileApi.md#getReferenceFilesLocaleCode) | **GET** /api/rest/v1/assets/{asset_code}/reference-files/{locale_code} | Get a reference file
[**postReferenceFilesLocaleCode**](PAMAssetReferenceFileApi.md#postReferenceFilesLocaleCode) | **POST** /api/rest/v1/assets/{asset_code}/reference-files/{locale_code} | Upload a new reference file



## getReferenceFilesChannelCodeLocaleCodeDownload

> getReferenceFilesChannelCodeLocaleCodeDownload(assetCode, localeCode)

Download a reference file

This endpoint allows you to download a given reference file.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PAMAssetReferenceFileApi();
let assetCode = "assetCode_example"; // String | Code of the asset
let localeCode = "localeCode_example"; // String | Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable
apiInstance.getReferenceFilesChannelCodeLocaleCodeDownload(assetCode, localeCode, (error, data, response) => {
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
 **assetCode** | **String**| Code of the asset | 
 **localeCode** | **String**| Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## getReferenceFilesLocaleCode

> GetReferenceFilesLocaleCode200Response getReferenceFilesLocaleCode(assetCode, localeCode)

Get a reference file

This endpoint allows you to get the information about a reference file of a given PAM asset.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PAMAssetReferenceFileApi();
let assetCode = "assetCode_example"; // String | Code of the asset
let localeCode = "localeCode_example"; // String | Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable
apiInstance.getReferenceFilesLocaleCode(assetCode, localeCode, (error, data, response) => {
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
 **assetCode** | **String**| Code of the asset | 
 **localeCode** | **String**| Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable | 

### Return type

[**GetReferenceFilesLocaleCode200Response**](GetReferenceFilesLocaleCode200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## postReferenceFilesLocaleCode

> PostReferenceFilesLocaleCode201Response postReferenceFilesLocaleCode(assetCode, localeCode, contentType, opts)

Upload a new reference file

This endpoint allows you to upload a new reference file for a given PAM asset and locale. It will also automatically generate all the variation files corresponding to this reference file.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PAMAssetReferenceFileApi();
let assetCode = "assetCode_example"; // String | Code of the asset
let localeCode = "localeCode_example"; // String | Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable
let contentType = "contentType_example"; // String | Equal to 'multipart/form-data', no other value allowed
let opts = {
  'body': new AkeneoPimRestApi.PostReferenceFilesLocaleCodeRequest() // PostReferenceFilesLocaleCodeRequest | 
};
apiInstance.postReferenceFilesLocaleCode(assetCode, localeCode, contentType, opts, (error, data, response) => {
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
 **assetCode** | **String**| Code of the asset | 
 **localeCode** | **String**| Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable | 
 **contentType** | **String**| Equal to &#39;multipart/form-data&#39;, no other value allowed | 
 **body** | [**PostReferenceFilesLocaleCodeRequest**](PostReferenceFilesLocaleCodeRequest.md)|  | [optional] 

### Return type

[**PostReferenceFilesLocaleCode201Response**](PostReferenceFilesLocaleCode201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links

