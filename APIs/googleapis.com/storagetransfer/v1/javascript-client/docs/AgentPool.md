# StorageTransferApi.AgentPool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidthLimit** | [**BandwidthLimit**](BandwidthLimit.md) |  | [optional] 
**displayName** | **String** | Specifies the client-specified AgentPool description. | [optional] 
**name** | **String** | Required. Specifies a unique string that identifies the agent pool. Format: &#x60;projects/{project_id}/agentPools/{agent_pool_id}&#x60; | [optional] 
**state** | **String** | Output only. Specifies the state of the AgentPool. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `CREATED` (value: `"CREATED"`)

* `DELETING` (value: `"DELETING"`)




