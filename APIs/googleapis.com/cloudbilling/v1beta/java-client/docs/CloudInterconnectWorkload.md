

# CloudInterconnectWorkload

Specifies usage for Cloud Interconnect resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**interconnectAttachments** | [**List&lt;VlanAttachment&gt;**](VlanAttachment.md) | VLAN attachment used for interconnect. |  [optional] |
|**interconnectType** | [**InterconnectTypeEnum**](#InterconnectTypeEnum) | VLAN attachment type |  [optional] |
|**linkType** | [**LinkTypeEnum**](#LinkTypeEnum) | Interconnect circuit link type. |  [optional] |
|**provisionedLinkCount** | [**Usage**](Usage.md) |  |  [optional] |



## Enum: InterconnectTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;INTERCONNECT_TYPE_UNSPECIFIED&quot; |
| DEDICATED | &quot;INTERCONNECT_TYPE_DEDICATED&quot; |
| PARTNER | &quot;INTERCONNECT_TYPE_PARTNER&quot; |



## Enum: LinkTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;LINK_TYPE_UNSPECIFIED&quot; |
| ETHERNET_10_G_LR | &quot;LINK_TYPE_ETHERNET_10G_LR&quot; |
| ETHERNET_100_G_LR | &quot;LINK_TYPE_ETHERNET_100G_LR&quot; |



