# AwsMediaTailor.CreateChannelRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fillerSlate** | [**UpdateChannelRequestFillerSlate**](UpdateChannelRequestFillerSlate.md) |  | [optional] 
**outputs** | [**[RequestOutputItem]**](RequestOutputItem.md) | An object that represents an object in the CreateChannel request. | 
**playbackMode** | **String** | &lt;p&gt;The type of playback mode to use for this channel.&lt;/p&gt; &lt;p&gt; &lt;code&gt;LINEAR&lt;/code&gt; - The programs in the schedule play once back-to-back in the schedule.&lt;/p&gt; &lt;p&gt; &lt;code&gt;LOOP&lt;/code&gt; - The programs in the schedule play back-to-back in an endless loop. When the last program in the schedule stops playing, playback loops back to the first program in the schedule.&lt;/p&gt; | 
**tags** | **{String: String}** | The tags to assign to the channel. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html\&quot;&gt;Tagging AWS Elemental MediaTailor Resources&lt;/a&gt;. | [optional] 
**tier** | **String** | The tier of the channel. | [optional] 



## Enum: PlaybackModeEnum


* `LOOP` (value: `"LOOP"`)

* `LINEAR` (value: `"LINEAR"`)





## Enum: TierEnum


* `BASIC` (value: `"BASIC"`)

* `STANDARD` (value: `"STANDARD"`)




