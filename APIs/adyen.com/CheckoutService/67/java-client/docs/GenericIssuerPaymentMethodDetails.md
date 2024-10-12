

# GenericIssuerPaymentMethodDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**issuer** | **String** | The issuer id of the shopper&#39;s selected bank. |  |
|**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**storedPaymentMethodId** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **genericissuer** |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ONLINE_BANKING_PL | &quot;onlineBanking_PL&quot; |
| EPS | &quot;eps&quot; |
| ONLINE_BANKING_SK | &quot;onlineBanking_SK&quot; |
| ONLINE_BANKING_CZ | &quot;onlineBanking_CZ&quot; |



