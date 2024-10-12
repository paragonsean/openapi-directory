# AuditApi.AuditEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**EventLink**](EventLink.md) |  | [optional] 
**accountId** | **String** | The NEXMO_API_KEY of the Vonage API account that the audit event is associated with. | [optional] 
**context** | [**AuditEventContext**](AuditEventContext.md) |  | [optional] 
**createdAt** | **Date** | When the audit event was created. | [optional] 
**eventType** | [**EventTypes**](EventTypes.md) |  | [optional] 
**eventTypeDescription** | **String** | A description of the event type | [optional] 
**id** | **String** | UUID of the audit event | [optional] 
**source** | **String** | The source of the event. CD: Customer Dashboard DEVAPI: via Developer API  | [optional] 
**sourceCountry** | **String** | ISO 3166-1 Alpha-2 country code recorded for the event. | [optional] 
**sourceDescription** | **String** | Description of the audit event source. | [optional] 
**sourceIp** | **String** | The IP address used to make the account change. | [optional] 
**userEmail** | **String** | Email of the user whose account the audit event is associated with. | [optional] 
**userId** | **Number** | The ID of the user that the audit event is associated with. | [optional] 



## Enum: SourceEnum


* `CD` (value: `"CD"`)

* `DEVAPI` (value: `"DEVAPI"`)





## Enum: SourceDescriptionEnum


* `Customer Dashboard` (value: `"Customer Dashboard"`)

* `Developer API` (value: `"Developer API"`)




