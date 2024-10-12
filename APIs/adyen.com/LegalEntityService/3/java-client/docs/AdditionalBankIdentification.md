

# AdditionalBankIdentification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | The value of the additional bank identification. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of additional bank identification, depending on the country.  Possible values:   * **gbSortCode**: The 6-digit [UK sort code](https://en.wikipedia.org/wiki/Sort_code), without separators or spaces  * **usRoutingNumber**: The 9-digit [routing number](https://en.wikipedia.org/wiki/ABA_routing_transit_number), without separators or spaces. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| GB_SORT_CODE | &quot;gbSortCode&quot; |
| US_ROUTING_NUMBER | &quot;usRoutingNumber&quot; |



