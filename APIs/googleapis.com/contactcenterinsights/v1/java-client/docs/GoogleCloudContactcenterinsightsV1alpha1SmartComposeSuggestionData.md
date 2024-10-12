

# GoogleCloudContactcenterinsightsV1alpha1SmartComposeSuggestionData

Agent Assist Smart Compose suggestion data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidenceScore** | **Double** | The system&#39;s confidence score that this suggestion is a good match for this conversation, ranging from 0.0 (completely uncertain) to 1.0 (completely certain). |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | Map that contains metadata about the Smart Compose suggestion and the document from which it originates. |  [optional] |
|**queryRecord** | **String** | The name of the answer record. Format: projects/{project}/locations/{location}/answerRecords/{answer_record} |  [optional] |
|**suggestion** | **String** | The content of the suggestion. |  [optional] |



