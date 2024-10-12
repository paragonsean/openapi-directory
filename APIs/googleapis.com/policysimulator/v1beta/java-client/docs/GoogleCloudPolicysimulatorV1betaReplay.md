

# GoogleCloudPolicysimulatorV1betaReplay

A resource describing a `Replay`, or simulation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**config** | [**GoogleCloudPolicysimulatorV1betaReplayConfig**](GoogleCloudPolicysimulatorV1betaReplayConfig.md) |  |  [optional] |
|**name** | **String** | Output only. The resource name of the &#x60;Replay&#x60;, which has the following format: &#x60;{projects|folders|organizations}/{resource-id}/locations/global/replays/{replay-id}&#x60;, where &#x60;{resource-id}&#x60; is the ID of the project, folder, or organization that owns the Replay. Example: &#x60;projects/my-example-project/locations/global/replays/506a5f7f-38ce-4d7d-8e03-479ce1833c36&#x60; |  [optional] [readonly] |
|**resultsSummary** | [**GoogleCloudPolicysimulatorV1betaReplayResultsSummary**](GoogleCloudPolicysimulatorV1betaReplayResultsSummary.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of the &#x60;Replay&#x60;. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |



