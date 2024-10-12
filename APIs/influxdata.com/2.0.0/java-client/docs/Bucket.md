

# Bucket


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**description** | **String** |  |  [optional] |
|**id** | **String** |  |  [optional] [readonly] |
|**labels** | [**List&lt;Label&gt;**](Label.md) |  |  [optional] |
|**links** | [**BucketLinks**](BucketLinks.md) |  |  [optional] |
|**name** | **String** |  |  |
|**orgID** | **String** |  |  [optional] |
|**retentionRules** | [**List&lt;RetentionRule&gt;**](RetentionRule.md) | Rules to expire or retain data.  No rules means data never expires. |  |
|**rp** | **String** |  |  [optional] |
|**schemaType** | **SchemaType** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] [readonly] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| USER | &quot;user&quot; |
| SYSTEM | &quot;system&quot; |



