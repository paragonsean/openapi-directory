# ApigeeApi.GoogleCloudApigeeV1RuntimeTraceConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **String** | Endpoint of the exporter. | [optional] 
**exporter** | **String** | Exporter that is used to view the distributed trace captured using OpenCensus. An exporter sends traces to any backend that is capable of consuming them. Recorded spans can be exported by registered exporters. | [optional] 
**name** | **String** | Name of the trace config in the following format: &#x60;organizations/{org}/environment/{env}/traceConfig&#x60; | [optional] 
**overrides** | [**[GoogleCloudApigeeV1RuntimeTraceConfigOverride]**](GoogleCloudApigeeV1RuntimeTraceConfigOverride.md) | List of trace configuration overrides for spicific API proxies. | [optional] 
**revisionCreateTime** | **String** | The timestamp that the revision was created or updated. | [optional] 
**revisionId** | **String** | Revision number which can be used by the runtime to detect if the trace config has changed between two versions. | [optional] 
**samplingConfig** | [**GoogleCloudApigeeV1RuntimeTraceSamplingConfig**](GoogleCloudApigeeV1RuntimeTraceSamplingConfig.md) |  | [optional] 



## Enum: ExporterEnum


* `EXPORTER_UNSPECIFIED` (value: `"EXPORTER_UNSPECIFIED"`)

* `JAEGER` (value: `"JAEGER"`)

* `CLOUD_TRACE` (value: `"CLOUD_TRACE"`)




