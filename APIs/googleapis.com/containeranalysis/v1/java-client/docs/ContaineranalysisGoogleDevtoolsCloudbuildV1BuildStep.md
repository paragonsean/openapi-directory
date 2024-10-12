

# ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStep

A step in the build pipeline.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowExitCodes** | **List&lt;Integer&gt;** | Allow this build step to fail without failing the entire build if and only if the exit code is one of the specified codes. If allow_failure is also specified, this field will take precedence. |  [optional] |
|**allowFailure** | **Boolean** | Allow this build step to fail without failing the entire build. If false, the entire build will fail if this step fails. Otherwise, the build will succeed, but this step will still have a failure status. Error information will be reported in the failure_detail field. |  [optional] |
|**args** | **List&lt;String&gt;** | A list of arguments that will be presented to the step when it is started. If the image used to run the step&#39;s container has an entrypoint, the &#x60;args&#x60; are used as arguments to that entrypoint. If the image does not define an entrypoint, the first element in args is used as the entrypoint, and the remainder will be used as arguments. |  [optional] |
|**automapSubstitutions** | **Boolean** | Option to include built-in and custom substitutions as env variables for this build step. This option will override the global option in BuildOption. |  [optional] |
|**dir** | **String** | Working directory to use when running this step&#39;s container. If this value is a relative path, it is relative to the build&#39;s working directory. If this value is absolute, it may be outside the build&#39;s working directory, in which case the contents of the path may not be persisted across build step executions, unless a &#x60;volume&#x60; for that path is specified. If the build specifies a &#x60;RepoSource&#x60; with &#x60;dir&#x60; and a step with a &#x60;dir&#x60;, which specifies an absolute path, the &#x60;RepoSource&#x60; &#x60;dir&#x60; is ignored for the step&#39;s execution. |  [optional] |
|**entrypoint** | **String** | Entrypoint to be used instead of the build step image&#39;s default entrypoint. If unset, the image&#39;s default entrypoint is used. |  [optional] |
|**env** | **List&lt;String&gt;** | A list of environment variable definitions to be used when running a step. The elements are of the form \&quot;KEY&#x3D;VALUE\&quot; for the environment variable \&quot;KEY\&quot; being given the value \&quot;VALUE\&quot;. |  [optional] |
|**exitCode** | **Integer** | Output only. Return code from running the step. |  [optional] [readonly] |
|**id** | **String** | Unique identifier for this build step, used in &#x60;wait_for&#x60; to reference this build step as a dependency. |  [optional] |
|**name** | **String** | Required. The name of the container image that will run this particular build step. If the image is available in the host&#39;s Docker daemon&#39;s cache, it will be run directly. If not, the host will attempt to pull the image first, using the builder service account&#39;s credentials if necessary. The Docker daemon&#39;s cache will already have the latest versions of all of the officially supported build steps ([https://github.com/GoogleCloudPlatform/cloud-builders](https://github.com/GoogleCloudPlatform/cloud-builders)). The Docker daemon will also have cached many of the layers for some popular images, like \&quot;ubuntu\&quot;, \&quot;debian\&quot;, but they will be refreshed at the time you attempt to use them. If you built an image in a previous build step, it will be stored in the host&#39;s Docker daemon&#39;s cache and is available to use as the name for a later build step. |  [optional] |
|**pullTiming** | [**ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan**](ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan.md) |  |  [optional] |
|**script** | **String** | A shell script to be executed in the step. When script is provided, the user cannot specify the entrypoint or args. |  [optional] |
|**secretEnv** | **List&lt;String&gt;** | A list of environment variables which are encrypted using a Cloud Key Management Service crypto key. These values must be specified in the build&#39;s &#x60;Secret&#x60;. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Output only. Status of the build step. At this time, build step status is only updated on build completion; step status is not updated in real-time as the build progresses. |  [optional] [readonly] |
|**timeout** | **String** | Time limit for executing this build step. If not defined, the step has no time limit and will be allowed to continue to run until either it completes or the build itself times out. |  [optional] |
|**timing** | [**ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan**](ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan.md) |  |  [optional] |
|**volumes** | [**List&lt;ContaineranalysisGoogleDevtoolsCloudbuildV1Volume&gt;**](ContaineranalysisGoogleDevtoolsCloudbuildV1Volume.md) | List of volumes to mount into the build step. Each volume is created as an empty volume prior to execution of the build step. Upon completion of the build, volumes and their contents are discarded. Using a named volume in only one step is not valid as it is indicative of a build request with an incorrect configuration. |  [optional] |
|**waitFor** | **List&lt;String&gt;** | The ID(s) of the step(s) that this build step depends on. This build step will not start until all the build steps in &#x60;wait_for&#x60; have completed successfully. If &#x60;wait_for&#x60; is empty, this build step will start when all previous build steps in the &#x60;Build.Steps&#x60; list have completed successfully. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNKNOWN | &quot;STATUS_UNKNOWN&quot; |
| PENDING | &quot;PENDING&quot; |
| QUEUED | &quot;QUEUED&quot; |
| WORKING | &quot;WORKING&quot; |
| SUCCESS | &quot;SUCCESS&quot; |
| FAILURE | &quot;FAILURE&quot; |
| INTERNAL_ERROR | &quot;INTERNAL_ERROR&quot; |
| TIMEOUT | &quot;TIMEOUT&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| EXPIRED | &quot;EXPIRED&quot; |



