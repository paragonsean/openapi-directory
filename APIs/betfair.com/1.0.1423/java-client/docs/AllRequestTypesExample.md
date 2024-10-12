

# AllRequestTypesExample


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authentication** | [**AuthenticationMessage**](AuthenticationMessage.md) |  |  [optional] |
|**heartbeat** | [**HeartbeatMessage**](HeartbeatMessage.md) |  |  [optional] |
|**marketSubscription** | [**MarketSubscriptionMessage**](MarketSubscriptionMessage.md) |  |  [optional] |
|**opTypes** | [**OpTypesEnum**](#OpTypesEnum) |  |  [optional] |
|**orderSubscriptionMessage** | [**OrderSubscriptionMessage**](OrderSubscriptionMessage.md) |  |  [optional] |



## Enum: OpTypesEnum

| Name | Value |
|---- | -----|
| HEARTBEAT | &quot;heartbeat&quot; |
| AUTHENTICATION | &quot;authentication&quot; |
| MARKET_SUBSCRIPTION | &quot;marketSubscription&quot; |
| ORDER_SUBSCRIPTION | &quot;orderSubscription&quot; |



