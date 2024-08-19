

# InputDataConfig

<p>Contains the Amazon S3 location of the training data you want to use to create a new custom language model, and permissions to access this location.</p> <p>When using <code>InputDataConfig</code>, you must include these sub-parameters: <code>S3Uri</code> and <code>DataAccessRoleArn</code>. You can optionally include <code>TuningDataS3Uri</code>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**s3Uri** | [**String**](String.md) |  |  |
|**tuningDataS3Uri** | [**String**](String.md) |  |  [optional] |
|**dataAccessRoleArn** | [**String**](String.md) |  |  |



