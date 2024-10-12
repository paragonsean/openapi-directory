# PolicySimulatorApi.GoogleCloudPolicysimulatorV1Replay

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**GoogleCloudPolicysimulatorV1ReplayConfig**](GoogleCloudPolicysimulatorV1ReplayConfig.md) |  | [optional] 
**name** | **String** | Output only. The resource name of the &#x60;Replay&#x60;, which has the following format: &#x60;{projects|folders|organizations}/{resource-id}/locations/global/replays/{replay-id}&#x60;, where &#x60;{resource-id}&#x60; is the ID of the project, folder, or organization that owns the Replay. Example: &#x60;projects/my-example-project/locations/global/replays/506a5f7f-38ce-4d7d-8e03-479ce1833c36&#x60; | [optional] [readonly] 
**resultsSummary** | [**GoogleCloudPolicysimulatorV1ReplayResultsSummary**](GoogleCloudPolicysimulatorV1ReplayResultsSummary.md) |  | [optional] 
**state** | **String** | Output only. The current state of the &#x60;Replay&#x60;. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `RUNNING` (value: `"RUNNING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)




