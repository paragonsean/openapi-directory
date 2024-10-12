

# PricingPlanProperties

An Application Insights component daily data volume cap

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cap** | **BigDecimal** | Daily data volume cap in GB. |  [optional] |
|**maxHistoryCap** | **BigDecimal** | Maximum daily data volume cap that the user can set for this component. |  [optional] [readonly] |
|**planType** | **String** | Pricing Plan Type Name. |  [optional] |
|**resetHour** | **Integer** | Daily data volume cap UTC reset hour. |  [optional] [readonly] |
|**stopSendNotificationWhenHitCap** | **Boolean** | Do not send a notification email when the daily data volume cap is met. |  [optional] |
|**stopSendNotificationWhenHitThreshold** | **Boolean** | Reserved, not used for now. |  [optional] |
|**warningThreshold** | **Integer** | Reserved, not used for now. |  [optional] |



