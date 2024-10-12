# PosApi.PosWebhookEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumerId** | **String** | Unique consumer identifier. You can freely choose a consumer ID yourself. Most of the time, this is an ID of your internal data model that represents a user or account in your system (for example account:12345). If the consumer doesn&#39;t exist yet, Vault will upsert a consumer based on your ID. | [optional] 
**entityId** | **String** | The service provider&#39;s ID of the entity that triggered this event | [optional] 
**entityType** | **String** | The type entity that triggered this event | [optional] 
**entityUrl** | **String** | The url to retrieve entity detail. | [optional] 
**eventId** | **String** | Unique reference to this request event | [optional] 
**executionAttempt** | **Number** | The current count this request event has been attempted | [optional] 
**occurredAt** | **String** | ISO Datetime for when the original event occurred | [optional] 
**serviceId** | **String** | Service provider identifier | [optional] 
**unifiedApi** | **String** | Name of Apideck Unified API | [optional] 
**eventType** | **String** |  | [optional] 



## Enum: UnifiedApiEnum


* `accounting` (value: `"accounting"`)

* `ats` (value: `"ats"`)

* `calendar` (value: `"calendar"`)

* `crm` (value: `"crm"`)

* `csp` (value: `"csp"`)

* `customer-support` (value: `"customer-support"`)

* `ecommerce` (value: `"ecommerce"`)

* `email` (value: `"email"`)

* `email-marketing` (value: `"email-marketing"`)

* `expense-management` (value: `"expense-management"`)

* `file-storage` (value: `"file-storage"`)

* `form` (value: `"form"`)

* `hris` (value: `"hris"`)

* `lead` (value: `"lead"`)

* `payroll` (value: `"payroll"`)

* `pos` (value: `"pos"`)

* `procurement` (value: `"procurement"`)

* `project-management` (value: `"project-management"`)

* `script` (value: `"script"`)

* `sms` (value: `"sms"`)

* `spreadsheet` (value: `"spreadsheet"`)

* `team-messaging` (value: `"team-messaging"`)

* `issue-tracking` (value: `"issue-tracking"`)

* `time-registration` (value: `"time-registration"`)

* `transactional-email` (value: `"transactional-email"`)

* `vault` (value: `"vault"`)

* `data-warehouse` (value: `"data-warehouse"`)





## Enum: EventTypeEnum


* `order.created` (value: `"pos.order.created"`)

* `order.updated` (value: `"pos.order.updated"`)

* `order.deleted` (value: `"pos.order.deleted"`)

* `payment.created` (value: `"pos.payment.created"`)

* `payment.updated` (value: `"pos.payment.updated"`)

* `payment.deleted` (value: `"pos.payment.deleted"`)

* `merchant.created` (value: `"pos.merchant.created"`)

* `merchant.updated` (value: `"pos.merchant.updated"`)

* `merchant.deleted` (value: `"pos.merchant.deleted"`)

* `location.created` (value: `"pos.location.created"`)

* `location.updated` (value: `"pos.location.updated"`)

* `location.deleted` (value: `"pos.location.deleted"`)

* `item.created` (value: `"pos.item.created"`)

* `item.updated` (value: `"pos.item.updated"`)

* `item.deleted` (value: `"pos.item.deleted"`)

* `modifier.created` (value: `"pos.modifier.created"`)

* `modifier.updated` (value: `"pos.modifier.updated"`)

* `modifier.deleted` (value: `"pos.modifier.deleted"`)

* `modifier-group.created` (value: `"pos.modifier-group.created"`)

* `modifier-group.updated` (value: `"pos.modifier-group.updated"`)

* `modifier-group.deleted` (value: `"pos.modifier-group.deleted"`)




