# ContactCenterAiInsightsApi.GoogleCloudContactcenterinsightsV1ConversationTranscriptTranscriptSegment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channelTag** | **Number** | For conversations derived from multi-channel audio, this is the channel number corresponding to the audio from that channel. For audioChannelCount &#x3D; N, its output values can range from &#39;1&#39; to &#39;N&#39;. A channel tag of 0 indicates that the audio is mono. | [optional] 
**confidence** | **Number** | A confidence estimate between 0.0 and 1.0 of the fidelity of this segment. A default value of 0.0 indicates that the value is unset. | [optional] 
**dialogflowSegmentMetadata** | [**GoogleCloudContactcenterinsightsV1ConversationTranscriptTranscriptSegmentDialogflowSegmentMetadata**](GoogleCloudContactcenterinsightsV1ConversationTranscriptTranscriptSegmentDialogflowSegmentMetadata.md) |  | [optional] 
**languageCode** | **String** | The language code of this segment as a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: \&quot;en-US\&quot;. | [optional] 
**messageTime** | **String** | The time that the message occurred, if provided. | [optional] 
**segmentParticipant** | [**GoogleCloudContactcenterinsightsV1ConversationParticipant**](GoogleCloudContactcenterinsightsV1ConversationParticipant.md) |  | [optional] 
**sentiment** | [**GoogleCloudContactcenterinsightsV1SentimentData**](GoogleCloudContactcenterinsightsV1SentimentData.md) |  | [optional] 
**text** | **String** | The text of this segment. | [optional] 
**words** | [**[GoogleCloudContactcenterinsightsV1ConversationTranscriptTranscriptSegmentWordInfo]**](GoogleCloudContactcenterinsightsV1ConversationTranscriptTranscriptSegmentWordInfo.md) | A list of the word-specific information for each word in the segment. | [optional] 


