

# PaymeroAllOfSettings

Paymero settings object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountExceeded** | **Boolean** | Decline transactions when the amount received exceeds the amount requested. |  [optional] |
|**mainCurrency** | [**MainCurrencyEnum**](#MainCurrencyEnum) | This will be the blockchain on which currency runs. |  [optional] |
|**targetCurrency** | **String** | This will be the currency to which you want to auto-convert the received cryptocurrency in to. |  [optional] |



## Enum: MainCurrencyEnum

| Name | Value |
|---- | -----|
| TRX | &quot;TRX&quot; |
| ETH | &quot;ETH&quot; |



