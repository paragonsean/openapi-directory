# GkeHubApi.PolicyControllerMembershipState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**componentStates** | [**{String: PolicyControllerOnClusterState}**](PolicyControllerOnClusterState.md) | Currently these include (also serving as map keys): 1. \&quot;admission\&quot; 2. \&quot;audit\&quot; 3. \&quot;mutation\&quot; | [optional] 
**policyContentState** | [**PolicyControllerPolicyContentState**](PolicyControllerPolicyContentState.md) |  | [optional] 
**state** | **String** | The overall Policy Controller lifecycle state observed by the Hub Feature controller. | [optional] 



## Enum: StateEnum


* `LIFECYCLE_STATE_UNSPECIFIED` (value: `"LIFECYCLE_STATE_UNSPECIFIED"`)

* `NOT_INSTALLED` (value: `"NOT_INSTALLED"`)

* `INSTALLING` (value: `"INSTALLING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `UPDATING` (value: `"UPDATING"`)

* `DECOMMISSIONING` (value: `"DECOMMISSIONING"`)

* `CLUSTER_ERROR` (value: `"CLUSTER_ERROR"`)

* `HUB_ERROR` (value: `"HUB_ERROR"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `DETACHED` (value: `"DETACHED"`)




