

# Item

Represents item metadata added to an Items dataset using the <code>PutItems</code> API. For more information see <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/importing-items.html\">Importing Items Incrementally</a>. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**itemId** | [**String**](String.md) |  |  |
|**properties** | **Object** | &lt;p&gt;A string map of item-specific metadata. Each element in the map consists of a key-value pair. For example, &lt;code&gt;{\&quot;numberOfRatings\&quot;: \&quot;12\&quot;}&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The keys use camel case names that match the fields in the schema for the Items dataset. In the previous example, the &lt;code&gt;numberOfRatings&lt;/code&gt; matches the &#39;NUMBER_OF_RATINGS&#39; field defined in the Items schema. For categorical string data, to include multiple categories for a single item, separate each category with a pipe separator (&lt;code&gt;|&lt;/code&gt;). For example, &lt;code&gt;\\\&quot;Horror|Action\\\&quot;&lt;/code&gt;.&lt;/p&gt; |  [optional] |



