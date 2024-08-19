

# CheckoutCustomFieldFields


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**area** | [**AreaEnum**](#AreaEnum) | Area of the CheckoutCustomField |  [optional] |
|**customFieldSelectOptions** | **List&lt;String&gt;** | The values for the CheckoutCustomField selection |  [optional] |
|**deletable** | **Boolean** | True if the CheckoutCustomField can be removed from the store |  [optional] |
|**id** | **Integer** | Unique identifier of the CheckoutCustomField |  [optional] |
|**label** | **String** | Label given to the CheckoutCustomField |  [optional] |
|**position** | **Integer** | Position of the CheckoutCustomField |  [optional] |
|**required** | **Boolean** | True if the CheckoutCustomField is mandatory |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the CheckoutCustomField |  [optional] |



## Enum: AreaEnum

| Name | Value |
|---- | -----|
| CONTACT | &quot;contact&quot; |
| BILLING_SHIPPING | &quot;billing_shipping&quot; |
| OTHER | &quot;other&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TEXT | &quot;text&quot; |
| SELECT | &quot;select&quot; |
| INPUT | &quot;input&quot; |
| CHECKBOX | &quot;checkbox&quot; |



