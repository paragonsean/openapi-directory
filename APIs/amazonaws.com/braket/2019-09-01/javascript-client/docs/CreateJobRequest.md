# Braket.CreateJobRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithmSpecification** | [**CreateJobRequestAlgorithmSpecification**](CreateJobRequestAlgorithmSpecification.md) |  | 
**checkpointConfig** | [**CreateJobRequestCheckpointConfig**](CreateJobRequestCheckpointConfig.md) |  | [optional] 
**clientToken** | **String** | A unique token that guarantees that the call to this API is idempotent. | 
**deviceConfig** | [**CreateJobRequestDeviceConfig**](CreateJobRequestDeviceConfig.md) |  | 
**hyperParameters** | **{String: String}** | Algorithm-specific parameters used by an Amazon Braket job that influence the quality of the training job. The values are set with a string of JSON key:value pairs, where the key is the name of the hyperparameter and the value is the value of th hyperparameter. | [optional] 
**inputDataConfig** | [**[InputFileConfig]**](InputFileConfig.md) | A list of parameters that specify the name and type of input data and where it is located. | [optional] 
**instanceConfig** | [**CreateJobRequestInstanceConfig**](CreateJobRequestInstanceConfig.md) |  | 
**jobName** | **String** | The name of the Amazon Braket job. | 
**outputDataConfig** | [**CreateJobRequestOutputDataConfig**](CreateJobRequestOutputDataConfig.md) |  | 
**roleArn** | **String** | The Amazon Resource Name (ARN) of an IAM role that Amazon Braket can assume to perform tasks on behalf of a user. It can access user resources, run an Amazon Braket job container on behalf of user, and output resources to the users&#39; s3 buckets. | 
**stoppingCondition** | [**CreateJobRequestStoppingCondition**](CreateJobRequestStoppingCondition.md) |  | [optional] 
**tags** | **{String: String}** | A tag object that consists of a key and an optional value, used to manage metadata for Amazon Braket resources. | [optional] 


