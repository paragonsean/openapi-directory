# FlexV1InteractionChannelParticipantApi

All URIs are relative to *https://flex-api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createInteractionChannelParticipant**](FlexV1InteractionChannelParticipantApi.md#createInteractionChannelParticipant) | **POST** /v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Participants |  |
| [**listInteractionChannelParticipant**](FlexV1InteractionChannelParticipantApi.md#listInteractionChannelParticipant) | **GET** /v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Participants |  |
| [**updateInteractionChannelParticipant**](FlexV1InteractionChannelParticipantApi.md#updateInteractionChannelParticipant) | **POST** /v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Participants/{Sid} |  |


<a id="createInteractionChannelParticipant"></a>
# **createInteractionChannelParticipant**
> FlexV1InteractionInteractionChannelInteractionChannelParticipant createInteractionChannelParticipant(interactionSid, channelSid, mediaProperties, type, routingProperties)



Add a Participant to a Channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InteractionChannelParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InteractionChannelParticipantApi apiInstance = new FlexV1InteractionChannelParticipantApi(defaultClient);
    String interactionSid = "interactionSid_example"; // String | The Interaction Sid for the new Channel Participant.
    String channelSid = "channelSid_example"; // String | The Channel Sid for the new Channel Participant.
    Object mediaProperties = null; // Object | JSON representing the Media Properties for the new Participant.
    InteractionChannelParticipantEnumType type = InteractionChannelParticipantEnumType.fromValue("supervisor"); // InteractionChannelParticipantEnumType | 
    Object routingProperties = null; // Object | Object representing the Routing Properties for the new Participant.
    try {
      FlexV1InteractionInteractionChannelInteractionChannelParticipant result = apiInstance.createInteractionChannelParticipant(interactionSid, channelSid, mediaProperties, type, routingProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InteractionChannelParticipantApi#createInteractionChannelParticipant");
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
| **interactionSid** | **String**| The Interaction Sid for the new Channel Participant. | |
| **channelSid** | **String**| The Channel Sid for the new Channel Participant. | |
| **mediaProperties** | [**Object**](Object.md)| JSON representing the Media Properties for the new Participant. | |
| **type** | **InteractionChannelParticipantEnumType**|  | [enum: supervisor, customer, external, agent, unknown] |
| **routingProperties** | [**Object**](Object.md)| Object representing the Routing Properties for the new Participant. | [optional] |

### Return type

[**FlexV1InteractionInteractionChannelInteractionChannelParticipant**](FlexV1InteractionInteractionChannelInteractionChannelParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="listInteractionChannelParticipant"></a>
# **listInteractionChannelParticipant**
> ListInteractionChannelParticipantResponse listInteractionChannelParticipant(interactionSid, channelSid, pageSize, page, pageToken)



List all Participants for a Channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InteractionChannelParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InteractionChannelParticipantApi apiInstance = new FlexV1InteractionChannelParticipantApi(defaultClient);
    String interactionSid = "interactionSid_example"; // String | The Interaction Sid for this channel.
    String channelSid = "channelSid_example"; // String | The Channel Sid for this Participant.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListInteractionChannelParticipantResponse result = apiInstance.listInteractionChannelParticipant(interactionSid, channelSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InteractionChannelParticipantApi#listInteractionChannelParticipant");
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
| **interactionSid** | **String**| The Interaction Sid for this channel. | |
| **channelSid** | **String**| The Channel Sid for this Participant. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListInteractionChannelParticipantResponse**](ListInteractionChannelParticipantResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateInteractionChannelParticipant"></a>
# **updateInteractionChannelParticipant**
> FlexV1InteractionInteractionChannelInteractionChannelParticipant updateInteractionChannelParticipant(interactionSid, channelSid, sid, status)



Update an existing Channel Participant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InteractionChannelParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InteractionChannelParticipantApi apiInstance = new FlexV1InteractionChannelParticipantApi(defaultClient);
    String interactionSid = "interactionSid_example"; // String | The Interaction Sid for this channel.
    String channelSid = "channelSid_example"; // String | The Channel Sid for this Participant.
    String sid = "sid_example"; // String | The unique string created by Twilio to identify an Interaction Channel resource.
    InteractionChannelParticipantEnumStatus status = InteractionChannelParticipantEnumStatus.fromValue("closed"); // InteractionChannelParticipantEnumStatus | 
    try {
      FlexV1InteractionInteractionChannelInteractionChannelParticipant result = apiInstance.updateInteractionChannelParticipant(interactionSid, channelSid, sid, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InteractionChannelParticipantApi#updateInteractionChannelParticipant");
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
| **interactionSid** | **String**| The Interaction Sid for this channel. | |
| **channelSid** | **String**| The Channel Sid for this Participant. | |
| **sid** | **String**| The unique string created by Twilio to identify an Interaction Channel resource. | |
| **status** | **InteractionChannelParticipantEnumStatus**|  | [enum: closed, wrapup] |

### Return type

[**FlexV1InteractionInteractionChannelInteractionChannelParticipant**](FlexV1InteractionInteractionChannelInteractionChannelParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

