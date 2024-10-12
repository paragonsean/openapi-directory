# AiPlatformTrainingPredictionApi.GoogleCloudMlV1CompleteTrialRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finalMeasurement** | [**GoogleCloudMlV1Measurement**](GoogleCloudMlV1Measurement.md) |  | [optional] 
**infeasibleReason** | **String** | Optional. A human readable reason why the trial was infeasible. This should only be provided if &#x60;trial_infeasible&#x60; is true. | [optional] 
**trialInfeasible** | **Boolean** | Optional. True if the trial cannot be run with the given Parameter, and final_measurement will be ignored. | [optional] 


