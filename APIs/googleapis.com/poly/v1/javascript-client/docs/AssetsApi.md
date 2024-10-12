# PolyApi.AssetsApi

All URIs are relative to *https://poly.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**polyAssetsGet**](AssetsApi.md#polyAssetsGet) | **GET** /v1/{name} | 
[**polyAssetsList**](AssetsApi.md#polyAssetsList) | **GET** /v1/assets | 



## polyAssetsGet

> Asset polyAssetsGet(name, opts)



Returns detailed information about an asset given its name. PRIVATE assets are returned only if the currently authenticated user (via OAuth token) is the author of the asset.

### Example

```javascript
import PolyApi from 'poly_api';

let apiInstance = new PolyApi.AssetsApi();
let name = "name_example"; // String | Required. An asset's name in the form `assets/{ASSET_ID}`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.polyAssetsGet(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. An asset&#39;s name in the form &#x60;assets/{ASSET_ID}&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## polyAssetsList

> ListAssetsResponse polyAssetsList(opts)



Lists all public, remixable assets. These are assets with an access level of PUBLIC and published under the CC-By license.

### Example

```javascript
import PolyApi from 'poly_api';

let apiInstance = new PolyApi.AssetsApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'category': "category_example", // String | Filter assets based on the specified category. Supported values are: `animals`, `architecture`, `art`, `food`, `nature`, `objects`, `people`, `scenes`, `technology`, and `transport`.
  'curated': true, // Boolean | Return only assets that have been curated by the Poly team.
  'format': "format_example", // String | Return only assets with the matching format. Acceptable values are: `BLOCKS`, `FBX`, `GLTF`, `GLTF2`, `OBJ`, `TILT`.
  'keywords': "keywords_example", // String | One or more search terms to be matched against all text that Poly has indexed for assets, which includes display_name, description, and tags. Multiple keywords should be separated by spaces.
  'maxComplexity': "maxComplexity_example", // String | Returns assets that are of the specified complexity or less. Defaults to COMPLEX. For example, a request for MEDIUM assets also includes SIMPLE assets.
  'orderBy': "orderBy_example", // String | Specifies an ordering for assets. Acceptable values are: `BEST`, `NEWEST`, `OLDEST`. Defaults to `BEST`, which ranks assets based on a combination of popularity and other features.
  'pageSize': 56, // Number | The maximum number of assets to be returned. This value must be between `1` and `100`. Defaults to `20`.
  'pageToken': "pageToken_example" // String | Specifies a continuation token from a previous search whose results were split into multiple pages. To get the next page, submit the same request specifying the value from next_page_token.
};
apiInstance.polyAssetsList(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **category** | **String**| Filter assets based on the specified category. Supported values are: &#x60;animals&#x60;, &#x60;architecture&#x60;, &#x60;art&#x60;, &#x60;food&#x60;, &#x60;nature&#x60;, &#x60;objects&#x60;, &#x60;people&#x60;, &#x60;scenes&#x60;, &#x60;technology&#x60;, and &#x60;transport&#x60;. | [optional] 
 **curated** | **Boolean**| Return only assets that have been curated by the Poly team. | [optional] 
 **format** | **String**| Return only assets with the matching format. Acceptable values are: &#x60;BLOCKS&#x60;, &#x60;FBX&#x60;, &#x60;GLTF&#x60;, &#x60;GLTF2&#x60;, &#x60;OBJ&#x60;, &#x60;TILT&#x60;. | [optional] 
 **keywords** | **String**| One or more search terms to be matched against all text that Poly has indexed for assets, which includes display_name, description, and tags. Multiple keywords should be separated by spaces. | [optional] 
 **maxComplexity** | **String**| Returns assets that are of the specified complexity or less. Defaults to COMPLEX. For example, a request for MEDIUM assets also includes SIMPLE assets. | [optional] 
 **orderBy** | **String**| Specifies an ordering for assets. Acceptable values are: &#x60;BEST&#x60;, &#x60;NEWEST&#x60;, &#x60;OLDEST&#x60;. Defaults to &#x60;BEST&#x60;, which ranks assets based on a combination of popularity and other features. | [optional] 
 **pageSize** | **Number**| The maximum number of assets to be returned. This value must be between &#x60;1&#x60; and &#x60;100&#x60;. Defaults to &#x60;20&#x60;. | [optional] 
 **pageToken** | **String**| Specifies a continuation token from a previous search whose results were split into multiple pages. To get the next page, submit the same request specifying the value from next_page_token. | [optional] 

### Return type

[**ListAssetsResponse**](ListAssetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

