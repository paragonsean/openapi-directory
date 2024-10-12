

# StartTalkRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**language** | **Language** |  |  [optional] |
|**level** | **String** | The volume level that the speech is played. This can be any value between &#x60;-1&#x60; to &#x60;1&#x60; in &#x60;0.1&#x60; increments, with &#x60;0&#x60; being the default. |  [optional] |
|**loop** | **Integer** | The number of times to repeat the text the file, 0 for infinite |  [optional] |
|**premium** | **Boolean** | Set to true to use the premium version of the specified style if available, otherwise the standard version will be used. The default value is false. You can find more information about Premium Voices in the [Text-To-Speech guide](/voice/voice-api/guides/text-to-speech#premium-voices). |  [optional] |
|**style** | **Integer** | The vocal style (vocal range, tessitura, and timbre) to use |  [optional] |
|**text** | **String** | The text to read |  |
|**voiceName** | **VoiceName** |  |  [optional] |



