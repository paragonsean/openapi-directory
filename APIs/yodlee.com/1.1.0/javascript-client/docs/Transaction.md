# YodleeCoreApis.Transaction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CONTAINER** | **String** | The account&#39;s container.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] [readonly] 
**accountId** | **Number** | The account from which the transaction was made. This is basically the primary key of the account resource. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] [readonly] 
**amount** | [**Money**](Money.md) |  | [optional] 
**baseType** | **String** | Indicates if the transaction appears as a debit or a credit transaction in the account. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] [readonly] 
**category** | **String** | The name of the category assigned to the transaction. This is the category field of the transaction category resource. The supported values are provided by the GET transactions/categories.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] [readonly] 
**categoryId** | **Number** | The id of the category assigned to the transaction. This is the id field of the transaction category resource. The supported values are provided by the GET transactions/categories.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] [readonly] 
**categorySource** | **String** | Indicates the source of the category, i.e., categories derived by the system or assigned/provided by the consumer. This is the source field of the transaction category resource. The supported values are provided by the GET transactions/categories.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] [readonly] 
**categoryType** | **String** | The categoryType of the category assigned to the transaction. This is the type field of the transaction category resource. The supported values are provided by the GET transactions/categories.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] [readonly] 
**checkNumber** | **String** | The checkNumber of the transaction.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank&lt;br&gt; | [optional] [readonly] 
**commission** | [**Money**](Money.md) |  | [optional] 
**createdDate** | **String** |  | [optional] [readonly] 
**cusipNumber** | **String** | The CUSIP (Committee on Uniform Securities Identification Procedures) identifies the financial instruments in the United States and Canada.&lt;br&gt;&lt;b&gt;&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;&lt;/b&gt;: The CUSIP number field applies only to trade related transactions.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**date** | **String** | The value provided will be either postDate or transactionDate. postDate takes higher priority than transactionDate, except for the investment container as only transactionDate is available. The availability of postDate or transactionDate depends on the provider site.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] [readonly] 
**description** | [**Description**](Description.md) |  | [optional] 
**detailCategoryId** | **Number** | The id of the detail category that is assigned to the transaction. The supported values are provided by GET transactions/categories.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard&lt;br&gt; | [optional] [readonly] 
**highLevelCategoryId** | **Number** | The high level category assigned to the transaction. The supported values are provided by the GET transactions/categories. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] [readonly] 
**holdingDescription** | **String** | For transactions involving securities, this captures the securities description.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**id** | **Number** | An unique identifier for the transaction. The combination of the id and account container are unique in the system. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] [readonly] 
**interest** | [**Money**](Money.md) |  | [optional] 
**isManual** | **Boolean** | Indicates if the transaction is aggregated from the FI site or the consumer has manually created the transaction using the application or an API. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] [readonly] 
**isin** | **String** | International Securities Identification Number (ISIN) standard is used worldwide to identify specific securities.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**lastUpdated** | **String** |  | [optional] [readonly] 
**memo** | **String** | Additional notes provided by the user for a particular  transaction through application or API services. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] [readonly] 
**merchant** | [**Merchant**](Merchant.md) |  | [optional] 
**parentCategoryId** | **Number** | The parentCategoryId of the category assigned to the transaction.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: This field will be provided in the response if the transaction is assigned to a user-created category. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] [readonly] 
**postDate** | **String** | The date on which the transaction is posted to the account.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,insurance,loan&lt;br&gt; | [optional] [readonly] 
**price** | [**Money**](Money.md) |  | [optional] 
**principal** | [**Money**](Money.md) |  | [optional] 
**quantity** | **Number** | The quantity associated with the transaction.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The quantity field applies only to trade-related transactions.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**runningBalance** | [**Money**](Money.md) |  | [optional] 
**sedol** | **String** | SEDOL stands for Stock Exchange Daily Official List, a list of security identifiers used in the United Kingdom and Ireland for clearing purposes.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**settleDate** | **String** | It is the date on which the transaction is finalized, that is, the date the ownership of the security is transferred to the buyer. The settlement date is usually few days after the transaction date.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**sourceId** | **String** | A unique ID that the provider site has assigned to the transaction. The source ID is only available for the pre-populated accounts.&lt;br&gt;Pre-populated accounts are the accounts that the FI customers shares with Yodlee, so that the user does not have to add or aggregate those accounts. | [optional] [readonly] 
**sourceType** | **String** | The source through which the transaction is added to the Yodlee system.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loann&lt;br&gt;&lt;b&gt;Applicable Values:&lt;/b&gt;&lt;br&gt; | [optional] [readonly] 
**status** | **String** | The status of the transaction: pending or posted.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: Most FI sites only display posted transactions. If the FI site displays transaction status, same will be aggregated.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] [readonly] 
**subType** | **String** | The transaction subtype field provides a detailed transaction type. For example, purchase is a transaction type and the transaction subtype field indicates if the purchase was made using a debit or credit card.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The transaction subtype field is available only in the United States, Canada, United Kingdom, and India.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] [readonly] 
**symbol** | **String** | The symbol of the security being traded.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The settle date field applies only to trade-related transactions. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 
**transactionDate** | **String** | The date the transaction happens in the account. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; | [optional] [readonly] 
**type** | **String** | The nature of the transaction, i.e., deposit, refund, payment, etc.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The transaction type field is available only for the United States, Canada, United Kingdom, and India based provider sites. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment&lt;br&gt; | [optional] [readonly] 
**valoren** | **String** | It is an identification number that is assigned to financial instruments such as stocks and bonds trading in Switzerland.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; | [optional] [readonly] 



