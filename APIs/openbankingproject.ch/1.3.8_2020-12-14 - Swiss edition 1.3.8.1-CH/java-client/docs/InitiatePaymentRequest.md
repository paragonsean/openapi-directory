

# InitiatePaymentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chargeBearer** | **ChargeBearer** |  |  [optional] |
|**creditorAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  |  |
|**creditorAddress** | [**Address**](Address.md) |  |  [optional] |
|**creditorAgent** | [**CreditorAgent7CH**](CreditorAgent7CH.md) |  |  [optional] |
|**creditorAgentName** | **String** | Creditor agent name. |  [optional] |
|**creditorId** | **String** | Identification of Creditors, e.g. a SEPA Creditor ID. |  [optional] |
|**creditorName** | **String** | Creditor name. |  |
|**creditorNameAndAddress** | **String** | Creditor Name and Address in a free text field. |  [optional] |
|**debtorAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  |  |
|**debtorAgent** | [**DebtorAgent7CH**](DebtorAgent7CH.md) |  |  |
|**debtorId** | **String** | Debtor Id. |  [optional] |
|**debtorName** | **String** | Debtor name. |  |
|**endToEndIdentification** | **String** |  |  |
|**equivalentAmount** | [**Amount**](Amount.md) |  |  [optional] |
|**exchangeRateInformation** | [**ExchangeRateInformation1**](ExchangeRateInformation1.md) |  |  [optional] |
|**instructedAmount** | [**Amount**](Amount.md) |  |  [optional] |
|**intermediaryAgent** | **String** | BICFI  |  [optional] |
|**purposeCode** | **PurposeCode** |  |  [optional] |
|**remittanceInformationStructured** | [**RemittanceInformationStructured**](RemittanceInformationStructured.md) |  |  [optional] |
|**remittanceInformationUnstructured** | **String** | Unstructured remittance information.  |  [optional] |
|**requestedExecutionDate** | **LocalDate** |  |  |
|**serviceLevel** | **ExternalServiceLevel1Code** |  |  [optional] |
|**transactionCurrency** | **String** | ISO 4217 Alpha 3 currency code.  |  [optional] |
|**ultimateCreditor** | **String** | Ultimate creditor. |  [optional] |
|**ultimateDebtor** | **String** | Ultimate debtor. |  [optional] |
|**dayOfExecution** | **DayOfExecution** |  |  [optional] |
|**endDate** | **LocalDate** | The last applicable day of execution. If not given, it is an infinite standing order.  |  [optional] |
|**executionRule** | **ExecutionRule** |  |  [optional] |
|**frequency** | **FrequencyCode** |  |  |
|**startDate** | **LocalDate** | The first applicable day of execution starting from this date is the first payment.  |  |
|**batchBookingPreferred** | **Boolean** | If this element equals &#39;true&#39;, the PSU prefers only one booking entry. If this element equals &#39;false&#39;, the PSU prefers individual booking of all contained individual transactions.  The ASPSP will follow this preference according to contracts agreed on with the PSU.  |  [optional] |
|**payments** | [**List&lt;PaymentInitiationBulkElementJson&gt;**](PaymentInitiationBulkElementJson.md) | A list of generic JSON bodies payment initations for bulk payments via JSON.  Note: Some fields from single payments do not occcur in a bulk payment element  |  |
|**requestedExecutionTime** | **OffsetDateTime** |  |  [optional] |



