# SiriKitCloudMedia.IntentApi

All URIs are relative to *https://cloudextension-testservice.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addMediaIntentHandling**](IntentApi.md#addMediaIntentHandling) | **POST** /intent/addMedia | addMedia
[**playMediaIntentHandling**](IntentApi.md#playMediaIntentHandling) | **POST** /intent/playMedia | playMedia
[**updateMediaAffinityIntentHandling**](IntentApi.md#updateMediaAffinityIntentHandling) | **POST** /intent/updateMediaAffinity | updateMediaAffinity



## addMediaIntentHandling

> [AddMediaIntentHandlingInvocationResponse] addMediaIntentHandling(xApplecloudextensionSessionId, requestTimeout, userAgent, acceptLanguage, opts)

addMedia

### Example

```javascript
import SiriKitCloudMedia from 'siri_kit_cloud_media';

let apiInstance = new SiriKitCloudMedia.IntentApi();
let xApplecloudextensionSessionId = "xApplecloudextensionSessionId_example"; // String | 
let requestTimeout = 3.4; // Number | 
let userAgent = "userAgent_example"; // String | 
let acceptLanguage = "acceptLanguage_example"; // String | 
let opts = {
  'xApplecloudextensionRetryCount': 3.4, // Number | 
  'addMediaIntentHandlingInvocation': [new SiriKitCloudMedia.AddMediaIntentHandlingInvocation()] // [AddMediaIntentHandlingInvocation] | 
};
apiInstance.addMediaIntentHandling(xApplecloudextensionSessionId, requestTimeout, userAgent, acceptLanguage, opts, (error, data, response) => {
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
 **xApplecloudextensionRetryCount** | **Number**|  | [optional] 
 **addMediaIntentHandlingInvocation** | [**[AddMediaIntentHandlingInvocation]**](AddMediaIntentHandlingInvocation.md)|  | [optional] 

### Return type

[**[AddMediaIntentHandlingInvocationResponse]**](AddMediaIntentHandlingInvocationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## playMediaIntentHandling

> [PlayMediaIntentHandlingInvocationResponse] playMediaIntentHandling(xApplecloudextensionSessionId, requestTimeout, userAgent, acceptLanguage, opts)

playMedia

### Example

```javascript
import SiriKitCloudMedia from 'siri_kit_cloud_media';

let apiInstance = new SiriKitCloudMedia.IntentApi();
let xApplecloudextensionSessionId = "xApplecloudextensionSessionId_example"; // String | 
let requestTimeout = 3.4; // Number | 
let userAgent = "userAgent_example"; // String | 
let acceptLanguage = "acceptLanguage_example"; // String | 
let opts = {
  'xApplecloudextensionRetryCount': 3.4, // Number | 
  'playMediaIntentHandlingInvocation': [new SiriKitCloudMedia.PlayMediaIntentHandlingInvocation()] // [PlayMediaIntentHandlingInvocation] | 
};
apiInstance.playMediaIntentHandling(xApplecloudextensionSessionId, requestTimeout, userAgent, acceptLanguage, opts, (error, data, response) => {
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
 **xApplecloudextensionRetryCount** | **Number**|  | [optional] 
 **playMediaIntentHandlingInvocation** | [**[PlayMediaIntentHandlingInvocation]**](PlayMediaIntentHandlingInvocation.md)|  | [optional] 

### Return type

[**[PlayMediaIntentHandlingInvocationResponse]**](PlayMediaIntentHandlingInvocationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMediaAffinityIntentHandling

> [UpdateMediaAffinityIntentHandlingInvocationResponse] updateMediaAffinityIntentHandling(xApplecloudextensionSessionId, requestTimeout, userAgent, acceptLanguage, opts)

updateMediaAffinity

### Example

```javascript
import SiriKitCloudMedia from 'siri_kit_cloud_media';

let apiInstance = new SiriKitCloudMedia.IntentApi();
let xApplecloudextensionSessionId = "xApplecloudextensionSessionId_example"; // String | 
let requestTimeout = 3.4; // Number | 
let userAgent = "userAgent_example"; // String | 
let acceptLanguage = "acceptLanguage_example"; // String | 
let opts = {
  'xApplecloudextensionRetryCount': 3.4, // Number | 
  'updateMediaAffinityIntentHandlingInvocation': [new SiriKitCloudMedia.UpdateMediaAffinityIntentHandlingInvocation()] // [UpdateMediaAffinityIntentHandlingInvocation] | 
};
apiInstance.updateMediaAffinityIntentHandling(xApplecloudextensionSessionId, requestTimeout, userAgent, acceptLanguage, opts, (error, data, response) => {
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
 **xApplecloudextensionRetryCount** | **Number**|  | [optional] 
 **updateMediaAffinityIntentHandlingInvocation** | [**[UpdateMediaAffinityIntentHandlingInvocation]**](UpdateMediaAffinityIntentHandlingInvocation.md)|  | [optional] 

### Return type

[**[UpdateMediaAffinityIntentHandlingInvocationResponse]**](UpdateMediaAffinityIntentHandlingInvocationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

