# AmazonCloudWatchEvidently.UpdateLaunchRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | An optional description for the launch. | [optional] 
**groups** | [**[LaunchGroupConfig]**](LaunchGroupConfig.md) | An array of structures that contains the feature and variations that are to be used for the launch. | [optional] 
**metricMonitors** | [**[MetricMonitorConfig]**](MetricMonitorConfig.md) | An array of structures that define the metrics that will be used to monitor the launch performance. | [optional] 
**randomizationSalt** | **String** | When Evidently assigns a particular user session to a launch, it must use a randomization ID to determine which variation the user session is served. This randomization ID is a combination of the entity ID and &lt;code&gt;randomizationSalt&lt;/code&gt;. If you omit &lt;code&gt;randomizationSalt&lt;/code&gt;, Evidently uses the launch name as the &lt;code&gt;randomizationSalt&lt;/code&gt;. | [optional] 
**scheduledSplitsConfig** | [**CreateLaunchRequestScheduledSplitsConfig**](CreateLaunchRequestScheduledSplitsConfig.md) |  | [optional] 


