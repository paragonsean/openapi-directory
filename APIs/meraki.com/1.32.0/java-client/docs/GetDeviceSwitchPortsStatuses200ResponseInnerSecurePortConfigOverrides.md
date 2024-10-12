

# GetDeviceSwitchPortsStatuses200ResponseInnerSecurePortConfigOverrides

The configuration overrides applied to this port when Secure Port is active.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedVlans** | **String** | The VLANs allowed on the . Only applicable to trunk ports. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the  (&#39;trunk&#39; or &#39;access&#39;). |  [optional] |
|**vlan** | **Integer** | The VLAN of the . A null value will clear the value set for trunk ports. |  [optional] |
|**voiceVlan** | **Integer** | The voice VLAN of the . Only applicable to access ports. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACCESS | &quot;access&quot; |
| TRUNK | &quot;trunk&quot; |



