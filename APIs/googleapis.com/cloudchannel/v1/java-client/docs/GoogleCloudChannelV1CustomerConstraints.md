

# GoogleCloudChannelV1CustomerConstraints

Represents constraints required to purchase the Offer for a customer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedCustomerTypes** | [**List&lt;AllowedCustomerTypesEnum&gt;**](#List&lt;AllowedCustomerTypesEnum&gt;) | Allowed Customer Type. |  [optional] |
|**allowedRegions** | **List&lt;String&gt;** | Allowed geographical regions of the customer. |  [optional] |
|**promotionalOrderTypes** | [**List&lt;PromotionalOrderTypesEnum&gt;**](#List&lt;PromotionalOrderTypesEnum&gt;) | Allowed Promotional Order Type. Present for Promotional offers. |  [optional] |



## Enum: List&lt;AllowedCustomerTypesEnum&gt;

| Name | Value |
|---- | -----|
| CUSTOMER_TYPE_UNSPECIFIED | &quot;CUSTOMER_TYPE_UNSPECIFIED&quot; |
| DOMAIN | &quot;DOMAIN&quot; |
| TEAM | &quot;TEAM&quot; |



## Enum: List&lt;PromotionalOrderTypesEnum&gt;

| Name | Value |
|---- | -----|
| PROMOTIONAL_TYPE_UNSPECIFIED | &quot;PROMOTIONAL_TYPE_UNSPECIFIED&quot; |
| NEW_UPGRADE | &quot;NEW_UPGRADE&quot; |
| TRANSFER | &quot;TRANSFER&quot; |
| PROMOTION_SWITCH | &quot;PROMOTION_SWITCH&quot; |



