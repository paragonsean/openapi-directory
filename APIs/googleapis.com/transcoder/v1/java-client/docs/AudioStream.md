

# AudioStream

Audio stream resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bitrateBps** | **Integer** | Required. Audio bitrate in bits per second. Must be between 1 and 10,000,000. |  [optional] |
|**channelCount** | **Integer** | Number of audio channels. Must be between 1 and 6. The default is 2. |  [optional] |
|**channelLayout** | **List&lt;String&gt;** | A list of channel names specifying layout of the audio channels. This only affects the metadata embedded in the container headers, if supported by the specified format. The default is &#x60;[\&quot;fl\&quot;, \&quot;fr\&quot;]&#x60;. Supported channel names: - &#x60;fl&#x60; - Front left channel - &#x60;fr&#x60; - Front right channel - &#x60;sl&#x60; - Side left channel - &#x60;sr&#x60; - Side right channel - &#x60;fc&#x60; - Front center channel - &#x60;lfe&#x60; - Low frequency |  [optional] |
|**codec** | **String** | The codec for this audio stream. The default is &#x60;aac&#x60;. Supported audio codecs: - &#x60;aac&#x60; - &#x60;aac-he&#x60; - &#x60;aac-he-v2&#x60; - &#x60;mp3&#x60; - &#x60;ac3&#x60; - &#x60;eac3&#x60; |  [optional] |
|**displayName** | **String** | The name for this particular audio stream that will be added to the HLS/DASH manifest. Not supported in MP4 files. |  [optional] |
|**languageCode** | **String** | The BCP-47 language code, such as &#x60;en-US&#x60; or &#x60;sr-Latn&#x60;. For more information, see https://www.unicode.org/reports/tr35/#Unicode_locale_identifier. Not supported in MP4 files. |  [optional] |
|**mapping** | [**List&lt;AudioMapping&gt;**](AudioMapping.md) | The mapping for the JobConfig.edit_list atoms with audio EditAtom.inputs. |  [optional] |
|**sampleRateHertz** | **Integer** | The audio sample rate in Hertz. The default is 48000 Hertz. |  [optional] |



