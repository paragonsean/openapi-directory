# ApigeeApi.GoogleCloudApigeeV1RuntimeTraceConfigOverride

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiProxy** | **String** | Name of the API proxy that will have its trace configuration overridden following format: &#x60;organizations/{org}/apis/{api}&#x60; | [optional] 
**name** | **String** | Name of the trace config override in the following format: &#x60;organizations/{org}/environment/{env}/traceConfig/overrides/{override}&#x60; | [optional] 
**revisionCreateTime** | **String** | The timestamp that the revision was created or updated. | [optional] 
**revisionId** | **String** | Revision number which can be used by the runtime to detect if the trace config override has changed between two versions. | [optional] 
**samplingConfig** | [**GoogleCloudApigeeV1RuntimeTraceSamplingConfig**](GoogleCloudApigeeV1RuntimeTraceSamplingConfig.md) |  | [optional] 
**uid** | **String** | Unique ID for the configuration override. The ID will only change if the override is deleted and recreated. Corresponds to name&#39;s \&quot;override\&quot; field. | [optional] 


