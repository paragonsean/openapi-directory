

# GoogleCloudContactcenterinsightsV1alpha1ConversationTranscriptTranscriptSegment

A segment of a full transcript.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channelTag** | **Integer** | For conversations derived from multi-channel audio, this is the channel number corresponding to the audio from that channel. For audioChannelCount &#x3D; N, its output values can range from &#39;1&#39; to &#39;N&#39;. A channel tag of 0 indicates that the audio is mono. |  [optional] |
|**confidence** | **Float** | A confidence estimate between 0.0 and 1.0 of the fidelity of this segment. A default value of 0.0 indicates that the value is unset. |  [optional] |
|**dialogflowSegmentMetadata** | [**GoogleCloudContactcenterinsightsV1alpha1ConversationTranscriptTranscriptSegmentDialogflowSegmentMetadata**](GoogleCloudContactcenterinsightsV1alpha1ConversationTranscriptTranscriptSegmentDialogflowSegmentMetadata.md) |  |  [optional] |
|**languageCode** | **String** | The language code of this segment as a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: \&quot;en-US\&quot;. |  [optional] |
|**messageTime** | **String** | The time that the message occurred, if provided. |  [optional] |
|**segmentParticipant** | [**GoogleCloudContactcenterinsightsV1alpha1ConversationParticipant**](GoogleCloudContactcenterinsightsV1alpha1ConversationParticipant.md) |  |  [optional] |
|**sentiment** | [**GoogleCloudContactcenterinsightsV1alpha1SentimentData**](GoogleCloudContactcenterinsightsV1alpha1SentimentData.md) |  |  [optional] |
|**text** | **String** | The text of this segment. |  [optional] |
|**words** | [**List&lt;GoogleCloudContactcenterinsightsV1alpha1ConversationTranscriptTranscriptSegmentWordInfo&gt;**](GoogleCloudContactcenterinsightsV1alpha1ConversationTranscriptTranscriptSegmentWordInfo.md) | A list of the word-specific information for each word in the segment. |  [optional] |



