# TransfersApi.USLocalAccountIdentification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountNumber** | **String** | The bank account number, without separators or whitespace. | 
**accountType** | **String** | The bank account type.  Possible values: **checking** or **savings**. Defaults to **checking**. | [optional] [default to &#39;checking&#39;]
**routingNumber** | **String** | The 9-digit [routing number](https://en.wikipedia.org/wiki/ABA_routing_transit_number), without separators or whitespace. | 
**type** | **String** | **usLocal** | [default to &#39;usLocal&#39;]



## Enum: AccountTypeEnum


* `checking` (value: `"checking"`)

* `savings` (value: `"savings"`)





## Enum: TypeEnum


* `usLocal` (value: `"usLocal"`)




