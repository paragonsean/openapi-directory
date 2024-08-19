# VertexAiApi.GoogleCloudAiplatformV1beta1BatchPredictionJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completionStats** | [**GoogleCloudAiplatformV1beta1CompletionStats**](GoogleCloudAiplatformV1beta1CompletionStats.md) |  | [optional] 
**createTime** | **String** | Output only. Time when the BatchPredictionJob was created. | [optional] [readonly] 
**dedicatedResources** | [**GoogleCloudAiplatformV1beta1BatchDedicatedResources**](GoogleCloudAiplatformV1beta1BatchDedicatedResources.md) |  | [optional] 
**disableContainerLogging** | **Boolean** | For custom-trained Models and AutoML Tabular Models, the container of the DeployedModel instances will send &#x60;stderr&#x60; and &#x60;stdout&#x60; streams to Cloud Logging by default. Please note that the logs incur cost, which are subject to [Cloud Logging pricing](https://cloud.google.com/logging/pricing). User can disable container logging by setting this flag to true. | [optional] 
**displayName** | **String** | Required. The user-defined name of this BatchPredictionJob. | [optional] 
**encryptionSpec** | [**GoogleCloudAiplatformV1beta1EncryptionSpec**](GoogleCloudAiplatformV1beta1EncryptionSpec.md) |  | [optional] 
**endTime** | **String** | Output only. Time when the BatchPredictionJob entered any of the following states: &#x60;JOB_STATE_SUCCEEDED&#x60;, &#x60;JOB_STATE_FAILED&#x60;, &#x60;JOB_STATE_CANCELLED&#x60;. | [optional] [readonly] 
**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 
**explanationSpec** | [**GoogleCloudAiplatformV1beta1ExplanationSpec**](GoogleCloudAiplatformV1beta1ExplanationSpec.md) |  | [optional] 
**generateExplanation** | **Boolean** | Generate explanation with the batch prediction results. When set to &#x60;true&#x60;, the batch prediction output changes based on the &#x60;predictions_format&#x60; field of the BatchPredictionJob.output_config object: * &#x60;bigquery&#x60;: output includes a column named &#x60;explanation&#x60;. The value is a struct that conforms to the Explanation object. * &#x60;jsonl&#x60;: The JSON objects on each line include an additional entry keyed &#x60;explanation&#x60;. The value of the entry is a JSON object that conforms to the Explanation object. * &#x60;csv&#x60;: Generating explanations for CSV format is not supported. If this field is set to true, either the Model.explanation_spec or explanation_spec must be populated. | [optional] 
**inputConfig** | [**GoogleCloudAiplatformV1beta1BatchPredictionJobInputConfig**](GoogleCloudAiplatformV1beta1BatchPredictionJobInputConfig.md) |  | [optional] 
**instanceConfig** | [**GoogleCloudAiplatformV1beta1BatchPredictionJobInstanceConfig**](GoogleCloudAiplatformV1beta1BatchPredictionJobInstanceConfig.md) |  | [optional] 
**labels** | **{String: String}** | The labels with user-defined metadata to organize BatchPredictionJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. | [optional] 
**manualBatchTuningParameters** | [**GoogleCloudAiplatformV1beta1ManualBatchTuningParameters**](GoogleCloudAiplatformV1beta1ManualBatchTuningParameters.md) |  | [optional] 
**model** | **String** | The name of the Model resource that produces the predictions via this job, must share the same ancestor Location. Starting this job has no impact on any existing deployments of the Model and their resources. Exactly one of model and unmanaged_container_model must be set. The model resource name may contain version id or version alias to specify the version. Example: &#x60;projects/{project}/locations/{location}/models/{model}@2&#x60; or &#x60;projects/{project}/locations/{location}/models/{model}@golden&#x60; if no version is specified, the default version will be deployed. The model resource could also be a publisher model. Example: &#x60;publishers/{publisher}/models/{model}&#x60; or &#x60;projects/{project}/locations/{location}/publishers/{publisher}/models/{model}&#x60; | [optional] 
**modelMonitoringConfig** | [**GoogleCloudAiplatformV1beta1ModelMonitoringConfig**](GoogleCloudAiplatformV1beta1ModelMonitoringConfig.md) |  | [optional] 
**modelMonitoringStatsAnomalies** | [**[GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomalies]**](GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomalies.md) | Get batch prediction job monitoring statistics. | [optional] 
**modelMonitoringStatus** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 
**modelParameters** | **Object** | The parameters that govern the predictions. The schema of the parameters may be specified via the Model&#39;s PredictSchemata&#39;s parameters_schema_uri. | [optional] 
**modelVersionId** | **String** | Output only. The version ID of the Model that produces the predictions via this job. | [optional] [readonly] 
**name** | **String** | Output only. Resource name of the BatchPredictionJob. | [optional] [readonly] 
**outputConfig** | [**GoogleCloudAiplatformV1beta1BatchPredictionJobOutputConfig**](GoogleCloudAiplatformV1beta1BatchPredictionJobOutputConfig.md) |  | [optional] 
**outputInfo** | [**GoogleCloudAiplatformV1beta1BatchPredictionJobOutputInfo**](GoogleCloudAiplatformV1beta1BatchPredictionJobOutputInfo.md) |  | [optional] 
**partialFailures** | [**[GoogleRpcStatus]**](GoogleRpcStatus.md) | Output only. Partial failures encountered. For example, single files that can&#39;t be read. This field never exceeds 20 entries. Status details fields contain standard Google Cloud error details. | [optional] [readonly] 
**resourcesConsumed** | [**GoogleCloudAiplatformV1beta1ResourcesConsumed**](GoogleCloudAiplatformV1beta1ResourcesConsumed.md) |  | [optional] 
**serviceAccount** | **String** | The service account that the DeployedModel&#39;s container runs as. If not specified, a system generated one will be used, which has minimal permissions and the custom container, if used, may not have enough permission to access other Google Cloud resources. Users deploying the Model must have the &#x60;iam.serviceAccounts.actAs&#x60; permission on this service account. | [optional] 
**startTime** | **String** | Output only. Time when the BatchPredictionJob for the first time entered the &#x60;JOB_STATE_RUNNING&#x60; state. | [optional] [readonly] 
**state** | **String** | Output only. The detailed state of the job. | [optional] [readonly] 
**unmanagedContainerModel** | [**GoogleCloudAiplatformV1beta1UnmanagedContainerModel**](GoogleCloudAiplatformV1beta1UnmanagedContainerModel.md) |  | [optional] 
**updateTime** | **String** | Output only. Time when the BatchPredictionJob was most recently updated. | [optional] [readonly] 



## Enum: StateEnum


* `UNSPECIFIED` (value: `"JOB_STATE_UNSPECIFIED"`)

* `QUEUED` (value: `"JOB_STATE_QUEUED"`)

* `PENDING` (value: `"JOB_STATE_PENDING"`)

* `RUNNING` (value: `"JOB_STATE_RUNNING"`)

* `SUCCEEDED` (value: `"JOB_STATE_SUCCEEDED"`)

* `FAILED` (value: `"JOB_STATE_FAILED"`)

* `CANCELLING` (value: `"JOB_STATE_CANCELLING"`)

* `CANCELLED` (value: `"JOB_STATE_CANCELLED"`)

* `PAUSED` (value: `"JOB_STATE_PAUSED"`)

* `EXPIRED` (value: `"JOB_STATE_EXPIRED"`)

* `UPDATING` (value: `"JOB_STATE_UPDATING"`)

* `PARTIALLY_SUCCEEDED` (value: `"JOB_STATE_PARTIALLY_SUCCEEDED"`)




