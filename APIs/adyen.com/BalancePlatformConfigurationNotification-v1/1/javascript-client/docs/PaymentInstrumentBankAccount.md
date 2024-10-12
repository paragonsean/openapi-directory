# ConfigurationWebhooks.PaymentInstrumentBankAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formFactor** | **String** | The form factor of bank account. | [optional] [default to &#39;physical&#39;]
**iban** | **String** | The international bank account number as defined in the [ISO-13616](https://www.iso.org/standard/81090.html) standard. | 
**type** | **String** | **iban** | [default to &#39;iban&#39;]
**accountNumber** | **String** | The bank account number, without separators or whitespace. | 
**accountType** | **String** | The bank account type.  Possible values: **checking** or **savings**. Defaults to **checking**. | [optional] [default to &#39;checking&#39;]
**routingNumber** | **String** | The 9-digit [routing number](https://en.wikipedia.org/wiki/ABA_routing_transit_number), without separators or whitespace. | 



## Enum: TypeEnum


* `iban` (value: `"iban"`)

* `usLocal` (value: `"usLocal"`)





## Enum: AccountTypeEnum


* `checking` (value: `"checking"`)

* `savings` (value: `"savings"`)




