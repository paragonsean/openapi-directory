

# GoogleCloudContactcenterinsightsV1CallAnnotation

A piece of metadata that applies to a window of a call.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationEndBoundary** | [**GoogleCloudContactcenterinsightsV1AnnotationBoundary**](GoogleCloudContactcenterinsightsV1AnnotationBoundary.md) |  |  [optional] |
|**annotationStartBoundary** | [**GoogleCloudContactcenterinsightsV1AnnotationBoundary**](GoogleCloudContactcenterinsightsV1AnnotationBoundary.md) |  |  [optional] |
|**channelTag** | **Integer** | The channel of the audio where the annotation occurs. For single-channel audio, this field is not populated. |  [optional] |
|**entityMentionData** | [**GoogleCloudContactcenterinsightsV1EntityMentionData**](GoogleCloudContactcenterinsightsV1EntityMentionData.md) |  |  [optional] |
|**holdData** | **Object** | The data for a hold annotation. |  [optional] |
|**intentMatchData** | [**GoogleCloudContactcenterinsightsV1IntentMatchData**](GoogleCloudContactcenterinsightsV1IntentMatchData.md) |  |  [optional] |
|**interruptionData** | **Object** | The data for an interruption annotation. |  [optional] |
|**issueMatchData** | [**GoogleCloudContactcenterinsightsV1IssueMatchData**](GoogleCloudContactcenterinsightsV1IssueMatchData.md) |  |  [optional] |
|**phraseMatchData** | [**GoogleCloudContactcenterinsightsV1PhraseMatchData**](GoogleCloudContactcenterinsightsV1PhraseMatchData.md) |  |  [optional] |
|**sentimentData** | [**GoogleCloudContactcenterinsightsV1SentimentData**](GoogleCloudContactcenterinsightsV1SentimentData.md) |  |  [optional] |
|**silenceData** | **Object** | The data for a silence annotation. |  [optional] |



