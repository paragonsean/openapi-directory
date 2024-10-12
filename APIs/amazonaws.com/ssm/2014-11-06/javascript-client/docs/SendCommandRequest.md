# AmazonSimpleSystemsManagerSsm.SendCommandRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instanceIds** | **Array** |  | [optional] 
**targets** | **Array** |  | [optional] 
**documentName** | **String** |  | 
**documentVersion** | **String** |  | [optional] 
**documentHash** | **String** |  | [optional] 
**documentHashType** | [**DocumentHashType**](DocumentHashType.md) |  | [optional] 
**timeoutSeconds** | **Number** |  | [optional] 
**comment** | **String** |  | [optional] 
**parameters** | **Object** |  | [optional] 
**outputS3Region** | **String** |  | [optional] 
**outputS3BucketName** | **String** |  | [optional] 
**outputS3KeyPrefix** | **String** |  | [optional] 
**maxConcurrency** | **String** |  | [optional] 
**maxErrors** | **String** |  | [optional] 
**serviceRoleArn** | **String** |  | [optional] 
**notificationConfig** | [**SendCommandRequestNotificationConfig**](SendCommandRequestNotificationConfig.md) |  | [optional] 
**cloudWatchOutputConfig** | [**SendCommandRequestCloudWatchOutputConfig**](SendCommandRequestCloudWatchOutputConfig.md) |  | [optional] 
**alarmConfiguration** | [**SendCommandRequestAlarmConfiguration**](SendCommandRequestAlarmConfiguration.md) |  | [optional] 


