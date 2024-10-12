# InfluxOssApiService.Bucket

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** |  | [optional] [readonly] 
**description** | **String** |  | [optional] 
**id** | **String** |  | [optional] [readonly] 
**labels** | [**[Label]**](Label.md) |  | [optional] 
**links** | [**BucketLinks**](BucketLinks.md) |  | [optional] 
**name** | **String** |  | 
**orgID** | **String** |  | [optional] 
**retentionRules** | [**[RetentionRule]**](RetentionRule.md) | Rules to expire or retain data.  No rules means data never expires. | 
**rp** | **String** |  | [optional] 
**schemaType** | [**SchemaType**](SchemaType.md) |  | [optional] 
**type** | **String** |  | [optional] [readonly] [default to &#39;user&#39;]
**updatedAt** | **Date** |  | [optional] [readonly] 



## Enum: TypeEnum


* `user` (value: `"user"`)

* `system` (value: `"system"`)




