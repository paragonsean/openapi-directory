

# Field

Message representing a single field of a struct.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the field. For reads, this is the column name. For SQL queries, it is the column alias (e.g., &#x60;\&quot;Word\&quot;&#x60; in the query &#x60;\&quot;SELECT &#39;hello&#39; AS Word\&quot;&#x60;), or the column name (e.g., &#x60;\&quot;ColName\&quot;&#x60; in the query &#x60;\&quot;SELECT ColName FROM Table\&quot;&#x60;). Some columns might have an empty name (e.g., &#x60;\&quot;SELECT UPPER(ColName)\&quot;&#x60;). Note that a query result can contain multiple fields with the same name. |  [optional] |
|**type** | [**Type**](Type.md) |  |  [optional] |



