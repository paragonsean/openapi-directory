# AmazonEventBridge.Target

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** |  | 
**arn** | **String** |  | 
**roleArn** | **String** |  | [optional] 
**input** | **String** |  | [optional] 
**inputPath** | **String** |  | [optional] 
**inputTransformer** | [**TargetInputTransformer**](TargetInputTransformer.md) |  | [optional] 
**kinesisParameters** | [**TargetKinesisParameters**](TargetKinesisParameters.md) |  | [optional] 
**runCommandParameters** | [**TargetRunCommandParameters**](TargetRunCommandParameters.md) |  | [optional] 
**ecsParameters** | [**TargetEcsParameters**](TargetEcsParameters.md) |  | [optional] 
**batchParameters** | [**TargetBatchParameters**](TargetBatchParameters.md) |  | [optional] 
**sqsParameters** | [**TargetSqsParameters**](TargetSqsParameters.md) |  | [optional] 
**httpParameters** | [**TargetHttpParameters**](TargetHttpParameters.md) |  | [optional] 
**redshiftDataParameters** | [**TargetRedshiftDataParameters**](TargetRedshiftDataParameters.md) |  | [optional] 
**sageMakerPipelineParameters** | [**TargetSageMakerPipelineParameters**](TargetSageMakerPipelineParameters.md) |  | [optional] 
**deadLetterConfig** | [**TargetDeadLetterConfig**](TargetDeadLetterConfig.md) |  | [optional] 
**retryPolicy** | [**TargetRetryPolicy**](TargetRetryPolicy.md) |  | [optional] 


