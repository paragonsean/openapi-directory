

# Instance

a vm instance

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Output only. name of the VM |  [optional] [readonly] |
|**region** | **String** | Output only. The location of the VM |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Output only. The state of the VM |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| INSTANCESTATE_UNSPECIFIED | &quot;INSTANCESTATE_UNSPECIFIED&quot; |
| PROVISIONING | &quot;PROVISIONING&quot; |
| STAGING | &quot;STAGING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| STOPPING | &quot;STOPPING&quot; |
| STOPPED | &quot;STOPPED&quot; |
| TERMINATED | &quot;TERMINATED&quot; |
| SUSPENDING | &quot;SUSPENDING&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |
| REPAIRING | &quot;REPAIRING&quot; |
| DEPROVISIONING | &quot;DEPROVISIONING&quot; |



