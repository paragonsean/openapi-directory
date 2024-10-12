# IncreaseApi.DeclinedTransactionSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**achDecline** | [**ACHDecline**](ACHDecline.md) |  | 
**cardDecline** | [**CardDecline**](CardDecline.md) |  | 
**cardRouteDecline** | [**DeprecatedCardDecline**](DeprecatedCardDecline.md) |  | 
**category** | **String** | The type of decline that took place. We may add additional possible values for this enum over time; your application should be able to handle such additions gracefully. | 
**checkDecline** | [**CheckDecline**](CheckDecline.md) |  | 
**inboundRealTimePaymentsTransferDecline** | [**InboundRealTimePaymentsTransferDecline**](InboundRealTimePaymentsTransferDecline.md) |  | 
**internationalAchDecline** | [**InternationalACHDecline**](InternationalACHDecline.md) |  | 



## Enum: CategoryEnum


* `ach_decline` (value: `"ach_decline"`)

* `card_decline` (value: `"card_decline"`)

* `check_decline` (value: `"check_decline"`)

* `inbound_real_time_payments_transfer_decline` (value: `"inbound_real_time_payments_transfer_decline"`)

* `international_ach_decline` (value: `"international_ach_decline"`)

* `card_route_decline` (value: `"card_route_decline"`)

* `other` (value: `"other"`)




