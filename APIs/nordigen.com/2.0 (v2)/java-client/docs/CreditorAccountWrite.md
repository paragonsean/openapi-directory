

# CreditorAccountWrite

Creditor account write serializer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | **String** | Creditor account type identifier |  |
|**addressCountry** | **AddressCountryEnum** |  |  [optional] |
|**addressStreet** | **String** | Creditor account address street |  [optional] |
|**agent** | **String** | Creditor account BICFI Identifier |  [optional] |
|**agentName** | **String** | Creditor account agent name |  [optional] |
|**currency** | **String** | Creditor account currency |  |
|**id** | **UUID** | Unique entry ID |  [optional] [readonly] |
|**institutionId** | **String** | an Institution ID for this CreditorAccount |  [optional] |
|**name** | **String** | Creditor account name |  |
|**postCode** | **String** | Creditor account address post code |  [optional] |
|**type** | **TypeEnum** | Creditor account type  * &#x60;IBAN&#x60; - IBAN * &#x60;SCAN&#x60; - SortCodeAccountNumber |  [optional] |



