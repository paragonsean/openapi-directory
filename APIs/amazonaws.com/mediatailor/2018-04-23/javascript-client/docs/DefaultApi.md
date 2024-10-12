# AwsMediaTailor.DefaultApi

All URIs are relative to *http://api.mediatailor.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configureLogsForChannel**](DefaultApi.md#configureLogsForChannel) | **PUT** /configureLogs/channel | 
[**configureLogsForPlaybackConfiguration**](DefaultApi.md#configureLogsForPlaybackConfiguration) | **PUT** /configureLogs/playbackConfiguration | 
[**createChannel**](DefaultApi.md#createChannel) | **POST** /channel/{ChannelName} | 
[**createLiveSource**](DefaultApi.md#createLiveSource) | **POST** /sourceLocation/{SourceLocationName}/liveSource/{LiveSourceName} | 
[**createPrefetchSchedule**](DefaultApi.md#createPrefetchSchedule) | **POST** /prefetchSchedule/{PlaybackConfigurationName}/{Name} | 
[**createProgram**](DefaultApi.md#createProgram) | **POST** /channel/{ChannelName}/program/{ProgramName} | 
[**createSourceLocation**](DefaultApi.md#createSourceLocation) | **POST** /sourceLocation/{SourceLocationName} | 
[**createVodSource**](DefaultApi.md#createVodSource) | **POST** /sourceLocation/{SourceLocationName}/vodSource/{VodSourceName} | 
[**deleteChannel**](DefaultApi.md#deleteChannel) | **DELETE** /channel/{ChannelName} | 
[**deleteChannelPolicy**](DefaultApi.md#deleteChannelPolicy) | **DELETE** /channel/{ChannelName}/policy | 
[**deleteLiveSource**](DefaultApi.md#deleteLiveSource) | **DELETE** /sourceLocation/{SourceLocationName}/liveSource/{LiveSourceName} | 
[**deletePlaybackConfiguration**](DefaultApi.md#deletePlaybackConfiguration) | **DELETE** /playbackConfiguration/{Name} | 
[**deletePrefetchSchedule**](DefaultApi.md#deletePrefetchSchedule) | **DELETE** /prefetchSchedule/{PlaybackConfigurationName}/{Name} | 
[**deleteProgram**](DefaultApi.md#deleteProgram) | **DELETE** /channel/{ChannelName}/program/{ProgramName} | 
[**deleteSourceLocation**](DefaultApi.md#deleteSourceLocation) | **DELETE** /sourceLocation/{SourceLocationName} | 
[**deleteVodSource**](DefaultApi.md#deleteVodSource) | **DELETE** /sourceLocation/{SourceLocationName}/vodSource/{VodSourceName} | 
[**describeChannel**](DefaultApi.md#describeChannel) | **GET** /channel/{ChannelName} | 
[**describeLiveSource**](DefaultApi.md#describeLiveSource) | **GET** /sourceLocation/{SourceLocationName}/liveSource/{LiveSourceName} | 
[**describeProgram**](DefaultApi.md#describeProgram) | **GET** /channel/{ChannelName}/program/{ProgramName} | 
[**describeSourceLocation**](DefaultApi.md#describeSourceLocation) | **GET** /sourceLocation/{SourceLocationName} | 
[**describeVodSource**](DefaultApi.md#describeVodSource) | **GET** /sourceLocation/{SourceLocationName}/vodSource/{VodSourceName} | 
[**getChannelPolicy**](DefaultApi.md#getChannelPolicy) | **GET** /channel/{ChannelName}/policy | 
[**getChannelSchedule**](DefaultApi.md#getChannelSchedule) | **GET** /channel/{ChannelName}/schedule | 
[**getPlaybackConfiguration**](DefaultApi.md#getPlaybackConfiguration) | **GET** /playbackConfiguration/{Name} | 
[**getPrefetchSchedule**](DefaultApi.md#getPrefetchSchedule) | **GET** /prefetchSchedule/{PlaybackConfigurationName}/{Name} | 
[**listAlerts**](DefaultApi.md#listAlerts) | **GET** /alerts#resourceArn | 
[**listChannels**](DefaultApi.md#listChannels) | **GET** /channels | 
[**listLiveSources**](DefaultApi.md#listLiveSources) | **GET** /sourceLocation/{SourceLocationName}/liveSources | 
[**listPlaybackConfigurations**](DefaultApi.md#listPlaybackConfigurations) | **GET** /playbackConfigurations | 
[**listPrefetchSchedules**](DefaultApi.md#listPrefetchSchedules) | **POST** /prefetchSchedule/{PlaybackConfigurationName} | 
[**listSourceLocations**](DefaultApi.md#listSourceLocations) | **GET** /sourceLocations | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{ResourceArn} | 
[**listVodSources**](DefaultApi.md#listVodSources) | **GET** /sourceLocation/{SourceLocationName}/vodSources | 
[**putChannelPolicy**](DefaultApi.md#putChannelPolicy) | **PUT** /channel/{ChannelName}/policy | 
[**putPlaybackConfiguration**](DefaultApi.md#putPlaybackConfiguration) | **PUT** /playbackConfiguration | 
[**startChannel**](DefaultApi.md#startChannel) | **PUT** /channel/{ChannelName}/start | 
[**stopChannel**](DefaultApi.md#stopChannel) | **PUT** /channel/{ChannelName}/stop | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{ResourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{ResourceArn}#tagKeys | 
[**updateChannel**](DefaultApi.md#updateChannel) | **PUT** /channel/{ChannelName} | 
[**updateLiveSource**](DefaultApi.md#updateLiveSource) | **PUT** /sourceLocation/{SourceLocationName}/liveSource/{LiveSourceName} | 
[**updateProgram**](DefaultApi.md#updateProgram) | **PUT** /channel/{ChannelName}/program/{ProgramName} | 
[**updateSourceLocation**](DefaultApi.md#updateSourceLocation) | **PUT** /sourceLocation/{SourceLocationName} | 
[**updateVodSource**](DefaultApi.md#updateVodSource) | **PUT** /sourceLocation/{SourceLocationName}/vodSource/{VodSourceName} | 



## configureLogsForChannel

> ConfigureLogsForChannelResponse configureLogsForChannel(configureLogsForChannelRequest, opts)



Configures Amazon CloudWatch log settings for a channel.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let configureLogsForChannelRequest = new AwsMediaTailor.ConfigureLogsForChannelRequest(); // ConfigureLogsForChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.configureLogsForChannel(configureLogsForChannelRequest, opts, (error, data, response) => {
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
 **configureLogsForChannelRequest** | [**ConfigureLogsForChannelRequest**](ConfigureLogsForChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ConfigureLogsForChannelResponse**](ConfigureLogsForChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## configureLogsForPlaybackConfiguration

> ConfigureLogsForPlaybackConfigurationResponse configureLogsForPlaybackConfiguration(configureLogsForPlaybackConfigurationRequest, opts)



Amazon CloudWatch log settings for a playback configuration.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let configureLogsForPlaybackConfigurationRequest = new AwsMediaTailor.ConfigureLogsForPlaybackConfigurationRequest(); // ConfigureLogsForPlaybackConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.configureLogsForPlaybackConfiguration(configureLogsForPlaybackConfigurationRequest, opts, (error, data, response) => {
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
 **configureLogsForPlaybackConfigurationRequest** | [**ConfigureLogsForPlaybackConfigurationRequest**](ConfigureLogsForPlaybackConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ConfigureLogsForPlaybackConfigurationResponse**](ConfigureLogsForPlaybackConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createChannel

> CreateChannelResponse createChannel(channelName, createChannelRequest, opts)



Creates a channel. For information about MediaTailor channels, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html\&quot;&gt;Working with channels&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let channelName = "channelName_example"; // String | The name of the channel.
let createChannelRequest = new AwsMediaTailor.CreateChannelRequest(); // CreateChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createChannel(channelName, createChannelRequest, opts, (error, data, response) => {
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
 **channelName** | **String**| The name of the channel. | 
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


## createLiveSource

> CreateLiveSourceResponse createLiveSource(liveSourceName, sourceLocationName, createLiveSourceRequest, opts)



The live source configuration.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let liveSourceName = "liveSourceName_example"; // String | The name of the live source.
let sourceLocationName = "sourceLocationName_example"; // String | The name of the source location.
let createLiveSourceRequest = new AwsMediaTailor.CreateLiveSourceRequest(); // CreateLiveSourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createLiveSource(liveSourceName, sourceLocationName, createLiveSourceRequest, opts, (error, data, response) => {
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
 **liveSourceName** | **String**| The name of the live source. | 
 **sourceLocationName** | **String**| The name of the source location. | 
 **createLiveSourceRequest** | [**CreateLiveSourceRequest**](CreateLiveSourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateLiveSourceResponse**](CreateLiveSourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPrefetchSchedule

> CreatePrefetchScheduleResponse createPrefetchSchedule(name, playbackConfigurationName, createPrefetchScheduleRequest, opts)



Creates a prefetch schedule for a playback configuration. A prefetch schedule allows you to tell MediaTailor to fetch and prepare certain ads before an ad break happens. For more information about ad prefetching, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html\&quot;&gt;Using ad prefetching&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let name = "name_example"; // String | The name to assign to the schedule request.
let playbackConfigurationName = "playbackConfigurationName_example"; // String | The name to assign to the playback configuration.
let createPrefetchScheduleRequest = new AwsMediaTailor.CreatePrefetchScheduleRequest(); // CreatePrefetchScheduleRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createPrefetchSchedule(name, playbackConfigurationName, createPrefetchScheduleRequest, opts, (error, data, response) => {
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
 **name** | **String**| The name to assign to the schedule request. | 
 **playbackConfigurationName** | **String**| The name to assign to the playback configuration. | 
 **createPrefetchScheduleRequest** | [**CreatePrefetchScheduleRequest**](CreatePrefetchScheduleRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreatePrefetchScheduleResponse**](CreatePrefetchScheduleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createProgram

> CreateProgramResponse createProgram(channelName, programName, createProgramRequest, opts)



Creates a program within a channel. For information about programs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-programs.html\&quot;&gt;Working with programs&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let channelName = "channelName_example"; // String | The name of the channel for this Program.
let programName = "programName_example"; // String | The name of the Program.
let createProgramRequest = new AwsMediaTailor.CreateProgramRequest(); // CreateProgramRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createProgram(channelName, programName, createProgramRequest, opts, (error, data, response) => {
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
 **channelName** | **String**| The name of the channel for this Program. | 
 **programName** | **String**| The name of the Program. | 
 **createProgramRequest** | [**CreateProgramRequest**](CreateProgramRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateProgramResponse**](CreateProgramResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSourceLocation

> CreateSourceLocationResponse createSourceLocation(sourceLocationName, createSourceLocationRequest, opts)



Creates a source location. A source location is a container for sources. For more information about source locations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html\&quot;&gt;Working with source locations&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let sourceLocationName = "sourceLocationName_example"; // String | The name associated with the source location.
let createSourceLocationRequest = new AwsMediaTailor.CreateSourceLocationRequest(); // CreateSourceLocationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSourceLocation(sourceLocationName, createSourceLocationRequest, opts, (error, data, response) => {
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
 **sourceLocationName** | **String**| The name associated with the source location. | 
 **createSourceLocationRequest** | [**CreateSourceLocationRequest**](CreateSourceLocationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSourceLocationResponse**](CreateSourceLocationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVodSource

> CreateVodSourceResponse createVodSource(sourceLocationName, vodSourceName, createVodSourceRequest, opts)



The VOD source configuration parameters.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let sourceLocationName = "sourceLocationName_example"; // String | The name of the source location for this VOD source.
let vodSourceName = "vodSourceName_example"; // String | The name associated with the VOD source.&gt;
let createVodSourceRequest = new AwsMediaTailor.CreateVodSourceRequest(); // CreateVodSourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createVodSource(sourceLocationName, vodSourceName, createVodSourceRequest, opts, (error, data, response) => {
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
 **sourceLocationName** | **String**| The name of the source location for this VOD source. | 
 **vodSourceName** | **String**| The name associated with the VOD source.&amp;gt; | 
 **createVodSourceRequest** | [**CreateVodSourceRequest**](CreateVodSourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateVodSourceResponse**](CreateVodSourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteChannel

> Object deleteChannel(channelName, opts)



Deletes a channel. For information about MediaTailor channels, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html\&quot;&gt;Working with channels&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let channelName = "channelName_example"; // String | The name of the channel.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteChannel(channelName, opts, (error, data, response) => {
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
 **channelName** | **String**| The name of the channel. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteChannelPolicy

> Object deleteChannelPolicy(channelName, opts)



The channel policy to delete.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let channelName = "channelName_example"; // String | The name of the channel associated with this channel policy.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteChannelPolicy(channelName, opts, (error, data, response) => {
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
 **channelName** | **String**| The name of the channel associated with this channel policy. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteLiveSource

> Object deleteLiveSource(liveSourceName, sourceLocationName, opts)



The live source to delete.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let liveSourceName = "liveSourceName_example"; // String | The name of the live source.
let sourceLocationName = "sourceLocationName_example"; // String | The name of the source location associated with this Live Source.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteLiveSource(liveSourceName, sourceLocationName, opts, (error, data, response) => {
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
 **liveSourceName** | **String**| The name of the live source. | 
 **sourceLocationName** | **String**| The name of the source location associated with this Live Source. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePlaybackConfiguration

> Object deletePlaybackConfiguration(name, opts)



Deletes a playback configuration. For information about MediaTailor configurations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html\&quot;&gt;Working with configurations in AWS Elemental MediaTailor&lt;/a&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let name = "name_example"; // String | The name of the playback configuration.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deletePlaybackConfiguration(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the playback configuration. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePrefetchSchedule

> Object deletePrefetchSchedule(name, playbackConfigurationName, opts)



Deletes a prefetch schedule for a specific playback configuration. If you call &lt;code&gt;DeletePrefetchSchedule&lt;/code&gt; on an expired prefetch schedule, MediaTailor returns an HTTP 404 status code. For more information about ad prefetching, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html\&quot;&gt;Using ad prefetching&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let name = "name_example"; // String | The name of the prefetch schedule. If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.
let playbackConfigurationName = "playbackConfigurationName_example"; // String | The name of the playback configuration for this prefetch schedule.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deletePrefetchSchedule(name, playbackConfigurationName, opts, (error, data, response) => {
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
 **name** | **String**| The name of the prefetch schedule. If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body. | 
 **playbackConfigurationName** | **String**| The name of the playback configuration for this prefetch schedule. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteProgram

> Object deleteProgram(channelName, programName, opts)



Deletes a program within a channel. For information about programs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-programs.html\&quot;&gt;Working with programs&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let channelName = "channelName_example"; // String | The name of the channel.
let programName = "programName_example"; // String | The name of the program.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteProgram(channelName, programName, opts, (error, data, response) => {
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
 **channelName** | **String**| The name of the channel. | 
 **programName** | **String**| The name of the program. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSourceLocation

> Object deleteSourceLocation(sourceLocationName, opts)



Deletes a source location. A source location is a container for sources. For more information about source locations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html\&quot;&gt;Working with source locations&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let sourceLocationName = "sourceLocationName_example"; // String | The name of the source location.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSourceLocation(sourceLocationName, opts, (error, data, response) => {
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
 **sourceLocationName** | **String**| The name of the source location. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVodSource

> Object deleteVodSource(sourceLocationName, vodSourceName, opts)



The video on demand (VOD) source to delete.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let sourceLocationName = "sourceLocationName_example"; // String | The name of the source location associated with this VOD Source.
let vodSourceName = "vodSourceName_example"; // String | The name of the VOD source.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteVodSource(sourceLocationName, vodSourceName, opts, (error, data, response) => {
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
 **sourceLocationName** | **String**| The name of the source location associated with this VOD Source. | 
 **vodSourceName** | **String**| The name of the VOD source. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeChannel

> DescribeChannelResponse describeChannel(channelName, opts)



Describes a channel. For information about MediaTailor channels, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html\&quot;&gt;Working with channels&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let channelName = "channelName_example"; // String | The name of the channel.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeChannel(channelName, opts, (error, data, response) => {
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
 **channelName** | **String**| The name of the channel. | 
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


## describeLiveSource

> DescribeLiveSourceResponse describeLiveSource(liveSourceName, sourceLocationName, opts)



The live source to describe.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let liveSourceName = "liveSourceName_example"; // String | The name of the live source.
let sourceLocationName = "sourceLocationName_example"; // String | The name of the source location associated with this Live Source.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeLiveSource(liveSourceName, sourceLocationName, opts, (error, data, response) => {
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
 **liveSourceName** | **String**| The name of the live source. | 
 **sourceLocationName** | **String**| The name of the source location associated with this Live Source. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeLiveSourceResponse**](DescribeLiveSourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeProgram

> DescribeProgramResponse describeProgram(channelName, programName, opts)



Describes a program within a channel. For information about programs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-programs.html\&quot;&gt;Working with programs&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let channelName = "channelName_example"; // String | The name of the channel associated with this Program.
let programName = "programName_example"; // String | The name of the program.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeProgram(channelName, programName, opts, (error, data, response) => {
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
 **channelName** | **String**| The name of the channel associated with this Program. | 
 **programName** | **String**| The name of the program. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeProgramResponse**](DescribeProgramResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeSourceLocation

> DescribeSourceLocationResponse describeSourceLocation(sourceLocationName, opts)



Describes a source location. A source location is a container for sources. For more information about source locations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html\&quot;&gt;Working with source locations&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let sourceLocationName = "sourceLocationName_example"; // String | The name of the source location.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeSourceLocation(sourceLocationName, opts, (error, data, response) => {
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
 **sourceLocationName** | **String**| The name of the source location. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeSourceLocationResponse**](DescribeSourceLocationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeVodSource

> DescribeVodSourceResponse describeVodSource(sourceLocationName, vodSourceName, opts)



Provides details about a specific video on demand (VOD) source in a specific source location.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let sourceLocationName = "sourceLocationName_example"; // String | The name of the source location associated with this VOD Source.
let vodSourceName = "vodSourceName_example"; // String | The name of the VOD Source.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeVodSource(sourceLocationName, vodSourceName, opts, (error, data, response) => {
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
 **sourceLocationName** | **String**| The name of the source location associated with this VOD Source. | 
 **vodSourceName** | **String**| The name of the VOD Source. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeVodSourceResponse**](DescribeVodSourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelPolicy

> GetChannelPolicyResponse getChannelPolicy(channelName, opts)



Returns the channel&#39;s IAM policy. IAM policies are used to control access to your channel.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let channelName = "channelName_example"; // String | The name of the channel associated with this Channel Policy.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getChannelPolicy(channelName, opts, (error, data, response) => {
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
 **channelName** | **String**| The name of the channel associated with this Channel Policy. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetChannelPolicyResponse**](GetChannelPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelSchedule

> GetChannelScheduleResponse getChannelSchedule(channelName, opts)



Retrieves information about your channel&#39;s schedule.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let channelName = "channelName_example"; // String | The name of the channel associated with this Channel Schedule.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'durationMinutes': "durationMinutes_example", // String | The duration in minutes of the channel schedule.
  'maxResults': 56, // Number | The maximum number of channel schedules that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> channel schedules, use the value of <code>NextToken</code> in the response to get the next page of results.
  'nextToken': "nextToken_example", // String | <p>(Optional) If the playback configuration has more than <code>MaxResults</code> channel schedules, use <code>NextToken</code> to get the second and subsequent pages of results.</p> <p>For the first <code>GetChannelScheduleRequest</code> request, omit this value.</p> <p>For the second and subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request.</p> <p>If the previous response didn't include a <code>NextToken</code> element, there are no more channel schedules to get.</p>
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.getChannelSchedule(channelName, opts, (error, data, response) => {
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
 **channelName** | **String**| The name of the channel associated with this Channel Schedule. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **durationMinutes** | **String**| The duration in minutes of the channel schedule. | [optional] 
 **maxResults** | **Number**| The maximum number of channel schedules that you want MediaTailor to return in response to the current request. If there are more than &lt;code&gt;MaxResults&lt;/code&gt; channel schedules, use the value of &lt;code&gt;NextToken&lt;/code&gt; in the response to get the next page of results. | [optional] 
 **nextToken** | **String**| &lt;p&gt;(Optional) If the playback configuration has more than &lt;code&gt;MaxResults&lt;/code&gt; channel schedules, use &lt;code&gt;NextToken&lt;/code&gt; to get the second and subsequent pages of results.&lt;/p&gt; &lt;p&gt;For the first &lt;code&gt;GetChannelScheduleRequest&lt;/code&gt; request, omit this value.&lt;/p&gt; &lt;p&gt;For the second and subsequent requests, get the value of &lt;code&gt;NextToken&lt;/code&gt; from the previous response and specify that value for &lt;code&gt;NextToken&lt;/code&gt; in the request.&lt;/p&gt; &lt;p&gt;If the previous response didn&#39;t include a &lt;code&gt;NextToken&lt;/code&gt; element, there are no more channel schedules to get.&lt;/p&gt; | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**GetChannelScheduleResponse**](GetChannelScheduleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPlaybackConfiguration

> GetPlaybackConfigurationResponse getPlaybackConfiguration(name, opts)



Retrieves a playback configuration. For information about MediaTailor configurations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html\&quot;&gt;Working with configurations in AWS Elemental MediaTailor&lt;/a&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let name = "name_example"; // String | The identifier for the playback configuration.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPlaybackConfiguration(name, opts, (error, data, response) => {
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
 **name** | **String**| The identifier for the playback configuration. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPlaybackConfigurationResponse**](GetPlaybackConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPrefetchSchedule

> GetPrefetchScheduleResponse getPrefetchSchedule(name, playbackConfigurationName, opts)



Retrieves a prefetch schedule for a playback configuration. A prefetch schedule allows you to tell MediaTailor to fetch and prepare certain ads before an ad break happens. For more information about ad prefetching, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html\&quot;&gt;Using ad prefetching&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let name = "name_example"; // String | The name of the prefetch schedule. The name must be unique among all prefetch schedules that are associated with the specified playback configuration.
let playbackConfigurationName = "playbackConfigurationName_example"; // String | Returns information about the prefetch schedule for a specific playback configuration. If you call <code>GetPrefetchSchedule</code> on an expired prefetch schedule, MediaTailor returns an HTTP 404 status code.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPrefetchSchedule(name, playbackConfigurationName, opts, (error, data, response) => {
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
 **name** | **String**| The name of the prefetch schedule. The name must be unique among all prefetch schedules that are associated with the specified playback configuration. | 
 **playbackConfigurationName** | **String**| Returns information about the prefetch schedule for a specific playback configuration. If you call &lt;code&gt;GetPrefetchSchedule&lt;/code&gt; on an expired prefetch schedule, MediaTailor returns an HTTP 404 status code. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPrefetchScheduleResponse**](GetPrefetchScheduleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAlerts

> ListAlertsResponse listAlerts(resourceArn, opts)



Lists the alerts that are associated with a MediaTailor channel assembly resource.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of alerts that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> alerts, use the value of <code>NextToken</code> in the response to get the next page of results.
  'nextToken': "nextToken_example", // String | Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listAlerts(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of alerts that you want MediaTailor to return in response to the current request. If there are more than &lt;code&gt;MaxResults&lt;/code&gt; alerts, use the value of &lt;code&gt;NextToken&lt;/code&gt; in the response to get the next page of results. | [optional] 
 **nextToken** | **String**| Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListAlertsResponse**](ListAlertsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannels

> ListChannelsResponse listChannels(opts)



Retrieves information about the channels that are associated with the current AWS account.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of channels that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> channels, use the value of <code>NextToken</code> in the response to get the next page of results.
  'nextToken': "nextToken_example", // String | Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChannels(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of channels that you want MediaTailor to return in response to the current request. If there are more than &lt;code&gt;MaxResults&lt;/code&gt; channels, use the value of &lt;code&gt;NextToken&lt;/code&gt; in the response to get the next page of results. | [optional] 
 **nextToken** | **String**| Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChannelsResponse**](ListChannelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listLiveSources

> ListLiveSourcesResponse listLiveSources(sourceLocationName, opts)



Lists the live sources contained in a source location. A source represents a piece of content.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let sourceLocationName = "sourceLocationName_example"; // String | The name of the source location associated with this Live Sources list.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of live sources that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> live sources, use the value of <code>NextToken</code> in the response to get the next page of results.
  'nextToken': "nextToken_example", // String | Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listLiveSources(sourceLocationName, opts, (error, data, response) => {
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
 **sourceLocationName** | **String**| The name of the source location associated with this Live Sources list. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of live sources that you want MediaTailor to return in response to the current request. If there are more than &lt;code&gt;MaxResults&lt;/code&gt; live sources, use the value of &lt;code&gt;NextToken&lt;/code&gt; in the response to get the next page of results. | [optional] 
 **nextToken** | **String**| Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListLiveSourcesResponse**](ListLiveSourcesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPlaybackConfigurations

> ListPlaybackConfigurationsResponse listPlaybackConfigurations(opts)



Retrieves existing playback configurations. For information about MediaTailor configurations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html\&quot;&gt;Working with Configurations in AWS Elemental MediaTailor&lt;/a&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of playback configurations that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> playback configurations, use the value of <code>NextToken</code> in the response to get the next page of results.
  'nextToken': "nextToken_example" // String | Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
};
apiInstance.listPlaybackConfigurations(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of playback configurations that you want MediaTailor to return in response to the current request. If there are more than &lt;code&gt;MaxResults&lt;/code&gt; playback configurations, use the value of &lt;code&gt;NextToken&lt;/code&gt; in the response to get the next page of results. | [optional] 
 **nextToken** | **String**| Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results. | [optional] 

### Return type

[**ListPlaybackConfigurationsResponse**](ListPlaybackConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPrefetchSchedules

> ListPrefetchSchedulesResponse listPrefetchSchedules(playbackConfigurationName, listPrefetchSchedulesRequest, opts)



Lists the prefetch schedules for a playback configuration.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let playbackConfigurationName = "playbackConfigurationName_example"; // String | Retrieves the prefetch schedule(s) for a specific playback configuration.
let listPrefetchSchedulesRequest = new AwsMediaTailor.ListPrefetchSchedulesRequest(); // ListPrefetchSchedulesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listPrefetchSchedules(playbackConfigurationName, listPrefetchSchedulesRequest, opts, (error, data, response) => {
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
 **playbackConfigurationName** | **String**| Retrieves the prefetch schedule(s) for a specific playback configuration. | 
 **listPrefetchSchedulesRequest** | [**ListPrefetchSchedulesRequest**](ListPrefetchSchedulesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListPrefetchSchedulesResponse**](ListPrefetchSchedulesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listSourceLocations

> ListSourceLocationsResponse listSourceLocations(opts)



Lists the source locations for a channel. A source location defines the host server URL, and contains a list of sources.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number |  The maximum number of source locations that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> source locations, use the value of <code>NextToken</code> in the response to get the next page of results.
  'nextToken': "nextToken_example", // String | Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listSourceLocations(opts, (error, data, response) => {
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
 **maxResults** | **Number**|  The maximum number of source locations that you want MediaTailor to return in response to the current request. If there are more than &lt;code&gt;MaxResults&lt;/code&gt; source locations, use the value of &lt;code&gt;NextToken&lt;/code&gt; in the response to get the next page of results. | [optional] 
 **nextToken** | **String**| Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListSourceLocationsResponse**](ListSourceLocationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



A list of tags that are associated with this resource. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\&quot;&gt;Tagging AWS Elemental MediaTailor Resources&lt;/a&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) associated with this resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) associated with this resource. | 
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


## listVodSources

> ListVodSourcesResponse listVodSources(sourceLocationName, opts)



Lists the VOD sources contained in a source location. A source represents a piece of content.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let sourceLocationName = "sourceLocationName_example"; // String | The name of the source location associated with this VOD Source list.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number |  The maximum number of VOD sources that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> VOD sources, use the value of <code>NextToken</code> in the response to get the next page of results.
  'nextToken': "nextToken_example", // String | Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listVodSources(sourceLocationName, opts, (error, data, response) => {
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
 **sourceLocationName** | **String**| The name of the source location associated with this VOD Source list. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**|  The maximum number of VOD sources that you want MediaTailor to return in response to the current request. If there are more than &lt;code&gt;MaxResults&lt;/code&gt; VOD sources, use the value of &lt;code&gt;NextToken&lt;/code&gt; in the response to get the next page of results. | [optional] 
 **nextToken** | **String**| Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListVodSourcesResponse**](ListVodSourcesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putChannelPolicy

> Object putChannelPolicy(channelName, putChannelPolicyRequest, opts)



Creates an IAM policy for the channel. IAM policies are used to control access to your channel.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let channelName = "channelName_example"; // String | The channel name associated with this Channel Policy.
let putChannelPolicyRequest = new AwsMediaTailor.PutChannelPolicyRequest(); // PutChannelPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putChannelPolicy(channelName, putChannelPolicyRequest, opts, (error, data, response) => {
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
 **channelName** | **String**| The channel name associated with this Channel Policy. | 
 **putChannelPolicyRequest** | [**PutChannelPolicyRequest**](PutChannelPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putPlaybackConfiguration

> PutPlaybackConfigurationResponse putPlaybackConfiguration(putPlaybackConfigurationRequest, opts)



Creates a playback configuration. For information about MediaTailor configurations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html\&quot;&gt;Working with configurations in AWS Elemental MediaTailor&lt;/a&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let putPlaybackConfigurationRequest = new AwsMediaTailor.PutPlaybackConfigurationRequest(); // PutPlaybackConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putPlaybackConfiguration(putPlaybackConfigurationRequest, opts, (error, data, response) => {
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
 **putPlaybackConfigurationRequest** | [**PutPlaybackConfigurationRequest**](PutPlaybackConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutPlaybackConfigurationResponse**](PutPlaybackConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startChannel

> Object startChannel(channelName, opts)



Starts a channel. For information about MediaTailor channels, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html\&quot;&gt;Working with channels&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let channelName = "channelName_example"; // String | The name of the channel.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startChannel(channelName, opts, (error, data, response) => {
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
 **channelName** | **String**| The name of the channel. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stopChannel

> Object stopChannel(channelName, opts)



Stops a channel. For information about MediaTailor channels, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html\&quot;&gt;Working with channels&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let channelName = "channelName_example"; // String | The name of the channel.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopChannel(channelName, opts, (error, data, response) => {
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
 **channelName** | **String**| The name of the channel. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagResource

> tagResource(resourceArn, tagResourceRequest, opts)



The resource to tag. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\&quot;&gt;Tagging AWS Elemental MediaTailor Resources&lt;/a&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) associated with the resource.
let tagResourceRequest = new AwsMediaTailor.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(resourceArn, tagResourceRequest, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) associated with the resource. | 
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

> untagResource(resourceArn, tagKeys, opts)



The resource to untag.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource to untag.
let tagKeys = ["null"]; // [String] | The tag keys associated with the resource.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(resourceArn, tagKeys, opts, (error, data, response) => {
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource to untag. | 
 **tagKeys** | [**[String]**](String.md)| The tag keys associated with the resource. | 
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


## updateChannel

> UpdateChannelResponse updateChannel(channelName, updateChannelRequest, opts)



Updates a channel. For information about MediaTailor channels, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-channels.html\&quot;&gt;Working with channels&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let channelName = "channelName_example"; // String | The name of the channel.
let updateChannelRequest = new AwsMediaTailor.UpdateChannelRequest(); // UpdateChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateChannel(channelName, updateChannelRequest, opts, (error, data, response) => {
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
 **channelName** | **String**| The name of the channel. | 
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


## updateLiveSource

> UpdateLiveSourceResponse updateLiveSource(liveSourceName, sourceLocationName, updateLiveSourceRequest, opts)



Updates a live source&#39;s configuration.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let liveSourceName = "liveSourceName_example"; // String | The name of the live source.
let sourceLocationName = "sourceLocationName_example"; // String | The name of the source location associated with this Live Source.
let updateLiveSourceRequest = new AwsMediaTailor.UpdateLiveSourceRequest(); // UpdateLiveSourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateLiveSource(liveSourceName, sourceLocationName, updateLiveSourceRequest, opts, (error, data, response) => {
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
 **liveSourceName** | **String**| The name of the live source. | 
 **sourceLocationName** | **String**| The name of the source location associated with this Live Source. | 
 **updateLiveSourceRequest** | [**UpdateLiveSourceRequest**](UpdateLiveSourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateLiveSourceResponse**](UpdateLiveSourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateProgram

> UpdateProgramResponse updateProgram(channelName, programName, updateProgramRequest, opts)



Updates a program within a channel.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let channelName = "channelName_example"; // String | The name of the channel for this Program.
let programName = "programName_example"; // String | The name of the Program.
let updateProgramRequest = new AwsMediaTailor.UpdateProgramRequest(); // UpdateProgramRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateProgram(channelName, programName, updateProgramRequest, opts, (error, data, response) => {
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
 **channelName** | **String**| The name of the channel for this Program. | 
 **programName** | **String**| The name of the Program. | 
 **updateProgramRequest** | [**UpdateProgramRequest**](UpdateProgramRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateProgramResponse**](UpdateProgramResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSourceLocation

> UpdateSourceLocationResponse updateSourceLocation(sourceLocationName, updateSourceLocationRequest, opts)



Updates a source location. A source location is a container for sources. For more information about source locations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html\&quot;&gt;Working with source locations&lt;/a&gt; in the &lt;i&gt;MediaTailor User Guide&lt;/i&gt;.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let sourceLocationName = "sourceLocationName_example"; // String | The name of the source location.
let updateSourceLocationRequest = new AwsMediaTailor.UpdateSourceLocationRequest(); // UpdateSourceLocationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSourceLocation(sourceLocationName, updateSourceLocationRequest, opts, (error, data, response) => {
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
 **sourceLocationName** | **String**| The name of the source location. | 
 **updateSourceLocationRequest** | [**UpdateSourceLocationRequest**](UpdateSourceLocationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSourceLocationResponse**](UpdateSourceLocationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateVodSource

> UpdateVodSourceResponse updateVodSource(sourceLocationName, vodSourceName, updateLiveSourceRequest, opts)



Updates a VOD source&#39;s configuration.

### Example

```javascript
import AwsMediaTailor from 'aws_media_tailor';
let defaultClient = AwsMediaTailor.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMediaTailor.DefaultApi();
let sourceLocationName = "sourceLocationName_example"; // String | The name of the source location associated with this VOD Source.
let vodSourceName = "vodSourceName_example"; // String | The name of the VOD source.
let updateLiveSourceRequest = new AwsMediaTailor.UpdateLiveSourceRequest(); // UpdateLiveSourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateVodSource(sourceLocationName, vodSourceName, updateLiveSourceRequest, opts, (error, data, response) => {
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
 **sourceLocationName** | **String**| The name of the source location associated with this VOD Source. | 
 **vodSourceName** | **String**| The name of the VOD source. | 
 **updateLiveSourceRequest** | [**UpdateLiveSourceRequest**](UpdateLiveSourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateVodSourceResponse**](UpdateVodSourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

