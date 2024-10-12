# RubrikRestApi.DbLogReportProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enableDelayNotification** | **Boolean** | Indicates whether the database log backup delay notification is enabled. Set to &#39;true&#39; to send an email notification when the log backup delay is more than the configured threshold, and &#39;false&#39; to disable the behavior. | 
**logDelayNotificationFrequencyInMin** | **Number** | The frequency for sending an email notification to the customer when the log backup delay is more than the threshold. | 
**logDelayThresholdInMin** | **Number** | The threshold for the delay in log backup before an email notification should be created. | 


