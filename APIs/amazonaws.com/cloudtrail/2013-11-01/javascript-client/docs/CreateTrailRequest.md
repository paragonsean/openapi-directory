# AwsCloudTrail.CreateTrailRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** |  | 
**s3BucketName** | **String** |  | 
**s3KeyPrefix** | **String** |  | [optional] 
**snsTopicName** | **String** |  | [optional] 
**includeGlobalServiceEvents** | **Boolean** |  | [optional] 
**isMultiRegionTrail** | **Boolean** |  | [optional] 
**enableLogFileValidation** | **Boolean** |  | [optional] 
**cloudWatchLogsLogGroupArn** | **String** |  | [optional] 
**cloudWatchLogsRoleArn** | **String** |  | [optional] 
**kmsKeyId** | **String** |  | [optional] 
**isOrganizationTrail** | **Boolean** |  | [optional] 
**tagsList** | [**[Tag]**](Tag.md) | A list of tags. | [optional] 


