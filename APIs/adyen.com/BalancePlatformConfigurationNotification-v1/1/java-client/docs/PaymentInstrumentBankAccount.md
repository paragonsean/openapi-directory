

# PaymentInstrumentBankAccount

Contains the business account details. Returned when you create a payment instrument with `type` **bankAccount**.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**formFactor** | **String** | The form factor of bank account. |  [optional] |
|**iban** | **String** | The international bank account number as defined in the [ISO-13616](https://www.iso.org/standard/81090.html) standard. |  |
|**type** | [**TypeEnum**](#TypeEnum) | **iban** |  |
|**accountNumber** | **String** | The bank account number, without separators or whitespace. |  |
|**accountType** | [**AccountTypeEnum**](#AccountTypeEnum) | The bank account type.  Possible values: **checking** or **savings**. Defaults to **checking**. |  [optional] |
|**routingNumber** | **String** | The 9-digit [routing number](https://en.wikipedia.org/wiki/ABA_routing_transit_number), without separators or whitespace. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IBAN | &quot;iban&quot; |
| US_LOCAL | &quot;usLocal&quot; |



## Enum: AccountTypeEnum

| Name | Value |
|---- | -----|
| CHECKING | &quot;checking&quot; |
| SAVINGS | &quot;savings&quot; |



