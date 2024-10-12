# NetlifysApiDocumentation.AssetApi

All URIs are relative to *https://api.netlify.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSiteAsset**](AssetApi.md#createSiteAsset) | **POST** /sites/{site_id}/assets | 
[**deleteSiteAsset**](AssetApi.md#deleteSiteAsset) | **DELETE** /sites/{site_id}/assets/{asset_id} | 
[**getSiteAssetInfo**](AssetApi.md#getSiteAssetInfo) | **GET** /sites/{site_id}/assets/{asset_id} | 
[**listSiteAssets**](AssetApi.md#listSiteAssets) | **GET** /sites/{site_id}/assets | 
[**updateSiteAsset**](AssetApi.md#updateSiteAsset) | **PUT** /sites/{site_id}/assets/{asset_id} | 



## createSiteAsset

> AssetSignature createSiteAsset(siteId, name, size, contentType, opts)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.AssetApi();
let siteId = "siteId_example"; // String | 
let name = "name_example"; // String | 
let size = 789; // Number | 
let contentType = "contentType_example"; // String | 
let opts = {
  'visibility': "visibility_example" // String | 
};
apiInstance.createSiteAsset(siteId, name, size, contentType, opts, (error, data, response) => {
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
 **name** | **String**|  | 
 **size** | **Number**|  | 
 **contentType** | **String**|  | 
 **visibility** | **String**|  | [optional] 

### Return type

[**AssetSignature**](AssetSignature.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSiteAsset

> deleteSiteAsset(siteId, assetId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.AssetApi();
let siteId = "siteId_example"; // String | 
let assetId = "assetId_example"; // String | 
apiInstance.deleteSiteAsset(siteId, assetId, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **assetId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSiteAssetInfo

> Asset getSiteAssetInfo(siteId, assetId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.AssetApi();
let siteId = "siteId_example"; // String | 
let assetId = "assetId_example"; // String | 
apiInstance.getSiteAssetInfo(siteId, assetId, (error, data, response) => {
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

[**Asset**](Asset.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSiteAssets

> [Asset] listSiteAssets(siteId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.AssetApi();
let siteId = "siteId_example"; // String | 
apiInstance.listSiteAssets(siteId, (error, data, response) => {
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

### Return type

[**[Asset]**](Asset.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSiteAsset

> Asset updateSiteAsset(siteId, assetId, state)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.AssetApi();
let siteId = "siteId_example"; // String | 
let assetId = "assetId_example"; // String | 
let state = "state_example"; // String | 
apiInstance.updateSiteAsset(siteId, assetId, state, (error, data, response) => {
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
 **state** | **String**|  | 

### Return type

[**Asset**](Asset.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

