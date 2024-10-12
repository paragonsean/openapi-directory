

# Soundtrack

A music or audio file in mp3 format that plays for the duration of the rendered video or the length of the audio file, which ever is shortest.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**effect** | [**EffectEnum**](#EffectEnum) | The effect to apply to the audio file &lt;ul&gt;   &lt;li&gt;&#x60;fadeIn&#x60; - fade volume in only&lt;/li&gt;   &lt;li&gt;&#x60;fadeOut&#x60; - fade volume out only&lt;/li&gt;   &lt;li&gt;&#x60;fadeInFadeOut&#x60; - fade volume in and out&lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**src** | **String** | The URL of the mp3 audio file. The URL must be publicly accessible or include credentials. |  |
|**volume** | **BigDecimal** | Set the volume for the soundtrack between 0 and 1 where 0 is muted and 1 is full volume (defaults to 1). |  [optional] |



## Enum: EffectEnum

| Name | Value |
|---- | -----|
| FADE_IN | &quot;fadeIn&quot; |
| FADE_OUT | &quot;fadeOut&quot; |
| FADE_IN_FADE_OUT | &quot;fadeInFadeOut&quot; |



