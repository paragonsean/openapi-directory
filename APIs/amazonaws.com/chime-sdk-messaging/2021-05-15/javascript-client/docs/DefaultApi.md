# AmazonChimeSdkMessaging.DefaultApi

All URIs are relative to *http://messaging-chime.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateChannelFlow**](DefaultApi.md#associateChannelFlow) | **PUT** /channels/{channelArn}/channel-flow#x-amz-chime-bearer | 
[**batchCreateChannelMembership**](DefaultApi.md#batchCreateChannelMembership) | **POST** /channels/{channelArn}/memberships#operation&#x3D;batch-create&amp;x-amz-chime-bearer | 
[**channelFlowCallback**](DefaultApi.md#channelFlowCallback) | **POST** /channels/{channelArn}#operation&#x3D;channel-flow-callback | 
[**createChannel**](DefaultApi.md#createChannel) | **POST** /channels#x-amz-chime-bearer | 
[**createChannelBan**](DefaultApi.md#createChannelBan) | **POST** /channels/{channelArn}/bans#x-amz-chime-bearer | 
[**createChannelFlow**](DefaultApi.md#createChannelFlow) | **POST** /channel-flows | 
[**createChannelMembership**](DefaultApi.md#createChannelMembership) | **POST** /channels/{channelArn}/memberships#x-amz-chime-bearer | 
[**createChannelModerator**](DefaultApi.md#createChannelModerator) | **POST** /channels/{channelArn}/moderators#x-amz-chime-bearer | 
[**deleteChannel**](DefaultApi.md#deleteChannel) | **DELETE** /channels/{channelArn}#x-amz-chime-bearer | 
[**deleteChannelBan**](DefaultApi.md#deleteChannelBan) | **DELETE** /channels/{channelArn}/bans/{memberArn}#x-amz-chime-bearer | 
[**deleteChannelFlow**](DefaultApi.md#deleteChannelFlow) | **DELETE** /channel-flows/{channelFlowArn} | 
[**deleteChannelMembership**](DefaultApi.md#deleteChannelMembership) | **DELETE** /channels/{channelArn}/memberships/{memberArn}#x-amz-chime-bearer | 
[**deleteChannelMessage**](DefaultApi.md#deleteChannelMessage) | **DELETE** /channels/{channelArn}/messages/{messageId}#x-amz-chime-bearer | 
[**deleteChannelModerator**](DefaultApi.md#deleteChannelModerator) | **DELETE** /channels/{channelArn}/moderators/{channelModeratorArn}#x-amz-chime-bearer | 
[**deleteMessagingStreamingConfigurations**](DefaultApi.md#deleteMessagingStreamingConfigurations) | **DELETE** /app-instances/{appInstanceArn}/streaming-configurations | 
[**describeChannel**](DefaultApi.md#describeChannel) | **GET** /channels/{channelArn}#x-amz-chime-bearer | 
[**describeChannelBan**](DefaultApi.md#describeChannelBan) | **GET** /channels/{channelArn}/bans/{memberArn}#x-amz-chime-bearer | 
[**describeChannelFlow**](DefaultApi.md#describeChannelFlow) | **GET** /channel-flows/{channelFlowArn} | 
[**describeChannelMembership**](DefaultApi.md#describeChannelMembership) | **GET** /channels/{channelArn}/memberships/{memberArn}#x-amz-chime-bearer | 
[**describeChannelMembershipForAppInstanceUser**](DefaultApi.md#describeChannelMembershipForAppInstanceUser) | **GET** /channels/{channelArn}#scope&#x3D;app-instance-user-membership&amp;app-instance-user-arn&amp;x-amz-chime-bearer | 
[**describeChannelModeratedByAppInstanceUser**](DefaultApi.md#describeChannelModeratedByAppInstanceUser) | **GET** /channels/{channelArn}#scope&#x3D;app-instance-user-moderated-channel&amp;app-instance-user-arn&amp;x-amz-chime-bearer | 
[**describeChannelModerator**](DefaultApi.md#describeChannelModerator) | **GET** /channels/{channelArn}/moderators/{channelModeratorArn}#x-amz-chime-bearer | 
[**disassociateChannelFlow**](DefaultApi.md#disassociateChannelFlow) | **DELETE** /channels/{channelArn}/channel-flow/{channelFlowArn}#x-amz-chime-bearer | 
[**getChannelMembershipPreferences**](DefaultApi.md#getChannelMembershipPreferences) | **GET** /channels/{channelArn}/memberships/{memberArn}/preferences#x-amz-chime-bearer | 
[**getChannelMessage**](DefaultApi.md#getChannelMessage) | **GET** /channels/{channelArn}/messages/{messageId}#x-amz-chime-bearer | 
[**getChannelMessageStatus**](DefaultApi.md#getChannelMessageStatus) | **GET** /channels/{channelArn}/messages/{messageId}#scope&#x3D;message-status&amp;x-amz-chime-bearer | 
[**getMessagingSessionEndpoint**](DefaultApi.md#getMessagingSessionEndpoint) | **GET** /endpoints/messaging-session | 
[**getMessagingStreamingConfigurations**](DefaultApi.md#getMessagingStreamingConfigurations) | **GET** /app-instances/{appInstanceArn}/streaming-configurations | 
[**listChannelBans**](DefaultApi.md#listChannelBans) | **GET** /channels/{channelArn}/bans#x-amz-chime-bearer | 
[**listChannelFlows**](DefaultApi.md#listChannelFlows) | **GET** /channel-flows#app-instance-arn | 
[**listChannelMemberships**](DefaultApi.md#listChannelMemberships) | **GET** /channels/{channelArn}/memberships#x-amz-chime-bearer | 
[**listChannelMembershipsForAppInstanceUser**](DefaultApi.md#listChannelMembershipsForAppInstanceUser) | **GET** /channels#scope&#x3D;app-instance-user-memberships&amp;x-amz-chime-bearer | 
[**listChannelMessages**](DefaultApi.md#listChannelMessages) | **GET** /channels/{channelArn}/messages#x-amz-chime-bearer | 
[**listChannelModerators**](DefaultApi.md#listChannelModerators) | **GET** /channels/{channelArn}/moderators#x-amz-chime-bearer | 
[**listChannels**](DefaultApi.md#listChannels) | **GET** /channels#app-instance-arn&amp;x-amz-chime-bearer | 
[**listChannelsAssociatedWithChannelFlow**](DefaultApi.md#listChannelsAssociatedWithChannelFlow) | **GET** /channels#scope&#x3D;channel-flow-associations&amp;channel-flow-arn | 
[**listChannelsModeratedByAppInstanceUser**](DefaultApi.md#listChannelsModeratedByAppInstanceUser) | **GET** /channels#scope&#x3D;app-instance-user-moderated-channels&amp;x-amz-chime-bearer | 
[**listSubChannels**](DefaultApi.md#listSubChannels) | **GET** /channels/{channelArn}/subchannels#x-amz-chime-bearer | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags#arn | 
[**putChannelExpirationSettings**](DefaultApi.md#putChannelExpirationSettings) | **PUT** /channels/{channelArn}/expiration-settings | 
[**putChannelMembershipPreferences**](DefaultApi.md#putChannelMembershipPreferences) | **PUT** /channels/{channelArn}/memberships/{memberArn}/preferences#x-amz-chime-bearer | 
[**putMessagingStreamingConfigurations**](DefaultApi.md#putMessagingStreamingConfigurations) | **PUT** /app-instances/{appInstanceArn}/streaming-configurations | 
[**redactChannelMessage**](DefaultApi.md#redactChannelMessage) | **POST** /channels/{channelArn}/messages/{messageId}#operation&#x3D;redact&amp;x-amz-chime-bearer | 
[**searchChannels**](DefaultApi.md#searchChannels) | **POST** /channels#operation&#x3D;search | 
[**sendChannelMessage**](DefaultApi.md#sendChannelMessage) | **POST** /channels/{channelArn}/messages#x-amz-chime-bearer | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags#operation&#x3D;tag-resource | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /tags#operation&#x3D;untag-resource | 
[**updateChannel**](DefaultApi.md#updateChannel) | **PUT** /channels/{channelArn}#x-amz-chime-bearer | 
[**updateChannelFlow**](DefaultApi.md#updateChannelFlow) | **PUT** /channel-flows/{channelFlowArn} | 
[**updateChannelMessage**](DefaultApi.md#updateChannelMessage) | **PUT** /channels/{channelArn}/messages/{messageId}#x-amz-chime-bearer | 
[**updateChannelReadMarker**](DefaultApi.md#updateChannelReadMarker) | **PUT** /channels/{channelArn}/readMarker#x-amz-chime-bearer | 



## associateChannelFlow

> associateChannelFlow(channelArn, xAmzChimeBearer, associateChannelFlowRequest, opts)



&lt;p&gt;Associates a channel flow with a channel. Once associated, all messages to that channel go through channel flow processors. To stop processing, use the &lt;code&gt;DisassociateChannelFlow&lt;/code&gt; API.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only administrators or channel moderators can associate a channel flow. The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user making the API call.
let associateChannelFlowRequest = new AmazonChimeSdkMessaging.AssociateChannelFlowRequest(); // AssociateChannelFlowRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateChannelFlow(channelArn, xAmzChimeBearer, associateChannelFlowRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel. | 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user making the API call. | 
 **associateChannelFlowRequest** | [**AssociateChannelFlowRequest**](AssociateChannelFlowRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchCreateChannelMembership

> BatchCreateChannelMembershipResponse batchCreateChannelMembership(channelArn, xAmzChimeBearer, operation, batchCreateChannelMembershipRequest, opts)



Adds a specified number of users and bots to a channel. 

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel to which you're adding users or bots.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let operation = "operation_example"; // String | 
let batchCreateChannelMembershipRequest = new AmazonChimeSdkMessaging.BatchCreateChannelMembershipRequest(); // BatchCreateChannelMembershipRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchCreateChannelMembership(channelArn, xAmzChimeBearer, operation, batchCreateChannelMembershipRequest, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel to which you&#39;re adding users or bots. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **operation** | **String**|  | 
 **batchCreateChannelMembershipRequest** | [**BatchCreateChannelMembershipRequest**](BatchCreateChannelMembershipRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchCreateChannelMembershipResponse**](BatchCreateChannelMembershipResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## channelFlowCallback

> ChannelFlowCallbackResponse channelFlowCallback(channelArn, operation, channelFlowCallbackRequest, opts)



&lt;p&gt;Calls back Amazon Chime SDK messaging with a processing response message. This should be invoked from the processor Lambda. This is a developer API.&lt;/p&gt; &lt;p&gt;You can return one of the following processing responses:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Update message content or metadata&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Deny a message&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Make no changes to the message&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let operation = "operation_example"; // String | 
let channelFlowCallbackRequest = new AmazonChimeSdkMessaging.ChannelFlowCallbackRequest(); // ChannelFlowCallbackRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.channelFlowCallback(channelArn, operation, channelFlowCallbackRequest, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel. | 
 **operation** | **String**|  | 
 **channelFlowCallbackRequest** | [**ChannelFlowCallbackRequest**](ChannelFlowCallbackRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ChannelFlowCallbackResponse**](ChannelFlowCallbackResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createChannel

> CreateChannelResponse createChannel(xAmzChimeBearer, createChannelRequest, opts)



&lt;p&gt;Creates a channel to which you can add users and send messages.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Restriction&lt;/b&gt;: You can&#39;t change a channel&#39;s privacy.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let createChannelRequest = new AmazonChimeSdkMessaging.CreateChannelRequest(); // CreateChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createChannel(xAmzChimeBearer, createChannelRequest, opts, (error, data, response) => {
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
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **createChannelRequest** | [**CreateChannelRequest**](CreateChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateChannelResponse**](CreateChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createChannelBan

> CreateChannelBanResponse createChannelBan(channelArn, xAmzChimeBearer, createChannelBanRequest, opts)



&lt;p&gt;Permanently bans a member from a channel. Moderators can&#39;t add banned members to a channel. To undo a ban, you first have to &lt;code&gt;DeleteChannelBan&lt;/code&gt;, and then &lt;code&gt;CreateChannelMembership&lt;/code&gt;. Bans are cleaned up when you delete users or channels.&lt;/p&gt; &lt;p&gt;If you ban a user who is already part of a channel, that user is automatically kicked from the channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the ban request.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let createChannelBanRequest = new AmazonChimeSdkMessaging.CreateChannelBanRequest(); // CreateChannelBanRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createChannelBan(channelArn, xAmzChimeBearer, createChannelBanRequest, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the ban request. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **createChannelBanRequest** | [**CreateChannelBanRequest**](CreateChannelBanRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateChannelBanResponse**](CreateChannelBanResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createChannelFlow

> CreateChannelFlowResponse createChannelFlow(createChannelFlowRequest, opts)



&lt;p&gt;Creates a channel flow, a container for processors. Processors are AWS Lambda functions that perform actions on chat messages, such as stripping out profanity. You can associate channel flows with channels, and the processors in the channel flow then take action on all messages sent to that channel. This is a developer API.&lt;/p&gt; &lt;p&gt;Channel flows process the following items:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;New and updated messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Persistent and non-persistent messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The Standard message type&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;note&gt; &lt;p&gt;Channel flows don&#39;t process Control or System messages. For more information about the message types provided by Chime SDK messaging, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/dg/using-the-messaging-sdk.html#msg-types\&quot;&gt;Message types&lt;/a&gt; in the &lt;i&gt;Amazon Chime developer guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let createChannelFlowRequest = new AmazonChimeSdkMessaging.CreateChannelFlowRequest(); // CreateChannelFlowRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createChannelFlow(createChannelFlowRequest, opts, (error, data, response) => {
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
 **createChannelFlowRequest** | [**CreateChannelFlowRequest**](CreateChannelFlowRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateChannelFlowResponse**](CreateChannelFlowResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createChannelMembership

> CreateChannelMembershipResponse createChannelMembership(channelArn, xAmzChimeBearer, createChannelMembershipRequest, opts)



&lt;p&gt;Adds a member to a channel. The &lt;code&gt;InvitedBy&lt;/code&gt; field in &lt;code&gt;ChannelMembership&lt;/code&gt; is derived from the request header. A channel member can:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;List messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Send messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Receive messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Edit their own messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Leave the channel&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Privacy settings impact this action as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Public Channels: You do not need to be a member to list messages, but you must be a member to send messages.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Private Channels: You must be a member to list or send messages.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel to which you're adding users.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let createChannelMembershipRequest = new AmazonChimeSdkMessaging.CreateChannelMembershipRequest(); // CreateChannelMembershipRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createChannelMembership(channelArn, xAmzChimeBearer, createChannelMembershipRequest, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel to which you&#39;re adding users. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **createChannelMembershipRequest** | [**CreateChannelMembershipRequest**](CreateChannelMembershipRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateChannelMembershipResponse**](CreateChannelMembershipResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createChannelModerator

> CreateChannelModeratorResponse createChannelModerator(channelArn, xAmzChimeBearer, createChannelModeratorRequest, opts)



&lt;p&gt;Creates a new &lt;code&gt;ChannelModerator&lt;/code&gt;. A channel moderator can:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Add and remove other members of the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Add and remove other moderators of the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Add and remove user bans for the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Redact messages in the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;List messages in the channel.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt;of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let createChannelModeratorRequest = new AmazonChimeSdkMessaging.CreateChannelModeratorRequest(); // CreateChannelModeratorRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createChannelModerator(channelArn, xAmzChimeBearer, createChannelModeratorRequest, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **createChannelModeratorRequest** | [**CreateChannelModeratorRequest**](CreateChannelModeratorRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateChannelModeratorResponse**](CreateChannelModeratorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteChannel

> deleteChannel(channelArn, xAmzChimeBearer, opts)



&lt;p&gt;Immediately makes a channel and its memberships inaccessible and marks them for deletion. This is an irreversible process.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel being deleted.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteChannel(channelArn, xAmzChimeBearer, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel being deleted. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteChannelBan

> deleteChannelBan(channelArn, memberArn, xAmzChimeBearer, opts)



&lt;p&gt;Removes a member from a channel&#39;s ban list.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel from which the <code>AppInstanceUser</code> was banned.
let memberArn = "memberArn_example"; // String | The ARN of the <code>AppInstanceUser</code> that you want to reinstate.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteChannelBan(channelArn, memberArn, xAmzChimeBearer, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel from which the &lt;code&gt;AppInstanceUser&lt;/code&gt; was banned. | 
 **memberArn** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; that you want to reinstate. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteChannelFlow

> deleteChannelFlow(channelFlowArn, opts)



&lt;p&gt;Deletes a channel flow, an irreversible process. This is a developer API.&lt;/p&gt; &lt;note&gt; &lt;p&gt; This API works only when the channel flow is not associated with any channel. To get a list of all channels that a channel flow is associated with, use the &lt;code&gt;ListChannelsAssociatedWithChannelFlow&lt;/code&gt; API. Use the &lt;code&gt;DisassociateChannelFlow&lt;/code&gt; API to disassociate a channel flow from all channels. &lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelFlowArn = "channelFlowArn_example"; // String | The ARN of the channel flow.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteChannelFlow(channelFlowArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelFlowArn** | **String**| The ARN of the channel flow. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteChannelMembership

> deleteChannelMembership(channelArn, memberArn, xAmzChimeBearer, opts)



&lt;p&gt;Removes a member from a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel from which you want to remove the user.
let memberArn = "memberArn_example"; // String | The <code>AppInstanceUserArn</code> of the member that you're removing from the channel.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'subChannelId': "subChannelId_example" // String | <p>The ID of the SubChannel in the request.</p> <note> <p>Only for use by moderators.</p> </note>
};
apiInstance.deleteChannelMembership(channelArn, memberArn, xAmzChimeBearer, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel from which you want to remove the user. | 
 **memberArn** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the member that you&#39;re removing from the channel. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **subChannelId** | **String**| &lt;p&gt;The ID of the SubChannel in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only for use by moderators.&lt;/p&gt; &lt;/note&gt; | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteChannelMessage

> deleteChannelMessage(channelArn, messageId, xAmzChimeBearer, opts)



&lt;p&gt;Deletes a channel message. Only admins can perform this action. Deletion makes messages inaccessible immediately. A background process deletes any revisions created by &lt;code&gt;UpdateChannelMessage&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let messageId = "messageId_example"; // String | The ID of the message being deleted.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'subChannelId': "subChannelId_example" // String | <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when deleting messages in a SubChannel that the user belongs to.</p> </note>
};
apiInstance.deleteChannelMessage(channelArn, messageId, xAmzChimeBearer, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel. | 
 **messageId** | **String**| The ID of the message being deleted. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **subChannelId** | **String**| &lt;p&gt;The ID of the SubChannel in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only required when deleting messages in a SubChannel that the user belongs to.&lt;/p&gt; &lt;/note&gt; | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteChannelModerator

> deleteChannelModerator(channelArn, channelModeratorArn, xAmzChimeBearer, opts)



&lt;p&gt;Deletes a channel moderator.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let channelModeratorArn = "channelModeratorArn_example"; // String | The <code>AppInstanceUserArn</code> of the moderator being deleted.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteChannelModerator(channelArn, channelModeratorArn, xAmzChimeBearer, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel. | 
 **channelModeratorArn** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the moderator being deleted. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteMessagingStreamingConfigurations

> deleteMessagingStreamingConfigurations(appInstanceArn, opts)



Deletes the streaming configurations for an &lt;code&gt;AppInstance&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/streaming-export.html\&quot;&gt;Streaming messaging data&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let appInstanceArn = "appInstanceArn_example"; // String | The ARN of the streaming configurations being deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMessagingStreamingConfigurations(appInstanceArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appInstanceArn** | **String**| The ARN of the streaming configurations being deleted. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeChannel

> DescribeChannelResponse describeChannel(channelArn, xAmzChimeBearer, opts)



&lt;p&gt;Returns the full details of a channel in an Amazon Chime &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeChannel(channelArn, xAmzChimeBearer, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeChannelResponse**](DescribeChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeChannelBan

> DescribeChannelBanResponse describeChannelBan(channelArn, memberArn, xAmzChimeBearer, opts)



&lt;p&gt;Returns the full details of a channel ban.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel from which the user is banned.
let memberArn = "memberArn_example"; // String | The <code>AppInstanceUserArn</code> of the member being banned.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeChannelBan(channelArn, memberArn, xAmzChimeBearer, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel from which the user is banned. | 
 **memberArn** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the member being banned. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeChannelBanResponse**](DescribeChannelBanResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeChannelFlow

> DescribeChannelFlowResponse describeChannelFlow(channelFlowArn, opts)



Returns the full details of a channel flow in an Amazon Chime &lt;code&gt;AppInstance&lt;/code&gt;. This is a developer API.

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelFlowArn = "channelFlowArn_example"; // String | The ARN of the channel flow.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeChannelFlow(channelFlowArn, opts, (error, data, response) => {
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
 **channelFlowArn** | **String**| The ARN of the channel flow. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeChannelFlowResponse**](DescribeChannelFlowResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeChannelMembership

> DescribeChannelMembershipResponse describeChannelMembership(channelArn, memberArn, xAmzChimeBearer, opts)



&lt;p&gt;Returns the full details of a user&#39;s channel membership.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let memberArn = "memberArn_example"; // String | The <code>AppInstanceUserArn</code> of the member.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'subChannelId': "subChannelId_example" // String | <p>The ID of the SubChannel in the request. The response contains an <code>ElasticChannelConfiguration</code> object.</p> <note> <p>Only required to get a user’s SubChannel membership details.</p> </note>
};
apiInstance.describeChannelMembership(channelArn, memberArn, xAmzChimeBearer, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel. | 
 **memberArn** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the member. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **subChannelId** | **String**| &lt;p&gt;The ID of the SubChannel in the request. The response contains an &lt;code&gt;ElasticChannelConfiguration&lt;/code&gt; object.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only required to get a user’s SubChannel membership details.&lt;/p&gt; &lt;/note&gt; | [optional] 

### Return type

[**DescribeChannelMembershipResponse**](DescribeChannelMembershipResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeChannelMembershipForAppInstanceUser

> DescribeChannelMembershipForAppInstanceUserResponse describeChannelMembershipForAppInstanceUser(channelArn, appInstanceUserArn, xAmzChimeBearer, scope, opts)



&lt;p&gt; Returns the details of a channel based on the membership of the specified &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel to which the user belongs.
let appInstanceUserArn = "appInstanceUserArn_example"; // String | The ARN of the user or bot in a channel.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let scope = "scope_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeChannelMembershipForAppInstanceUser(channelArn, appInstanceUserArn, xAmzChimeBearer, scope, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel to which the user belongs. | 
 **appInstanceUserArn** | **String**| The ARN of the user or bot in a channel. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **scope** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeChannelMembershipForAppInstanceUserResponse**](DescribeChannelMembershipForAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeChannelModeratedByAppInstanceUser

> DescribeChannelModeratedByAppInstanceUserResponse describeChannelModeratedByAppInstanceUser(channelArn, appInstanceUserArn, xAmzChimeBearer, scope, opts)



&lt;p&gt;Returns the full details of a channel moderated by the specified &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the moderated channel.
let appInstanceUserArn = "appInstanceUserArn_example"; // String | The ARN of the user or bot in the moderated channel.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let scope = "scope_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeChannelModeratedByAppInstanceUser(channelArn, appInstanceUserArn, xAmzChimeBearer, scope, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the moderated channel. | 
 **appInstanceUserArn** | **String**| The ARN of the user or bot in the moderated channel. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **scope** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeChannelModeratedByAppInstanceUserResponse**](DescribeChannelModeratedByAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeChannelModerator

> DescribeChannelModeratorResponse describeChannelModerator(channelArn, channelModeratorArn, xAmzChimeBearer, opts)



&lt;p&gt;Returns the full details of a single ChannelModerator.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let channelModeratorArn = "channelModeratorArn_example"; // String | The <code>AppInstanceUserArn</code> of the channel moderator.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeChannelModerator(channelArn, channelModeratorArn, xAmzChimeBearer, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel. | 
 **channelModeratorArn** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the channel moderator. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeChannelModeratorResponse**](DescribeChannelModeratorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociateChannelFlow

> disassociateChannelFlow(channelArn, channelFlowArn, xAmzChimeBearer, opts)



&lt;p&gt;Disassociates a channel flow from all its channels. Once disassociated, all messages to that channel stop going through the channel flow processor.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only administrators or channel moderators can disassociate a channel flow.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let channelFlowArn = "channelFlowArn_example"; // String | The ARN of the channel flow.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user making the API call.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateChannelFlow(channelArn, channelFlowArn, xAmzChimeBearer, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel. | 
 **channelFlowArn** | **String**| The ARN of the channel flow. | 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user making the API call. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelMembershipPreferences

> GetChannelMembershipPreferencesResponse getChannelMembershipPreferences(channelArn, memberArn, xAmzChimeBearer, opts)



&lt;p&gt;Gets the membership preferences of an &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; for the specified channel. A user or a bot must be a member of the channel and own the membership in order to retrieve membership preferences. Users or bots in the &lt;code&gt;AppInstanceAdmin&lt;/code&gt; and channel moderator roles can&#39;t retrieve preferences for other users or bots. Banned users or bots can&#39;t retrieve membership preferences for the channel from which they are banned.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let memberArn = "memberArn_example"; // String | The <code>AppInstanceUserArn</code> of the member retrieving the preferences.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getChannelMembershipPreferences(channelArn, memberArn, xAmzChimeBearer, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel. | 
 **memberArn** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the member retrieving the preferences. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetChannelMembershipPreferencesResponse**](GetChannelMembershipPreferencesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelMessage

> GetChannelMessageResponse getChannelMessage(channelArn, messageId, xAmzChimeBearer, opts)



&lt;p&gt;Gets the full details of a channel message.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let messageId = "messageId_example"; // String | The ID of the message.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'subChannelId': "subChannelId_example" // String | <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when getting messages in a SubChannel that the user belongs to.</p> </note>
};
apiInstance.getChannelMessage(channelArn, messageId, xAmzChimeBearer, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel. | 
 **messageId** | **String**| The ID of the message. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **subChannelId** | **String**| &lt;p&gt;The ID of the SubChannel in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only required when getting messages in a SubChannel that the user belongs to.&lt;/p&gt; &lt;/note&gt; | [optional] 

### Return type

[**GetChannelMessageResponse**](GetChannelMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelMessageStatus

> GetChannelMessageStatusResponse getChannelMessageStatus(channelArn, messageId, xAmzChimeBearer, scope, opts)



&lt;p&gt;Gets message status for a specified &lt;code&gt;messageId&lt;/code&gt;. Use this API to determine the intermediate status of messages going through channel flow processing. The API provides an alternative to retrieving message status if the event was not received because a client wasn&#39;t connected to a websocket. &lt;/p&gt; &lt;p&gt;Messages can have any one of these statuses.&lt;/p&gt; &lt;dl&gt; &lt;dt&gt;SENT&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Message processed successfully&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;PENDING&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Ongoing processing&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;FAILED&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Processing failed&lt;/p&gt; &lt;/dd&gt; &lt;dt&gt;DENIED&lt;/dt&gt; &lt;dd&gt; &lt;p&gt;Message denied by the processor&lt;/p&gt; &lt;/dd&gt; &lt;/dl&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;This API does not return statuses for denied messages, because we don&#39;t store them once the processor denies them. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Only the message sender can invoke this API.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel
let messageId = "messageId_example"; // String | The ID of the message.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user making the API call.
let scope = "scope_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'subChannelId': "subChannelId_example" // String | <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when getting message status in a SubChannel that the user belongs to.</p> </note>
};
apiInstance.getChannelMessageStatus(channelArn, messageId, xAmzChimeBearer, scope, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel | 
 **messageId** | **String**| The ID of the message. | 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user making the API call. | 
 **scope** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **subChannelId** | **String**| &lt;p&gt;The ID of the SubChannel in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only required when getting message status in a SubChannel that the user belongs to.&lt;/p&gt; &lt;/note&gt; | [optional] 

### Return type

[**GetChannelMessageStatusResponse**](GetChannelMessageStatusResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMessagingSessionEndpoint

> GetMessagingSessionEndpointResponse getMessagingSessionEndpoint(opts)



The details of the endpoint for the messaging session.

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMessagingSessionEndpoint(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMessagingSessionEndpointResponse**](GetMessagingSessionEndpointResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMessagingStreamingConfigurations

> GetMessagingStreamingConfigurationsResponse getMessagingStreamingConfigurations(appInstanceArn, opts)



Retrieves the data streaming configuration for an &lt;code&gt;AppInstance&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/streaming-export.html\&quot;&gt;Streaming messaging data&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let appInstanceArn = "appInstanceArn_example"; // String | The ARN of the streaming configurations.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMessagingStreamingConfigurations(appInstanceArn, opts, (error, data, response) => {
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
 **appInstanceArn** | **String**| The ARN of the streaming configurations. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMessagingStreamingConfigurationsResponse**](GetMessagingStreamingConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannelBans

> ListChannelBansResponse listChannelBans(channelArn, xAmzChimeBearer, opts)



&lt;p&gt;Lists all the users and bots banned from a particular channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of bans that you want returned.
  'nextToken': "nextToken_example", // String | The token passed by previous API calls until all requested bans are returned.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChannelBans(channelArn, xAmzChimeBearer, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of bans that you want returned. | [optional] 
 **nextToken** | **String**| The token passed by previous API calls until all requested bans are returned. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChannelBansResponse**](ListChannelBansResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannelFlows

> ListChannelFlowsResponse listChannelFlows(appInstanceArn, opts)



Returns a paginated lists of all the channel flows created under a single Chime. This is a developer API.

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let appInstanceArn = "appInstanceArn_example"; // String | The ARN of the app instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of channel flows that you want to return.
  'nextToken': "nextToken_example", // String | The token passed by previous API calls until all requested channel flows are returned.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChannelFlows(appInstanceArn, opts, (error, data, response) => {
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
 **appInstanceArn** | **String**| The ARN of the app instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of channel flows that you want to return. | [optional] 
 **nextToken** | **String**| The token passed by previous API calls until all requested channel flows are returned. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChannelFlowsResponse**](ListChannelFlowsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannelMemberships

> ListChannelMembershipsResponse listChannelMemberships(channelArn, xAmzChimeBearer, opts)



&lt;p&gt;Lists all channel memberships in a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;If you want to list the channels to which a specific app instance user belongs, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/APIReference/API_messaging-chime_ListChannelMembershipsForAppInstanceUser.html\&quot;&gt;ListChannelMembershipsForAppInstanceUser&lt;/a&gt; API.&lt;/p&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The maximum number of channel memberships that you want returned.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'type': "type_example", // String | The membership type of a user, <code>DEFAULT</code> or <code>HIDDEN</code>. Default members are returned as part of <code>ListChannelMemberships</code> if no type is specified. Hidden members are only returned if the type filter in <code>ListChannelMemberships</code> equals <code>HIDDEN</code>.
  'maxResults': 56, // Number | The maximum number of channel memberships that you want returned.
  'nextToken': "nextToken_example", // String | The token passed by previous API calls until all requested channel memberships are returned.
  'subChannelId': "subChannelId_example", // String | <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when listing a user's memberships in a particular sub-channel of an elastic channel.</p> </note>
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChannelMemberships(channelArn, xAmzChimeBearer, opts, (error, data, response) => {
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
 **channelArn** | **String**| The maximum number of channel memberships that you want returned. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **type** | **String**| The membership type of a user, &lt;code&gt;DEFAULT&lt;/code&gt; or &lt;code&gt;HIDDEN&lt;/code&gt;. Default members are returned as part of &lt;code&gt;ListChannelMemberships&lt;/code&gt; if no type is specified. Hidden members are only returned if the type filter in &lt;code&gt;ListChannelMemberships&lt;/code&gt; equals &lt;code&gt;HIDDEN&lt;/code&gt;. | [optional] 
 **maxResults** | **Number**| The maximum number of channel memberships that you want returned. | [optional] 
 **nextToken** | **String**| The token passed by previous API calls until all requested channel memberships are returned. | [optional] 
 **subChannelId** | **String**| &lt;p&gt;The ID of the SubChannel in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only required when listing a user&#39;s memberships in a particular sub-channel of an elastic channel.&lt;/p&gt; &lt;/note&gt; | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChannelMembershipsResponse**](ListChannelMembershipsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannelMembershipsForAppInstanceUser

> ListChannelMembershipsForAppInstanceUserResponse listChannelMembershipsForAppInstanceUser(xAmzChimeBearer, scope, opts)



&lt;p&gt; Lists all channels that an &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; is a part of. Only an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; can call the API with a user ARN that is not their own. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let scope = "scope_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'appInstanceUserArn': "appInstanceUserArn_example", // String | The ARN of the user or bot.
  'maxResults': 56, // Number | The maximum number of users that you want returned.
  'nextToken': "nextToken_example", // String | The token returned from previous API requests until the number of channel memberships is reached.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChannelMembershipsForAppInstanceUser(xAmzChimeBearer, scope, opts, (error, data, response) => {
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
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **scope** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **appInstanceUserArn** | **String**| The ARN of the user or bot. | [optional] 
 **maxResults** | **Number**| The maximum number of users that you want returned. | [optional] 
 **nextToken** | **String**| The token returned from previous API requests until the number of channel memberships is reached. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChannelMembershipsForAppInstanceUserResponse**](ListChannelMembershipsForAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannelMessages

> ListChannelMessagesResponse listChannelMessages(channelArn, xAmzChimeBearer, opts)



&lt;p&gt;List all the messages in a channel. Returns a paginated list of &lt;code&gt;ChannelMessages&lt;/code&gt;. By default, sorted by creation timestamp in descending order.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Redacted messages appear in the results as empty, since they are only redacted, not deleted. Deleted messages do not appear in the results. This action always returns the latest version of an edited message.&lt;/p&gt; &lt;p&gt;Also, the &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'sortOrder': "sortOrder_example", // String | The order in which you want messages sorted. Default is Descending, based on time created.
  'notBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | The initial or starting time stamp for your requested messages.
  'notAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | The final or ending time stamp for your requested messages.
  'maxResults': 56, // Number | The maximum number of messages that you want returned.
  'nextToken': "nextToken_example", // String | The token passed by previous API calls until all requested messages are returned.
  'subChannelId': "subChannelId_example", // String | <p>The ID of the SubChannel in the request.</p> <note> <p>Only required when listing the messages in a SubChannel that the user belongs to.</p> </note>
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChannelMessages(channelArn, xAmzChimeBearer, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **sortOrder** | **String**| The order in which you want messages sorted. Default is Descending, based on time created. | [optional] 
 **notBefore** | **Date**| The initial or starting time stamp for your requested messages. | [optional] 
 **notAfter** | **Date**| The final or ending time stamp for your requested messages. | [optional] 
 **maxResults** | **Number**| The maximum number of messages that you want returned. | [optional] 
 **nextToken** | **String**| The token passed by previous API calls until all requested messages are returned. | [optional] 
 **subChannelId** | **String**| &lt;p&gt;The ID of the SubChannel in the request.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only required when listing the messages in a SubChannel that the user belongs to.&lt;/p&gt; &lt;/note&gt; | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChannelMessagesResponse**](ListChannelMessagesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannelModerators

> ListChannelModeratorsResponse listChannelModerators(channelArn, xAmzChimeBearer, opts)



&lt;p&gt;Lists all the moderators for a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of moderators that you want returned.
  'nextToken': "nextToken_example", // String | The token passed by previous API calls until all requested moderators are returned.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChannelModerators(channelArn, xAmzChimeBearer, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of moderators that you want returned. | [optional] 
 **nextToken** | **String**| The token passed by previous API calls until all requested moderators are returned. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChannelModeratorsResponse**](ListChannelModeratorsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannels

> ListChannelsResponse listChannels(appInstanceArn, xAmzChimeBearer, opts)



&lt;p&gt;Lists all Channels created under a single Chime App as a paginated list. You can specify filters to narrow results.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Functionality &amp;amp; restrictions&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use privacy &#x3D; &lt;code&gt;PUBLIC&lt;/code&gt; to retrieve all public channels in the account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Only an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; can set privacy &#x3D; &lt;code&gt;PRIVATE&lt;/code&gt; to list the private channels in an account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'privacy': "privacy_example", // String | The privacy setting. <code>PUBLIC</code> retrieves all the public channels. <code>PRIVATE</code> retrieves private channels. Only an <code>AppInstanceAdmin</code> can retrieve private channels. 
  'maxResults': 56, // Number | The maximum number of channels that you want to return.
  'nextToken': "nextToken_example", // String | The token passed by previous API calls until all requested channels are returned.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChannels(appInstanceArn, xAmzChimeBearer, opts, (error, data, response) => {
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
 **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **privacy** | **String**| The privacy setting. &lt;code&gt;PUBLIC&lt;/code&gt; retrieves all the public channels. &lt;code&gt;PRIVATE&lt;/code&gt; retrieves private channels. Only an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; can retrieve private channels.  | [optional] 
 **maxResults** | **Number**| The maximum number of channels that you want to return. | [optional] 
 **nextToken** | **String**| The token passed by previous API calls until all requested channels are returned. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChannelsResponse**](ListChannelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannelsAssociatedWithChannelFlow

> ListChannelsAssociatedWithChannelFlowResponse listChannelsAssociatedWithChannelFlow(channelFlowArn, scope, opts)



Lists all channels associated with a specified channel flow. You can associate a channel flow with multiple channels, but you can only associate a channel with one channel flow. This is a developer API.

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelFlowArn = "channelFlowArn_example"; // String | The ARN of the channel flow.
let scope = "scope_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of channels that you want to return.
  'nextToken': "nextToken_example", // String | The token passed by previous API calls until all requested channels are returned.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChannelsAssociatedWithChannelFlow(channelFlowArn, scope, opts, (error, data, response) => {
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
 **channelFlowArn** | **String**| The ARN of the channel flow. | 
 **scope** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of channels that you want to return. | [optional] 
 **nextToken** | **String**| The token passed by previous API calls until all requested channels are returned. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChannelsAssociatedWithChannelFlowResponse**](ListChannelsAssociatedWithChannelFlowResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannelsModeratedByAppInstanceUser

> ListChannelsModeratedByAppInstanceUserResponse listChannelsModeratedByAppInstanceUser(xAmzChimeBearer, scope, opts)



&lt;p&gt;A list of the channels moderated by an &lt;code&gt;AppInstanceUser&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let scope = "scope_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'appInstanceUserArn': "appInstanceUserArn_example", // String | The ARN of the user or bot in the moderated channel.
  'maxResults': 56, // Number | The maximum number of channels in the request.
  'nextToken': "nextToken_example", // String | The token returned from previous API requests until the number of channels moderated by the user is reached.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChannelsModeratedByAppInstanceUser(xAmzChimeBearer, scope, opts, (error, data, response) => {
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
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **scope** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **appInstanceUserArn** | **String**| The ARN of the user or bot in the moderated channel. | [optional] 
 **maxResults** | **Number**| The maximum number of channels in the request. | [optional] 
 **nextToken** | **String**| The token returned from previous API requests until the number of channels moderated by the user is reached. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChannelsModeratedByAppInstanceUserResponse**](ListChannelsModeratedByAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSubChannels

> ListSubChannelsResponse listSubChannels(channelArn, xAmzChimeBearer, opts)



Lists all the SubChannels in an elastic channel when given a channel ID. Available only to the app instance admins and channel moderators of elastic channels.

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of elastic channel.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user making the API call.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of sub-channels that you want to return.
  'nextToken': "nextToken_example", // String | The token passed by previous API calls until all requested sub-channels are returned.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listSubChannels(channelArn, xAmzChimeBearer, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of elastic channel. | 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user making the API call. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of sub-channels that you want to return. | [optional] 
 **nextToken** | **String**| The token passed by previous API calls until all requested sub-channels are returned. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListSubChannelsResponse**](ListSubChannelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(arn, opts)



Lists the tags applied to an Amazon Chime SDK messaging resource.

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let arn = "arn_example"; // String | The ARN of the resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(arn, opts, (error, data, response) => {
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
 **arn** | **String**| The ARN of the resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putChannelExpirationSettings

> PutChannelExpirationSettingsResponse putChannelExpirationSettings(channelArn, putChannelExpirationSettingsRequest, opts)



&lt;p&gt;Sets the number of days before the channel is automatically deleted.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A background process deletes expired channels within 6 hours of expiration. Actual deletion times may vary.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Expired channels that have not yet been deleted appear as active, and you can update their expiration settings. The system honors the new settings.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let putChannelExpirationSettingsRequest = new AmazonChimeSdkMessaging.PutChannelExpirationSettingsRequest(); // PutChannelExpirationSettingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
};
apiInstance.putChannelExpirationSettings(channelArn, putChannelExpirationSettingsRequest, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel. | 
 **putChannelExpirationSettingsRequest** | [**PutChannelExpirationSettingsRequest**](PutChannelExpirationSettingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | [optional] 

### Return type

[**PutChannelExpirationSettingsResponse**](PutChannelExpirationSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putChannelMembershipPreferences

> PutChannelMembershipPreferencesResponse putChannelMembershipPreferences(channelArn, memberArn, xAmzChimeBearer, putChannelMembershipPreferencesRequest, opts)



&lt;p&gt;Sets the membership preferences of an &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; for the specified channel. The user or bot must be a member of the channel. Only the user or bot who owns the membership can set preferences. Users or bots in the &lt;code&gt;AppInstanceAdmin&lt;/code&gt; and channel moderator roles can&#39;t set preferences for other users. Banned users or bots can&#39;t set membership preferences for the channel from which they are banned.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The x-amz-chime-bearer request header is mandatory. Use the ARN of an &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let memberArn = "memberArn_example"; // String | The ARN of the member setting the preferences.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let putChannelMembershipPreferencesRequest = new AmazonChimeSdkMessaging.PutChannelMembershipPreferencesRequest(); // PutChannelMembershipPreferencesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putChannelMembershipPreferences(channelArn, memberArn, xAmzChimeBearer, putChannelMembershipPreferencesRequest, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel. | 
 **memberArn** | **String**| The ARN of the member setting the preferences. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **putChannelMembershipPreferencesRequest** | [**PutChannelMembershipPreferencesRequest**](PutChannelMembershipPreferencesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutChannelMembershipPreferencesResponse**](PutChannelMembershipPreferencesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putMessagingStreamingConfigurations

> PutMessagingStreamingConfigurationsResponse putMessagingStreamingConfigurations(appInstanceArn, putMessagingStreamingConfigurationsRequest, opts)



Sets the data streaming configuration for an &lt;code&gt;AppInstance&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/streaming-export.html\&quot;&gt;Streaming messaging data&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let appInstanceArn = "appInstanceArn_example"; // String | The ARN of the streaming configuration.
let putMessagingStreamingConfigurationsRequest = new AmazonChimeSdkMessaging.PutMessagingStreamingConfigurationsRequest(); // PutMessagingStreamingConfigurationsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putMessagingStreamingConfigurations(appInstanceArn, putMessagingStreamingConfigurationsRequest, opts, (error, data, response) => {
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
 **appInstanceArn** | **String**| The ARN of the streaming configuration. | 
 **putMessagingStreamingConfigurationsRequest** | [**PutMessagingStreamingConfigurationsRequest**](PutMessagingStreamingConfigurationsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutMessagingStreamingConfigurationsResponse**](PutMessagingStreamingConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## redactChannelMessage

> RedactChannelMessageResponse redactChannelMessage(channelArn, messageId, xAmzChimeBearer, operation, redactChannelMessageRequest, opts)



&lt;p&gt;Redacts message content, but not metadata. The message exists in the back end, but the action returns null content, and the state shows as redacted.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel containing the messages that you want to redact.
let messageId = "messageId_example"; // String | The ID of the message being redacted.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let operation = "operation_example"; // String | 
let redactChannelMessageRequest = new AmazonChimeSdkMessaging.RedactChannelMessageRequest(); // RedactChannelMessageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.redactChannelMessage(channelArn, messageId, xAmzChimeBearer, operation, redactChannelMessageRequest, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel containing the messages that you want to redact. | 
 **messageId** | **String**| The ID of the message being redacted. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **operation** | **String**|  | 
 **redactChannelMessageRequest** | [**RedactChannelMessageRequest**](RedactChannelMessageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RedactChannelMessageResponse**](RedactChannelMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchChannels

> SearchChannelsResponse searchChannels(operation, searchChannelsRequest, opts)



&lt;p&gt;Allows the &lt;code&gt;ChimeBearer&lt;/code&gt; to search channels by channel members. Users or bots can search across the channels that they belong to. Users in the &lt;code&gt;AppInstanceAdmin&lt;/code&gt; role can search across all channels.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let operation = "operation_example"; // String | 
let searchChannelsRequest = new AmazonChimeSdkMessaging.SearchChannelsRequest(); // SearchChannelsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example", // String | The <code>AppInstanceUserArn</code> of the user making the API call.
  'maxResults': 56, // Number | The maximum number of channels that you want returned.
  'nextToken': "nextToken_example", // String | The token returned from previous API requests until the number of channels is reached.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.searchChannels(operation, searchChannelsRequest, opts, (error, data, response) => {
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
 **operation** | **String**|  | 
 **searchChannelsRequest** | [**SearchChannelsRequest**](SearchChannelsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user making the API call. | [optional] 
 **maxResults** | **Number**| The maximum number of channels that you want returned. | [optional] 
 **nextToken** | **String**| The token returned from previous API requests until the number of channels is reached. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**SearchChannelsResponse**](SearchChannelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendChannelMessage

> SendChannelMessageResponse sendChannelMessage(channelArn, xAmzChimeBearer, sendChannelMessageRequest, opts)



&lt;p&gt;Sends a message to a particular channel that the member is a part of.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;p&gt;Also, &lt;code&gt;STANDARD&lt;/code&gt; messages can be up to 4KB in size and contain metadata. Metadata is arbitrary, and you can use it in a variety of ways, such as containing a link to an attachment.&lt;/p&gt; &lt;p&gt; &lt;code&gt;CONTROL&lt;/code&gt; messages are limited to 30 bytes and do not contain metadata.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let sendChannelMessageRequest = new AmazonChimeSdkMessaging.SendChannelMessageRequest(); // SendChannelMessageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.sendChannelMessage(channelArn, xAmzChimeBearer, sendChannelMessageRequest, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **sendChannelMessageRequest** | [**SendChannelMessageRequest**](SendChannelMessageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SendChannelMessageResponse**](SendChannelMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> tagResource(operation, tagResourceRequest, opts)



Applies the specified tags to the specified Amazon Chime SDK messaging resource.

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let operation = "operation_example"; // String | 
let tagResourceRequest = new AmazonChimeSdkMessaging.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(operation, tagResourceRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation** | **String**|  | 
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> untagResource(operation, untagResourceRequest, opts)



Removes the specified tags from the specified Amazon Chime SDK messaging resource.

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let operation = "operation_example"; // String | 
let untagResourceRequest = new AmazonChimeSdkMessaging.UntagResourceRequest(); // UntagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(operation, untagResourceRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation** | **String**|  | 
 **untagResourceRequest** | [**UntagResourceRequest**](UntagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateChannel

> UpdateChannelResponse updateChannel(channelArn, xAmzChimeBearer, updateChannelRequest, opts)



&lt;p&gt;Update a channel&#39;s attributes.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Restriction&lt;/b&gt;: You can&#39;t change a channel&#39;s privacy. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let updateChannelRequest = new AmazonChimeSdkMessaging.UpdateChannelRequest(); // UpdateChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateChannel(channelArn, xAmzChimeBearer, updateChannelRequest, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **updateChannelRequest** | [**UpdateChannelRequest**](UpdateChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateChannelResponse**](UpdateChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateChannelFlow

> UpdateChannelFlowResponse updateChannelFlow(channelFlowArn, updateChannelFlowRequest, opts)



Updates channel flow attributes. This is a developer API.

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelFlowArn = "channelFlowArn_example"; // String | The ARN of the channel flow.
let updateChannelFlowRequest = new AmazonChimeSdkMessaging.UpdateChannelFlowRequest(); // UpdateChannelFlowRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateChannelFlow(channelFlowArn, updateChannelFlowRequest, opts, (error, data, response) => {
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
 **channelFlowArn** | **String**| The ARN of the channel flow. | 
 **updateChannelFlowRequest** | [**UpdateChannelFlowRequest**](UpdateChannelFlowRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateChannelFlowResponse**](UpdateChannelFlowResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateChannelMessage

> UpdateChannelMessageResponse updateChannelMessage(channelArn, messageId, xAmzChimeBearer, updateChannelMessageRequest, opts)



&lt;p&gt;Updates the content of a message.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let messageId = "messageId_example"; // String | The ID string of the message being updated.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let updateChannelMessageRequest = new AmazonChimeSdkMessaging.UpdateChannelMessageRequest(); // UpdateChannelMessageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateChannelMessage(channelArn, messageId, xAmzChimeBearer, updateChannelMessageRequest, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel. | 
 **messageId** | **String**| The ID string of the message being updated. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **updateChannelMessageRequest** | [**UpdateChannelMessageRequest**](UpdateChannelMessageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateChannelMessageResponse**](UpdateChannelMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateChannelReadMarker

> UpdateChannelReadMarkerResponse updateChannelReadMarker(channelArn, xAmzChimeBearer, opts)



&lt;p&gt;The details of the time when a user last read messages in a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonChimeSdkMessaging from 'amazon_chime_sdk_messaging';
let defaultClient = AmazonChimeSdkMessaging.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChimeSdkMessaging.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The ARN of the <code>AppInstanceUser</code> or <code>AppInstanceBot</code> that makes the API call.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateChannelReadMarker(channelArn, xAmzChimeBearer, opts, (error, data, response) => {
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
 **channelArn** | **String**| The ARN of the channel. | 
 **xAmzChimeBearer** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; or &lt;code&gt;AppInstanceBot&lt;/code&gt; that makes the API call. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateChannelReadMarkerResponse**](UpdateChannelReadMarkerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

