

# DeclinedTransactionSource

This is an object giving more details on the network-level event that caused the Declined Transaction. For example, for a card transaction this lists the merchant's industry and location. Note that for backwards compatibility reasons, additional undocumented keys may appear in this object. These should be treated as deprecated and will be removed in the future.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**achDecline** | [**ACHDecline**](ACHDecline.md) |  |  |
|**cardDecline** | [**CardDecline**](CardDecline.md) |  |  |
|**cardRouteDecline** | [**DeprecatedCardDecline**](DeprecatedCardDecline.md) |  |  |
|**category** | [**CategoryEnum**](#CategoryEnum) | The type of decline that took place. We may add additional possible values for this enum over time; your application should be able to handle such additions gracefully. |  |
|**checkDecline** | [**CheckDecline**](CheckDecline.md) |  |  |
|**inboundRealTimePaymentsTransferDecline** | [**InboundRealTimePaymentsTransferDecline**](InboundRealTimePaymentsTransferDecline.md) |  |  |
|**internationalAchDecline** | [**InternationalACHDecline**](InternationalACHDecline.md) |  |  |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| ACH_DECLINE | &quot;ach_decline&quot; |
| CARD_DECLINE | &quot;card_decline&quot; |
| CHECK_DECLINE | &quot;check_decline&quot; |
| INBOUND_REAL_TIME_PAYMENTS_TRANSFER_DECLINE | &quot;inbound_real_time_payments_transfer_decline&quot; |
| INTERNATIONAL_ACH_DECLINE | &quot;international_ach_decline&quot; |
| CARD_ROUTE_DECLINE | &quot;card_route_decline&quot; |
| OTHER | &quot;other&quot; |



