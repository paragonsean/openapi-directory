

# Order


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cartId** | **String** |  |  [optional] |
|**changeDate** | **OffsetDateTime** |  |  |
|**createDate** | **OffsetDateTime** |  |  |
|**currency** | **String** |  |  |
|**customer** | [**Customer**](Customer.md) |  |  |
|**items** | [**List&lt;OrderItem&gt;**](OrderItem.md) |  |  |
|**orderDate** | **OffsetDateTime** |  |  |
|**orderNumber** | **String** |  |  |
|**previousItems** | [**List&lt;OrderItem&gt;**](OrderItem.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**subtotal** | **BigDecimal** |  |  |
|**total** | **BigDecimal** |  |  |
|**totalDiscounts** | **BigDecimal** |  |  |
|**totalPaymentCost** | **BigDecimal** |  |  |
|**totalShipping** | **BigDecimal** |  |  |
|**totalTax** | **BigDecimal** |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;accepted&quot; |



