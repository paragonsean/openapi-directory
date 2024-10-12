# CloudProfilerApi.Profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment** | [**Deployment**](Deployment.md) |  | [optional] 
**duration** | **String** | Duration of the profiling session. Input (for the offline mode) or output (for the online mode). The field represents requested profiling duration. It may slightly differ from the effective profiling duration, which is recorded in the profile data, in case the profiling can&#39;t be stopped immediately (e.g. in case stopping the profiling is handled asynchronously). | [optional] 
**labels** | **{String: String}** | Input only. Labels associated to this specific profile. These labels will get merged with the deployment labels for the final data set. See documentation on deployment labels for validation rules and limits. | [optional] 
**name** | **String** | Output only. Opaque, server-assigned, unique ID for this profile. | [optional] [readonly] 
**profileBytes** | **Blob** | Input only. Profile bytes, as a gzip compressed serialized proto, the format is https://github.com/google/pprof/blob/master/proto/profile.proto. | [optional] 
**profileType** | **String** | Type of profile. For offline mode, this must be specified when creating the profile. For online mode it is assigned and returned by the server. | [optional] 
**startTime** | **String** | Output only. Start time for the profile. This output is only present in response from the ListProfiles method. | [optional] [readonly] 



## Enum: ProfileTypeEnum


* `PROFILE_TYPE_UNSPECIFIED` (value: `"PROFILE_TYPE_UNSPECIFIED"`)

* `CPU` (value: `"CPU"`)

* `WALL` (value: `"WALL"`)

* `HEAP` (value: `"HEAP"`)

* `THREADS` (value: `"THREADS"`)

* `CONTENTION` (value: `"CONTENTION"`)

* `PEAK_HEAP` (value: `"PEAK_HEAP"`)

* `HEAP_ALLOC` (value: `"HEAP_ALLOC"`)




