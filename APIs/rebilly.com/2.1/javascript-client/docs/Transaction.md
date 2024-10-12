# RebillyRestApi.Transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_3ds** | [**ThreeDSecureResult**](ThreeDSecureResult.md) |  | [optional] 
**amount** | **Number** | The transaction&#39;s amount. | [optional] [readonly] 
**billingAddress** | [**ContactObject**](ContactObject.md) | Billing address. | [optional] 
**billingDescriptor** | **String** | The billing descriptor that appears on the periodic billing statement. Commonly 12 or fewer characters for a credit card statement.  | [optional] [readonly] 
**childTransactions** | **[String]** | The child transaction IDs. | [optional] [readonly] 
**createdTime** | **Date** | Transaction created time. | [optional] [readonly] 
**currency** | **String** | ISO 4217 alphabetic currency code. | [optional] [readonly] 
**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  | [optional] 
**customerId** | **String** | The сustomer&#39;s ID. | [optional] 
**description** | **String** | The payment description. | [optional] 
**gatewayName** | [**GatewayName**](GatewayName.md) | Payment Gateway name, available only after the gateway is selected for the transaction.  | [optional] [readonly] 
**has3ds** | **Boolean** |  | [optional] [readonly] 
**hasAmountAdjustment** | **Boolean** | True if transaction has amount adjustment. | [optional] [readonly] 
**id** | **String** | The transaction ID. | [optional] [readonly] 
**invoiceIds** | **[String]** | The invoice IDs related to transaction. | [optional] [readonly] 
**isRebill** | **Boolean** |  | [optional] [readonly] 
**isRetry** | **Boolean** | True if this transaction is retry. | [optional] [readonly] 
**parentTransactionId** | **String** | The parent&#39;s transaction ID. | [optional] [readonly] 
**paymentInstrument** | [**PaymentInstrument**](PaymentInstrument.md) |  | [optional] 
**planIds** | **[String]** | The plan IDs related to transaction&#39;s order(s). | [optional] [readonly] 
**processedTime** | **Date** | Transaction processed time. | [optional] [readonly] 
**purchaseAmount** | **Number** | The amount actually purchased which may have differed from the originally requested amount in case of an adjustment. | [optional] [readonly] 
**purchaseCurrency** | **String** | ISO 4217 alphabetic currency code. | [optional] [readonly] 
**rebillNumber** | **Number** | The transaction&#39;s rebill number. | [optional] [readonly] 
**redirectUrl** | **String** | The URL to redirect the end-user when an offsite transaction is completed. Defaults to the website&#39;s configured URL. | [optional] 
**requestAmount** | **Number** | The amount in the payment request. If adjusted, the purchase amount and billing amount may vary from it. | [optional] [readonly] 
**requestCurrency** | **String** | ISO 4217 alphabetic currency code. | [optional] [readonly] 
**requestId** | **String** | The transaction&#39;s request ID.  This ID must be unique within a 24 hour period. Use this field to prevent duplicated transactions. | [optional] 
**result** | **String** | Transaction result. | [optional] [readonly] 
**retryNumber** | **Number** | The position in the sequence of retries. | [optional] [readonly] 
**status** | **String** | Transaction status. | [optional] [readonly] 
**subscriptionIds** | **[String]** | The orders IDs related to transaction&#39;s invoice(s). | [optional] [readonly] 
**type** | **String** | Transaction type. | [optional] [readonly] 
**updatedTime** | **Date** | Transaction updated time. | [optional] [readonly] 
**websiteId** | **String** | The website ID. | [optional] [readonly] 
**embedded** | [**[TransactionAllOfEmbedded]**](TransactionAllOfEmbedded.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. | [optional] [readonly] 
**links** | [**[TransactionAllOfLinks]**](TransactionAllOfLinks.md) | The links related to resource. | [optional] [readonly] 
**acquirerName** | [**AcquirerName**](AcquirerName.md) | Acquirer name, available only when transaction use gateway, else null. | [optional] [readonly] 
**arn** | **String** | The acquirer reference number. | [optional] [readonly] 
**bin** | **String** | Payment Card BIN. | [optional] [readonly] 
**bumpOffer** | [**TransactionAllOfBumpOffer**](TransactionAllOfBumpOffer.md) |  | [optional] 
**dcc** | [**TransactionAllOfDcc**](TransactionAllOfDcc.md) |  | [optional] 
**discrepancyTime** | **Date** | The time of the most recent discrepancy on the transaction. | [optional] [readonly] 
**disputeStatus** | **String** | The dispute&#39;s status, else null. | [optional] [readonly] 
**disputeTime** | **Date** | Time the dispute was created, else null. | [optional] [readonly] 
**gateway** | [**TransactionAllOfGateway**](TransactionAllOfGateway.md) |  | [optional] 
**gatewayAccountId** | **String** | The transaction&#39;s Gateway Account ID. | [optional] [readonly] 
**gatewayTransactionId** | **String** | The gateway&#39;s transaction ID. | [optional] [readonly] 
**hadDiscrepancy** | **Boolean** | True if the transaction has been updated due to a discrepancy with its. source of truth. | [optional] [readonly] 
**hasBumpOffer** | **Boolean** | True if transaction has a Bump offer. | [optional] [readonly] 
**hasDcc** | **Boolean** | True if transaction has Dynamic Currency Conversion applied. | [optional] [readonly] 
**isDisputed** | **Boolean** | True if transaction is disputed. | [optional] [readonly] 
**isMerchantInitiated** | **Boolean** | True if the transaction was initiated by the merchant. | [optional] 
**isProcessedOutside** | **Boolean** | True if the transaction was processed outside of Rebilly. | [optional] 
**isReconciled** | **Boolean** | True if the transaction has been verified with gateway batch data. | [optional] [readonly] 
**method** | [**PaymentMethod**](PaymentMethod.md) | Payment Method. Use &#x60;paymentInstrument.method&#x60; instead. | [optional] 
**notificationUrl** | **String** | The URL where a server-to-server POST notification will be sent.  It  will be sent when the transaction&#39;s result is finalized after a timeout or an offsite interaction. Do not trust the notification; follow with a GET request to confirm the result of the transaction. Please respond with a 2xx HTTP status code, or we will reattempt the request again. The 2 placeholders are available to use in this URI: &#x60;{id}&#x60; and &#x60;{result}&#x60;.  | [optional] 
**orderId** | **String** | The transaction&#39;s order ID.  This ID must be unique within a 24 hour period. This field was renamed to the &#x60;requestId&#x60;. | [optional] 
**referenceData** | **{String: String}** | Transaction reference data. | [optional] [readonly] 
**reportAmount** | **Number** | Transaction amount converted to organization&amp;nbsp;selected report currency. | [optional] [readonly] 
**reportCurrency** | **String** | ISO 4217 alphabetic currency code. | [optional] [readonly] 
**retriedTransactionId** | **String** | The retried transaction ID. | [optional] [readonly] 
**retriesResult** | **String** | Retries sequence result. | [optional] [readonly] 
**retryInstruction** | [**PaymentRetry**](PaymentRetry.md) |  | [optional] 
**revision** | **Number** | The number of times the transaction data has been modified. The revision is useful when analyzing webhook data to determine if the change takes precedence over the current representation.  | [optional] [readonly] 
**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) | Risk metadata. | [optional] 
**riskScore** | **Number** | The transaction&#39;s risk score. | [optional] [readonly] 
**scheduledTime** | **Date** | The time the transaction is scheduled for collection. | [optional] 
**settlementTime** | **Date** | The time that the transaction was settled by the banking instuition. | [optional] [readonly] 
**velocity** | **Number** | The number of transactions by the same customer in the past 24 hours. | [optional] 



