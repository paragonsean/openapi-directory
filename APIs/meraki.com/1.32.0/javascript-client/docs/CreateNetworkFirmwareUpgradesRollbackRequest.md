# MerakiDashboardApi.CreateNetworkFirmwareUpgradesRollbackRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | **String** | Product type to rollback (if the network is a combined network) | [optional] 
**reasons** | [**[CreateNetworkFirmwareUpgradesRollbackRequestReasonsInner]**](CreateNetworkFirmwareUpgradesRollbackRequestReasonsInner.md) | Reasons for the rollback | 
**time** | **Date** | Scheduled time for the rollback | [optional] 
**toVersion** | [**CreateNetworkFirmwareUpgradesRollbackRequestToVersion**](CreateNetworkFirmwareUpgradesRollbackRequestToVersion.md) |  | [optional] 



## Enum: ProductEnum


* `appliance` (value: `"appliance"`)

* `camera` (value: `"camera"`)

* `cellularGateway` (value: `"cellularGateway"`)

* `switch` (value: `"switch"`)

* `wireless` (value: `"wireless"`)




