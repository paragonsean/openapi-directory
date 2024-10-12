# PolicySimulatorApi.GoogleCloudPolicysimulatorV1alphaReplayResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessTuple** | [**GoogleCloudPolicysimulatorV1alphaAccessTuple**](GoogleCloudPolicysimulatorV1alphaAccessTuple.md) |  | [optional] 
**diff** | [**GoogleCloudPolicysimulatorV1alphaReplayDiff**](GoogleCloudPolicysimulatorV1alphaReplayDiff.md) |  | [optional] 
**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 
**lastSeenDate** | [**GoogleTypeDate**](GoogleTypeDate.md) |  | [optional] 
**name** | **String** | The resource name of the &#x60;ReplayResult&#x60;, in the following format: &#x60;{projects|folders|organizations}/{resource-id}/locations/global/replays/{replay-id}/results/{replay-result-id}&#x60;, where &#x60;{resource-id}&#x60; is the ID of the project, folder, or organization that owns the Replay. Example: &#x60;projects/my-example-project/locations/global/replays/506a5f7f-38ce-4d7d-8e03-479ce1833c36/results/1234&#x60; | [optional] 
**parent** | **String** | The Replay that the access tuple was included in. | [optional] 


