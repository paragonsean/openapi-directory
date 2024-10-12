# ClassicPlatformsNotifications.OtherApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postPAYMENTFAILURE**](OtherApi.md#postPAYMENTFAILURE) | **POST** /PAYMENT_FAILURE | Booking for a capture or refund failed
[**postREPORTAVAILABLE**](OtherApi.md#postREPORTAVAILABLE) | **POST** /REPORT_AVAILABLE | Report available



## postPAYMENTFAILURE

> NotificationResponse postPAYMENTFAILURE(opts)

Booking for a capture or refund failed

Adyen sends this notification when a [split payment](https://docs.adyen.com/marketplaces-and-platforms/classic/processing-payments#providing-split-information) booking for a capture or refund fails. When a booking fails due to an invalid account status or an unknown &#x60;accountCode&#x60;, the funds are credited or debited to or fromyour platform&#39;s liable account instead of the account specified in the split data.

### Example

```javascript
import ClassicPlatformsNotifications from 'classic_platforms_notifications';
let defaultClient = ClassicPlatformsNotifications.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ClassicPlatformsNotifications.OtherApi();
let opts = {
  'paymentFailureNotification': new ClassicPlatformsNotifications.PaymentFailureNotification() // PaymentFailureNotification | 
};
apiInstance.postPAYMENTFAILURE(opts, (error, data, response) => {
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
 **paymentFailureNotification** | [**PaymentFailureNotification**](PaymentFailureNotification.md)|  | [optional] 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postREPORTAVAILABLE

> NotificationResponse postREPORTAVAILABLE(opts)

Report available

Adyen sends this notification when a report has been generated and it is available for download.

### Example

```javascript
import ClassicPlatformsNotifications from 'classic_platforms_notifications';
let defaultClient = ClassicPlatformsNotifications.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ClassicPlatformsNotifications.OtherApi();
let opts = {
  'reportAvailableNotification': new ClassicPlatformsNotifications.ReportAvailableNotification() // ReportAvailableNotification | 
};
apiInstance.postREPORTAVAILABLE(opts, (error, data, response) => {
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
 **reportAvailableNotification** | [**ReportAvailableNotification**](ReportAvailableNotification.md)|  | [optional] 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

