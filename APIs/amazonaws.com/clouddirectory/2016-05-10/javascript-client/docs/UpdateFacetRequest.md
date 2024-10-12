# AmazonCloudDirectory.UpdateFacetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the facet. | 
**attributeUpdates** | [**[FacetAttributeUpdate]**](FacetAttributeUpdate.md) | List of attributes that need to be updated in a given schema &lt;a&gt;Facet&lt;/a&gt;. Each attribute is followed by &lt;code&gt;AttributeAction&lt;/code&gt;, which specifies the type of update operation to perform.  | [optional] 
**objectType** | **String** | The object type that is associated with the facet. See &lt;a&gt;CreateFacetRequest$ObjectType&lt;/a&gt; for more details. | [optional] 



## Enum: ObjectTypeEnum


* `NODE` (value: `"NODE"`)

* `LEAF_NODE` (value: `"LEAF_NODE"`)

* `POLICY` (value: `"POLICY"`)

* `INDEX` (value: `"INDEX"`)




