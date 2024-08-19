

# DescribeTransformJobResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**transformJobName** | [**String**](String.md) |  |  |
|**transformJobArn** | [**String**](String.md) |  |  |
|**transformJobStatus** | [**TransformJobStatus**](TransformJobStatus.md) |  |  |
|**failureReason** | [**String**](String.md) |  |  [optional] |
|**modelName** | [**String**](String.md) |  |  |
|**maxConcurrentTransforms** | [**Integer**](Integer.md) |  |  [optional] |
|**modelClientConfig** | [**DescribeTransformJobResponseModelClientConfig**](DescribeTransformJobResponseModelClientConfig.md) |  |  [optional] |
|**maxPayloadInMB** | [**Integer**](Integer.md) |  |  [optional] |
|**batchStrategy** | [**BatchStrategy**](BatchStrategy.md) |  |  [optional] |
|**environment** | [**Map**](Map.md) |  |  [optional] |
|**transformInput** | [**DescribeTransformJobResponseTransformInput**](DescribeTransformJobResponseTransformInput.md) |  |  |
|**transformOutput** | [**DescribeTransformJobResponseTransformOutput**](DescribeTransformJobResponseTransformOutput.md) |  |  [optional] |
|**dataCaptureConfig** | [**CreateTransformJobRequestDataCaptureConfig**](CreateTransformJobRequestDataCaptureConfig.md) |  |  [optional] |
|**transformResources** | [**CreateTransformJobRequestTransformResources**](CreateTransformJobRequestTransformResources.md) |  |  |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**transformStartTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**transformEndTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**labelingJobArn** | [**String**](String.md) |  |  [optional] |
|**autoMLJobArn** | [**String**](String.md) |  |  [optional] |
|**dataProcessing** | [**DataProcessing**](DataProcessing.md) |  |  [optional] |
|**experimentConfig** | [**ExperimentConfig**](ExperimentConfig.md) |  |  [optional] |



