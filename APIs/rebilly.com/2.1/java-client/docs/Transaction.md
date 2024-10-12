

# Transaction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_3ds** | [**ThreeDSecureResult**](ThreeDSecureResult.md) |  |  [optional] |
|**amount** | **Double** | The transaction&#39;s amount. |  [optional] [readonly] |
|**billingAddress** | [**ContactObject**](ContactObject.md) | Billing address. |  [optional] |
|**billingDescriptor** | **String** | The billing descriptor that appears on the periodic billing statement. Commonly 12 or fewer characters for a credit card statement.  |  [optional] [readonly] |
|**childTransactions** | **List&lt;String&gt;** | The child transaction IDs. |  [optional] [readonly] |
|**createdTime** | **OffsetDateTime** | Transaction created time. |  [optional] [readonly] |
|**currency** | **String** | ISO 4217 alphabetic currency code. |  [optional] [readonly] |
|**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  |  [optional] |
|**customerId** | **String** | The сustomer&#39;s ID. |  [optional] |
|**description** | **String** | The payment description. |  [optional] |
|**gatewayName** | **GatewayName** | Payment Gateway name, available only after the gateway is selected for the transaction.  |  [optional] [readonly] |
|**has3ds** | **Boolean** |  |  [optional] [readonly] |
|**hasAmountAdjustment** | **Boolean** | True if transaction has amount adjustment. |  [optional] [readonly] |
|**id** | **String** | The transaction ID. |  [optional] [readonly] |
|**invoiceIds** | **List&lt;String&gt;** | The invoice IDs related to transaction. |  [optional] [readonly] |
|**isRebill** | **Boolean** |  |  [optional] [readonly] |
|**isRetry** | **Boolean** | True if this transaction is retry. |  [optional] [readonly] |
|**parentTransactionId** | **String** | The parent&#39;s transaction ID. |  [optional] [readonly] |
|**paymentInstrument** | [**PaymentInstrument**](PaymentInstrument.md) |  |  [optional] |
|**planIds** | **List&lt;String&gt;** | The plan IDs related to transaction&#39;s order(s). |  [optional] [readonly] |
|**processedTime** | **OffsetDateTime** | Transaction processed time. |  [optional] [readonly] |
|**purchaseAmount** | **Double** | The amount actually purchased which may have differed from the originally requested amount in case of an adjustment. |  [optional] [readonly] |
|**purchaseCurrency** | **String** | ISO 4217 alphabetic currency code. |  [optional] [readonly] |
|**rebillNumber** | **Integer** | The transaction&#39;s rebill number. |  [optional] [readonly] |
|**redirectUrl** | **URI** | The URL to redirect the end-user when an offsite transaction is completed. Defaults to the website&#39;s configured URL. |  [optional] |
|**requestAmount** | **Double** | The amount in the payment request. If adjusted, the purchase amount and billing amount may vary from it. |  [optional] [readonly] |
|**requestCurrency** | **String** | ISO 4217 alphabetic currency code. |  [optional] [readonly] |
|**requestId** | **String** | The transaction&#39;s request ID.  This ID must be unique within a 24 hour period. Use this field to prevent duplicated transactions. |  [optional] |
|**result** | [**ResultEnum**](#ResultEnum) | Transaction result. |  [optional] [readonly] |
|**retryNumber** | **Integer** | The position in the sequence of retries. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Transaction status. |  [optional] [readonly] |
|**subscriptionIds** | **List&lt;String&gt;** | The orders IDs related to transaction&#39;s invoice(s). |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Transaction type. |  [optional] [readonly] |
|**updatedTime** | **OffsetDateTime** | Transaction updated time. |  [optional] [readonly] |
|**websiteId** | **String** | The website ID. |  [optional] [readonly] |
|**embedded** | [**List&lt;TransactionAllOfEmbedded&gt;**](TransactionAllOfEmbedded.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. |  [optional] [readonly] |
|**links** | [**List&lt;TransactionAllOfLinks&gt;**](TransactionAllOfLinks.md) | The links related to resource. |  [optional] [readonly] |
|**acquirerName** | **AcquirerName** | Acquirer name, available only when transaction use gateway, else null. |  [optional] [readonly] |
|**arn** | **String** | The acquirer reference number. |  [optional] [readonly] |
|**bin** | **String** | Payment Card BIN. |  [optional] [readonly] |
|**bumpOffer** | [**TransactionAllOfBumpOffer**](TransactionAllOfBumpOffer.md) |  |  [optional] |
|**dcc** | [**TransactionAllOfDcc**](TransactionAllOfDcc.md) |  |  [optional] |
|**discrepancyTime** | **OffsetDateTime** | The time of the most recent discrepancy on the transaction. |  [optional] [readonly] |
|**disputeStatus** | [**DisputeStatusEnum**](#DisputeStatusEnum) | The dispute&#39;s status, else null. |  [optional] [readonly] |
|**disputeTime** | **OffsetDateTime** | Time the dispute was created, else null. |  [optional] [readonly] |
|**gateway** | [**TransactionAllOfGateway**](TransactionAllOfGateway.md) |  |  [optional] |
|**gatewayAccountId** | **String** | The transaction&#39;s Gateway Account ID. |  [optional] [readonly] |
|**gatewayTransactionId** | **String** | The gateway&#39;s transaction ID. |  [optional] [readonly] |
|**hadDiscrepancy** | **Boolean** | True if the transaction has been updated due to a discrepancy with its. source of truth. |  [optional] [readonly] |
|**hasBumpOffer** | **Boolean** | True if transaction has a Bump offer. |  [optional] [readonly] |
|**hasDcc** | **Boolean** | True if transaction has Dynamic Currency Conversion applied. |  [optional] [readonly] |
|**isDisputed** | **Boolean** | True if transaction is disputed. |  [optional] [readonly] |
|**isMerchantInitiated** | **Boolean** | True if the transaction was initiated by the merchant. |  [optional] |
|**isProcessedOutside** | **Boolean** | True if the transaction was processed outside of Rebilly. |  [optional] |
|**isReconciled** | **Boolean** | True if the transaction has been verified with gateway batch data. |  [optional] [readonly] |
|**method** | **PaymentMethod** | Payment Method. Use &#x60;paymentInstrument.method&#x60; instead. |  [optional] |
|**notificationUrl** | **URI** | The URL where a server-to-server POST notification will be sent.  It  will be sent when the transaction&#39;s result is finalized after a timeout or an offsite interaction. Do not trust the notification; follow with a GET request to confirm the result of the transaction. Please respond with a 2xx HTTP status code, or we will reattempt the request again. The 2 placeholders are available to use in this URI: &#x60;{id}&#x60; and &#x60;{result}&#x60;.  |  [optional] |
|**orderId** | **String** | The transaction&#39;s order ID.  This ID must be unique within a 24 hour period. This field was renamed to the &#x60;requestId&#x60;. |  [optional] |
|**referenceData** | **Map&lt;String, String&gt;** | Transaction reference data. |  [optional] [readonly] |
|**reportAmount** | **Double** | Transaction amount converted to organization&amp;nbsp;selected report currency. |  [optional] [readonly] |
|**reportCurrency** | **String** | ISO 4217 alphabetic currency code. |  [optional] [readonly] |
|**retriedTransactionId** | **String** | The retried transaction ID. |  [optional] [readonly] |
|**retriesResult** | [**RetriesResultEnum**](#RetriesResultEnum) | Retries sequence result. |  [optional] [readonly] |
|**retryInstruction** | [**PaymentRetry**](PaymentRetry.md) |  |  [optional] |
|**revision** | **Integer** | The number of times the transaction data has been modified. The revision is useful when analyzing webhook data to determine if the change takes precedence over the current representation.  |  [optional] [readonly] |
|**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) | Risk metadata. |  [optional] |
|**riskScore** | **Integer** | The transaction&#39;s risk score. |  [optional] [readonly] |
|**scheduledTime** | **OffsetDateTime** | The time the transaction is scheduled for collection. |  [optional] |
|**settlementTime** | **OffsetDateTime** | The time that the transaction was settled by the banking instuition. |  [optional] [readonly] |
|**velocity** | **Integer** | The number of transactions by the same customer in the past 24 hours. |  [optional] |



## Enum: ResultEnum

| Name | Value |
|---- | -----|
| ABANDONED | &quot;abandoned&quot; |
| APPROVED | &quot;approved&quot; |
| CANCELED | &quot;canceled&quot; |
| DECLINED | &quot;declined&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| COMPLETED | &quot;completed&quot; |
| CONN_ERROR | &quot;conn-error&quot; |
| DISPUTED | &quot;disputed&quot; |
| NEVER_SENT | &quot;never-sent&quot; |
| OFFSITE | &quot;offsite&quot; |
| PARTIALLY_REFUNDED | &quot;partially-refunded&quot; |
| PENDING | &quot;pending&quot; |
| REFUNDED | &quot;refunded&quot; |
| SENDING | &quot;sending&quot; |
| SUSPENDED | &quot;suspended&quot; |
| TIMEOUT | &quot;timeout&quot; |
| VOIDED | &quot;voided&quot; |
| WAITING_APPROVAL | &quot;waiting-approval&quot; |
| WAITING_CAPTURE | &quot;waiting-capture&quot; |
| WAITING_GATEWAY | &quot;waiting-gateway&quot; |
| WAITING_REFUND | &quot;waiting-refund&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| _3DS_AUTHENTICATION | &quot;3ds-authentication&quot; |
| AUTHORIZE | &quot;authorize&quot; |
| CAPTURE | &quot;capture&quot; |
| CREDIT | &quot;credit&quot; |
| REFUND | &quot;refund&quot; |
| SALE | &quot;sale&quot; |
| VOID | &quot;void&quot; |



## Enum: DisputeStatusEnum

| Name | Value |
|---- | -----|
| RESPONSE_NEEDED | &quot;response-needed&quot; |
| UNDER_REVIEW | &quot;under-review&quot; |
| FORFEITED | &quot;forfeited&quot; |
| WON | &quot;won&quot; |
| LOST | &quot;lost&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: RetriesResultEnum

| Name | Value |
|---- | -----|
| APPROVED | &quot;approved&quot; |
| CANCELED | &quot;canceled&quot; |
| DECLINED | &quot;declined&quot; |
| SCHEDULED | &quot;scheduled&quot; |



