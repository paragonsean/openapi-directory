

# BBANInstrument

Bank account BBAN instrument.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumber** | **String** | Bank Account Number. |  |
|**accountType** | [**AccountTypeEnum**](#AccountTypeEnum) | Bank Account Type. |  |
|**bankName** | **String** | Bank name. |  [optional] |
|**bic** | **String** | Bank Identifier Code. |  [optional] |
|**last4** | **String** | Bank Account Number&#39;s last 4 digits. |  [optional] [readonly] |
|**routingNumber** | **String** | Bank Routing Number. |  |



## Enum: AccountTypeEnum

| Name | Value |
|---- | -----|
| CHECKING | &quot;checking&quot; |
| SAVINGS | &quot;savings&quot; |
| OTHER | &quot;other&quot; |



