

# PolicyControllerMembershipState

**Policy Controller**: State for a single cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**componentStates** | [**Map&lt;String, PolicyControllerOnClusterState&gt;**](PolicyControllerOnClusterState.md) | Currently these include (also serving as map keys): 1. \&quot;admission\&quot; 2. \&quot;audit\&quot; 3. \&quot;mutation\&quot; |  [optional] |
|**policyContentState** | [**PolicyControllerPolicyContentState**](PolicyControllerPolicyContentState.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The overall Policy Controller lifecycle state observed by the Hub Feature controller. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| LIFECYCLE_STATE_UNSPECIFIED | &quot;LIFECYCLE_STATE_UNSPECIFIED&quot; |
| NOT_INSTALLED | &quot;NOT_INSTALLED&quot; |
| INSTALLING | &quot;INSTALLING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| UPDATING | &quot;UPDATING&quot; |
| DECOMMISSIONING | &quot;DECOMMISSIONING&quot; |
| CLUSTER_ERROR | &quot;CLUSTER_ERROR&quot; |
| HUB_ERROR | &quot;HUB_ERROR&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |
| DETACHED | &quot;DETACHED&quot; |



