

# LogSplit

Additional information used to correlate multiple log entries. Used when a single LogEntry would exceed the Google Cloud Logging size limit and is split across multiple log entries.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**index** | **Integer** | The index of this LogEntry in the sequence of split log entries. Log entries are given |index| values 0, 1, ..., n-1 for a sequence of n log entries. |  [optional] |
|**totalSplits** | **Integer** | The total number of log entries that the original LogEntry was split into. |  [optional] |
|**uid** | **String** | A globally unique identifier for all log entries in a sequence of split log entries. All log entries with the same |LogSplit.uid| are assumed to be part of the same sequence of split log entries. |  [optional] |



