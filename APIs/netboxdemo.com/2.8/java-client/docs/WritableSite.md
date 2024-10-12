

# WritableSite


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**asn** | **Integer** | 32-bit autonomous system number |  [optional] |
|**circuitCount** | **Integer** |  |  [optional] [readonly] |
|**comments** | **String** |  |  [optional] |
|**contactEmail** | **String** |  |  [optional] |
|**contactName** | **String** |  |  [optional] |
|**contactPhone** | **String** |  |  [optional] |
|**created** | **LocalDate** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**deviceCount** | **Integer** |  |  [optional] [readonly] |
|**facility** | **String** | Local facility ID or description |  [optional] |
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
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**tenant** | **Integer** |  |  [optional] |
|**timeZone** | **String** |  |  [optional] |
|**virtualmachineCount** | **Integer** |  |  [optional] [readonly] |
|**vlanCount** | **Integer** |  |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PLANNED | &quot;planned&quot; |
| RETIRED | &quot;retired&quot; |



