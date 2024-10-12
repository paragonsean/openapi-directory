

# GoogleCloudContactcenterinsightsV1alpha1CallAnnotation

A piece of metadata that applies to a window of a call.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotationEndBoundary** | [**GoogleCloudContactcenterinsightsV1alpha1AnnotationBoundary**](GoogleCloudContactcenterinsightsV1alpha1AnnotationBoundary.md) |  |  [optional] |
|**annotationStartBoundary** | [**GoogleCloudContactcenterinsightsV1alpha1AnnotationBoundary**](GoogleCloudContactcenterinsightsV1alpha1AnnotationBoundary.md) |  |  [optional] |
|**channelTag** | **Integer** | The channel of the audio where the annotation occurs. For single-channel audio, this field is not populated. |  [optional] |
|**entityMentionData** | [**GoogleCloudContactcenterinsightsV1alpha1EntityMentionData**](GoogleCloudContactcenterinsightsV1alpha1EntityMentionData.md) |  |  [optional] |
|**holdData** | **Object** | The data for a hold annotation. |  [optional] |
|**intentMatchData** | [**GoogleCloudContactcenterinsightsV1alpha1IntentMatchData**](GoogleCloudContactcenterinsightsV1alpha1IntentMatchData.md) |  |  [optional] |
|**interruptionData** | **Object** | The data for an interruption annotation. |  [optional] |
|**issueMatchData** | [**GoogleCloudContactcenterinsightsV1alpha1IssueMatchData**](GoogleCloudContactcenterinsightsV1alpha1IssueMatchData.md) |  |  [optional] |
|**phraseMatchData** | [**GoogleCloudContactcenterinsightsV1alpha1PhraseMatchData**](GoogleCloudContactcenterinsightsV1alpha1PhraseMatchData.md) |  |  [optional] |
|**sentimentData** | [**GoogleCloudContactcenterinsightsV1alpha1SentimentData**](GoogleCloudContactcenterinsightsV1alpha1SentimentData.md) |  |  [optional] |
|**silenceData** | **Object** | The data for a silence annotation. |  [optional] |



