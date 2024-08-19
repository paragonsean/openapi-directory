

# GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageObjectDetectionInputs


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**budgetMilliNodeHours** | **String** | The training budget of creating this model, expressed in milli node hours i.e. 1,000 value in this field means 1 node hour. The actual metadata.costMilliNodeHours will be equal or less than this value. If further model training ceases to provide any improvements, it will stop without using the full budget and the metadata.successfulStopReason will be &#x60;model-converged&#x60;. Note, node_hour &#x3D; actual_hour * number_of_nodes_involved. For modelType &#x60;cloud&#x60;(default), the budget must be between 20,000 and 900,000 milli node hours, inclusive. The default value is 216,000 which represents one day in wall time, considering 9 nodes are used. For model types &#x60;mobile-tf-low-latency-1&#x60;, &#x60;mobile-tf-versatile-1&#x60;, &#x60;mobile-tf-high-accuracy-1&#x60; the training budget must be between 1,000 and 100,000 milli node hours, inclusive. The default value is 24,000 which represents one day in wall time on a single node that is used. |  [optional] |
|**disableEarlyStopping** | **Boolean** | Use the entire training budget. This disables the early stopping feature. When false the early stopping feature is enabled, which means that AutoML Image Object Detection might stop training before the entire training budget has been used. |  [optional] |
|**modelType** | [**ModelTypeEnum**](#ModelTypeEnum) |  |  [optional] |
|**tunableParameter** | [**GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutomlImageTrainingTunableParameter**](GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutomlImageTrainingTunableParameter.md) |  |  [optional] |
|**uptrainBaseModelId** | **String** | The ID of &#x60;base&#x60; model for upTraining. If it is specified, the new model will be upTrained based on the &#x60;base&#x60; model for upTraining. Otherwise, the new model will be trained from scratch. The &#x60;base&#x60; model for upTraining must be in the same Project and Location as the new Model to train, and have the same modelType. |  [optional] |



## Enum: ModelTypeEnum

| Name | Value |
|---- | -----|
| MODEL_TYPE_UNSPECIFIED | &quot;MODEL_TYPE_UNSPECIFIED&quot; |
| CLOUD_HIGH_ACCURACY_1 | &quot;CLOUD_HIGH_ACCURACY_1&quot; |
| CLOUD_LOW_LATENCY_1 | &quot;CLOUD_LOW_LATENCY_1&quot; |
| CLOUD_1 | &quot;CLOUD_1&quot; |
| MOBILE_TF_LOW_LATENCY_1 | &quot;MOBILE_TF_LOW_LATENCY_1&quot; |
| MOBILE_TF_VERSATILE_1 | &quot;MOBILE_TF_VERSATILE_1&quot; |
| MOBILE_TF_HIGH_ACCURACY_1 | &quot;MOBILE_TF_HIGH_ACCURACY_1&quot; |
| CLOUD_STREAMING_1 | &quot;CLOUD_STREAMING_1&quot; |
| SPINENET | &quot;SPINENET&quot; |
| YOLO | &quot;YOLO&quot; |



