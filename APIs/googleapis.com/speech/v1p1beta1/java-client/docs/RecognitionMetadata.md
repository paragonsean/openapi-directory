

# RecognitionMetadata

Description of audio data to be recognized.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audioTopic** | **String** | Description of the content. Eg. \&quot;Recordings of federal supreme court hearings from 2012\&quot;. |  [optional] |
|**industryNaicsCodeOfAudio** | **Integer** | The industry vertical to which this speech recognition request most closely applies. This is most indicative of the topics contained in the audio. Use the 6-digit NAICS code to identify the industry vertical - see https://www.naics.com/search/. |  [optional] |
|**interactionType** | [**InteractionTypeEnum**](#InteractionTypeEnum) | The use case most closely describing the audio content to be recognized. |  [optional] |
|**microphoneDistance** | [**MicrophoneDistanceEnum**](#MicrophoneDistanceEnum) | The audio type that most closely describes the audio being recognized. |  [optional] |
|**obfuscatedId** | **String** | Obfuscated (privacy-protected) ID of the user, to identify number of unique users using the service. |  [optional] |
|**originalMediaType** | [**OriginalMediaTypeEnum**](#OriginalMediaTypeEnum) | The original media the speech was recorded on. |  [optional] |
|**originalMimeType** | **String** | Mime type of the original audio file. For example &#x60;audio/m4a&#x60;, &#x60;audio/x-alaw-basic&#x60;, &#x60;audio/mp3&#x60;, &#x60;audio/3gpp&#x60;. A list of possible audio mime types is maintained at http://www.iana.org/assignments/media-types/media-types.xhtml#audio |  [optional] |
|**recordingDeviceName** | **String** | The device used to make the recording. Examples &#39;Nexus 5X&#39; or &#39;Polycom SoundStation IP 6000&#39; or &#39;POTS&#39; or &#39;VoIP&#39; or &#39;Cardioid Microphone&#39;. |  [optional] |
|**recordingDeviceType** | [**RecordingDeviceTypeEnum**](#RecordingDeviceTypeEnum) | The type of device the speech was recorded with. |  [optional] |



## Enum: InteractionTypeEnum

| Name | Value |
|---- | -----|
| INTERACTION_TYPE_UNSPECIFIED | &quot;INTERACTION_TYPE_UNSPECIFIED&quot; |
| DISCUSSION | &quot;DISCUSSION&quot; |
| PRESENTATION | &quot;PRESENTATION&quot; |
| PHONE_CALL | &quot;PHONE_CALL&quot; |
| VOICEMAIL | &quot;VOICEMAIL&quot; |
| PROFESSIONALLY_PRODUCED | &quot;PROFESSIONALLY_PRODUCED&quot; |
| VOICE_SEARCH | &quot;VOICE_SEARCH&quot; |
| VOICE_COMMAND | &quot;VOICE_COMMAND&quot; |
| DICTATION | &quot;DICTATION&quot; |



## Enum: MicrophoneDistanceEnum

| Name | Value |
|---- | -----|
| MICROPHONE_DISTANCE_UNSPECIFIED | &quot;MICROPHONE_DISTANCE_UNSPECIFIED&quot; |
| NEARFIELD | &quot;NEARFIELD&quot; |
| MIDFIELD | &quot;MIDFIELD&quot; |
| FARFIELD | &quot;FARFIELD&quot; |



## Enum: OriginalMediaTypeEnum

| Name | Value |
|---- | -----|
| ORIGINAL_MEDIA_TYPE_UNSPECIFIED | &quot;ORIGINAL_MEDIA_TYPE_UNSPECIFIED&quot; |
| AUDIO | &quot;AUDIO&quot; |
| VIDEO | &quot;VIDEO&quot; |



## Enum: RecordingDeviceTypeEnum

| Name | Value |
|---- | -----|
| RECORDING_DEVICE_TYPE_UNSPECIFIED | &quot;RECORDING_DEVICE_TYPE_UNSPECIFIED&quot; |
| SMARTPHONE | &quot;SMARTPHONE&quot; |
| PC | &quot;PC&quot; |
| PHONE_LINE | &quot;PHONE_LINE&quot; |
| VEHICLE | &quot;VEHICLE&quot; |
| OTHER_OUTDOOR_DEVICE | &quot;OTHER_OUTDOOR_DEVICE&quot; |
| OTHER_INDOOR_DEVICE | &quot;OTHER_INDOOR_DEVICE&quot; |



