

# ConnectionWebhook


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**deliveryUrl** | **URI** | The delivery url of the webhook endpoint. |  |
|**description** | **String** | A description of the object. |  [optional] |
|**disabledReason** | [**DisabledReasonEnum**](#DisabledReasonEnum) | Indicates if the webhook has has been disabled as it reached its retry limit or if account is over the usage allocated by it&#39;s plan. |  [optional] |
|**events** | [**List&lt;EventsEnum&gt;**](#List&lt;EventsEnum&gt;) | The list of subscribed events for this webhook. [&#x60;*&#x60;] indicates that all events are enabled. |  |
|**executeBaseUrl** | **URI** | The Unify Base URL events from connectors will be sent to after service id is appended. |  [readonly] |
|**id** | **String** |  |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the webhook. |  |
|**unifiedApi** | **UnifiedApiId** |  |  |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |



## Enum: DisabledReasonEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| RETRY_LIMIT | &quot;retry_limit&quot; |
| USAGE_LIMIT | &quot;usage_limit&quot; |



## Enum: List&lt;EventsEnum&gt;

| Name | Value |
|---- | -----|
| STAR | &quot;*&quot; |
| CRM_ACTIVITY_CREATED | &quot;crm.activity.created&quot; |
| CRM_ACTIVITY_UPDATED | &quot;crm.activity.updated&quot; |
| CRM_ACTIVITY_DELETED | &quot;crm.activity.deleted&quot; |
| CRM_COMPANY_CREATED | &quot;crm.company.created&quot; |
| CRM_COMPANY_UPDATED | &quot;crm.company.updated&quot; |
| CRM_COMPANY_DELETED | &quot;crm.company.deleted&quot; |
| CRM_CONTACT_CREATED | &quot;crm.contact.created&quot; |
| CRM_CONTACT_UPDATED | &quot;crm.contact.updated&quot; |
| CRM_CONTACT_DELETED | &quot;crm.contact.deleted&quot; |
| CRM_LEAD_CREATED | &quot;crm.lead.created&quot; |
| CRM_LEAD_UPDATED | &quot;crm.lead.updated&quot; |
| CRM_LEAD_DELETED | &quot;crm.lead.deleted&quot; |
| CRM_NOTE_CREATED | &quot;crm.note.created&quot; |
| CRM_NOTES_UPDATED | &quot;crm.notes.updated&quot; |
| CRM_NOTES_DELETED | &quot;crm.notes.deleted&quot; |
| CRM_OPPORTUNITY_CREATED | &quot;crm.opportunity.created&quot; |
| CRM_OPPORTUNITY_UPDATED | &quot;crm.opportunity.updated&quot; |
| CRM_OPPORTUNITY_DELETED | &quot;crm.opportunity.deleted&quot; |
| LEAD_LEAD_CREATED | &quot;lead.lead.created&quot; |
| LEAD_LEAD_UPDATED | &quot;lead.lead.updated&quot; |
| LEAD_LEAD_DELETED | &quot;lead.lead.deleted&quot; |
| VAULT_CONNECTION_CREATED | &quot;vault.connection.created&quot; |
| VAULT_CONNECTION_UPDATED | &quot;vault.connection.updated&quot; |
| VAULT_CONNECTION_DISABLED | &quot;vault.connection.disabled&quot; |
| VAULT_CONNECTION_DELETED | &quot;vault.connection.deleted&quot; |
| VAULT_CONNECTION_CALLABLE | &quot;vault.connection.callable&quot; |
| VAULT_CONNECTION_REVOKED | &quot;vault.connection.revoked&quot; |
| VAULT_CONNECTION_TOKEN_REFRESH_FAILED | &quot;vault.connection.token_refresh.failed&quot; |
| ATS_JOB_CREATED | &quot;ats.job.created&quot; |
| ATS_JOB_UPDATED | &quot;ats.job.updated&quot; |
| ATS_JOB_DELETED | &quot;ats.job.deleted&quot; |
| ATS_APPLICANT_CREATED | &quot;ats.applicant.created&quot; |
| ATS_APPLICANT_UPDATED | &quot;ats.applicant.updated&quot; |
| ATS_APPLICANT_DELETED | &quot;ats.applicant.deleted&quot; |
| ACCOUNTING_CUSTOMER_CREATED | &quot;accounting.customer.created&quot; |
| ACCOUNTING_CUSTOMER_UPDATED | &quot;accounting.customer.updated&quot; |
| ACCOUNTING_CUSTOMER_DELETED | &quot;accounting.customer.deleted&quot; |
| ACCOUNTING_INVOICE_CREATED | &quot;accounting.invoice.created&quot; |
| ACCOUNTING_INVOICE_UPDATED | &quot;accounting.invoice.updated&quot; |
| ACCOUNTING_INVOICE_DELETED | &quot;accounting.invoice.deleted&quot; |
| ACCOUNTING_INVOICE_ITEM_CREATED | &quot;accounting.invoice_item.created&quot; |
| ACCOUNTING_INVOICE_ITEM_UPDATED | &quot;accounting.invoice_item.updated&quot; |
| ACCOUNTING_INVOICE_ITEM_DELETED | &quot;accounting.invoice_item.deleted&quot; |
| ACCOUNTING_LEDGER_ACCOUNT_CREATED | &quot;accounting.ledger_account.created&quot; |
| ACCOUNTING_LEDGER_ACCOUNT_UPDATED | &quot;accounting.ledger_account.updated&quot; |
| ACCOUNTING_LEDGER_ACCOUNT_DELETED | &quot;accounting.ledger_account.deleted&quot; |
| ACCOUNTING_TAX_RATE_CREATED | &quot;accounting.tax_rate.created&quot; |
| ACCOUNTING_TAX_RATE_UPDATED | &quot;accounting.tax_rate.updated&quot; |
| ACCOUNTING_TAX_RATE_DELETED | &quot;accounting.tax_rate.deleted&quot; |
| ACCOUNTING_BILL_CREATED | &quot;accounting.bill.created&quot; |
| ACCOUNTING_BILL_UPDATED | &quot;accounting.bill.updated&quot; |
| ACCOUNTING_BILL_DELETED | &quot;accounting.bill.deleted&quot; |
| ACCOUNTING_PAYMENT_CREATED | &quot;accounting.payment.created&quot; |
| ACCOUNTING_PAYMENT_UPDATED | &quot;accounting.payment.updated&quot; |
| ACCOUNTING_PAYMENT_DELETED | &quot;accounting.payment.deleted&quot; |
| ACCOUNTING_SUPPLIER_CREATED | &quot;accounting.supplier.created&quot; |
| ACCOUNTING_SUPPLIER_UPDATED | &quot;accounting.supplier.updated&quot; |
| ACCOUNTING_SUPPLIER_DELETED | &quot;accounting.supplier.deleted&quot; |
| ACCOUNTING_PURCHASE_ORDER_CREATED | &quot;accounting.purchase-order.created&quot; |
| ACCOUNTING_PURCHASE_ORDER_UPDATED | &quot;accounting.purchase-order.updated&quot; |
| ACCOUNTING_PURCHASE_ORDER_DELETED | &quot;accounting.purchase-order.deleted&quot; |
| POS_ORDER_CREATED | &quot;pos.order.created&quot; |
| POS_ORDER_UPDATED | &quot;pos.order.updated&quot; |
| POS_ORDER_DELETED | &quot;pos.order.deleted&quot; |
| POS_PRODUCT_CREATED | &quot;pos.product.created&quot; |
| POS_PRODUCT_UPDATED | &quot;pos.product.updated&quot; |
| POS_PRODUCT_DELETED | &quot;pos.product.deleted&quot; |
| POS_PAYMENT_CREATED | &quot;pos.payment.created&quot; |
| POS_PAYMENT_UPDATED | &quot;pos.payment.updated&quot; |
| POS_PAYMENT_DELETED | &quot;pos.payment.deleted&quot; |
| POS_MERCHANT_CREATED | &quot;pos.merchant.created&quot; |
| POS_MERCHANT_UPDATED | &quot;pos.merchant.updated&quot; |
| POS_MERCHANT_DELETED | &quot;pos.merchant.deleted&quot; |
| POS_LOCATION_CREATED | &quot;pos.location.created&quot; |
| POS_LOCATION_UPDATED | &quot;pos.location.updated&quot; |
| POS_LOCATION_DELETED | &quot;pos.location.deleted&quot; |
| POS_ITEM_CREATED | &quot;pos.item.created&quot; |
| POS_ITEM_UPDATED | &quot;pos.item.updated&quot; |
| POS_ITEM_DELETED | &quot;pos.item.deleted&quot; |
| POS_MODIFIER_CREATED | &quot;pos.modifier.created&quot; |
| POS_MODIFIER_UPDATED | &quot;pos.modifier.updated&quot; |
| POS_MODIFIER_DELETED | &quot;pos.modifier.deleted&quot; |
| POS_MODIFIER_GROUP_CREATED | &quot;pos.modifier-group.created&quot; |
| POS_MODIFIER_GROUP_UPDATED | &quot;pos.modifier-group.updated&quot; |
| POS_MODIFIER_GROUP_DELETED | &quot;pos.modifier-group.deleted&quot; |
| HRIS_EMPLOYEE_CREATED | &quot;hris.employee.created&quot; |
| HRIS_EMPLOYEE_UPDATED | &quot;hris.employee.updated&quot; |
| HRIS_EMPLOYEE_DELETED | &quot;hris.employee.deleted&quot; |
| HRIS_EMPLOYEE_TERMINATED | &quot;hris.employee.terminated&quot; |
| HRIS_COMPANY_CREATED | &quot;hris.company.created&quot; |
| HRIS_COMPANY_UPDATED | &quot;hris.company.updated&quot; |
| HRIS_COMPANY_DELETED | &quot;hris.company.deleted&quot; |
| FILE_STORAGE_FILE_CREATED | &quot;file-storage.file.created&quot; |
| FILE_STORAGE_FILE_UPDATED | &quot;file-storage.file.updated&quot; |
| FILE_STORAGE_FILE_DELETED | &quot;file-storage.file.deleted&quot; |
| ISSUE_TRACKING_TICKET_CREATED | &quot;issue-tracking.ticket.created&quot; |
| ISSUE_TRACKING_TICKET_UPDATED | &quot;issue-tracking.ticket.updated&quot; |
| ISSUE_TRACKING_TICKET_DELETED | &quot;issue-tracking.ticket.deleted&quot; |
| ATS_APPLICATION_CREATED | &quot;ats.application.created&quot; |
| ATS_APPLICATION_UPDATED | &quot;ats.application.updated&quot; |
| ATS_APPLICATION_DELETED | &quot;ats.application.deleted&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;enabled&quot; |
| DISABLED | &quot;disabled&quot; |



