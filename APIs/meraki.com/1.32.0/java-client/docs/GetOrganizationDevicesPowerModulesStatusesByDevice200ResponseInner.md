

# GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mac** | **String** | The device MAC address. |  [optional] |
|**name** | **String** | The device name. |  [optional] |
|**network** | [**GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerNetwork**](GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerNetwork.md) |  |  [optional] |
|**productType** | [**ProductTypeEnum**](#ProductTypeEnum) | Device product type. |  [optional] |
|**serial** | **String** | The device serial number. |  [optional] |
|**slots** | [**List&lt;GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner&gt;**](GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.md) | Information for the device&#39;s AC power supplies. |  [optional] |
|**tags** | **List&lt;String&gt;** | List of custom tags for the device. |  [optional] |



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



