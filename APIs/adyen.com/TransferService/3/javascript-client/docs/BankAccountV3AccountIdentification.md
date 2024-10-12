# TransfersApi.BankAccountV3AccountIdentification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountNumber** | **String** | The bank account number, without separators or whitespace. | 
**bsbCode** | **String** | The 6-digit [Bank State Branch (BSB) code](https://en.wikipedia.org/wiki/Bank_state_branch), without separators or whitespace. | 
**type** | **String** | **auLocal** | [default to &#39;auLocal&#39;]
**bankCode** | **String** | The 4-digit bank code (Registreringsnummer) (without separators or whitespace). | 
**branchNumber** | **String** | The bank account branch number, without separators or whitespace. | 
**accountType** | **String** | The bank account type.  Possible values: **checking** or **savings**. Defaults to **checking**. | [optional] [default to &#39;checking&#39;]
**institutionNumber** | **String** | The 3-digit institution number, without separators or whitespace. | 
**transitNumber** | **String** | The 5-digit transit number, without separators or whitespace. | 
**clearingCode** | **String** | The 3-digit clearing code, without separators or whitespace. | 
**iban** | **String** | The international bank account number as defined in the [ISO-13616](https://www.iso.org/standard/81090.html) standard. | 
**additionalBankIdentification** | [**AdditionalBankIdentification**](AdditionalBankIdentification.md) | Additional identification codes of the bank. Some banks may require these identifiers for cross-border transfers. | [optional] 
**bic** | **String** | The bank&#39;s 8- or 11-character BIC or SWIFT code. | 
**clearingNumber** | **String** | The 4- to 5-digit clearing number ([Clearingnummer](https://sv.wikipedia.org/wiki/Clearingnummer)), without separators or whitespace. | 
**sortCode** | **String** | The 6-digit [sort code](https://en.wikipedia.org/wiki/Sort_code), without separators or whitespace. | 
**routingNumber** | **String** | The 9-digit [routing number](https://en.wikipedia.org/wiki/ABA_routing_transit_number), without separators or whitespace. | 



## Enum: TypeEnum


* `auLocal` (value: `"auLocal"`)

* `brLocal` (value: `"brLocal"`)

* `caLocal` (value: `"caLocal"`)

* `czLocal` (value: `"czLocal"`)

* `dkLocal` (value: `"dkLocal"`)

* `hkLocal` (value: `"hkLocal"`)

* `huLocal` (value: `"huLocal"`)

* `iban` (value: `"iban"`)

* `noLocal` (value: `"noLocal"`)

* `nzLocal` (value: `"nzLocal"`)

* `numberAndBic` (value: `"numberAndBic"`)

* `plLocal` (value: `"plLocal"`)

* `seLocal` (value: `"seLocal"`)

* `sgLocal` (value: `"sgLocal"`)

* `ukLocal` (value: `"ukLocal"`)

* `usLocal` (value: `"usLocal"`)





## Enum: AccountTypeEnum


* `checking` (value: `"checking"`)

* `savings` (value: `"savings"`)




