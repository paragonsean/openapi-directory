

# Refund


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**RefundLinksForSearch**](RefundLinksForSearch.md) |  |  [optional] |
|**amount** | **Long** |  |  [optional] [readonly] |
|**createdDate** | **String** |  |  [optional] [readonly] |
|**refundId** | **String** |  |  [optional] [readonly] |
|**settlementSummary** | [**RefundSettlementSummary**](RefundSettlementSummary.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUBMITTED | &quot;submitted&quot; |
| SUCCESS | &quot;success&quot; |
| ERROR | &quot;error&quot; |



