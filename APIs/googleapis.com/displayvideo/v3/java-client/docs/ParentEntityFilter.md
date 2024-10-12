

# ParentEntityFilter

A filtering option that filters on selected file types belonging to a chosen set of filter entities.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileType** | [**List&lt;FileTypeEnum&gt;**](#List&lt;FileTypeEnum&gt;) | Required. File types that will be returned. |  [optional] |
|**filterIds** | **List&lt;String&gt;** | The IDs of the specified filter type. This is used to filter entities to fetch. If filter type is not &#x60;FILTER_TYPE_NONE&#x60;, at least one ID must be specified. |  [optional] |
|**filterType** | [**FilterTypeEnum**](#FilterTypeEnum) | Required. Filter type used to filter fetched entities. |  [optional] |



## Enum: List&lt;FileTypeEnum&gt;

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;FILE_TYPE_UNSPECIFIED&quot; |
| CAMPAIGN | &quot;FILE_TYPE_CAMPAIGN&quot; |
| MEDIA_PRODUCT | &quot;FILE_TYPE_MEDIA_PRODUCT&quot; |
| INSERTION_ORDER | &quot;FILE_TYPE_INSERTION_ORDER&quot; |
| LINE_ITEM | &quot;FILE_TYPE_LINE_ITEM&quot; |
| AD_GROUP | &quot;FILE_TYPE_AD_GROUP&quot; |
| AD | &quot;FILE_TYPE_AD&quot; |



## Enum: FilterTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;FILTER_TYPE_UNSPECIFIED&quot; |
| NONE | &quot;FILTER_TYPE_NONE&quot; |
| ADVERTISER_ID | &quot;FILTER_TYPE_ADVERTISER_ID&quot; |
| CAMPAIGN_ID | &quot;FILTER_TYPE_CAMPAIGN_ID&quot; |
| MEDIA_PRODUCT_ID | &quot;FILTER_TYPE_MEDIA_PRODUCT_ID&quot; |
| INSERTION_ORDER_ID | &quot;FILTER_TYPE_INSERTION_ORDER_ID&quot; |
| LINE_ITEM_ID | &quot;FILTER_TYPE_LINE_ITEM_ID&quot; |



