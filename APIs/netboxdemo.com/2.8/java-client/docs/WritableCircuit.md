

# WritableCircuit


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cid** | **String** |  |  |
|**comments** | **String** |  |  [optional] |
|**commitRate** | **Integer** |  |  [optional] |
|**created** | **LocalDate** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**installDate** | **LocalDate** |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**provider** | **Integer** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**tenant** | **Integer** |  |  [optional] |
|**terminationA** | **String** |  |  [optional] [readonly] |
|**terminationZ** | **String** |  |  [optional] [readonly] |
|**type** | **Integer** |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PLANNED | &quot;planned&quot; |
| PROVISIONING | &quot;provisioning&quot; |
| ACTIVE | &quot;active&quot; |
| OFFLINE | &quot;offline&quot; |
| DEPROVISIONING | &quot;deprovisioning&quot; |
| DECOMMISSIONED | &quot;decommissioned&quot; |



