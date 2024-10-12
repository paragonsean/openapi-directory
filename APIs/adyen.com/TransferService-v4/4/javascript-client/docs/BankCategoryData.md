# TransfersApi.BankCategoryData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **String** | The priority for the bank transfer. This sets the speed at which the transfer is sent and the fees that you have to pay. Required for transfers with &#x60;category&#x60; **bank**.  Possible values:  * **regular**: For normal, low-value transactions.  * **fast**: Faster way to transfer funds but has higher fees. Recommended for high-priority, low-value transactions.  * **wire**: Fastest way to transfer funds but has the highest fees. Recommended for high-priority, high-value transactions.  * **instant**: Instant way to transfer funds in [SEPA countries](https://www.ecb.europa.eu/paym/integration/retail/sepa/html/index.en.html).  * **crossBorder**: High-value transfer to a recipient in a different country.  * **internal**: Transfer to an Adyen-issued business bank account (by bank account number/IBAN). | [optional] 
**type** | **String** | **bank** | [optional] [default to &#39;bank&#39;]



## Enum: PriorityEnum


* `crossBorder` (value: `"crossBorder"`)

* `fast` (value: `"fast"`)

* `instant` (value: `"instant"`)

* `internal` (value: `"internal"`)

* `regular` (value: `"regular"`)

* `wire` (value: `"wire"`)





## Enum: TypeEnum


* `bank` (value: `"bank"`)




