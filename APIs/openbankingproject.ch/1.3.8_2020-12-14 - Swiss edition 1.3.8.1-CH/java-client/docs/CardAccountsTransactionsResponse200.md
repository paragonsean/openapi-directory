

# CardAccountsTransactionsResponse200

Body of the JSON response for a successful read card account transaction list request. This card account report contains transactions resulting from the query parameters. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | **LinksDownload** |  |  [optional] |
|**balances** | [**List&lt;Balance&gt;**](Balance.md) | A list of balances regarding this account, e.g. the current balance, the last booked balance. The list might be restricted to the current balance.  |  [optional] |
|**cardAccount** | [**AccountReference16CH**](AccountReference16CH.md) |  |  [optional] |
|**cardTransactions** | [**CardAccountReport**](CardAccountReport.md) |  |  [optional] |
|**debitAccounting** | **Boolean** | If true, the amounts of debits on the reports are quoted positive with the related consequence for balances. If false, the amount of debits on the reports are quoted negative.  |  [optional] |



