# RequestsApi

All URIs are relative to *https://api.nexmo.com/verify*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**verifyRequest**](RequestsApi.md#verifyRequest) | **POST** /{format} | Request a Verification |


<a id="verifyRequest"></a>
# **verifyRequest**
> VerifyRequestWithPSD2200Response verifyRequest(format, apiKey, apiSecret, brand, number, codeLength, country, lg, nextEventWait, pinCode, pinExpiry, senderId, workflowId)

Request a Verification

Use Verify request to generate and send a PIN to your user:  1. Create a request to send a verification code to your user.  2. Check the &#x60;status&#x60; field in the response to ensure that your request was successful (zero is success).  3. Use the &#x60;request_id&#x60; field in the response for the Verify check.  *Note that this endpoint is available by &#x60;GET&#x60; request as well as &#x60;POST&#x60;.*

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/verify");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    String format = "json"; // String | The response format.
    String apiKey = "apiKey_example"; // String | You can find your API key in your [account dashboard](https://dashboard.nexmo.com)
    String apiSecret = "apiSecret_example"; // String | You can find your API secret in your [account dashboard](https://dashboard.nexmo.com)
    String brand = "brand_example"; // String | An 18-character alphanumeric string you can use to personalize the verification request SMS body, to help users identify your company or application name. For example: \\\"Your `Acme Inc` PIN is ...\\\"
    String number = "number_example"; // String | The mobile or landline phone number to verify. Unless you are setting `country` explicitly, this number must be in [E.164](https://en.wikipedia.org/wiki/E.164) format.
    Integer codeLength = 4; // Integer | The length of the verification code.
    String country = "country_example"; // String | If you do not provide `number` in international format or you are not sure if `number` is correctly formatted, specify the two-character country code in `country`. Verify will then format the number for you.
    String lg = "ar-xa"; // String | By default, the SMS or text-to-speech (TTS) message is generated in the locale that matches the `number`. For example, the text message or TTS message for a `33*` number is sent in French. Use this parameter to explicitly control the language used for the Verify request. A list of languages is available: <https://developer.nexmo.com/verify/guides/verify-languages>
    Integer nextEventWait = 300; // Integer | Specifies the wait time in seconds between attempts to deliver the verification code.
    String pinCode = "pinCode_example"; // String | A custom PIN to send to the user. If a PIN is not provided, Verify will generate a random PIN for you. <b>This feature is not enabled by default</b> - please discuss with your Account Manager if you would like it enabled. If this feature is not enabled on your account, error status `20` will be returned.
    Integer pinExpiry = 300; // Integer | How long the generated verification code is valid for, in seconds. When you specify both `pin_expiry` and `next_event_wait` then `pin_expiry` must be an integer multiple of `next_event_wait` otherwise `pin_expiry` is defaulted to equal next_event_wait. See [changing the event timings](https://developer.nexmo.com/verify/guides/changing-default-timings).
    String senderId = "VERIFY"; // String | An 11-character alphanumeric string that represents the [identity of the sender](https://developer.nexmo.com/messaging/sms/guides/custom-sender-id) of the verification request. Depending on the destination of the phone number you are sending the verification SMS to, restrictions might apply.
    Integer workflowId = 1; // Integer | Selects the predefined sequence of SMS and TTS (Text To Speech) actions to use in order to convey the PIN to your user. For example, an id of 1 identifies the workflow SMS - TTS - TTS. For a list of all workflows and their associated ids, please visit the [developer portal](https://developer.nexmo.com/verify/guides/workflows-and-events).
    try {
      VerifyRequestWithPSD2200Response result = apiInstance.verifyRequest(format, apiKey, apiSecret, brand, number, codeLength, country, lg, nextEventWait, pinCode, pinExpiry, senderId, workflowId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#verifyRequest");
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
| **format** | **String**| The response format. | [enum: json, xml] |
| **apiKey** | **String**| You can find your API key in your [account dashboard](https://dashboard.nexmo.com) | |
| **apiSecret** | **String**| You can find your API secret in your [account dashboard](https://dashboard.nexmo.com) | |
| **brand** | **String**| An 18-character alphanumeric string you can use to personalize the verification request SMS body, to help users identify your company or application name. For example: \\\&quot;Your &#x60;Acme Inc&#x60; PIN is ...\\\&quot; | |
| **number** | **String**| The mobile or landline phone number to verify. Unless you are setting &#x60;country&#x60; explicitly, this number must be in [E.164](https://en.wikipedia.org/wiki/E.164) format. | |
| **codeLength** | **Integer**| The length of the verification code. | [optional] [default to 4] [enum: 4, 6] |
| **country** | **String**| If you do not provide &#x60;number&#x60; in international format or you are not sure if &#x60;number&#x60; is correctly formatted, specify the two-character country code in &#x60;country&#x60;. Verify will then format the number for you. | [optional] |
| **lg** | **String**| By default, the SMS or text-to-speech (TTS) message is generated in the locale that matches the &#x60;number&#x60;. For example, the text message or TTS message for a &#x60;33*&#x60; number is sent in French. Use this parameter to explicitly control the language used for the Verify request. A list of languages is available: &lt;https://developer.nexmo.com/verify/guides/verify-languages&gt; | [optional] [default to en-us] [enum: ar-xa, cs-cz, cy-cy, cy-gb, da-dk, de-de, el-gr, en-au, en-gb, en-in, en-us, es-es, es-mx, es-us, fi-fi, fil-ph, fr-ca, fr-fr, hi-in, hu-hu, id-id, is-is, it-it, ja-jp, ko-kr, nb-no, nl-nl, pl-pl, pt-br, pt-pt, ro-ro, ru-ru, sv-se, th-th, tr-tr, vi-vn, yue-cn, zh-cn, zh-tw] |
| **nextEventWait** | **Integer**| Specifies the wait time in seconds between attempts to deliver the verification code. | [optional] [default to 300] |
| **pinCode** | **String**| A custom PIN to send to the user. If a PIN is not provided, Verify will generate a random PIN for you. &lt;b&gt;This feature is not enabled by default&lt;/b&gt; - please discuss with your Account Manager if you would like it enabled. If this feature is not enabled on your account, error status &#x60;20&#x60; will be returned. | [optional] |
| **pinExpiry** | **Integer**| How long the generated verification code is valid for, in seconds. When you specify both &#x60;pin_expiry&#x60; and &#x60;next_event_wait&#x60; then &#x60;pin_expiry&#x60; must be an integer multiple of &#x60;next_event_wait&#x60; otherwise &#x60;pin_expiry&#x60; is defaulted to equal next_event_wait. See [changing the event timings](https://developer.nexmo.com/verify/guides/changing-default-timings). | [optional] [default to 300] |
| **senderId** | **String**| An 11-character alphanumeric string that represents the [identity of the sender](https://developer.nexmo.com/messaging/sms/guides/custom-sender-id) of the verification request. Depending on the destination of the phone number you are sending the verification SMS to, restrictions might apply. | [optional] [default to VERIFY] |
| **workflowId** | **Integer**| Selects the predefined sequence of SMS and TTS (Text To Speech) actions to use in order to convey the PIN to your user. For example, an id of 1 identifies the workflow SMS - TTS - TTS. For a list of all workflows and their associated ids, please visit the [developer portal](https://developer.nexmo.com/verify/guides/workflows-and-events). | [optional] [default to 1] [enum: 1, 2, 3, 4, 5, 6, 7] |

### Return type

[**VerifyRequestWithPSD2200Response**](VerifyRequestWithPSD2200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

