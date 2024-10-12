# AnchoreEngineApiServer.MappingRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** |  | [optional] 
**image** | [**ImageRef**](ImageRef.md) |  | 
**name** | **String** |  | 
**policyId** | **String** | Optional single policy to evalute, if set will override any value in policy_ids, for backwards compatibility. Generally, policy_ids should be used even with a array of length 1. | [optional] 
**policyIds** | **[String]** | List of policyIds to evaluate in order, to completion | [optional] 
**registry** | **String** |  | 
**repository** | **String** |  | 
**whitelistIds** | **[String]** |  | [optional] 


