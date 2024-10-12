# LegalEntityManagementApi.SELocalAccountIdentification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountNumber** | **String** | The 7- to 10-digit bank account number ([Bankkontonummer](https://sv.wikipedia.org/wiki/Bankkonto)), without the clearing number, separators, or whitespace. | 
**clearingNumber** | **String** | The 4- to 5-digit clearing number ([Clearingnummer](https://sv.wikipedia.org/wiki/Clearingnummer)), without separators or whitespace. | 
**formFactor** | **String** | The form factor of the account.  Possible values: **physical**, **virtual**. Default value: **physical**. | [optional] [default to &#39;physical&#39;]
**type** | **String** | **seLocal** | [default to &#39;seLocal&#39;]



## Enum: TypeEnum


* `seLocal` (value: `"seLocal"`)




