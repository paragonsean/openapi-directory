# VertexAiApi.GoogleCloudAiplatformV1Explanation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributions** | [**[GoogleCloudAiplatformV1Attribution]**](GoogleCloudAiplatformV1Attribution.md) | Output only. Feature attributions grouped by predicted outputs. For Models that predict only one output, such as regression Models that predict only one score, there is only one attibution that explains the predicted output. For Models that predict multiple outputs, such as multiclass Models that predict multiple classes, each element explains one specific item. Attribution.output_index can be used to identify which output this attribution is explaining. By default, we provide Shapley values for the predicted class. However, you can configure the explanation request to generate Shapley values for any other classes too. For example, if a model predicts a probability of &#x60;0.4&#x60; for approving a loan application, the model&#39;s decision is to reject the application since &#x60;p(reject) &#x3D; 0.6 &gt; p(approve) &#x3D; 0.4&#x60;, and the default Shapley values would be computed for rejection decision and not approval, even though the latter might be the positive class. If users set ExplanationParameters.top_k, the attributions are sorted by instance_output_value in descending order. If ExplanationParameters.output_indices is specified, the attributions are stored by Attribution.output_index in the same order as they appear in the output_indices. | [optional] [readonly] 
**neighbors** | [**[GoogleCloudAiplatformV1Neighbor]**](GoogleCloudAiplatformV1Neighbor.md) | Output only. List of the nearest neighbors for example-based explanations. For models deployed with the examples explanations feature enabled, the attributions field is empty and instead the neighbors field is populated. | [optional] [readonly] 


