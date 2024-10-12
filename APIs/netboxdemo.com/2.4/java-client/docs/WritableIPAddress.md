

# WritableIPAddress


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | IPv4 or IPv6 address (with mask) |  |
|**created** | **LocalDate** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**family** | **Integer** |  |  [optional] [readonly] |
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
| NUMBER_10 | 10 |
| NUMBER_20 | 20 |
| NUMBER_30 | 30 |
| NUMBER_40 | 40 |
| NUMBER_41 | 41 |
| NUMBER_42 | 42 |
| NUMBER_43 | 43 |
| NUMBER_44 | 44 |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_5 | 5 |



