# RebillyRestApi.SubscriptionReactivation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**[SelfLink]**](SelfLink.md) | The links related to resource. | [optional] [readonly] 
**cancellationId** | **String** | Identifier of the related cancellation. | [optional] [readonly] 
**createdTime** | **Date** | The time of resource creation (when it is posted). | [optional] [readonly] 
**description** | **String** | Reactivation reason description in free form. | [optional] 
**effectiveTime** | **Date** | The date from which the service period would start, unless the subscription is canceled but still active. In case the susbcription is still active, the subscription will continue the current service period. If omitted, it will default to the current time.  | [optional] 
**id** | **String** | Reactivation identifier. | [optional] [readonly] 
**renewalTime** | **Date** | The time of the next subscription renewal. If omitted then it is computed from the effective time. If the subscription is canceled but active it is ignored, so the next renewal will happen as scheduled.  | [optional] 
**subscriptionId** | **String** | Identifier of the reactivated subscription. | 


