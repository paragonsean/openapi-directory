# SiriKitCloudMedia.QueuesApi

All URIs are relative to *https://cloudextension-testservice.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**playMediaOnQueue**](QueuesApi.md#playMediaOnQueue) | **POST** /queues/playMedia | playMedia
[**updateActivityOnQueue**](QueuesApi.md#updateActivityOnQueue) | **POST** /queues/updateActivity | updateActivity



## playMediaOnQueue

> Queue playMediaOnQueue(xApplecloudextensionSessionId, userAgent, acceptLanguage, opts)

playMedia

### Example

```javascript
import SiriKitCloudMedia from 'siri_kit_cloud_media';

let apiInstance = new SiriKitCloudMedia.QueuesApi();
let xApplecloudextensionSessionId = "xApplecloudextensionSessionId_example"; // String | 
let userAgent = "userAgent_example"; // String | 
let acceptLanguage = "acceptLanguage_example"; // String | 
let opts = {
  'xApplecloudextensionRetryCount': 3.4, // Number | 
  'playMediaRequest': new SiriKitCloudMedia.PlayMediaRequest() // PlayMediaRequest | 
};
apiInstance.playMediaOnQueue(xApplecloudextensionSessionId, userAgent, acceptLanguage, opts, (error, data, response) => {
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
 **userAgent** | **String**|  | 
 **acceptLanguage** | **String**|  | 
 **xApplecloudextensionRetryCount** | **Number**|  | [optional] 
 **playMediaRequest** | [**PlayMediaRequest**](PlayMediaRequest.md)|  | [optional] 

### Return type

[**Queue**](Queue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateActivityOnQueue

> UpdateActivityResponse updateActivityOnQueue(xApplecloudextensionSessionId, userAgent, acceptLanguage, opts)

updateActivity

### Example

```javascript
import SiriKitCloudMedia from 'siri_kit_cloud_media';

let apiInstance = new SiriKitCloudMedia.QueuesApi();
let xApplecloudextensionSessionId = "xApplecloudextensionSessionId_example"; // String | 
let userAgent = "userAgent_example"; // String | 
let acceptLanguage = "acceptLanguage_example"; // String | 
let opts = {
  'xApplecloudextensionRetryCount': 3.4, // Number | 
  'updateActivityRequest': new SiriKitCloudMedia.UpdateActivityRequest() // UpdateActivityRequest | 
};
apiInstance.updateActivityOnQueue(xApplecloudextensionSessionId, userAgent, acceptLanguage, opts, (error, data, response) => {
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
 **userAgent** | **String**|  | 
 **acceptLanguage** | **String**|  | 
 **xApplecloudextensionRetryCount** | **Number**|  | [optional] 
 **updateActivityRequest** | [**UpdateActivityRequest**](UpdateActivityRequest.md)|  | [optional] 

### Return type

[**UpdateActivityResponse**](UpdateActivityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

