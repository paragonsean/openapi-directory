

# UpdateExpense


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Double** | Expense Amount (Required). Must be &amp;gt;&#x3D; 0 |  [optional] |
|**currencyCode** | **String** | A 3-letter ISO CurrencyCode for the expense currency. (e.g. USD). If not provided, defaults to the Account base currency. |  [optional] |
|**customerIDFK** | **Integer** | The Avaza Customer ID to associate the Expense with. |  [optional] |
|**exchangeRate** | **Double** | Optional (Only relevant if the expense currency is different to your account currency. If not provided we will look up the market exchange rate for you based on the expense date.) Exchange Rate &#x3D; Expense Currency Amount / Base Currency Amount (e.g. if Expense currency is in AUD, and Base Currency is in USD, Exchange Rate &#x3D; AUD $140 / USD $100 &#x3D; 1.4) |  [optional] |
|**expenseCategoryIDFK** | **Integer** | The expense category to link the Expense to. |  [optional] |
|**expenseDate** | **OffsetDateTime** | The date of the expense entry |  [optional] |
|**expenseID** | **Long** |  |  |
|**expensePaymentMethodIDFK** | **Integer** | (Optional) ID of Expense Payment Method. |  [optional] |
|**fieldsToUpdate** | **List&lt;String&gt;** |  |  |
|**fileAttachmentIDs** | **List&lt;Long&gt;** | Array of File Attachment IDs to associate with this expense. The files need to have already been uploaded. Currently only accepts a single file. |  [optional] |
|**groupTripName** | **String** | Links the expense to a Grouping/Trip report. If no matching name found, creates a new Group/Trip Report name. |  [optional] |
|**merchant** | **String** | The name of the merchant. |  [optional] |
|**merchantTaxNumber** | **String** | A Tax number identifier for the merchant. |  [optional] |
|**notes** | **String** | Expense Notes |  [optional] |
|**projectIDFK** | **Integer** | The Avaza project ID to associate the Expense with. |  [optional] |
|**quantity** | **Double** | Conditional - available for expenses that are assigned a unit priced based expense category. e.g Mileage |  [optional] |
|**taskIDFK** | **Integer** | (optional) TaskID of a Task to link the new Expense to. A Customer and Project must be provided also. |  [optional] |
|**taxIDFK** | **Integer** | Avaza Tax ID the expense belongs to. |  [optional] |
|**transactionTaxConfigCode** | **String** | Optional - Enter \&quot;INC\&quot; if the tax amount is included in the expense amount otherwise enter \&quot;EX\&quot; when the amount exlcudes the tax. Defaults to \&quot;Ex\&quot;. The tax amount on the expense will be autocalculated. |  [optional] |
|**verifyAndSave** | **Boolean** | Pass false if creating a draft expense. True otherwise. |  [optional] |
|**isChargeable** | **Boolean** | aka Billable. Defaults to false if not provided. If set to true, a CustomerIDFK or CustomerName must be provided. |  [optional] |
|**isReimbursable** | **Boolean** | Defaults to false if not provided. |  [optional] |



