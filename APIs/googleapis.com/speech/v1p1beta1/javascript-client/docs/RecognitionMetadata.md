# CloudSpeechToTextApi.RecognitionMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audioTopic** | **String** | Description of the content. Eg. \&quot;Recordings of federal supreme court hearings from 2012\&quot;. | [optional] 
**industryNaicsCodeOfAudio** | **Number** | The industry vertical to which this speech recognition request most closely applies. This is most indicative of the topics contained in the audio. Use the 6-digit NAICS code to identify the industry vertical - see https://www.naics.com/search/. | [optional] 
**interactionType** | **String** | The use case most closely describing the audio content to be recognized. | [optional] 
**microphoneDistance** | **String** | The audio type that most closely describes the audio being recognized. | [optional] 
**obfuscatedId** | **String** | Obfuscated (privacy-protected) ID of the user, to identify number of unique users using the service. | [optional] 
**originalMediaType** | **String** | The original media the speech was recorded on. | [optional] 
**originalMimeType** | **String** | Mime type of the original audio file. For example &#x60;audio/m4a&#x60;, &#x60;audio/x-alaw-basic&#x60;, &#x60;audio/mp3&#x60;, &#x60;audio/3gpp&#x60;. A list of possible audio mime types is maintained at http://www.iana.org/assignments/media-types/media-types.xhtml#audio | [optional] 
**recordingDeviceName** | **String** | The device used to make the recording. Examples &#39;Nexus 5X&#39; or &#39;Polycom SoundStation IP 6000&#39; or &#39;POTS&#39; or &#39;VoIP&#39; or &#39;Cardioid Microphone&#39;. | [optional] 
**recordingDeviceType** | **String** | The type of device the speech was recorded with. | [optional] 



## Enum: InteractionTypeEnum


* `INTERACTION_TYPE_UNSPECIFIED` (value: `"INTERACTION_TYPE_UNSPECIFIED"`)

* `DISCUSSION` (value: `"DISCUSSION"`)

* `PRESENTATION` (value: `"PRESENTATION"`)

* `PHONE_CALL` (value: `"PHONE_CALL"`)

* `VOICEMAIL` (value: `"VOICEMAIL"`)

* `PROFESSIONALLY_PRODUCED` (value: `"PROFESSIONALLY_PRODUCED"`)

* `VOICE_SEARCH` (value: `"VOICE_SEARCH"`)

* `VOICE_COMMAND` (value: `"VOICE_COMMAND"`)

* `DICTATION` (value: `"DICTATION"`)





## Enum: MicrophoneDistanceEnum


* `MICROPHONE_DISTANCE_UNSPECIFIED` (value: `"MICROPHONE_DISTANCE_UNSPECIFIED"`)

* `NEARFIELD` (value: `"NEARFIELD"`)

* `MIDFIELD` (value: `"MIDFIELD"`)

* `FARFIELD` (value: `"FARFIELD"`)





## Enum: OriginalMediaTypeEnum


* `ORIGINAL_MEDIA_TYPE_UNSPECIFIED` (value: `"ORIGINAL_MEDIA_TYPE_UNSPECIFIED"`)

* `AUDIO` (value: `"AUDIO"`)

* `VIDEO` (value: `"VIDEO"`)





## Enum: RecordingDeviceTypeEnum


* `RECORDING_DEVICE_TYPE_UNSPECIFIED` (value: `"RECORDING_DEVICE_TYPE_UNSPECIFIED"`)

* `SMARTPHONE` (value: `"SMARTPHONE"`)

* `PC` (value: `"PC"`)

* `PHONE_LINE` (value: `"PHONE_LINE"`)

* `VEHICLE` (value: `"VEHICLE"`)

* `OTHER_OUTDOOR_DEVICE` (value: `"OTHER_OUTDOOR_DEVICE"`)

* `OTHER_INDOOR_DEVICE` (value: `"OTHER_INDOOR_DEVICE"`)




