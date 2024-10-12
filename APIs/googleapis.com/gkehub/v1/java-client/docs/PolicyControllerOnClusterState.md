

# PolicyControllerOnClusterState

OnClusterState represents the state of a sub-component of Policy Controller.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | **String** | Surface potential errors or information logs. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The lifecycle state of this component. |  [optional] |



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



