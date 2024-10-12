# AltoroJRestApi.Class4FeedbackApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getFeedback**](Class4FeedbackApi.md#getFeedback) | **GET** /feedback/{feedbackId} | 
[**sendFeedback**](Class4FeedbackApi.md#sendFeedback) | **POST** /feedback/submit | 



## getFeedback

> getFeedback(authorization, feedbackId)



Retrieve feedback

### Example

```javascript
import AltoroJRestApi from 'altoro_j_rest_api';

let apiInstance = new AltoroJRestApi.Class4FeedbackApi();
let authorization = "authorization_example"; // String | Authorization token (provided upon successful login)
let feedbackId = "feedbackId_example"; // String | 
apiInstance.getFeedback(authorization, feedbackId, (error, data, response) => {
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
 **authorization** | **String**| Authorization token (provided upon successful login) | 
 **feedbackId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## sendFeedback

> sendFeedback(body)



Submit feedback for the bank

### Example

```javascript
import AltoroJRestApi from 'altoro_j_rest_api';

let apiInstance = new AltoroJRestApi.Class4FeedbackApi();
let body = new AltoroJRestApi.Feedback(); // Feedback | Feedback details including name, email the subject and complete message
apiInstance.sendFeedback(body, (error, data, response) => {
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
 **body** | [**Feedback**](Feedback.md)| Feedback details including name, email the subject and complete message | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

