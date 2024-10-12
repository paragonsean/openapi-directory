

# LabeledUtterance

A prediction and label pair of an example.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entityLabels** | [**List&lt;EntityLabel&gt;**](EntityLabel.md) | The entities matching the example. |  [optional] |
|**entityPredictions** | [**List&lt;EntityPrediction&gt;**](EntityPrediction.md) | List of suggested entities. |  [optional] |
|**id** | **Integer** | ID of Labeled Utterance. |  [optional] |
|**intentLabel** | **String** | The intent matching the example. |  [optional] |
|**intentPredictions** | [**List&lt;IntentPrediction&gt;**](IntentPrediction.md) | List of suggested intents. |  [optional] |
|**text** | **String** | The utterance. For example, \&quot;What&#39;s the weather like in seattle?\&quot; |  [optional] |
|**tokenizedText** | **List&lt;String&gt;** | The utterance tokenized. |  [optional] |



