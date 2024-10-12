

# DateOptions

Options for a date field. Dates and times are specified in UTC (Coordinated Universal Time) according to IETF RFC3339: yyyy-mm-ddT00:00:00Z. Present if <code>IndexFieldType</code> specifies the field is of type <code>date</code>. All options are enabled by default.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultValue** | [**String**](String.md) |  |  [optional] |
|**sourceField** | **String** | &lt;p&gt;A string that represents the name of an index field. CloudSearch supports regular index fields as well as dynamic fields. A dynamic field&#39;s name defines a pattern that begins or ends with a wildcard. Any document fields that don&#39;t map to a regular index field but do match a dynamic field&#39;s pattern are configured with the dynamic field&#39;s indexing options. &lt;/p&gt; &lt;p&gt;Regular field names begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards, and wildcards embedded within a string are not supported. &lt;/p&gt; &lt;p&gt;The name &lt;code&gt;score&lt;/code&gt; is reserved and cannot be used as a field name. To reference a document&#39;s ID, you can use the name &lt;code&gt;_id&lt;/code&gt;. &lt;/p&gt; |  [optional] |
|**facetEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**searchEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**returnEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**sortEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |



