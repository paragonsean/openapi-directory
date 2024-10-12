# ChecksApi.MediaApi

All URIs are relative to *https://checks.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checksMediaUpload**](MediaApi.md#checksMediaUpload) | **POST** /v1alpha/{parent}/reports:analyzeUpload | 



## checksMediaUpload

> Operation checksMediaUpload(parent, opts)



Analyzes the uploaded app bundle and returns a google.longrunning.Operation containing the generated Report. ## Example (upload only) Send a regular POST request with the header &#x60;X-Goog-Upload-Protocol: raw&#x60;. &#x60;&#x60;&#x60; POST https://checks.googleapis.com/upload/v1alpha/{parent&#x3D;accounts/_*_/apps/_*}/reports:analyzeUpload HTTP/1.1 X-Goog-Upload-Protocol: raw Content-Length: Content-Type: application/octet-stream &#x60;&#x60;&#x60; ## Example (upload with metadata) Send a multipart POST request where the first body part contains the metadata JSON and the second body part contains the binary upload. Include the header &#x60;X-Goog-Upload-Protocol: multipart&#x60;. &#x60;&#x60;&#x60; POST https://checks.googleapis.com/upload/v1alpha/{parent&#x3D;accounts/_*_/apps/_*}/reports:analyzeUpload HTTP/1.1 X-Goog-Upload-Protocol: multipart Content-Length: ? Content-Type: multipart/related; boundary&#x3D;BOUNDARY --BOUNDARY Content-Type: application/json {\&quot;code_reference_id\&quot;:\&quot;db5bcc20f94055fb5bc08cbb9b0e7a5530308786\&quot;} --BOUNDARY --BOUNDARY-- &#x60;&#x60;&#x60; *Note:* Metadata-only requests are not supported. 

### Example

```javascript
import ChecksApi from 'checks_api';

let apiInstance = new ChecksApi.MediaApi();
let parent = "parent_example"; // String | Required. Resource name of the app. Example: `accounts/123/apps/456`
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
  'googleChecksReportV1alphaAnalyzeUploadRequest': new ChecksApi.GoogleChecksReportV1alphaAnalyzeUploadRequest() // GoogleChecksReportV1alphaAnalyzeUploadRequest | 
};
apiInstance.checksMediaUpload(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Resource name of the app. Example: &#x60;accounts/123/apps/456&#x60; | 
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
 **googleChecksReportV1alphaAnalyzeUploadRequest** | [**GoogleChecksReportV1alphaAnalyzeUploadRequest**](GoogleChecksReportV1alphaAnalyzeUploadRequest.md)|  | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json

