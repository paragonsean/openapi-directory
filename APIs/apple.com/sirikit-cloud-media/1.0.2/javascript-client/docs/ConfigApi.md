# SiriKitCloudMedia.ConfigApi

All URIs are relative to *https://cloudextension-testservice.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extensionConfiguration**](ConfigApi.md#extensionConfiguration) | **GET** /configuration | Configuration Resource



## extensionConfiguration

> ExtensionConfig extensionConfiguration(xApplecloudextensionSessionId, requestTimeout, userAgent, acceptLanguage, cacheControl, opts)

Configuration Resource

### Example

```javascript
import SiriKitCloudMedia from 'siri_kit_cloud_media';

let apiInstance = new SiriKitCloudMedia.ConfigApi();
let xApplecloudextensionSessionId = "xApplecloudextensionSessionId_example"; // String | 
let requestTimeout = 3.4; // Number | 
let userAgent = "userAgent_example"; // String | 
let acceptLanguage = "acceptLanguage_example"; // String | 
let cacheControl = "cacheControl_example"; // String | 
let opts = {
  'xApplecloudextensionRetryCount': 3.4, // Number | 
  'ifNoneMatch': "ifNoneMatch_example" // String | 
};
apiInstance.extensionConfiguration(xApplecloudextensionSessionId, requestTimeout, userAgent, acceptLanguage, cacheControl, opts, (error, data, response) => {
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
 **xApplecloudextensionSessionId** | **String**|  | 
 **requestTimeout** | **Number**|  | 
 **userAgent** | **String**|  | 
 **acceptLanguage** | **String**|  | 
 **cacheControl** | **String**|  | 
 **xApplecloudextensionRetryCount** | **Number**|  | [optional] 
 **ifNoneMatch** | **String**|  | [optional] 

### Return type

[**ExtensionConfig**](ExtensionConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/jose

