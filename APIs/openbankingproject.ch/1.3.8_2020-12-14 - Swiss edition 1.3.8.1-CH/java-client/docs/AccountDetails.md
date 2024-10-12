

# AccountDetails

The ASPSP shall give at least one of the account reference identifiers:   - iban   - bban   - pan   - maskedPan   - msisdn If the account is a multicurrency account currency code in \"currency\" is set to \"XXX\". 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | **LinksAccountDetails** |  |  [optional] |
|**balances** | [**List&lt;Balance&gt;**](Balance.md) | A list of balances regarding this account, e.g. the current balance, the last booked balance. The list might be restricted to the current balance.  |  [optional] |
|**bban** | **String** | Basic Bank Account Number (BBAN) Identifier.  This data element can be used in the body of the consent request.   Message for retrieving account access consent from this account. This   data elements is used for payment accounts which have no IBAN.   ISO20022: Basic Bank Account Number (BBAN).       Identifier used nationally by financial institutions, i.e., in individual countries,    generally as part of a National Account Numbering Scheme(s),    which uniquely identifies the account of a customer.  |  [optional] |
|**bic** | **String** | BICFI  |  [optional] |
|**cashAccountType** | **String** | ExternalCashAccountType1Code from ISO 20022.  |  [optional] |
|**currency** | **String** | ISO 4217 Alpha 3 currency code.  |  |
|**details** | **String** | Specifications that might be provided by the ASPSP:   - characteristics of the account   - characteristics of the relevant card  |  [optional] |
|**displayName** | **String** | Name of the account as defined by the PSU within online channels.  |  [optional] |
|**iban** | **String** | IBAN of an account. |  [optional] |
|**linkedAccounts** | **String** | Case of a set of pending card transactions, the APSP will provide the relevant cash account the card is set up on. |  [optional] |
|**msisdn** | **String** | Mobile phone number. |  [optional] |
|**name** | **String** | Name of the account, as assigned by the ASPSP, in agreement with the account owner in order to provide an additional means of identification of the account. |  [optional] |
|**ownerName** | **String** | Name of the legal account owner.  If there is more than one owner, then e.g. two names might be noted here.  For a corporate account, the corporate name is used for this attribute. Even if supported by the ASPSP, the provision of this field might depend on the fact whether an explicit consent to this specific additional account information has been given by the PSU.  |  [optional] |
|**product** | **String** | Product name of the bank for this account, proprietary definition. |  [optional] |
|**resourceId** | **String** | This shall be filled, if addressable resource are created by the ASPSP on the /accounts or /card-accounts endpoint. |  [optional] |
|**status** | **AccountStatus** |  |  [optional] |
|**usage** | [**UsageEnum**](#UsageEnum) | Specifies the usage of the account:   * PRIV: private personal account   * ORGA: professional account  |  [optional] |



## Enum: UsageEnum

| Name | Value |
|---- | -----|
| PRIV | &quot;PRIV&quot; |
| ORGA | &quot;ORGA&quot; |



