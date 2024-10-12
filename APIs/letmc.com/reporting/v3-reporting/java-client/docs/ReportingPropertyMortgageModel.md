

# ReportingPropertyMortgageModel

Represents an receivership case.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Double** | Amount. |  [optional] |
|**borrowersAccountName** | **String** | Borrowers Account Name |  [optional] |
|**createdAt** | **OffsetDateTime** | The created at date. |  [optional] |
|**displayType** | **String** | Friendly type name. |  [optional] [readonly] |
|**extraNotes** | **String** | Extra notes. |  [optional] |
|**from** | **OffsetDateTime** | The from date. |  [optional] |
|**intrestRate** | **Double** | The mortgages intrest rate. |  [optional] |
|**marketValue** | **Double** | The property market value. |  [optional] |
|**monthlyPayment** | **Double** | The mortgages monthly payment. |  [optional] |
|**mortgageAccountNumber** | **String** | Mortgage account number. |  [optional] |
|**mortgageProvider** | **String** | Mortgages provider. |  [optional] |
|**propertyOwnableID** | **String** | The unique Property Ownable identifier. |  [optional] |
|**salesInstructionID** | **String** | The unique Sales Instruction identifier. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The mortgages type. |  [optional] |
|**valuationDate** | **OffsetDateTime** | The mortgages valuation date. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INTEREST_ONLY_FIXED_RATE | &quot;InterestOnlyFixedRate&quot; |
| INTEREST_ONLY_SVR | &quot;InterestOnlySVR&quot; |
| INTEREST_ONLY_DISCOUNT_MORTGAGE | &quot;InterestOnlyDiscountMortgage&quot; |
| INTEREST_ONLY_TRACKER | &quot;InterestOnlyTracker&quot; |
| INTEREST_ONLY_CAPPED | &quot;InterestOnlyCapped&quot; |
| INTEREST_ONLY_OFFSET | &quot;InterestOnlyOffset&quot; |
| CAPITAL_REPAYMENT_FIXED_RATE | &quot;CapitalRepaymentFixedRate&quot; |
| CAPITAL_REPAYMENT_SVR | &quot;CapitalRepaymentSVR&quot; |
| CAPITAL_REPAYMENT_DISCOUNT_MORTGAGE | &quot;CapitalRepaymentDiscountMortgage&quot; |
| CAPITAL_REPAYMENT_TRACKER | &quot;CapitalRepaymentTracker&quot; |
| CAPITAL_REPAYMENT_CAPPED | &quot;CapitalRepaymentCapped&quot; |
| CAPITAL_REPAYMENT_OFFSET | &quot;CapitalRepaymentOffset&quot; |



