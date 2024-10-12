

# CreateAccountHolderRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHolderCode** | **String** | Your unique identifier for the prospective account holder. The length must be between three (3) and fifty (50) characters long. Only letters, digits, and hyphens (-) are allowed. |  |
|**accountHolderDetails** | [**AccountHolderDetails**](AccountHolderDetails.md) | The details of the prospective account holder. |  |
|**createDefaultAccount** | **Boolean** | If set to **true**, an account with the default options is automatically created for the account holder. By default, this field is set to **true**. |  [optional] |
|**description** | **String** | A description of the prospective account holder, maximum 256 characters. You can use alphanumeric characters (A-Z, a-z, 0-9), white spaces, and underscores &#x60;_&#x60;. |  [optional] |
|**legalEntity** | [**LegalEntityEnum**](#LegalEntityEnum) | The legal entity type of the account holder. This determines the information that should be provided in the request.  Possible values: **Business**, **Individual**, or **NonProfit**.  * If set to **Business** or **NonProfit**, then &#x60;accountHolderDetails.businessDetails&#x60; must be provided, with at least one entry in the &#x60;accountHolderDetails.businessDetails.shareholders&#x60; list.  * If set to **Individual**, then &#x60;accountHolderDetails.individualDetails&#x60; must be provided. |  |
|**primaryCurrency** | **String** | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes), with which the prospective account holder primarily deals. |  [optional] |
|**processingTier** | **Integer** | The starting [processing tier](https://docs.adyen.com/marketplaces-and-platforms/classic/onboarding-and-verification/precheck-kyc-information) for the prospective account holder. |  [optional] |
|**verificationProfile** | **String** | The identifier of the profile that applies to this entity. |  [optional] |



## Enum: LegalEntityEnum

| Name | Value |
|---- | -----|
| BUSINESS | &quot;Business&quot; |
| INDIVIDUAL | &quot;Individual&quot; |
| NON_PROFIT | &quot;NonProfit&quot; |
| PARTNERSHIP | &quot;Partnership&quot; |
| PUBLIC_COMPANY | &quot;PublicCompany&quot; |



