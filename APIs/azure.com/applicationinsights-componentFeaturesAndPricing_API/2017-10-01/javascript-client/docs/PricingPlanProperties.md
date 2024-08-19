# ApplicationInsightsManagementClient.PricingPlanProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cap** | **Number** | Daily data volume cap in GB. | [optional] 
**maxHistoryCap** | **Number** | Maximum daily data volume cap that the user can set for this component. | [optional] [readonly] 
**planType** | **String** | Pricing Plan Type Name. | [optional] 
**resetHour** | **Number** | Daily data volume cap UTC reset hour. | [optional] [readonly] 
**stopSendNotificationWhenHitCap** | **Boolean** | Do not send a notification email when the daily data volume cap is met. | [optional] 
**stopSendNotificationWhenHitThreshold** | **Boolean** | Reserved, not used for now. | [optional] 
**warningThreshold** | **Number** | Reserved, not used for now. | [optional] 


