# AmazonKinesisVideoSignalingChannels.DefaultApi

All URIs are relative to *http://kinesisvideo.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getIceServerConfig**](DefaultApi.md#getIceServerConfig) | **POST** /v1/get-ice-server-config | 
[**sendAlexaOfferToMaster**](DefaultApi.md#sendAlexaOfferToMaster) | **POST** /v1/send-alexa-offer-to-master | 



## getIceServerConfig

> GetIceServerConfigResponse getIceServerConfig(getIceServerConfigRequest, opts)



&lt;p&gt;Gets the Interactive Connectivity Establishment (ICE) server configuration information, including URIs, username, and password which can be used to configure the WebRTC connection. The ICE component uses this configuration information to setup the WebRTC connection, including authenticating with the Traversal Using Relays around NAT (TURN) relay server. &lt;/p&gt; &lt;p&gt;TURN is a protocol that is used to improve the connectivity of peer-to-peer applications. By providing a cloud-based relay service, TURN ensures that a connection can be established even when one or more peers are incapable of a direct peer-to-peer connection. For more information, see &lt;a href&#x3D;\&quot;https://tools.ietf.org/html/draft-uberti-rtcweb-turn-rest-00\&quot;&gt;A REST API For Access To TURN Services&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; You can invoke this API to establish a fallback mechanism in case either of the peers is unable to establish a direct peer-to-peer connection over a signaling channel. You must specify either a signaling channel ARN or the client ID in order to invoke this API.&lt;/p&gt;

### Example

```javascript
import AmazonKinesisVideoSignalingChannels from 'amazon_kinesis_video_signaling_channels';
let defaultClient = AmazonKinesisVideoSignalingChannels.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoSignalingChannels.DefaultApi();
let getIceServerConfigRequest = new AmazonKinesisVideoSignalingChannels.GetIceServerConfigRequest(); // GetIceServerConfigRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getIceServerConfig(getIceServerConfigRequest, opts, (error, data, response) => {
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
 **getIceServerConfigRequest** | [**GetIceServerConfigRequest**](GetIceServerConfigRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetIceServerConfigResponse**](GetIceServerConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendAlexaOfferToMaster

> SendAlexaOfferToMasterResponse sendAlexaOfferToMaster(sendAlexaOfferToMasterRequest, opts)



This API allows you to connect WebRTC-enabled devices with Alexa display devices. When invoked, it sends the Alexa Session Description Protocol (SDP) offer to the master peer. The offer is delivered as soon as the master is connected to the specified signaling channel. This API returns the SDP answer from the connected master. If the master is not connected to the signaling channel, redelivery requests are made until the message expires.

### Example

```javascript
import AmazonKinesisVideoSignalingChannels from 'amazon_kinesis_video_signaling_channels';
let defaultClient = AmazonKinesisVideoSignalingChannels.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoSignalingChannels.DefaultApi();
let sendAlexaOfferToMasterRequest = new AmazonKinesisVideoSignalingChannels.SendAlexaOfferToMasterRequest(); // SendAlexaOfferToMasterRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.sendAlexaOfferToMaster(sendAlexaOfferToMasterRequest, opts, (error, data, response) => {
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
 **sendAlexaOfferToMasterRequest** | [**SendAlexaOfferToMasterRequest**](SendAlexaOfferToMasterRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SendAlexaOfferToMasterResponse**](SendAlexaOfferToMasterResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

