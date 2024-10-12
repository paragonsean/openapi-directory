

# PlacementGroup

Contains properties of a package or roadblock.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Account ID of this placement group. This is a read-only field that can be left blank. |  [optional] |
|**advertiserId** | **String** | Advertiser ID of this placement group. This is a required field on insertion. |  [optional] |
|**advertiserIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**archived** | **Boolean** | Whether this placement group is archived. |  [optional] |
|**campaignId** | **String** | Campaign ID of this placement group. This field is required on insertion. |  [optional] |
|**campaignIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**childPlacementIds** | **List&lt;String&gt;** | IDs of placements which are assigned to this placement group. This is a read-only, auto-generated field. |  [optional] |
|**comment** | **String** | Comments for this placement group. |  [optional] |
|**contentCategoryId** | **String** | ID of the content category assigned to this placement group. |  [optional] |
|**createInfo** | [**LastModifiedInfo**](LastModifiedInfo.md) |  |  [optional] |
|**directorySiteId** | **String** | Directory site ID associated with this placement group. On insert, you must set either this field or the site_id field to specify the site associated with this placement group. This is a required field that is read-only after insertion. |  [optional] |
|**directorySiteIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**externalId** | **String** | External ID for this placement. |  [optional] |
|**id** | **String** | ID of this placement group. This is a read-only, auto-generated field. |  [optional] |
|**idDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#placementGroup\&quot;. |  [optional] |
|**lastModifiedInfo** | [**LastModifiedInfo**](LastModifiedInfo.md) |  |  [optional] |
|**name** | **String** | Name of this placement group. This is a required field and must be less than 256 characters long. |  [optional] |
|**placementGroupType** | [**PlacementGroupTypeEnum**](#PlacementGroupTypeEnum) | Type of this placement group. A package is a simple group of placements that acts as a single pricing point for a group of tags. A roadblock is a group of placements that not only acts as a single pricing point, but also assumes that all the tags in it will be served at the same time. A roadblock requires one of its assigned placements to be marked as primary for reporting. This field is required on insertion. |  [optional] |
|**placementStrategyId** | **String** | ID of the placement strategy assigned to this placement group. |  [optional] |
|**pricingSchedule** | [**PricingSchedule**](PricingSchedule.md) |  |  [optional] |
|**primaryPlacementId** | **String** | ID of the primary placement, used to calculate the media cost of a roadblock (placement group). Modifying this field will automatically modify the primary field on all affected roadblock child placements. |  [optional] |
|**primaryPlacementIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**siteId** | **String** | Site ID associated with this placement group. On insert, you must set either this field or the directorySiteId field to specify the site associated with this placement group. This is a required field that is read-only after insertion. |  [optional] |
|**siteIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**subaccountId** | **String** | Subaccount ID of this placement group. This is a read-only field that can be left blank. |  [optional] |



## Enum: PlacementGroupTypeEnum

| Name | Value |
|---- | -----|
| PACKAGE | &quot;PLACEMENT_PACKAGE&quot; |
| ROADBLOCK | &quot;PLACEMENT_ROADBLOCK&quot; |



