# ChatV3ChannelApi

All URIs are relative to *https://chat.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**updateChannel**](ChatV3ChannelApi.md#updateChannel) | **POST** /v3/Services/{ServiceSid}/Channels/{Sid} |  |


<a id="updateChannel"></a>
# **updateChannel**
> ChatV3Channel updateChannel(serviceSid, sid, xTwilioWebhookEnabled, messagingServiceSid, type)



Update a specific Channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV3ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV3ChannelApi apiInstance = new ChatV3ChannelApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Service.
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies this Channel.
    ChannelEnumWebhookEnabledType xTwilioWebhookEnabled = ChannelEnumWebhookEnabledType.fromValue("true"); // ChannelEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String messagingServiceSid = "messagingServiceSid_example"; // String | The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this channel belongs to.
    ChannelEnumChannelType type = ChannelEnumChannelType.fromValue("public"); // ChannelEnumChannelType | 
    try {
      ChatV3Channel result = apiInstance.updateChannel(serviceSid, sid, xTwilioWebhookEnabled, messagingServiceSid, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV3ChannelApi#updateChannel");
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
| **serviceSid** | **String**| The unique SID identifier of the Service. | |
| **sid** | **String**| A 34 character string that uniquely identifies this Channel. | |
| **xTwilioWebhookEnabled** | **ChannelEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **messagingServiceSid** | **String**| The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this channel belongs to. | [optional] |
| **type** | **ChannelEnumChannelType**|  | [optional] [enum: public, private] |

### Return type

[**ChatV3Channel**](ChatV3Channel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

