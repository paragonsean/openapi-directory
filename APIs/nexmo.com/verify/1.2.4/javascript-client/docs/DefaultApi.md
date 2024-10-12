# VerifyApi.DefaultApi

All URIs are relative to *https://api.nexmo.com/verify*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verifyCheck**](DefaultApi.md#verifyCheck) | **POST** /check/{format} | Verify Check
[**verifyControl**](DefaultApi.md#verifyControl) | **POST** /control/{format} | Verify Control
[**verifyRequestWithPSD2**](DefaultApi.md#verifyRequestWithPSD2) | **POST** /psd2/{format} | PSD2 (Payment Services Directive 2) Request
[**verifySearch**](DefaultApi.md#verifySearch) | **GET** /search/{format} | Verify Search



## verifyCheck

> VerifyCheck200Response verifyCheck(format, apiKey, apiSecret, code, requestId, opts)

Verify Check

Use Verify check to confirm that the PIN you received from your user matches the one sent by Vonage in your Verify request.  1. Send the verification &#x60;code&#x60; that your user supplied, with the corresponding &#x60;request_id&#x60; from the Verify request. 2. Check the &#x60;status&#x60; of the response to determine if the code the user supplied matches the one sent by Vonage.  *Note that this endpoint is available by &#x60;GET&#x60; request as well as &#x60;POST&#x60;.*

### Example

```javascript
import VerifyApi from 'verify_api';

let apiInstance = new VerifyApi.DefaultApi();
let format = "json"; // String | The response format.
let apiKey = "apiKey_example"; // String | You can find your API key in your [account dashboard](https://dashboard.nexmo.com)
let apiSecret = "apiSecret_example"; // String | You can find your API secret in your [account dashboard](https://dashboard.nexmo.com)
let code = "code_example"; // String | The verification code entered by your user.
let requestId = "requestId_example"; // String | The Verify request to check. This is the `request_id` you received in the response to the Verify request.
let opts = {
  'ipAddress': "ipAddress_example" // String | (This field is no longer used)
};
apiInstance.verifyCheck(format, apiKey, apiSecret, code, requestId, opts, (error, data, response) => {
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
 **format** | **String**| The response format. | 
 **apiKey** | **String**| You can find your API key in your [account dashboard](https://dashboard.nexmo.com) | 
 **apiSecret** | **String**| You can find your API secret in your [account dashboard](https://dashboard.nexmo.com) | 
 **code** | **String**| The verification code entered by your user. | 
 **requestId** | **String**| The Verify request to check. This is the &#x60;request_id&#x60; you received in the response to the Verify request. | 
 **ipAddress** | **String**| (This field is no longer used) | [optional] 

### Return type

[**VerifyCheck200Response**](VerifyCheck200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, text/xml


## verifyControl

> VerifyControl200Response verifyControl(format, apiKey, apiSecret, cmd, requestId)

Verify Control

Control the progress of your Verify requests. To cancel an existing Verify request, or to trigger the next verification event:   1. Send a Verify control request with the appropriate command (&#x60;cmd&#x60;) for what you want to achieve.  2. Check the &#x60;status&#x60; in the response.   *Note that this endpoint is available by &#x60;GET&#x60; request as well as &#x60;POST&#x60;.*

### Example

```javascript
import VerifyApi from 'verify_api';

let apiInstance = new VerifyApi.DefaultApi();
let format = "json"; // String | The response format.
let apiKey = "apiKey_example"; // String | You can find your API key in your [account dashboard](https://dashboard.nexmo.com)
let apiSecret = "apiSecret_example"; // String | You can find your API secret in your [account dashboard](https://dashboard.nexmo.com)
let cmd = "cmd_example"; // String | The possible commands are `cancel` to request cancellation of the verification process, or `trigger_next_event` to advance  to the next verification event (if any). Cancellation is only possible 30 seconds after the start of the verification request and before the second event (either TTS or SMS) has taken place.
let requestId = "requestId_example"; // String | The `request_id` you received in the response to the Verify request.
apiInstance.verifyControl(format, apiKey, apiSecret, cmd, requestId, (error, data, response) => {
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
 **format** | **String**| The response format. | 
 **apiKey** | **String**| You can find your API key in your [account dashboard](https://dashboard.nexmo.com) | 
 **apiSecret** | **String**| You can find your API secret in your [account dashboard](https://dashboard.nexmo.com) | 
 **cmd** | **String**| The possible commands are &#x60;cancel&#x60; to request cancellation of the verification process, or &#x60;trigger_next_event&#x60; to advance  to the next verification event (if any). Cancellation is only possible 30 seconds after the start of the verification request and before the second event (either TTS or SMS) has taken place. | 
 **requestId** | **String**| The &#x60;request_id&#x60; you received in the response to the Verify request. | 

### Return type

[**VerifyControl200Response**](VerifyControl200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, text/xml


## verifyRequestWithPSD2

> VerifyRequestWithPSD2200Response verifyRequestWithPSD2(format, amount, apiKey, apiSecret, number, payee, opts)

PSD2 (Payment Services Directive 2) Request

Use Verify request to generate and send a PIN to your user to authorize a payment: 1. Create a request to send a verification code to your user. 2. Check the &#x60;status&#x60; field in the response to ensure that your request was successful (zero is success). 3. Use the &#x60;request_id&#x60; field in the response for the Verify check. (Please note that XML format is not supported for the Payment Services Directive endpoint at this time.)

### Example

```javascript
import VerifyApi from 'verify_api';

let apiInstance = new VerifyApi.DefaultApi();
let format = "json"; // String | The response format.
let amount = 3.4; // Number | The decimal amount of the payment to be confirmed, in Euros
let apiKey = "apiKey_example"; // String | You can find your API key in your [account dashboard](https://dashboard.nexmo.com)
let apiSecret = "apiSecret_example"; // String | You can find your API secret in your [account dashboard](https://dashboard.nexmo.com)
let number = "number_example"; // String | The mobile or landline phone number to verify. Unless you are setting `country` explicitly, this number must be in [E.164](https://en.wikipedia.org/wiki/E.164) format.
let payee = "payee_example"; // String | An alphanumeric string to indicate to the user the name of the recipient that they are confirming a payment to.
let opts = {
  'codeLength': 4, // Number | The length of the verification code.
  'country': "country_example", // String | If you do not provide `number` in international format or you are not sure if `number` is correctly formatted, specify the two-character country code in `country`. Verify will then format the number for you.
  'lg': "'en-gb'", // String | By default, the SMS or text-to-speech (TTS) message is generated in the locale that matches the `number`. For example, the text message or TTS message for a `33*` number is sent in French. Use this parameter to explicitly control the language used. *Note: Voice calls in English for `bg-bg`, `ee-et`, `ga-ie`, `lv-lv`, `lt-lt`, `mt-mt`, `sk-sk`, `sk-si`
  'nextEventWait': 300, // Number | Specifies the wait time in seconds between attempts to deliver the verification code.
  'pinExpiry': 300, // Number | How long the generated verification code is valid for, in seconds. When you specify both `pin_expiry` and `next_event_wait` then `pin_expiry` must be an integer multiple of `next_event_wait` otherwise `pin_expiry` is defaulted to equal next_event_wait. See [changing the event timings](https://developer.nexmo.com/verify/guides/changing-default-timings).
  'workflowId': 1 // Number | Selects the predefined sequence of SMS and TTS (Text To Speech) actions to use in order to convey the PIN to your user. For example, an id of 1 identifies the workflow SMS - TTS - TTS. For a list of all workflows and their associated ids, please visit the [developer portal](https://developer.nexmo.com/verify/guides/workflows-and-events).
};
apiInstance.verifyRequestWithPSD2(format, amount, apiKey, apiSecret, number, payee, opts, (error, data, response) => {
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
 **format** | **String**| The response format. | 
 **amount** | **Number**| The decimal amount of the payment to be confirmed, in Euros | 
 **apiKey** | **String**| You can find your API key in your [account dashboard](https://dashboard.nexmo.com) | 
 **apiSecret** | **String**| You can find your API secret in your [account dashboard](https://dashboard.nexmo.com) | 
 **number** | **String**| The mobile or landline phone number to verify. Unless you are setting &#x60;country&#x60; explicitly, this number must be in [E.164](https://en.wikipedia.org/wiki/E.164) format. | 
 **payee** | **String**| An alphanumeric string to indicate to the user the name of the recipient that they are confirming a payment to. | 
 **codeLength** | **Number**| The length of the verification code. | [optional] [default to 4]
 **country** | **String**| If you do not provide &#x60;number&#x60; in international format or you are not sure if &#x60;number&#x60; is correctly formatted, specify the two-character country code in &#x60;country&#x60;. Verify will then format the number for you. | [optional] 
 **lg** | **String**| By default, the SMS or text-to-speech (TTS) message is generated in the locale that matches the &#x60;number&#x60;. For example, the text message or TTS message for a &#x60;33*&#x60; number is sent in French. Use this parameter to explicitly control the language used. *Note: Voice calls in English for &#x60;bg-bg&#x60;, &#x60;ee-et&#x60;, &#x60;ga-ie&#x60;, &#x60;lv-lv&#x60;, &#x60;lt-lt&#x60;, &#x60;mt-mt&#x60;, &#x60;sk-sk&#x60;, &#x60;sk-si&#x60; | [optional] [default to &#39;en-gb&#39;]
 **nextEventWait** | **Number**| Specifies the wait time in seconds between attempts to deliver the verification code. | [optional] [default to 300]
 **pinExpiry** | **Number**| How long the generated verification code is valid for, in seconds. When you specify both &#x60;pin_expiry&#x60; and &#x60;next_event_wait&#x60; then &#x60;pin_expiry&#x60; must be an integer multiple of &#x60;next_event_wait&#x60; otherwise &#x60;pin_expiry&#x60; is defaulted to equal next_event_wait. See [changing the event timings](https://developer.nexmo.com/verify/guides/changing-default-timings). | [optional] [default to 300]
 **workflowId** | **Number**| Selects the predefined sequence of SMS and TTS (Text To Speech) actions to use in order to convey the PIN to your user. For example, an id of 1 identifies the workflow SMS - TTS - TTS. For a list of all workflows and their associated ids, please visit the [developer portal](https://developer.nexmo.com/verify/guides/workflows-and-events). | [optional] [default to 1]

### Return type

[**VerifyRequestWithPSD2200Response**](VerifyRequestWithPSD2200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## verifySearch

> VerifySearch200Response verifySearch(format, apiKey, apiSecret, requestId, opts)

Verify Search

Use Verify search to check the status of past or current verification requests:  1. Send a Verify search request containing the &#x60;request_id&#x60;s of the verification requests you are interested in. 2. Use the &#x60;status&#x60; of each verification request in the &#x60;checks&#x60; array of the response object to determine the outcome.  *Note that this endpoint is available by &#x60;POST&#x60; request as well as &#x60;GET&#x60;.*

### Example

```javascript
import VerifyApi from 'verify_api';

let apiInstance = new VerifyApi.DefaultApi();
let format = "json"; // String | The response format.
let apiKey = "apiKey_example"; // String | 
let apiSecret = "apiSecret_example"; // String | 
let requestId = "abcdef0123456789abcdef0123456789"; // String | The `request_id` you received in the Verify Request Response. Required if `request_ids` not provided.
let opts = {
  'requestIds': ["abcdef0123456789abcdef0123456789"] // [String] | More than one `request_id`. Each `request_id` is a new parameter in the Verify Search request. Required if `request_id` not provided.
};
apiInstance.verifySearch(format, apiKey, apiSecret, requestId, opts, (error, data, response) => {
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
 **format** | **String**| The response format. | 
 **apiKey** | **String**|  | 
 **apiSecret** | **String**|  | 
 **requestId** | **String**| The &#x60;request_id&#x60; you received in the Verify Request Response. Required if &#x60;request_ids&#x60; not provided. | 
 **requestIds** | [**[String]**](String.md)| More than one &#x60;request_id&#x60;. Each &#x60;request_id&#x60; is a new parameter in the Verify Search request. Required if &#x60;request_id&#x60; not provided. | [optional] 

### Return type

[**VerifySearch200Response**](VerifySearch200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/xml

