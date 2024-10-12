

# Balance

A single balance element. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**balanceAmount** | [**Amount**](Amount.md) |  |  |
|**balanceType** | **BalanceType** |  |  |
|**creditLimitIncluded** | **Boolean** | A flag indicating if the credit limit of the corresponding account is included in the calculation of the balance, where applicable.  |  [optional] |
|**lastChangeDateTime** | **OffsetDateTime** | This data element might be used to indicate e.g. with the expected or booked balance that no action is known on the account, which is not yet booked.  |  [optional] |
|**lastCommittedTransaction** | **String** | \&quot;entryReference\&quot; of the last commited transaction to support the TPP in identifying whether all PSU transactions are already known.  |  [optional] |
|**referenceDate** | **LocalDate** | Indicates the date of the balance. |  [optional] |



