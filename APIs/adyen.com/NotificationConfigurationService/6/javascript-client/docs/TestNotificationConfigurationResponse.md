# NotificationConfigurationApi.TestNotificationConfigurationResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorMessages** | **[String]** | Any error messages encountered. | [optional] 
**eventTypes** | **[String]** | The event types that were tested. &gt;Permitted values: &#x60;ACCOUNT_HOLDER_CREATED&#x60;, &#x60;ACCOUNT_CREATED&#x60;, &#x60;ACCOUNT_UPDATED&#x60;, &#x60;ACCOUNT_HOLDER_UPDATED&#x60;, &#x60;ACCOUNT_HOLDER_STATUS_CHANGE&#x60;, &#x60;ACCOUNT_HOLDER_STORE_STATUS_CHANGE&#x60; &#x60;ACCOUNT_HOLDER_VERIFICATION&#x60;, &#x60;ACCOUNT_HOLDER_LIMIT_REACHED&#x60;, &#x60;ACCOUNT_HOLDER_PAYOUT&#x60;, &#x60;PAYMENT_FAILURE&#x60;, &#x60;SCHEDULED_REFUNDS&#x60;, &#x60;REPORT_AVAILABLE&#x60;, &#x60;TRANSFER_FUNDS&#x60;, &#x60;BENEFICIARY_SETUP&#x60;, &#x60;COMPENSATE_NEGATIVE_BALANCE&#x60;. | [optional] 
**exchangeMessages** | [**[ExchangeMessage]**](ExchangeMessage.md) | The notification message and related response messages. | [optional] 
**invalidFields** | [**[ErrorFieldType]**](ErrorFieldType.md) | Contains field validation errors that would prevent requests from being processed. | [optional] 
**notificationId** | **Number** | The ID of the notification subscription configuration. | 
**okMessages** | **[String]** | A list of messages describing the testing steps. | [optional] 
**pspReference** | **String** | The reference of a request. Can be used to uniquely identify the request. | [optional] 
**resultCode** | **String** | The result code. | [optional] 



## Enum: [EventTypesEnum]


* `ACCOUNT_CLOSED` (value: `"ACCOUNT_CLOSED"`)

* `ACCOUNT_CREATED` (value: `"ACCOUNT_CREATED"`)

* `ACCOUNT_FUNDS_BELOW_THRESHOLD` (value: `"ACCOUNT_FUNDS_BELOW_THRESHOLD"`)

* `ACCOUNT_HOLDER_CREATED` (value: `"ACCOUNT_HOLDER_CREATED"`)

* `ACCOUNT_HOLDER_LIMIT_REACHED` (value: `"ACCOUNT_HOLDER_LIMIT_REACHED"`)

* `ACCOUNT_HOLDER_MIGRATED` (value: `"ACCOUNT_HOLDER_MIGRATED"`)

* `ACCOUNT_HOLDER_PAYOUT` (value: `"ACCOUNT_HOLDER_PAYOUT"`)

* `ACCOUNT_HOLDER_STATUS_CHANGE` (value: `"ACCOUNT_HOLDER_STATUS_CHANGE"`)

* `ACCOUNT_HOLDER_STORE_STATUS_CHANGE` (value: `"ACCOUNT_HOLDER_STORE_STATUS_CHANGE"`)

* `ACCOUNT_HOLDER_UPCOMING_DEADLINE` (value: `"ACCOUNT_HOLDER_UPCOMING_DEADLINE"`)

* `ACCOUNT_HOLDER_UPDATED` (value: `"ACCOUNT_HOLDER_UPDATED"`)

* `ACCOUNT_HOLDER_VERIFICATION` (value: `"ACCOUNT_HOLDER_VERIFICATION"`)

* `ACCOUNT_UPDATED` (value: `"ACCOUNT_UPDATED"`)

* `BENEFICIARY_SETUP` (value: `"BENEFICIARY_SETUP"`)

* `COMPENSATE_NEGATIVE_BALANCE` (value: `"COMPENSATE_NEGATIVE_BALANCE"`)

* `DIRECT_DEBIT_INITIATED` (value: `"DIRECT_DEBIT_INITIATED"`)

* `FUNDS_MIGRATED` (value: `"FUNDS_MIGRATED"`)

* `PAYMENT_FAILURE` (value: `"PAYMENT_FAILURE"`)

* `PENDING_CREDIT` (value: `"PENDING_CREDIT"`)

* `REFUND_FUNDS_TRANSFER` (value: `"REFUND_FUNDS_TRANSFER"`)

* `REPORT_AVAILABLE` (value: `"REPORT_AVAILABLE"`)

* `SCHEDULED_REFUNDS` (value: `"SCHEDULED_REFUNDS"`)

* `SCORE_SIGNAL_TRIGGERED` (value: `"SCORE_SIGNAL_TRIGGERED"`)

* `TRANSFER_FUNDS` (value: `"TRANSFER_FUNDS"`)

* `TRANSFER_NOT_PAIDOUT_TRANSFERS` (value: `"TRANSFER_NOT_PAIDOUT_TRANSFERS"`)




