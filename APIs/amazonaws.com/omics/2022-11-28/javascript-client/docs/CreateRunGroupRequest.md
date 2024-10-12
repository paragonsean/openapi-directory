# AmazonOmics.CreateRunGroupRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | A name for the group. | [optional] 
**maxCpus** | **Number** | The maximum number of CPUs to use in the group. | [optional] 
**maxRuns** | **Number** | The maximum number of concurrent runs for the group. | [optional] 
**maxDuration** | **Number** | A maximum run time for the group in minutes. | [optional] 
**tags** | **{String: String}** | Tags for the group. | [optional] 
**requestId** | **String** | To ensure that requests don&#39;t run multiple times, specify a unique ID for each request. | 
**maxGpus** | **Number** |  The maximum GPUs that can be used by a run group.  | [optional] 


