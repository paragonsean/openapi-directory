

# GoogleCloudAiplatformV1beta1TrainingPipeline

The TrainingPipeline orchestrates tasks associated with training a Model. It always executes the training task, and optionally may also export data from Vertex AI's Dataset which becomes the training input, upload the Model to Vertex AI, and evaluate the Model.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Time when the TrainingPipeline was created. |  [optional] [readonly] |
|**displayName** | **String** | Required. The user-defined name of this TrainingPipeline. |  [optional] |
|**encryptionSpec** | [**GoogleCloudAiplatformV1beta1EncryptionSpec**](GoogleCloudAiplatformV1beta1EncryptionSpec.md) |  |  [optional] |
|**endTime** | **String** | Output only. Time when the TrainingPipeline entered any of the following states: &#x60;PIPELINE_STATE_SUCCEEDED&#x60;, &#x60;PIPELINE_STATE_FAILED&#x60;, &#x60;PIPELINE_STATE_CANCELLED&#x60;. |  [optional] [readonly] |
|**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |
|**inputDataConfig** | [**GoogleCloudAiplatformV1beta1InputDataConfig**](GoogleCloudAiplatformV1beta1InputDataConfig.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The labels with user-defined metadata to organize TrainingPipelines. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |  [optional] |
|**modelId** | **String** | Optional. The ID to use for the uploaded Model, which will become the final component of the model resource name. This value may be up to 63 characters, and valid characters are &#x60;[a-z0-9_-]&#x60;. The first character cannot be a number or hyphen. |  [optional] |
|**modelToUpload** | [**GoogleCloudAiplatformV1beta1Model**](GoogleCloudAiplatformV1beta1Model.md) |  |  [optional] |
|**name** | **String** | Output only. Resource name of the TrainingPipeline. |  [optional] [readonly] |
|**parentModel** | **String** | Optional. When specify this field, the &#x60;model_to_upload&#x60; will not be uploaded as a new model, instead, it will become a new version of this &#x60;parent_model&#x60;. |  [optional] |
|**startTime** | **String** | Output only. Time when the TrainingPipeline for the first time entered the &#x60;PIPELINE_STATE_RUNNING&#x60; state. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The detailed state of the pipeline. |  [optional] [readonly] |
|**trainingTaskDefinition** | **String** | Required. A Google Cloud Storage path to the YAML file that defines the training task which is responsible for producing the model artifact, and may also include additional auxiliary work. The definition files that can be used here are found in gs://google-cloud-aiplatform/schema/trainingjob/definition/. Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access. |  [optional] |
|**trainingTaskInputs** | **Object** | Required. The training task&#39;s parameter(s), as specified in the training_task_definition&#39;s &#x60;inputs&#x60;. |  [optional] |
|**trainingTaskMetadata** | **Object** | Output only. The metadata information as specified in the training_task_definition&#39;s &#x60;metadata&#x60;. This metadata is an auxiliary runtime and final information about the training task. While the pipeline is running this information is populated only at a best effort basis. Only present if the pipeline&#39;s training_task_definition contains &#x60;metadata&#x60; object. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Time when the TrainingPipeline was most recently updated. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PIPELINE_STATE_UNSPECIFIED&quot; |
| QUEUED | &quot;PIPELINE_STATE_QUEUED&quot; |
| PENDING | &quot;PIPELINE_STATE_PENDING&quot; |
| RUNNING | &quot;PIPELINE_STATE_RUNNING&quot; |
| SUCCEEDED | &quot;PIPELINE_STATE_SUCCEEDED&quot; |
| FAILED | &quot;PIPELINE_STATE_FAILED&quot; |
| CANCELLING | &quot;PIPELINE_STATE_CANCELLING&quot; |
| CANCELLED | &quot;PIPELINE_STATE_CANCELLED&quot; |
| PAUSED | &quot;PIPELINE_STATE_PAUSED&quot; |



