

# TailLogEntriesResponse

Result returned from TailLogEntries.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entries** | [**List&lt;LogEntry&gt;**](LogEntry.md) | A list of log entries. Each response in the stream will order entries with increasing values of LogEntry.timestamp. Ordering is not guaranteed between separate responses. |  [optional] |
|**suppressionInfo** | [**List&lt;SuppressionInfo&gt;**](SuppressionInfo.md) | If entries that otherwise would have been included in the session were not sent back to the client, counts of relevant entries omitted from the session with the reason that they were not included. There will be at most one of each reason per response. The counts represent the number of suppressed entries since the last streamed response. |  [optional] |



