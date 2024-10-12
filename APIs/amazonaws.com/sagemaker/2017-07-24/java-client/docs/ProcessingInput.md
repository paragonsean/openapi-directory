

# ProcessingInput

The inputs for a processing job. The processing input must specify exactly one of either <code>S3Input</code> or <code>DatasetDefinition</code> types.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inputName** | [**String**](String.md) |  |  |
|**appManaged** | [**Boolean**](Boolean.md) |  |  [optional] |
|**s3Input** | [**ProcessingInputS3Input**](ProcessingInputS3Input.md) |  |  [optional] |
|**datasetDefinition** | [**ProcessingInputDatasetDefinition**](ProcessingInputDatasetDefinition.md) |  |  [optional] |



