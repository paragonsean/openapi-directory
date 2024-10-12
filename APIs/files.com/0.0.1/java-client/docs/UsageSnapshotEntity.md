

# UsageSnapshotEntity

List Usage Snapshots

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bytesSent** | **Double** | Transfer Usage for period - Outbound GB from Files Native Storage |  [optional] |
|**currentStorage** | **Double** | Current total Storage Usage GB as of end date (not necessarily high water mark, which is used for billing) |  [optional] |
|**deletedFilesCountedInMinimum** | **Double** | Storage Usage for files that are deleted but uploaded within last 30 days as of end date (not necessarily high water mark, which is used for billing) |  [optional] |
|**deletedFilesStorage** | **Double** | Storage Usage for files that are deleted but retained as backups as of end date (not necessarily high water mark, which is used for billing) |  [optional] |
|**endAt** | **OffsetDateTime** | Usage snapshot end date/time |  [optional] |
|**highWaterStorage** | **Double** | Highest Storage Usage GB recorded in time period (used for billing) |  [optional] |
|**highWaterUserCount** | **Double** | Highest user count number in time period |  [optional] |
|**id** | **Integer** | Usage snapshot ID |  [optional] |
|**rootStorage** | **Double** | Storage Usage for root folder as of end date (not necessarily high water mark, which is used for billing) |  [optional] |
|**startAt** | **OffsetDateTime** | Usage snapshot start date/time |  [optional] |
|**syncBytesReceived** | **Double** | Transfer Usage for period - Inbound GB to Remote Servers (Sync/Mount) |  [optional] |
|**syncBytesSent** | **Double** | Transfer Usage for period - Outbound GB from Remote Servers (Sync/Mount) |  [optional] |
|**totalBillableTransferUsage** | **Double** | Transfer usage for period - Total Billable amount |  [optional] |
|**totalBillableUsage** | **Double** | Storage + Transfer Usage - Total Billable amount |  [optional] |
|**usageByTopLevelDir** | **Object** | Storage Usage - map of root folders to their usage as of end date (not necessarily high water mark, which is used for billing) |  [optional] |



