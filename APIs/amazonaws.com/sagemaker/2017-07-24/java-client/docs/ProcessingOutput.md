

# ProcessingOutput

Describes the results of a processing job. The processing output must specify exactly one of either <code>S3Output</code> or <code>FeatureStoreOutput</code> types.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**outputName** | [**String**](String.md) |  |  |
|**s3Output** | [**ProcessingOutputS3Output**](ProcessingOutputS3Output.md) |  |  [optional] |
|**featureStoreOutput** | [**ProcessingOutputFeatureStoreOutput**](ProcessingOutputFeatureStoreOutput.md) |  |  [optional] |
|**appManaged** | [**Boolean**](Boolean.md) |  |  [optional] |



