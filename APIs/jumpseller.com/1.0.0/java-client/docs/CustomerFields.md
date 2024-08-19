

# CustomerFields


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAddress** | [**BillingAddress**](BillingAddress.md) |  |  [optional] |
|**customerAdditionalFields** | [**List&lt;CustomerAdditionalField&gt;**](CustomerAdditionalField.md) |  |  [optional] |
|**customerCategories** | [**List&lt;CustomerCategory&gt;**](CustomerCategory.md) |  |  [optional] |
|**email** | **String** | Email of the Customer |  [optional] |
|**id** | **Integer** | Unique identifier of the Customer |  [optional] |
|**name** | **String** | Name of the Customer |  [optional] |
|**phone** | **String** | Phone of the Customer |  [optional] |
|**shippingAddress** | [**ShippingAddress**](ShippingAddress.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the Customer |  [optional] |
|**surname** | **String** | Surname of the Customer |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| APPROVED | &quot;approved&quot; |
| PENDING | &quot;pending&quot; |
| DISABLED | &quot;disabled&quot; |



