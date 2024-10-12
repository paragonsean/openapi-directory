

# BankAccountInfoAccountIdentification

Identification of the bank account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumber** | **String** | The bank account number, without separators or whitespace. |  |
|**bsbCode** | **String** | The 6-digit [Bank State Branch (BSB) code](https://en.wikipedia.org/wiki/Bank_state_branch), without separators or whitespace. |  |
|**formFactor** | **String** | The form factor of the account.  Possible values: **physical**, **virtual**. Default value: **physical**. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **auLocal** |  |
|**accountType** | [**AccountTypeEnum**](#AccountTypeEnum) | The bank account type.  Possible values: **checking** or **savings**. Defaults to **checking**. |  [optional] |
|**institutionNumber** | **String** | The 3-digit institution number, without separators or whitespace. |  |
|**transitNumber** | **String** | The 5-digit transit number, without separators or whitespace. |  |
|**bankCode** | **String** | The 4-digit bank code (Registreringsnummer) (without separators or whitespace). |  |
|**clearingCode** | **String** | The 3-digit clearing code, without separators or whitespace. |  |
|**iban** | **String** | The international bank account number as defined in the [ISO-13616](https://www.iso.org/standard/81090.html) standard. |  |
|**additionalBankIdentification** | [**AdditionalBankIdentification**](AdditionalBankIdentification.md) | Additional identification codes of the bank. Some banks may require these identifiers for cross-border transfers. |  [optional] |
|**bic** | **String** | The bank&#39;s 8- or 11-character BIC or SWIFT code. |  |
|**clearingNumber** | **String** | The 4- to 5-digit clearing number ([Clearingnummer](https://sv.wikipedia.org/wiki/Clearingnummer)), without separators or whitespace. |  |
|**sortCode** | **String** | The 6-digit [sort code](https://en.wikipedia.org/wiki/Sort_code), without separators or whitespace. |  |
|**routingNumber** | **String** | The 9-digit [routing number](https://en.wikipedia.org/wiki/ABA_routing_transit_number), without separators or whitespace. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AU_LOCAL | &quot;auLocal&quot; |
| CA_LOCAL | &quot;caLocal&quot; |
| CZ_LOCAL | &quot;czLocal&quot; |
| DK_LOCAL | &quot;dkLocal&quot; |
| HK_LOCAL | &quot;hkLocal&quot; |
| HU_LOCAL | &quot;huLocal&quot; |
| IBAN | &quot;iban&quot; |
| NO_LOCAL | &quot;noLocal&quot; |
| NZ_LOCAL | &quot;nzLocal&quot; |
| NUMBER_AND_BIC | &quot;numberAndBic&quot; |
| PL_LOCAL | &quot;plLocal&quot; |
| SE_LOCAL | &quot;seLocal&quot; |
| SG_LOCAL | &quot;sgLocal&quot; |
| UK_LOCAL | &quot;ukLocal&quot; |
| US_LOCAL | &quot;usLocal&quot; |



## Enum: AccountTypeEnum

| Name | Value |
|---- | -----|
| CHECKING | &quot;checking&quot; |
| SAVINGS | &quot;savings&quot; |



