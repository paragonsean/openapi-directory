# SendPersonToMerchant.TestPaymentNotificationApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sendNotificationPaymentRetry**](TestPaymentNotificationApi.md#sendNotificationPaymentRetry) | **POST** /send/v1/partners/{partnerId}/events/generate/payment | Client can simulate a Mastercard Merchant Presented QR Payment notification to the registered URL endpoint. 



## sendNotificationPaymentRetry

> NotificationResponse162Wrapper sendNotificationPaymentRetry(partnerId, opts)

Client can simulate a Mastercard Merchant Presented QR Payment notification to the registered URL endpoint. 

Client can simulate a Mastercard Merchant Presented QR Payment notification to the registered URL endpoint. 

### Example

```javascript
import SendPersonToMerchant from 'send_person_to_merchant';

let apiInstance = new SendPersonToMerchant.TestPaymentNotificationApi();
let partnerId = "partnerId_example"; // String | Path Param - Provider assigned partner id. Details - string, 32
let opts = {
  'notificationRequest': new SendPersonToMerchant.NotificationRequest159Wrapper() // NotificationRequest159Wrapper | Contains the details of the request message.
};
apiInstance.sendNotificationPaymentRetry(partnerId, opts, (error, data, response) => {
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
 **partnerId** | **String**| Path Param - Provider assigned partner id. Details - string, 32 | 
 **notificationRequest** | [**NotificationRequest159Wrapper**](NotificationRequest159Wrapper.md)| Contains the details of the request message. | [optional] 

### Return type

[**NotificationResponse162Wrapper**](NotificationResponse162Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/xml
- **Accept**: N/A

