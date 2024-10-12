

# StartSimulationJobBatchRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientRequestToken** | **String** | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. |  [optional] |
|**batchPolicy** | [**StartSimulationJobBatchRequestBatchPolicy**](StartSimulationJobBatchRequestBatchPolicy.md) |  |  [optional] |
|**createSimulationJobRequests** | [**List&lt;SimulationJobRequest&gt;**](SimulationJobRequest.md) | A list of simulation job requests to create in the batch. |  |
|**tags** | **Map&lt;String, String&gt;** | A map that contains tag keys and tag values that are attached to the deployment job batch. |  [optional] |



