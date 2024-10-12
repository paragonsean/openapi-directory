# DefaultApi

All URIs are relative to *http://messaging-chime.us-east-1.amazonaws.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**associateChannelFlow**](DefaultApi.md#associateChannelFlow) | **PUT** /channels/{channelArn}/channel-flow#x-amz-chime-bearer |  |
| [**batchCreateChannelMembership**](DefaultApi.md#batchCreateChannelMembership) | **POST** /channels/{channelArn}/memberships#operation&#x3D;batch-create&amp;x-amz-chime-bearer |  |
| [**channelFlowCallback**](DefaultApi.md#channelFlowCallback) | **POST** /channels/{channelArn}#operation&#x3D;channel-flow-callback |  |
| [**createChannel**](DefaultApi.md#createChannel) | **POST** /channels#x-amz-chime-bearer |  |
| [**createChannelBan**](DefaultApi.md#createChannelBan) | **POST** /channels/{channelArn}/bans#x-amz-chime-bearer |  |
| [**createChannelFlow**](DefaultApi.md#createChannelFlow) | **POST** /channel-flows |  |
| [**createChannelMembership**](DefaultApi.md#createChannelMembership) | **POST** /channels/{channelArn}/memberships#x-amz-chime-bearer |  |
| [**createChannelModerator**](DefaultApi.md#createChannelModerator) | **POST** /channels/{channelArn}/moderators#x-amz-chime-bearer |  |
| [**deleteChannel**](DefaultApi.md#deleteChannel) | **DELETE** /channels/{channelArn}#x-amz-chime-bearer |  |
| [**deleteChannelBan**](DefaultApi.md#deleteChannelBan) | **DELETE** /channels/{channelArn}/bans/{memberArn}#x-amz-chime-bearer |  |
| [**deleteChannelFlow**](DefaultApi.md#deleteChannelFlow) | **DELETE** /channel-flows/{channelFlowArn} |  |
| [**deleteChannelMembership**](DefaultApi.md#deleteChannelMembership) | **DELETE** /channels/{channelArn}/memberships/{memberArn}#x-amz-chime-bearer |  |
| [**deleteChannelMessage**](DefaultApi.md#deleteChannelMessage) | **DELETE** /channels/{channelArn}/messages/{messageId}#x-amz-chime-bearer |  |
| [**deleteChannelModerator**](DefaultApi.md#deleteChannelModerator) | **DELETE** /channels/{channelArn}/moderators/{channelModeratorArn}#x-amz-chime-bearer |  |
| [**deleteMessagingStreamingConfigurations**](DefaultApi.md#deleteMessagingStreamingConfigurations) | **DELETE** /app-instances/{appInstanceArn}/streaming-configurations |  |
| [**describeChannel**](DefaultApi.md#describeChannel) | **GET** /channels/{channelArn}#x-amz-chime-bearer |  |
| [**describeChannelBan**](DefaultApi.md#describeChannelBan) | **GET** /channels/{channelArn}/bans/{memberArn}#x-amz-chime-bearer |  |
| [**describeChannelFlow**](DefaultApi.md#describeChannelFlow) | **GET** /channel-flows/{channelFlowArn} |  |
| [**describeChannelMembership**](DefaultApi.md#describeChannelMembership) | **GET** /channels/{channelArn}/memberships/{memberArn}#x-amz-chime-bearer |  |
| [**describeChannelMembershipForAppInstanceUser**](DefaultApi.md#describeChannelMembershipForAppInstanceUser) | **GET** /channels/{channelArn}#scope&#x3D;app-instance-user-membership&amp;app-instance-user-arn&amp;x-amz-chime-bearer |  |
| [**describeChannelModeratedByAppInstanceUser**](DefaultApi.md#describeChannelModeratedByAppInstanceUser) | **GET** /channels/{channelArn}#scope&#x3D;app-instance-user-moderated-channel&amp;app-instance-user-arn&amp;x-amz-chime-bearer |  |
| [**describeChannelModerator**](DefaultApi.md#describeChannelModerator) | **GET** /channels/{channelArn}/moderators/{channelModeratorArn}#x-amz-chime-bearer |  |
| [**disassociateChannelFlow**](DefaultApi.md#disassociateChannelFlow) | **DELETE** /channels/{channelArn}/channel-flow/{channelFlowArn}#x-amz-chime-bearer |  |
| [**getChannelMembershipPreferences**](DefaultApi.md#getChannelMembershipPreferences) | **GET** /channels/{channelArn}/memberships/{memberArn}/preferences#x-amz-chime-bearer |  |
| [**getChannelMessage**](DefaultApi.md#getChannelMessage) | **GET** /channels/{channelArn}/messages/{messageId}#x-amz-chime-bearer |  |
| [**getChannelMessageStatus**](DefaultApi.md#getChannelMessageStatus) | **GET** /channels/{channelArn}/messages/{messageId}#scope&#x3D;message-status&amp;x-amz-chime-bearer |  |
| [**getMessagingSessionEndpoint**](DefaultApi.md#getMessagingSessionEndpoint) | **GET** /endpoints/messaging-session |  |
| [**getMessagingStreamingConfigurations**](DefaultApi.md#getMessagingStreamingConfigurations) | **GET** /app-instances/{appInstanceArn}/streaming-configurations |  |
| [**listChannelBans**](DefaultApi.md#listChannelBans) | **GET** /channels/{channelArn}/bans#x-amz-chime-bearer |  |
| [**listChannelFlows**](DefaultApi.md#listChannelFlows) | **GET** /channel-flows#app-instance-arn |  |
| [**listChannelMemberships**](DefaultApi.md#listChannelMemberships) | **GET** /channels/{channelArn}/memberships#x-amz-chime-bearer |  |
| [**listChannelMembershipsForAppInstanceUser**](DefaultApi.md#listChannelMembershipsForAppInstanceUser) | **GET** /channels#scope&#x3D;app-instance-user-memberships&amp;x-amz-chime-bearer |  |
| [**listChannelMessages**](DefaultApi.md#listChannelMessages) | **GET** /channels/{channelArn}/messages#x-amz-chime-bearer |  |
| [**listChannelModerators**](DefaultApi.md#listChannelModerators) | **GET** /channels/{channelArn}/moderators#x-amz-chime-bearer |  |
| [**listChannels**](DefaultApi.md#listChannels) | **GET** /channels#app-instance-arn&amp;x-amz-chime-bearer |  |
| [**listChannelsAssociatedWithChannelFlow**](DefaultApi.md#listChannelsAssociatedWithChannelFlow) | **GET** /channels#scope&#x3D;channel-flow-associations&amp;channel-flow-arn |  |
| [**listChannelsModeratedByAppInstanceUser**](DefaultApi.md#listChannelsModeratedByAppInstanceUser) | **GET** /channels#scope&#x3D;app-instance-user-moderated-channels&amp;x-amz-chime-bearer |  |
| [**listSubChannels**](DefaultApi.md#listSubChannels) | **GET** /channels/{channelArn}/subchannels#x-amz-chime-bearer |  |
| [**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags#arn |  |
| [**putChannelExpirationSettings**](DefaultApi.md#putChannelExpirationSettings) | **PUT** /channels/{channelArn}/expiration-settings |  |
| [**putChannelMembershipPreferences**](DefaultApi.md#putChannelMembershipPreferences) | **PUT** /channels/{channelArn}/memberships/{memberArn}/preferences#x-amz-chime-bearer |  |
| [**putMessagingStreamingConfigurations**](DefaultApi.md#putMessagingStreamingConfigurations) | **PUT** /app-instances/{appInstanceArn}/streaming-configurations |  |
| [**redactChannelMessage**](DefaultApi.md#redactChannelMessage) | **POST** /channels/{channelArn}/messages/{messageId}#operation&#x3D;redact&amp;x-amz-chime-bearer |  |
| [**searchChannels**](DefaultApi.md#searchChannels) | **POST** /channels#operation&#x3D;search |  |
| [**sendChannelMessage**](DefaultApi.md#sendChannelMessage) | **POST** /channels/{channelArn}/messages#x-amz-chime-bearer |  |
| [**tagResource**](DefaultApi.md#tagResource) | **POST** /tags#operation&#x3D;tag-resource |  |
| [**untagResource**](DefaultApi.md#untagResource) | **POST** /tags#operation&#x3D;untag-resource |  |
| [**updateChannel**](DefaultApi.md#updateChannel) | **PUT** /channels/{channelArn}#x-amz-chime-bearer |  |
| [**updateChannelFlow**](DefaultApi.md#updateChannelFlow) | **PUT** /channel-flows/{channelFlowArn} |  |
| [**updateChannelMessage**](DefaultApi.md#updateChannelMessage) | **PUT** /channels/{channelArn}/messages/{messageId}#x-amz-chime-bearer |  |
| [**updateChannelReadMarker**](DefaultApi.md#updateChannelReadMarker) | **PUT** /channels/{channelArn}/readMarker#x-amz-chime-bearer |  |


<a id="associateChannelFlow"></a>
# **associateChannelFlow**
> associateChannelFlow(channelArn, xAmzChimeBearer, associateChannelFlowRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Associates a channel flow with a channel. Once associated, all messages to that channel go through channel flow processors. To stop processing, use the &lt;code&gt;DisassociateChannelFlow&lt;/code&gt; API.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only administrators or channel moderators can associate a channel flow. The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user making the API call.
    AssociateChannelFlowRequest associateChannelFlowRequest = new AssociateChannelFlowRequest(); // AssociateChannelFlowRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.associateChannelFlow(channelArn, xAmzChimeBearer, associateChannelFlowRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#associateChannelFlow");
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
| **channelArn** | **String**| The ARN of the channel. | |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user making the API call. | |
| **associateChannelFlowRequest** | [**AssociateChannelFlowRequest**](AssociateChannelFlowRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ConflictException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="batchCreateChannelMembership"></a>
# **batchCreateChannelMembership**
> BatchCreateChannelMembershipResponse batchCreateChannelMembership(channelArn, xAmzChimeBearer, operation, batchCreateChannelMembershipRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Adds a specified number of users and bots to a channel. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel to which you're adding users or bots.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String operation = "batch-create"; // String | 
    BatchCreateChannelMembershipRequest batchCreateChannelMembershipRequest = new BatchCreateChannelMembershipRequest(); // BatchCreateChannelMembershipRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      BatchCreateChannelMembershipResponse result = apiInstance.batchCreateChannelMembership(channelArn, xAmzChimeBearer, operation, batchCreateChannelMembershipRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchCreateChannelMembership");
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
| **channelArn** | **String**| The ARN of the channel to which you&#39;re adding users or bots. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **operation** | **String**|  | [enum: batch-create] |
| **batchCreateChannelMembershipRequest** | [**BatchCreateChannelMembershipRequest**](BatchCreateChannelMembershipRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**BatchCreateChannelMembershipResponse**](BatchCreateChannelMembershipResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ServiceFailureException |  -  |
| **481** | ServiceUnavailableException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | BadRequestException |  -  |
| **484** | NotFoundException |  -  |
| **485** | ForbiddenException |  -  |
| **486** | ThrottledClientException |  -  |
| **487** | ResourceLimitExceededException |  -  |

<a id="channelFlowCallback"></a>
# **channelFlowCallback**
> ChannelFlowCallbackResponse channelFlowCallback(channelArn, operation, channelFlowCallbackRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Calls back Amazon Chime SDK messaging with a processing response message. This should be invoked from the processor Lambda. This is a developer API.&lt;/p&gt; &lt;p&gt;You can return one of the following processing responses:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Update message content or metadata&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Deny a message&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Make no changes to the message&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String operation = "channel-flow-callback"; // String | 
    ChannelFlowCallbackRequest channelFlowCallbackRequest = new ChannelFlowCallbackRequest(); // ChannelFlowCallbackRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ChannelFlowCallbackResponse result = apiInstance.channelFlowCallback(channelArn, operation, channelFlowCallbackRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#channelFlowCallback");
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
| **channelArn** | **String**| The ARN of the channel. | |
| **operation** | **String**|  | [enum: channel-flow-callback] |
| **channelFlowCallbackRequest** | [**ChannelFlowCallbackRequest**](ChannelFlowCallbackRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ChannelFlowCallbackResponse**](ChannelFlowCallbackResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ConflictException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="createChannel"></a>
# **createChannel**
> CreateChannelResponse createChannel(xAmzChimeBearer, createChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a channel to which you can add users and send messages.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Restriction&lt;/b&gt;: You can&#39;t change a channel&#39;s privacy.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    CreateChannelRequest createChannelRequest = new CreateChannelRequest(); // CreateChannelRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateChannelResponse result = apiInstance.createChannel(xAmzChimeBearer, createChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createChannel");
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
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **createChannelRequest** | [**CreateChannelRequest**](CreateChannelRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateChannelResponse**](CreateChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ConflictException |  -  |
| **484** | ResourceLimitExceededException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="createChannelBan"></a>
# **createChannelBan**
> CreateChannelBanResponse createChannelBan(channelArn, xAmzChimeBearer, createChannelBanRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Permanently bans a member from a channel. Moderators can&#39;t add banned members to a channel. To undo a ban, you first have to &lt;code&gt;DeleteChannelBan&lt;/code&gt;, and then &lt;code&gt;CreateChannelMembership&lt;/code&gt;. Bans are cleaned up when you delete users or channels.&lt;/p&gt; &lt;p&gt;If you ban a user who is already part of a channel, that user is automatically kicked from the channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the ban request.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    CreateChannelBanRequest createChannelBanRequest = new CreateChannelBanRequest(); // CreateChannelBanRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateChannelBanResponse result = apiInstance.createChannelBan(channelArn, xAmzChimeBearer, createChannelBanRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createChannelBan");
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
| **channelArn** | **String**| The ARN of the ban request. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **createChannelBanRequest** | [**CreateChannelBanRequest**](CreateChannelBanRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateChannelBanResponse**](CreateChannelBanResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ConflictException |  -  |
| **484** | ResourceLimitExceededException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="createChannelFlow"></a>
# **createChannelFlow**
> CreateChannelFlowResponse createChannelFlow(createChannelFlowRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a channel flow, a container for processors. Processors are AWS Lambda functions that perform actions on chat messages, such as stripping out profanity. You can associate channel flows with channels, and the processors in the channel flow then take action on all messages sent to that channel. This is a developer API.&lt;/p&gt; &lt;p&gt;Channel flows process the following items:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;New and updated messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Persistent and non-persistent messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The Standard message type&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;note&gt; &lt;p&gt;Channel flows don&#39;t process Control or System messages. For more information about the message types provided by Chime SDK messaging, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/dg/using-the-messaging-sdk.html#msg-types\&quot;&gt;Message types&lt;/a&gt; in the &lt;i&gt;Amazon Chime developer guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateChannelFlowRequest createChannelFlowRequest = new CreateChannelFlowRequest(); // CreateChannelFlowRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateChannelFlowResponse result = apiInstance.createChannelFlow(createChannelFlowRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createChannelFlow");
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
| **createChannelFlowRequest** | [**CreateChannelFlowRequest**](CreateChannelFlowRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateChannelFlowResponse**](CreateChannelFlowResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ConflictException |  -  |
| **484** | ResourceLimitExceededException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="createChannelMembership"></a>
# **createChannelMembership**
> CreateChannelMembershipResponse createChannelMembership(channelArn, xAmzChimeBearer, createChannelMembershipRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Adds a member to a channel. The &lt;code&gt;InvitedBy&lt;/code&gt; field in &lt;code&gt;ChannelMembership&lt;/code&gt; is derived from the request header. A channel member can:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;List messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Send messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Receive messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Edit their own messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Leave the channel&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Privacy settings impact this action as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Public Channels: You do not need to be a member to list messages, but you must be a member to send messages.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Private Channels: You must be a member to list or send messages.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel to which you're adding users.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    CreateChannelMembershipRequest createChannelMembershipRequest = new CreateChannelMembershipRequest(); // CreateChannelMembershipRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateChannelMembershipResponse result = apiInstance.createChannelMembership(channelArn, xAmzChimeBearer, createChannelMembershipRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createChannelMembership");
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
| **channelArn** | **String**| The ARN of the channel to which you&#39;re adding users. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **createChannelMembershipRequest** | [**CreateChannelMembershipRequest**](CreateChannelMembershipRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateChannelMembershipResponse**](CreateChannelMembershipResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ConflictException |  -  |
| **485** | ResourceLimitExceededException |  -  |
| **486** | ThrottledClientException |  -  |
| **487** | ServiceUnavailableException |  -  |
| **488** | ServiceFailureException |  -  |

<a id="createChannelModerator"></a>
# **createChannelModerator**
> CreateChannelModeratorResponse createChannelModerator(channelArn, xAmzChimeBearer, createChannelModeratorRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a new &lt;code&gt;ChannelModerator&lt;/code&gt;. A channel moderator can:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Add and remove other members of the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Add and remove other moderators of the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Add and remove user bans for the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Redact messages in the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;List messages in the channel.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt;of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    CreateChannelModeratorRequest createChannelModeratorRequest = new CreateChannelModeratorRequest(); // CreateChannelModeratorRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateChannelModeratorResponse result = apiInstance.createChannelModerator(channelArn, xAmzChimeBearer, createChannelModeratorRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createChannelModerator");
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
| **channelArn** | **String**| The ARN of the channel. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **createChannelModeratorRequest** | [**CreateChannelModeratorRequest**](CreateChannelModeratorRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateChannelModeratorResponse**](CreateChannelModeratorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ConflictException |  -  |
| **484** | ResourceLimitExceededException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="deleteChannel"></a>
# **deleteChannel**
> deleteChannel(channelArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Immediately makes a channel and its memberships inaccessible and marks them for deletion. This is an irreversible process.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel being deleted.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteChannel(channelArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteChannel");
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
| **channelArn** | **String**| The ARN of the channel being deleted. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ConflictException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="deleteChannelBan"></a>
# **deleteChannelBan**
> deleteChannelBan(channelArn, memberArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Removes a member from a channel&#39;s ban list.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel from which the <code>AppInstanceUser</code> was banned.
    String memberArn = "memberArn_example"; // String | The ARN of the <code>AppInstanceUser</code> that you want to reinstate.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteChannelBan(channelArn, memberArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteChannelBan");
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
| **channelArn** | **String**| The ARN of the channel from which the &lt;code&gt;AppInstanceUser&lt;/code&gt; was banned. | |
| **memberArn** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; that you want to reinstate. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="deleteChannelFlow"></a>
# **deleteChannelFlow**
> deleteChannelFlow(channelFlowArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes a channel flow, an irreversible process. This is a developer API.&lt;/p&gt; &lt;note&gt; &lt;p&gt; This API works only when the channel flow is not associated with any channel. To get a list of all channels that a channel flow is associated with, use the &lt;code&gt;ListChannelsAssociatedWithChannelFlow&lt;/code&gt; API. Use the &lt;code&gt;DisassociateChannelFlow&lt;/code&gt; API to disassociate a channel flow from all channels. &lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelFlowArn = "channelFlowArn_example"; // String | The ARN of the channel flow.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteChannelFlow(channelFlowArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteChannelFlow");
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
| **channelFlowArn** | **String**| The ARN of the channel flow. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ConflictException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="deleteChannelMembership"></a>
# **deleteChannelMembership**
> deleteChannelMembership(channelArn, memberArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, subChannelId)



&lt;p&gt;Removes a member from a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel from which you want to remove the user.
    String memberArn = "memberArn_example"; // String | The <code>AppInstanceUserArn</code> of the member that you're removing from the channel.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String subChannelId = "subChannelId_example"; // String | <p>The ID of the SubChannel in the request.</p> <note> <p>Only for use by moderators.</p> </note>
    try {
      apiInstance.deleteChannelMembership(channelArn, memberArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, subChannelId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteChannelMembership");
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
| **channelArn** | **String**| The ARN of the channel from which you want to remove the user. | |
| **memberArn** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the member that you&#39;re removing from the channel. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **subChannelId** | **String**| &lt;p&gt;The ID of the SubChannel in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only for use by moderators.&lt;/p&gt; &lt;/note&gt; | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ConflictException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="deleteChannelMessage"></a>
# **deleteChannelMessage**
> deleteChannelMessage(channelArn, messageId, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, subChannelId)



&lt;p&gt;Deletes a channel message. Only admins can perform this action. Deletion makes messages inaccessible immediately. A background process deletes any revisions created by &lt;code&gt;UpdateChannelMessage&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String messageId = "messageId_example"; // String | The ID of the message being deleted.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String subChannelId = "subChannelId_example"; // String | <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when deleting messages in a SubChannel that the user belongs to.</p> </note>
    try {
      apiInstance.deleteChannelMessage(channelArn, messageId, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, subChannelId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteChannelMessage");
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
| **channelArn** | **String**| The ARN of the channel. | |
| **messageId** | **String**| The ID of the message being deleted. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **subChannelId** | **String**| &lt;p&gt;The ID of the SubChannel in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only required when deleting messages in a SubChannel that the user belongs to.&lt;/p&gt; &lt;/note&gt; | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="deleteChannelModerator"></a>
# **deleteChannelModerator**
> deleteChannelModerator(channelArn, channelModeratorArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes a channel moderator.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String channelModeratorArn = "channelModeratorArn_example"; // String | The <code>AppInstanceUserArn</code> of the moderator being deleted.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteChannelModerator(channelArn, channelModeratorArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteChannelModerator");
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
| **channelArn** | **String**| The ARN of the channel. | |
| **channelModeratorArn** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the moderator being deleted. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="deleteMessagingStreamingConfigurations"></a>
# **deleteMessagingStreamingConfigurations**
> deleteMessagingStreamingConfigurations(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes the streaming configurations for an &lt;code&gt;AppInstance&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/streaming-export.html\&quot;&gt;Streaming messaging data&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceArn = "appInstanceArn_example"; // String | The ARN of the streaming configurations being deleted.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteMessagingStreamingConfigurations(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteMessagingStreamingConfigurations");
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
| **appInstanceArn** | **String**| The ARN of the streaming configurations being deleted. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="describeChannel"></a>
# **describeChannel**
> DescribeChannelResponse describeChannel(channelArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns the full details of a channel in an Amazon Chime &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeChannelResponse result = apiInstance.describeChannel(channelArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeChannel");
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
| **channelArn** | **String**| The ARN of the channel. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeChannelResponse**](DescribeChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="describeChannelBan"></a>
# **describeChannelBan**
> DescribeChannelBanResponse describeChannelBan(channelArn, memberArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns the full details of a channel ban.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel from which the user is banned.
    String memberArn = "memberArn_example"; // String | The <code>AppInstanceUserArn</code> of the member being banned.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeChannelBanResponse result = apiInstance.describeChannelBan(channelArn, memberArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeChannelBan");
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
| **channelArn** | **String**| The ARN of the channel from which the user is banned. | |
| **memberArn** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the member being banned. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeChannelBanResponse**](DescribeChannelBanResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="describeChannelFlow"></a>
# **describeChannelFlow**
> DescribeChannelFlowResponse describeChannelFlow(channelFlowArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Returns the full details of a channel flow in an Amazon Chime &lt;code&gt;AppInstance&lt;/code&gt;. This is a developer API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelFlowArn = "channelFlowArn_example"; // String | The ARN of the channel flow.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeChannelFlowResponse result = apiInstance.describeChannelFlow(channelFlowArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeChannelFlow");
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
| **channelFlowArn** | **String**| The ARN of the channel flow. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeChannelFlowResponse**](DescribeChannelFlowResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="describeChannelMembership"></a>
# **describeChannelMembership**
> DescribeChannelMembershipResponse describeChannelMembership(channelArn, memberArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, subChannelId)



&lt;p&gt;Returns the full details of a user&#39;s channel membership.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String memberArn = "memberArn_example"; // String | The <code>AppInstanceUserArn</code> of the member.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String subChannelId = "subChannelId_example"; // String | <p>The ID of the SubChannel in the request. The response contains an <code>ElasticChannelConfiguration</code> object.</p> <note> <p>Only required to get a user’s SubChannel membership details.</p> </note>
    try {
      DescribeChannelMembershipResponse result = apiInstance.describeChannelMembership(channelArn, memberArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, subChannelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeChannelMembership");
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
| **channelArn** | **String**| The ARN of the channel. | |
| **memberArn** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the member. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **subChannelId** | **String**| &lt;p&gt;The ID of the SubChannel in the request. The response contains an &lt;code&gt;ElasticChannelConfiguration&lt;/code&gt; object.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only required to get a user’s SubChannel membership details.&lt;/p&gt; &lt;/note&gt; | [optional] |

### Return type

[**DescribeChannelMembershipResponse**](DescribeChannelMembershipResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="describeChannelMembershipForAppInstanceUser"></a>
# **describeChannelMembershipForAppInstanceUser**
> DescribeChannelMembershipForAppInstanceUserResponse describeChannelMembershipForAppInstanceUser(channelArn, appInstanceUserArn, xAmzChimeBearer, scope, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt; Returns the details of a channel based on the membership of the specified &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel to which the user belongs.
    String appInstanceUserArn = "appInstanceUserArn_example"; // String | The ARN of the user or bot in a channel.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String scope = "app-instance-user-membership"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeChannelMembershipForAppInstanceUserResponse result = apiInstance.describeChannelMembershipForAppInstanceUser(channelArn, appInstanceUserArn, xAmzChimeBearer, scope, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeChannelMembershipForAppInstanceUser");
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
| **channelArn** | **String**| The ARN of the channel to which the user belongs. | |
| **appInstanceUserArn** | **String**| The ARN of the user or bot in a channel. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **scope** | **String**|  | [enum: app-instance-user-membership] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeChannelMembershipForAppInstanceUserResponse**](DescribeChannelMembershipForAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="describeChannelModeratedByAppInstanceUser"></a>
# **describeChannelModeratedByAppInstanceUser**
> DescribeChannelModeratedByAppInstanceUserResponse describeChannelModeratedByAppInstanceUser(channelArn, appInstanceUserArn, xAmzChimeBearer, scope, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns the full details of a channel moderated by the specified &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the moderated channel.
    String appInstanceUserArn = "appInstanceUserArn_example"; // String | The ARN of the user or bot in the moderated channel.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String scope = "app-instance-user-moderated-channel"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeChannelModeratedByAppInstanceUserResponse result = apiInstance.describeChannelModeratedByAppInstanceUser(channelArn, appInstanceUserArn, xAmzChimeBearer, scope, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeChannelModeratedByAppInstanceUser");
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
| **channelArn** | **String**| The ARN of the moderated channel. | |
| **appInstanceUserArn** | **String**| The ARN of the user or bot in the moderated channel. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **scope** | **String**|  | [enum: app-instance-user-moderated-channel] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeChannelModeratedByAppInstanceUserResponse**](DescribeChannelModeratedByAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="describeChannelModerator"></a>
# **describeChannelModerator**
> DescribeChannelModeratorResponse describeChannelModerator(channelArn, channelModeratorArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns the full details of a single ChannelModerator.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String channelModeratorArn = "channelModeratorArn_example"; // String | The <code>AppInstanceUserArn</code> of the channel moderator.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeChannelModeratorResponse result = apiInstance.describeChannelModerator(channelArn, channelModeratorArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeChannelModerator");
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
| **channelArn** | **String**| The ARN of the channel. | |
| **channelModeratorArn** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the channel moderator. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeChannelModeratorResponse**](DescribeChannelModeratorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="disassociateChannelFlow"></a>
# **disassociateChannelFlow**
> disassociateChannelFlow(channelArn, channelFlowArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Disassociates a channel flow from all its channels. Once disassociated, all messages to that channel stop going through the channel flow processor.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only administrators or channel moderators can disassociate a channel flow.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String channelFlowArn = "channelFlowArn_example"; // String | The ARN of the channel flow.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user making the API call.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.disassociateChannelFlow(channelArn, channelFlowArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#disassociateChannelFlow");
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
| **channelArn** | **String**| The ARN of the channel. | |
| **channelFlowArn** | **String**| The ARN of the channel flow. | |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user making the API call. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ConflictException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="getChannelMembershipPreferences"></a>
# **getChannelMembershipPreferences**
> GetChannelMembershipPreferencesResponse getChannelMembershipPreferences(channelArn, memberArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets the membership preferences of an &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; for the specified channel. A user or a bot must be a member of the channel and own the membership in order to retrieve membership preferences. Users or bots in the &lt;code&gt;AppInstanceAdmin&lt;/code&gt; and channel moderator roles can&#39;t retrieve preferences for other users or bots. Banned users or bots can&#39;t retrieve membership preferences for the channel from which they are banned.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String memberArn = "memberArn_example"; // String | The <code>AppInstanceUserArn</code> of the member retrieving the preferences.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetChannelMembershipPreferencesResponse result = apiInstance.getChannelMembershipPreferences(channelArn, memberArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getChannelMembershipPreferences");
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
| **channelArn** | **String**| The ARN of the channel. | |
| **memberArn** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the member retrieving the preferences. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetChannelMembershipPreferencesResponse**](GetChannelMembershipPreferencesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | UnauthorizedClientException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="getChannelMessage"></a>
# **getChannelMessage**
> GetChannelMessageResponse getChannelMessage(channelArn, messageId, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, subChannelId)



&lt;p&gt;Gets the full details of a channel message.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String messageId = "messageId_example"; // String | The ID of the message.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String subChannelId = "subChannelId_example"; // String | <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when getting messages in a SubChannel that the user belongs to.</p> </note>
    try {
      GetChannelMessageResponse result = apiInstance.getChannelMessage(channelArn, messageId, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, subChannelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getChannelMessage");
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
| **channelArn** | **String**| The ARN of the channel. | |
| **messageId** | **String**| The ID of the message. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **subChannelId** | **String**| &lt;p&gt;The ID of the SubChannel in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only required when getting messages in a SubChannel that the user belongs to.&lt;/p&gt; &lt;/note&gt; | [optional] |

### Return type

[**GetChannelMessageResponse**](GetChannelMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getChannelMessageStatus"></a>
# **getChannelMessageStatus**
> GetChannelMessageStatusResponse getChannelMessageStatus(channelArn, messageId, xAmzChimeBearer, scope, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, subChannelId)



&lt;p&gt;Gets message status for a specified &lt;code&gt;messageId&lt;/code&gt;. Use this API to determine the intermediate status of messages going through channel flow processing. The API provides an alternative to retrieving message status if the event was not received because a client wasn&#39;t connected to a websocket. &lt;/p&gt; &lt;p&gt;Messages can have any one of these statuses.&lt;/p&gt; &lt;dl&gt; &lt;dt&gt;SENT&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Message processed successfully&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;PENDING&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Ongoing processing&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;FAILED&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Processing failed&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;DENIED&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Message denied by the processor&lt;/p&gt; &lt;/dd&gt; &lt;/dl&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;This API does not return statuses for denied messages, because we don&#39;t store them once the processor denies them. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Only the message sender can invoke this API.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel
    String messageId = "messageId_example"; // String | The ID of the message.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user making the API call.
    String scope = "message-status"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String subChannelId = "subChannelId_example"; // String | <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when getting message status in a SubChannel that the user belongs to.</p> </note>
    try {
      GetChannelMessageStatusResponse result = apiInstance.getChannelMessageStatus(channelArn, messageId, xAmzChimeBearer, scope, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, subChannelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getChannelMessageStatus");
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
| **channelArn** | **String**| The ARN of the channel | |
| **messageId** | **String**| The ID of the message. | |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user making the API call. | |
| **scope** | **String**|  | [enum: message-status] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **subChannelId** | **String**| &lt;p&gt;The ID of the SubChannel in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only required when getting message status in a SubChannel that the user belongs to.&lt;/p&gt; &lt;/note&gt; | [optional] |

### Return type

[**GetChannelMessageStatusResponse**](GetChannelMessageStatusResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="getMessagingSessionEndpoint"></a>
# **getMessagingSessionEndpoint**
> GetMessagingSessionEndpointResponse getMessagingSessionEndpoint(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



The details of the endpoint for the messaging session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetMessagingSessionEndpointResponse result = apiInstance.getMessagingSessionEndpoint(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMessagingSessionEndpoint");
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
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetMessagingSessionEndpointResponse**](GetMessagingSessionEndpointResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ThrottledClientException |  -  |
| **483** | ServiceUnavailableException |  -  |
| **484** | ServiceFailureException |  -  |

<a id="getMessagingStreamingConfigurations"></a>
# **getMessagingStreamingConfigurations**
> GetMessagingStreamingConfigurationsResponse getMessagingStreamingConfigurations(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves the data streaming configuration for an &lt;code&gt;AppInstance&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/streaming-export.html\&quot;&gt;Streaming messaging data&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceArn = "appInstanceArn_example"; // String | The ARN of the streaming configurations.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetMessagingStreamingConfigurationsResponse result = apiInstance.getMessagingStreamingConfigurations(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMessagingStreamingConfigurations");
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
| **appInstanceArn** | **String**| The ARN of the streaming configurations. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetMessagingStreamingConfigurationsResponse**](GetMessagingStreamingConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="listChannelBans"></a>
# **listChannelBans**
> ListChannelBansResponse listChannelBans(channelArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2)



&lt;p&gt;Lists all the users and bots banned from a particular channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer maxResults = 56; // Integer | The maximum number of bans that you want returned.
    String nextToken = "nextToken_example"; // String | The token passed by previous API calls until all requested bans are returned.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListChannelBansResponse result = apiInstance.listChannelBans(channelArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listChannelBans");
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
| **channelArn** | **String**| The ARN of the channel. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **Integer**| The maximum number of bans that you want returned. | [optional] |
| **nextToken** | **String**| The token passed by previous API calls until all requested bans are returned. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListChannelBansResponse**](ListChannelBansResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listChannelFlows"></a>
# **listChannelFlows**
> ListChannelFlowsResponse listChannelFlows(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2)



Returns a paginated lists of all the channel flows created under a single Chime. This is a developer API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceArn = "appInstanceArn_example"; // String | The ARN of the app instance.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer maxResults = 56; // Integer | The maximum number of channel flows that you want to return.
    String nextToken = "nextToken_example"; // String | The token passed by previous API calls until all requested channel flows are returned.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListChannelFlowsResponse result = apiInstance.listChannelFlows(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listChannelFlows");
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
| **appInstanceArn** | **String**| The ARN of the app instance. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **Integer**| The maximum number of channel flows that you want to return. | [optional] |
| **nextToken** | **String**| The token passed by previous API calls until all requested channel flows are returned. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListChannelFlowsResponse**](ListChannelFlowsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listChannelMemberships"></a>
# **listChannelMemberships**
> ListChannelMembershipsResponse listChannelMemberships(channelArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, type, maxResults, nextToken, subChannelId, maxResults2, nextToken2)



&lt;p&gt;Lists all channel memberships in a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;If you want to list the channels to which a specific app instance user belongs, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/APIReference/API_messaging-chime_ListChannelMembershipsForAppInstanceUser.html\&quot;&gt;ListChannelMembershipsForAppInstanceUser&lt;/a&gt; API.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The maximum number of channel memberships that you want returned.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String type = "DEFAULT"; // String | The membership type of a user, <code>DEFAULT</code> or <code>HIDDEN</code>. Default members are returned as part of <code>ListChannelMemberships</code> if no type is specified. Hidden members are only returned if the type filter in <code>ListChannelMemberships</code> equals <code>HIDDEN</code>.
    Integer maxResults = 56; // Integer | The maximum number of channel memberships that you want returned.
    String nextToken = "nextToken_example"; // String | The token passed by previous API calls until all requested channel memberships are returned.
    String subChannelId = "subChannelId_example"; // String | <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when listing a user's memberships in a particular sub-channel of an elastic channel.</p> </note>
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListChannelMembershipsResponse result = apiInstance.listChannelMemberships(channelArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, type, maxResults, nextToken, subChannelId, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listChannelMemberships");
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
| **channelArn** | **String**| The maximum number of channel memberships that you want returned. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **type** | **String**| The membership type of a user, &lt;code&gt;DEFAULT&lt;/code&gt; or &lt;code&gt;HIDDEN&lt;/code&gt;. Default members are returned as part of &lt;code&gt;ListChannelMemberships&lt;/code&gt; if no type is specified. Hidden members are only returned if the type filter in &lt;code&gt;ListChannelMemberships&lt;/code&gt; equals &lt;code&gt;HIDDEN&lt;/code&gt;. | [optional] [enum: DEFAULT, HIDDEN] |
| **maxResults** | **Integer**| The maximum number of channel memberships that you want returned. | [optional] |
| **nextToken** | **String**| The token passed by previous API calls until all requested channel memberships are returned. | [optional] |
| **subChannelId** | **String**| &lt;p&gt;The ID of the SubChannel in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only required when listing a user&#39;s memberships in a particular sub-channel of an elastic channel.&lt;/p&gt; &lt;/note&gt; | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListChannelMembershipsResponse**](ListChannelMembershipsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listChannelMembershipsForAppInstanceUser"></a>
# **listChannelMembershipsForAppInstanceUser**
> ListChannelMembershipsForAppInstanceUserResponse listChannelMembershipsForAppInstanceUser(xAmzChimeBearer, scope, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, appInstanceUserArn, maxResults, nextToken, maxResults2, nextToken2)



&lt;p&gt; Lists all channels that an &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; is a part of. Only an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; can call the API with a user ARN that is not their own. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String scope = "app-instance-user-memberships"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String appInstanceUserArn = "appInstanceUserArn_example"; // String | The ARN of the user or bot.
    Integer maxResults = 56; // Integer | The maximum number of users that you want returned.
    String nextToken = "nextToken_example"; // String | The token returned from previous API requests until the number of channel memberships is reached.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListChannelMembershipsForAppInstanceUserResponse result = apiInstance.listChannelMembershipsForAppInstanceUser(xAmzChimeBearer, scope, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, appInstanceUserArn, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listChannelMembershipsForAppInstanceUser");
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
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **scope** | **String**|  | [enum: app-instance-user-memberships] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **appInstanceUserArn** | **String**| The ARN of the user or bot. | [optional] |
| **maxResults** | **Integer**| The maximum number of users that you want returned. | [optional] |
| **nextToken** | **String**| The token returned from previous API requests until the number of channel memberships is reached. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListChannelMembershipsForAppInstanceUserResponse**](ListChannelMembershipsForAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listChannelMessages"></a>
# **listChannelMessages**
> ListChannelMessagesResponse listChannelMessages(channelArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, sortOrder, notBefore, notAfter, maxResults, nextToken, subChannelId, maxResults2, nextToken2)



&lt;p&gt;List all the messages in a channel. Returns a paginated list of &lt;code&gt;ChannelMessages&lt;/code&gt;. By default, sorted by creation timestamp in descending order.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Redacted messages appear in the results as empty, since they are only redacted, not deleted. Deleted messages do not appear in the results. This action always returns the latest version of an edited message.&lt;/p&gt; &lt;p&gt;Also, the &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String sortOrder = "ASCENDING"; // String | The order in which you want messages sorted. Default is Descending, based on time created.
    OffsetDateTime notBefore = OffsetDateTime.now(); // OffsetDateTime | The initial or starting time stamp for your requested messages.
    OffsetDateTime notAfter = OffsetDateTime.now(); // OffsetDateTime | The final or ending time stamp for your requested messages.
    Integer maxResults = 56; // Integer | The maximum number of messages that you want returned.
    String nextToken = "nextToken_example"; // String | The token passed by previous API calls until all requested messages are returned.
    String subChannelId = "subChannelId_example"; // String | <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when listing the messages in a SubChannel that the user belongs to.</p> </note>
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListChannelMessagesResponse result = apiInstance.listChannelMessages(channelArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, sortOrder, notBefore, notAfter, maxResults, nextToken, subChannelId, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listChannelMessages");
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
| **channelArn** | **String**| The ARN of the channel. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **sortOrder** | **String**| The order in which you want messages sorted. Default is Descending, based on time created. | [optional] [enum: ASCENDING, DESCENDING] |
| **notBefore** | **OffsetDateTime**| The initial or starting time stamp for your requested messages. | [optional] |
| **notAfter** | **OffsetDateTime**| The final or ending time stamp for your requested messages. | [optional] |
| **maxResults** | **Integer**| The maximum number of messages that you want returned. | [optional] |
| **nextToken** | **String**| The token passed by previous API calls until all requested messages are returned. | [optional] |
| **subChannelId** | **String**| &lt;p&gt;The ID of the SubChannel in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only required when listing the messages in a SubChannel that the user belongs to.&lt;/p&gt; &lt;/note&gt; | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListChannelMessagesResponse**](ListChannelMessagesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listChannelModerators"></a>
# **listChannelModerators**
> ListChannelModeratorsResponse listChannelModerators(channelArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2)



&lt;p&gt;Lists all the moderators for a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer maxResults = 56; // Integer | The maximum number of moderators that you want returned.
    String nextToken = "nextToken_example"; // String | The token passed by previous API calls until all requested moderators are returned.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListChannelModeratorsResponse result = apiInstance.listChannelModerators(channelArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listChannelModerators");
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
| **channelArn** | **String**| The ARN of the channel. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **Integer**| The maximum number of moderators that you want returned. | [optional] |
| **nextToken** | **String**| The token passed by previous API calls until all requested moderators are returned. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListChannelModeratorsResponse**](ListChannelModeratorsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listChannels"></a>
# **listChannels**
> ListChannelsResponse listChannels(appInstanceArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, privacy, maxResults, nextToken, maxResults2, nextToken2)



&lt;p&gt;Lists all Channels created under a single Chime App as a paginated list. You can specify filters to narrow results.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Functionality &amp;amp; restrictions&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use privacy &#x3D; &lt;code&gt;PUBLIC&lt;/code&gt; to retrieve all public channels in the account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Only an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; can set privacy &#x3D; &lt;code&gt;PRIVATE&lt;/code&gt; to list the private channels in an account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String privacy = "PUBLIC"; // String | The privacy setting. <code>PUBLIC</code> retrieves all the public channels. <code>PRIVATE</code> retrieves private channels. Only an <code>AppInstanceAdmin</code> can retrieve private channels. 
    Integer maxResults = 56; // Integer | The maximum number of channels that you want to return.
    String nextToken = "nextToken_example"; // String | The token passed by previous API calls until all requested channels are returned.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListChannelsResponse result = apiInstance.listChannels(appInstanceArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, privacy, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listChannels");
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
| **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **privacy** | **String**| The privacy setting. &lt;code&gt;PUBLIC&lt;/code&gt; retrieves all the public channels. &lt;code&gt;PRIVATE&lt;/code&gt; retrieves private channels. Only an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; can retrieve private channels.  | [optional] [enum: PUBLIC, PRIVATE] |
| **maxResults** | **Integer**| The maximum number of channels that you want to return. | [optional] |
| **nextToken** | **String**| The token passed by previous API calls until all requested channels are returned. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListChannelsResponse**](ListChannelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listChannelsAssociatedWithChannelFlow"></a>
# **listChannelsAssociatedWithChannelFlow**
> ListChannelsAssociatedWithChannelFlowResponse listChannelsAssociatedWithChannelFlow(channelFlowArn, scope, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2)



Lists all channels associated with a specified channel flow. You can associate a channel flow with multiple channels, but you can only associate a channel with one channel flow. This is a developer API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelFlowArn = "channelFlowArn_example"; // String | The ARN of the channel flow.
    String scope = "channel-flow-associations"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer maxResults = 56; // Integer | The maximum number of channels that you want to return.
    String nextToken = "nextToken_example"; // String | The token passed by previous API calls until all requested channels are returned.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListChannelsAssociatedWithChannelFlowResponse result = apiInstance.listChannelsAssociatedWithChannelFlow(channelFlowArn, scope, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listChannelsAssociatedWithChannelFlow");
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
| **channelFlowArn** | **String**| The ARN of the channel flow. | |
| **scope** | **String**|  | [enum: channel-flow-associations] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **Integer**| The maximum number of channels that you want to return. | [optional] |
| **nextToken** | **String**| The token passed by previous API calls until all requested channels are returned. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListChannelsAssociatedWithChannelFlowResponse**](ListChannelsAssociatedWithChannelFlowResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listChannelsModeratedByAppInstanceUser"></a>
# **listChannelsModeratedByAppInstanceUser**
> ListChannelsModeratedByAppInstanceUserResponse listChannelsModeratedByAppInstanceUser(xAmzChimeBearer, scope, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, appInstanceUserArn, maxResults, nextToken, maxResults2, nextToken2)



&lt;p&gt;A list of the channels moderated by an &lt;code&gt;AppInstanceUser&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String scope = "app-instance-user-moderated-channels"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String appInstanceUserArn = "appInstanceUserArn_example"; // String | The ARN of the user or bot in the moderated channel.
    Integer maxResults = 56; // Integer | The maximum number of channels in the request.
    String nextToken = "nextToken_example"; // String | The token returned from previous API requests until the number of channels moderated by the user is reached.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListChannelsModeratedByAppInstanceUserResponse result = apiInstance.listChannelsModeratedByAppInstanceUser(xAmzChimeBearer, scope, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, appInstanceUserArn, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listChannelsModeratedByAppInstanceUser");
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
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **scope** | **String**|  | [enum: app-instance-user-moderated-channels] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **appInstanceUserArn** | **String**| The ARN of the user or bot in the moderated channel. | [optional] |
| **maxResults** | **Integer**| The maximum number of channels in the request. | [optional] |
| **nextToken** | **String**| The token returned from previous API requests until the number of channels moderated by the user is reached. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListChannelsModeratedByAppInstanceUserResponse**](ListChannelsModeratedByAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listSubChannels"></a>
# **listSubChannels**
> ListSubChannelsResponse listSubChannels(channelArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2)



Lists all the SubChannels in an elastic channel when given a channel ID. Available only to the app instance admins and channel moderators of elastic channels.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of elastic channel.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user making the API call.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer maxResults = 56; // Integer | The maximum number of sub-channels that you want to return.
    String nextToken = "nextToken_example"; // String | The token passed by previous API calls until all requested sub-channels are returned.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListSubChannelsResponse result = apiInstance.listSubChannels(channelArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listSubChannels");
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
| **channelArn** | **String**| The ARN of elastic channel. | |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user making the API call. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **Integer**| The maximum number of sub-channels that you want to return. | [optional] |
| **nextToken** | **String**| The token passed by previous API calls until all requested sub-channels are returned. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListSubChannelsResponse**](ListSubChannelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listTagsForResource"></a>
# **listTagsForResource**
> ListTagsForResourceResponse listTagsForResource(arn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Lists the tags applied to an Amazon Chime SDK messaging resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String arn = "arn_example"; // String | The ARN of the resource.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListTagsForResourceResponse result = apiInstance.listTagsForResource(arn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTagsForResource");
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
| **arn** | **String**| The ARN of the resource. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="putChannelExpirationSettings"></a>
# **putChannelExpirationSettings**
> PutChannelExpirationSettingsResponse putChannelExpirationSettings(channelArn, putChannelExpirationSettingsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Sets the number of days before the channel is automatically deleted.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A background process deletes expired channels within 6 hours of expiration. Actual deletion times may vary.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Expired channels that have not yet been deleted appear as active, and you can update their expiration settings. The system honors the new settings.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    PutChannelExpirationSettingsRequest putChannelExpirationSettingsRequest = new PutChannelExpirationSettingsRequest(); // PutChannelExpirationSettingsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    try {
      PutChannelExpirationSettingsResponse result = apiInstance.putChannelExpirationSettings(channelArn, putChannelExpirationSettingsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putChannelExpirationSettings");
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
| **channelArn** | **String**| The ARN of the channel. | |
| **putChannelExpirationSettingsRequest** | [**PutChannelExpirationSettingsRequest**](PutChannelExpirationSettingsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | [optional] |

### Return type

[**PutChannelExpirationSettingsResponse**](PutChannelExpirationSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ConflictException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="putChannelMembershipPreferences"></a>
# **putChannelMembershipPreferences**
> PutChannelMembershipPreferencesResponse putChannelMembershipPreferences(channelArn, memberArn, xAmzChimeBearer, putChannelMembershipPreferencesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Sets the membership preferences of an &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; for the specified channel. The user or bot must be a member of the channel. Only the user or bot who owns the membership can set preferences. Users or bots in the &lt;code&gt;AppInstanceAdmin&lt;/code&gt; and channel moderator roles can&#39;t set preferences for other users. Banned users or bots can&#39;t set membership preferences for the channel from which they are banned.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The x-amz-chime-bearer request header is mandatory. Use the ARN of an &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String memberArn = "memberArn_example"; // String | The ARN of the member setting the preferences.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    PutChannelMembershipPreferencesRequest putChannelMembershipPreferencesRequest = new PutChannelMembershipPreferencesRequest(); // PutChannelMembershipPreferencesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutChannelMembershipPreferencesResponse result = apiInstance.putChannelMembershipPreferences(channelArn, memberArn, xAmzChimeBearer, putChannelMembershipPreferencesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putChannelMembershipPreferences");
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
| **channelArn** | **String**| The ARN of the channel. | |
| **memberArn** | **String**| The ARN of the member setting the preferences. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **putChannelMembershipPreferencesRequest** | [**PutChannelMembershipPreferencesRequest**](PutChannelMembershipPreferencesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutChannelMembershipPreferencesResponse**](PutChannelMembershipPreferencesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ConflictException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="putMessagingStreamingConfigurations"></a>
# **putMessagingStreamingConfigurations**
> PutMessagingStreamingConfigurationsResponse putMessagingStreamingConfigurations(appInstanceArn, putMessagingStreamingConfigurationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Sets the data streaming configuration for an &lt;code&gt;AppInstance&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/streaming-export.html\&quot;&gt;Streaming messaging data&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceArn = "appInstanceArn_example"; // String | The ARN of the streaming configuration.
    PutMessagingStreamingConfigurationsRequest putMessagingStreamingConfigurationsRequest = new PutMessagingStreamingConfigurationsRequest(); // PutMessagingStreamingConfigurationsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutMessagingStreamingConfigurationsResponse result = apiInstance.putMessagingStreamingConfigurations(appInstanceArn, putMessagingStreamingConfigurationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putMessagingStreamingConfigurations");
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
| **appInstanceArn** | **String**| The ARN of the streaming configuration. | |
| **putMessagingStreamingConfigurationsRequest** | [**PutMessagingStreamingConfigurationsRequest**](PutMessagingStreamingConfigurationsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutMessagingStreamingConfigurationsResponse**](PutMessagingStreamingConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ConflictException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="redactChannelMessage"></a>
# **redactChannelMessage**
> RedactChannelMessageResponse redactChannelMessage(channelArn, messageId, xAmzChimeBearer, operation, redactChannelMessageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Redacts message content, but not metadata. The message exists in the back end, but the action returns null content, and the state shows as redacted.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel containing the messages that you want to redact.
    String messageId = "messageId_example"; // String | The ID of the message being redacted.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String operation = "redact"; // String | 
    RedactChannelMessageRequest redactChannelMessageRequest = new RedactChannelMessageRequest(); // RedactChannelMessageRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      RedactChannelMessageResponse result = apiInstance.redactChannelMessage(channelArn, messageId, xAmzChimeBearer, operation, redactChannelMessageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#redactChannelMessage");
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
| **channelArn** | **String**| The ARN of the channel containing the messages that you want to redact. | |
| **messageId** | **String**| The ID of the message being redacted. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **operation** | **String**|  | [enum: redact] |
| **redactChannelMessageRequest** | [**RedactChannelMessageRequest**](RedactChannelMessageRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**RedactChannelMessageResponse**](RedactChannelMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ConflictException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="searchChannels"></a>
# **searchChannels**
> SearchChannelsResponse searchChannels(operation, searchChannelsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer, maxResults, nextToken, maxResults2, nextToken2)



&lt;p&gt;Allows the &lt;code&gt;ChimeBearer&lt;/code&gt; to search channels by channel members. Users or bots can search across the channels that they belong to. Users in the &lt;code&gt;AppInstanceAdmin&lt;/code&gt; role can search across all channels.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String operation = "search"; // String | 
    SearchChannelsRequest searchChannelsRequest = new SearchChannelsRequest(); // SearchChannelsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user making the API call.
    Integer maxResults = 56; // Integer | The maximum number of channels that you want returned.
    String nextToken = "nextToken_example"; // String | The token returned from previous API requests until the number of channels is reached.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      SearchChannelsResponse result = apiInstance.searchChannels(operation, searchChannelsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#searchChannels");
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
| **operation** | **String**|  | [enum: search] |
| **searchChannelsRequest** | [**SearchChannelsRequest**](SearchChannelsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user making the API call. | [optional] |
| **maxResults** | **Integer**| The maximum number of channels that you want returned. | [optional] |
| **nextToken** | **String**| The token returned from previous API requests until the number of channels is reached. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**SearchChannelsResponse**](SearchChannelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="sendChannelMessage"></a>
# **sendChannelMessage**
> SendChannelMessageResponse sendChannelMessage(channelArn, xAmzChimeBearer, sendChannelMessageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Sends a message to a particular channel that the member is a part of.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;p&gt;Also, &lt;code&gt;STANDARD&lt;/code&gt; messages can be up to 4KB in size and contain metadata. Metadata is arbitrary, and you can use it in a variety of ways, such as containing a link to an attachment.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CONTROL&lt;/code&gt; messages are limited to 30 bytes and do not contain metadata.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    SendChannelMessageRequest sendChannelMessageRequest = new SendChannelMessageRequest(); // SendChannelMessageRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      SendChannelMessageResponse result = apiInstance.sendChannelMessage(channelArn, xAmzChimeBearer, sendChannelMessageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sendChannelMessage");
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
| **channelArn** | **String**| The ARN of the channel. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **sendChannelMessageRequest** | [**SendChannelMessageRequest**](SendChannelMessageRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**SendChannelMessageResponse**](SendChannelMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ConflictException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="tagResource"></a>
# **tagResource**
> tagResource(operation, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Applies the specified tags to the specified Amazon Chime SDK messaging resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String operation = "tag-resource"; // String | 
    TagResourceRequest tagResourceRequest = new TagResourceRequest(); // TagResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.tagResource(operation, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagResource");
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
| **operation** | **String**|  | [enum: tag-resource] |
| **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ResourceLimitExceededException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="untagResource"></a>
# **untagResource**
> untagResource(operation, untagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Removes the specified tags from the specified Amazon Chime SDK messaging resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String operation = "untag-resource"; // String | 
    UntagResourceRequest untagResourceRequest = new UntagResourceRequest(); // UntagResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.untagResource(operation, untagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#untagResource");
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
| **operation** | **String**|  | [enum: untag-resource] |
| **untagResourceRequest** | [**UntagResourceRequest**](UntagResourceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="updateChannel"></a>
# **updateChannel**
> UpdateChannelResponse updateChannel(channelArn, xAmzChimeBearer, updateChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Update a channel&#39;s attributes.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Restriction&lt;/b&gt;: You can&#39;t change a channel&#39;s privacy. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    UpdateChannelRequest updateChannelRequest = new UpdateChannelRequest(); // UpdateChannelRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateChannelResponse result = apiInstance.updateChannel(channelArn, xAmzChimeBearer, updateChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateChannel");
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
| **channelArn** | **String**| The ARN of the channel. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **updateChannelRequest** | [**UpdateChannelRequest**](UpdateChannelRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateChannelResponse**](UpdateChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ConflictException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="updateChannelFlow"></a>
# **updateChannelFlow**
> UpdateChannelFlowResponse updateChannelFlow(channelFlowArn, updateChannelFlowRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates channel flow attributes. This is a developer API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelFlowArn = "channelFlowArn_example"; // String | The ARN of the channel flow.
    UpdateChannelFlowRequest updateChannelFlowRequest = new UpdateChannelFlowRequest(); // UpdateChannelFlowRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateChannelFlowResponse result = apiInstance.updateChannelFlow(channelFlowArn, updateChannelFlowRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateChannelFlow");
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
| **channelFlowArn** | **String**| The ARN of the channel flow. | |
| **updateChannelFlowRequest** | [**UpdateChannelFlowRequest**](UpdateChannelFlowRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateChannelFlowResponse**](UpdateChannelFlowResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ConflictException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="updateChannelMessage"></a>
# **updateChannelMessage**
> UpdateChannelMessageResponse updateChannelMessage(channelArn, messageId, xAmzChimeBearer, updateChannelMessageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates the content of a message.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String messageId = "messageId_example"; // String | The ID string of the message being updated.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    UpdateChannelMessageRequest updateChannelMessageRequest = new UpdateChannelMessageRequest(); // UpdateChannelMessageRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateChannelMessageResponse result = apiInstance.updateChannelMessage(channelArn, messageId, xAmzChimeBearer, updateChannelMessageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateChannelMessage");
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
| **channelArn** | **String**| The ARN of the channel. | |
| **messageId** | **String**| The ID string of the message being updated. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **updateChannelMessageRequest** | [**UpdateChannelMessageRequest**](UpdateChannelMessageRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateChannelMessageResponse**](UpdateChannelMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ConflictException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="updateChannelReadMarker"></a>
# **updateChannelReadMarker**
> UpdateChannelReadMarkerResponse updateChannelReadMarker(channelArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;The details of the time when a user last read messages in a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://messaging-chime.us-east-1.amazonaws.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateChannelReadMarkerResponse result = apiInstance.updateChannelReadMarker(channelArn, xAmzChimeBearer, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateChannelReadMarker");
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
| **channelArn** | **String**| The ARN of the channel. | |
| **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateChannelReadMarkerResponse**](UpdateChannelReadMarkerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ConflictException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

