

# GoogleCloudApigeeV1RuntimeTraceConfig

NEXT ID: 8 RuntimeTraceConfig defines the configurations for distributed trace in an environment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endpoint** | **String** | Endpoint of the exporter. |  [optional] |
|**exporter** | [**ExporterEnum**](#ExporterEnum) | Exporter that is used to view the distributed trace captured using OpenCensus. An exporter sends traces to any backend that is capable of consuming them. Recorded spans can be exported by registered exporters. |  [optional] |
|**name** | **String** | Name of the trace config in the following format: &#x60;organizations/{org}/environment/{env}/traceConfig&#x60; |  [optional] |
|**overrides** | [**List&lt;GoogleCloudApigeeV1RuntimeTraceConfigOverride&gt;**](GoogleCloudApigeeV1RuntimeTraceConfigOverride.md) | List of trace configuration overrides for spicific API proxies. |  [optional] |
|**revisionCreateTime** | **String** | The timestamp that the revision was created or updated. |  [optional] |
|**revisionId** | **String** | Revision number which can be used by the runtime to detect if the trace config has changed between two versions. |  [optional] |
|**samplingConfig** | [**GoogleCloudApigeeV1RuntimeTraceSamplingConfig**](GoogleCloudApigeeV1RuntimeTraceSamplingConfig.md) |  |  [optional] |



## Enum: ExporterEnum

| Name | Value |
|---- | -----|
| EXPORTER_UNSPECIFIED | &quot;EXPORTER_UNSPECIFIED&quot; |
| JAEGER | &quot;JAEGER&quot; |
| CLOUD_TRACE | &quot;CLOUD_TRACE&quot; |



