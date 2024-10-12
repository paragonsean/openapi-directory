

# BulkPaymentInitiationWithStatusResponse

Generic JSON response body consistion of the corresponding bulk payment initation JSON body together with an optional transaction status field. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptorTransactionDateTime** | **OffsetDateTime** |  |  [optional] |
|**batchBookingPreferred** | **Boolean** | If this element equals &#39;true&#39;, the PSU prefers only one booking entry. If this element equals &#39;false&#39;, the PSU prefers individual booking of all contained individual transactions.  The ASPSP will follow this preference according to contracts agreed on with the PSU.  |  [optional] |
|**debtorAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  |  |
|**paymentInformationId** | **String** |  |  [optional] |
|**payments** | [**List&lt;PaymentInitiationBulkElementJson&gt;**](PaymentInitiationBulkElementJson.md) | A list of generic JSON bodies payment initations for bulk payments via JSON.  Note: Some fields from single payments do not occcur in a bulk payment element  |  |
|**requestedExecutionDate** | **LocalDate** |  |  [optional] |
|**transactionStatus** | **TransactionStatus** |  |  [optional] |



