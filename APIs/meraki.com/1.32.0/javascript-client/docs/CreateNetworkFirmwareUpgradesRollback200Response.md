# MerakiDashboardApi.CreateNetworkFirmwareUpgradesRollback200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **String** | Product type to rollback (if the network is a combined network) | [optional] 
**reasons** | [**[CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner]**](CreateNetworkFirmwareUpgradesRollback200ResponseReasonsInner.md) | Reasons for the rollback | [optional] 
**status** | **String** | Status of the rollback | [optional] 
**time** | **Date** | Scheduled time for the rollback | [optional] 
**toVersion** | [**CreateNetworkFirmwareUpgradesRollback200ResponseToVersion**](CreateNetworkFirmwareUpgradesRollback200ResponseToVersion.md) |  | [optional] 
**upgradeBatchId** | **String** | Batch ID of the firmware rollback | [optional] 



## Enum: ProductEnum


* `appliance` (value: `"appliance"`)

* `camera` (value: `"camera"`)

* `cellularGateway` (value: `"cellularGateway"`)

* `switch` (value: `"switch"`)

* `wireless` (value: `"wireless"`)





## Enum: StatusEnum


* `canceled` (value: `"canceled"`)

* `completed` (value: `"completed"`)

* `in_progress` (value: `"in_progress"`)

* `pending` (value: `"pending"`)




