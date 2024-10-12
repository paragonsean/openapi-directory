

# GatewayAccountLimit


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**List&lt;SelfLink&gt;**](SelfLink.md) | The links related to resource. |  [optional] [readonly] |
|**cap** | **Integer** | The limit&#39;s value cap is the maximum desired value. If type is money, the currency is the report currency. The cap only applies to approved transactions of type &#x60;authorize&#x60; or &#x60;sale&#x60;.  |  |
|**createdTime** | **OffsetDateTime** | Gateway account limit created time. |  [optional] [readonly] |
|**endTime** | **OffsetDateTime** | The limit&#39;s current period end time. At this time, the limit will reset. |  [optional] [readonly] |
|**frequency** | [**FrequencyEnum**](#FrequencyEnum) | The limit&#39;s period will reset according to the frequency. |  [optional] [readonly] |
|**id** | **String** | The gateway account limit identifier. |  [optional] [readonly] |
|**startTime** | **OffsetDateTime** | The limit&#39;s current period start time. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The gateway account limit status. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The limit can be on &#x60;money&#x60; or &#x60;count&#x60; of transactions. If &#x60;money&#x60; is chosen, the currency is the report currency.  |  [optional] [readonly] |
|**updatedTime** | **OffsetDateTime** | Gateway account limit updated time. |  [optional] [readonly] |
|**usage** | **Integer** | The limit&#39;s actual usage during this period. |  [optional] [readonly] |



## Enum: FrequencyEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;daily&quot; |
| MONTHLY | &quot;monthly&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| MONITORING | &quot;monitoring&quot; |
| REACHED | &quot;reached&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| COUNT | &quot;count&quot; |
| MONEY | &quot;money&quot; |



