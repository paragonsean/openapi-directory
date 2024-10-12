# GooglePlayAndroidDeveloperApi.SubscriptionOfferPhase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **String** | Required. The duration of a single recurrence of this phase. Specified in ISO 8601 format. | [optional] 
**otherRegionsConfig** | [**OtherRegionsSubscriptionOfferPhaseConfig**](OtherRegionsSubscriptionOfferPhaseConfig.md) |  | [optional] 
**recurrenceCount** | **Number** | Required. The number of times this phase repeats. If this offer phase is not free, each recurrence charges the user the price of this offer phase. | [optional] 
**regionalConfigs** | [**[RegionalSubscriptionOfferPhaseConfig]**](RegionalSubscriptionOfferPhaseConfig.md) | Required. The region-specific configuration of this offer phase. This list must contain exactly one entry for each region for which the subscription offer has a regional config. | [optional] 


