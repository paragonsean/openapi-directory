

# WritableIPAddress


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | IPv4 or IPv6 address (with mask) |  |
|**assignedObject** | **Object** |  |  [optional] [readonly] |
|**assignedObjectId** | **Integer** |  |  [optional] |
|**assignedObjectType** | **String** |  |  [optional] |
|**comments** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**display** | **String** |  |  [optional] [readonly] |
|**dnsName** | **String** | Hostname or FQDN (not case-sensitive) |  [optional] |
|**family** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**natInside** | **Integer** | The IP for which this address is the \&quot;outside\&quot; IP |  [optional] |
|**natOutside** | [**List&lt;NestedIPAddress&gt;**](NestedIPAddress.md) |  |  [optional] [readonly] |
|**role** | [**RoleEnum**](#RoleEnum) | The functional role of this IP |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The operational status of this IP |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**tenant** | **Integer** |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |
|**vrf** | **Integer** |  |  [optional] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| LOOPBACK | &quot;loopback&quot; |
| SECONDARY | &quot;secondary&quot; |
| ANYCAST | &quot;anycast&quot; |
| VIP | &quot;vip&quot; |
| VRRP | &quot;vrrp&quot; |
| HSRP | &quot;hsrp&quot; |
| GLBP | &quot;glbp&quot; |
| CARP | &quot;carp&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| RESERVED | &quot;reserved&quot; |
| DEPRECATED | &quot;deprecated&quot; |
| DHCP | &quot;dhcp&quot; |
| SLAAC | &quot;slaac&quot; |



