

# CreateNetworkFirmwareUpgradesRollback200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**product** | [**ProductEnum**](#ProductEnum) | Product type to rollback (if the network is a combined network) |  [optional] |
|**reasons** | [**List&lt;CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner&gt;**](CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner.md) | Reasons for the rollback |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the rollback |  [optional] |
|**time** | **OffsetDateTime** | Scheduled time for the rollback |  [optional] |
|**toVersion** | [**CreateNetworkFirmwareUpgradesRollback200ResponseToVersion**](CreateNetworkFirmwareUpgradesRollback200ResponseToVersion.md) |  |  [optional] |
|**upgradeBatchId** | **String** | Batch ID of the firmware rollback |  [optional] |



## Enum: ProductEnum

| Name | Value |
|---- | -----|
| APPLIANCE | &quot;appliance&quot; |
| CAMERA | &quot;camera&quot; |
| CELLULAR_GATEWAY | &quot;cellularGateway&quot; |
| SWITCH | &quot;switch&quot; |
| WIRELESS | &quot;wireless&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CANCELED | &quot;canceled&quot; |
| COMPLETED | &quot;completed&quot; |
| IN_PROGRESS | &quot;in_progress&quot; |
| PENDING | &quot;pending&quot; |



