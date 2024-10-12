

# GoogleCloudAiplatformV1beta1StudySpecDecayCurveAutomatedStoppingSpec

The decay curve automated stopping rule builds a Gaussian Process Regressor to predict the final objective value of a Trial based on the already completed Trials and the intermediate measurements of the current Trial. Early stopping is requested for the current Trial if there is very low probability to exceed the optimal value found so far.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**useElapsedDuration** | **Boolean** | True if Measurement.elapsed_duration is used as the x-axis of each Trials Decay Curve. Otherwise, Measurement.step_count will be used as the x-axis. |  [optional] |



