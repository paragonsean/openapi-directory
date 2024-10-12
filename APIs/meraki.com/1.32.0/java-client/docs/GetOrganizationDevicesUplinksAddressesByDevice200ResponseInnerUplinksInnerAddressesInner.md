

# GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | Device uplink address. |  [optional] |
|**assignmentMode** | [**AssignmentModeEnum**](#AssignmentModeEnum) | Indicates how the device uplink address is assigned. Available options are: static, dynamic. |  [optional] |
|**gateway** | **String** | Device uplink gateway address. |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Type of address for the device uplink. Available options are: ipv4, ipv6. |  [optional] |
|**_public** | [**GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInnerPublic**](GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInnerAddressesInnerPublic.md) |  |  [optional] |



## Enum: AssignmentModeEnum

| Name | Value |
|---- | -----|
| DYNAMIC | &quot;dynamic&quot; |
| STATIC | &quot;static&quot; |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| IPV4 | &quot;ipv4&quot; |
| IPV6 | &quot;ipv6&quot; |



