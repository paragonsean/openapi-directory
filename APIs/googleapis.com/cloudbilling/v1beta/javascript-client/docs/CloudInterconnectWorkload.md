# CloudBillingApi.CloudInterconnectWorkload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interconnectAttachments** | [**[VlanAttachment]**](VlanAttachment.md) | VLAN attachment used for interconnect. | [optional] 
**interconnectType** | **String** | VLAN attachment type | [optional] 
**linkType** | **String** | Interconnect circuit link type. | [optional] 
**provisionedLinkCount** | [**Usage**](Usage.md) |  | [optional] 



## Enum: InterconnectTypeEnum


* `UNSPECIFIED` (value: `"INTERCONNECT_TYPE_UNSPECIFIED"`)

* `DEDICATED` (value: `"INTERCONNECT_TYPE_DEDICATED"`)

* `PARTNER` (value: `"INTERCONNECT_TYPE_PARTNER"`)





## Enum: LinkTypeEnum


* `UNSPECIFIED` (value: `"LINK_TYPE_UNSPECIFIED"`)

* `ETHERNET_10G_LR` (value: `"LINK_TYPE_ETHERNET_10G_LR"`)

* `ETHERNET_100G_LR` (value: `"LINK_TYPE_ETHERNET_100G_LR"`)




