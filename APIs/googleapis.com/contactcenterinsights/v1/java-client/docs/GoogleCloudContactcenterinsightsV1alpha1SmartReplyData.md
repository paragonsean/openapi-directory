

# GoogleCloudContactcenterinsightsV1alpha1SmartReplyData

Agent Assist Smart Reply data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidenceScore** | **Double** | The system&#39;s confidence score that this reply is a good match for this conversation, ranging from 0.0 (completely uncertain) to 1.0 (completely certain). |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | Map that contains metadata about the Smart Reply and the document from which it originates. |  [optional] |
|**queryRecord** | **String** | The name of the answer record. Format: projects/{project}/locations/{location}/answerRecords/{answer_record} |  [optional] |
|**reply** | **String** | The content of the reply. |  [optional] |



