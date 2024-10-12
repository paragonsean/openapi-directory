

# Metadata

Carries information about the pipeline execution that is returned in the long running operation's metadata field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | The time at which the operation was created by the API. |  [optional] |
|**endTime** | **String** | The time at which execution was completed and resources were cleaned up. |  [optional] |
|**events** | [**List&lt;Event&gt;**](Event.md) | The list of events that have happened so far during the execution of this operation. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The user-defined labels associated with this operation. |  [optional] |
|**pipeline** | [**Pipeline**](Pipeline.md) |  |  [optional] |
|**pubSubTopic** | **String** | The name of the Cloud Pub/Sub topic where notifications of operation status changes are sent. |  [optional] |
|**startTime** | **String** | The first time at which resources were allocated to execute the pipeline. |  [optional] |



