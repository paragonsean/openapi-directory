# AmazonKinesisVideoStreams.UpdateNotificationConfigurationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**streamName** | **String** | The name of the stream from which to update the notification configuration. You must specify either the &lt;code&gt;StreamName&lt;/code&gt; or the &lt;code&gt;StreamARN&lt;/code&gt;. | [optional] 
**streamARN** | **String** | The Amazon Resource Name (ARN) of the Kinesis video stream from where you want to update the notification configuration. You must specify either the &lt;code&gt;StreamName&lt;/code&gt; or the &lt;code&gt;StreamARN&lt;/code&gt;. | [optional] 
**notificationConfiguration** | [**UpdateNotificationConfigurationRequestNotificationConfiguration**](UpdateNotificationConfigurationRequestNotificationConfiguration.md) |  | [optional] 


