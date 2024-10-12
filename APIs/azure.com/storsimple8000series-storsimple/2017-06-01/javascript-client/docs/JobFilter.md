# StorSimple8000SeriesManagementClient.JobFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobType** | **String** | Specifies the type of the jobs to be filtered. For e.g., \&quot;ScheduledBackup\&quot;, \&quot;ManualBackup\&quot;, \&quot;RestoreBackup\&quot;, \&quot;CloneVolume\&quot;, \&quot;FailoverVolumeContainers\&quot;, \&quot;CreateLocallyPinnedVolume\&quot;, \&quot;ModifyVolume\&quot;, \&quot;InstallUpdates\&quot;, \&quot;SupportPackageLogs\&quot;, or \&quot;CreateCloudAppliance\&quot;. Only &#39;Equality&#39; operator can be used for this property. | [optional] 
**startTime** | **Date** | Specifies the start time of the jobs to be filtered.  Only &#39;Greater Than or Equal To&#39; and &#39;Lesser Than or Equal To&#39; operators are supported for this property. | [optional] 
**status** | **String** | Specifies the status of the jobs to be filtered. For e.g., \&quot;Running\&quot;, \&quot;Succeeded\&quot;, \&quot;Failed\&quot; or \&quot;Canceled\&quot;. Only &#39;Equality&#39; operator is supported for this property. | [optional] 


