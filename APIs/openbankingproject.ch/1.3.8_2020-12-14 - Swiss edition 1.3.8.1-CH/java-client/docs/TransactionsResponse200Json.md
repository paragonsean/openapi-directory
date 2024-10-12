

# TransactionsResponse200Json

Body of the JSON response for a successful read transaction list request. This account report contains transactions resulting from the query parameters. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | **LinksDownload** |  |  [optional] |
|**account** | [**AccountReference16CH**](AccountReference16CH.md) |  |  [optional] |
|**balances** | [**List&lt;Balance&gt;**](Balance.md) | A list of balances regarding this account, e.g. the current balance, the last booked balance. The list might be restricted to the current balance.  |  [optional] |
|**transactions** | [**AccountReport**](AccountReport.md) |  |  [optional] |



