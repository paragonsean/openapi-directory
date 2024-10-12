

# GoogleAdsSearchads360V0ResourcesCustomerAsset

A link between a customer and an asset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**asset** | **String** | Required. Immutable. The asset which is linked to the customer. |  [optional] |
|**resourceName** | **String** | Immutable. The resource name of the customer asset. CustomerAsset resource names have the form: &#x60;customers/{customer_id}/customerAssets/{asset_id}~{field_type}&#x60; |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the customer asset. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ENABLED | &quot;ENABLED&quot; |
| REMOVED | &quot;REMOVED&quot; |
| PAUSED | &quot;PAUSED&quot; |



