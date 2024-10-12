# AmazonCodeGuruProfiler.CreateProfilingGroupRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentOrchestrationConfig** | [**CreateProfilingGroupRequestAgentOrchestrationConfig**](CreateProfilingGroupRequestAgentOrchestrationConfig.md) |  | [optional] 
**computePlatform** | **String** |  The compute platform of the profiling group. Use &lt;code&gt;AWSLambda&lt;/code&gt; if your application runs on AWS Lambda. Use &lt;code&gt;Default&lt;/code&gt; if your application runs on a compute platform that is not AWS Lambda, such an Amazon EC2 instance, an on-premises server, or a different platform. If not specified, &lt;code&gt;Default&lt;/code&gt; is used.  | [optional] 
**profilingGroupName** | **String** | The name of the profiling group to create. | 
**tags** | **{String: String}** |  A list of tags to add to the created profiling group.  | [optional] 



## Enum: ComputePlatformEnum


* `Default` (value: `"Default"`)

* `AWSLambda` (value: `"AWSLambda"`)




