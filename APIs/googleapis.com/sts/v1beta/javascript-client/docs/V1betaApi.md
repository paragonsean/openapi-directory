# SecurityTokenServiceApi.V1betaApi

All URIs are relative to *https://sts.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stsToken**](V1betaApi.md#stsToken) | **POST** /v1beta/token | 



## stsToken

> GoogleIdentityStsV1betaExchangeTokenResponse stsToken(opts)



Exchanges a credential for a Google OAuth 2.0 access token. The token asserts an external identity within a workload identity pool, or it applies a Credential Access Boundary to a Google access token. When you call this method, do not send the &#x60;Authorization&#x60; HTTP header in the request. This method does not require the &#x60;Authorization&#x60; header, and using the header can cause the request to fail.

### Example

```javascript
import SecurityTokenServiceApi from 'security_token_service_api';

let apiInstance = new SecurityTokenServiceApi.V1betaApi();
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
  'googleIdentityStsV1betaExchangeTokenRequest': new SecurityTokenServiceApi.GoogleIdentityStsV1betaExchangeTokenRequest() // GoogleIdentityStsV1betaExchangeTokenRequest | 
};
apiInstance.stsToken(opts, (error, data, response) => {
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
 **googleIdentityStsV1betaExchangeTokenRequest** | [**GoogleIdentityStsV1betaExchangeTokenRequest**](GoogleIdentityStsV1betaExchangeTokenRequest.md)|  | [optional] 

### Return type

[**GoogleIdentityStsV1betaExchangeTokenResponse**](GoogleIdentityStsV1betaExchangeTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

