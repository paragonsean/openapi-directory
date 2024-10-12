# AmazonKinesisVideoWebRtcStorage.DefaultApi

All URIs are relative to *http://kinesisvideo.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**joinStorageSession**](DefaultApi.md#joinStorageSession) | **POST** /joinStorageSession | 



## joinStorageSession

> joinStorageSession(joinStorageSessionRequest, opts)



&lt;p&gt; Join the ongoing one way-video and/or multi-way audio WebRTC session as a video producing device for an input channel. If there’s no existing session for the channel, a new streaming session needs to be created, and the Amazon Resource Name (ARN) of the signaling channel must be provided. &lt;/p&gt; &lt;p&gt;Currently for the &lt;code&gt;SINGLE_MASTER&lt;/code&gt; type, a video producing device is able to ingest both audio and video media into a stream, while viewers can only ingest audio. Both a video producing device and viewers can join the session first, and wait for other participants.&lt;/p&gt; &lt;p&gt;While participants are having peer to peer conversations through webRTC, the ingested media session will be stored into the Kinesis Video Stream. Multiple viewers are able to playback real-time media.&lt;/p&gt; &lt;p&gt;Customers can also use existing Kinesis Video Streams features like &lt;code&gt;HLS&lt;/code&gt; or &lt;code&gt;DASH&lt;/code&gt; playback, Image generation, and more with ingested WebRTC media.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Assume that only one video producing device client can be associated with a session for the channel. If more than one client joins the session of a specific channel as a video producing device, the most recent client request takes precedence. &lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonKinesisVideoWebRtcStorage from 'amazon_kinesis_video_web_rtc_storage';
let defaultClient = AmazonKinesisVideoWebRtcStorage.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonKinesisVideoWebRtcStorage.DefaultApi();
let joinStorageSessionRequest = new AmazonKinesisVideoWebRtcStorage.JoinStorageSessionRequest(); // JoinStorageSessionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.joinStorageSession(joinStorageSessionRequest, opts, (error, data, response) => {
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
 **joinStorageSessionRequest** | [**JoinStorageSessionRequest**](JoinStorageSessionRequest.md)|  | 
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

