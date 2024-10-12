

# WritablePrefix


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **LocalDate** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**family** | **Integer** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**isPool** | **Boolean** | All IP addresses within this prefix are considered usable |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**prefix** | **String** | IPv4 or IPv6 network with mask |  |
|**role** | **Integer** | The primary function of this prefix |  [optional] |
|**site** | **Integer** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Operational status of this prefix |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**tenant** | **Integer** |  |  [optional] |
|**vlan** | **Integer** |  |  [optional] |
|**vrf** | **Integer** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |



