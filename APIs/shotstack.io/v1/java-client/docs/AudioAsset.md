

# AudioAsset

The AudioAsset is used to add sound effects and audio at specific intervals on the timeline. The src must be a publicly accessible URL to an audio resource such  as an mp3 file.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**effect** | [**EffectEnum**](#EffectEnum) | The effect to apply to the audio asset &lt;ul&gt;   &lt;li&gt;&#x60;fadeIn&#x60; - fade volume in only&lt;/li&gt;   &lt;li&gt;&#x60;fadeOut&#x60; - fade volume out only&lt;/li&gt;   &lt;li&gt;&#x60;fadeInFadeOut&#x60; - fade volume in and out&lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**src** | **String** | The audio source URL. The URL must be publicly accessible or include credentials. |  |
|**trim** | **BigDecimal** | The start trim point of the audio clip, in seconds (defaults to 0). Audio will start from the in trim point. The audio will play until the file ends or the Clip length is reached. |  [optional] |
|**type** | **String** | The type of asset - set to &#x60;audio&#x60; for audio assets. |  |
|**volume** | **BigDecimal** | Set the volume for the audio clip between 0 and 1 where 0 is muted and 1 is full volume (defaults to 1). |  [optional] |



## Enum: EffectEnum

| Name | Value |
|---- | -----|
| FADE_IN | &quot;fadeIn&quot; |
| FADE_OUT | &quot;fadeOut&quot; |
| FADE_IN_FADE_OUT | &quot;fadeInFadeOut&quot; |



