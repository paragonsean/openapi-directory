# DisplayVideo360Api.ParentEntityFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fileType** | **[String]** | Required. File types that will be returned. | [optional] 
**filterIds** | **[String]** | The IDs of the specified filter type. This is used to filter entities to fetch. If filter type is not &#x60;FILTER_TYPE_NONE&#x60;, at least one ID must be specified. | [optional] 
**filterType** | **String** | Required. Filter type used to filter fetched entities. | [optional] 



## Enum: [FileTypeEnum]


* `UNSPECIFIED` (value: `"FILE_TYPE_UNSPECIFIED"`)

* `CAMPAIGN` (value: `"FILE_TYPE_CAMPAIGN"`)

* `MEDIA_PRODUCT` (value: `"FILE_TYPE_MEDIA_PRODUCT"`)

* `INSERTION_ORDER` (value: `"FILE_TYPE_INSERTION_ORDER"`)

* `LINE_ITEM` (value: `"FILE_TYPE_LINE_ITEM"`)

* `AD_GROUP` (value: `"FILE_TYPE_AD_GROUP"`)

* `AD` (value: `"FILE_TYPE_AD"`)





## Enum: FilterTypeEnum


* `UNSPECIFIED` (value: `"FILTER_TYPE_UNSPECIFIED"`)

* `NONE` (value: `"FILTER_TYPE_NONE"`)

* `ADVERTISER_ID` (value: `"FILTER_TYPE_ADVERTISER_ID"`)

* `CAMPAIGN_ID` (value: `"FILTER_TYPE_CAMPAIGN_ID"`)

* `MEDIA_PRODUCT_ID` (value: `"FILTER_TYPE_MEDIA_PRODUCT_ID"`)

* `INSERTION_ORDER_ID` (value: `"FILTER_TYPE_INSERTION_ORDER_ID"`)

* `LINE_ITEM_ID` (value: `"FILTER_TYPE_LINE_ITEM_ID"`)




