# LinodeApi.Notification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **String** | A full description of this Notification, in markdown format.  Not all Notifications include bodies.  | [optional] [readonly] 
**entity** | [**NotificationEntity**](NotificationEntity.md) |  | [optional] 
**label** | **String** | A short description of this Notification.  | [optional] [readonly] 
**message** | **String** | A human-readable description of the Notification. | [optional] [readonly] 
**severity** | **String** | The severity of this Notification.  This field can be used to decide how prominently to display the Notification, what color to make the display text, etc.  | [optional] [readonly] 
**type** | **String** | The type of Notification this is. | [optional] [readonly] 
**until** | **Date** | If this Notification has a duration, this will be the ending time for the Event/action. For example, if there is scheduled maintenance for one of our systems, &#x60;until&#x60; would be set to the end of the maintenance window.  | [optional] [readonly] 
**when** | **Date** | If this Notification is of an Event that will happen at a fixed, future time, this is when the named action will be taken. For example, if a Linode is to be migrated in response to a Security Advisory, this field will contain the approximate time the Linode will be taken offline for migration.  | [optional] [readonly] 



## Enum: SeverityEnum


* `minor` (value: `"minor"`)

* `major` (value: `"major"`)

* `critical` (value: `"critical"`)





## Enum: TypeEnum


* `migration_scheduled` (value: `"migration_scheduled"`)

* `migration_imminent` (value: `"migration_imminent"`)

* `migration_pending` (value: `"migration_pending"`)

* `reboot_scheduled` (value: `"reboot_scheduled"`)

* `outage` (value: `"outage"`)

* `payment_due` (value: `"payment_due"`)

* `ticket_important` (value: `"ticket_important"`)

* `ticket_abuse` (value: `"ticket_abuse"`)

* `notice` (value: `"notice"`)

* `maintenance` (value: `"maintenance"`)

* `promotion` (value: `"promotion"`)




