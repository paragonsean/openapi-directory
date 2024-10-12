

# ServiceMeshDataPlaneManagement

Status of data plane management. Only reported per-member.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | [**List&lt;ServiceMeshStatusDetails&gt;**](ServiceMeshStatusDetails.md) | Explanation of the status. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Lifecycle status of data plane management. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| LIFECYCLE_STATE_UNSPECIFIED | &quot;LIFECYCLE_STATE_UNSPECIFIED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| FAILED_PRECONDITION | &quot;FAILED_PRECONDITION&quot; |
| PROVISIONING | &quot;PROVISIONING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| STALLED | &quot;STALLED&quot; |
| NEEDS_ATTENTION | &quot;NEEDS_ATTENTION&quot; |
| DEGRADED | &quot;DEGRADED&quot; |



