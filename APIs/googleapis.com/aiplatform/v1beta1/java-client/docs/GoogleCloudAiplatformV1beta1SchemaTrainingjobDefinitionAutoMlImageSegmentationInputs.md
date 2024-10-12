

# GoogleCloudAiplatformV1beta1SchemaTrainingjobDefinitionAutoMlImageSegmentationInputs


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseModelId** | **String** | The ID of the &#x60;base&#x60; model. If it is specified, the new model will be trained based on the &#x60;base&#x60; model. Otherwise, the new model will be trained from scratch. The &#x60;base&#x60; model must be in the same Project and Location as the new Model to train, and have the same modelType. |  [optional] |
|**budgetMilliNodeHours** | **String** | The training budget of creating this model, expressed in milli node hours i.e. 1,000 value in this field means 1 node hour. The actual metadata.costMilliNodeHours will be equal or less than this value. If further model training ceases to provide any improvements, it will stop without using the full budget and the metadata.successfulStopReason will be &#x60;model-converged&#x60;. Note, node_hour &#x3D; actual_hour * number_of_nodes_involved. Or actual_wall_clock_hours &#x3D; train_budget_milli_node_hours / (number_of_nodes_involved * 1000) For modelType &#x60;cloud-high-accuracy-1&#x60;(default), the budget must be between 20,000 and 2,000,000 milli node hours, inclusive. The default value is 192,000 which represents one day in wall time (1000 milli * 24 hours * 8 nodes). |  [optional] |
|**modelType** | [**ModelTypeEnum**](#ModelTypeEnum) |  |  [optional] |



## Enum: ModelTypeEnum

| Name | Value |
|---- | -----|
| MODEL_TYPE_UNSPECIFIED | &quot;MODEL_TYPE_UNSPECIFIED&quot; |
| CLOUD_HIGH_ACCURACY_1 | &quot;CLOUD_HIGH_ACCURACY_1&quot; |
| CLOUD_LOW_ACCURACY_1 | &quot;CLOUD_LOW_ACCURACY_1&quot; |
| MOBILE_TF_LOW_LATENCY_1 | &quot;MOBILE_TF_LOW_LATENCY_1&quot; |



