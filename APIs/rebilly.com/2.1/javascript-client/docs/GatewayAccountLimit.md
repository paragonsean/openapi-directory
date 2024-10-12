# RebillyRestApi.GatewayAccountLimit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**[SelfLink]**](SelfLink.md) | The links related to resource. | [optional] [readonly] 
**cap** | **Number** | The limit&#39;s value cap is the maximum desired value. If type is money, the currency is the report currency. The cap only applies to approved transactions of type &#x60;authorize&#x60; or &#x60;sale&#x60;.  | 
**createdTime** | **Date** | Gateway account limit created time. | [optional] [readonly] 
**endTime** | **Date** | The limit&#39;s current period end time. At this time, the limit will reset. | [optional] [readonly] 
**frequency** | **String** | The limit&#39;s period will reset according to the frequency. | [optional] [readonly] 
**id** | **String** | The gateway account limit identifier. | [optional] [readonly] 
**startTime** | **Date** | The limit&#39;s current period start time. | [optional] [readonly] 
**status** | **String** | The gateway account limit status. | [optional] [readonly] 
**type** | **String** | The limit can be on &#x60;money&#x60; or &#x60;count&#x60; of transactions. If &#x60;money&#x60; is chosen, the currency is the report currency.  | [optional] [readonly] 
**updatedTime** | **Date** | Gateway account limit updated time. | [optional] [readonly] 
**usage** | **Number** | The limit&#39;s actual usage during this period. | [optional] [readonly] 



## Enum: FrequencyEnum


* `daily` (value: `"daily"`)

* `monthly` (value: `"monthly"`)





## Enum: StatusEnum


* `monitoring` (value: `"monitoring"`)

* `reached` (value: `"reached"`)





## Enum: TypeEnum


* `count` (value: `"count"`)

* `money` (value: `"money"`)




