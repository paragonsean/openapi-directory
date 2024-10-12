

# WritablePowerFeed


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amperage** | **Integer** |  |  [optional] |
|**comments** | **String** |  |  [optional] |
|**created** | **LocalDate** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**maxUtilization** | **Integer** | Maximum permissible draw (percentage) |  [optional] |
|**name** | **String** |  |  |
|**phase** | [**PhaseEnum**](#PhaseEnum) |  |  [optional] |
|**powerPanel** | **Integer** |  |  |
|**rack** | **Integer** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**supply** | [**SupplyEnum**](#SupplyEnum) |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**voltage** | **Integer** |  |  [optional] |



## Enum: PhaseEnum

| Name | Value |
|---- | -----|
| SINGLE_PHASE | &quot;single-phase&quot; |
| THREE_PHASE | &quot;three-phase&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OFFLINE | &quot;offline&quot; |
| ACTIVE | &quot;active&quot; |
| PLANNED | &quot;planned&quot; |
| FAILED | &quot;failed&quot; |



## Enum: SupplyEnum

| Name | Value |
|---- | -----|
| AC | &quot;ac&quot; |
| DC | &quot;dc&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PRIMARY | &quot;primary&quot; |
| REDUNDANT | &quot;redundant&quot; |



