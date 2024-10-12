

# CustomerTokenCreationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAddress** | [**Address**](Address.md) |  |  [optional] |
|**customer** | [**Customer**](Customer.md) |  |  [optional] |
|**description** | **String** | Description of the purpose of the token. |  |
|**intendedUse** | [**IntendedUseEnum**](#IntendedUseEnum) | Intended use for the token. |  |
|**locale** | **String** | RFC 1766 customer&#39;s locale. |  |
|**purchaseCountry** | **String** | ISO 3166 alpha-2 purchase country. |  |
|**purchaseCurrency** | **String** | ISO 4217 purchase currency. |  |



## Enum: IntendedUseEnum

| Name | Value |
|---- | -----|
| SUBSCRIPTION | &quot;SUBSCRIPTION&quot; |



