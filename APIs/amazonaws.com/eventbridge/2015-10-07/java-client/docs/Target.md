

# Target

<p>Targets are the resources to be invoked when a rule is triggered. For a complete list of services and resources that can be set as a target, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutTargets.html\">PutTargets</a>.</p> <p>If you are setting the event bus of another account as the target, and that account granted permission to your account through an organization instead of directly by the account ID, then you must specify a <code>RoleArn</code> with proper permissions in the <code>Target</code> structure. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-cross-account-event-delivery.html\">Sending and Receiving Events Between Amazon Web Services Accounts</a> in the <i>Amazon EventBridge User Guide</i>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**String**](String.md) |  |  |
|**arn** | [**String**](String.md) |  |  |
|**roleArn** | [**String**](String.md) |  |  [optional] |
|**input** | [**String**](String.md) |  |  [optional] |
|**inputPath** | [**String**](String.md) |  |  [optional] |
|**inputTransformer** | [**TargetInputTransformer**](TargetInputTransformer.md) |  |  [optional] |
|**kinesisParameters** | [**TargetKinesisParameters**](TargetKinesisParameters.md) |  |  [optional] |
|**runCommandParameters** | [**TargetRunCommandParameters**](TargetRunCommandParameters.md) |  |  [optional] |
|**ecsParameters** | [**TargetEcsParameters**](TargetEcsParameters.md) |  |  [optional] |
|**batchParameters** | [**TargetBatchParameters**](TargetBatchParameters.md) |  |  [optional] |
|**sqsParameters** | [**TargetSqsParameters**](TargetSqsParameters.md) |  |  [optional] |
|**httpParameters** | [**TargetHttpParameters**](TargetHttpParameters.md) |  |  [optional] |
|**redshiftDataParameters** | [**TargetRedshiftDataParameters**](TargetRedshiftDataParameters.md) |  |  [optional] |
|**sageMakerPipelineParameters** | [**TargetSageMakerPipelineParameters**](TargetSageMakerPipelineParameters.md) |  |  [optional] |
|**deadLetterConfig** | [**TargetDeadLetterConfig**](TargetDeadLetterConfig.md) |  |  [optional] |
|**retryPolicy** | [**TargetRetryPolicy**](TargetRetryPolicy.md) |  |  [optional] |



