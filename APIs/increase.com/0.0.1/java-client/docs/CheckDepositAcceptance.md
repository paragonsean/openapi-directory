

# CheckDepositAcceptance

If your deposit is successfully parsed and accepted by Increase, this will contain details of the parsed check.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumber** | **String** | The account number printed on the check. |  |
|**amount** | **Integer** | The amount to be deposited in the minor unit of the transaction&#39;s currency. For dollars, for example, this is cents. |  |
|**auxiliaryOnUs** | **String** | An additional line of metadata printed on the check. This typically includes the check number for business checks. |  |
|**checkDepositId** | **String** | The ID of the Check Deposit that was accepted. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the transaction&#39;s currency. |  |
|**routingNumber** | **String** | The routing number printed on the check. |  |
|**serialNumber** | **String** | The check serial number, if present, for consumer checks. For business checks, the serial number is usually in the &#x60;auxiliary_on_us&#x60; field. |  |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| CAD | &quot;CAD&quot; |
| CHF | &quot;CHF&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| JPY | &quot;JPY&quot; |
| USD | &quot;USD&quot; |



