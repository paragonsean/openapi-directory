

# TestNotificationConfigurationResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorMessages** | **List&lt;String&gt;** | Any error messages encountered. |  [optional] |
|**eventTypes** | [**List&lt;EventTypesEnum&gt;**](#List&lt;EventTypesEnum&gt;) | The event types that were tested. &gt;Permitted values: &#x60;ACCOUNT_HOLDER_CREATED&#x60;, &#x60;ACCOUNT_CREATED&#x60;, &#x60;ACCOUNT_UPDATED&#x60;, &#x60;ACCOUNT_HOLDER_UPDATED&#x60;, &#x60;ACCOUNT_HOLDER_STATUS_CHANGE&#x60;, &#x60;ACCOUNT_HOLDER_STORE_STATUS_CHANGE&#x60; &#x60;ACCOUNT_HOLDER_VERIFICATION&#x60;, &#x60;ACCOUNT_HOLDER_LIMIT_REACHED&#x60;, &#x60;ACCOUNT_HOLDER_PAYOUT&#x60;, &#x60;PAYMENT_FAILURE&#x60;, &#x60;SCHEDULED_REFUNDS&#x60;, &#x60;REPORT_AVAILABLE&#x60;, &#x60;TRANSFER_FUNDS&#x60;, &#x60;BENEFICIARY_SETUP&#x60;, &#x60;COMPENSATE_NEGATIVE_BALANCE&#x60;. |  [optional] |
|**exchangeMessages** | [**List&lt;ExchangeMessage&gt;**](ExchangeMessage.md) | The notification message and related response messages. |  [optional] |
|**invalidFields** | [**List&lt;ErrorFieldType&gt;**](ErrorFieldType.md) | Contains field validation errors that would prevent requests from being processed. |  [optional] |
|**notificationId** | **Long** | The ID of the notification subscription configuration. |  |
|**okMessages** | **List&lt;String&gt;** | A list of messages describing the testing steps. |  [optional] |
|**pspReference** | **String** | The reference of a request. Can be used to uniquely identify the request. |  [optional] |
|**resultCode** | **String** | The result code. |  [optional] |



## Enum: List&lt;EventTypesEnum&gt;

| Name | Value |
|---- | -----|
| ACCOUNT_CLOSED | &quot;ACCOUNT_CLOSED&quot; |
| ACCOUNT_CREATED | &quot;ACCOUNT_CREATED&quot; |
| ACCOUNT_FUNDS_BELOW_THRESHOLD | &quot;ACCOUNT_FUNDS_BELOW_THRESHOLD&quot; |
| ACCOUNT_HOLDER_CREATED | &quot;ACCOUNT_HOLDER_CREATED&quot; |
| ACCOUNT_HOLDER_LIMIT_REACHED | &quot;ACCOUNT_HOLDER_LIMIT_REACHED&quot; |
| ACCOUNT_HOLDER_MIGRATED | &quot;ACCOUNT_HOLDER_MIGRATED&quot; |
| ACCOUNT_HOLDER_PAYOUT | &quot;ACCOUNT_HOLDER_PAYOUT&quot; |
| ACCOUNT_HOLDER_STATUS_CHANGE | &quot;ACCOUNT_HOLDER_STATUS_CHANGE&quot; |
| ACCOUNT_HOLDER_STORE_STATUS_CHANGE | &quot;ACCOUNT_HOLDER_STORE_STATUS_CHANGE&quot; |
| ACCOUNT_HOLDER_UPCOMING_DEADLINE | &quot;ACCOUNT_HOLDER_UPCOMING_DEADLINE&quot; |
| ACCOUNT_HOLDER_UPDATED | &quot;ACCOUNT_HOLDER_UPDATED&quot; |
| ACCOUNT_HOLDER_VERIFICATION | &quot;ACCOUNT_HOLDER_VERIFICATION&quot; |
| ACCOUNT_UPDATED | &quot;ACCOUNT_UPDATED&quot; |
| BENEFICIARY_SETUP | &quot;BENEFICIARY_SETUP&quot; |
| COMPENSATE_NEGATIVE_BALANCE | &quot;COMPENSATE_NEGATIVE_BALANCE&quot; |
| DIRECT_DEBIT_INITIATED | &quot;DIRECT_DEBIT_INITIATED&quot; |
| FUNDS_MIGRATED | &quot;FUNDS_MIGRATED&quot; |
| PAYMENT_FAILURE | &quot;PAYMENT_FAILURE&quot; |
| PENDING_CREDIT | &quot;PENDING_CREDIT&quot; |
| REFUND_FUNDS_TRANSFER | &quot;REFUND_FUNDS_TRANSFER&quot; |
| REPORT_AVAILABLE | &quot;REPORT_AVAILABLE&quot; |
| SCHEDULED_REFUNDS | &quot;SCHEDULED_REFUNDS&quot; |
| SCORE_SIGNAL_TRIGGERED | &quot;SCORE_SIGNAL_TRIGGERED&quot; |
| TRANSFER_FUNDS | &quot;TRANSFER_FUNDS&quot; |
| TRANSFER_NOT_PAIDOUT_TRANSFERS | &quot;TRANSFER_NOT_PAIDOUT_TRANSFERS&quot; |



