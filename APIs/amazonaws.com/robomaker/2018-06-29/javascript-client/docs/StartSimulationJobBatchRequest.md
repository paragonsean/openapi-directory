# AwsRoboMaker.StartSimulationJobBatchRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientRequestToken** | **String** | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. | [optional] 
**batchPolicy** | [**StartSimulationJobBatchRequestBatchPolicy**](StartSimulationJobBatchRequestBatchPolicy.md) |  | [optional] 
**createSimulationJobRequests** | [**[SimulationJobRequest]**](SimulationJobRequest.md) | A list of simulation job requests to create in the batch. | 
**tags** | **{String: String}** | A map that contains tag keys and tag values that are attached to the deployment job batch. | [optional] 


