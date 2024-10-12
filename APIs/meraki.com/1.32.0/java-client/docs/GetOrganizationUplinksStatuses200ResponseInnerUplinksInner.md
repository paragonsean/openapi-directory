

# GetOrganizationUplinksStatuses200ResponseInnerUplinksInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apn** | **String** | Access Point Name |  [optional] |
|**connectionType** | **String** | Connection Type |  [optional] |
|**dns1** | **String** | Primary DNS IP |  [optional] |
|**dns2** | **String** | Secondary DNS IP |  [optional] |
|**gateway** | **String** | Gateway IP |  [optional] |
|**iccid** | **String** | Integrated Circuit Card Identification Number |  [optional] |
|**_interface** | [**InterfaceEnum**](#InterfaceEnum) | Uplink interface |  [optional] |
|**ip** | **String** | Uplink IP |  [optional] |
|**ipAssignedBy** | **String** | The way in which the IP is assigned |  [optional] |
|**primaryDns** | **String** | Primary DNS IP |  [optional] |
|**provider** | **String** | Network Provider |  [optional] |
|**publicIp** | **String** | Public IP |  [optional] |
|**secondaryDns** | **String** | Secondary DNS IP |  [optional] |
|**signalStat** | [**GetOrganizationCellularGatewayUplinkStatuses200ResponseInnerUplinksInnerSignalStat**](GetOrganizationCellularGatewayUplinkStatuses200ResponseInnerUplinksInnerSignalStat.md) |  |  [optional] |
|**signalType** | **String** | Signal Type |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Uplink status |  [optional] |



## Enum: InterfaceEnum

| Name | Value |
|---- | -----|
| CELLULAR | &quot;cellular&quot; |
| WAN1 | &quot;wan1&quot; |
| WAN2 | &quot;wan2&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| CONNECTING | &quot;connecting&quot; |
| FAILED | &quot;failed&quot; |
| NOT_CONNECTED | &quot;not connected&quot; |
| READY | &quot;ready&quot; |



