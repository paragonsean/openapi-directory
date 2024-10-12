

# GoogleCloudAiplatformV1beta1TensorboardExperiment

A TensorboardExperiment is a group of TensorboardRuns, that are typically the results of a training job run, in a Tensorboard.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Timestamp when this TensorboardExperiment was created. |  [optional] [readonly] |
|**description** | **String** | Description of this TensorboardExperiment. |  [optional] |
|**displayName** | **String** | User provided name of this TensorboardExperiment. |  [optional] |
|**etag** | **String** | Used to perform consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The labels with user-defined metadata to organize your TensorboardExperiment. Label keys and values cannot be longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Dataset (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with &#x60;aiplatform.googleapis.com/&#x60; and are immutable. The following system labels exist for each Dataset: * &#x60;aiplatform.googleapis.com/dataset_metadata_schema&#x60;: output only. Its value is the metadata_schema&#39;s title. |  [optional] |
|**name** | **String** | Output only. Name of the TensorboardExperiment. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}&#x60; |  [optional] [readonly] |
|**source** | **String** | Immutable. Source of the TensorboardExperiment. Example: a custom training job. |  [optional] |
|**updateTime** | **String** | Output only. Timestamp when this TensorboardExperiment was last updated. |  [optional] [readonly] |



