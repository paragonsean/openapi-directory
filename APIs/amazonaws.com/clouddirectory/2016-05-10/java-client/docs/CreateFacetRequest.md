

# CreateFacetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the &lt;a&gt;Facet&lt;/a&gt;, which is unique for a given schema. |  |
|**attributes** | [**List&lt;FacetAttribute&gt;**](FacetAttribute.md) | The attributes that are associated with the &lt;a&gt;Facet&lt;/a&gt;. |  [optional] |
|**objectType** | [**ObjectTypeEnum**](#ObjectTypeEnum) | &lt;p&gt;Specifies whether a given object created from this facet is of type node, leaf node, policy or index.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Node: Can have multiple children but one parent.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Leaf node: Cannot have children but can have multiple parents.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Policy: Allows you to store a policy document and policy type. For more information, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/directoryservice/latest/admin-guide/cd_key_concepts.html#policies\&quot;&gt;Policies&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Index: Can be created with the Index API.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  |



## Enum: ObjectTypeEnum

| Name | Value |
|---- | -----|
| NODE | &quot;NODE&quot; |
| LEAF_NODE | &quot;LEAF_NODE&quot; |
| POLICY | &quot;POLICY&quot; |
| INDEX | &quot;INDEX&quot; |



