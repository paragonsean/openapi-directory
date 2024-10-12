# RebillyRestApi.Product

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdTime** | **Date** | The product created time. | [optional] [readonly] 
**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  | [optional] 
**description** | **String** | The product description. | [optional] 
**id** | **String** | The product ID. | [optional] [readonly] 
**name** | **String** | The product name. | 
**options** | **[String]** | The product options such as color, size, etc. The product options definition does not include option values. Those are defined within the plans.  | [optional] 
**requiresShipping** | **Boolean** | If the product requires shipping, shipping calculations will be applied. | [optional] 
**unitLabel** | **String** | The unit label, such as per &#x60;seat&#x60; or per &#x60;unit&#x60;. | [optional] [default to &#39;unit&#39;]
**updatedTime** | **Date** | The product updated time. | [optional] [readonly] 
**links** | [**[SelfLink]**](SelfLink.md) | The links related to resource. | [optional] [readonly] 
**accountingCode** | **String** | The product accounting code. | [optional] 
**taxCategoryId** | **String** | The product&#39;s tax category identifier string. | [optional] 



## Enum: TaxCategoryIdEnum


* `00000` (value: `"00000"`)

* `99999` (value: `"99999"`)

* `20010` (value: `"20010"`)

* `40030` (value: `"40030"`)

* `51020` (value: `"51020"`)

* `51010` (value: `"51010"`)

* `31000` (value: `"31000"`)

* `30070` (value: `"30070"`)




