# WowzaStreamingCloudRestApiReferenceDocumentation.StreamSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupIpAddress** | **String** | If &lt;em&gt;location_method&lt;/em&gt; is &lt;strong&gt;ip_address&lt;/strong&gt;, specify the backup IP address of the source encoder. | [optional] 
**backupUrl** | **String** | The backup RTMP playback URL of the transcoded stream. | [optional] 
**createdAt** | **Date** | The date and time that the stream source was created. | [optional] 
**id** | **String** | The unique alphanumeric string that identifies the stream source. | [optional] 
**ipAddress** | **String** | If &lt;em&gt;location_method&lt;/em&gt; is &lt;strong&gt;ip_address&lt;/strong&gt;, specify the primary IP address of the source encoder. | [optional] 
**location** | **String** | If &lt;em&gt;location_method&lt;/em&gt; is &lt;strong&gt;region&lt;/strong&gt;, specify a location as close as possible to the source encoder. | [optional] 
**locationMethod** | **String** | The method used to determine the location of the stream source, either by &lt;strong&gt;region&lt;/strong&gt; or based on the source encoder&#39;s &lt;strong&gt;ip_address&lt;/strong&gt;. | [optional] 
**name** | **String** | A descriptive name for the stream source. Maximum 255 characters. | [optional] 
**password** | **String** | The password that you can use to configure the source encoder to authenticate to the stream source. | [optional] 
**playbackUrl** | **String** | The full RTMP playback URL. | [optional] 
**primaryUrl** | **String** | The primary RTMP playback URL of the transcoded stream. | [optional] 
**provider** | **String** | The provider of the Wowza Streaming Cloud stream source. | [optional] 
**streamName** | **String** | The name of the stream that you can use to configure the source encoder to connect to the stream source. | [optional] 
**updatedAt** | **Date** | The date and time that the stream source was updated. | [optional] 
**username** | **String** | The username that you can use to configure the source encoder to authenticate to the stream source. | [optional] 



## Enum: LocationEnum


* `asia_pacific_australia` (value: `"asia_pacific_australia"`)

* `asia_pacific_japan` (value: `"asia_pacific_japan"`)

* `asia_pacific_singapore` (value: `"asia_pacific_singapore"`)

* `asia_pacific_taiwan` (value: `"asia_pacific_taiwan"`)

* `eu_belgium` (value: `"eu_belgium"`)

* `eu_germany` (value: `"eu_germany"`)

* `eu_ireland` (value: `"eu_ireland"`)

* `south_america_brazil` (value: `"south_america_brazil"`)

* `us_central_iowa` (value: `"us_central_iowa"`)

* `us_east_s_carolina` (value: `"us_east_s_carolina"`)

* `us_east_virginia` (value: `"us_east_virginia"`)

* `us_west_california` (value: `"us_west_california"`)

* `us_west_oregon` (value: `"us_west_oregon"`)





## Enum: LocationMethodEnum


* `region` (value: `"region"`)

* `ip_address` (value: `"ip_address"`)