## Enum: ResultEnum


* `abandoned` (value: `"abandoned"`)

* `approved` (value: `"approved"`)

* `canceled` (value: `"canceled"`)

* `declined` (value: `"declined"`)

* `unknown` (value: `"unknown"`)





## Enum: StatusEnum


* `completed` (value: `"completed"`)

* `conn-error` (value: `"conn-error"`)

* `disputed` (value: `"disputed"`)

* `never-sent` (value: `"never-sent"`)

* `offsite` (value: `"offsite"`)

* `partially-refunded` (value: `"partially-refunded"`)

* `pending` (value: `"pending"`)

* `refunded` (value: `"refunded"`)

* `sending` (value: `"sending"`)

* `suspended` (value: `"suspended"`)

* `timeout` (value: `"timeout"`)

* `voided` (value: `"voided"`)

* `waiting-approval` (value: `"waiting-approval"`)

* `waiting-capture` (value: `"waiting-capture"`)

* `waiting-gateway` (value: `"waiting-gateway"`)

* `waiting-refund` (value: `"waiting-refund"`)





## Enum: TypeEnum


* `3ds-authentication` (value: `"3ds-authentication"`)

* `authorize` (value: `"authorize"`)

* `capture` (value: `"capture"`)

* `credit` (value: `"credit"`)

* `refund` (value: `"refund"`)

* `sale` (value: `"sale"`)

* `void` (value: `"void"`)





## Enum: DisputeStatusEnum


* `response-needed` (value: `"response-needed"`)

* `under-review` (value: `"under-review"`)

* `forfeited` (value: `"forfeited"`)

* `won` (value: `"won"`)

* `lost` (value: `"lost"`)

* `unknown` (value: `"unknown"`)





## Enum: RetriesResultEnum


* `approved` (value: `"approved"`)

* `canceled` (value: `"canceled"`)

* `declined` (value: `"declined"`)

* `scheduled` (value: `"scheduled"`)




