

# Transaction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**CONTAINER** | [**CONTAINEREnum**](#CONTAINEREnum) | The account&#39;s container.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; |  [optional] [readonly] |
|**accountId** | **Long** | The account from which the transaction was made. This is basically the primary key of the account resource. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; |  [optional] [readonly] |
|**amount** | [**Money**](Money.md) |  |  [optional] |
|**baseType** | [**BaseTypeEnum**](#BaseTypeEnum) | Indicates if the transaction appears as a debit or a credit transaction in the account. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; |  [optional] [readonly] |
|**category** | **String** | The name of the category assigned to the transaction. This is the category field of the transaction category resource. The supported values are provided by the GET transactions/categories.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; |  [optional] [readonly] |
|**categoryId** | **Long** | The id of the category assigned to the transaction. This is the id field of the transaction category resource. The supported values are provided by the GET transactions/categories.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; |  [optional] [readonly] |
|**categorySource** | [**CategorySourceEnum**](#CategorySourceEnum) | Indicates the source of the category, i.e., categories derived by the system or assigned/provided by the consumer. This is the source field of the transaction category resource. The supported values are provided by the GET transactions/categories.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; |  [optional] [readonly] |
|**categoryType** | [**CategoryTypeEnum**](#CategoryTypeEnum) | The categoryType of the category assigned to the transaction. This is the type field of the transaction category resource. The supported values are provided by the GET transactions/categories.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; |  [optional] [readonly] |
|**checkNumber** | **String** | The checkNumber of the transaction.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank&lt;br&gt; |  [optional] [readonly] |
|**commission** | [**Money**](Money.md) |  |  [optional] |
|**createdDate** | **String** |  |  [optional] [readonly] |
|**cusipNumber** | **String** | The CUSIP (Committee on Uniform Securities Identification Procedures) identifies the financial instruments in the United States and Canada.&lt;br&gt;&lt;b&gt;&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;&lt;/b&gt;: The CUSIP number field applies only to trade related transactions.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; |  [optional] [readonly] |
|**date** | **String** | The value provided will be either postDate or transactionDate. postDate takes higher priority than transactionDate, except for the investment container as only transactionDate is available. The availability of postDate or transactionDate depends on the provider site.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; |  [optional] [readonly] |
|**description** | [**Description**](Description.md) |  |  [optional] |
|**detailCategoryId** | **Long** | The id of the detail category that is assigned to the transaction. The supported values are provided by GET transactions/categories.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard&lt;br&gt; |  [optional] [readonly] |
|**highLevelCategoryId** | **Long** | The high level category assigned to the transaction. The supported values are provided by the GET transactions/categories. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; |  [optional] [readonly] |
|**holdingDescription** | **String** | For transactions involving securities, this captures the securities description.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; |  [optional] [readonly] |
|**id** | **Long** | An unique identifier for the transaction. The combination of the id and account container are unique in the system. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; |  [optional] [readonly] |
|**interest** | [**Money**](Money.md) |  |  [optional] |
|**isManual** | **Boolean** | Indicates if the transaction is aggregated from the FI site or the consumer has manually created the transaction using the application or an API. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; |  [optional] [readonly] |
|**isin** | **String** | International Securities Identification Number (ISIN) standard is used worldwide to identify specific securities.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; |  [optional] [readonly] |
|**lastUpdated** | **String** |  |  [optional] [readonly] |
|**memo** | **String** | Additional notes provided by the user for a particular  transaction through application or API services. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; |  [optional] [readonly] |
|**merchant** | [**Merchant**](Merchant.md) |  |  [optional] |
|**parentCategoryId** | **Long** | The parentCategoryId of the category assigned to the transaction.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: This field will be provided in the response if the transaction is assigned to a user-created category. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; |  [optional] [readonly] |
|**postDate** | **String** | The date on which the transaction is posted to the account.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,insurance,loan&lt;br&gt; |  [optional] [readonly] |
|**price** | [**Money**](Money.md) |  |  [optional] |
|**principal** | [**Money**](Money.md) |  |  [optional] |
|**quantity** | **Double** | The quantity associated with the transaction.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The quantity field applies only to trade-related transactions.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; |  [optional] [readonly] |
|**runningBalance** | [**Money**](Money.md) |  |  [optional] |
|**sedol** | **String** | SEDOL stands for Stock Exchange Daily Official List, a list of security identifiers used in the United Kingdom and Ireland for clearing purposes.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; |  [optional] [readonly] |
|**settleDate** | **String** | It is the date on which the transaction is finalized, that is, the date the ownership of the security is transferred to the buyer. The settlement date is usually few days after the transaction date.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; |  [optional] [readonly] |
|**sourceId** | **String** | A unique ID that the provider site has assigned to the transaction. The source ID is only available for the pre-populated accounts.&lt;br&gt;Pre-populated accounts are the accounts that the FI customers shares with Yodlee, so that the user does not have to add or aggregate those accounts. |  [optional] [readonly] |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | The source through which the transaction is added to the Yodlee system.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loann&lt;br&gt;&lt;b&gt;Applicable Values:&lt;/b&gt;&lt;br&gt; |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the transaction: pending or posted.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: Most FI sites only display posted transactions. If the FI site displays transaction status, same will be aggregated.  &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; |  [optional] [readonly] |
|**subType** | [**SubTypeEnum**](#SubTypeEnum) | The transaction subtype field provides a detailed transaction type. For example, purchase is a transaction type and the transaction subtype field indicates if the purchase was made using a debit or credit card.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The transaction subtype field is available only in the United States, Canada, United Kingdom, and India.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; |  [optional] [readonly] |
|**symbol** | **String** | The symbol of the security being traded.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The settle date field applies only to trade-related transactions. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; |  [optional] [readonly] |
|**transactionDate** | **String** | The date the transaction happens in the account. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment,insurance,loan&lt;br&gt; |  [optional] [readonly] |
|**type** | **String** | The nature of the transaction, i.e., deposit, refund, payment, etc.&lt;br&gt;&lt;b&gt;Note&lt;/b&gt;: The transaction type field is available only for the United States, Canada, United Kingdom, and India based provider sites. &lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: bank,creditCard,investment&lt;br&gt; |  [optional] [readonly] |
|**valoren** | **String** | It is an identification number that is assigned to financial instruments such as stocks and bonds trading in Switzerland.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: investment&lt;br&gt; |  [optional] [readonly] |



## Enum: CONTAINEREnum

| Name | Value |
|---- | -----|
| BANK | &quot;bank&quot; |
| CREDIT_CARD | &quot;creditCard&quot; |
| INVESTMENT | &quot;investment&quot; |
| INSURANCE | &quot;insurance&quot; |
| LOAN | &quot;loan&quot; |
| REWARD | &quot;reward&quot; |
| REAL_ESTATE | &quot;realEstate&quot; |
| OTHER_ASSETS | &quot;otherAssets&quot; |
| OTHER_LIABILITIES | &quot;otherLiabilities&quot; |



## Enum: BaseTypeEnum

| Name | Value |
|---- | -----|
| CREDIT | &quot;CREDIT&quot; |
| DEBIT | &quot;DEBIT&quot; |



## Enum: CategorySourceEnum

| Name | Value |
|---- | -----|
| SYSTEM | &quot;SYSTEM&quot; |
| USER | &quot;USER&quot; |



## Enum: CategoryTypeEnum

| Name | Value |
|---- | -----|
| TRANSFER | &quot;TRANSFER&quot; |
| DEFERRED_COMPENSATION | &quot;DEFERRED_COMPENSATION&quot; |
| UNCATEGORIZE | &quot;UNCATEGORIZE&quot; |
| INCOME | &quot;INCOME&quot; |
| EXPENSE | &quot;EXPENSE&quot; |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| AGGREGATED | &quot;AGGREGATED&quot; |
| MANUAL | &quot;MANUAL&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| POSTED | &quot;POSTED&quot; |
| PENDING | &quot;PENDING&quot; |
| SCHEDULED | &quot;SCHEDULED&quot; |
| FAILED | &quot;FAILED&quot; |
| CLEARED | &quot;CLEARED&quot; |



## Enum: SubTypeEnum

| Name | Value |
|---- | -----|
| AUTH_HOLD | &quot;AUTH_HOLD&quot; |
| AUTH_REQUEST | &quot;AUTH_REQUEST&quot; |
| OVERDRAFT_CHARGE | &quot;OVERDRAFT_CHARGE&quot; |
| CREDIT_ADJUSTMENT | &quot;CREDIT_ADJUSTMENT&quot; |
| PIN_DEBIT | &quot;PIN_DEBIT&quot; |
| BANK_DIRECT_DEPOSIT | &quot;BANK_DIRECT_DEPOSIT&quot; |
| DIVIDEND_DEPOSIT | &quot;DIVIDEND_DEPOSIT&quot; |
| INTEREST_SAVINGS | &quot;INTEREST_SAVINGS&quot; |
| INTEREST_ADJUSTMENT | &quot;INTEREST_ADJUSTMENT&quot; |
| ONLINE_PURCHASE | &quot;ONLINE_PURCHASE&quot; |
| PURCHASED_WITH_CHECK | &quot;PURCHASED_WITH_CHECK&quot; |
| RECURRING_BILLING | &quot;RECURRING_BILLING&quot; |
| TAX_PAYMENT | &quot;TAX_PAYMENT&quot; |
| PAYMENT_BY_CHECK | &quot;PAYMENT_BY_CHECK&quot; |
| PAYMENT_PLAN | &quot;PAYMENT_PLAN&quot; |
| FEE_REFUND | &quot;FEE_REFUND&quot; |
| WIRE_TRANSFER_CHARGE | &quot;WIRE_TRANSFER_CHARGE&quot; |
| ACCOUNT_TO_ACCOUNT_TRANSFER | &quot;ACCOUNT_TO_ACCOUNT_TRANSFER&quot; |
| BANK_TO_BANK_TRANSACTION | &quot;BANK_TO_BANK_TRANSACTION&quot; |
| BANK_TO_NON_BANK_ACCOUNT_TRANSFER | &quot;BANK_TO_NON_BANK_ACCOUNT_TRANSFER&quot; |
| CASH_WITHDRAWAL_AT_FI | &quot;CASH_WITHDRAWAL_AT_FI&quot; |
| ATM_CASH_WITHDRAWAL | &quot;ATM_CASH_WITHDRAWAL&quot; |
| AUTH_PROCESSING | &quot;AUTH_PROCESSING&quot; |
| AUTH_RELEASE | &quot;AUTH_RELEASE&quot; |
| PRE_AUTH | &quot;PRE_AUTH&quot; |
| AUTH_COMPLETE | &quot;AUTH_COMPLETE&quot; |
| AUTH_VOID | &quot;AUTH_VOID&quot; |
| BALANCE_ENQUIRY | &quot;BALANCE_ENQUIRY&quot; |
| ACCOUNT_VERIFICATION | &quot;ACCOUNT_VERIFICATION&quot; |
| PRE_AUTH_COMPLETION | &quot;PRE_AUTH_COMPLETION&quot; |
| SERVICE_CHARGE | &quot;SERVICE_CHARGE&quot; |
| SERVICE_CHARGE_FEE_REFUND | &quot;SERVICE_CHARGE_FEE_REFUND&quot; |
| RETURNED_CHECK_CHARGE | &quot;RETURNED_CHECK_CHARGE&quot; |
| RETURNED_CHECK_REIMBURSEMENT | &quot;RETURNED_CHECK_REIMBURSEMENT&quot; |
| CASH_ADVANCE | &quot;CASH_ADVANCE&quot; |
| BILL_PAY_CHARGE | &quot;BILL_PAY_CHARGE&quot; |
| CHECK_IMAGE_SERVICE_CHARGE | &quot;CHECK_IMAGE_SERVICE_CHARGE&quot; |
| OVERDRAFT_PROTECTION_CHARGE | &quot;OVERDRAFT_PROTECTION_CHARGE&quot; |
| STOP_PAYMENT_CHARGE | &quot;STOP_PAYMENT_CHARGE&quot; |
| CHECKS_ORDERING_CHARGE | &quot;CHECKS_ORDERING_CHARGE&quot; |
| MONTHLY_MAINTENANCE_CHARGE | &quot;MONTHLY_MAINTENANCE_CHARGE&quot; |
| DEBIT_CARD_FEE | &quot;DEBIT_CARD_FEE&quot; |
| CONVENIENCE_FEE | &quot;CONVENIENCE_FEE&quot; |
| PERSONAL_LOAN_CREDIT | &quot;PERSONAL_LOAN_CREDIT&quot; |
| CREDIT_CARD_CREDIT | &quot;CREDIT_CARD_CREDIT&quot; |
| AUTO_LOAN | &quot;AUTO_LOAN&quot; |
| HOME_LOAN_MORTGAGE | &quot;HOME_LOAN_MORTGAGE&quot; |
| SHORT_TERM_CREDIT | &quot;SHORT_TERM_CREDIT&quot; |
| SIGNATURE_DEBIT | &quot;SIGNATURE_DEBIT&quot; |
| CONTACT_LESS_DEBIT | &quot;CONTACT_LESS_DEBIT&quot; |
| DEFERRED_DEPOSIT | &quot;DEFERRED_DEPOSIT&quot; |
| DEFERRED_BILL_PAY | &quot;DEFERRED_BILL_PAY&quot; |
| INSTALLMENT_PAYMENT | &quot;INSTALLMENT_PAYMENT&quot; |
| RECURRING_SUBSCRIPTION_PAYMENT | &quot;RECURRING_SUBSCRIPTION_PAYMENT&quot; |
| HOLD_CHECK_PAYMENT | &quot;HOLD_CHECK_PAYMENT&quot; |
| CAPITAL_GAINS_DISTIBUTION | &quot;CAPITAL_GAINS_DISTIBUTION&quot; |
| CG_LONG_TERM_DEPOSIT | &quot;CG_LONG_TERM_DEPOSIT&quot; |
| OPEN_SALE_DEPOSIT | &quot;OPEN_SALE_DEPOSIT&quot; |
| INTEREST__CHECK | &quot;INTEREST__CHECK&quot; |
| PURCHASE_VOID | &quot;PURCHASE_VOID&quot; |
| PURCHASE_WITH_CREDIT_CARD | &quot;PURCHASE_WITH_CREDIT_CARD&quot; |
| PURCHASE_WITH_DEBIT_CARD | &quot;PURCHASE_WITH_DEBIT_CARD&quot; |
| CHARGE_A_REPEAT_CUSTOMER | &quot;CHARGE_A_REPEAT_CUSTOMER&quot; |
| DOWN_PAYMENT_OR_ANNUITY_PAYMENT_OR_DIRECT_PAYMENT | &quot;DOWN_PAYMENT_OR_ANNUITY_PAYMENT_OR_DIRECT_PAYMENT&quot; |
| FEE_PAYMENT | &quot;FEE_PAYMENT&quot; |
| FINANCE_CHARGE_REFUND | &quot;FINANCE_CHARGE_REFUND&quot; |
| TRANSACTION_VOID | &quot;TRANSACTION_VOID&quot; |
| FEE_VOID | &quot;FEE_VOID&quot; |
| DEBIT_CARD_WITHDRAWAL_AT_STORE | &quot;DEBIT_CARD_WITHDRAWAL_AT_STORE&quot; |
| ELECTRONIC_PAYMENT | &quot;ELECTRONIC_PAYMENT&quot; |
| ACH_DEBIT | &quot;ACH_DEBIT&quot; |
| ATM_TELLER_DEPOSIT | &quot;ATM_TELLER_DEPOSIT&quot; |
| POS_DEBIT | &quot;POS_DEBIT&quot; |
| BANK_ADJUSTMENT | &quot;BANK_ADJUSTMENT&quot; |
| CHARGES_FEES | &quot;CHARGES_FEES&quot; |
| INTEREST | &quot;INTEREST&quot; |
| DEPOSITS_CREDITS | &quot;DEPOSITS_CREDITS&quot; |
| PAYMENT | &quot;PAYMENT&quot; |
| PURCHASE | &quot;PURCHASE&quot; |
| REFUND | &quot;REFUND&quot; |
| TRANSFER | &quot;TRANSFER&quot; |
| WITHDRAWAL | &quot;WITHDRAWAL&quot; |
| OTHER_DEPOSITS | &quot;OTHER_DEPOSITS&quot; |
| OTHER_WITHDRAWALS | &quot;OTHER_WITHDRAWALS&quot; |
| ADJUSTMENT | &quot;ADJUSTMENT&quot; |
| FINANCE_CHARGE | &quot;FINANCE_CHARGE&quot; |
| OTHER_CHARGES_FEES | &quot;OTHER_CHARGES_FEES&quot; |
| ANNUAL_FEE | &quot;ANNUAL_FEE&quot; |
| DEPOSIT | &quot;DEPOSIT&quot; |
| DIRECT_DEPOSIT_SALARY | &quot;DIRECT_DEPOSIT_SALARY&quot; |
| INVESTMENT_INCOME_CASH | &quot;INVESTMENT_INCOME_CASH&quot; |
| SSA | &quot;SSA&quot; |
| REWARDS | &quot;REWARDS&quot; |
| CHECK_DEPOSIT | &quot;CHECK_DEPOSIT&quot; |
| MOBILE_REMOTE_DEPOSIT | &quot;MOBILE_REMOTE_DEPOSIT&quot; |
| TELLER_DEPOSIT | &quot;TELLER_DEPOSIT&quot; |
| TAX_REFUND | &quot;TAX_REFUND&quot; |
| CREDIT_CARD_PAYMENT | &quot;CREDIT_CARD_PAYMENT&quot; |
| INSURANCE_PAYMENT | &quot;INSURANCE_PAYMENT&quot; |
| UTILITIES_PAYMENT | &quot;UTILITIES_PAYMENT&quot; |
| CHILD_SUPPORT | &quot;CHILD_SUPPORT&quot; |
| LOAN | &quot;LOAN&quot; |
| PERSONAL_LOAN | &quot;PERSONAL_LOAN&quot; |
| STUDENT_LOAN | &quot;STUDENT_LOAN&quot; |
| SALES_TAX | &quot;SALES_TAX&quot; |
| REIMBURSEMENT | &quot;REIMBURSEMENT&quot; |
| BALANCE_TRANSFER | &quot;BALANCE_TRANSFER&quot; |
| WIRE_TRANSFER | &quot;WIRE_TRANSFER&quot; |
| OVERDRAFT_PROTECTION | &quot;OVERDRAFT_PROTECTION&quot; |
| DEBIT | &quot;DEBIT&quot; |
| CREDIT | &quot;CREDIT&quot; |
| NSF_FEES | &quot;NSF_FEES&quot; |



