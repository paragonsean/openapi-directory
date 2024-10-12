

# GoogleCloudAiplatformV1Model

A trained machine learning Model.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artifactUri** | **String** | Immutable. The path to the directory containing the Model artifact and any of its supporting files. Not required for AutoML Models. |  [optional] |
|**containerSpec** | [**GoogleCloudAiplatformV1ModelContainerSpec**](GoogleCloudAiplatformV1ModelContainerSpec.md) |  |  [optional] |
|**createTime** | **String** | Output only. Timestamp when this Model was uploaded into Vertex AI. |  [optional] [readonly] |
|**dataStats** | [**GoogleCloudAiplatformV1ModelDataStats**](GoogleCloudAiplatformV1ModelDataStats.md) |  |  [optional] |
|**deployedModels** | [**List&lt;GoogleCloudAiplatformV1DeployedModelRef&gt;**](GoogleCloudAiplatformV1DeployedModelRef.md) | Output only. The pointers to DeployedModels created from this Model. Note that Model could have been deployed to Endpoints in different Locations. |  [optional] [readonly] |
|**description** | **String** | The description of the Model. |  [optional] |
|**displayName** | **String** | Required. The display name of the Model. The name can be up to 128 characters long and can consist of any UTF-8 characters. |  [optional] |
|**encryptionSpec** | [**GoogleCloudAiplatformV1EncryptionSpec**](GoogleCloudAiplatformV1EncryptionSpec.md) |  |  [optional] |
|**etag** | **String** | Used to perform consistent read-modify-write updates. If not set, a blind \&quot;overwrite\&quot; update happens. |  [optional] |
|**explanationSpec** | [**GoogleCloudAiplatformV1ExplanationSpec**](GoogleCloudAiplatformV1ExplanationSpec.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The labels with user-defined metadata to organize your Models. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |  [optional] |
|**metadata** | **Object** | Immutable. An additional information about the Model; the schema of the metadata can be found in metadata_schema. Unset if the Model does not have any additional information. |  [optional] |
|**metadataArtifact** | **String** | Output only. The resource name of the Artifact that was created in MetadataStore when creating the Model. The Artifact resource name pattern is &#x60;projects/{project}/locations/{location}/metadataStores/{metadata_store}/artifacts/{artifact}&#x60;. |  [optional] [readonly] |
|**metadataSchemaUri** | **String** | Immutable. Points to a YAML file stored on Google Cloud Storage describing additional information about the Model, that is specific to it. Unset if the Model does not have any additional information. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). AutoML Models always have this field populated by Vertex AI, if no additional metadata is needed, this field is set to an empty string. Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access. |  [optional] |
|**modelSourceInfo** | [**GoogleCloudAiplatformV1ModelSourceInfo**](GoogleCloudAiplatformV1ModelSourceInfo.md) |  |  [optional] |
|**name** | **String** | The resource name of the Model. |  [optional] |
|**originalModelInfo** | [**GoogleCloudAiplatformV1ModelOriginalModelInfo**](GoogleCloudAiplatformV1ModelOriginalModelInfo.md) |  |  [optional] |
|**pipelineJob** | **String** | Optional. This field is populated if the model is produced by a pipeline job. |  [optional] |
|**predictSchemata** | [**GoogleCloudAiplatformV1PredictSchemata**](GoogleCloudAiplatformV1PredictSchemata.md) |  |  [optional] |
|**supportedDeploymentResourcesTypes** | [**List&lt;SupportedDeploymentResourcesTypesEnum&gt;**](#List&lt;SupportedDeploymentResourcesTypesEnum&gt;) | Output only. When this Model is deployed, its prediction resources are described by the &#x60;prediction_resources&#x60; field of the Endpoint.deployed_models object. Because not all Models support all resource configuration types, the configuration types this Model supports are listed here. If no configuration types are listed, the Model cannot be deployed to an Endpoint and does not support online predictions (PredictionService.Predict or PredictionService.Explain). Such a Model can serve predictions by using a BatchPredictionJob, if it has at least one entry each in supported_input_storage_formats and supported_output_storage_formats. |  [optional] [readonly] |
|**supportedExportFormats** | [**List&lt;GoogleCloudAiplatformV1ModelExportFormat&gt;**](GoogleCloudAiplatformV1ModelExportFormat.md) | Output only. The formats in which this Model may be exported. If empty, this Model is not available for export. |  [optional] [readonly] |
|**supportedInputStorageFormats** | **List&lt;String&gt;** | Output only. The formats this Model supports in BatchPredictionJob.input_config. If PredictSchemata.instance_schema_uri exists, the instances should be given as per that schema. The possible formats are: * &#x60;jsonl&#x60; The JSON Lines format, where each instance is a single line. Uses GcsSource. * &#x60;csv&#x60; The CSV format, where each instance is a single comma-separated line. The first line in the file is the header, containing comma-separated field names. Uses GcsSource. * &#x60;tf-record&#x60; The TFRecord format, where each instance is a single record in tfrecord syntax. Uses GcsSource. * &#x60;tf-record-gzip&#x60; Similar to &#x60;tf-record&#x60;, but the file is gzipped. Uses GcsSource. * &#x60;bigquery&#x60; Each instance is a single row in BigQuery. Uses BigQuerySource. * &#x60;file-list&#x60; Each line of the file is the location of an instance to process, uses &#x60;gcs_source&#x60; field of the InputConfig object. If this Model doesn&#39;t support any of these formats it means it cannot be used with a BatchPredictionJob. However, if it has supported_deployment_resources_types, it could serve online predictions by using PredictionService.Predict or PredictionService.Explain. |  [optional] [readonly] |
|**supportedOutputStorageFormats** | **List&lt;String&gt;** | Output only. The formats this Model supports in BatchPredictionJob.output_config. If both PredictSchemata.instance_schema_uri and PredictSchemata.prediction_schema_uri exist, the predictions are returned together with their instances. In other words, the prediction has the original instance data first, followed by the actual prediction content (as per the schema). The possible formats are: * &#x60;jsonl&#x60; The JSON Lines format, where each prediction is a single line. Uses GcsDestination. * &#x60;csv&#x60; The CSV format, where each prediction is a single comma-separated line. The first line in the file is the header, containing comma-separated field names. Uses GcsDestination. * &#x60;bigquery&#x60; Each prediction is a single row in a BigQuery table, uses BigQueryDestination . If this Model doesn&#39;t support any of these formats it means it cannot be used with a BatchPredictionJob. However, if it has supported_deployment_resources_types, it could serve online predictions by using PredictionService.Predict or PredictionService.Explain. |  [optional] [readonly] |
|**trainingPipeline** | **String** | Output only. The resource name of the TrainingPipeline that uploaded this Model, if any. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Timestamp when this Model was most recently updated. |  [optional] [readonly] |
|**versionAliases** | **List&lt;String&gt;** | User provided version aliases so that a model version can be referenced via alias (i.e. &#x60;projects/{project}/locations/{location}/models/{model_id}@{version_alias}&#x60; instead of auto-generated version id (i.e. &#x60;projects/{project}/locations/{location}/models/{model_id}@{version_id})&#x60;. The format is a-z{0,126}[a-z0-9] to distinguish from version_id. A default version alias will be created for the first version of the model, and there must be exactly one default version alias for a model. |  [optional] |
|**versionCreateTime** | **String** | Output only. Timestamp when this version was created. |  [optional] [readonly] |
|**versionDescription** | **String** | The description of this version. |  [optional] |
|**versionId** | **String** | Output only. Immutable. The version ID of the model. A new version is committed when a new model version is uploaded or trained under an existing model id. It is an auto-incrementing decimal number in string representation. |  [optional] [readonly] |
|**versionUpdateTime** | **String** | Output only. Timestamp when this version was most recently updated. |  [optional] [readonly] |



## Enum: List&lt;SupportedDeploymentResourcesTypesEnum&gt;

| Name | Value |
|---- | -----|
| DEPLOYMENT_RESOURCES_TYPE_UNSPECIFIED | &quot;DEPLOYMENT_RESOURCES_TYPE_UNSPECIFIED&quot; |
| DEDICATED_RESOURCES | &quot;DEDICATED_RESOURCES&quot; |
| AUTOMATIC_RESOURCES | &quot;AUTOMATIC_RESOURCES&quot; |
| SHARED_RESOURCES | &quot;SHARED_RESOURCES&quot; |



