

# CreateQuantumTaskRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | **String** | The action associated with the task. |  |
|**clientToken** | **String** | The client token associated with the request. |  |
|**deviceArn** | **String** | The ARN of the device to run the task on. |  |
|**deviceParameters** | **String** | The parameters for the device to run the task on. |  [optional] |
|**jobToken** | **String** | The token for an Amazon Braket job that associates it with the quantum task. |  [optional] |
|**outputS3Bucket** | **String** | The S3 bucket to store task result files in. |  |
|**outputS3KeyPrefix** | **String** | The key prefix for the location in the S3 bucket to store task results in. |  |
|**shots** | **Integer** | The number of shots to use for the task. |  |
|**tags** | **Map&lt;String, String&gt;** | Tags to be added to the quantum task you&#39;re creating. |  [optional] |



