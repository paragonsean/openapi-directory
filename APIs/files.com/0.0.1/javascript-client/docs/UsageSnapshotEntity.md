# FilesComApi.UsageSnapshotEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytesSent** | **Number** | Transfer Usage for period - Outbound GB from Files Native Storage | [optional] 
**currentStorage** | **Number** | Current total Storage Usage GB as of end date (not necessarily high water mark, which is used for billing) | [optional] 
**deletedFilesCountedInMinimum** | **Number** | Storage Usage for files that are deleted but uploaded within last 30 days as of end date (not necessarily high water mark, which is used for billing) | [optional] 
**deletedFilesStorage** | **Number** | Storage Usage for files that are deleted but retained as backups as of end date (not necessarily high water mark, which is used for billing) | [optional] 
**endAt** | **Date** | Usage snapshot end date/time | [optional] 
**highWaterStorage** | **Number** | Highest Storage Usage GB recorded in time period (used for billing) | [optional] 
**highWaterUserCount** | **Number** | Highest user count number in time period | [optional] 
**id** | **Number** | Usage snapshot ID | [optional] 
**rootStorage** | **Number** | Storage Usage for root folder as of end date (not necessarily high water mark, which is used for billing) | [optional] 
**startAt** | **Date** | Usage snapshot start date/time | [optional] 
**syncBytesReceived** | **Number** | Transfer Usage for period - Inbound GB to Remote Servers (Sync/Mount) | [optional] 
**syncBytesSent** | **Number** | Transfer Usage for period - Outbound GB from Remote Servers (Sync/Mount) | [optional] 
**totalBillableTransferUsage** | **Number** | Transfer usage for period - Total Billable amount | [optional] 
**totalBillableUsage** | **Number** | Storage + Transfer Usage - Total Billable amount | [optional] 
**usageByTopLevelDir** | **Object** | Storage Usage - map of root folders to their usage as of end date (not necessarily high water mark, which is used for billing) | [optional] 


