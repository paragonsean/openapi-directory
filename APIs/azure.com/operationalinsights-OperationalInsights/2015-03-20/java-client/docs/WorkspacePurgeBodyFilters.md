

# WorkspacePurgeBodyFilters

User-defined filters to return data which will be purged from the table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**column** | **String** | The column of the table over which the given query should run |  [optional] |
|**key** | **String** | When filtering over custom dimensions, this key will be used as the name of the custom dimension. |  [optional] |
|**operator** | **String** | A query operator to evaluate over the provided column and value(s). Supported operators are &#x3D;&#x3D;, &#x3D;~, in, in~, &gt;, &gt;&#x3D;, &lt;, &lt;&#x3D;, between, and have the same behavior as they would in a KQL query. |  [optional] |
|**value** | **Object** | the value for the operator to function over. This can be a number (e.g., &gt; 100), a string (timestamp &gt;&#x3D; &#39;2017-09-01&#39;) or array of values. |  [optional] |



