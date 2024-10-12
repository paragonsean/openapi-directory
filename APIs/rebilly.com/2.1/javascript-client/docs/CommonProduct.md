# RebillyRestApi.CommonProduct

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


