# WebSiteManagementClient.FileSystemHttpLogsConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Boolean** | Enabled | [optional] 
**retentionInDays** | **Number** | Retention in days.              Remove files older than X days.              0 or lower means no retention. | [optional] 
**retentionInMb** | **Number** | Maximum size in megabytes that http log files can use.              When reached old log files will be removed to make space for new ones.              Value can range between 25 and 100. | [optional] 


