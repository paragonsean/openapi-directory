# FrankieFinancialApi.PushNotificationApi

All URIs are relative to *https://api.demo.frankiefinancial.io/compliance/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notifyResult**](PushNotificationApi.md#notifyResult) | **POST** /your/configured/path/{requestId} | Push Notification Payload



## notifyResult

> notifyResult(requestId, opts)

Push Notification Payload

Whenever you request that a transaction be put into the background, there needs to be a mechanism for notifying you that the request has been completed. This notification will push you the high-level details of the result, and you can then query the results at your leisiure.  The same notification process will also be used to push alerts to your system. This means that RequestIDs may not match your records 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';

let apiInstance = new FrankieFinancialApi.PushNotificationApi();
let requestId = "requestId_example"; // String | This will be the same RequestId that was sent in the 202 acceptance response. 
let opts = {
  'notifcationResult': new FrankieFinancialApi.NotificationResultObject() // NotificationResultObject | 
};
apiInstance.notifyResult(requestId, opts, (error, data, response) => {
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
 **requestId** | **String**| This will be the same RequestId that was sent in the 202 acceptance response.  | 
 **notifcationResult** | [**NotificationResultObject**](NotificationResultObject.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

