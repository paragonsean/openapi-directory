

# UpdateAccountHolderRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHolderCode** | **String** | The code of the Account Holder to be updated. |  |
|**accountHolderDetails** | [**AccountHolderDetails**](AccountHolderDetails.md) | The details to which the Account Holder should be updated.  Required if a processingTier is not provided. |  [optional] |
|**description** | **String** | A description of the account holder, maximum 256 characters. You can use alphanumeric characters (A-Z, a-z, 0-9), white spaces, and underscores &#x60;_&#x60;. |  [optional] |
|**legalEntity** | [**LegalEntityEnum**](#LegalEntityEnum) | The legal entity type of the account holder. This determines the information that should be provided in the request.  Possible values: **Business**, **Individual**, or **NonProfit**.  * If set to **Business** or **NonProfit**, then &#x60;accountHolderDetails.businessDetails&#x60; must be provided, with at least one entry in the &#x60;accountHolderDetails.businessDetails.shareholders&#x60; list.  * If set to **Individual**, then &#x60;accountHolderDetails.individualDetails&#x60; must be provided. |  [optional] |
|**primaryCurrency** | **String** | The primary three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes), to which the account holder should be updated. |  [optional] |
|**processingTier** | **Integer** | The processing tier to which the Account Holder should be updated. &gt;The processing tier can not be lowered through this request.  &gt;Required if accountHolderDetails are not provided. |  [optional] |



## Enum: LegalEntityEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;Business&quot; |
| INDIVIDUAL | &quot;Individual&quot; |
| NON_PROFIT | &quot;NonProfit&quot; |



