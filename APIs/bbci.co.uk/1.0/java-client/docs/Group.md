

# Group


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **BigDecimal** |  |  [optional] |
|**episodeSortDirection** | **String** |  |  [optional] |
|**groupType** | [**GroupTypeEnum**](#GroupTypeEnum) |  |  [optional] |
|**id** | **String** |  |  |
|**images** | [**GroupImages**](GroupImages.md) |  |  [optional] |
|**initialChildren** | [**List&lt;GroupInitialChildrenInner&gt;**](GroupInitialChildrenInner.md) |  |  [optional] |
|**masterBrand** | [**MasterBrand**](MasterBrand.md) |  |  [optional] |
|**relatedLinks** | [**List&lt;GroupRelatedLinksInner&gt;**](GroupRelatedLinksInner.md) |  |  [optional] |
|**shortTitle** | **String** |  |  [optional] |
|**stacked** | **Boolean** |  |  [optional] |
|**synopses** | [**ClipVersionsInnerGuidanceText**](ClipVersionsInnerGuidanceText.md) |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |



## Enum: GroupTypeEnum

| Name | Value |
|---- | -----|
| TLEO | &quot;tleo&quot; |
| CURATED | &quot;curated&quot; |
| AUTOMATED | &quot;automated&quot; |
| EVENT | &quot;event&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| GROUP | &quot;group&quot; |
| GROUP_LARGE | &quot;group_large&quot; |



