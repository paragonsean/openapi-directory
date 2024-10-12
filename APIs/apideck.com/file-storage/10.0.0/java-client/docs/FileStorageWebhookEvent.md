

# FileStorageWebhookEvent


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
|**eventType** | **FileStorageEventType** |  |  [optional] |



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



