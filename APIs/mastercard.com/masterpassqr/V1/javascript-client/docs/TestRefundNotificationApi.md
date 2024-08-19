# SendPersonToMerchant.TestRefundNotificationApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sendNotificationRefundRetry**](TestRefundNotificationApi.md#sendNotificationRefundRetry) | **POST** /send/v1/partners/{partnerId}/events/generate/refund | Client can simulate a Mastercard Merchant Presented QR Refund notification to the registered URL endpoint. 



## sendNotificationRefundRetry

> NotificationResponse166Wrapper sendNotificationRefundRetry(partnerId, opts)

Client can simulate a Mastercard Merchant Presented QR Refund notification to the registered URL endpoint. 

Client can simulate a Mastercard Merchant Presented QR Refund notification to the registered URL endpoint. 

### Example

```javascript
import SendPersonToMerchant from 'send_person_to_merchant';

let apiInstance = new SendPersonToMerchant.TestRefundNotificationApi();
let partnerId = "partnerId_example"; // String | Path Param - Provider assigned partner id. Details - string, 32
let opts = {
  'notificationRequest': new SendPersonToMerchant.NotificationRequest163Wrapper() // NotificationRequest163Wrapper | Contains the details of the request message.
};
apiInstance.sendNotificationRefundRetry(partnerId, opts, (error, data, response) => {
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
 **notificationRequest** | [**NotificationRequest163Wrapper**](NotificationRequest163Wrapper.md)| Contains the details of the request message. | [optional] 

### Return type

[**NotificationResponse166Wrapper**](NotificationResponse166Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/xml
- **Accept**: N/A

