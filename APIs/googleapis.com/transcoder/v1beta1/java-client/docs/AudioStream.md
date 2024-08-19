

# AudioStream

Audio stream resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bitrateBps** | **Integer** | Required. Audio bitrate in bits per second. Must be between 1 and 10,000,000. |  [optional] |
|**channelCount** | **Integer** | Number of audio channels. Must be between 1 and 6. The default is 2. |  [optional] |
|**channelLayout** | **List&lt;String&gt;** | A list of channel names specifying layout of the audio channels. This only affects the metadata embedded in the container headers, if supported by the specified format. The default is &#x60;[\&quot;fl\&quot;, \&quot;fr\&quot;]&#x60;. Supported channel names: - &#39;fl&#39; - Front left channel - &#39;fr&#39; - Front right channel - &#39;sl&#39; - Side left channel - &#39;sr&#39; - Side right channel - &#39;fc&#39; - Front center channel - &#39;lfe&#39; - Low frequency |  [optional] |
|**codec** | **String** | The codec for this audio stream. The default is &#x60;\&quot;aac\&quot;&#x60;. Supported audio codecs: - &#39;aac&#39; - &#39;aac-he&#39; - &#39;aac-he-v2&#39; - &#39;mp3&#39; - &#39;ac3&#39; - &#39;eac3&#39; |  [optional] |
|**mapping** | [**List&lt;AudioAtom&gt;**](AudioAtom.md) | The mapping for the &#x60;Job.edit_list&#x60; atoms with audio &#x60;EditAtom.inputs&#x60;. |  [optional] |
|**sampleRateHertz** | **Integer** | The audio sample rate in Hertz. The default is 48000 Hertz. |  [optional] |