## Enum: CONTAINEREnum


* `bank` (value: `"bank"`)

* `creditCard` (value: `"creditCard"`)

* `investment` (value: `"investment"`)

* `insurance` (value: `"insurance"`)

* `loan` (value: `"loan"`)

* `reward` (value: `"reward"`)

* `realEstate` (value: `"realEstate"`)

* `otherAssets` (value: `"otherAssets"`)

* `otherLiabilities` (value: `"otherLiabilities"`)





## Enum: BaseTypeEnum


* `CREDIT` (value: `"CREDIT"`)

* `DEBIT` (value: `"DEBIT"`)





## Enum: CategorySourceEnum


* `SYSTEM` (value: `"SYSTEM"`)

* `USER` (value: `"USER"`)





## Enum: CategoryTypeEnum


* `TRANSFER` (value: `"TRANSFER"`)

* `DEFERRED_COMPENSATION` (value: `"DEFERRED_COMPENSATION"`)

* `UNCATEGORIZE` (value: `"UNCATEGORIZE"`)

* `INCOME` (value: `"INCOME"`)

* `EXPENSE` (value: `"EXPENSE"`)





## Enum: SourceTypeEnum


* `AGGREGATED` (value: `"AGGREGATED"`)

* `MANUAL` (value: `"MANUAL"`)





## Enum: StatusEnum


* `POSTED` (value: `"POSTED"`)

* `PENDING` (value: `"PENDING"`)

* `SCHEDULED` (value: `"SCHEDULED"`)

* `FAILED` (value: `"FAILED"`)

* `CLEARED` (value: `"CLEARED"`)





## Enum: SubTypeEnum


* `AUTH_HOLD` (value: `"AUTH_HOLD"`)

* `AUTH_REQUEST` (value: `"AUTH_REQUEST"`)

* `OVERDRAFT_CHARGE` (value: `"OVERDRAFT_CHARGE"`)

* `CREDIT_ADJUSTMENT` (value: `"CREDIT_ADJUSTMENT"`)

* `PIN_DEBIT` (value: `"PIN_DEBIT"`)

* `BANK_DIRECT_DEPOSIT` (value: `"BANK_DIRECT_DEPOSIT"`)

* `DIVIDEND_DEPOSIT` (value: `"DIVIDEND_DEPOSIT"`)

* `INTEREST_SAVINGS` (value: `"INTEREST_SAVINGS"`)

* `INTEREST_ADJUSTMENT` (value: `"INTEREST_ADJUSTMENT"`)

* `ONLINE_PURCHASE` (value: `"ONLINE_PURCHASE"`)

* `PURCHASED_WITH_CHECK` (value: `"PURCHASED_WITH_CHECK"`)

* `RECURRING_BILLING` (value: `"RECURRING_BILLING"`)

* `TAX_PAYMENT` (value: `"TAX_PAYMENT"`)

* `PAYMENT_BY_CHECK` (value: `"PAYMENT_BY_CHECK"`)

* `PAYMENT_PLAN` (value: `"PAYMENT_PLAN"`)

* `FEE_REFUND` (value: `"FEE_REFUND"`)

* `WIRE_TRANSFER_CHARGE` (value: `"WIRE_TRANSFER_CHARGE"`)

* `ACCOUNT_TO_ACCOUNT_TRANSFER` (value: `"ACCOUNT_TO_ACCOUNT_TRANSFER"`)

* `BANK_TO_BANK_TRANSACTION` (value: `"BANK_TO_BANK_TRANSACTION"`)

