# TwilioApi.Api20100401PaymentApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPayments**](Api20100401PaymentApi.md#createPayments) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Payments.json | 
[**updatePayments**](Api20100401PaymentApi.md#updatePayments) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Payments/{Sid}.json | 



## createPayments

> ApiV2010AccountCallPayments createPayments(accountSid, callSid, idempotencyKey, statusCallback, opts)



create an instance of payments. This will start a new payments session

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401PaymentApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
let callSid = "callSid_example"; // String | The SID of the call that will create the resource. Call leg associated with this sid is expected to provide payment information thru DTMF.
let idempotencyKey = "idempotencyKey_example"; // String | A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated.
let statusCallback = "statusCallback_example"; // String | Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [expected StatusCallback values](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback)
let opts = {
  'bankAccountType': "bankAccountType_example", // PaymentsEnumBankAccountType | 
  'chargeAmount': 3.4, // Number | A positive decimal value less than 1,000,000 to charge against the credit card or bank account. Default currency can be overwritten with `currency` field. Leave blank or set to 0 to tokenize.
  'currency': "currency_example", // String | The currency of the `charge_amount`, formatted as [ISO 4127](http://www.iso.org/iso/home/standards/currency_codes.htm) format. The default value is `USD` and all values allowed from the Pay Connector are accepted.
  'description': "description_example", // String | The description can be used to provide more details regarding the transaction. This information is submitted along with the payment details to the Payment Connector which are then posted on the transactions.
  'input': "input_example", // String | A list of inputs that should be accepted. Currently only `dtmf` is supported. All digits captured during a pay session are redacted from the logs.
  'minPostalCodeLength': 56, // Number | A positive integer that is used to validate the length of the `PostalCode` inputted by the user. User must enter this many digits.
  'parameter': null, // Object | A single-level JSON object used to pass custom parameters to payment processors. (Required for ACH payments). The information that has to be included here depends on the <Pay> Connector. [Read more](https://www.twilio.com/console/voice/pay-connectors).
  'paymentConnector': "paymentConnector_example", // String | This is the unique name corresponding to the Pay Connector installed in the Twilio Add-ons. Learn more about [<Pay> Connectors](https://www.twilio.com/console/voice/pay-connectors). The default value is `Default`.
  'paymentMethod': "paymentMethod_example", // PaymentsEnumPaymentMethod | 
  'postalCode': true, // Boolean | Indicates whether the credit card postal code (zip code) is a required piece of payment information that must be provided by the caller. The default is `true`.
  'securityCode': true, // Boolean | Indicates whether the credit card security code is a required piece of payment information that must be provided by the caller. The default is `true`.
  'timeout': 56, // Number | The number of seconds that <Pay> should wait for the caller to press a digit between each subsequent digit, after the first one, before moving on to validate the digits captured. The default is `5`, maximum is `600`.
  'tokenType': "tokenType_example", // PaymentsEnumTokenType | 
  'validCardTypes': "validCardTypes_example" // String | Credit card types separated by space that Pay should accept. The default value is `visa mastercard amex`
};
apiInstance.createPayments(accountSid, callSid, idempotencyKey, statusCallback, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. | 
 **callSid** | **String**| The SID of the call that will create the resource. Call leg associated with this sid is expected to provide payment information thru DTMF. | 
 **idempotencyKey** | **String**| A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated. | 
 **statusCallback** | **String**| Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [expected StatusCallback values](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback) | 
 **bankAccountType** | **PaymentsEnumBankAccountType**|  | [optional] 
 **chargeAmount** | **Number**| A positive decimal value less than 1,000,000 to charge against the credit card or bank account. Default currency can be overwritten with &#x60;currency&#x60; field. Leave blank or set to 0 to tokenize. | [optional] 
 **currency** | **String**| The currency of the &#x60;charge_amount&#x60;, formatted as [ISO 4127](http://www.iso.org/iso/home/standards/currency_codes.htm) format. The default value is &#x60;USD&#x60; and all values allowed from the Pay Connector are accepted. | [optional] 
 **description** | **String**| The description can be used to provide more details regarding the transaction. This information is submitted along with the payment details to the Payment Connector which are then posted on the transactions. | [optional] 
 **input** | **String**| A list of inputs that should be accepted. Currently only &#x60;dtmf&#x60; is supported. All digits captured during a pay session are redacted from the logs. | [optional] 
 **minPostalCodeLength** | **Number**| A positive integer that is used to validate the length of the &#x60;PostalCode&#x60; inputted by the user. User must enter this many digits. | [optional] 
 **parameter** | [**Object**](Object.md)| A single-level JSON object used to pass custom parameters to payment processors. (Required for ACH payments). The information that has to be included here depends on the &lt;Pay&gt; Connector. [Read more](https://www.twilio.com/console/voice/pay-connectors). | [optional] 
 **paymentConnector** | **String**| This is the unique name corresponding to the Pay Connector installed in the Twilio Add-ons. Learn more about [&lt;Pay&gt; Connectors](https://www.twilio.com/console/voice/pay-connectors). The default value is &#x60;Default&#x60;. | [optional] 
 **paymentMethod** | **PaymentsEnumPaymentMethod**|  | [optional] 
 **postalCode** | **Boolean**| Indicates whether the credit card postal code (zip code) is a required piece of payment information that must be provided by the caller. The default is &#x60;true&#x60;. | [optional] 
 **securityCode** | **Boolean**| Indicates whether the credit card security code is a required piece of payment information that must be provided by the caller. The default is &#x60;true&#x60;. | [optional] 
 **timeout** | **Number**| The number of seconds that &lt;Pay&gt; should wait for the caller to press a digit between each subsequent digit, after the first one, before moving on to validate the digits captured. The default is &#x60;5&#x60;, maximum is &#x60;600&#x60;. | [optional] 
 **tokenType** | **PaymentsEnumTokenType**|  | [optional] 
 **validCardTypes** | **String**| Credit card types separated by space that Pay should accept. The default value is &#x60;visa mastercard amex&#x60; | [optional] 

### Return type

[**ApiV2010AccountCallPayments**](ApiV2010AccountCallPayments.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## updatePayments

> ApiV2010AccountCallPayments updatePayments(accountSid, callSid, sid, idempotencyKey, statusCallback, opts)



update an instance of payments with different phases of payment flows.

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401PaymentApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will update the resource.
let callSid = "callSid_example"; // String | The SID of the call that will update the resource. This should be the same call sid that was used to create payments resource.
let sid = "sid_example"; // String | The SID of Payments session that needs to be updated.
let idempotencyKey = "idempotencyKey_example"; // String | A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated.
let statusCallback = "statusCallback_example"; // String | Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [Update](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-update) and [Complete/Cancel](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-cancelcomplete) POST requests.
let opts = {
  'capture': "capture_example", // PaymentsEnumCapture | 
  'status': "status_example" // PaymentsEnumStatus | 
};
apiInstance.updatePayments(accountSid, callSid, sid, idempotencyKey, statusCallback, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will update the resource. | 
 **callSid** | **String**| The SID of the call that will update the resource. This should be the same call sid that was used to create payments resource. | 
 **sid** | **String**| The SID of Payments session that needs to be updated. | 
 **idempotencyKey** | **String**| A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated. | 
 **statusCallback** | **String**| Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [Update](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-update) and [Complete/Cancel](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-cancelcomplete) POST requests. | 
 **capture** | **PaymentsEnumCapture**|  | [optional] 
 **status** | **PaymentsEnumStatus**|  | [optional] 

### Return type

[**ApiV2010AccountCallPayments**](ApiV2010AccountCallPayments.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

