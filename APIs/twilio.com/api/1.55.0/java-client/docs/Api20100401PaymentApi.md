# Api20100401PaymentApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPayments**](Api20100401PaymentApi.md#createPayments) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Payments.json |  |
| [**updatePayments**](Api20100401PaymentApi.md#updatePayments) | **POST** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Payments/{Sid}.json |  |


<a id="createPayments"></a>
# **createPayments**
> ApiV2010AccountCallPayments createPayments(accountSid, callSid, idempotencyKey, statusCallback, bankAccountType, chargeAmount, currency, description, input, minPostalCodeLength, parameter, paymentConnector, paymentMethod, postalCode, securityCode, timeout, tokenType, validCardTypes)



create an instance of payments. This will start a new payments session

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401PaymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401PaymentApi apiInstance = new Api20100401PaymentApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    String callSid = "callSid_example"; // String | The SID of the call that will create the resource. Call leg associated with this sid is expected to provide payment information thru DTMF.
    String idempotencyKey = "idempotencyKey_example"; // String | A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated.
    URI statusCallback = new URI(); // URI | Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [expected StatusCallback values](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback)
    PaymentsEnumBankAccountType bankAccountType = PaymentsEnumBankAccountType.fromValue("consumer-checking"); // PaymentsEnumBankAccountType | 
    BigDecimal chargeAmount = new BigDecimal(78); // BigDecimal | A positive decimal value less than 1,000,000 to charge against the credit card or bank account. Default currency can be overwritten with `currency` field. Leave blank or set to 0 to tokenize.
    String currency = "currency_example"; // String | The currency of the `charge_amount`, formatted as [ISO 4127](http://www.iso.org/iso/home/standards/currency_codes.htm) format. The default value is `USD` and all values allowed from the Pay Connector are accepted.
    String description = "description_example"; // String | The description can be used to provide more details regarding the transaction. This information is submitted along with the payment details to the Payment Connector which are then posted on the transactions.
    String input = "input_example"; // String | A list of inputs that should be accepted. Currently only `dtmf` is supported. All digits captured during a pay session are redacted from the logs.
    Integer minPostalCodeLength = 56; // Integer | A positive integer that is used to validate the length of the `PostalCode` inputted by the user. User must enter this many digits.
    Object parameter = null; // Object | A single-level JSON object used to pass custom parameters to payment processors. (Required for ACH payments). The information that has to be included here depends on the <Pay> Connector. [Read more](https://www.twilio.com/console/voice/pay-connectors).
    String paymentConnector = "paymentConnector_example"; // String | This is the unique name corresponding to the Pay Connector installed in the Twilio Add-ons. Learn more about [<Pay> Connectors](https://www.twilio.com/console/voice/pay-connectors). The default value is `Default`.
    PaymentsEnumPaymentMethod paymentMethod = PaymentsEnumPaymentMethod.fromValue("credit-card"); // PaymentsEnumPaymentMethod | 
    Boolean postalCode = true; // Boolean | Indicates whether the credit card postal code (zip code) is a required piece of payment information that must be provided by the caller. The default is `true`.
    Boolean securityCode = true; // Boolean | Indicates whether the credit card security code is a required piece of payment information that must be provided by the caller. The default is `true`.
    Integer timeout = 56; // Integer | The number of seconds that <Pay> should wait for the caller to press a digit between each subsequent digit, after the first one, before moving on to validate the digits captured. The default is `5`, maximum is `600`.
    PaymentsEnumTokenType tokenType = PaymentsEnumTokenType.fromValue("one-time"); // PaymentsEnumTokenType | 
    String validCardTypes = "validCardTypes_example"; // String | Credit card types separated by space that Pay should accept. The default value is `visa mastercard amex`
    try {
      ApiV2010AccountCallPayments result = apiInstance.createPayments(accountSid, callSid, idempotencyKey, statusCallback, bankAccountType, chargeAmount, currency, description, input, minPostalCodeLength, parameter, paymentConnector, paymentMethod, postalCode, securityCode, timeout, tokenType, validCardTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401PaymentApi#createPayments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. | |
| **callSid** | **String**| The SID of the call that will create the resource. Call leg associated with this sid is expected to provide payment information thru DTMF. | |
| **idempotencyKey** | **String**| A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated. | |
| **statusCallback** | **URI**| Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [expected StatusCallback values](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback) | |
| **bankAccountType** | **PaymentsEnumBankAccountType**|  | [optional] [enum: consumer-checking, consumer-savings, commercial-checking] |
| **chargeAmount** | **BigDecimal**| A positive decimal value less than 1,000,000 to charge against the credit card or bank account. Default currency can be overwritten with &#x60;currency&#x60; field. Leave blank or set to 0 to tokenize. | [optional] |
| **currency** | **String**| The currency of the &#x60;charge_amount&#x60;, formatted as [ISO 4127](http://www.iso.org/iso/home/standards/currency_codes.htm) format. The default value is &#x60;USD&#x60; and all values allowed from the Pay Connector are accepted. | [optional] |
| **description** | **String**| The description can be used to provide more details regarding the transaction. This information is submitted along with the payment details to the Payment Connector which are then posted on the transactions. | [optional] |
| **input** | **String**| A list of inputs that should be accepted. Currently only &#x60;dtmf&#x60; is supported. All digits captured during a pay session are redacted from the logs. | [optional] |
| **minPostalCodeLength** | **Integer**| A positive integer that is used to validate the length of the &#x60;PostalCode&#x60; inputted by the user. User must enter this many digits. | [optional] |
| **parameter** | [**Object**](Object.md)| A single-level JSON object used to pass custom parameters to payment processors. (Required for ACH payments). The information that has to be included here depends on the &lt;Pay&gt; Connector. [Read more](https://www.twilio.com/console/voice/pay-connectors). | [optional] |
| **paymentConnector** | **String**| This is the unique name corresponding to the Pay Connector installed in the Twilio Add-ons. Learn more about [&lt;Pay&gt; Connectors](https://www.twilio.com/console/voice/pay-connectors). The default value is &#x60;Default&#x60;. | [optional] |
| **paymentMethod** | **PaymentsEnumPaymentMethod**|  | [optional] [enum: credit-card, ach-debit] |
| **postalCode** | **Boolean**| Indicates whether the credit card postal code (zip code) is a required piece of payment information that must be provided by the caller. The default is &#x60;true&#x60;. | [optional] |
| **securityCode** | **Boolean**| Indicates whether the credit card security code is a required piece of payment information that must be provided by the caller. The default is &#x60;true&#x60;. | [optional] |
| **timeout** | **Integer**| The number of seconds that &lt;Pay&gt; should wait for the caller to press a digit between each subsequent digit, after the first one, before moving on to validate the digits captured. The default is &#x60;5&#x60;, maximum is &#x60;600&#x60;. | [optional] |
| **tokenType** | **PaymentsEnumTokenType**|  | [optional] [enum: one-time, reusable] |
| **validCardTypes** | **String**| Credit card types separated by space that Pay should accept. The default value is &#x60;visa mastercard amex&#x60; | [optional] |

### Return type

[**ApiV2010AccountCallPayments**](ApiV2010AccountCallPayments.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="updatePayments"></a>
# **updatePayments**
> ApiV2010AccountCallPayments updatePayments(accountSid, callSid, sid, idempotencyKey, statusCallback, capture, status)



update an instance of payments with different phases of payment flows.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401PaymentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401PaymentApi apiInstance = new Api20100401PaymentApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will update the resource.
    String callSid = "callSid_example"; // String | The SID of the call that will update the resource. This should be the same call sid that was used to create payments resource.
    String sid = "sid_example"; // String | The SID of Payments session that needs to be updated.
    String idempotencyKey = "idempotencyKey_example"; // String | A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated.
    URI statusCallback = new URI(); // URI | Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [Update](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-update) and [Complete/Cancel](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-cancelcomplete) POST requests.
    PaymentsEnumCapture capture = PaymentsEnumCapture.fromValue("payment-card-number"); // PaymentsEnumCapture | 
    PaymentsEnumStatus status = PaymentsEnumStatus.fromValue("complete"); // PaymentsEnumStatus | 
    try {
      ApiV2010AccountCallPayments result = apiInstance.updatePayments(accountSid, callSid, sid, idempotencyKey, statusCallback, capture, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401PaymentApi#updatePayments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will update the resource. | |
| **callSid** | **String**| The SID of the call that will update the resource. This should be the same call sid that was used to create payments resource. | |
| **sid** | **String**| The SID of Payments session that needs to be updated. | |
| **idempotencyKey** | **String**| A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated. | |
| **statusCallback** | **URI**| Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [Update](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-update) and [Complete/Cancel](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-cancelcomplete) POST requests. | |
| **capture** | **PaymentsEnumCapture**|  | [optional] [enum: payment-card-number, expiration-date, security-code, postal-code, bank-routing-number, bank-account-number] |
| **status** | **PaymentsEnumStatus**|  | [optional] [enum: complete, cancel] |

### Return type

[**ApiV2010AccountCallPayments**](ApiV2010AccountCallPayments.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |

