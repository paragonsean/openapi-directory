

# InventoryCategory


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archived** | **Boolean** | If the category is archived or not |  [optional] |
|**categoryType** | [**CategoryTypeEnum**](#CategoryTypeEnum) | Can be one of &#x60;\&quot;vaccine\&quot;&#x60;, &#x60;\&quot;product\&quot;&#x60; or &#x60;\&quot;service\&quot;&#x60; |  [optional] |
|**createdAt** | **String** |  |  [optional] [readonly] |
|**doctor** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**name** | **String** | Name of the inventory category |  [optional] |
|**updatedAt** | **String** |  |  [optional] [readonly] |



## Enum: CategoryTypeEnum

| Name | Value |
|---- | -----|
| VACCINE | &quot;vaccine&quot; |
| PRODUCT | &quot;product&quot; |
| SERVICE | &quot;service&quot; |



