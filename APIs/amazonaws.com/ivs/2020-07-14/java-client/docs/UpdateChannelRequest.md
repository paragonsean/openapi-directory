

# UpdateChannelRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arn** | **String** | ARN of the channel to be updated. |  |
|**authorized** | **Boolean** | Whether the channel is private (enabled for playback authorization). |  [optional] |
|**insecureIngest** | **Boolean** | Whether the channel allows insecure RTMP ingest. Default: &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**latencyMode** | [**LatencyModeEnum**](#LatencyModeEnum) | Channel latency mode. Use &lt;code&gt;NORMAL&lt;/code&gt; to broadcast and deliver live video up to Full HD. Use &lt;code&gt;LOW&lt;/code&gt; for near-real-time interaction with viewers. (Note: In the Amazon IVS console, &lt;code&gt;LOW&lt;/code&gt; and &lt;code&gt;NORMAL&lt;/code&gt; correspond to Ultra-low and Standard, respectively.) |  [optional] |
|**name** | **String** | Channel name. |  [optional] |
|**preset** | [**PresetEnum**](#PresetEnum) | Optional transcode preset for the channel. This is selectable only for &lt;code&gt;ADVANCED_HD&lt;/code&gt; and &lt;code&gt;ADVANCED_SD&lt;/code&gt; channel types. For those channel types, the default &lt;code&gt;preset&lt;/code&gt; is &lt;code&gt;HIGHER_BANDWIDTH_DELIVERY&lt;/code&gt;. For other channel types (&lt;code&gt;BASIC&lt;/code&gt; and &lt;code&gt;STANDARD&lt;/code&gt;), &lt;code&gt;preset&lt;/code&gt; is the empty string (&lt;code&gt;\&quot;\&quot;&lt;/code&gt;). |  [optional] |
|**recordingConfigurationArn** | **String** | Recording-configuration ARN. If this is set to an empty string, recording is disabled. A value other than an empty string indicates that recording is enabled |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | &lt;p&gt;Channel type, which determines the allowable resolution and bitrate. &lt;i&gt;If you exceed the allowable input resolution or bitrate, the stream probably will disconnect immediately.&lt;/i&gt; Some types generate multiple qualities (renditions) from the original input; this automatically gives viewers the best experience for their devices and network conditions. Some types provide transcoded video; transcoding allows higher playback quality across a range of download speeds. Default: &lt;code&gt;STANDARD&lt;/code&gt;. Valid values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;BASIC&lt;/code&gt;: Video is transmuxed: Amazon IVS delivers the original input quality to viewers. The viewer’s video-quality choice is limited to the original input. Input resolution can be up to 1080p and bitrate can be up to 1.5 Mbps for 480p and up to 3.5 Mbps for resolutions between 480p and 1080p. Original audio is passed through.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;STANDARD&lt;/code&gt;: Video is transcoded: multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Transcoding allows higher playback quality across a range of download speeds. Resolution can be up to 1080p and bitrate can be up to 8.5 Mbps. Audio is transcoded only for renditions 360p and below; above that, audio is passed through. This is the default when you create a channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ADVANCED_SD&lt;/code&gt;: Video is transcoded; multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Input resolution can be up to 1080p and bitrate can be up to 8.5 Mbps; output is capped at SD quality (480p). You can select an optional transcode preset (see below). Audio for all renditions is transcoded, and an audio-only rendition is available.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ADVANCED_HD&lt;/code&gt;: Video is transcoded; multiple qualities are generated from the original input, to automatically give viewers the best experience for their devices and network conditions. Input resolution can be up to 1080p and bitrate can be up to 8.5 Mbps; output is capped at HD quality (720p). You can select an optional transcode preset (see below). Audio for all renditions is transcoded, and an audio-only rendition is available.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Optional &lt;i&gt;transcode presets&lt;/i&gt; (available for the &lt;code&gt;ADVANCED&lt;/code&gt; types) allow you to trade off available download bandwidth and video quality, to optimize the viewing experience. There are two presets:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Constrained bandwidth delivery&lt;/i&gt; uses a lower bitrate for each quality level. Use it if you have low download bandwidth and/or simple video content (e.g., talking heads)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Higher bandwidth delivery&lt;/i&gt; uses a higher bitrate for each quality level. Use it if you have high download bandwidth and/or complex video content (e.g., flashes and quick scene changes).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |



## Enum: LatencyModeEnum

| Name | Value |
|---- | -----|
| NORMAL | &quot;NORMAL&quot; |
| LOW | &quot;LOW&quot; |



## Enum: PresetEnum

| Name | Value |
|---- | -----|
| HIGHER_BANDWIDTH_DELIVERY | &quot;HIGHER_BANDWIDTH_DELIVERY&quot; |
| CONSTRAINED_BANDWIDTH_DELIVERY | &quot;CONSTRAINED_BANDWIDTH_DELIVERY&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BASIC | &quot;BASIC&quot; |
| STANDARD | &quot;STANDARD&quot; |
| ADVANCED_SD | &quot;ADVANCED_SD&quot; |
| ADVANCED_HD | &quot;ADVANCED_HD&quot; |



