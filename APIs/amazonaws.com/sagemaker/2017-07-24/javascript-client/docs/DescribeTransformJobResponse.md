# AmazonSageMakerService.DescribeTransformJobResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transformJobName** | **String** |  | 
**transformJobArn** | **String** |  | 
**transformJobStatus** | [**TransformJobStatus**](TransformJobStatus.md) |  | 
**failureReason** | **String** |  | [optional] 
**modelName** | **String** |  | 
**maxConcurrentTransforms** | **Number** |  | [optional] 
**modelClientConfig** | [**DescribeTransformJobResponseModelClientConfig**](DescribeTransformJobResponseModelClientConfig.md) |  | [optional] 
**maxPayloadInMB** | **Number** |  | [optional] 
**batchStrategy** | [**BatchStrategy**](BatchStrategy.md) |  | [optional] 
**environment** | **Object** |  | [optional] 
**transformInput** | [**DescribeTransformJobResponseTransformInput**](DescribeTransformJobResponseTransformInput.md) |  | 
**transformOutput** | [**DescribeTransformJobResponseTransformOutput**](DescribeTransformJobResponseTransformOutput.md) |  | [optional] 
**dataCaptureConfig** | [**CreateTransformJobRequestDataCaptureConfig**](CreateTransformJobRequestDataCaptureConfig.md) |  | [optional] 
**transformResources** | [**CreateTransformJobRequestTransformResources**](CreateTransformJobRequestTransformResources.md) |  | 
**creationTime** | **Date** |  | 
**transformStartTime** | **Date** |  | [optional] 
**transformEndTime** | **Date** |  | [optional] 
**labelingJobArn** | **String** |  | [optional] 
**autoMLJobArn** | **String** |  | [optional] 
**dataProcessing** | [**DataProcessing**](DataProcessing.md) |  | [optional] 
**experimentConfig** | [**ExperimentConfig**](ExperimentConfig.md) |  | [optional] 


