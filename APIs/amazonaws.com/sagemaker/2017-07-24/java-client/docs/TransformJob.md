

# TransformJob

A batch transform job. For information about SageMaker batch transform, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html\">Use Batch Transform</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**transformJobName** | [**String**](String.md) |  |  [optional] |
|**transformJobArn** | [**String**](String.md) |  |  [optional] |
|**transformJobStatus** | [**TransformJobStatus**](TransformJobStatus.md) |  |  [optional] |
|**failureReason** | [**String**](String.md) |  |  [optional] |
|**modelName** | [**String**](String.md) |  |  [optional] |
|**maxConcurrentTransforms** | [**Integer**](Integer.md) |  |  [optional] |
|**modelClientConfig** | [**ModelClientConfig**](ModelClientConfig.md) |  |  [optional] |
|**maxPayloadInMB** | [**Integer**](Integer.md) |  |  [optional] |
|**batchStrategy** | [**BatchStrategy**](BatchStrategy.md) |  |  [optional] |
|**environment** | [**Map**](Map.md) |  |  [optional] |
|**transformInput** | [**TransformInput**](TransformInput.md) |  |  [optional] |
|**transformOutput** | [**TransformOutput**](TransformOutput.md) |  |  [optional] |
|**transformResources** | [**TransformResources**](TransformResources.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**transformStartTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**transformEndTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**labelingJobArn** | [**String**](String.md) |  |  [optional] |
|**autoMLJobArn** | [**String**](String.md) |  |  [optional] |
|**dataProcessing** | [**DataProcessing**](DataProcessing.md) |  |  [optional] |
|**experimentConfig** | [**ExperimentConfig**](ExperimentConfig.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**dataCaptureConfig** | [**BatchDataCaptureConfig**](BatchDataCaptureConfig.md) |  |  [optional] |



