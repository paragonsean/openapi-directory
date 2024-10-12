

# GoogleCloudAiplatformV1ModelExplanation

Aggregated explanation metrics for a Model over a set of instances.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**meanAttributions** | [**List&lt;GoogleCloudAiplatformV1Attribution&gt;**](GoogleCloudAiplatformV1Attribution.md) | Output only. Aggregated attributions explaining the Model&#39;s prediction outputs over the set of instances. The attributions are grouped by outputs. For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining. The baselineOutputValue, instanceOutputValue and featureAttributions fields are averaged over the test data. NOTE: Currently AutoML tabular classification Models produce only one attribution, which averages attributions over all the classes it predicts. Attribution.approximation_error is not populated. |  [optional] [readonly] |



