

# AudioDescription

Settings related to one audio tab on the MediaConvert console. In your job JSON, an instance of AudioDescription is equivalent to one audio tab in the console. Usually, one audio tab corresponds to one output audio track. Depending on how you set up your input audio selectors and whether you use audio selector groups, one audio tab can correspond to a group of output audio tracks.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioChannelTaggingSettings** | [**AudioDescriptionAudioChannelTaggingSettings**](AudioDescriptionAudioChannelTaggingSettings.md) |  |  [optional] |
|**audioNormalizationSettings** | [**AudioDescriptionAudioNormalizationSettings**](AudioDescriptionAudioNormalizationSettings.md) |  |  [optional] |
|**audioSourceName** | [**String**](String.md) |  |  [optional] |
|**audioType** | [**Integer**](Integer.md) |  |  [optional] |
|**audioTypeControl** | [**AudioTypeControl**](AudioTypeControl.md) |  |  [optional] |
|**codecSettings** | [**AudioDescriptionCodecSettings**](AudioDescriptionCodecSettings.md) |  |  [optional] |
|**customLanguageCode** | [**String**](String.md) |  |  [optional] |
|**languageCode** | [**LanguageCode**](LanguageCode.md) |  |  [optional] |
|**languageCodeControl** | [**AudioLanguageCodeControl**](AudioLanguageCodeControl.md) |  |  [optional] |
|**remixSettings** | [**AudioDescriptionRemixSettings**](AudioDescriptionRemixSettings.md) |  |  [optional] |
|**streamName** | [**String**](String.md) |  |  [optional] |



