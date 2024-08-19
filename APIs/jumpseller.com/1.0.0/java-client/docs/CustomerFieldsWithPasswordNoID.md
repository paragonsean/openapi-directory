

# CustomerFieldsWithPasswordNoID


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAddress** | [**BillingAddress**](BillingAddress.md) |  |  [optional] |
|**customerCategory** | **List&lt;Integer&gt;** |  |  [optional] |
|**email** | **String** | Email of the Customer |  [optional] |
|**password** | **String** | Password |  [optional] |
|**phone** | **String** | Phone of the Customer |  [optional] |
|**shippingAddress** | [**ShippingAddress**](ShippingAddress.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the Customer |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| APPROVED | &quot;approved&quot; |
| PENDING | &quot;pending&quot; |
| DISABLED | &quot;disabled&quot; |



