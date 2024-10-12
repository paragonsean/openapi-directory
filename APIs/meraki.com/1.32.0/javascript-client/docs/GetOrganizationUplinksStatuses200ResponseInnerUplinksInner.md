# MerakiDashboardApi.GetOrganizationUplinksStatuses200ResponseInnerUplinksInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apn** | **String** | Access Point Name | [optional] 
**connectionType** | **String** | Connection Type | [optional] 
**dns1** | **String** | Primary DNS IP | [optional] 
**dns2** | **String** | Secondary DNS IP | [optional] 
**gateway** | **String** | Gateway IP | [optional] 
**iccid** | **String** | Integrated Circuit Card Identification Number | [optional] 
**_interface** | **String** | Uplink interface | [optional] 
**ip** | **String** | Uplink IP | [optional] 
**ipAssignedBy** | **String** | The way in which the IP is assigned | [optional] 
**primaryDns** | **String** | Primary DNS IP | [optional] 
**provider** | **String** | Network Provider | [optional] 
**publicIp** | **String** | Public IP | [optional] 
**secondaryDns** | **String** | Secondary DNS IP | [optional] 
**signalStat** | [**GetOrganizationCellularGatewayUplinkStatuses200ResponseInnerUplinksInnerSignalStat**](GetOrganizationCellularGatewayUplinkStatuses200ResponseInnerUplinksInnerSignalStat.md) |  | [optional] 
**signalType** | **String** | Signal Type | [optional] 
**status** | **String** | Uplink status | [optional] 



## Enum: InterfaceEnum


* `cellular` (value: `"cellular"`)

* `wan1` (value: `"wan1"`)

* `wan2` (value: `"wan2"`)





## Enum: StatusEnum


* `active` (value: `"active"`)

* `connecting` (value: `"connecting"`)

* `failed` (value: `"failed"`)

* `not connected` (value: `"not connected"`)

* `ready` (value: `"ready"`)




