

# GoogleCloudApigeeV1TraceConfig

TraceConfig defines the configurations in an environment of distributed trace.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endpoint** | **String** | Required. Endpoint of the exporter. |  [optional] |
|**exporter** | [**ExporterEnum**](#ExporterEnum) | Required. Exporter that is used to view the distributed trace captured using OpenCensus. An exporter sends traces to any backend that is capable of consuming them. Recorded spans can be exported by registered exporters. |  [optional] |
|**samplingConfig** | [**GoogleCloudApigeeV1TraceSamplingConfig**](GoogleCloudApigeeV1TraceSamplingConfig.md) |  |  [optional] |



## Enum: ExporterEnum

| Name | Value |
|---- | -----|
| EXPORTER_UNSPECIFIED | &quot;EXPORTER_UNSPECIFIED&quot; |
| JAEGER | &quot;JAEGER&quot; |
| CLOUD_TRACE | &quot;CLOUD_TRACE&quot; |



