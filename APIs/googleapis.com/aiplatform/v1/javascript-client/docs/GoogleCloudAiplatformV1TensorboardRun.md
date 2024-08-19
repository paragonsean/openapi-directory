# VertexAiApi.GoogleCloudAiplatformV1TensorboardRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Timestamp when this TensorboardRun was created. | [optional] [readonly] 
**description** | **String** | Description of this TensorboardRun. | [optional] 
**displayName** | **String** | Required. User provided name of this TensorboardRun. This value must be unique among all TensorboardRuns belonging to the same parent TensorboardExperiment. | [optional] 
**etag** | **String** | Used to perform a consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. | [optional] 
**labels** | **{String: String}** | The labels with user-defined metadata to organize your TensorboardRuns. This field will be used to filter and visualize Runs in the Tensorboard UI. For example, a Vertex AI training job can set a label aiplatform.googleapis.com/training_job_id&#x3D;xxxxx to all the runs created within that job. An end user can set a label experiment_id&#x3D;xxxxx for all the runs produced in a Jupyter notebook. These runs can be grouped by a label value and visualized together in the Tensorboard UI. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one TensorboardRun (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with \&quot;aiplatform.googleapis.com/\&quot; and are immutable. | [optional] 
**name** | **String** | Output only. Name of the TensorboardRun. Format: &#x60;projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}/runs/{run}&#x60; | [optional] [readonly] 
**updateTime** | **String** | Output only. Timestamp when this TensorboardRun was last updated. | [optional] [readonly] 


