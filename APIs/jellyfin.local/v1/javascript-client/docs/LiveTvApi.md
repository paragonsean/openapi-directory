# JellyfinApi.LiveTvApi

All URIs are relative to *http://jellyfin.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addListingProvider**](LiveTvApi.md#addListingProvider) | **POST** /LiveTv/ListingProviders | Adds a listings provider.
[**addTunerHost**](LiveTvApi.md#addTunerHost) | **POST** /LiveTv/TunerHosts | Adds a tuner host.
[**cancelSeriesTimer**](LiveTvApi.md#cancelSeriesTimer) | **DELETE** /LiveTv/SeriesTimers/{timerId} | Cancels a live tv series timer.
[**cancelTimer**](LiveTvApi.md#cancelTimer) | **DELETE** /LiveTv/Timers/{timerId} | Cancels a live tv timer.
[**createSeriesTimer**](LiveTvApi.md#createSeriesTimer) | **POST** /LiveTv/SeriesTimers | Creates a live tv series timer.
[**createTimer**](LiveTvApi.md#createTimer) | **POST** /LiveTv/Timers | Creates a live tv timer.
[**deleteListingProvider**](LiveTvApi.md#deleteListingProvider) | **DELETE** /LiveTv/ListingProviders | Delete listing provider.
[**deleteRecording**](LiveTvApi.md#deleteRecording) | **DELETE** /LiveTv/Recordings/{recordingId} | Deletes a live tv recording.
[**deleteTunerHost**](LiveTvApi.md#deleteTunerHost) | **DELETE** /LiveTv/TunerHosts | Deletes a tuner host.
[**discoverTuners**](LiveTvApi.md#discoverTuners) | **GET** /LiveTv/Tuners/Discover | Discover tuners.
[**discvoverTuners**](LiveTvApi.md#discvoverTuners) | **GET** /LiveTv/Tuners/Discvover | Discover tuners.
[**getChannel**](LiveTvApi.md#getChannel) | **GET** /LiveTv/Channels/{channelId} | Gets a live tv channel.
[**getChannelMappingOptions**](LiveTvApi.md#getChannelMappingOptions) | **GET** /LiveTv/ChannelMappingOptions | Get channel mapping options.
[**getDefaultListingProvider**](LiveTvApi.md#getDefaultListingProvider) | **GET** /LiveTv/ListingProviders/Default | Gets default listings provider info.
[**getDefaultTimer**](LiveTvApi.md#getDefaultTimer) | **GET** /LiveTv/Timers/Defaults | Gets the default values for a new timer.
[**getGuideInfo**](LiveTvApi.md#getGuideInfo) | **GET** /LiveTv/GuideInfo | Get guid info.
[**getLineups**](LiveTvApi.md#getLineups) | **GET** /LiveTv/ListingProviders/Lineups | Gets available lineups.
[**getLiveRecordingFile**](LiveTvApi.md#getLiveRecordingFile) | **GET** /LiveTv/LiveRecordings/{recordingId}/stream | Gets a live tv recording stream.
[**getLiveStreamFile**](LiveTvApi.md#getLiveStreamFile) | **GET** /LiveTv/LiveStreamFiles/{streamId}/stream.{container} | Gets a live tv channel stream.
[**getLiveTvChannels**](LiveTvApi.md#getLiveTvChannels) | **GET** /LiveTv/Channels | Gets available live tv channels.
[**getLiveTvInfo**](LiveTvApi.md#getLiveTvInfo) | **GET** /LiveTv/Info | Gets available live tv services.
[**getLiveTvPrograms**](LiveTvApi.md#getLiveTvPrograms) | **GET** /LiveTv/Programs | Gets available live tv epgs.
[**getProgram**](LiveTvApi.md#getProgram) | **GET** /LiveTv/Programs/{programId} | Gets a live tv program.
[**getPrograms**](LiveTvApi.md#getPrograms) | **POST** /LiveTv/Programs | Gets available live tv epgs.
[**getRecommendedPrograms**](LiveTvApi.md#getRecommendedPrograms) | **GET** /LiveTv/Programs/Recommended | Gets recommended live tv epgs.
[**getRecording**](LiveTvApi.md#getRecording) | **GET** /LiveTv/Recordings/{recordingId} | Gets a live tv recording.
[**getRecordingFolders**](LiveTvApi.md#getRecordingFolders) | **GET** /LiveTv/Recordings/Folders | Gets recording folders.
[**getRecordingGroup**](LiveTvApi.md#getRecordingGroup) | **GET** /LiveTv/Recordings/Groups/{groupId} | Get recording group.
[**getRecordingGroups**](LiveTvApi.md#getRecordingGroups) | **GET** /LiveTv/Recordings/Groups | Gets live tv recording groups.
[**getRecordings**](LiveTvApi.md#getRecordings) | **GET** /LiveTv/Recordings | Gets live tv recordings.
[**getRecordingsSeries**](LiveTvApi.md#getRecordingsSeries) | **GET** /LiveTv/Recordings/Series | Gets live tv recording series.
[**getSchedulesDirectCountries**](LiveTvApi.md#getSchedulesDirectCountries) | **GET** /LiveTv/ListingProviders/SchedulesDirect/Countries | Gets available countries.
[**getSeriesTimer**](LiveTvApi.md#getSeriesTimer) | **GET** /LiveTv/SeriesTimers/{timerId} | Gets a live tv series timer.
[**getSeriesTimers**](LiveTvApi.md#getSeriesTimers) | **GET** /LiveTv/SeriesTimers | Gets live tv series timers.
[**getTimer**](LiveTvApi.md#getTimer) | **GET** /LiveTv/Timers/{timerId} | Gets a timer.
[**getTimers**](LiveTvApi.md#getTimers) | **GET** /LiveTv/Timers | Gets the live tv timers.
[**getTunerHostTypes**](LiveTvApi.md#getTunerHostTypes) | **GET** /LiveTv/TunerHosts/Types | Get tuner host types.
[**resetTuner**](LiveTvApi.md#resetTuner) | **POST** /LiveTv/Tuners/{tunerId}/Reset | Resets a tv tuner.
[**setChannelMapping**](LiveTvApi.md#setChannelMapping) | **POST** /LiveTv/ChannelMappings | Set channel mappings.
[**updateSeriesTimer**](LiveTvApi.md#updateSeriesTimer) | **POST** /LiveTv/SeriesTimers/{timerId} | Updates a live tv series timer.
[**updateTimer**](LiveTvApi.md#updateTimer) | **POST** /LiveTv/Timers/{timerId} | Updates a live tv timer.



## addListingProvider

> ListingsProviderInfo addListingProvider(opts)

Adds a listings provider.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'pw': "pw_example", // String | Password.
  'validateListings': false, // Boolean | Validate listings.
  'validateLogin': false, // Boolean | Validate login.
  'listingsProviderInfo': new JellyfinApi.ListingsProviderInfo() // ListingsProviderInfo | New listings info.
};
apiInstance.addListingProvider(opts, (error, data, response) => {
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
 **pw** | **String**| Password. | [optional] 
 **validateListings** | **Boolean**| Validate listings. | [optional] [default to false]
 **validateLogin** | **Boolean**| Validate login. | [optional] [default to false]
 **listingsProviderInfo** | [**ListingsProviderInfo**](ListingsProviderInfo.md)| New listings info. | [optional] 

### Return type

[**ListingsProviderInfo**](ListingsProviderInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## addTunerHost

> TunerHostInfo addTunerHost(opts)

Adds a tuner host.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'tunerHostInfo': new JellyfinApi.TunerHostInfo() // TunerHostInfo | New tuner host.
};
apiInstance.addTunerHost(opts, (error, data, response) => {
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
 **tunerHostInfo** | [**TunerHostInfo**](TunerHostInfo.md)| New tuner host. | [optional] 

### Return type

[**TunerHostInfo**](TunerHostInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## cancelSeriesTimer

> cancelSeriesTimer(timerId)

Cancels a live tv series timer.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let timerId = "timerId_example"; // String | Timer id.
apiInstance.cancelSeriesTimer(timerId, (error, data, response) => {
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
 **timerId** | **String**| Timer id. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## cancelTimer

> cancelTimer(timerId)

Cancels a live tv timer.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let timerId = "timerId_example"; // String | Timer id.
apiInstance.cancelTimer(timerId, (error, data, response) => {
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
 **timerId** | **String**| Timer id. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createSeriesTimer

> createSeriesTimer(opts)

Creates a live tv series timer.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'seriesTimerInfoDto': new JellyfinApi.SeriesTimerInfoDto() // SeriesTimerInfoDto | New series timer info.
};
apiInstance.createSeriesTimer(opts, (error, data, response) => {
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
 **seriesTimerInfoDto** | [**SeriesTimerInfoDto**](SeriesTimerInfoDto.md)| New series timer info. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined


## createTimer

> createTimer(opts)

Creates a live tv timer.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'timerInfoDto': new JellyfinApi.TimerInfoDto() // TimerInfoDto | New timer info.
};
apiInstance.createTimer(opts, (error, data, response) => {
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
 **timerInfoDto** | [**TimerInfoDto**](TimerInfoDto.md)| New timer info. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined


## deleteListingProvider

> deleteListingProvider(opts)

Delete listing provider.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'id': "id_example" // String | Listing provider id.
};
apiInstance.deleteListingProvider(opts, (error, data, response) => {
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
 **id** | **String**| Listing provider id. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteRecording

> deleteRecording(recordingId)

Deletes a live tv recording.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let recordingId = "recordingId_example"; // String | Recording id.
apiInstance.deleteRecording(recordingId, (error, data, response) => {
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
 **recordingId** | **String**| Recording id. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## deleteTunerHost

> deleteTunerHost(opts)

Deletes a tuner host.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'id': "id_example" // String | Tuner host id.
};
apiInstance.deleteTunerHost(opts, (error, data, response) => {
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
 **id** | **String**| Tuner host id. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## discoverTuners

> [TunerHostInfo] discoverTuners(opts)

Discover tuners.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'newDevicesOnly': false // Boolean | Only discover new tuners.
};
apiInstance.discoverTuners(opts, (error, data, response) => {
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
 **newDevicesOnly** | **Boolean**| Only discover new tuners. | [optional] [default to false]

### Return type

[**[TunerHostInfo]**](TunerHostInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## discvoverTuners

> [TunerHostInfo] discvoverTuners(opts)

Discover tuners.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'newDevicesOnly': false // Boolean | Only discover new tuners.
};
apiInstance.discvoverTuners(opts, (error, data, response) => {
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
 **newDevicesOnly** | **Boolean**| Only discover new tuners. | [optional] [default to false]

### Return type

[**[TunerHostInfo]**](TunerHostInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getChannel

> BaseItemDto getChannel(channelId, opts)

Gets a live tv channel.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let channelId = "channelId_example"; // String | Channel id.
let opts = {
  'userId': "userId_example" // String | Optional. Attach user data.
};
apiInstance.getChannel(channelId, opts, (error, data, response) => {
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
 **channelId** | **String**| Channel id. | 
 **userId** | **String**| Optional. Attach user data. | [optional] 

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getChannelMappingOptions

> ChannelMappingOptionsDto getChannelMappingOptions(opts)

Get channel mapping options.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'providerId': "providerId_example" // String | Provider id.
};
apiInstance.getChannelMappingOptions(opts, (error, data, response) => {
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
 **providerId** | **String**| Provider id. | [optional] 

### Return type

[**ChannelMappingOptionsDto**](ChannelMappingOptionsDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getDefaultListingProvider

> ListingsProviderInfo getDefaultListingProvider()

Gets default listings provider info.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
apiInstance.getDefaultListingProvider((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ListingsProviderInfo**](ListingsProviderInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getDefaultTimer

> SeriesTimerInfoDto getDefaultTimer(opts)

Gets the default values for a new timer.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'programId': "programId_example" // String | Optional. To attach default values based on a program.
};
apiInstance.getDefaultTimer(opts, (error, data, response) => {
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
 **programId** | **String**| Optional. To attach default values based on a program. | [optional] 

### Return type

[**SeriesTimerInfoDto**](SeriesTimerInfoDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getGuideInfo

> GuideInfo getGuideInfo()

Get guid info.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
apiInstance.getGuideInfo((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GuideInfo**](GuideInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getLineups

> [NameIdPair] getLineups(opts)

Gets available lineups.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'id': "id_example", // String | Provider id.
  'type': "type_example", // String | Provider type.
  'location': "location_example", // String | Location.
  'country': "country_example" // String | Country.
};
apiInstance.getLineups(opts, (error, data, response) => {
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
 **id** | **String**| Provider id. | [optional] 
 **type** | **String**| Provider type. | [optional] 
 **location** | **String**| Location. | [optional] 
 **country** | **String**| Country. | [optional] 

### Return type

[**[NameIdPair]**](NameIdPair.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getLiveRecordingFile

> File getLiveRecordingFile(recordingId)

Gets a live tv recording stream.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.LiveTvApi();
let recordingId = "recordingId_example"; // String | Recording id.
apiInstance.getLiveRecordingFile(recordingId, (error, data, response) => {
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
 **recordingId** | **String**| Recording id. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: video/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getLiveStreamFile

> File getLiveStreamFile(streamId, container)

Gets a live tv channel stream.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';

let apiInstance = new JellyfinApi.LiveTvApi();
let streamId = "streamId_example"; // String | Stream id.
let container = "container_example"; // String | Container type.
apiInstance.getLiveStreamFile(streamId, container, (error, data, response) => {
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
 **streamId** | **String**| Stream id. | 
 **container** | **String**| Container type. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: video/*, application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getLiveTvChannels

> BaseItemDtoQueryResult getLiveTvChannels(opts)

Gets available live tv channels.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'type': new JellyfinApi.ChannelType(), // ChannelType | Optional. Filter by channel type.
  'userId': "userId_example", // String | Optional. Filter by user and attach user data.
  'startIndex': 56, // Number | Optional. The record index to start at. All items with a lower index will be dropped from the results.
  'isMovie': true, // Boolean | Optional. Filter for movies.
  'isSeries': true, // Boolean | Optional. Filter for series.
  'isNews': true, // Boolean | Optional. Filter for news.
  'isKids': true, // Boolean | Optional. Filter for kids.
  'isSports': true, // Boolean | Optional. Filter for sports.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'isFavorite': true, // Boolean | Optional. Filter by channels that are favorites, or not.
  'isLiked': true, // Boolean | Optional. Filter by channels that are liked, or not.
  'isDisliked': true, // Boolean | Optional. Filter by channels that are disliked, or not.
  'enableImages': true, // Boolean | Optional. Include image information in output.
  'imageTypeLimit': 56, // Number | Optional. The max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()], // [ImageType] | \"Optional. The image types to include in the output.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'enableUserData': true, // Boolean | Optional. Include user data.
  'sortBy': ["null"], // [String] | Optional. Key to sort by.
  'sortOrder': new JellyfinApi.SortOrder(), // SortOrder | Optional. Sort order.
  'enableFavoriteSorting': false, // Boolean | Optional. Incorporate favorite and like status into channel sorting.
  'addCurrentProgram': true // Boolean | Optional. Adds current program info to each channel.
};
apiInstance.getLiveTvChannels(opts, (error, data, response) => {
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
 **type** | [**ChannelType**](.md)| Optional. Filter by channel type. | [optional] 
 **userId** | **String**| Optional. Filter by user and attach user data. | [optional] 
 **startIndex** | **Number**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **isMovie** | **Boolean**| Optional. Filter for movies. | [optional] 
 **isSeries** | **Boolean**| Optional. Filter for series. | [optional] 
 **isNews** | **Boolean**| Optional. Filter for news. | [optional] 
 **isKids** | **Boolean**| Optional. Filter for kids. | [optional] 
 **isSports** | **Boolean**| Optional. Filter for sports. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **isFavorite** | **Boolean**| Optional. Filter by channels that are favorites, or not. | [optional] 
 **isLiked** | **Boolean**| Optional. Filter by channels that are liked, or not. | [optional] 
 **isDisliked** | **Boolean**| Optional. Filter by channels that are disliked, or not. | [optional] 
 **enableImages** | **Boolean**| Optional. Include image information in output. | [optional] 
 **imageTypeLimit** | **Number**| Optional. The max number of images to return, per image type. | [optional] 
 **enableImageTypes** | [**[ImageType]**](ImageType.md)| \&quot;Optional. The image types to include in the output. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **enableUserData** | **Boolean**| Optional. Include user data. | [optional] 
 **sortBy** | [**[String]**](String.md)| Optional. Key to sort by. | [optional] 
 **sortOrder** | [**SortOrder**](.md)| Optional. Sort order. | [optional] 
 **enableFavoriteSorting** | **Boolean**| Optional. Incorporate favorite and like status into channel sorting. | [optional] [default to false]
 **addCurrentProgram** | **Boolean**| Optional. Adds current program info to each channel. | [optional] [default to true]

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getLiveTvInfo

> LiveTvInfo getLiveTvInfo()

Gets available live tv services.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
apiInstance.getLiveTvInfo((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**LiveTvInfo**](LiveTvInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getLiveTvPrograms

> BaseItemDtoQueryResult getLiveTvPrograms(opts)

Gets available live tv epgs.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'channelIds': ["null"], // [String] | The channels to return guide information for.
  'userId': "userId_example", // String | Optional. Filter by user id.
  'minStartDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. The minimum premiere start date.
  'hasAired': true, // Boolean | Optional. Filter by programs that have completed airing, or not.
  'isAiring': true, // Boolean | Optional. Filter by programs that are currently airing, or not.
  'maxStartDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. The maximum premiere start date.
  'minEndDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. The minimum premiere end date.
  'maxEndDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. The maximum premiere end date.
  'isMovie': true, // Boolean | Optional. Filter for movies.
  'isSeries': true, // Boolean | Optional. Filter for series.
  'isNews': true, // Boolean | Optional. Filter for news.
  'isKids': true, // Boolean | Optional. Filter for kids.
  'isSports': true, // Boolean | Optional. Filter for sports.
  'startIndex': 56, // Number | Optional. The record index to start at. All items with a lower index will be dropped from the results.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'sortBy': "sortBy_example", // String | Optional. Specify one or more sort orders, comma delimited. Options: Name, StartDate.
  'sortOrder': "sortOrder_example", // String | Sort Order - Ascending,Descending.
  'genres': ["null"], // [String] | The genres to return guide information for.
  'genreIds': ["null"], // [String] | The genre ids to return guide information for.
  'enableImages': true, // Boolean | Optional. Include image information in output.
  'imageTypeLimit': 56, // Number | Optional. The max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()], // [ImageType] | Optional. The image types to include in the output.
  'enableUserData': true, // Boolean | Optional. Include user data.
  'seriesTimerId': "seriesTimerId_example", // String | Optional. Filter by series timer id.
  'librarySeriesId': "librarySeriesId_example", // String | Optional. Filter by library series id.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'enableTotalRecordCount': true // Boolean | Retrieve total record count.
};
apiInstance.getLiveTvPrograms(opts, (error, data, response) => {
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
 **channelIds** | [**[String]**](String.md)| The channels to return guide information for. | [optional] 
 **userId** | **String**| Optional. Filter by user id. | [optional] 
 **minStartDate** | **Date**| Optional. The minimum premiere start date. | [optional] 
 **hasAired** | **Boolean**| Optional. Filter by programs that have completed airing, or not. | [optional] 
 **isAiring** | **Boolean**| Optional. Filter by programs that are currently airing, or not. | [optional] 
 **maxStartDate** | **Date**| Optional. The maximum premiere start date. | [optional] 
 **minEndDate** | **Date**| Optional. The minimum premiere end date. | [optional] 
 **maxEndDate** | **Date**| Optional. The maximum premiere end date. | [optional] 
 **isMovie** | **Boolean**| Optional. Filter for movies. | [optional] 
 **isSeries** | **Boolean**| Optional. Filter for series. | [optional] 
 **isNews** | **Boolean**| Optional. Filter for news. | [optional] 
 **isKids** | **Boolean**| Optional. Filter for kids. | [optional] 
 **isSports** | **Boolean**| Optional. Filter for sports. | [optional] 
 **startIndex** | **Number**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **sortBy** | **String**| Optional. Specify one or more sort orders, comma delimited. Options: Name, StartDate. | [optional] 
 **sortOrder** | **String**| Sort Order - Ascending,Descending. | [optional] 
 **genres** | [**[String]**](String.md)| The genres to return guide information for. | [optional] 
 **genreIds** | [**[String]**](String.md)| The genre ids to return guide information for. | [optional] 
 **enableImages** | **Boolean**| Optional. Include image information in output. | [optional] 
 **imageTypeLimit** | **Number**| Optional. The max number of images to return, per image type. | [optional] 
 **enableImageTypes** | [**[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **enableUserData** | **Boolean**| Optional. Include user data. | [optional] 
 **seriesTimerId** | **String**| Optional. Filter by series timer id. | [optional] 
 **librarySeriesId** | **String**| Optional. Filter by library series id. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **enableTotalRecordCount** | **Boolean**| Retrieve total record count. | [optional] [default to true]

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getProgram

> BaseItemDto getProgram(programId, opts)

Gets a live tv program.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let programId = "programId_example"; // String | Program id.
let opts = {
  'userId': "userId_example" // String | Optional. Attach user data.
};
apiInstance.getProgram(programId, opts, (error, data, response) => {
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
 **programId** | **String**| Program id. | 
 **userId** | **String**| Optional. Attach user data. | [optional] 

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getPrograms

> BaseItemDtoQueryResult getPrograms(opts)

Gets available live tv epgs.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'getProgramsDto': new JellyfinApi.GetProgramsDto() // GetProgramsDto | Request body.
};
apiInstance.getPrograms(opts, (error, data, response) => {
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
 **getProgramsDto** | [**GetProgramsDto**](GetProgramsDto.md)| Request body. | [optional] 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getRecommendedPrograms

> BaseItemDtoQueryResult getRecommendedPrograms(opts)

Gets recommended live tv epgs.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'userId': "userId_example", // String | Optional. filter by user id.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'isAiring': true, // Boolean | Optional. Filter by programs that are currently airing, or not.
  'hasAired': true, // Boolean | Optional. Filter by programs that have completed airing, or not.
  'isSeries': true, // Boolean | Optional. Filter for series.
  'isMovie': true, // Boolean | Optional. Filter for movies.
  'isNews': true, // Boolean | Optional. Filter for news.
  'isKids': true, // Boolean | Optional. Filter for kids.
  'isSports': true, // Boolean | Optional. Filter for sports.
  'enableImages': true, // Boolean | Optional. Include image information in output.
  'imageTypeLimit': 56, // Number | Optional. The max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()], // [ImageType] | Optional. The image types to include in the output.
  'genreIds': ["null"], // [String] | The genres to return guide information for.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'enableUserData': true, // Boolean | Optional. include user data.
  'enableTotalRecordCount': true // Boolean | Retrieve total record count.
};
apiInstance.getRecommendedPrograms(opts, (error, data, response) => {
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
 **userId** | **String**| Optional. filter by user id. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **isAiring** | **Boolean**| Optional. Filter by programs that are currently airing, or not. | [optional] 
 **hasAired** | **Boolean**| Optional. Filter by programs that have completed airing, or not. | [optional] 
 **isSeries** | **Boolean**| Optional. Filter for series. | [optional] 
 **isMovie** | **Boolean**| Optional. Filter for movies. | [optional] 
 **isNews** | **Boolean**| Optional. Filter for news. | [optional] 
 **isKids** | **Boolean**| Optional. Filter for kids. | [optional] 
 **isSports** | **Boolean**| Optional. Filter for sports. | [optional] 
 **enableImages** | **Boolean**| Optional. Include image information in output. | [optional] 
 **imageTypeLimit** | **Number**| Optional. The max number of images to return, per image type. | [optional] 
 **enableImageTypes** | [**[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **genreIds** | [**[String]**](String.md)| The genres to return guide information for. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **enableUserData** | **Boolean**| Optional. include user data. | [optional] 
 **enableTotalRecordCount** | **Boolean**| Retrieve total record count. | [optional] [default to true]

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getRecording

> BaseItemDto getRecording(recordingId, opts)

Gets a live tv recording.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let recordingId = "recordingId_example"; // String | Recording id.
let opts = {
  'userId': "userId_example" // String | Optional. Attach user data.
};
apiInstance.getRecording(recordingId, opts, (error, data, response) => {
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
 **recordingId** | **String**| Recording id. | 
 **userId** | **String**| Optional. Attach user data. | [optional] 

### Return type

[**BaseItemDto**](BaseItemDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getRecordingFolders

> BaseItemDtoQueryResult getRecordingFolders(opts)

Gets recording folders.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'userId': "userId_example" // String | Optional. Filter by user and attach user data.
};
apiInstance.getRecordingFolders(opts, (error, data, response) => {
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
 **userId** | **String**| Optional. Filter by user and attach user data. | [optional] 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getRecordingGroup

> getRecordingGroup(groupId)

Get recording group.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let groupId = "groupId_example"; // String | Group id.
apiInstance.getRecordingGroup(groupId, (error, data, response) => {
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
 **groupId** | **String**| Group id. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getRecordingGroups

> BaseItemDtoQueryResult getRecordingGroups(opts)

Gets live tv recording groups.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'userId': "userId_example" // String | Optional. Filter by user and attach user data.
};
apiInstance.getRecordingGroups(opts, (error, data, response) => {
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
 **userId** | **String**| Optional. Filter by user and attach user data. | [optional] 

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getRecordings

> BaseItemDtoQueryResult getRecordings(opts)

Gets live tv recordings.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'channelId': "channelId_example", // String | Optional. Filter by channel id.
  'userId': "userId_example", // String | Optional. Filter by user and attach user data.
  'startIndex': 56, // Number | Optional. The record index to start at. All items with a lower index will be dropped from the results.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'status': new JellyfinApi.RecordingStatus(), // RecordingStatus | Optional. Filter by recording status.
  'isInProgress': true, // Boolean | Optional. Filter by recordings that are in progress, or not.
  'seriesTimerId': "seriesTimerId_example", // String | Optional. Filter by recordings belonging to a series timer.
  'enableImages': true, // Boolean | Optional. Include image information in output.
  'imageTypeLimit': 56, // Number | Optional. The max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()], // [ImageType] | Optional. The image types to include in the output.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'enableUserData': true, // Boolean | Optional. Include user data.
  'isMovie': true, // Boolean | Optional. Filter for movies.
  'isSeries': true, // Boolean | Optional. Filter for series.
  'isKids': true, // Boolean | Optional. Filter for kids.
  'isSports': true, // Boolean | Optional. Filter for sports.
  'isNews': true, // Boolean | Optional. Filter for news.
  'isLibraryItem': true, // Boolean | Optional. Filter for is library item.
  'enableTotalRecordCount': true // Boolean | Optional. Return total record count.
};
apiInstance.getRecordings(opts, (error, data, response) => {
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
 **channelId** | **String**| Optional. Filter by channel id. | [optional] 
 **userId** | **String**| Optional. Filter by user and attach user data. | [optional] 
 **startIndex** | **Number**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **status** | [**RecordingStatus**](.md)| Optional. Filter by recording status. | [optional] 
 **isInProgress** | **Boolean**| Optional. Filter by recordings that are in progress, or not. | [optional] 
 **seriesTimerId** | **String**| Optional. Filter by recordings belonging to a series timer. | [optional] 
 **enableImages** | **Boolean**| Optional. Include image information in output. | [optional] 
 **imageTypeLimit** | **Number**| Optional. The max number of images to return, per image type. | [optional] 
 **enableImageTypes** | [**[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **enableUserData** | **Boolean**| Optional. Include user data. | [optional] 
 **isMovie** | **Boolean**| Optional. Filter for movies. | [optional] 
 **isSeries** | **Boolean**| Optional. Filter for series. | [optional] 
 **isKids** | **Boolean**| Optional. Filter for kids. | [optional] 
 **isSports** | **Boolean**| Optional. Filter for sports. | [optional] 
 **isNews** | **Boolean**| Optional. Filter for news. | [optional] 
 **isLibraryItem** | **Boolean**| Optional. Filter for is library item. | [optional] 
 **enableTotalRecordCount** | **Boolean**| Optional. Return total record count. | [optional] [default to true]

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getRecordingsSeries

> BaseItemDtoQueryResult getRecordingsSeries(opts)

Gets live tv recording series.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'channelId': "channelId_example", // String | Optional. Filter by channel id.
  'userId': "userId_example", // String | Optional. Filter by user and attach user data.
  'groupId': "groupId_example", // String | Optional. Filter by recording group.
  'startIndex': 56, // Number | Optional. The record index to start at. All items with a lower index will be dropped from the results.
  'limit': 56, // Number | Optional. The maximum number of records to return.
  'status': new JellyfinApi.RecordingStatus(), // RecordingStatus | Optional. Filter by recording status.
  'isInProgress': true, // Boolean | Optional. Filter by recordings that are in progress, or not.
  'seriesTimerId': "seriesTimerId_example", // String | Optional. Filter by recordings belonging to a series timer.
  'enableImages': true, // Boolean | Optional. Include image information in output.
  'imageTypeLimit': 56, // Number | Optional. The max number of images to return, per image type.
  'enableImageTypes': [new JellyfinApi.ImageType()], // [ImageType] | Optional. The image types to include in the output.
  'fields': [new JellyfinApi.ItemFields()], // [ItemFields] | Optional. Specify additional fields of information to return in the output.
  'enableUserData': true, // Boolean | Optional. Include user data.
  'enableTotalRecordCount': true // Boolean | Optional. Return total record count.
};
apiInstance.getRecordingsSeries(opts, (error, data, response) => {
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
 **channelId** | **String**| Optional. Filter by channel id. | [optional] 
 **userId** | **String**| Optional. Filter by user and attach user data. | [optional] 
 **groupId** | **String**| Optional. Filter by recording group. | [optional] 
 **startIndex** | **Number**| Optional. The record index to start at. All items with a lower index will be dropped from the results. | [optional] 
 **limit** | **Number**| Optional. The maximum number of records to return. | [optional] 
 **status** | [**RecordingStatus**](.md)| Optional. Filter by recording status. | [optional] 
 **isInProgress** | **Boolean**| Optional. Filter by recordings that are in progress, or not. | [optional] 
 **seriesTimerId** | **String**| Optional. Filter by recordings belonging to a series timer. | [optional] 
 **enableImages** | **Boolean**| Optional. Include image information in output. | [optional] 
 **imageTypeLimit** | **Number**| Optional. The max number of images to return, per image type. | [optional] 
 **enableImageTypes** | [**[ImageType]**](ImageType.md)| Optional. The image types to include in the output. | [optional] 
 **fields** | [**[ItemFields]**](ItemFields.md)| Optional. Specify additional fields of information to return in the output. | [optional] 
 **enableUserData** | **Boolean**| Optional. Include user data. | [optional] 
 **enableTotalRecordCount** | **Boolean**| Optional. Return total record count. | [optional] [default to true]

### Return type

[**BaseItemDtoQueryResult**](BaseItemDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getSchedulesDirectCountries

> File getSchedulesDirectCountries()

Gets available countries.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
apiInstance.getSchedulesDirectCountries((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**File**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSeriesTimer

> SeriesTimerInfoDto getSeriesTimer(timerId)

Gets a live tv series timer.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let timerId = "timerId_example"; // String | Timer id.
apiInstance.getSeriesTimer(timerId, (error, data, response) => {
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
 **timerId** | **String**| Timer id. | 

### Return type

[**SeriesTimerInfoDto**](SeriesTimerInfoDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getSeriesTimers

> SeriesTimerInfoDtoQueryResult getSeriesTimers(opts)

Gets live tv series timers.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'sortBy': "sortBy_example", // String | Optional. Sort by SortName or Priority.
  'sortOrder': new JellyfinApi.SortOrder() // SortOrder | Optional. Sort in Ascending or Descending order.
};
apiInstance.getSeriesTimers(opts, (error, data, response) => {
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
 **sortBy** | **String**| Optional. Sort by SortName or Priority. | [optional] 
 **sortOrder** | [**SortOrder**](.md)| Optional. Sort in Ascending or Descending order. | [optional] 

### Return type

[**SeriesTimerInfoDtoQueryResult**](SeriesTimerInfoDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getTimer

> TimerInfoDto getTimer(timerId)

Gets a timer.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let timerId = "timerId_example"; // String | Timer id.
apiInstance.getTimer(timerId, (error, data, response) => {
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
 **timerId** | **String**| Timer id. | 

### Return type

[**TimerInfoDto**](TimerInfoDto.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getTimers

> TimerInfoDtoQueryResult getTimers(opts)

Gets the live tv timers.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let opts = {
  'channelId': "channelId_example", // String | Optional. Filter by channel id.
  'seriesTimerId': "seriesTimerId_example", // String | Optional. Filter by timers belonging to a series timer.
  'isActive': true, // Boolean | Optional. Filter by timers that are active.
  'isScheduled': true // Boolean | Optional. Filter by timers that are scheduled.
};
apiInstance.getTimers(opts, (error, data, response) => {
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
 **channelId** | **String**| Optional. Filter by channel id. | [optional] 
 **seriesTimerId** | **String**| Optional. Filter by timers belonging to a series timer. | [optional] 
 **isActive** | **Boolean**| Optional. Filter by timers that are active. | [optional] 
 **isScheduled** | **Boolean**| Optional. Filter by timers that are scheduled. | [optional] 

### Return type

[**TimerInfoDtoQueryResult**](TimerInfoDtoQueryResult.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## getTunerHostTypes

> [NameIdPair] getTunerHostTypes()

Get tuner host types.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
apiInstance.getTunerHostTypes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[NameIdPair]**](NameIdPair.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## resetTuner

> resetTuner(tunerId)

Resets a tv tuner.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let tunerId = "tunerId_example"; // String | Tuner id.
apiInstance.resetTuner(tunerId, (error, data, response) => {
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
 **tunerId** | **String**| Tuner id. | 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setChannelMapping

> TunerChannelMapping setChannelMapping(setChannelMappingDto)

Set channel mappings.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let setChannelMappingDto = new JellyfinApi.SetChannelMappingDto(); // SetChannelMappingDto | The set channel mapping dto.
apiInstance.setChannelMapping(setChannelMappingDto, (error, data, response) => {
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
 **setChannelMappingDto** | [**SetChannelMappingDto**](SetChannelMappingDto.md)| The set channel mapping dto. | 

### Return type

[**TunerChannelMapping**](TunerChannelMapping.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, application/json; profile=CamelCase, application/json; profile=PascalCase


## updateSeriesTimer

> updateSeriesTimer(timerId, opts)

Updates a live tv series timer.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let timerId = "timerId_example"; // String | Timer id.
let opts = {
  'seriesTimerInfoDto': new JellyfinApi.SeriesTimerInfoDto() // SeriesTimerInfoDto | New series timer info.
};
apiInstance.updateSeriesTimer(timerId, opts, (error, data, response) => {
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
 **timerId** | **String**| Timer id. | 
 **seriesTimerInfoDto** | [**SeriesTimerInfoDto**](SeriesTimerInfoDto.md)| New series timer info. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined


## updateTimer

> updateTimer(timerId, opts)

Updates a live tv timer.

### Example

```javascript
import JellyfinApi from 'jellyfin_api';
let defaultClient = JellyfinApi.ApiClient.instance;
// Configure API key authorization: CustomAuthentication
let CustomAuthentication = defaultClient.authentications['CustomAuthentication'];
CustomAuthentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//CustomAuthentication.apiKeyPrefix = 'Token';

let apiInstance = new JellyfinApi.LiveTvApi();
let timerId = "timerId_example"; // String | Timer id.
let opts = {
  'timerInfoDto': new JellyfinApi.TimerInfoDto() // TimerInfoDto | New timer info.
};
apiInstance.updateTimer(timerId, opts, (error, data, response) => {
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
 **timerId** | **String**| Timer id. | 
 **timerInfoDto** | [**TimerInfoDto**](TimerInfoDto.md)| New timer info. | [optional] 

### Return type

null (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined

