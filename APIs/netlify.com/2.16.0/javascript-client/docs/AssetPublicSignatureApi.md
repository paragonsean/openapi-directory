# NetlifysApiDocumentation.AssetPublicSignatureApi

All URIs are relative to *https://api.netlify.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSiteAssetPublicSignature**](AssetPublicSignatureApi.md#getSiteAssetPublicSignature) | **GET** /sites/{site_id}/assets/{asset_id}/public_signature | 



## getSiteAssetPublicSignature

> AssetPublicSignature getSiteAssetPublicSignature(siteId, assetId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.AssetPublicSignatureApi();
let siteId = "siteId_example"; // String | 
let assetId = "assetId_example"; // String | 
apiInstance.getSiteAssetPublicSignature(siteId, assetId, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **assetId** | **String**|  | 

### Return type

[**AssetPublicSignature**](AssetPublicSignature.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

