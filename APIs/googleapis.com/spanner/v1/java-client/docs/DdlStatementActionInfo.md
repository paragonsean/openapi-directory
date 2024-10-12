

# DdlStatementActionInfo

Action information extracted from a DDL statement. This proto is used to display the brief info of the DDL statement for the operation UpdateDatabaseDdl.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | **String** | The action for the DDL statement, e.g. CREATE, ALTER, DROP, GRANT, etc. This field is a non-empty string. |  [optional] |
|**entityNames** | **List&lt;String&gt;** | The entity name(s) being operated on the DDL statement. E.g. 1. For statement \&quot;CREATE TABLE t1(...)\&quot;, &#x60;entity_names&#x60; &#x3D; [\&quot;t1\&quot;]. 2. For statement \&quot;GRANT ROLE r1, r2 ...\&quot;, &#x60;entity_names&#x60; &#x3D; [\&quot;r1\&quot;, \&quot;r2\&quot;]. 3. For statement \&quot;ANALYZE\&quot;, &#x60;entity_names&#x60; &#x3D; []. |  [optional] |
|**entityType** | **String** | The entity type for the DDL statement, e.g. TABLE, INDEX, VIEW, etc. This field can be empty string for some DDL statement, e.g. for statement \&quot;ANALYZE\&quot;, &#x60;entity_type&#x60; &#x3D; \&quot;\&quot;. |  [optional] |



