# ContainerAnalysisApi.ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automapSubstitutions** | **Boolean** | Option to include built-in and custom substitutions as env variables for all build steps. | [optional] 
**defaultLogsBucketBehavior** | **String** | Optional. Option to specify how default logs buckets are setup. | [optional] 
**diskSizeGb** | **String** | Requested disk size for the VM that runs the build. Note that this is *NOT* \&quot;disk free\&quot;; some of the space will be used by the operating system and build utilities. Also note that this is the minimum disk size that will be allocated for the build -- the build may run with a larger disk than requested. At present, the maximum disk size is 2000GB; builds that request more than the maximum are rejected with an error. | [optional] 
**dynamicSubstitutions** | **Boolean** | Option to specify whether or not to apply bash style string operations to the substitutions. NOTE: this is always enabled for triggered builds and cannot be overridden in the build configuration file. | [optional] 
**env** | **[String]** | A list of global environment variable definitions that will exist for all build steps in this build. If a variable is defined in both globally and in a build step, the variable will use the build step value. The elements are of the form \&quot;KEY&#x3D;VALUE\&quot; for the environment variable \&quot;KEY\&quot; being given the value \&quot;VALUE\&quot;. | [optional] 
**logStreamingOption** | **String** | Option to define build log streaming behavior to Cloud Storage. | [optional] 
**logging** | **String** | Option to specify the logging mode, which determines if and where build logs are stored. | [optional] 
**machineType** | **String** | Compute Engine machine type on which to run the build. | [optional] 
**pool** | [**ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOption**](ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOption.md) |  | [optional] 
**requestedVerifyOption** | **String** | Requested verifiability options. | [optional] 
**secretEnv** | **[String]** | A list of global environment variables, which are encrypted using a Cloud Key Management Service crypto key. These values must be specified in the build&#39;s &#x60;Secret&#x60;. These variables will be available to all build steps in this build. | [optional] 
**sourceProvenanceHash** | **[String]** | Requested hash for SourceProvenance. | [optional] 
**substitutionOption** | **String** | Option to specify behavior when there is an error in the substitution checks. NOTE: this is always set to ALLOW_LOOSE for triggered builds and cannot be overridden in the build configuration file. | [optional] 
**volumes** | [**[ContaineranalysisGoogleDevtoolsCloudbuildV1Volume]**](ContaineranalysisGoogleDevtoolsCloudbuildV1Volume.md) | Global list of volumes to mount for ALL build steps Each volume is created as an empty volume prior to starting the build process. Upon completion of the build, volumes and their contents are discarded. Global volume names and paths cannot conflict with the volumes defined a build step. Using a global volume in a build with only one step is not valid as it is indicative of a build request with an incorrect configuration. | [optional] 
**workerPool** | **String** | This field deprecated; please use &#x60;pool.name&#x60; instead. | [optional] 



## Enum: DefaultLogsBucketBehaviorEnum


* `DEFAULT_LOGS_BUCKET_BEHAVIOR_UNSPECIFIED` (value: `"DEFAULT_LOGS_BUCKET_BEHAVIOR_UNSPECIFIED"`)

* `REGIONAL_USER_OWNED_BUCKET` (value: `"REGIONAL_USER_OWNED_BUCKET"`)





## Enum: LogStreamingOptionEnum


* `DEFAULT` (value: `"STREAM_DEFAULT"`)

* `ON` (value: `"STREAM_ON"`)

* `OFF` (value: `"STREAM_OFF"`)





## Enum: LoggingEnum


* `LOGGING_UNSPECIFIED` (value: `"LOGGING_UNSPECIFIED"`)

* `LEGACY` (value: `"LEGACY"`)

* `GCS_ONLY` (value: `"GCS_ONLY"`)

* `STACKDRIVER_ONLY` (value: `"STACKDRIVER_ONLY"`)

* `CLOUD_LOGGING_ONLY` (value: `"CLOUD_LOGGING_ONLY"`)

* `NONE` (value: `"NONE"`)





## Enum: MachineTypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `N1_HIGHCPU_8` (value: `"N1_HIGHCPU_8"`)

* `N1_HIGHCPU_32` (value: `"N1_HIGHCPU_32"`)

* `E2_HIGHCPU_8` (value: `"E2_HIGHCPU_8"`)

* `E2_HIGHCPU_32` (value: `"E2_HIGHCPU_32"`)

* `E2_MEDIUM` (value: `"E2_MEDIUM"`)





## Enum: RequestedVerifyOptionEnum


* `NOT_VERIFIED` (value: `"NOT_VERIFIED"`)

* `VERIFIED` (value: `"VERIFIED"`)





## Enum: [SourceProvenanceHashEnum]


* `NONE` (value: `"NONE"`)

* `SHA256` (value: `"SHA256"`)

* `MD5` (value: `"MD5"`)

* `SHA512` (value: `"SHA512"`)





## Enum: SubstitutionOptionEnum


* `MUST_MATCH` (value: `"MUST_MATCH"`)

* `ALLOW_LOOSE` (value: `"ALLOW_LOOSE"`)




