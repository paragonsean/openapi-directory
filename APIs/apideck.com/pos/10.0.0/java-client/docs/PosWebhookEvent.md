

# PosWebhookEvent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumerId** | **String** | Unique consumer identifier. You can freely choose a consumer ID yourself. Most of the time, this is an ID of your internal data model that represents a user or account in your system (for example account:12345). If the consumer doesn&#39;t exist yet, Vault will upsert a consumer based on your ID. |  [optional] |
|**entityId** | **String** | The service provider&#39;s ID of the entity that triggered this event |  [optional] |
|**entityType** | **String** | The type entity that triggered this event |  [optional] |
|**entityUrl** | **String** | The url to retrieve entity detail. |  [optional] |
|**eventId** | **String** | Unique reference to this request event |  [optional] |
|**executionAttempt** | **BigDecimal** | The current count this request event has been attempted |  [optional] |
|**occurredAt** | **String** | ISO Datetime for when the original event occurred |  [optional] |
|**serviceId** | **String** | Service provider identifier |  [optional] |
|**unifiedApi** | [**UnifiedApiEnum**](#UnifiedApiEnum) | Name of Apideck Unified API |  [optional] |
|**eventType** | [**EventTypeEnum**](#EventTypeEnum) |  |  [optional] |



## Enum: UnifiedApiEnum

| Name | Value |
|---- | -----|
| ACCOUNTING | &quot;accounting&quot; |
| ATS | &quot;ats&quot; |
| CALENDAR | &quot;calendar&quot; |
| CRM | &quot;crm&quot; |
| CSP | &quot;csp&quot; |
| CUSTOMER_SUPPORT | &quot;customer-support&quot; |
| ECOMMERCE | &quot;ecommerce&quot; |
| EMAIL | &quot;email&quot; |
| EMAIL_MARKETING | &quot;email-marketing&quot; |
| EXPENSE_MANAGEMENT | &quot;expense-management&quot; |
| FILE_STORAGE | &quot;file-storage&quot; |
| FORM | &quot;form&quot; |
| HRIS | &quot;hris&quot; |
| LEAD | &quot;lead&quot; |
| PAYROLL | &quot;payroll&quot; |
| POS | &quot;pos&quot; |
| PROCUREMENT | &quot;procurement&quot; |
| PROJECT_MANAGEMENT | &quot;project-management&quot; |
| SCRIPT | &quot;script&quot; |
| SMS | &quot;sms&quot; |
| SPREADSHEET | &quot;spreadsheet&quot; |
| TEAM_MESSAGING | &quot;team-messaging&quot; |
| ISSUE_TRACKING | &quot;issue-tracking&quot; |
| TIME_REGISTRATION | &quot;time-registration&quot; |
| TRANSACTIONAL_EMAIL | &quot;transactional-email&quot; |
| VAULT | &quot;vault&quot; |
| DATA_WAREHOUSE | &quot;data-warehouse&quot; |



## Enum: EventTypeEnum

| Name | Value |
|---- | -----|
| ORDER_CREATED | &quot;pos.order.created&quot; |
| ORDER_UPDATED | &quot;pos.order.updated&quot; |
| ORDER_DELETED | &quot;pos.order.deleted&quot; |
| PAYMENT_CREATED | &quot;pos.payment.created&quot; |
| PAYMENT_UPDATED | &quot;pos.payment.updated&quot; |
| PAYMENT_DELETED | &quot;pos.payment.deleted&quot; |
| MERCHANT_CREATED | &quot;pos.merchant.created&quot; |
| MERCHANT_UPDATED | &quot;pos.merchant.updated&quot; |
| MERCHANT_DELETED | &quot;pos.merchant.deleted&quot; |
| LOCATION_CREATED | &quot;pos.location.created&quot; |
| LOCATION_UPDATED | &quot;pos.location.updated&quot; |
| LOCATION_DELETED | &quot;pos.location.deleted&quot; |
| ITEM_CREATED | &quot;pos.item.created&quot; |
| ITEM_UPDATED | &quot;pos.item.updated&quot; |
| ITEM_DELETED | &quot;pos.item.deleted&quot; |
| MODIFIER_CREATED | &quot;pos.modifier.created&quot; |
| MODIFIER_UPDATED | &quot;pos.modifier.updated&quot; |
| MODIFIER_DELETED | &quot;pos.modifier.deleted&quot; |
| MODIFIER_GROUP_CREATED | &quot;pos.modifier-group.created&quot; |
| MODIFIER_GROUP_UPDATED | &quot;pos.modifier-group.updated&quot; |
| MODIFIER_GROUP_DELETED | &quot;pos.modifier-group.deleted&quot; |



