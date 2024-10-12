# DefaultApi

All URIs are relative to *https://rest.nexmo.com/sms*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sendAnSms**](DefaultApi.md#sendAnSms) | **POST** /{format} | Send an SMS |


<a id="sendAnSms"></a>
# **sendAnSms**
> SendAnSms200Response sendAnSms(format, apiKey, from, to, accountRef, apiSecret, body, paramCallback, clientRef, contentId, entityId, messageClass, protocolId, sig, statusReportReq, text, ttl, type, udh)

Send an SMS

Send an outbound SMS from your Vonage account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.nexmo.com/sms");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "json"; // String | The format of the response
    String apiKey = "apiKey_example"; // String | Your API key
    String from = "from_example"; // String | The name or number the message should be sent from. Alphanumeric senderID's are not supported in all countries, see [Global Messaging](/messaging/sms/guides/global-messaging#country-specific-features) for more details. If alphanumeric, spaces will be ignored. Numbers are specified in E.164 format.
    String to = "to_example"; // String | The number that the message should be sent to. Numbers are specified in E.164 format.
    String accountRef = "accountRef_example"; // String | **Advanced**: An optional string used to identify separate accounts using the SMS endpoint for billing purposes. To use this feature, please email [support@nexmo.com](mailto:support@nexmo.com)
    String apiSecret = "apiSecret_example"; // String | Your API secret. Required unless `sig` is provided
    String body = "body_example"; // String | **Advanced**: Hex encoded binary data. Depends on `type` parameter having the value `binary`.
    String paramCallback = "paramCallback_example"; // String | **Advanced**: The webhook endpoint the delivery receipt for this sms is sent to. This parameter overrides the webhook endpoint you set in Dashboard. Max 100 characters.
    String clientRef = "clientRef_example"; // String | **Advanced**: You can optionally include your own reference of up to 100 characters.
    String contentId = "contentId_example"; // String | **Advanced**: A string parameter that satisfies regulatory requirements when sending an SMS to specific countries. For more information please refer to the [Country-Specific Outbound SMS Features](https://help.nexmo.com/hc/en-us/articles/115011781468)
    String entityId = "entityId_example"; // String | **Advanced**: A string parameter that satisfies regulatory requirements when sending an SMS to specific countries. For more information please refer to the [Country-Specific Outbound SMS Features](https://help.nexmo.com/hc/en-us/articles/115011781468)
    Integer messageClass = 0; // Integer | **Advanced**: The Data Coding Scheme value of the message
    Integer protocolId = 56; // Integer | **Advanced**: The value of the [protocol identifier](https://en.wikipedia.org/wiki/GSM_03.40#Protocol_Identifier) to use. Ensure that the value is aligned with `udh`.
    String sig = "sig_example"; // String | The hash of the request parameters in alphabetical order, a timestamp and the signature secret. See [Signing Requests](/concepts/guides/signing-messages) for more details.
    Boolean statusReportReq = true; // Boolean | **Advanced**: Boolean indicating if you like to receive a [Delivery Receipt](/messaging/sms/building-blocks/receive-a-delivery-receipt).
    String text = "text_example"; // String | The body of the message being sent. If your message contains characters that can be encoded according to the GSM Standard and Extended tables then you can set the `type` to `text`. If your message contains characters outside this range, then you will need to set the `type` to `unicode`.
    Integer ttl = 259200000; // Integer | **Advanced**: The duration in milliseconds the delivery of an SMS will be attempted.§§ By default Vonage attempts delivery for 72 hours, however the maximum effective value depends on the operator and is typically 24 - 48 hours. We recommend this value should be kept at its default or at least 30 minutes.
    String type = "text"; // String | **Advanced**: The format of the message body
    String udh = "udh_example"; // String | **Advanced**: Your custom Hex encoded [User Data Header](https://en.wikipedia.org/wiki/User_Data_Header). Depends on `type` parameter having the value `binary`.
    try {
      SendAnSms200Response result = apiInstance.sendAnSms(format, apiKey, from, to, accountRef, apiSecret, body, paramCallback, clientRef, contentId, entityId, messageClass, protocolId, sig, statusReportReq, text, ttl, type, udh);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sendAnSms");
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
| **format** | **String**| The format of the response | [default to json] [enum: json, xml] |
| **apiKey** | **String**| Your API key | |
| **from** | **String**| The name or number the message should be sent from. Alphanumeric senderID&#39;s are not supported in all countries, see [Global Messaging](/messaging/sms/guides/global-messaging#country-specific-features) for more details. If alphanumeric, spaces will be ignored. Numbers are specified in E.164 format. | |
| **to** | **String**| The number that the message should be sent to. Numbers are specified in E.164 format. | |
| **accountRef** | **String**| **Advanced**: An optional string used to identify separate accounts using the SMS endpoint for billing purposes. To use this feature, please email [support@nexmo.com](mailto:support@nexmo.com) | [optional] |
| **apiSecret** | **String**| Your API secret. Required unless &#x60;sig&#x60; is provided | [optional] |
| **body** | **String**| **Advanced**: Hex encoded binary data. Depends on &#x60;type&#x60; parameter having the value &#x60;binary&#x60;. | [optional] |
| **paramCallback** | **String**| **Advanced**: The webhook endpoint the delivery receipt for this sms is sent to. This parameter overrides the webhook endpoint you set in Dashboard. Max 100 characters. | [optional] |
| **clientRef** | **String**| **Advanced**: You can optionally include your own reference of up to 100 characters. | [optional] |
| **contentId** | **String**| **Advanced**: A string parameter that satisfies regulatory requirements when sending an SMS to specific countries. For more information please refer to the [Country-Specific Outbound SMS Features](https://help.nexmo.com/hc/en-us/articles/115011781468) | [optional] |
| **entityId** | **String**| **Advanced**: A string parameter that satisfies regulatory requirements when sending an SMS to specific countries. For more information please refer to the [Country-Specific Outbound SMS Features](https://help.nexmo.com/hc/en-us/articles/115011781468) | [optional] |
| **messageClass** | **Integer**| **Advanced**: The Data Coding Scheme value of the message | [optional] [enum: 0, 1, 2, 3] |
| **protocolId** | **Integer**| **Advanced**: The value of the [protocol identifier](https://en.wikipedia.org/wiki/GSM_03.40#Protocol_Identifier) to use. Ensure that the value is aligned with &#x60;udh&#x60;. | [optional] |
| **sig** | **String**| The hash of the request parameters in alphabetical order, a timestamp and the signature secret. See [Signing Requests](/concepts/guides/signing-messages) for more details. | [optional] |
| **statusReportReq** | **Boolean**| **Advanced**: Boolean indicating if you like to receive a [Delivery Receipt](/messaging/sms/building-blocks/receive-a-delivery-receipt). | [optional] [default to true] |
| **text** | **String**| The body of the message being sent. If your message contains characters that can be encoded according to the GSM Standard and Extended tables then you can set the &#x60;type&#x60; to &#x60;text&#x60;. If your message contains characters outside this range, then you will need to set the &#x60;type&#x60; to &#x60;unicode&#x60;. | [optional] |
| **ttl** | **Integer**| **Advanced**: The duration in milliseconds the delivery of an SMS will be attempted.§§ By default Vonage attempts delivery for 72 hours, however the maximum effective value depends on the operator and is typically 24 - 48 hours. We recommend this value should be kept at its default or at least 30 minutes. | [optional] [default to 259200000] |
| **type** | **String**| **Advanced**: The format of the message body | [optional] [default to text] [enum: text, binary, unicode] |
| **udh** | **String**| **Advanced**: Your custom Hex encoded [User Data Header](https://en.wikipedia.org/wiki/User_Data_Header). Depends on &#x60;type&#x60; parameter having the value &#x60;binary&#x60;. | [optional] |

### Return type

[**SendAnSms200Response**](SendAnSms200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

