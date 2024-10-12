# MarketingEvents.MarketingEventCreateRequestParams

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customProperties** | [**[PropertyValue]**](PropertyValue.md) | A list of PropertyValues. These can be whatever kind of property names and values you want. However, they must already exist on the HubSpot account&#39;s definition of the MarketingEvent Object. If they don&#39;t they will be filtered out and not set. In order to do this you&#39;ll need to create a new PropertyGroup on the HubSpot account&#39;s MarketingEvent object for your specific app and create the Custom Property you want to track on that HubSpot account. Do not create any new default properties on the MarketingEvent object as that will apply to all HubSpot accounts.  | [optional] 
**endDateTime** | **Date** | The end date and time of the marketing event. | [optional] 
**eventCancelled** | **Boolean** | Indicates if the marketing event has been cancelled.  Defaults to &#x60;false&#x60; | [optional] 
**eventDescription** | **String** | The description of the marketing event. | [optional] 
**eventName** | **String** | The name of the marketing event. | 
**eventOrganizer** | **String** | The name of the organizer of the marketing event. | 
**eventType** | **String** | Describes what type of event this is.  For example: &#x60;WEBINAR&#x60;, &#x60;CONFERENCE&#x60;, &#x60;WORKSHOP&#x60; | [optional] 
**eventUrl** | **String** | A URL in the external event application where the marketing event can be managed. | [optional] 
**externalAccountId** | **String** | The accountId that is associated with this marketing event in the external event application. | 
**externalEventId** | **String** | The id of the marketing event in the external event application. | 
**startDateTime** | **Date** | The start date and time of the marketing event. | [optional] 


