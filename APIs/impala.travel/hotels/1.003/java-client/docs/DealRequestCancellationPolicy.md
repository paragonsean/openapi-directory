

# DealRequestCancellationPolicy

Public rates hotels offer come with cancellation policies the hotel defines (e.g. free to cancel until 14 days before arrival). If you agree on cancellation policies here, this means they override the hotel's own policies for any booking made with this deal (e.g. free to cancel until two days before arrival).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **BigDecimal** | This is the cancellation policy applicable to the deal. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Cancellation may exist in minutes, hours or days prior to a stay. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MIDNIGHT | &quot;DAYS_BEFORE_ARRIVAL_AT_MIDNIGHT&quot; |
| CHECK_IN_TIME | &quot;DAYS_BEFORE_ARRIVAL_AT_CHECK_IN_TIME&quot; |



