# AiPlatformTrainingPredictionApi.GoogleCloudMlV1PredictionInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batchSize** | **String** | Optional. Number of records per batch, defaults to 64. The service will buffer batch_size number of records in memory before invoking one Tensorflow prediction call internally. So take the record size and memory available into consideration when setting this parameter. | [optional] 
**dataFormat** | **String** | Required. The format of the input data files. | [optional] 
**inputPaths** | **[String]** | Required. The Cloud Storage location of the input data files. May contain wildcards. | [optional] 
**maxWorkerCount** | **String** | Optional. The maximum number of workers to be used for parallel processing. Defaults to 10 if not specified. | [optional] 
**modelName** | **String** | Use this field if you want to use the default version for the specified model. The string must use the following format: &#x60;\&quot;projects/YOUR_PROJECT/models/YOUR_MODEL\&quot;&#x60; | [optional] 
**outputDataFormat** | **String** | Optional. Format of the output data files, defaults to JSON. | [optional] 
**outputPath** | **String** | Required. The output Google Cloud Storage location. | [optional] 
**region** | **String** | Required. The Google Compute Engine region to run the prediction job in. See the available regions for AI Platform services. | [optional] 
**runtimeVersion** | **String** | Optional. The AI Platform runtime version to use for this batch prediction. If not set, AI Platform will pick the runtime version used during the CreateVersion request for this model version, or choose the latest stable version when model version information is not available such as when the model is specified by uri. | [optional] 
**signatureName** | **String** | Optional. The name of the signature defined in the SavedModel to use for this job. Please refer to [SavedModel](https://tensorflow.github.io/serving/serving_basic.html) for information about how to use signatures. Defaults to [DEFAULT_SERVING_SIGNATURE_DEF_KEY](https://www.tensorflow.org/api_docs/python/tf/saved_model/signature_constants) , which is \&quot;serving_default\&quot;. | [optional] 
**uri** | **String** | Use this field if you want to specify a Google Cloud Storage path for the model to use. | [optional] 
**versionName** | **String** | Use this field if you want to specify a version of the model to use. The string is formatted the same way as &#x60;model_version&#x60;, with the addition of the version information: &#x60;\&quot;projects/YOUR_PROJECT/models/YOUR_MODEL/versions/YOUR_VERSION\&quot;&#x60; | [optional] 



## Enum: DataFormatEnum


* `DATA_FORMAT_UNSPECIFIED` (value: `"DATA_FORMAT_UNSPECIFIED"`)

* `JSON` (value: `"JSON"`)

* `TEXT` (value: `"TEXT"`)

* `TF_RECORD` (value: `"TF_RECORD"`)

* `TF_RECORD_GZIP` (value: `"TF_RECORD_GZIP"`)

* `CSV` (value: `"CSV"`)





## Enum: OutputDataFormatEnum


* `DATA_FORMAT_UNSPECIFIED` (value: `"DATA_FORMAT_UNSPECIFIED"`)

* `JSON` (value: `"JSON"`)

* `TEXT` (value: `"TEXT"`)

* `TF_RECORD` (value: `"TF_RECORD"`)

* `TF_RECORD_GZIP` (value: `"TF_RECORD_GZIP"`)

* `CSV` (value: `"CSV"`)




