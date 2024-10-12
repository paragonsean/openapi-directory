

# JobProperties

Job custom data details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activityId** | **String** | The activity id. |  [optional] |
|**allowedActions** | **List&lt;String&gt;** | The Allowed action the job. |  [optional] |
|**customDetails** | [**JobDetails**](JobDetails.md) |  |  [optional] |
|**endTime** | **OffsetDateTime** | The end time. |  [optional] |
|**errors** | [**List&lt;JobErrorDetails&gt;**](JobErrorDetails.md) | The errors. |  [optional] |
|**friendlyName** | **String** | The DisplayName. |  [optional] |
|**scenarioName** | **String** | The ScenarioName. |  [optional] |
|**startTime** | **OffsetDateTime** | The start time. |  [optional] |
|**state** | **String** | The status of the Job. It is one of these values - NotStarted, InProgress, Succeeded, Failed, Cancelled, Suspended or Other. |  [optional] |
|**stateDescription** | **String** | The description of the state of the Job. For e.g. - For Succeeded state, description can be Completed, PartiallySucceeded, CompletedWithInformation or Skipped. |  [optional] |
|**targetInstanceType** | **String** | The type of the affected object which is of {Microsoft.Azure.SiteRecovery.V2015_11_10.AffectedObjectType} class. |  [optional] |
|**targetObjectId** | **String** | The affected Object Id. |  [optional] |
|**targetObjectName** | **String** | The name of the affected object. |  [optional] |
|**tasks** | [**List&lt;ASRTask&gt;**](ASRTask.md) | The tasks. |  [optional] |