* `BANK_TO_NON_BANK_ACCOUNT_TRANSFER` (value: `"BANK_TO_NON_BANK_ACCOUNT_TRANSFER"`)

* `CASH_WITHDRAWAL_AT_FI` (value: `"CASH_WITHDRAWAL_AT_FI"`)

* `ATM_CASH_WITHDRAWAL` (value: `"ATM_CASH_WITHDRAWAL"`)

* `AUTH_PROCESSING` (value: `"AUTH_PROCESSING"`)

* `AUTH_RELEASE` (value: `"AUTH_RELEASE"`)

* `PRE_AUTH` (value: `"PRE_AUTH"`)

* `AUTH_COMPLETE` (value: `"AUTH_COMPLETE"`)

* `AUTH_VOID` (value: `"AUTH_VOID"`)

* `BALANCE_ENQUIRY` (value: `"BALANCE_ENQUIRY"`)

* `ACCOUNT_VERIFICATION` (value: `"ACCOUNT_VERIFICATION"`)

* `PRE_AUTH_COMPLETION` (value: `"PRE_AUTH_COMPLETION"`)

* `SERVICE_CHARGE` (value: `"SERVICE_CHARGE"`)

* `SERVICE_CHARGE_FEE_REFUND` (value: `"SERVICE_CHARGE_FEE_REFUND"`)

* `RETURNED_CHECK_CHARGE` (value: `"RETURNED_CHECK_CHARGE"`)

* `RETURNED_CHECK_REIMBURSEMENT` (value: `"RETURNED_CHECK_REIMBURSEMENT"`)

* `CASH_ADVANCE` (value: `"CASH_ADVANCE"`)

* `BILL_PAY_CHARGE` (value: `"BILL_PAY_CHARGE"`)

* `CHECK_IMAGE_SERVICE_CHARGE` (value: `"CHECK_IMAGE_SERVICE_CHARGE"`)

* `OVERDRAFT_PROTECTION_CHARGE` (value: `"OVERDRAFT_PROTECTION_CHARGE"`)

* `STOP_PAYMENT_CHARGE` (value: `"STOP_PAYMENT_CHARGE"`)

* `CHECKS_ORDERING_CHARGE` (value: `"CHECKS_ORDERING_CHARGE"`)

* `MONTHLY_MAINTENANCE_CHARGE` (value: `"MONTHLY_MAINTENANCE_CHARGE"`)

* `DEBIT_CARD_FEE` (value: `"DEBIT_CARD_FEE"`)

* `CONVENIENCE_FEE` (value: `"CONVENIENCE_FEE"`)

* `PERSONAL_LOAN_CREDIT` (value: `"PERSONAL_LOAN_CREDIT"`)

* `CREDIT_CARD_CREDIT` (value: `"CREDIT_CARD_CREDIT"`)

* `AUTO_LOAN` (value: `"AUTO_LOAN"`)

* `HOME_LOAN_MORTGAGE` (value: `"HOME_LOAN_MORTGAGE"`)

* `SHORT_TERM_CREDIT` (value: `"SHORT_TERM_CREDIT"`)

* `SIGNATURE_DEBIT` (value: `"SIGNATURE_DEBIT"`)

* `CONTACT_LESS_DEBIT` (value: `"CONTACT_LESS_DEBIT"`)

* `DEFERRED_DEPOSIT` (value: `"DEFERRED_DEPOSIT"`)

* `DEFERRED_BILL_PAY` (value: `"DEFERRED_BILL_PAY"`)

* `INSTALLMENT_PAYMENT` (value: `"INSTALLMENT_PAYMENT"`)

* `RECURRING_SUBSCRIPTION_PAYMENT` (value: `"RECURRING_SUBSCRIPTION_PAYMENT"`)

* `HOLD_CHECK_PAYMENT` (value: `"HOLD_CHECK_PAYMENT"`)

* `CAPITAL_GAINS_DISTIBUTION` (value: `"CAPITAL_GAINS_DISTIBUTION"`)

* `CG_LONG_TERM_DEPOSIT` (value: `"CG_LONG_TERM_DEPOSIT"`)

* `OPEN_SALE_DEPOSIT` (value: `"OPEN_SALE_DEPOSIT"`)

* `INTEREST__CHECK` (value: `"INTEREST__CHECK"`)

* `PURCHASE_VOID` (value: `"PURCHASE_VOID"`)

* `PURCHASE_WITH_CREDIT_CARD` (value: `"PURCHASE_WITH_CREDIT_CARD"`)

* `PURCHASE_WITH_DEBIT_CARD` (value: `"PURCHASE_WITH_DEBIT_CARD"`)

* `CHARGE_A_REPEAT_CUSTOMER` (value: `"CHARGE_A_REPEAT_CUSTOMER"`)

* `DOWN_PAYMENT_OR_ANNUITY_PAYMENT_OR_DIRECT_PAYMENT` (value: `"DOWN_PAYMENT_OR_ANNUITY_PAYMENT_OR_DIRECT_PAYMENT"`)

* `FEE_PAYMENT` (value: `"FEE_PAYMENT"`)

* `FINANCE_CHARGE_REFUND` (value: `"FINANCE_CHARGE_REFUND"`)

* `TRANSACTION_VOID` (value: `"TRANSACTION_VOID"`)

* `FEE_VOID` (value: `"FEE_VOID"`)

* `DEBIT_CARD_WITHDRAWAL_AT_STORE` (value: `"DEBIT_CARD_WITHDRAWAL_AT_STORE"`)

* `ELECTRONIC_PAYMENT` (value: `"ELECTRONIC_PAYMENT"`)

* `ACH_DEBIT` (value: `"ACH_DEBIT"`)

* `ATM_TELLER_DEPOSIT` (value: `"ATM_TELLER_DEPOSIT"`)

* `POS_DEBIT` (value: `"POS_DEBIT"`)

* `BANK_ADJUSTMENT` (value: `"BANK_ADJUSTMENT"`)

* `CHARGES_FEES` (value: `"CHARGES_FEES"`)

* `INTEREST` (value: `"INTEREST"`)

* `DEPOSITS_CREDITS` (value: `"DEPOSITS_CREDITS"`)

* `PAYMENT` (value: `"PAYMENT"`)

* `PURCHASE` (value: `"PURCHASE"`)

* `REFUND` (value: `"REFUND"`)

* `TRANSFER` (value: `"TRANSFER"`)

* `WITHDRAWAL` (value: `"WITHDRAWAL"`)

* `OTHER_DEPOSITS` (value: `"OTHER_DEPOSITS"`)

* `OTHER_WITHDRAWALS` (value: `"OTHER_WITHDRAWALS"`)

* `ADJUSTMENT` (value: `"ADJUSTMENT"`)

* `FINANCE_CHARGE` (value: `"FINANCE_CHARGE"`)

* `OTHER_CHARGES_FEES` (value: `"OTHER_CHARGES_FEES"`)

* `ANNUAL_FEE` (value: `"ANNUAL_FEE"`)

* `DEPOSIT` (value: `"DEPOSIT"`)

* `DIRECT_DEPOSIT_SALARY` (value: `"DIRECT_DEPOSIT_SALARY"`)

* `INVESTMENT_INCOME_CASH` (value: `"INVESTMENT_INCOME_CASH"`)

* `SSA` (value: `"SSA"`)

* `REWARDS` (value: `"REWARDS"`)

* `CHECK_DEPOSIT` (value: `"CHECK_DEPOSIT"`)

* `MOBILE_REMOTE_DEPOSIT` (value: `"MOBILE_REMOTE_DEPOSIT"`)

* `TELLER_DEPOSIT` (value: `"TELLER_DEPOSIT"`)

* `TAX_REFUND` (value: `"TAX_REFUND"`)

* `CREDIT_CARD_PAYMENT` (value: `"CREDIT_CARD_PAYMENT"`)

* `INSURANCE_PAYMENT` (value: `"INSURANCE_PAYMENT"`)

* `UTILITIES_PAYMENT` (value: `"UTILITIES_PAYMENT"`)

* `CHILD_SUPPORT` (value: `"CHILD_SUPPORT"`)

* `LOAN` (value: `"LOAN"`)

* `PERSONAL_LOAN` (value: `"PERSONAL_LOAN"`)

* `STUDENT_LOAN` (value: `"STUDENT_LOAN"`)

* `SALES_TAX` (value: `"SALES_TAX"`)

* `REIMBURSEMENT` (value: `"REIMBURSEMENT"`)

* `BALANCE_TRANSFER` (value: `"BALANCE_TRANSFER"`)

* `WIRE_TRANSFER` (value: `"WIRE_TRANSFER"`)

* `OVERDRAFT_PROTECTION` (value: `"OVERDRAFT_PROTECTION"`)

* `DEBIT` (value: `"DEBIT"`)

* `CREDIT` (value: `"CREDIT"`)

* `NSF_FEES` (value: `"NSF_FEES"`)




