# AmazonInteractiveVideoService.CreateRecordingConfigurationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinationConfiguration** | [**CreateRecordingConfigurationRequestDestinationConfiguration**](CreateRecordingConfigurationRequestDestinationConfiguration.md) |  | 
**name** | **String** | Recording-configuration name. The value does not need to be unique. | [optional] 
**recordingReconnectWindowSeconds** | **Number** | If a broadcast disconnects and then reconnects within the specified interval, the multiple streams will be considered a single broadcast and merged together. Default: 0. | [optional] 
**renditionConfiguration** | [**CreateRecordingConfigurationRequestRenditionConfiguration**](CreateRecordingConfigurationRequestRenditionConfiguration.md) |  | [optional] 
**tags** | **{String: String}** | Array of 1-50 maps, each of the form &lt;code&gt;string:string (key:value)&lt;/code&gt;. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\&quot;&gt;Tagging Amazon Web Services Resources&lt;/a&gt; for more information, including restrictions that apply to tags and \&quot;Tag naming limits and requirements\&quot;; Amazon IVS has no service-specific constraints beyond what is documented there. | [optional] 
**thumbnailConfiguration** | [**CreateRecordingConfigurationRequestThumbnailConfiguration**](CreateRecordingConfigurationRequestThumbnailConfiguration.md) |  | [optional] 


