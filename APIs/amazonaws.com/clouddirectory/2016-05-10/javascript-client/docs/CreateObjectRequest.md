# AmazonCloudDirectory.CreateObjectRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schemaFacets** | [**[SchemaFacet]**](SchemaFacet.md) | A list of schema facets to be associated with the object. Do not provide minor version components. See &lt;a&gt;SchemaFacet&lt;/a&gt; for details. | 
**objectAttributeList** | [**[AttributeKeyAndValue]**](AttributeKeyAndValue.md) | The attribute map whose attribute ARN contains the key and attribute value as the map value. | [optional] 
**parentReference** | [**AddFacetToObjectRequestObjectReference**](AddFacetToObjectRequestObjectReference.md) |  | [optional] 
**linkName** | **String** | The name of link that is used to attach this object to a parent. | [optional] 


