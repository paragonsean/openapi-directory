

# Notification

An important, often time-sensitive item related to your Account. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | A full description of this Notification, in markdown format.  Not all Notifications include bodies.  |  [optional] [readonly] |
|**entity** | [**NotificationEntity**](NotificationEntity.md) |  |  [optional] |
|**label** | **String** | A short description of this Notification.  |  [optional] [readonly] |
|**message** | **String** | A human-readable description of the Notification. |  [optional] [readonly] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | The severity of this Notification.  This field can be used to decide how prominently to display the Notification, what color to make the display text, etc.  |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of Notification this is. |  [optional] [readonly] |
|**until** | **OffsetDateTime** | If this Notification has a duration, this will be the ending time for the Event/action. For example, if there is scheduled maintenance for one of our systems, &#x60;until&#x60; would be set to the end of the maintenance window.  |  [optional] [readonly] |
|**when** | **OffsetDateTime** | If this Notification is of an Event that will happen at a fixed, future time, this is when the named action will be taken. For example, if a Linode is to be migrated in response to a Security Advisory, this field will contain the approximate time the Linode will be taken offline for migration.  |  [optional] [readonly] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| MINOR | &quot;minor&quot; |
| MAJOR | &quot;major&quot; |
| CRITICAL | &quot;critical&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MIGRATION_SCHEDULED | &quot;migration_scheduled&quot; |
| MIGRATION_IMMINENT | &quot;migration_imminent&quot; |
| MIGRATION_PENDING | &quot;migration_pending&quot; |
| REBOOT_SCHEDULED | &quot;reboot_scheduled&quot; |
| OUTAGE | &quot;outage&quot; |
| PAYMENT_DUE | &quot;payment_due&quot; |
| TICKET_IMPORTANT | &quot;ticket_important&quot; |
| TICKET_ABUSE | &quot;ticket_abuse&quot; |
| NOTICE | &quot;notice&quot; |
| MAINTENANCE | &quot;maintenance&quot; |
| PROMOTION | &quot;promotion&quot; |



