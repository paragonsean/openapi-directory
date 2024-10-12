

# AccountReference16CH

Reference to an account by either   * IBAN, of a payment accounts, or   * otherAccountIdentification, for payment accounts if there is no IBAN adapted from ISO pain.001.001.03.ch.02 CashAccount16-CH_IdTpCcy 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cashAccountType** | **String** | ExternalCashAccountType1Code from ISO 20022.  |  [optional] |
|**currency** | **String** | ISO 4217 Alpha 3 currency code.  |  [optional] |
|**iban** | **String** | IBAN of an account. |  [optional] |
|**otherAccountIdentification** | **String** | Other payment account Identifier. adapted from ISO pain.001.001.03.ch.02 GenericAccountIdentification1-CH  |  [optional] |



