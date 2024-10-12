

# RowAccessPolicy

Represents access on a subset of rows on the specified table, defined by its filter predicate. Access to the subset of rows is controlled by its IAM policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **String** | Output only. The time when this row access policy was created, in milliseconds since the epoch. |  [optional] [readonly] |
|**etag** | **String** | Output only. A hash of this resource. |  [optional] [readonly] |
|**filterPredicate** | **String** | Required. A SQL boolean expression that represents the rows defined by this row access policy, similar to the boolean expression in a WHERE clause of a SELECT query on a table. References to other tables, routines, and temporary functions are not supported. Examples: region&#x3D;\&quot;EU\&quot; date_field &#x3D; CAST(&#39;2019-9-27&#39; as DATE) nullable_field is not NULL numeric_field BETWEEN 1.0 AND 5.0 |  [optional] |
|**lastModifiedTime** | **String** | Output only. The time when this row access policy was last modified, in milliseconds since the epoch. |  [optional] [readonly] |
|**rowAccessPolicyReference** | [**RowAccessPolicyReference**](RowAccessPolicyReference.md) |  |  [optional] |



