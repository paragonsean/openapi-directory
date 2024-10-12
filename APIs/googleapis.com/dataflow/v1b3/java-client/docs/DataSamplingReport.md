

# DataSamplingReport

Contains per-worker telemetry about the data sampling feature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bytesWrittenDelta** | **String** | Optional. Delta of bytes written to file from previous report. |  [optional] |
|**elementsSampledBytes** | **String** | Optional. Delta of bytes sampled from previous report. |  [optional] |
|**elementsSampledCount** | **String** | Optional. Delta of number of elements sampled from previous report. |  [optional] |
|**exceptionsSampledCount** | **String** | Optional. Delta of number of samples taken from user code exceptions from previous report. |  [optional] |
|**pcollectionsSampledCount** | **String** | Optional. Delta of number of PCollections sampled from previous report. |  [optional] |
|**persistenceErrorsCount** | **String** | Optional. Delta of errors counts from persisting the samples from previous report. |  [optional] |
|**translationErrorsCount** | **String** | Optional. Delta of errors counts from retrieving, or translating the samples from previous report. |  [optional] |



