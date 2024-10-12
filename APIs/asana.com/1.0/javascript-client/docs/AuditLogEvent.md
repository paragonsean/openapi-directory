# Asana.AuditLogEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | [**AuditLogEventActor**](AuditLogEventActor.md) |  | [optional] 
**context** | [**AuditLogEventContext**](AuditLogEventContext.md) |  | [optional] 
**createdAt** | **Date** | The time the event was created. | [optional] 
**details** | **Object** | Event specific details. The schema will vary depending on the &#x60;event_type&#x60;. | [optional] 
**eventCategory** | **String** | The category that this &#x60;event_type&#x60; belongs to. | [optional] 
**eventType** | **String** | The type of the event. | [optional] 
**gid** | **String** | Globally unique identifier of the &#x60;AuditLogEvent&#x60;, as a string. | [optional] 
**resource** | [**AuditLogEventResource**](AuditLogEventResource.md) |  | [optional] 


