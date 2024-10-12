

# UpdateMatchingWorkflowRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A description of the workflow. |  [optional] |
|**incrementalRunConfig** | [**CreateMatchingWorkflowRequestIncrementalRunConfig**](CreateMatchingWorkflowRequestIncrementalRunConfig.md) |  |  [optional] |
|**inputSourceConfig** | [**List&lt;InputSource&gt;**](InputSource.md) | A list of &lt;code&gt;InputSource&lt;/code&gt; objects, which have the fields &lt;code&gt;InputSourceARN&lt;/code&gt; and &lt;code&gt;SchemaName&lt;/code&gt;. |  |
|**outputSourceConfig** | [**List&lt;OutputSource&gt;**](OutputSource.md) | A list of &lt;code&gt;OutputSource&lt;/code&gt; objects, each of which contains fields &lt;code&gt;OutputS3Path&lt;/code&gt;, &lt;code&gt;ApplyNormalization&lt;/code&gt;, and &lt;code&gt;Output&lt;/code&gt;. |  |
|**resolutionTechniques** | [**CreateMatchingWorkflowRequestResolutionTechniques**](CreateMatchingWorkflowRequestResolutionTechniques.md) |  |  |
|**roleArn** | **String** | The Amazon Resource Name (ARN) of the IAM role. AWS Entity Resolution assumes this role to create resources on your behalf as part of workflow execution. |  |



