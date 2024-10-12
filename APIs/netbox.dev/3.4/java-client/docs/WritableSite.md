

# WritableSite


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**asns** | **Set&lt;Integer&gt;** |  |  [optional] |
|**circuitCount** | **Integer** |  |  [optional] [readonly] |
|**comments** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**deviceCount** | **Integer** |  |  [optional] [readonly] |
|**display** | **String** |  |  [optional] [readonly] |
|**facility** | **String** | Local facility ID or description |  [optional] |
|**group** | **Integer** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**latitude** | **BigDecimal** | GPS coordinate (latitude) |  [optional] |
|**longitude** | **BigDecimal** | GPS coordinate (longitude) |  [optional] |
|**name** | **String** |  |  |
|**physicalAddress** | **String** |  |  [optional] |
|**prefixCount** | **Integer** |  |  [optional] [readonly] |
|**rackCount** | **Integer** |  |  [optional] [readonly] |
|**region** | **Integer** |  |  [optional] |
|**shippingAddress** | **String** |  |  [optional] |
|**slug** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**tenant** | **Integer** |  |  [optional] |
|**timeZone** | **String** |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |
|**virtualmachineCount** | **Integer** |  |  [optional] [readonly] |
|**vlanCount** | **Integer** |  |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PLANNED | &quot;planned&quot; |
| STAGING | &quot;staging&quot; |
| ACTIVE | &quot;active&quot; |
| DECOMMISSIONING | &quot;decommissioning&quot; |
| RETIRED | &quot;retired&quot; |



