

# UpdateFacetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the facet. |  |
|**attributeUpdates** | [**List&lt;FacetAttributeUpdate&gt;**](FacetAttributeUpdate.md) | List of attributes that need to be updated in a given schema &lt;a&gt;Facet&lt;/a&gt;. Each attribute is followed by &lt;code&gt;AttributeAction&lt;/code&gt;, which specifies the type of update operation to perform.  |  [optional] |
|**objectType** | [**ObjectTypeEnum**](#ObjectTypeEnum) | The object type that is associated with the facet. See &lt;a&gt;CreateFacetRequest$ObjectType&lt;/a&gt; for more details. |  [optional] |



## Enum: ObjectTypeEnum

| Name | Value |
|---- | -----|
| NODE | &quot;NODE&quot; |
| LEAF_NODE | &quot;LEAF_NODE&quot; |
| POLICY | &quot;POLICY&quot; |
| INDEX | &quot;INDEX&quot; |



