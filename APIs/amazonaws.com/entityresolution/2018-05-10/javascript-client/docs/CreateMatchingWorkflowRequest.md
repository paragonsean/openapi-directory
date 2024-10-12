# AwsEntityResolution.CreateMatchingWorkflowRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A description of the workflow. | [optional] 
**incrementalRunConfig** | [**CreateMatchingWorkflowRequestIncrementalRunConfig**](CreateMatchingWorkflowRequestIncrementalRunConfig.md) |  | [optional] 
**inputSourceConfig** | [**[InputSource]**](InputSource.md) | A list of &lt;code&gt;InputSource&lt;/code&gt; objects, which have the fields &lt;code&gt;InputSourceARN&lt;/code&gt; and &lt;code&gt;SchemaName&lt;/code&gt;. | 
**outputSourceConfig** | [**[OutputSource]**](OutputSource.md) | A list of &lt;code&gt;OutputSource&lt;/code&gt; objects, each of which contains fields &lt;code&gt;OutputS3Path&lt;/code&gt;, &lt;code&gt;ApplyNormalization&lt;/code&gt;, and &lt;code&gt;Output&lt;/code&gt;. | 
**resolutionTechniques** | [**CreateMatchingWorkflowRequestResolutionTechniques**](CreateMatchingWorkflowRequestResolutionTechniques.md) |  | 
**roleArn** | **String** | The Amazon Resource Name (ARN) of the IAM role. AWS Entity Resolution assumes this role to create resources on your behalf as part of workflow execution. | 
**tags** | **{String: String}** | The tags used to organize, track, or control access for this resource. | [optional] 
**workflowName** | **String** | The name of the workflow. There cannot be multiple &lt;code&gt;DataIntegrationWorkflows&lt;/code&gt; with the same name. | 


