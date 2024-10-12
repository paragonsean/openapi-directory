# CloudSearchApi.EnterpriseTopazSidekickAgendaGroupCardProtoContext

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **String** | User friendly free text that describes the context of the card (e.g. \&quot;Next meeting with Bob\&quot;). This is largely only applicable when the card is generated from a query. | [optional] 
**date** | **String** | Localized free text that describes the dates represented by the card. Currently, the card will only represent a single day. | [optional] 
**eventsRestrict** | **String** | Represents restrictions applied to the events requested in the user&#39;s query. | [optional] 



## Enum: EventsRestrictEnum


* `NONE` (value: `"NONE"`)

* `NEXT_MEETING` (value: `"NEXT_MEETING"`)




