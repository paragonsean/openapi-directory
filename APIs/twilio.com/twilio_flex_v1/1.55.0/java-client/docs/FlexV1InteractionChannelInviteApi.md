# FlexV1InteractionChannelInviteApi

All URIs are relative to *https://flex-api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createInteractionChannelInvite**](FlexV1InteractionChannelInviteApi.md#createInteractionChannelInvite) | **POST** /v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Invites |  |
| [**listInteractionChannelInvite**](FlexV1InteractionChannelInviteApi.md#listInteractionChannelInvite) | **GET** /v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Invites |  |


<a id="createInteractionChannelInvite"></a>
# **createInteractionChannelInvite**
> FlexV1InteractionInteractionChannelInteractionChannelInvite createInteractionChannelInvite(interactionSid, channelSid, routing)



Invite an Agent or a TaskQueue to a Channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InteractionChannelInviteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InteractionChannelInviteApi apiInstance = new FlexV1InteractionChannelInviteApi(defaultClient);
    String interactionSid = "interactionSid_example"; // String | The Interaction SID for this Channel.
    String channelSid = "channelSid_example"; // String | The Channel SID for this Invite.
    Object routing = null; // Object | The Interaction's routing logic.
    try {
      FlexV1InteractionInteractionChannelInteractionChannelInvite result = apiInstance.createInteractionChannelInvite(interactionSid, channelSid, routing);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InteractionChannelInviteApi#createInteractionChannelInvite");
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
| **interactionSid** | **String**| The Interaction SID for this Channel. | |
| **channelSid** | **String**| The Channel SID for this Invite. | |
| **routing** | [**Object**](Object.md)| The Interaction&#39;s routing logic. | |

### Return type

[**FlexV1InteractionInteractionChannelInteractionChannelInvite**](FlexV1InteractionInteractionChannelInteractionChannelInvite.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="listInteractionChannelInvite"></a>
# **listInteractionChannelInvite**
> ListInteractionChannelInviteResponse listInteractionChannelInvite(interactionSid, channelSid, pageSize, page, pageToken)



List all Invites for a Channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InteractionChannelInviteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InteractionChannelInviteApi apiInstance = new FlexV1InteractionChannelInviteApi(defaultClient);
    String interactionSid = "interactionSid_example"; // String | The Interaction SID for this Channel.
    String channelSid = "channelSid_example"; // String | The Channel SID for this Participant.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListInteractionChannelInviteResponse result = apiInstance.listInteractionChannelInvite(interactionSid, channelSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InteractionChannelInviteApi#listInteractionChannelInvite");
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
| **interactionSid** | **String**| The Interaction SID for this Channel. | |
| **channelSid** | **String**| The Channel SID for this Participant. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListInteractionChannelInviteResponse**](ListInteractionChannelInviteResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

