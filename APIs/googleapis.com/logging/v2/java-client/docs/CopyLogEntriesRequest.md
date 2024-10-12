

# CopyLogEntriesRequest

The parameters to CopyLogEntries.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destination** | **String** | Required. Destination to which to copy log entries. |  [optional] |
|**filter** | **String** | Optional. A filter specifying which log entries to copy. The filter must be no more than 20k characters. An empty filter matches all log entries. |  [optional] |
|**name** | **String** | Required. Log bucket from which to copy log entries.For example:\&quot;projects/my-project/locations/global/buckets/my-source-bucket\&quot; |  [optional] |



