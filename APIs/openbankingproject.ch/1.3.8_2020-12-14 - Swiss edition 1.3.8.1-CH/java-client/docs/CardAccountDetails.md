

# CardAccountDetails

Card account details. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | **LinksAccountDetails** |  |  [optional] |
|**balances** | [**List&lt;Balance&gt;**](Balance.md) | A list of balances regarding this account, e.g. the current balance, the last booked balance. The list might be restricted to the current balance.  |  [optional] |
|**creditLimit** | [**Amount**](Amount.md) |  |  [optional] |
|**currency** | **String** | ISO 4217 Alpha 3 currency code.  |  |
|**debitAccounting** | **Boolean** | If true, the amounts of debits on the reports are quoted positive with the related consequence for balances. If false, the amount of debits on the reports are quoted negative.  |  [optional] |
|**details** | **String** | Specifications that might be provided by the ASPSP:   - characteristics of the account   - characteristics of the relevant card  |  [optional] |
|**displayName** | **String** | Name of the account as defined by the PSU within online channels.  |  [optional] |
|**maskedPan** | **String** | Masked Primary Account Number.  |  |
|**name** | **String** | Name of the account, as assigned by the ASPSP,  in agreement with the account owner in order to provide an additional means of identification of the account.  |  [optional] |
|**ownerName** | **String** | Name of the legal account owner.  If there is more than one owner, then e.g. two names might be noted here.  For a corporate account, the corporate name is used for this attribute. Even if supported by the ASPSP, the provision of this field might depend on the fact whether an explicit consent to this specific additional account information has been given by the PSU.  |  [optional] |
|**product** | **String** | Product Name of the Bank for this account, proprietary definition.  |  [optional] |
|**resourceId** | **String** | This is the data element to be used in the path when retrieving data from a dedicated account. This shall be filled, if addressable resource are created by the ASPSP on the /card-accounts endpoint.  |  [optional] |
|**status** | **AccountStatus** |  |  [optional] |
|**usage** | [**UsageEnum**](#UsageEnum) | Specifies the usage of the account:   * PRIV: private personal account   * ORGA: professional account  |  [optional] |



## Enum: UsageEnum

| Name | Value |
|---- | -----|
| PRIV | &quot;PRIV&quot; |
| ORGA | &quot;ORGA&quot; |



