# AmazonSimpleSystemsManagerSsm.Command

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commandId** | **String** |  | [optional] 
**documentName** | **String** |  | [optional] 
**documentVersion** | **String** |  | [optional] 
**comment** | **String** |  | [optional] 
**expiresAfter** | **Date** |  | [optional] 
**parameters** | **Object** |  | [optional] 
**instanceIds** | **Array** |  | [optional] 
**targets** | **Array** |  | [optional] 
**requestedDateTime** | **Date** |  | [optional] 
**status** | [**CommandStatus**](CommandStatus.md) |  | [optional] 
**statusDetails** | **String** |  | [optional] 
**outputS3Region** | **String** |  | [optional] 
**outputS3BucketName** | **String** |  | [optional] 
**outputS3KeyPrefix** | **String** |  | [optional] 
**maxConcurrency** | **String** |  | [optional] 
**maxErrors** | **String** |  | [optional] 
**targetCount** | **Number** |  | [optional] 
**completedCount** | **Number** |  | [optional] 
**errorCount** | **Number** |  | [optional] 
**deliveryTimedOutCount** | **Number** |  | [optional] 
**serviceRole** | **String** |  | [optional] 
**notificationConfig** | [**CommandNotificationConfig**](CommandNotificationConfig.md) |  | [optional] 
**cloudWatchOutputConfig** | [**CommandCloudWatchOutputConfig**](CommandCloudWatchOutputConfig.md) |  | [optional] 
**timeoutSeconds** | **Number** |  | [optional] 
**alarmConfiguration** | [**CommandAlarmConfiguration**](CommandAlarmConfiguration.md) |  | [optional] 
**triggeredAlarms** | **Array** |  | [optional] 


