# FlexV2WebChannelsApi

All URIs are relative to *https://flex-api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWebChannel**](FlexV2WebChannelsApi.md#createWebChannel) | **POST** /v2/WebChats |  |


<a id="createWebChannel"></a>
# **createWebChannel**
> FlexV2WebChannel createWebChannel(addressSid, chatFriendlyName, customerFriendlyName, preEngagementData)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV2WebChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV2WebChannelsApi apiInstance = new FlexV2WebChannelsApi(defaultClient);
    String addressSid = "addressSid_example"; // String | The SID of the Conversations Address. See [Address Configuration Resource](https://www.twilio.com/docs/conversations/api/address-configuration-resource) for configuration details. When a conversation is created on the Flex backend, the callback URL will be set to the corresponding Studio Flow SID or webhook URL in your address configuration.
    String chatFriendlyName = "chatFriendlyName_example"; // String | The Conversation's friendly name. See the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource) for an example.
    String customerFriendlyName = "customerFriendlyName_example"; // String | The Conversation participant's friendly name. See the [Conversation Participant Resource](https://www.twilio.com/docs/conversations/api/conversation-participant-resource) for an example.
    String preEngagementData = "preEngagementData_example"; // String | The pre-engagement data.
    try {
      FlexV2WebChannel result = apiInstance.createWebChannel(addressSid, chatFriendlyName, customerFriendlyName, preEngagementData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV2WebChannelsApi#createWebChannel");
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
| **addressSid** | **String**| The SID of the Conversations Address. See [Address Configuration Resource](https://www.twilio.com/docs/conversations/api/address-configuration-resource) for configuration details. When a conversation is created on the Flex backend, the callback URL will be set to the corresponding Studio Flow SID or webhook URL in your address configuration. | |
| **chatFriendlyName** | **String**| The Conversation&#39;s friendly name. See the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource) for an example. | [optional] |
| **customerFriendlyName** | **String**| The Conversation participant&#39;s friendly name. See the [Conversation Participant Resource](https://www.twilio.com/docs/conversations/api/conversation-participant-resource) for an example. | [optional] |
| **preEngagementData** | **String**| The pre-engagement data. | [optional] |

### Return type

[**FlexV2WebChannel**](FlexV2WebChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

