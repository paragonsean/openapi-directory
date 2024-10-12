

# WritableCircuit


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cid** | **String** |  |  |
|**comments** | **String** |  |  [optional] |
|**commitRate** | **Integer** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**display** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**installDate** | **LocalDate** |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**provider** | **Integer** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**tenant** | **Integer** |  |  [optional] |
|**terminationA** | **Integer** |  |  [optional] [readonly] |
|**terminationDate** | **LocalDate** |  |  [optional] |
|**terminationZ** | **Integer** |  |  [optional] [readonly] |
|**type** | **Integer** |  |  |
|**url** | **URI** |  |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PLANNED | &quot;planned&quot; |
| PROVISIONING | &quot;provisioning&quot; |
| ACTIVE | &quot;active&quot; |
| OFFLINE | &quot;offline&quot; |
| DEPROVISIONING | &quot;deprovisioning&quot; |
| DECOMMISSIONED | &quot;decommissioned&quot; |



