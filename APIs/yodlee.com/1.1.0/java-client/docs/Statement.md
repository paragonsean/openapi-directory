

# Statement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **Long** | Account to which the statement belongs to.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard,  loan, insurance&lt;br&gt; |  [optional] [readonly] |
|**amountDue** | [**Money**](Money.md) |  |  [optional] |
|**apr** | **Double** | The APR applied to the balance on the credit card account, as available in the statement.&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; In case of variable APR, the APR available on the statement might differ from the APR available at the account-level.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard,  loan, insurance&lt;br&gt; |  [optional] [readonly] |
|**billingPeriodEnd** | **String** | The end date of the statement period.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard,  loan, insurance&lt;br&gt; |  [optional] [readonly] |
|**billingPeriodStart** | **String** | The start date of the statement period.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard,  loan, insurance&lt;br&gt; |  [optional] [readonly] |
|**cashAdvance** | [**Money**](Money.md) |  |  [optional] |
|**cashApr** | **Double** | The APR applicable to cash withdrawals on the credit card account.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard,  loan, insurance&lt;br&gt; |  [optional] [readonly] |
|**dueDate** | **String** | The date by when the minimum payment is due to be paid.&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; The due date that appears in the statement may differ from the due date at the account-level.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard,  loan, insurance&lt;br&gt; |  [optional] [readonly] |
|**id** | **Long** | Unique identifier for the statement.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard,  loan, insurance&lt;br&gt; |  [optional] [readonly] |
|**interestAmount** | [**Money**](Money.md) |  |  [optional] |
|**isLatest** | **Boolean** | The field is set to true if the statement is the latest generated statement.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard,  loan, insurance&lt;br&gt; |  [optional] [readonly] |
|**lastPaymentAmount** | [**Money**](Money.md) |  |  [optional] |
|**lastPaymentDate** | **String** | The date on which the last payment was done during the billing cycle.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard,  loan, insurance&lt;br&gt; |  [optional] [readonly] |
|**lastUpdated** | **String** | The date when the account was last updated by Yodlee.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard,  loan, insurance&lt;br&gt; |  [optional] [readonly] |
|**loanBalance** | [**Money**](Money.md) |  |  [optional] |
|**minimumPayment** | [**Money**](Money.md) |  |  [optional] |
|**newCharges** | [**Money**](Money.md) |  |  [optional] |
|**principalAmount** | [**Money**](Money.md) |  |  [optional] |
|**statementDate** | **String** | The date on which the statement is generated.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard,  loan, insurance&lt;br&gt; |  [optional] [readonly] |



