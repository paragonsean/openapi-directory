

# GoogleAdsSearchads360V0ResourcesCustomerAssetSet

CustomerAssetSet is the linkage between a customer and an asset set. Adding a CustomerAssetSet links an asset set with a customer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetSet** | **String** | Immutable. The asset set which is linked to the customer. |  [optional] |
|**customer** | **String** | Immutable. The customer to which this asset set is linked. |  [optional] |
|**resourceName** | **String** | Immutable. The resource name of the customer asset set. Asset set asset resource names have the form: &#x60;customers/{customer_id}/customerAssetSets/{asset_set_id}&#x60; |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Output only. The status of the customer asset set asset. Read-only. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ENABLED | &quot;ENABLED&quot; |
| REMOVED | &quot;REMOVED&quot; |



