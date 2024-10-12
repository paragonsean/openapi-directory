# ApigeeApi.GoogleCloudApigeeV1TraceConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **String** | Required. Endpoint of the exporter. | [optional] 
**exporter** | **String** | Required. Exporter that is used to view the distributed trace captured using OpenCensus. An exporter sends traces to any backend that is capable of consuming them. Recorded spans can be exported by registered exporters. | [optional] 
**samplingConfig** | [**GoogleCloudApigeeV1TraceSamplingConfig**](GoogleCloudApigeeV1TraceSamplingConfig.md) |  | [optional] 



## Enum: ExporterEnum


* `EXPORTER_UNSPECIFIED` (value: `"EXPORTER_UNSPECIFIED"`)

* `JAEGER` (value: `"JAEGER"`)

* `CLOUD_TRACE` (value: `"CLOUD_TRACE"`)




