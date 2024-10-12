

# User

Represents user metadata added to a Users dataset using the <code>PutUsers</code> API. For more information see <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/importing-users.html\">Importing Users Incrementally</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**userId** | [**String**](String.md) |  |  |
|**properties** | **Object** | &lt;p&gt;A string map of user-specific metadata. Each element in the map consists of a key-value pair. For example, &lt;code&gt;{\&quot;numberOfVideosWatched\&quot;: \&quot;45\&quot;}&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;The keys use camel case names that match the fields in the schema for the Users dataset. In the previous example, the &lt;code&gt;numberOfVideosWatched&lt;/code&gt; matches the &#39;NUMBER_OF_VIDEOS_WATCHED&#39; field defined in the Users schema. For categorical string data, to include multiple categories for a single user, separate each category with a pipe separator (&lt;code&gt;|&lt;/code&gt;). For example, &lt;code&gt;\\\&quot;Member|Frequent shopper\\\&quot;&lt;/code&gt;.&lt;/p&gt; |  [optional] |



