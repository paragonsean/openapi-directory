

# CreateAnExternalAccountParameters


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumber** | **String** | The account number for the destination account. |  |
|**description** | **String** | The name you choose for the Account. |  |
|**funding** | [**FundingEnum**](#FundingEnum) | The type of the destination account. Defaults to &#x60;checking&#x60;. |  [optional] |
|**routingNumber** | **String** | The American Bankers&#39; Association (ABA) Routing Transit Number (RTN) for the destination account. |  |



## Enum: FundingEnum

| Name | Value |
|---- | -----|
| CHECKING | &quot;checking&quot; |
| SAVINGS | &quot;savings&quot; |
| OTHER | &quot;other&quot; |



