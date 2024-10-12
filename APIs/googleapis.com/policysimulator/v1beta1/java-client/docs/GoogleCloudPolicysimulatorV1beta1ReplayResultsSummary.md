

# GoogleCloudPolicysimulatorV1beta1ReplayResultsSummary

Summary statistics about the replayed log entries.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**differenceCount** | **Integer** | The number of replayed log entries with a difference between baseline and simulated policies. |  [optional] |
|**errorCount** | **Integer** | The number of log entries that could not be replayed. |  [optional] |
|**logCount** | **Integer** | The total number of log entries replayed. |  [optional] |
|**newestDate** | [**GoogleTypeDate**](GoogleTypeDate.md) |  |  [optional] |
|**oldestDate** | [**GoogleTypeDate**](GoogleTypeDate.md) |  |  [optional] |
|**unchangedCount** | **Integer** | The number of replayed log entries with no difference between baseline and simulated policies. |  [optional] |



