# Reverb.FeedbackApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**feedbackFeedbackIdGet**](FeedbackApi.md#feedbackFeedbackIdGet) | **GET** /feedback/{feedback_id} | Feedback details



## feedbackFeedbackIdGet

> feedbackFeedbackIdGet(feedbackId)

Feedback details

Feedback details

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.FeedbackApi();
let feedbackId = "feedbackId_example"; // String | 
apiInstance.feedbackFeedbackIdGet(feedbackId, (error, data, response) => {
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
 **feedbackId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

