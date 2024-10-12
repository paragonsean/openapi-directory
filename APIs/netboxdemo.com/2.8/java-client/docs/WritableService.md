

# WritableService


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **LocalDate** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**device** | **Integer** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**ipaddresses** | **Set&lt;Integer&gt;** |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**name** | **String** |  |  |
|**port** | **Integer** |  |  |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) |  |  |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**virtualMachine** | **Integer** |  |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| TCP | &quot;tcp&quot; |
| UDP | &quot;udp&quot; |



