# MerakiDashboardApi.GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | Device uplink address. | [optional] 
**assignmentMode** | **String** | Indicates how the device uplink address is assigned. Available options are: static, dynamic. | [optional] 
**gateway** | **String** | Device uplink gateway address. | [optional] 
**protocol** | **String** | Type of address for the device uplink. Available options are: ipv4, ipv6. | [optional] 
**_public** | [**GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInnerPublic**](GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInnerPublic.md) |  | [optional] 



## Enum: AssignmentModeEnum


* `dynamic` (value: `"dynamic"`)

* `static` (value: `"static"`)





## Enum: ProtocolEnum


* `ipv4` (value: `"ipv4"`)

* `ipv6` (value: `"ipv6"`)




