

# ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptions

Optional arguments to enable specific features of builds.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**automapSubstitutions** | **Boolean** | Option to include built-in and custom substitutions as env variables for all build steps. |  [optional] |
|**defaultLogsBucketBehavior** | [**DefaultLogsBucketBehaviorEnum**](#DefaultLogsBucketBehaviorEnum) | Optional. Option to specify how default logs buckets are setup. |  [optional] |
|**diskSizeGb** | **String** | Requested disk size for the VM that runs the build. Note that this is *NOT* \&quot;disk free\&quot;; some of the space will be used by the operating system and build utilities. Also note that this is the minimum disk size that will be allocated for the build -- the build may run with a larger disk than requested. At present, the maximum disk size is 2000GB; builds that request more than the maximum are rejected with an error. |  [optional] |
|**dynamicSubstitutions** | **Boolean** | Option to specify whether or not to apply bash style string operations to the substitutions. NOTE: this is always enabled for triggered builds and cannot be overridden in the build configuration file. |  [optional] |
|**env** | **List&lt;String&gt;** | A list of global environment variable definitions that will exist for all build steps in this build. If a variable is defined in both globally and in a build step, the variable will use the build step value. The elements are of the form \&quot;KEY&#x3D;VALUE\&quot; for the environment variable \&quot;KEY\&quot; being given the value \&quot;VALUE\&quot;. |  [optional] |
|**logStreamingOption** | [**LogStreamingOptionEnum**](#LogStreamingOptionEnum) | Option to define build log streaming behavior to Cloud Storage. |  [optional] |
|**logging** | [**LoggingEnum**](#LoggingEnum) | Option to specify the logging mode, which determines if and where build logs are stored. |  [optional] |
|**machineType** | [**MachineTypeEnum**](#MachineTypeEnum) | Compute Engine machine type on which to run the build. |  [optional] |
|**pool** | [**ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOption**](ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOption.md) |  |  [optional] |
|**requestedVerifyOption** | [**RequestedVerifyOptionEnum**](#RequestedVerifyOptionEnum) | Requested verifiability options. |  [optional] |
|**secretEnv** | **List&lt;String&gt;** | A list of global environment variables, which are encrypted using a Cloud Key Management Service crypto key. These values must be specified in the build&#39;s &#x60;Secret&#x60;. These variables will be available to all build steps in this build. |  [optional] |
|**sourceProvenanceHash** | [**List&lt;SourceProvenanceHashEnum&gt;**](#List&lt;SourceProvenanceHashEnum&gt;) | Requested hash for SourceProvenance. |  [optional] |
|**substitutionOption** | [**SubstitutionOptionEnum**](#SubstitutionOptionEnum) | Option to specify behavior when there is an error in the substitution checks. NOTE: this is always set to ALLOW_LOOSE for triggered builds and cannot be overridden in the build configuration file. |  [optional] |
|**volumes** | [**List&lt;ContaineranalysisGoogleDevtoolsCloudbuildV1Volume&gt;**](ContaineranalysisGoogleDevtoolsCloudbuildV1Volume.md) | Global list of volumes to mount for ALL build steps Each volume is created as an empty volume prior to starting the build process. Upon completion of the build, volumes and their contents are discarded. Global volume names and paths cannot conflict with the volumes defined a build step. Using a global volume in a build with only one step is not valid as it is indicative of a build request with an incorrect configuration. |  [optional] |
|**workerPool** | **String** | This field deprecated; please use &#x60;pool.name&#x60; instead. |  [optional] |



## Enum: DefaultLogsBucketBehaviorEnum

| Name | Value |
|---- | -----|
| DEFAULT_LOGS_BUCKET_BEHAVIOR_UNSPECIFIED | &quot;DEFAULT_LOGS_BUCKET_BEHAVIOR_UNSPECIFIED&quot; |
| REGIONAL_USER_OWNED_BUCKET | &quot;REGIONAL_USER_OWNED_BUCKET&quot; |



## Enum: LogStreamingOptionEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;STREAM_DEFAULT&quot; |
| ON | &quot;STREAM_ON&quot; |
| OFF | &quot;STREAM_OFF&quot; |



## Enum: LoggingEnum

| Name | Value |
|---- | -----|
| LOGGING_UNSPECIFIED | &quot;LOGGING_UNSPECIFIED&quot; |
| LEGACY | &quot;LEGACY&quot; |
| GCS_ONLY | &quot;GCS_ONLY&quot; |
| STACKDRIVER_ONLY | &quot;STACKDRIVER_ONLY&quot; |
| CLOUD_LOGGING_ONLY | &quot;CLOUD_LOGGING_ONLY&quot; |
| NONE | &quot;NONE&quot; |



## Enum: MachineTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| N1_HIGHCPU_8 | &quot;N1_HIGHCPU_8&quot; |
| N1_HIGHCPU_32 | &quot;N1_HIGHCPU_32&quot; |
| E2_HIGHCPU_8 | &quot;E2_HIGHCPU_8&quot; |
| E2_HIGHCPU_32 | &quot;E2_HIGHCPU_32&quot; |
| E2_MEDIUM | &quot;E2_MEDIUM&quot; |



## Enum: RequestedVerifyOptionEnum

| Name | Value |
|---- | -----|
| NOT_VERIFIED | &quot;NOT_VERIFIED&quot; |
| VERIFIED | &quot;VERIFIED&quot; |



## Enum: List&lt;SourceProvenanceHashEnum&gt;

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| SHA256 | &quot;SHA256&quot; |
| MD5 | &quot;MD5&quot; |
| SHA512 | &quot;SHA512&quot; |



## Enum: SubstitutionOptionEnum

| Name | Value |
|---- | -----|
| MUST_MATCH | &quot;MUST_MATCH&quot; |
| ALLOW_LOOSE | &quot;ALLOW_LOOSE&quot; |



