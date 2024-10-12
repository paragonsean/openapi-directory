

# WritableIPAddress


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | IPv4 or IPv6 address (with mask) |  |
|**created** | **LocalDate** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**dnsName** | **String** | Hostname or FQDN (not case-sensitive) |  [optional] |
|**family** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**_interface** | **Integer** |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**natInside** | **Integer** | The IP for which this address is the \&quot;outside\&quot; IP |  [optional] |
|**natOutside** | **Integer** |  |  |
|**role** | [**RoleEnum**](#RoleEnum) | The functional role of this IP |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The operational status of this IP |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**tenant** | **Integer** |  |  [optional] |
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



