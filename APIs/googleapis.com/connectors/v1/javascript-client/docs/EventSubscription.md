# ConnectorsApi.EventSubscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Created time. | [optional] [readonly] 
**destinations** | [**EventSubscriptionDestination**](EventSubscriptionDestination.md) |  | [optional] 
**eventTypeId** | **String** | Optional. Event type id of the event of current EventSubscription. | [optional] 
**jms** | [**JMS**](JMS.md) |  | [optional] 
**name** | **String** | Required. Resource name of the EventSubscription. Format: projects/{project}/locations/{location}/connections/{connection}/eventSubscriptions/{event_subscription} | [optional] 
**status** | [**EventSubscriptionStatus**](EventSubscriptionStatus.md) |  | [optional] 
**subscriber** | **String** | Optional. name of the Subscriber for the current EventSubscription. | [optional] 
**subscriberLink** | **String** | Optional. Link for Subscriber of the current EventSubscription. | [optional] 
**updateTime** | **String** | Output only. Updated time. | [optional] [readonly] 


