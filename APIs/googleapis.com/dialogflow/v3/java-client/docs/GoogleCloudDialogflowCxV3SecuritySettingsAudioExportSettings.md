

# GoogleCloudDialogflowCxV3SecuritySettingsAudioExportSettings

Settings for exporting audio.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioExportPattern** | **String** | Filename pattern for exported audio. |  [optional] |
|**audioFormat** | [**AudioFormatEnum**](#AudioFormatEnum) | File format for exported audio file. Currently only in telephony recordings. |  [optional] |
|**enableAudioRedaction** | **Boolean** | Enable audio redaction if it is true. |  [optional] |
|**gcsBucket** | **String** | Cloud Storage bucket to export audio record to. Setting this field would grant the Storage Object Creator role to the Dialogflow Service Agent. API caller that tries to modify this field should have the permission of storage.buckets.setIamPolicy. |  [optional] |



## Enum: AudioFormatEnum

| Name | Value |
|---- | -----|
| AUDIO_FORMAT_UNSPECIFIED | &quot;AUDIO_FORMAT_UNSPECIFIED&quot; |
| MULAW | &quot;MULAW&quot; |
| MP3 | &quot;MP3&quot; |
| OGG | &quot;OGG&quot; |



