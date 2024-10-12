# TwilioNumbers.NumbersV2BulkHostedNumberOrderApi

All URIs are relative to *https://numbers.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchBulkHostedNumberOrder**](NumbersV2BulkHostedNumberOrderApi.md#fetchBulkHostedNumberOrder) | **GET** /v2/HostedNumber/Orders/Bulk/{BulkHostingSid} | 



## fetchBulkHostedNumberOrder

> NumbersV2BulkHostedNumberOrder fetchBulkHostedNumberOrder(bulkHostingSid, opts)



Fetch a specific BulkHostedNumberOrder.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV2BulkHostedNumberOrderApi();
let bulkHostingSid = "bulkHostingSid_example"; // String | A 34 character string that uniquely identifies this BulkHostedNumberOrder.
let opts = {
  'orderStatus': "orderStatus_example" // String | Order status can be used for filtering on Hosted Number Order status values. To see a complete list of order statuses, please check 'https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values'.
};
apiInstance.fetchBulkHostedNumberOrder(bulkHostingSid, opts, (error, data, response) => {
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
 **bulkHostingSid** | **String**| A 34 character string that uniquely identifies this BulkHostedNumberOrder. | 
 **orderStatus** | **String**| Order status can be used for filtering on Hosted Number Order status values. To see a complete list of order statuses, please check &#39;https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/hosted-number-order-resource#status-values&#39;. | [optional] 

### Return type

[**NumbersV2BulkHostedNumberOrder**](NumbersV2BulkHostedNumberOrder.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

