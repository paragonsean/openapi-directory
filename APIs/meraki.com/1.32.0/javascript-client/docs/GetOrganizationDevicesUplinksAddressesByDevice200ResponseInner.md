# MerakiDashboardApi.GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac** | **String** | The device MAC address. | [optional] 
**name** | **String** | The device name. | [optional] 
**network** | [**GetOrganizationDevicesAvailabilities200ResponseInnerNetwork**](GetOrganizationDevicesAvailabilities200ResponseInnerNetwork.md) |  | [optional] 
**productType** | **String** | Device product type. | [optional] 
**serial** | **String** | The device serial number. | [optional] 
**tags** | **[String]** | List of custom tags for the device. | [optional] 
**uplinks** | [**[GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInner]**](GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInner.md) | List of device uplink addresses information. | [optional] 



## Enum: ProductTypeEnum


* `appliance` (value: `"appliance"`)

* `camera` (value: `"camera"`)

* `cellularGateway` (value: `"cellularGateway"`)

* `sensor` (value: `"sensor"`)

* `switch` (value: `"switch"`)

* `systemsManager` (value: `"systemsManager"`)

* `wireless` (value: `"wireless"`)




