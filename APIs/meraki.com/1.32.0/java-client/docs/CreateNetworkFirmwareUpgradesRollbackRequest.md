

# CreateNetworkFirmwareUpgradesRollbackRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**product** | [**ProductEnum**](#ProductEnum) | Product type to rollback (if the network is a combined network) |  [optional] |
|**reasons** | [**List&lt;CreateNetworkFirmwareUpgradesRollbackRequestReasonsInner&gt;**](CreateNetworkFirmwareUpgradesRollbackRequestReasonsInner.md) | Reasons for the rollback |  |
|**time** | **OffsetDateTime** | Scheduled time for the rollback |  [optional] |
|**toVersion** | [**CreateNetworkFirmwareUpgradesRollbackRequestToVersion**](CreateNetworkFirmwareUpgradesRollbackRequestToVersion.md) |  |  [optional] |



## Enum: ProductEnum

| Name | Value |
|---- | -----|
| APPLIANCE | &quot;appliance&quot; |
| CAMERA | &quot;camera&quot; |
| CELLULAR_GATEWAY | &quot;cellularGateway&quot; |
| SWITCH | &quot;switch&quot; |
| WIRELESS | &quot;wireless&quot; |



