# GooglePlayGroupingApi.AppsApi

All URIs are relative to *https://playgrouping.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**playgroupingAppsTokensTagsCreateOrUpdate**](AppsApi.md#playgroupingAppsTokensTagsCreateOrUpdate) | **POST** /v1alpha1/{appPackage}/{token}/tags:createOrUpdate | 
[**playgroupingAppsTokensVerify**](AppsApi.md#playgroupingAppsTokensVerify) | **POST** /v1alpha1/{appPackage}/{token}:verify | 



## playgroupingAppsTokensTagsCreateOrUpdate

> CreateOrUpdateTagsResponse playgroupingAppsTokensTagsCreateOrUpdate(appPackage, token, opts)



Create or update tags for the user and app that are represented by the given token.

### Example

```javascript
import GooglePlayGroupingApi from 'google_play_grouping_api';

let apiInstance = new GooglePlayGroupingApi.AppsApi();
let appPackage = "appPackage_example"; // String | Required. App whose tags are being manipulated. Format: apps/{package_name}
let token = "token_example"; // String | Required. Token for which the tags are being inserted or updated. Format: tokens/{token}
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
  'createOrUpdateTagsRequest': new GooglePlayGroupingApi.CreateOrUpdateTagsRequest() // CreateOrUpdateTagsRequest | 
};
apiInstance.playgroupingAppsTokensTagsCreateOrUpdate(appPackage, token, opts, (error, data, response) => {
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
 **appPackage** | **String**| Required. App whose tags are being manipulated. Format: apps/{package_name} | 
 **token** | **String**| Required. Token for which the tags are being inserted or updated. Format: tokens/{token} | 
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
 **createOrUpdateTagsRequest** | [**CreateOrUpdateTagsRequest**](CreateOrUpdateTagsRequest.md)|  | [optional] 

### Return type

[**CreateOrUpdateTagsResponse**](CreateOrUpdateTagsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## playgroupingAppsTokensVerify

> Object playgroupingAppsTokensVerify(appPackage, token, opts)



Verify an API token by asserting the app and persona it belongs to. The verification is a protection against client-side attacks and will fail if the contents of the token don&#39;t match the provided values. A token must be verified before it can be used to manipulate user tags.

### Example

```javascript
import GooglePlayGroupingApi from 'google_play_grouping_api';

let apiInstance = new GooglePlayGroupingApi.AppsApi();
let appPackage = "appPackage_example"; // String | Required. App the token belongs to. Format: apps/{package_name}
let token = "token_example"; // String | Required. The token to be verified. Format: tokens/{token}
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
  'verifyTokenRequest': new GooglePlayGroupingApi.VerifyTokenRequest() // VerifyTokenRequest | 
};
apiInstance.playgroupingAppsTokensVerify(appPackage, token, opts, (error, data, response) => {
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
 **appPackage** | **String**| Required. App the token belongs to. Format: apps/{package_name} | 
 **token** | **String**| Required. The token to be verified. Format: tokens/{token} | 
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
 **verifyTokenRequest** | [**VerifyTokenRequest**](VerifyTokenRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

