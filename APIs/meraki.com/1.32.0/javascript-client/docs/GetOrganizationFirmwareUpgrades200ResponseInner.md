# MerakiDashboardApi.GetOrganizationFirmwareUpgrades200ResponseInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completedAt** | **String** | Timestamp when upgrade completed. Null if status pending. | [optional] 
**fromVersion** | [**GetOrganizationFirmwareUpgrades200ResponseInnerFromVersion**](GetOrganizationFirmwareUpgrades200ResponseInnerFromVersion.md) |  | [optional] 
**network** | [**GetOrganizationFirmwareUpgrades200ResponseInnerNetwork**](GetOrganizationFirmwareUpgrades200ResponseInnerNetwork.md) |  | [optional] 
**productType** | **String** | product upgraded [wireless, appliance, switch, systemsManager, camera, cellularGateway, sensor] | [optional] 
**status** | **String** | Status of upgrade event: [Cancelled, Completed] | [optional] 
**time** | **Date** | Scheduled start time | [optional] 
**toVersion** | [**GetOrganizationFirmwareUpgrades200ResponseInnerToVersion**](GetOrganizationFirmwareUpgrades200ResponseInnerToVersion.md) |  | [optional] 
**upgradeBatchId** | **String** | The upgrade batch | [optional] 
**upgradeId** | **String** | The upgrade | [optional] 


