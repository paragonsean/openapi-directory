

# GoogleCloudAiplatformV1CompleteTrialRequest

Request message for VizierService.CompleteTrial.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**finalMeasurement** | [**GoogleCloudAiplatformV1Measurement**](GoogleCloudAiplatformV1Measurement.md) |  |  [optional] |
|**infeasibleReason** | **String** | Optional. A human readable reason why the trial was infeasible. This should only be provided if &#x60;trial_infeasible&#x60; is true. |  [optional] |
|**trialInfeasible** | **Boolean** | Optional. True if the Trial cannot be run with the given Parameter, and final_measurement will be ignored. |  [optional] |



