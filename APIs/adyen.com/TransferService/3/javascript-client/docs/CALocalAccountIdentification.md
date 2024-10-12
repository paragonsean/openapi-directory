# TransfersApi.CALocalAccountIdentification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountNumber** | **String** | The 5- to 12-digit bank account number, without separators or whitespace. | 
**accountType** | **String** | The bank account type.  Possible values: **checking** or **savings**. Defaults to **checking**. | [optional] [default to &#39;checking&#39;]
**institutionNumber** | **String** | The 3-digit institution number, without separators or whitespace. | 
**transitNumber** | **String** | The 5-digit transit number, without separators or whitespace. | 
**type** | **String** | **caLocal** | [default to &#39;caLocal&#39;]



## Enum: AccountTypeEnum


* `checking` (value: `"checking"`)

* `savings` (value: `"savings"`)





## Enum: TypeEnum


* `caLocal` (value: `"caLocal"`)




