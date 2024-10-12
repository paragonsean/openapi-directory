

# InvoiceItem

An InvoiceItem object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **BigDecimal** | The price, in US dollars, of the Invoice Item. Equal to the unit price multiplied by quantity. |  [optional] [readonly] |
|**from** | **OffsetDateTime** | The date the Invoice Item started, based on month. |  [optional] [readonly] |
|**label** | **String** | The Invoice Item&#39;s display label. |  [optional] [readonly] |
|**quantity** | **Integer** | The quantity of this Item for the specified Invoice. |  [optional] [readonly] |
|**tax** | **BigDecimal** | The amount of tax levied on this Item in US Dollars. |  [optional] [readonly] |
|**to** | **OffsetDateTime** | The date the Invoice Item ended, based on month. |  [optional] [readonly] |
|**total** | **BigDecimal** | The price of this Item after taxes in US Dollars. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of service, ether &#x60;hourly&#x60; or &#x60;misc&#x60;. |  [optional] [readonly] |
|**unitPrice** | **String** | The monthly service fee in US Dollars for this Item. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| HOURLY | &quot;hourly&quot; |
| MISC | &quot;misc&quot; |



