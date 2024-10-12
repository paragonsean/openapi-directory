

# PaymentInitiationWithStatusResponse

Generic JSON response body consistion of the corresponding payment initation JSON body together with an optional transaction status field. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creditorAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  |  |
|**creditorAddress** | [**Address**](Address.md) |  |  [optional] |
|**creditorAgent** | [**CreditorAgent7CH**](CreditorAgent7CH.md) |  |  [optional] |
|**creditorName** | **String** | Creditor name. |  |
|**debtorAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  |  |
|**endToEndIdentification** | **String** |  |  [optional] |
|**instructedAmount** | [**Amount**](Amount.md) |  |  |
|**purposeCode** | **PurposeCode** |  |  [optional] |
|**remittanceInformationStructured** | [**RemittanceInformationStructured**](RemittanceInformationStructured.md) |  |  [optional] |
|**remittanceInformationUnstructured** | **String** | Unstructured remittance information.  |  [optional] |
|**remittanceInformationUnstructuredArray** | **List&lt;String&gt;** | Array of unstructured remittance information.  |  [optional] |
|**requestedExecutionDate** | **LocalDate** |  |  [optional] |
|**requestedExecutionTime** | **OffsetDateTime** |  |  [optional] |
|**transactionStatus** | **TransactionStatus** |  |  [optional] |
|**ultimateCreditor** | **String** | Ultimate creditor. |  [optional] |
|**ultimateDebtor** | **String** | Ultimate debtor. |  [optional] |



