

# AuditLogEvent

An object representing a single event within an Asana domain.  Every audit log event is comprised of an `event_type`, `actor`, `resource`, and `context`. Some events will include additional metadata about the event under `details`. See our [currently supported list of events](/docs/supported-auditlogevents) for more details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actor** | [**AuditLogEventActor**](AuditLogEventActor.md) |  |  [optional] |
|**context** | [**AuditLogEventContext**](AuditLogEventContext.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** | The time the event was created. |  [optional] |
|**details** | **Object** | Event specific details. The schema will vary depending on the &#x60;event_type&#x60;. |  [optional] |
|**eventCategory** | **String** | The category that this &#x60;event_type&#x60; belongs to. |  [optional] |
|**eventType** | **String** | The type of the event. |  [optional] |
|**gid** | **String** | Globally unique identifier of the &#x60;AuditLogEvent&#x60;, as a string. |  [optional] |
|**resource** | [**AuditLogEventResource**](AuditLogEventResource.md) |  |  [optional] |



