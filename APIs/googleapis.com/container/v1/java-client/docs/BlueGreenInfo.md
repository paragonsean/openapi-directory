

# BlueGreenInfo

Information relevant to blue-green upgrade.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blueInstanceGroupUrls** | **List&lt;String&gt;** | The resource URLs of the [managed instance groups] (/compute/docs/instance-groups/creating-groups-of-managed-instances) associated with blue pool. |  [optional] |
|**bluePoolDeletionStartTime** | **String** | Time to start deleting blue pool to complete blue-green upgrade, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. |  [optional] |
|**greenInstanceGroupUrls** | **List&lt;String&gt;** | The resource URLs of the [managed instance groups] (/compute/docs/instance-groups/creating-groups-of-managed-instances) associated with green pool. |  [optional] |
|**greenPoolVersion** | **String** | Version of green pool. |  [optional] |
|**phase** | [**PhaseEnum**](#PhaseEnum) | Current blue-green upgrade phase. |  [optional] |



## Enum: PhaseEnum

| Name | Value |
|---- | -----|
| PHASE_UNSPECIFIED | &quot;PHASE_UNSPECIFIED&quot; |
| UPDATE_STARTED | &quot;UPDATE_STARTED&quot; |
| CREATING_GREEN_POOL | &quot;CREATING_GREEN_POOL&quot; |
| CORDONING_BLUE_POOL | &quot;CORDONING_BLUE_POOL&quot; |
| DRAINING_BLUE_POOL | &quot;DRAINING_BLUE_POOL&quot; |
| NODE_POOL_SOAKING | &quot;NODE_POOL_SOAKING&quot; |
| DELETING_BLUE_POOL | &quot;DELETING_BLUE_POOL&quot; |
| ROLLBACK_STARTED | &quot;ROLLBACK_STARTED&quot; |



