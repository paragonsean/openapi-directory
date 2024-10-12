# PolyApi.UsersApi

All URIs are relative to *https://poly.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**polyUsersAssetsList**](UsersApi.md#polyUsersAssetsList) | **GET** /v1/{name}/assets | 
[**polyUsersLikedassetsList**](UsersApi.md#polyUsersLikedassetsList) | **GET** /v1/{name}/likedassets | 



## polyUsersAssetsList

> ListUserAssetsResponse polyUsersAssetsList(name, opts)



Lists assets authored by the given user. Only the value &#39;me&#39;, representing the currently-authenticated user, is supported. May include assets with an access level of PRIVATE or UNLISTED and assets which are All Rights Reserved for the currently-authenticated user.

### Example

```javascript
import PolyApi from 'poly_api';

let apiInstance = new PolyApi.UsersApi();
let name = "name_example"; // String | A valid user id. Currently, only the special value 'me', representing the currently-authenticated user is supported. To use 'me', you must pass an OAuth token with the request.
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
  'format': "format_example", // String | Return only assets with the matching format. Acceptable values are: `BLOCKS`, `FBX`, `GLTF`, `GLTF2`, `OBJ`, and `TILT`.
  'orderBy': "orderBy_example", // String | Specifies an ordering for assets. Acceptable values are: `BEST`, `NEWEST`, `OLDEST`. Defaults to `BEST`, which ranks assets based on a combination of popularity and other features.
  'pageSize': 56, // Number | The maximum number of assets to be returned. This value must be between `1` and `100`. Defaults to `20`.
  'pageToken': "pageToken_example", // String | Specifies a continuation token from a previous search whose results were split into multiple pages. To get the next page, submit the same request specifying the value from next_page_token.
  'visibility': "visibility_example" // String | The visibility of the assets to be returned. Defaults to VISIBILITY_UNSPECIFIED which returns all assets.
};
apiInstance.polyUsersAssetsList(name, opts, (error, data, response) => {
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
 **name** | **String**| A valid user id. Currently, only the special value &#39;me&#39;, representing the currently-authenticated user is supported. To use &#39;me&#39;, you must pass an OAuth token with the request. | 
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
 **format** | **String**| Return only assets with the matching format. Acceptable values are: &#x60;BLOCKS&#x60;, &#x60;FBX&#x60;, &#x60;GLTF&#x60;, &#x60;GLTF2&#x60;, &#x60;OBJ&#x60;, and &#x60;TILT&#x60;. | [optional] 
 **orderBy** | **String**| Specifies an ordering for assets. Acceptable values are: &#x60;BEST&#x60;, &#x60;NEWEST&#x60;, &#x60;OLDEST&#x60;. Defaults to &#x60;BEST&#x60;, which ranks assets based on a combination of popularity and other features. | [optional] 
 **pageSize** | **Number**| The maximum number of assets to be returned. This value must be between &#x60;1&#x60; and &#x60;100&#x60;. Defaults to &#x60;20&#x60;. | [optional] 
 **pageToken** | **String**| Specifies a continuation token from a previous search whose results were split into multiple pages. To get the next page, submit the same request specifying the value from next_page_token. | [optional] 
 **visibility** | **String**| The visibility of the assets to be returned. Defaults to VISIBILITY_UNSPECIFIED which returns all assets. | [optional] 

### Return type

[**ListUserAssetsResponse**](ListUserAssetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## polyUsersLikedassetsList

> ListLikedAssetsResponse polyUsersLikedassetsList(name, opts)



Lists assets that the user has liked. Only the value &#39;me&#39;, representing the currently-authenticated user, is supported. May include assets with an access level of UNLISTED.

### Example

```javascript
import PolyApi from 'poly_api';

let apiInstance = new PolyApi.UsersApi();
let name = "name_example"; // String | A valid user id. Currently, only the special value 'me', representing the currently-authenticated user is supported. To use 'me', you must pass an OAuth token with the request.
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
  'format': "format_example", // String | Return only assets with the matching format. Acceptable values are: `BLOCKS`, `FBX`, `GLTF`, `GLTF2`, `OBJ`, `TILT`.
  'orderBy': "orderBy_example", // String | Specifies an ordering for assets. Acceptable values are: `BEST`, `NEWEST`, `OLDEST`, 'LIKED_TIME'. Defaults to `LIKED_TIME`, which ranks assets based on how recently they were liked.
  'pageSize': 56, // Number | The maximum number of assets to be returned. This value must be between `1` and `100`. Defaults to `20`.
  'pageToken': "pageToken_example" // String | Specifies a continuation token from a previous search whose results were split into multiple pages. To get the next page, submit the same request specifying the value from next_page_token.
};
apiInstance.polyUsersLikedassetsList(name, opts, (error, data, response) => {
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
 **name** | **String**| A valid user id. Currently, only the special value &#39;me&#39;, representing the currently-authenticated user is supported. To use &#39;me&#39;, you must pass an OAuth token with the request. | 
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
 **format** | **String**| Return only assets with the matching format. Acceptable values are: &#x60;BLOCKS&#x60;, &#x60;FBX&#x60;, &#x60;GLTF&#x60;, &#x60;GLTF2&#x60;, &#x60;OBJ&#x60;, &#x60;TILT&#x60;. | [optional] 
 **orderBy** | **String**| Specifies an ordering for assets. Acceptable values are: &#x60;BEST&#x60;, &#x60;NEWEST&#x60;, &#x60;OLDEST&#x60;, &#39;LIKED_TIME&#39;. Defaults to &#x60;LIKED_TIME&#x60;, which ranks assets based on how recently they were liked. | [optional] 
 **pageSize** | **Number**| The maximum number of assets to be returned. This value must be between &#x60;1&#x60; and &#x60;100&#x60;. Defaults to &#x60;20&#x60;. | [optional] 
 **pageToken** | **String**| Specifies a continuation token from a previous search whose results were split into multiple pages. To get the next page, submit the same request specifying the value from next_page_token. | [optional] 

### Return type

[**ListLikedAssetsResponse**](ListLikedAssetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

