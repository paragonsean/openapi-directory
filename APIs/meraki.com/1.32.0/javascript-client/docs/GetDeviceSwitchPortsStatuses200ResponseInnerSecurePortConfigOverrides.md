# MerakiDashboardApi.GetDeviceSwitchPortsStatuses200ResponseInnerSecurePortConfigOverrides

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedVlans** | **String** | The VLANs allowed on the . Only applicable to trunk ports. | [optional] 
**type** | **String** | The type of the  (&#39;trunk&#39; or &#39;access&#39;). | [optional] 
**vlan** | **Number** | The VLAN of the . A null value will clear the value set for trunk ports. | [optional] 
**voiceVlan** | **Number** | The voice VLAN of the . Only applicable to access ports. | [optional] 



## Enum: TypeEnum


* `access` (value: `"access"`)

* `trunk` (value: `"trunk"`)




