

# ChannelCatalogMarketplaceProperty

Model for fetching a channel catalog marketplace property

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Indicate the description of the property |  [optional] |
|**discriminatorType** | **ChannelCatalogMarketplacePropertyDiscriminatorType** |  |  |
|**info** | [**BeezUPCommonInfoSummaries**](BeezUPCommonInfoSummaries.md) |  |  [optional] |
|**lovLink** | [**BeezUPCommonLOVLink3**](BeezUPCommonLOVLink3.md) |  |  [optional] |
|**lovRequired** | **Boolean** | Indicates if the property value must be in the list of value. |  [optional] |
|**maxItems** | **Integer** | Indicates the maximum item count of the property value |  [optional] |
|**maxLength** | **Integer** | Indicates the maximum size of the property value |  [optional] |
|**minItems** | **Integer** | Indicates the minimum item count of the property value. |  [optional] |
|**minLength** | **Integer** | Indicates the minimum size of the property value |  [optional] |
|**name** | **String** | Channel catalog marketplace property name |  |
|**offerIdRequired** | **Integer** | Indicates the offer identifier required to configure this property. |  [optional] |
|**pattern** | **String** | Channel catalog marketplace setting value format validation regular expression |  [optional] |
|**position** | **Integer** | Indicate the position of the property in the display group |  |
|**readOnly** | **Boolean** | Indicate if the value cannot be changed. This is used for example for ebay token that should not be changed. |  |
|**required** | **Boolean** | Indicate if the property is required or not |  |
|**type** | **Type** |  |  |
|**visible** | **Boolean** | Indicates if this property should be displayed in the configuration page. |  |



