# JellyfinApi.AudioApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAudioStream**](AudioApi.md#getAudioStream) | **GET** /Audio/{itemId}/stream | Gets an audio stream.
[**getAudioStreamByContainer**](AudioApi.md#getAudioStreamByContainer) | **GET** /Audio/{itemId}/stream.{container} | Gets an audio stream.
[**headAudioStream**](AudioApi.md#headAudioStream) | **HEAD** /Audio/{itemId}/stream | Gets an audio stream.
[**headAudioStreamByContainer**](AudioApi.md#headAudioStreamByContainer) | **HEAD** /Audio/{itemId}/stream.{container} | Gets an audio stream.



## getAudioStream

> File getAudioStream(itemId, opts)

Gets an audio stream.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.AudioApi();
let itemId = "itemId_example"; // String | The item id.
let opts = {
  'container': "container_example", // String | The audio container.
  '_static': true, // Boolean | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false.
  'params': "params_example", // String | The streaming parameters.
  'tag': "tag_example", // String | The tag.
  'deviceProfileId': "deviceProfileId_example", // String | Optional. The dlna device profile id to utilize.
  'playSessionId': "playSessionId_example", // String | The play session id.
  'segmentContainer': "segmentContainer_example", // String | The segment container.
  'segmentLength': 56, // Number | The segment length.
  'minSegments': 56, // Number | The minimum number of segments.
  'mediaSourceId': "mediaSourceId_example", // String | The media version id, if playing an alternate version.
  'deviceId': "deviceId_example", // String | The device id of the client requesting. Used to stop encoding processes when needed.
  'audioCodec': "audioCodec_example", // String | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
  'enableAutoStreamCopy': true, // Boolean | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
  'allowVideoStreamCopy': true, // Boolean | Whether or not to allow copying of the video stream url.
  'allowAudioStreamCopy': true, // Boolean | Whether or not to allow copying of the audio stream url.
  'breakOnNonKeyFrames': true, // Boolean | Optional. Whether to break on non key frames.
  'audioSampleRate': 56, // Number | Optional. Specify a specific audio sample rate, e.g. 44100.
  'maxAudioBitDepth': 56, // Number | Optional. The maximum audio bit depth.
  'audioBitRate': 56, // Number | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
  'audioChannels': 56, // Number | Optional. Specify a specific number of audio channels to encode to, e.g. 2.
  'maxAudioChannels': 56, // Number | Optional. Specify a maximum number of audio channels to encode to, e.g. 2.
  'profile': "profile_example", // String | Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high.
  'level': "level_example", // String | Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1.
  'framerate': 3.4, // Number | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
  'maxFramerate': 3.4, // Number | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
  'copyTimestamps': true, // Boolean | Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
  'startTimeTicks': 789, // Number | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms.
  'width': 56, // Number | Optional. The fixed horizontal resolution of the encoded video.
  'height': 56, // Number | Optional. The fixed vertical resolution of the encoded video.
  'videoBitRate': 56, // Number | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
  'subtitleStreamIndex': 56, // Number | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
  'subtitleMethod': new JellyfinApi.SubtitleDeliveryMethod(), // SubtitleDeliveryMethod | Optional. Specify the subtitle delivery method.
  'maxRefFrames': 56, // Number | Optional.
  'maxVideoBitDepth': 56, // Number | Optional. The maximum video bit depth.
  'requireAvc': true, // Boolean | Optional. Whether to require avc.
  'deInterlace': true, // Boolean | Optional. Whether to deinterlace the video.
  'requireNonAnamorphic': true, // Boolean | Optional. Whether to require a non anamorphic stream.
  'transcodingMaxAudioChannels': 56, // Number | Optional. The maximum number of audio channels to transcode.
  'cpuCoreLimit': 56, // Number | Optional. The limit of how many cpu cores to use.
  'liveStreamId': "liveStreamId_example", // String | The live stream id.
  'enableMpegtsM2TsMode': true, // Boolean | Optional. Whether to enable the MpegtsM2Ts mode.
  'videoCodec': "videoCodec_example", // String | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h265, h264, mpeg4, theora, vpx, wmv.
  'subtitleCodec': "subtitleCodec_example", // String | Optional. Specify a subtitle codec to encode to.
  'transcodeReasons': "transcodeReasons_example", // String | Optional. The transcoding reason.
  'audioStreamIndex': 56, // Number | Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
  'videoStreamIndex': 56, // Number | Optional. The index of the video stream to use. If omitted the first video stream will be used.
  'context': new JellyfinApi.EncodingContext(), // EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext.
  'streamOptions': {key: "null"} // {String: String} | Optional. The streaming options.
};
apiInstance.getAudioStream(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **container** | **String**| The audio container. | [optional] 
 **_static** | **Boolean**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. | [optional] 
 **params** | **String**| The streaming parameters. | [optional] 
 **tag** | **String**| The tag. | [optional] 
 **deviceProfileId** | **String**| Optional. The dlna device profile id to utilize. | [optional] 
 **playSessionId** | **String**| The play session id. | [optional] 
 **segmentContainer** | **String**| The segment container. | [optional] 
 **segmentLength** | **Number**| The segment length. | [optional] 
 **minSegments** | **Number**| The minimum number of segments. | [optional] 
 **mediaSourceId** | **String**| The media version id, if playing an alternate version. | [optional] 
 **deviceId** | **String**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audioCodec** | **String**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#39;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enableAutoStreamCopy** | **Boolean**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **allowVideoStreamCopy** | **Boolean**| Whether or not to allow copying of the video stream url. | [optional] 
 **allowAudioStreamCopy** | **Boolean**| Whether or not to allow copying of the audio stream url. | [optional] 
 **breakOnNonKeyFrames** | **Boolean**| Optional. Whether to break on non key frames. | [optional] 
 **audioSampleRate** | **Number**| Optional. Specify a specific audio sample rate, e.g. 44100. | [optional] 
 **maxAudioBitDepth** | **Number**| Optional. The maximum audio bit depth. | [optional] 
 **audioBitRate** | **Number**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audioChannels** | **Number**| Optional. Specify a specific number of audio channels to encode to, e.g. 2. | [optional] 
 **maxAudioChannels** | **Number**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2. | [optional] 
 **profile** | **String**| Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high. | [optional] 
 **level** | **String**| Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1. | [optional] 
 **framerate** | **Number**| Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **maxFramerate** | **Number**| Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **copyTimestamps** | **Boolean**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **startTimeTicks** | **Number**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms. | [optional] 
 **width** | **Number**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **Number**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **videoBitRate** | **Number**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitleStreamIndex** | **Number**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitleMethod** | [**SubtitleDeliveryMethod**](.md)| Optional. Specify the subtitle delivery method. | [optional] 
 **maxRefFrames** | **Number**| Optional. | [optional] 
 **maxVideoBitDepth** | **Number**| Optional. The maximum video bit depth. | [optional] 
 **requireAvc** | **Boolean**| Optional. Whether to require avc. | [optional] 
 **deInterlace** | **Boolean**| Optional. Whether to deinterlace the video. | [optional] 
 **requireNonAnamorphic** | **Boolean**| Optional. Whether to require a non anamorphic stream. | [optional] 
 **transcodingMaxAudioChannels** | **Number**| Optional. The maximum number of audio channels to transcode. | [optional] 
 **cpuCoreLimit** | **Number**| Optional. The limit of how many cpu cores to use. | [optional] 
 **liveStreamId** | **String**| The live stream id. | [optional] 
 **enableMpegtsM2TsMode** | **Boolean**| Optional. Whether to enable the MpegtsM2Ts mode. | [optional] 
 **videoCodec** | **String**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#39;s extension. Options: h265, h264, mpeg4, theora, vpx, wmv. | [optional] 
 **subtitleCodec** | **String**| Optional. Specify a subtitle codec to encode to. | [optional] 
 **transcodeReasons** | **String**| Optional. The transcoding reason. | [optional] 
 **audioStreamIndex** | **Number**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **videoStreamIndex** | **Number**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 
 **context** | [**EncodingContext**](.md)| Optional. The MediaBrowser.Model.Dlna.EncodingContext. | [optional] 
 **streamOptions** | [**{String: String}**](String.md)| Optional. The streaming options. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: audio/*


## getAudioStreamByContainer

> File getAudioStreamByContainer(itemId, container, opts)

Gets an audio stream.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.AudioApi();
let itemId = "itemId_example"; // String | The item id.
let container = "container_example"; // String | The audio container.
let opts = {
  '_static': true, // Boolean | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false.
  'params': "params_example", // String | The streaming parameters.
  'tag': "tag_example", // String | The tag.
  'deviceProfileId': "deviceProfileId_example", // String | Optional. The dlna device profile id to utilize.
  'playSessionId': "playSessionId_example", // String | The play session id.
  'segmentContainer': "segmentContainer_example", // String | The segment container.
  'segmentLength': 56, // Number | The segment lenght.
  'minSegments': 56, // Number | The minimum number of segments.
  'mediaSourceId': "mediaSourceId_example", // String | The media version id, if playing an alternate version.
  'deviceId': "deviceId_example", // String | The device id of the client requesting. Used to stop encoding processes when needed.
  'audioCodec': "audioCodec_example", // String | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
  'enableAutoStreamCopy': true, // Boolean | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
  'allowVideoStreamCopy': true, // Boolean | Whether or not to allow copying of the video stream url.
  'allowAudioStreamCopy': true, // Boolean | Whether or not to allow copying of the audio stream url.
  'breakOnNonKeyFrames': true, // Boolean | Optional. Whether to break on non key frames.
  'audioSampleRate': 56, // Number | Optional. Specify a specific audio sample rate, e.g. 44100.
  'maxAudioBitDepth': 56, // Number | Optional. The maximum audio bit depth.
  'audioBitRate': 56, // Number | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
  'audioChannels': 56, // Number | Optional. Specify a specific number of audio channels to encode to, e.g. 2.
  'maxAudioChannels': 56, // Number | Optional. Specify a maximum number of audio channels to encode to, e.g. 2.
  'profile': "profile_example", // String | Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high.
  'level': "level_example", // String | Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1.
  'framerate': 3.4, // Number | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
  'maxFramerate': 3.4, // Number | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
  'copyTimestamps': true, // Boolean | Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
  'startTimeTicks': 789, // Number | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms.
  'width': 56, // Number | Optional. The fixed horizontal resolution of the encoded video.
  'height': 56, // Number | Optional. The fixed vertical resolution of the encoded video.
  'videoBitRate': 56, // Number | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
  'subtitleStreamIndex': 56, // Number | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
  'subtitleMethod': new JellyfinApi.SubtitleDeliveryMethod(), // SubtitleDeliveryMethod | Optional. Specify the subtitle delivery method.
  'maxRefFrames': 56, // Number | Optional.
  'maxVideoBitDepth': 56, // Number | Optional. The maximum video bit depth.
  'requireAvc': true, // Boolean | Optional. Whether to require avc.
  'deInterlace': true, // Boolean | Optional. Whether to deinterlace the video.
  'requireNonAnamorphic': true, // Boolean | Optional. Whether to require a non anamporphic stream.
  'transcodingMaxAudioChannels': 56, // Number | Optional. The maximum number of audio channels to transcode.
  'cpuCoreLimit': 56, // Number | Optional. The limit of how many cpu cores to use.
  'liveStreamId': "liveStreamId_example", // String | The live stream id.
  'enableMpegtsM2TsMode': true, // Boolean | Optional. Whether to enable the MpegtsM2Ts mode.
  'videoCodec': "videoCodec_example", // String | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h265, h264, mpeg4, theora, vpx, wmv.
  'subtitleCodec': "subtitleCodec_example", // String | Optional. Specify a subtitle codec to encode to.
  'transcodeReasons': "transcodeReasons_example", // String | Optional. The transcoding reason.
  'audioStreamIndex': 56, // Number | Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
  'videoStreamIndex': 56, // Number | Optional. The index of the video stream to use. If omitted the first video stream will be used.
  'context': new JellyfinApi.EncodingContext(), // EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext.
  'streamOptions': {key: "null"} // {String: String} | Optional. The streaming options.
};
apiInstance.getAudioStreamByContainer(itemId, container, opts, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **container** | **String**| The audio container. | 
 **_static** | **Boolean**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. | [optional] 
 **params** | **String**| The streaming parameters. | [optional] 
 **tag** | **String**| The tag. | [optional] 
 **deviceProfileId** | **String**| Optional. The dlna device profile id to utilize. | [optional] 
 **playSessionId** | **String**| The play session id. | [optional] 
 **segmentContainer** | **String**| The segment container. | [optional] 
 **segmentLength** | **Number**| The segment lenght. | [optional] 
 **minSegments** | **Number**| The minimum number of segments. | [optional] 
 **mediaSourceId** | **String**| The media version id, if playing an alternate version. | [optional] 
 **deviceId** | **String**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audioCodec** | **String**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#39;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enableAutoStreamCopy** | **Boolean**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **allowVideoStreamCopy** | **Boolean**| Whether or not to allow copying of the video stream url. | [optional] 
 **allowAudioStreamCopy** | **Boolean**| Whether or not to allow copying of the audio stream url. | [optional] 
 **breakOnNonKeyFrames** | **Boolean**| Optional. Whether to break on non key frames. | [optional] 
 **audioSampleRate** | **Number**| Optional. Specify a specific audio sample rate, e.g. 44100. | [optional] 
 **maxAudioBitDepth** | **Number**| Optional. The maximum audio bit depth. | [optional] 
 **audioBitRate** | **Number**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audioChannels** | **Number**| Optional. Specify a specific number of audio channels to encode to, e.g. 2. | [optional] 
 **maxAudioChannels** | **Number**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2. | [optional] 
 **profile** | **String**| Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high. | [optional] 
 **level** | **String**| Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1. | [optional] 
 **framerate** | **Number**| Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **maxFramerate** | **Number**| Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **copyTimestamps** | **Boolean**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **startTimeTicks** | **Number**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms. | [optional] 
 **width** | **Number**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **Number**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **videoBitRate** | **Number**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitleStreamIndex** | **Number**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitleMethod** | [**SubtitleDeliveryMethod**](.md)| Optional. Specify the subtitle delivery method. | [optional] 
 **maxRefFrames** | **Number**| Optional. | [optional] 
 **maxVideoBitDepth** | **Number**| Optional. The maximum video bit depth. | [optional] 
 **requireAvc** | **Boolean**| Optional. Whether to require avc. | [optional] 
 **deInterlace** | **Boolean**| Optional. Whether to deinterlace the video. | [optional] 
 **requireNonAnamorphic** | **Boolean**| Optional. Whether to require a non anamporphic stream. | [optional] 
 **transcodingMaxAudioChannels** | **Number**| Optional. The maximum number of audio channels to transcode. | [optional] 
 **cpuCoreLimit** | **Number**| Optional. The limit of how many cpu cores to use. | [optional] 
 **liveStreamId** | **String**| The live stream id. | [optional] 
 **enableMpegtsM2TsMode** | **Boolean**| Optional. Whether to enable the MpegtsM2Ts mode. | [optional] 
 **videoCodec** | **String**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#39;s extension. Options: h265, h264, mpeg4, theora, vpx, wmv. | [optional] 
 **subtitleCodec** | **String**| Optional. Specify a subtitle codec to encode to. | [optional] 
 **transcodeReasons** | **String**| Optional. The transcoding reason. | [optional] 
 **audioStreamIndex** | **Number**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **videoStreamIndex** | **Number**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 
 **context** | [**EncodingContext**](.md)| Optional. The MediaBrowser.Model.Dlna.EncodingContext. | [optional] 
 **streamOptions** | [**{String: String}**](String.md)| Optional. The streaming options. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: audio/*


## headAudioStream

> File headAudioStream(itemId, opts)

Gets an audio stream.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.AudioApi();
let itemId = "itemId_example"; // String | The item id.
let opts = {
  'container': "container_example", // String | The audio container.
  '_static': true, // Boolean | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false.
  'params': "params_example", // String | The streaming parameters.
  'tag': "tag_example", // String | The tag.
  'deviceProfileId': "deviceProfileId_example", // String | Optional. The dlna device profile id to utilize.
  'playSessionId': "playSessionId_example", // String | The play session id.
  'segmentContainer': "segmentContainer_example", // String | The segment container.
  'segmentLength': 56, // Number | The segment length.
  'minSegments': 56, // Number | The minimum number of segments.
  'mediaSourceId': "mediaSourceId_example", // String | The media version id, if playing an alternate version.
  'deviceId': "deviceId_example", // String | The device id of the client requesting. Used to stop encoding processes when needed.
  'audioCodec': "audioCodec_example", // String | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
  'enableAutoStreamCopy': true, // Boolean | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
  'allowVideoStreamCopy': true, // Boolean | Whether or not to allow copying of the video stream url.
  'allowAudioStreamCopy': true, // Boolean | Whether or not to allow copying of the audio stream url.
  'breakOnNonKeyFrames': true, // Boolean | Optional. Whether to break on non key frames.
  'audioSampleRate': 56, // Number | Optional. Specify a specific audio sample rate, e.g. 44100.
  'maxAudioBitDepth': 56, // Number | Optional. The maximum audio bit depth.
  'audioBitRate': 56, // Number | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
  'audioChannels': 56, // Number | Optional. Specify a specific number of audio channels to encode to, e.g. 2.
  'maxAudioChannels': 56, // Number | Optional. Specify a maximum number of audio channels to encode to, e.g. 2.
  'profile': "profile_example", // String | Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high.
  'level': "level_example", // String | Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1.
  'framerate': 3.4, // Number | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
  'maxFramerate': 3.4, // Number | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
  'copyTimestamps': true, // Boolean | Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
  'startTimeTicks': 789, // Number | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms.
  'width': 56, // Number | Optional. The fixed horizontal resolution of the encoded video.
  'height': 56, // Number | Optional. The fixed vertical resolution of the encoded video.
  'videoBitRate': 56, // Number | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
  'subtitleStreamIndex': 56, // Number | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
  'subtitleMethod': new JellyfinApi.SubtitleDeliveryMethod(), // SubtitleDeliveryMethod | Optional. Specify the subtitle delivery method.
  'maxRefFrames': 56, // Number | Optional.
  'maxVideoBitDepth': 56, // Number | Optional. The maximum video bit depth.
  'requireAvc': true, // Boolean | Optional. Whether to require avc.
  'deInterlace': true, // Boolean | Optional. Whether to deinterlace the video.
  'requireNonAnamorphic': true, // Boolean | Optional. Whether to require a non anamorphic stream.
  'transcodingMaxAudioChannels': 56, // Number | Optional. The maximum number of audio channels to transcode.
  'cpuCoreLimit': 56, // Number | Optional. The limit of how many cpu cores to use.
  'liveStreamId': "liveStreamId_example", // String | The live stream id.
  'enableMpegtsM2TsMode': true, // Boolean | Optional. Whether to enable the MpegtsM2Ts mode.
  'videoCodec': "videoCodec_example", // String | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h265, h264, mpeg4, theora, vpx, wmv.
  'subtitleCodec': "subtitleCodec_example", // String | Optional. Specify a subtitle codec to encode to.
  'transcodeReasons': "transcodeReasons_example", // String | Optional. The transcoding reason.
  'audioStreamIndex': 56, // Number | Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
  'videoStreamIndex': 56, // Number | Optional. The index of the video stream to use. If omitted the first video stream will be used.
  'context': new JellyfinApi.EncodingContext(), // EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext.
  'streamOptions': {key: "null"} // {String: String} | Optional. The streaming options.
};
apiInstance.headAudioStream(itemId, opts, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **container** | **String**| The audio container. | [optional] 
 **_static** | **Boolean**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. | [optional] 
 **params** | **String**| The streaming parameters. | [optional] 
 **tag** | **String**| The tag. | [optional] 
 **deviceProfileId** | **String**| Optional. The dlna device profile id to utilize. | [optional] 
 **playSessionId** | **String**| The play session id. | [optional] 
 **segmentContainer** | **String**| The segment container. | [optional] 
 **segmentLength** | **Number**| The segment length. | [optional] 
 **minSegments** | **Number**| The minimum number of segments. | [optional] 
 **mediaSourceId** | **String**| The media version id, if playing an alternate version. | [optional] 
 **deviceId** | **String**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audioCodec** | **String**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#39;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enableAutoStreamCopy** | **Boolean**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **allowVideoStreamCopy** | **Boolean**| Whether or not to allow copying of the video stream url. | [optional] 
 **allowAudioStreamCopy** | **Boolean**| Whether or not to allow copying of the audio stream url. | [optional] 
 **breakOnNonKeyFrames** | **Boolean**| Optional. Whether to break on non key frames. | [optional] 
 **audioSampleRate** | **Number**| Optional. Specify a specific audio sample rate, e.g. 44100. | [optional] 
 **maxAudioBitDepth** | **Number**| Optional. The maximum audio bit depth. | [optional] 
 **audioBitRate** | **Number**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audioChannels** | **Number**| Optional. Specify a specific number of audio channels to encode to, e.g. 2. | [optional] 
 **maxAudioChannels** | **Number**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2. | [optional] 
 **profile** | **String**| Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high. | [optional] 
 **level** | **String**| Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1. | [optional] 
 **framerate** | **Number**| Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **maxFramerate** | **Number**| Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **copyTimestamps** | **Boolean**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **startTimeTicks** | **Number**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms. | [optional] 
 **width** | **Number**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **Number**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **videoBitRate** | **Number**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitleStreamIndex** | **Number**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitleMethod** | [**SubtitleDeliveryMethod**](.md)| Optional. Specify the subtitle delivery method. | [optional] 
 **maxRefFrames** | **Number**| Optional. | [optional] 
 **maxVideoBitDepth** | **Number**| Optional. The maximum video bit depth. | [optional] 
 **requireAvc** | **Boolean**| Optional. Whether to require avc. | [optional] 
 **deInterlace** | **Boolean**| Optional. Whether to deinterlace the video. | [optional] 
 **requireNonAnamorphic** | **Boolean**| Optional. Whether to require a non anamorphic stream. | [optional] 
 **transcodingMaxAudioChannels** | **Number**| Optional. The maximum number of audio channels to transcode. | [optional] 
 **cpuCoreLimit** | **Number**| Optional. The limit of how many cpu cores to use. | [optional] 
 **liveStreamId** | **String**| The live stream id. | [optional] 
 **enableMpegtsM2TsMode** | **Boolean**| Optional. Whether to enable the MpegtsM2Ts mode. | [optional] 
 **videoCodec** | **String**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#39;s extension. Options: h265, h264, mpeg4, theora, vpx, wmv. | [optional] 
 **subtitleCodec** | **String**| Optional. Specify a subtitle codec to encode to. | [optional] 
 **transcodeReasons** | **String**| Optional. The transcoding reason. | [optional] 
 **audioStreamIndex** | **Number**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **videoStreamIndex** | **Number**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 
 **context** | [**EncodingContext**](.md)| Optional. The MediaBrowser.Model.Dlna.EncodingContext. | [optional] 
 **streamOptions** | [**{String: String}**](String.md)| Optional. The streaming options. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: audio/*


## headAudioStreamByContainer

> File headAudioStreamByContainer(itemId, container, opts)

Gets an audio stream.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.AudioApi();
let itemId = "itemId_example"; // String | The item id.
let container = "container_example"; // String | The audio container.
let opts = {
  '_static': true, // Boolean | Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false.
  'params': "params_example", // String | The streaming parameters.
  'tag': "tag_example", // String | The tag.
  'deviceProfileId': "deviceProfileId_example", // String | Optional. The dlna device profile id to utilize.
  'playSessionId': "playSessionId_example", // String | The play session id.
  'segmentContainer': "segmentContainer_example", // String | The segment container.
  'segmentLength': 56, // Number | The segment lenght.
  'minSegments': 56, // Number | The minimum number of segments.
  'mediaSourceId': "mediaSourceId_example", // String | The media version id, if playing an alternate version.
  'deviceId': "deviceId_example", // String | The device id of the client requesting. Used to stop encoding processes when needed.
  'audioCodec': "audioCodec_example", // String | Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
  'enableAutoStreamCopy': true, // Boolean | Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
  'allowVideoStreamCopy': true, // Boolean | Whether or not to allow copying of the video stream url.
  'allowAudioStreamCopy': true, // Boolean | Whether or not to allow copying of the audio stream url.
  'breakOnNonKeyFrames': true, // Boolean | Optional. Whether to break on non key frames.
  'audioSampleRate': 56, // Number | Optional. Specify a specific audio sample rate, e.g. 44100.
  'maxAudioBitDepth': 56, // Number | Optional. The maximum audio bit depth.
  'audioBitRate': 56, // Number | Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
  'audioChannels': 56, // Number | Optional. Specify a specific number of audio channels to encode to, e.g. 2.
  'maxAudioChannels': 56, // Number | Optional. Specify a maximum number of audio channels to encode to, e.g. 2.
  'profile': "profile_example", // String | Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high.
  'level': "level_example", // String | Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1.
  'framerate': 3.4, // Number | Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
  'maxFramerate': 3.4, // Number | Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
  'copyTimestamps': true, // Boolean | Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
  'startTimeTicks': 789, // Number | Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms.
  'width': 56, // Number | Optional. The fixed horizontal resolution of the encoded video.
  'height': 56, // Number | Optional. The fixed vertical resolution of the encoded video.
  'videoBitRate': 56, // Number | Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
  'subtitleStreamIndex': 56, // Number | Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
  'subtitleMethod': new JellyfinApi.SubtitleDeliveryMethod(), // SubtitleDeliveryMethod | Optional. Specify the subtitle delivery method.
  'maxRefFrames': 56, // Number | Optional.
  'maxVideoBitDepth': 56, // Number | Optional. The maximum video bit depth.
  'requireAvc': true, // Boolean | Optional. Whether to require avc.
  'deInterlace': true, // Boolean | Optional. Whether to deinterlace the video.
  'requireNonAnamorphic': true, // Boolean | Optional. Whether to require a non anamporphic stream.
  'transcodingMaxAudioChannels': 56, // Number | Optional. The maximum number of audio channels to transcode.
  'cpuCoreLimit': 56, // Number | Optional. The limit of how many cpu cores to use.
  'liveStreamId': "liveStreamId_example", // String | The live stream id.
  'enableMpegtsM2TsMode': true, // Boolean | Optional. Whether to enable the MpegtsM2Ts mode.
  'videoCodec': "videoCodec_example", // String | Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h265, h264, mpeg4, theora, vpx, wmv.
  'subtitleCodec': "subtitleCodec_example", // String | Optional. Specify a subtitle codec to encode to.
  'transcodeReasons': "transcodeReasons_example", // String | Optional. The transcoding reason.
  'audioStreamIndex': 56, // Number | Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
  'videoStreamIndex': 56, // Number | Optional. The index of the video stream to use. If omitted the first video stream will be used.
  'context': new JellyfinApi.EncodingContext(), // EncodingContext | Optional. The MediaBrowser.Model.Dlna.EncodingContext.
  'streamOptions': {key: "null"} // {String: String} | Optional. The streaming options.
};
apiInstance.headAudioStreamByContainer(itemId, container, opts, (error, data, response) => {
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
 **itemId** | **String**| The item id. | 
 **container** | **String**| The audio container. | 
 **_static** | **Boolean**| Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false. | [optional] 
 **params** | **String**| The streaming parameters. | [optional] 
 **tag** | **String**| The tag. | [optional] 
 **deviceProfileId** | **String**| Optional. The dlna device profile id to utilize. | [optional] 
 **playSessionId** | **String**| The play session id. | [optional] 
 **segmentContainer** | **String**| The segment container. | [optional] 
 **segmentLength** | **Number**| The segment lenght. | [optional] 
 **minSegments** | **Number**| The minimum number of segments. | [optional] 
 **mediaSourceId** | **String**| The media version id, if playing an alternate version. | [optional] 
 **deviceId** | **String**| The device id of the client requesting. Used to stop encoding processes when needed. | [optional] 
 **audioCodec** | **String**| Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#39;s extension. Options: aac, mp3, vorbis, wma. | [optional] 
 **enableAutoStreamCopy** | **Boolean**| Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true. | [optional] 
 **allowVideoStreamCopy** | **Boolean**| Whether or not to allow copying of the video stream url. | [optional] 
 **allowAudioStreamCopy** | **Boolean**| Whether or not to allow copying of the audio stream url. | [optional] 
 **breakOnNonKeyFrames** | **Boolean**| Optional. Whether to break on non key frames. | [optional] 
 **audioSampleRate** | **Number**| Optional. Specify a specific audio sample rate, e.g. 44100. | [optional] 
 **maxAudioBitDepth** | **Number**| Optional. The maximum audio bit depth. | [optional] 
 **audioBitRate** | **Number**| Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults. | [optional] 
 **audioChannels** | **Number**| Optional. Specify a specific number of audio channels to encode to, e.g. 2. | [optional] 
 **maxAudioChannels** | **Number**| Optional. Specify a maximum number of audio channels to encode to, e.g. 2. | [optional] 
 **profile** | **String**| Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high. | [optional] 
 **level** | **String**| Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1. | [optional] 
 **framerate** | **Number**| Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **maxFramerate** | **Number**| Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements. | [optional] 
 **copyTimestamps** | **Boolean**| Whether or not to copy timestamps when transcoding with an offset. Defaults to false. | [optional] 
 **startTimeTicks** | **Number**| Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms. | [optional] 
 **width** | **Number**| Optional. The fixed horizontal resolution of the encoded video. | [optional] 
 **height** | **Number**| Optional. The fixed vertical resolution of the encoded video. | [optional] 
 **videoBitRate** | **Number**| Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults. | [optional] 
 **subtitleStreamIndex** | **Number**| Optional. The index of the subtitle stream to use. If omitted no subtitles will be used. | [optional] 
 **subtitleMethod** | [**SubtitleDeliveryMethod**](.md)| Optional. Specify the subtitle delivery method. | [optional] 
 **maxRefFrames** | **Number**| Optional. | [optional] 
 **maxVideoBitDepth** | **Number**| Optional. The maximum video bit depth. | [optional] 
 **requireAvc** | **Boolean**| Optional. Whether to require avc. | [optional] 
 **deInterlace** | **Boolean**| Optional. Whether to deinterlace the video. | [optional] 
 **requireNonAnamorphic** | **Boolean**| Optional. Whether to require a non anamporphic stream. | [optional] 
 **transcodingMaxAudioChannels** | **Number**| Optional. The maximum number of audio channels to transcode. | [optional] 
 **cpuCoreLimit** | **Number**| Optional. The limit of how many cpu cores to use. | [optional] 
 **liveStreamId** | **String**| The live stream id. | [optional] 
 **enableMpegtsM2TsMode** | **Boolean**| Optional. Whether to enable the MpegtsM2Ts mode. | [optional] 
 **videoCodec** | **String**| Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#39;s extension. Options: h265, h264, mpeg4, theora, vpx, wmv. | [optional] 
 **subtitleCodec** | **String**| Optional. Specify a subtitle codec to encode to. | [optional] 
 **transcodeReasons** | **String**| Optional. The transcoding reason. | [optional] 
 **audioStreamIndex** | **Number**| Optional. The index of the audio stream to use. If omitted the first audio stream will be used. | [optional] 
 **videoStreamIndex** | **Number**| Optional. The index of the video stream to use. If omitted the first video stream will be used. | [optional] 
 **context** | [**EncodingContext**](.md)| Optional. The MediaBrowser.Model.Dlna.EncodingContext. | [optional] 
 **streamOptions** | [**{String: String}**](String.md)| Optional. The streaming options. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: audio/*

