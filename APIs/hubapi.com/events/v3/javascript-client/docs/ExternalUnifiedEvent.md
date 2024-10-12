# Events.ExternalUnifiedEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventType** | **String** | The format of the &#x60;eventType&#x60; string is &#x60;ae{appId}_{eventTypeLabel}&#x60;, &#x60;pe{portalId}_{eventTypeLabel}&#x60;, or just &#x60;e_{eventTypeLabel}&#x60; for HubSpot events. | 
**id** | **String** | A unique identifier for the event. | 
**objectId** | **String** | The objectId of the object which did the event. | 
**objectType** | **String** | The objectType for the object which did the event. | 
**occurredAt** | **Date** | An ISO 8601 timestamp when the event occurred. | 
**properties** | **{String: String}** |  | [optional] 


