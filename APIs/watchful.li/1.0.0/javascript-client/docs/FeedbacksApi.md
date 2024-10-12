# WatchfulLi.FeedbacksApi

All URIs are relative to *https://watchful.li/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createFeedbacks**](FeedbacksApi.md#createFeedbacks) | **POST** /feedbacks | Create a feedback
[**getFeedbacks**](FeedbacksApi.md#getFeedbacks) | **GET** /feedbacks | Get feedbacks
[**getFieldsFeedbacks**](FeedbacksApi.md#getFieldsFeedbacks) | **GET** /feedbacks/metadata | Get the list of fields



## createFeedbacks

> Audit createFeedbacks(body)

Create a feedback

Create a feedback

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.FeedbacksApi();
let body = new WatchfulLi.Feedback(); // Feedback | JSON object Feedback
apiInstance.createFeedbacks(body, (error, data, response) => {
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
 **body** | [**Feedback**](Feedback.md)| JSON object Feedback | 

### Return type

[**Audit**](Audit.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## getFeedbacks

> Feedback getFeedbacks(opts)

Get feedbacks

Returns a list of feedbacks

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.FeedbacksApi();
let opts = {
  'fields': "fields_example" // String | Fields to return separate by comas (es. name,id)
};
apiInstance.getFeedbacks(opts, (error, data, response) => {
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
 **fields** | **String**| Fields to return separate by comas (es. name,id) | [optional] 

### Return type

[**Feedback**](Feedback.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## getFieldsFeedbacks

> String getFieldsFeedbacks()

Get the list of fields

Returns a list of fields

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.FeedbacksApi();
apiInstance.getFieldsFeedbacks((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain

