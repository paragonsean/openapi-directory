# YouTubeDataApiV3.VideoSuggestions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**editorSuggestions** | **[String]** | A list of video editing operations that might improve the video quality or playback experience of the uploaded video. | [optional] 
**processingErrors** | **[String]** | A list of errors that will prevent YouTube from successfully processing the uploaded video video. These errors indicate that, regardless of the video&#39;s current processing status, eventually, that status will almost certainly be failed. | [optional] 
**processingHints** | **[String]** | A list of suggestions that may improve YouTube&#39;s ability to process the video. | [optional] 
**processingWarnings** | **[String]** | A list of reasons why YouTube may have difficulty transcoding the uploaded video or that might result in an erroneous transcoding. These warnings are generated before YouTube actually processes the uploaded video file. In addition, they identify issues that are unlikely to cause the video processing to fail but that might cause problems such as sync issues, video artifacts, or a missing audio track. | [optional] 
**tagSuggestions** | [**[VideoSuggestionsTagSuggestion]**](VideoSuggestionsTagSuggestion.md) | A list of keyword tags that could be added to the video&#39;s metadata to increase the likelihood that users will locate your video when searching or browsing on YouTube. | [optional] 



## Enum: [EditorSuggestionsEnum]


* `videoAutoLevels` (value: `"videoAutoLevels"`)

* `videoStabilize` (value: `"videoStabilize"`)

* `videoCrop` (value: `"videoCrop"`)

* `audioQuietAudioSwap` (value: `"audioQuietAudioSwap"`)





## Enum: [ProcessingErrorsEnum]


* `audioFile` (value: `"audioFile"`)

* `imageFile` (value: `"imageFile"`)

* `projectFile` (value: `"projectFile"`)

* `notAVideoFile` (value: `"notAVideoFile"`)

* `docFile` (value: `"docFile"`)

* `archiveFile` (value: `"archiveFile"`)

* `unsupportedSpatialAudioLayout` (value: `"unsupportedSpatialAudioLayout"`)





## Enum: [ProcessingHintsEnum]


* `nonStreamableMov` (value: `"nonStreamableMov"`)

* `sendBestQualityVideo` (value: `"sendBestQualityVideo"`)

* `sphericalVideo` (value: `"sphericalVideo"`)

* `spatialAudio` (value: `"spatialAudio"`)

* `vrVideo` (value: `"vrVideo"`)

* `hdrVideo` (value: `"hdrVideo"`)





## Enum: [ProcessingWarningsEnum]


* `unknownContainer` (value: `"unknownContainer"`)

* `unknownVideoCodec` (value: `"unknownVideoCodec"`)

* `unknownAudioCodec` (value: `"unknownAudioCodec"`)

* `inconsistentResolution` (value: `"inconsistentResolution"`)

* `hasEditlist` (value: `"hasEditlist"`)

* `problematicVideoCodec` (value: `"problematicVideoCodec"`)

* `problematicAudioCodec` (value: `"problematicAudioCodec"`)

* `unsupportedVrStereoMode` (value: `"unsupportedVrStereoMode"`)

* `unsupportedSphericalProjectionType` (value: `"unsupportedSphericalProjectionType"`)

* `unsupportedHdrPixelFormat` (value: `"unsupportedHdrPixelFormat"`)

* `unsupportedHdrColorMetadata` (value: `"unsupportedHdrColorMetadata"`)

* `problematicHdrLookupTable` (value: `"problematicHdrLookupTable"`)




