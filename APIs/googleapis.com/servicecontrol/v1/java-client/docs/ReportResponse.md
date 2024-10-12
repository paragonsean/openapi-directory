

# ReportResponse

Response message for the Report method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reportErrors** | [**List&lt;ReportError&gt;**](ReportError.md) | Partial failures, one for each &#x60;Operation&#x60; in the request that failed processing. There are three possible combinations of the RPC status: 1. The combination of a successful RPC status and an empty &#x60;report_errors&#x60; list indicates a complete success where all &#x60;Operations&#x60; in the request are processed successfully. 2. The combination of a successful RPC status and a non-empty &#x60;report_errors&#x60; list indicates a partial success where some &#x60;Operations&#x60; in the request succeeded. Each &#x60;Operation&#x60; that failed processing has a corresponding item in this list. 3. A failed RPC status indicates a general non-deterministic failure. When this happens, it&#39;s impossible to know which of the &#39;Operations&#39; in the request succeeded or failed. |  [optional] |
|**serviceConfigId** | **String** | The actual config id used to process the request. |  [optional] |
|**serviceRolloutId** | **String** | The current service rollout id used to process the request. |  [optional] |



