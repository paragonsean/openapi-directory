

# PeriodicPaymentInitiationWithStatusResponse

Generic JSON response body consistion of the corresponding periodic payment initation JSON body together with an optional transaction status field. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creditorAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  |  |
|**creditorAddress** | [**Address**](Address.md) |  |  [optional] |
|**creditorAgent** | [**CreditorAgent7CH**](CreditorAgent7CH.md) |  |  [optional] |
|**creditorName** | **String** | Creditor name. |  |
|**dayOfExecution** | **DayOfExecution** |  |  [optional] |
|**debtorAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  |  |
|**endDate** | **LocalDate** | The last applicable day of execution. If not given, it is an infinite standing order.  |  [optional] |
|**endToEndIdentification** | **String** |  |  [optional] |
|**executionRule** | **ExecutionRule** |  |  [optional] |
|**frequency** | **FrequencyCode** |  |  |
|**instructedAmount** | [**Amount**](Amount.md) |  |  |
|**purposeCode** | **PurposeCode** |  |  [optional] |
|**remittanceInformationStructured** | [**RemittanceInformationStructured**](RemittanceInformationStructured.md) |  |  [optional] |
|**remittanceInformationUnstructured** | **String** | Unstructured remittance information.  |  [optional] |
|**remittanceInformationUnstructuredArray** | **List&lt;String&gt;** | Array of unstructured remittance information.  |  [optional] |
|**requestedExecutionDate** | **LocalDate** |  |  [optional] |
|**requestedExecutionTime** | **OffsetDateTime** |  |  [optional] |
|**startDate** | **LocalDate** | The first applicable day of execution starting from this date is the first payment.  |  |
|**transactionStatus** | **TransactionStatus** |  |  [optional] |
|**ultimateCreditor** | **String** | Ultimate creditor. |  [optional] |
|**ultimateDebtor** | **String** | Ultimate debtor. |  [optional] |



