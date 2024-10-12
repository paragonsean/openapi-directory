

# S3JobDefinition

Specifies which S3 buckets contain the objects that a classification job analyzes, and the scope of that analysis. The bucket specification can be static (bucketDefinitions) or dynamic (bucketCriteria). If it's static, the job analyzes objects in the same predefined set of buckets each time the job runs. If it's dynamic, the job analyzes objects in any buckets that match the specified criteria each time the job starts to run.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bucketCriteria** | [**CreateClassificationJobRequestS3JobDefinitionBucketCriteria**](CreateClassificationJobRequestS3JobDefinitionBucketCriteria.md) |  |  [optional] |
|**bucketDefinitions** | [**List**](List.md) |  |  [optional] |
|**scoping** | [**CreateClassificationJobRequestS3JobDefinitionScoping**](CreateClassificationJobRequestS3JobDefinitionScoping.md) |  |  [optional] |



