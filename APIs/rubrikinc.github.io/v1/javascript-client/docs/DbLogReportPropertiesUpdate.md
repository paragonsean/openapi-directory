# RubrikRestApi.DbLogReportPropertiesUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enableDelayNotification** | **Boolean** | Indicates whether the database log backup delay notification is enabled. Set to &#39;true&#39; to send an email notification when the log backup delay is more than the configured threshold, and &#39;false&#39; to disable the behavior. | [optional] 
**logDelayNotificationFrequencyInMin** | **Number** | An integer that specifies an interval in minutes. Email notifications about the log backup delay exceeding the specified threshold are sent at a maximum frequency specified by the interval. | [optional] 
**logDelayThresholdInMin** | **Number** | An integer that specifies an interval in minutes. The CDM cluster sends an email notification when a log backup is delayed for longer than the specified interval. | [optional] 


