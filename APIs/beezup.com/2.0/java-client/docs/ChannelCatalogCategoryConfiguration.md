

# ChannelCatalogCategoryConfiguration

Represent a mapping between a catalog category path and a channel category path. The cost on this mapping can be applied. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoMapNewSubCategories** | **Boolean** | Great feature! In case of mapping to parent catalog category, you can ask to automatically map new sub catalog category in the next importation to this channel category path. |  |
|**catalogCategoryPath** | **List&lt;String&gt;** | The catalog category path |  |
|**channelCategoryPath** | **List&lt;String&gt;** | The channel category path |  [optional] |
|**costValue** | **BigDecimal** | In case of CPC_ByCategory or CPA_ByCategory cost type, you have to indicate the cost value. |  [optional] |



