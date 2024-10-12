

# AuditEvent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**EventLink**](EventLink.md) |  |  [optional] |
|**accountId** | **String** | The NEXMO_API_KEY of the Vonage API account that the audit event is associated with. |  [optional] |
|**context** | [**AuditEventContext**](AuditEventContext.md) |  |  [optional] |
|**createdAt** | **LocalDate** | When the audit event was created. |  [optional] |
|**eventType** | **EventTypes** |  |  [optional] |
|**eventTypeDescription** | **String** | A description of the event type |  [optional] |
|**id** | **String** | UUID of the audit event |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) | The source of the event. CD: Customer Dashboard DEVAPI: via Developer API  |  [optional] |
|**sourceCountry** | **String** | ISO 3166-1 Alpha-2 country code recorded for the event. |  [optional] |
|**sourceDescription** | [**SourceDescriptionEnum**](#SourceDescriptionEnum) | Description of the audit event source. |  [optional] |
|**sourceIp** | **String** | The IP address used to make the account change. |  [optional] |
|**userEmail** | **String** | Email of the user whose account the audit event is associated with. |  [optional] |
|**userId** | **Integer** | The ID of the user that the audit event is associated with. |  [optional] |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| CD | &quot;CD&quot; |
| DEVAPI | &quot;DEVAPI&quot; |



## Enum: SourceDescriptionEnum

| Name | Value |
|---- | -----|
| CUSTOMER_DASHBOARD | &quot;Customer Dashboard&quot; |
| DEVELOPER_API | &quot;Developer API&quot; |



