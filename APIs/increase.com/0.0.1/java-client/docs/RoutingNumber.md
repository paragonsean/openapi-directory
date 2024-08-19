

# RoutingNumber

Routing numbers are used to identify your bank in a financial transaction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**achTransfers** | [**AchTransfersEnum**](#AchTransfersEnum) | This routing number&#39;s support for ACH Transfers. |  |
|**name** | **String** | The name of the financial institution belonging to a routing number. |  |
|**realTimePaymentsTransfers** | [**RealTimePaymentsTransfersEnum**](#RealTimePaymentsTransfersEnum) | This routing number&#39;s support for Real Time Payments Transfers. |  |
|**routingNumber** | **String** | The nine digit routing number identifier. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;routing_number&#x60;. |  |
|**wireTransfers** | [**WireTransfersEnum**](#WireTransfersEnum) | This routing number&#39;s support for Wire Transfers. |  |



## Enum: AchTransfersEnum

| Name | Value |
|---- | -----|
| SUPPORTED | &quot;supported&quot; |
| NOT_SUPPORTED | &quot;not_supported&quot; |



## Enum: RealTimePaymentsTransfersEnum

| Name | Value |
|---- | -----|
| SUPPORTED | &quot;supported&quot; |
| NOT_SUPPORTED | &quot;not_supported&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ROUTING_NUMBER | &quot;routing_number&quot; |



## Enum: WireTransfersEnum

| Name | Value |
|---- | -----|
| SUPPORTED | &quot;supported&quot; |
| NOT_SUPPORTED | &quot;not_supported&quot; |



