# MerakiDashboardApi.GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac** | **String** | The device MAC address. | [optional] 
**name** | **String** | The device name. | [optional] 
**network** | [**GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerNetwork**](GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerNetwork.md) |  | [optional] 
**productType** | **String** | Device product type. | [optional] 
**serial** | **String** | The device serial number. | [optional] 
**slots** | [**[GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner]**](GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.md) | Information for the device&#39;s AC power supplies. | [optional] 
**tags** | **[String]** | List of custom tags for the device. | [optional] 



## Enum: ProductTypeEnum


* `appliance` (value: `"appliance"`)

* `camera` (value: `"camera"`)

* `cellularGateway` (value: `"cellularGateway"`)

* `sensor` (value: `"sensor"`)

* `switch` (value: `"switch"`)

* `systemsManager` (value: `"systemsManager"`)

* `wireless` (value: `"wireless"`)




