

# WorkerPool

Describes one particular pool of Cloud Dataflow workers to be instantiated by the Cloud Dataflow service in order to perform the computations required by a job. Note that a workflow job may use multiple pools, in order to match the various computational requirements of the various stages of the job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoscalingSettings** | [**AutoscalingSettings**](AutoscalingSettings.md) |  |  [optional] |
|**dataDisks** | [**List&lt;Disk&gt;**](Disk.md) | Data disks that are used by a VM in this workflow. |  [optional] |
|**defaultPackageSet** | [**DefaultPackageSetEnum**](#DefaultPackageSetEnum) | The default package set to install. This allows the service to select a default set of packages which are useful to worker harnesses written in a particular language. |  [optional] |
|**diskSizeGb** | **Integer** | Size of root disk for VMs, in GB. If zero or unspecified, the service will attempt to choose a reasonable default. |  [optional] |
|**diskSourceImage** | **String** | Fully qualified source image for disks. |  [optional] |
|**diskType** | **String** | Type of root disk for VMs. If empty or unspecified, the service will attempt to choose a reasonable default. |  [optional] |
|**ipConfiguration** | [**IpConfigurationEnum**](#IpConfigurationEnum) | Configuration for VM IPs. |  [optional] |
|**kind** | **String** | The kind of the worker pool; currently only &#x60;harness&#x60; and &#x60;shuffle&#x60; are supported. |  [optional] |
|**machineType** | **String** | Machine type (e.g. \&quot;n1-standard-1\&quot;). If empty or unspecified, the service will attempt to choose a reasonable default. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | Metadata to set on the Google Compute Engine VMs. |  [optional] |
|**network** | **String** | Network to which VMs will be assigned. If empty or unspecified, the service will use the network \&quot;default\&quot;. |  [optional] |
|**numThreadsPerWorker** | **Integer** | The number of threads per worker harness. If empty or unspecified, the service will choose a number of threads (according to the number of cores on the selected machine type for batch, or 1 by convention for streaming). |  [optional] |
|**numWorkers** | **Integer** | Number of Google Compute Engine workers in this pool needed to execute the job. If zero or unspecified, the service will attempt to choose a reasonable default. |  [optional] |
|**onHostMaintenance** | **String** | The action to take on host maintenance, as defined by the Google Compute Engine API. |  [optional] |
|**packages** | [**List&lt;ModelPackage&gt;**](ModelPackage.md) | Packages to be installed on workers. |  [optional] |
|**poolArgs** | **Map&lt;String, Object&gt;** | Extra arguments for this worker pool. |  [optional] |
|**sdkHarnessContainerImages** | [**List&lt;SdkHarnessContainerImage&gt;**](SdkHarnessContainerImage.md) | Set of SDK harness containers needed to execute this pipeline. This will only be set in the Fn API path. For non-cross-language pipelines this should have only one entry. Cross-language pipelines will have two or more entries. |  [optional] |
|**subnetwork** | **String** | Subnetwork to which VMs will be assigned, if desired. Expected to be of the form \&quot;regions/REGION/subnetworks/SUBNETWORK\&quot;. |  [optional] |
|**taskrunnerSettings** | [**TaskRunnerSettings**](TaskRunnerSettings.md) |  |  [optional] |
|**teardownPolicy** | [**TeardownPolicyEnum**](#TeardownPolicyEnum) | Sets the policy for determining when to turndown worker pool. Allowed values are: &#x60;TEARDOWN_ALWAYS&#x60;, &#x60;TEARDOWN_ON_SUCCESS&#x60;, and &#x60;TEARDOWN_NEVER&#x60;. &#x60;TEARDOWN_ALWAYS&#x60; means workers are always torn down regardless of whether the job succeeds. &#x60;TEARDOWN_ON_SUCCESS&#x60; means workers are torn down if the job succeeds. &#x60;TEARDOWN_NEVER&#x60; means the workers are never torn down. If the workers are not torn down by the service, they will continue to run and use Google Compute Engine VM resources in the user&#39;s project until they are explicitly terminated by the user. Because of this, Google recommends using the &#x60;TEARDOWN_ALWAYS&#x60; policy except for small, manually supervised test jobs. If unknown or unspecified, the service will attempt to choose a reasonable default. |  [optional] |
|**workerHarnessContainerImage** | **String** | Required. Docker container image that executes the Cloud Dataflow worker harness, residing in Google Container Registry. Deprecated for the Fn API path. Use sdk_harness_container_images instead. |  [optional] |
|**zone** | **String** | Zone to run the worker pools in. If empty or unspecified, the service will attempt to choose a reasonable default. |  [optional] |



## Enum: DefaultPackageSetEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;DEFAULT_PACKAGE_SET_UNKNOWN&quot; |
| NONE | &quot;DEFAULT_PACKAGE_SET_NONE&quot; |
| JAVA | &quot;DEFAULT_PACKAGE_SET_JAVA&quot; |
| PYTHON | &quot;DEFAULT_PACKAGE_SET_PYTHON&quot; |



## Enum: IpConfigurationEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;WORKER_IP_UNSPECIFIED&quot; |
| PUBLIC | &quot;WORKER_IP_PUBLIC&quot; |
| PRIVATE | &quot;WORKER_IP_PRIVATE&quot; |



## Enum: TeardownPolicyEnum

| Name | Value |
|---- | -----|
| POLICY_UNKNOWN | &quot;TEARDOWN_POLICY_UNKNOWN&quot; |
| ALWAYS | &quot;TEARDOWN_ALWAYS&quot; |
| ON_SUCCESS | &quot;TEARDOWN_ON_SUCCESS&quot; |
| NEVER | &quot;TEARDOWN_NEVER&quot; |



