

# GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mac** | **String** | The device MAC address. |  [optional] |
|**name** | **String** | The device name. |  [optional] |
|**network** | [**GetOrganizationDevicesAvailabilities200ResponseInnerNetwork**](GetOrganizationDevicesAvailabilities200ResponseInnerNetwork.md) |  |  [optional] |
|**productType** | [**ProductTypeEnum**](#ProductTypeEnum) | Device product type. |  [optional] |
|**serial** | **String** | The device serial number. |  [optional] |
|**tags** | **List&lt;String&gt;** | List of custom tags for the device. |  [optional] |
|**uplinks** | [**List&lt;GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInner&gt;**](GetOrganizationDevicesUplinksAddressesByDevice200ResponseInnerUplinksInner.md) | List of device uplink addresses information. |  [optional] |



## Enum: ProductTypeEnum

| Name | Value |
|---- | -----|
| APPLIANCE | &quot;appliance&quot; |
| CAMERA | &quot;camera&quot; |
| CELLULAR_GATEWAY | &quot;cellularGateway&quot; |
| SENSOR | &quot;sensor&quot; |
| SWITCH | &quot;switch&quot; |
| SYSTEMS_MANAGER | &quot;systemsManager&quot; |
| WIRELESS | &quot;wireless&quot; |



