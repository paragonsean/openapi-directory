

# VideoSuggestions

Specifies suggestions on how to improve video content, including encoding hints, tag suggestions, and editor suggestions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**editorSuggestions** | [**List&lt;EditorSuggestionsEnum&gt;**](#List&lt;EditorSuggestionsEnum&gt;) | A list of video editing operations that might improve the video quality or playback experience of the uploaded video. |  [optional] |
|**processingErrors** | [**List&lt;ProcessingErrorsEnum&gt;**](#List&lt;ProcessingErrorsEnum&gt;) | A list of errors that will prevent YouTube from successfully processing the uploaded video video. These errors indicate that, regardless of the video&#39;s current processing status, eventually, that status will almost certainly be failed. |  [optional] |
|**processingHints** | [**List&lt;ProcessingHintsEnum&gt;**](#List&lt;ProcessingHintsEnum&gt;) | A list of suggestions that may improve YouTube&#39;s ability to process the video. |  [optional] |
|**processingWarnings** | [**List&lt;ProcessingWarningsEnum&gt;**](#List&lt;ProcessingWarningsEnum&gt;) | A list of reasons why YouTube may have difficulty transcoding the uploaded video or that might result in an erroneous transcoding. These warnings are generated before YouTube actually processes the uploaded video file. In addition, they identify issues that are unlikely to cause the video processing to fail but that might cause problems such as sync issues, video artifacts, or a missing audio track. |  [optional] |
|**tagSuggestions** | [**List&lt;VideoSuggestionsTagSuggestion&gt;**](VideoSuggestionsTagSuggestion.md) | A list of keyword tags that could be added to the video&#39;s metadata to increase the likelihood that users will locate your video when searching or browsing on YouTube. |  [optional] |



## Enum: List&lt;EditorSuggestionsEnum&gt;

| Name | Value |
|---- | -----|
| VIDEO_AUTO_LEVELS | &quot;videoAutoLevels&quot; |
| VIDEO_STABILIZE | &quot;videoStabilize&quot; |
| VIDEO_CROP | &quot;videoCrop&quot; |
| AUDIO_QUIET_AUDIO_SWAP | &quot;audioQuietAudioSwap&quot; |



## Enum: List&lt;ProcessingErrorsEnum&gt;

| Name | Value |
|---- | -----|
| AUDIO_FILE | &quot;audioFile&quot; |
| IMAGE_FILE | &quot;imageFile&quot; |
| PROJECT_FILE | &quot;projectFile&quot; |
| NOT_A_VIDEO_FILE | &quot;notAVideoFile&quot; |
| DOC_FILE | &quot;docFile&quot; |
| ARCHIVE_FILE | &quot;archiveFile&quot; |
| UNSUPPORTED_SPATIAL_AUDIO_LAYOUT | &quot;unsupportedSpatialAudioLayout&quot; |



## Enum: List&lt;ProcessingHintsEnum&gt;

| Name | Value |
|---- | -----|
| NON_STREAMABLE_MOV | &quot;nonStreamableMov&quot; |
| SEND_BEST_QUALITY_VIDEO | &quot;sendBestQualityVideo&quot; |
| SPHERICAL_VIDEO | &quot;sphericalVideo&quot; |
| SPATIAL_AUDIO | &quot;spatialAudio&quot; |
| VR_VIDEO | &quot;vrVideo&quot; |
| HDR_VIDEO | &quot;hdrVideo&quot; |



## Enum: List&lt;ProcessingWarningsEnum&gt;

| Name | Value |
|---- | -----|
| UNKNOWN_CONTAINER | &quot;unknownContainer&quot; |
| UNKNOWN_VIDEO_CODEC | &quot;unknownVideoCodec&quot; |
| UNKNOWN_AUDIO_CODEC | &quot;unknownAudioCodec&quot; |
| INCONSISTENT_RESOLUTION | &quot;inconsistentResolution&quot; |
| HAS_EDITLIST | &quot;hasEditlist&quot; |
| PROBLEMATIC_VIDEO_CODEC | &quot;problematicVideoCodec&quot; |
| PROBLEMATIC_AUDIO_CODEC | &quot;problematicAudioCodec&quot; |
| UNSUPPORTED_VR_STEREO_MODE | &quot;unsupportedVrStereoMode&quot; |
| UNSUPPORTED_SPHERICAL_PROJECTION_TYPE | &quot;unsupportedSphericalProjectionType&quot; |
| UNSUPPORTED_HDR_PIXEL_FORMAT | &quot;unsupportedHdrPixelFormat&quot; |
| UNSUPPORTED_HDR_COLOR_METADATA | &quot;unsupportedHdrColorMetadata&quot; |
| PROBLEMATIC_HDR_LOOKUP_TABLE | &quot;problematicHdrLookupTable&quot; |



