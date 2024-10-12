

# ChaosSchedule

Defines the schedule used by Chaos.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chaosParametersDictionary** | [**List&lt;ChaosParametersDictionaryItem&gt;**](ChaosParametersDictionaryItem.md) | A mapping of string names to Chaos Parameters to be referenced by Chaos Schedule Jobs. |  [optional] |
|**expiryDate** | **OffsetDateTime** | The date and time Chaos will continue to use this schedule until. |  [optional] |
|**jobs** | [**List&lt;ChaosScheduleJob&gt;**](ChaosScheduleJob.md) | A list of all Chaos Schedule Jobs that will be automated by the schedule. |  [optional] |
|**startDate** | **OffsetDateTime** | The date and time Chaos will start using this schedule. |  [optional] |



