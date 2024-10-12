# Semantria.SubscriptionApi

All URIs are relative to *https://api.semantria.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSubscription**](SubscriptionApi.md#getSubscription) | **GET** /subscription.{content_type} | Retrieve subscription details



## getSubscription

> Subscription getSubscription(contentType)

Retrieve subscription details

This method retrieves user&#39;s subscription details that consist of the list of allowed features, configured limits and options on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.SubscriptionApi();
let contentType = "contentType_example"; // String | 
apiInstance.getSubscription(contentType, (error, data, response) => {
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
 **contentType** | **String**|  | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

