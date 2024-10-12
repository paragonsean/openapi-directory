

# GoogleAdsSearchads360V0ResourcesAssetGroupListingGroupFilter

AssetGroupListingGroupFilter represents a listing group filter tree node in an asset group.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assetGroup** | **String** | Immutable. The asset group which this asset group listing group filter is part of. |  [optional] |
|**caseValue** | [**GoogleAdsSearchads360V0ResourcesListingGroupFilterDimension**](GoogleAdsSearchads360V0ResourcesListingGroupFilterDimension.md) |  |  [optional] |
|**id** | **String** | Output only. The ID of the ListingGroupFilter. |  [optional] [readonly] |
|**parentListingGroupFilter** | **String** | Immutable. Resource name of the parent listing group subdivision. Null for the root listing group filter node. |  [optional] |
|**path** | [**GoogleAdsSearchads360V0ResourcesListingGroupFilterDimensionPath**](GoogleAdsSearchads360V0ResourcesListingGroupFilterDimensionPath.md) |  |  [optional] |
|**resourceName** | **String** | Immutable. The resource name of the asset group listing group filter. Asset group listing group filter resource name have the form: &#x60;customers/{customer_id}/assetGroupListingGroupFilters/{asset_group_id}~{listing_group_filter_id}&#x60; |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Immutable. Type of a listing group filter node. |  [optional] |
|**vertical** | [**VerticalEnum**](#VerticalEnum) | Immutable. The vertical the current node tree represents. All nodes in the same tree must belong to the same vertical. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| SUBDIVISION | &quot;SUBDIVISION&quot; |
| UNIT_INCLUDED | &quot;UNIT_INCLUDED&quot; |
| UNIT_EXCLUDED | &quot;UNIT_EXCLUDED&quot; |



## Enum: VerticalEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| SHOPPING | &quot;SHOPPING&quot; |



