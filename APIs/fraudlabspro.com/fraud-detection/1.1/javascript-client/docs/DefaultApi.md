# FraudLabsProFraudDetection.DefaultApi

All URIs are relative to *https://api.fraudlabspro.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1OrderFeedbackPost**](DefaultApi.md#v1OrderFeedbackPost) | **POST** /v1/order/feedback | 
[**v1OrderScreenPost**](DefaultApi.md#v1OrderScreenPost) | **POST** /v1/order/screen | 



## v1OrderFeedbackPost

> String v1OrderFeedbackPost(id, key, action, opts)



Feedback the status of an order transaction.

### Example

```javascript
import FraudLabsProFraudDetection from 'fraud_labs_pro_fraud_detection';

let apiInstance = new FraudLabsProFraudDetection.DefaultApi();
let id = "id_example"; // String | 
let key = "key_example"; // String | 
let action = "action_example"; // String | 
let opts = {
  'format': "format_example", // String | 
  'notes': "notes_example" // String | 
};
apiInstance.v1OrderFeedbackPost(id, key, action, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **key** | **String**|  | 
 **action** | **String**|  | 
 **format** | **String**|  | [optional] 
 **notes** | **String**|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## v1OrderScreenPost

> String v1OrderScreenPost(ip, key, opts)



Screen order for payment fraud.

### Example

```javascript
import FraudLabsProFraudDetection from 'fraud_labs_pro_fraud_detection';

let apiInstance = new FraudLabsProFraudDetection.DefaultApi();
let ip = "ip_example"; // String | 
let key = "key_example"; // String | 
let opts = {
  'format': "format_example", // String | 
  'lastName': "lastName_example", // String | 
  'firstName': "firstName_example", // String | 
  'billAddr': "billAddr_example", // String | 
  'billCity': "billCity_example", // String | 
  'billState': "billState_example", // String | 
  'billCountry': "billCountry_example", // String | 
  'billZipCode': "billZipCode_example", // String | 
  'shipAddr': "shipAddr_example", // String | 
  'shipCity': "shipCity_example", // String | 
  'shipState': "shipState_example", // String | 
  'shipCountry': "shipCountry_example", // String | 
  'shipZipCode': "shipZipCode_example", // String | 
  'emailDomain': "emailDomain_example", // String | 
  'userPhone': "userPhone_example", // String | 
  'email': "email_example", // String | 
  'emailHash': "emailHash_example", // String | 
  'usernameHash': "usernameHash_example", // String | 
  'passwordHash': "passwordHash_example", // String | 
  'binNo': "binNo_example", // String | 
  'cardHash': "cardHash_example", // String | 
  'avsResult': "avsResult_example", // String | 
  'cvvResult': "cvvResult_example", // String | 
  'userOrderId': "userOrderId_example", // String | 
  'userOrderMemo': "userOrderMemo_example", // String | 
  'amount': 3.4, // Number | 
  'quantity': 56, // Number | 
  'currency': "currency_example", // String | 
  'department': "department_example", // String | 
  'paymentMode': "paymentMode_example", // String | 
  'flpChecksum': "flpChecksum_example" // String | 
};
apiInstance.v1OrderScreenPost(ip, key, opts, (error, data, response) => {
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
 **ip** | **String**|  | 
 **key** | **String**|  | 
 **format** | **String**|  | [optional] 
 **lastName** | **String**|  | [optional] 
 **firstName** | **String**|  | [optional] 
 **billAddr** | **String**|  | [optional] 
 **billCity** | **String**|  | [optional] 
 **billState** | **String**|  | [optional] 
 **billCountry** | **String**|  | [optional] 
 **billZipCode** | **String**|  | [optional] 
 **shipAddr** | **String**|  | [optional] 
 **shipCity** | **String**|  | [optional] 
 **shipState** | **String**|  | [optional] 
 **shipCountry** | **String**|  | [optional] 
 **shipZipCode** | **String**|  | [optional] 
 **emailDomain** | **String**|  | [optional] 
 **userPhone** | **String**|  | [optional] 
 **email** | **String**|  | [optional] 
 **emailHash** | **String**|  | [optional] 
 **usernameHash** | **String**|  | [optional] 
 **passwordHash** | **String**|  | [optional] 
 **binNo** | **String**|  | [optional] 
 **cardHash** | **String**|  | [optional] 
 **avsResult** | **String**|  | [optional] 
 **cvvResult** | **String**|  | [optional] 
 **userOrderId** | **String**|  | [optional] 
 **userOrderMemo** | **String**|  | [optional] 
 **amount** | **Number**|  | [optional] 
 **quantity** | **Number**|  | [optional] 
 **currency** | **String**|  | [optional] 
 **department** | **String**|  | [optional] 
 **paymentMode** | **String**|  | [optional] 
 **flpChecksum** | **String**|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8

