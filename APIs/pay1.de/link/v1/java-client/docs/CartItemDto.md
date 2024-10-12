

# CartItemDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deliveryDateEnd** | **LocalDate** | delivery period end date |  [optional] |
|**deliveryDateStart** | **LocalDate** | delivery date |  [optional] |
|**description** | **String** | item description |  [optional] |
|**number** | **String** | item number |  |
|**price** | **Long** | gross price of single item |  |
|**quantity** | **Long** | total number of ordered items |  |
|**type** | [**TypeEnum**](#TypeEnum) | item type |  |
|**vatRate** | **Long** | vat rate (&lt;100 in %, &gt;&#x3D;100 in bp) |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| GOODS | &quot;goods&quot; |
| SHIPMENT | &quot;shipment&quot; |
| HANDLING | &quot;handling&quot; |
| VOUCHER | &quot;voucher&quot; |



