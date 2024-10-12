

# Product


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdTime** | **OffsetDateTime** | The product created time. |  [optional] [readonly] |
|**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  |  [optional] |
|**description** | **String** | The product description. |  [optional] |
|**id** | **String** | The product ID. |  [optional] [readonly] |
|**name** | **String** | The product name. |  |
|**options** | **List&lt;String&gt;** | The product options such as color, size, etc. The product options definition does not include option values. Those are defined within the plans.  |  [optional] |
|**requiresShipping** | **Boolean** | If the product requires shipping, shipping calculations will be applied. |  [optional] |
|**unitLabel** | **String** | The unit label, such as per &#x60;seat&#x60; or per &#x60;unit&#x60;. |  [optional] |
|**updatedTime** | **OffsetDateTime** | The product updated time. |  [optional] [readonly] |
|**links** | [**List&lt;SelfLink&gt;**](SelfLink.md) | The links related to resource. |  [optional] [readonly] |
|**accountingCode** | **String** | The product accounting code. |  [optional] |
|**taxCategoryId** | [**TaxCategoryIdEnum**](#TaxCategoryIdEnum) | The product&#39;s tax category identifier string. |  [optional] |



## Enum: TaxCategoryIdEnum

| Name | Value |
|---- | -----|
| _00000 | &quot;00000&quot; |
| _99999 | &quot;99999&quot; |
| _20010 | &quot;20010&quot; |
| _40030 | &quot;40030&quot; |
| _51020 | &quot;51020&quot; |
| _51010 | &quot;51010&quot; |
| _31000 | &quot;31000&quot; |
| _30070 | &quot;30070&quot; |



