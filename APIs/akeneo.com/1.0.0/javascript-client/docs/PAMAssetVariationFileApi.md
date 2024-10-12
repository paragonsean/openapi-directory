# AkeneoPimRestApi.PAMAssetVariationFileApi

All URIs are relative to *http://demo.akeneo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getVariationFilesChannelCodeLocaleCode**](PAMAssetVariationFileApi.md#getVariationFilesChannelCodeLocaleCode) | **GET** /api/rest/v1/assets/{asset_code}/variation-files/{channel_code}/{locale_code} | Get a variation file
[**getVariationFilesChannelCodeLocaleCodeDownload**](PAMAssetVariationFileApi.md#getVariationFilesChannelCodeLocaleCodeDownload) | **GET** /api/rest/v1/assets/{asset_code}/variation-files/{channel_code}/{locale_code}/download | Download a variation file
[**postVariationFilesChannelCodeLocaleCode**](PAMAssetVariationFileApi.md#postVariationFilesChannelCodeLocaleCode) | **POST** /api/rest/v1/assets/{asset_code}/variation-files/{channel_code}/{locale_code} | Upload a new variation file



## getVariationFilesChannelCodeLocaleCode

> GetVariationFilesChannelCodeLocaleCode200Response getVariationFilesChannelCodeLocaleCode(assetCode, channelCode, localeCode)

Get a variation file

This endpoint allows you to get the information about a variation file of a given PAM asset.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PAMAssetVariationFileApi();
let assetCode = "assetCode_example"; // String | Code of the asset
let channelCode = "channelCode_example"; // String | Code of the channel
let localeCode = "localeCode_example"; // String | Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable
apiInstance.getVariationFilesChannelCodeLocaleCode(assetCode, channelCode, localeCode, (error, data, response) => {
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
 **channelCode** | **String**| Code of the channel | 
 **localeCode** | **String**| Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable | 

### Return type

[**GetVariationFilesChannelCodeLocaleCode200Response**](GetVariationFilesChannelCodeLocaleCode200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## getVariationFilesChannelCodeLocaleCodeDownload

> getVariationFilesChannelCodeLocaleCodeDownload(assetCode, channelCode, localeCode)

Download a variation file

This endpoint allows you to download a given variation file.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PAMAssetVariationFileApi();
let assetCode = "assetCode_example"; // String | Code of the asset
let channelCode = "channelCode_example"; // String | Code of the channel
let localeCode = "localeCode_example"; // String | Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable
apiInstance.getVariationFilesChannelCodeLocaleCodeDownload(assetCode, channelCode, localeCode, (error, data, response) => {
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
 **channelCode** | **String**| Code of the channel | 
 **localeCode** | **String**| Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message


## postVariationFilesChannelCodeLocaleCode

> postVariationFilesChannelCodeLocaleCode(assetCode, channelCode, localeCode, contentType, opts)

Upload a new variation file

This endpoint allows you to upload a new variation file for a given PAM asset, channel and locale.

### Example

```javascript
import AkeneoPimRestApi from 'akeneo_pim_rest_api';

let apiInstance = new AkeneoPimRestApi.PAMAssetVariationFileApi();
let assetCode = "assetCode_example"; // String | Code of the asset
let channelCode = "channelCode_example"; // String | Code of the channel
let localeCode = "localeCode_example"; // String | Code of the locale if the asset is localizable or equal to `no-locale` if the asset is not localizable
let contentType = "contentType_example"; // String | Equal to 'multipart/form-data', no other value allowed
let opts = {
  'body': new AkeneoPimRestApi.PostReferenceFilesLocaleCodeRequest() // PostReferenceFilesLocaleCodeRequest | 
};
apiInstance.postVariationFilesChannelCodeLocaleCode(assetCode, channelCode, localeCode, contentType, opts, (error, data, response) => {
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
 **channelCode** | **String**| Code of the channel | 
 **localeCode** | **String**| Code of the locale if the asset is localizable or equal to &#x60;no-locale&#x60; if the asset is not localizable | 
 **contentType** | **String**| Equal to &#39;multipart/form-data&#39;, no other value allowed | 
 **body** | [**PostReferenceFilesLocaleCodeRequest**](PostReferenceFilesLocaleCodeRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, code, message, _links

