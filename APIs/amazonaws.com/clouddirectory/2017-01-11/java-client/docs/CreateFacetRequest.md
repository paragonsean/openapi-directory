

# CreateFacetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the &lt;a&gt;Facet&lt;/a&gt;, which is unique for a given schema. |  |
|**attributes** | [**List&lt;FacetAttribute&gt;**](FacetAttribute.md) | The attributes that are associated with the &lt;a&gt;Facet&lt;/a&gt;. |  [optional] |
|**objectType** | [**ObjectTypeEnum**](#ObjectTypeEnum) | &lt;p&gt;Specifies whether a given object created from this facet is of type node, leaf node, policy or index.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Node: Can have multiple children but one parent.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Leaf node: Cannot have children but can have multiple parents.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Policy: Allows you to store a policy document and policy type. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies\&quot;&gt;Policies&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Index: Can be created with the Index API.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**facetStyle** | [**FacetStyleEnum**](#FacetStyleEnum) | There are two different styles that you can define on any given facet, &lt;code&gt;Static&lt;/code&gt; and &lt;code&gt;Dynamic&lt;/code&gt;. For static facets, all attributes must be defined in the schema. For dynamic facets, attributes can be defined during data plane operations. |  [optional] |



## Enum: ObjectTypeEnum

| Name | Value |
|---- | -----|
| NODE | &quot;NODE&quot; |
| LEAF_NODE | &quot;LEAF_NODE&quot; |
| POLICY | &quot;POLICY&quot; |
| INDEX | &quot;INDEX&quot; |



## Enum: FacetStyleEnum

| Name | Value |
|---- | -----|
| STATIC | &quot;STATIC&quot; |
| DYNAMIC | &quot;DYNAMIC&quot; |



