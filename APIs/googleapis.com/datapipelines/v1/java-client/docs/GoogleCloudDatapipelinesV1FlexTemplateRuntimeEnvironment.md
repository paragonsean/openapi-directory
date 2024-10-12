

# GoogleCloudDatapipelinesV1FlexTemplateRuntimeEnvironment

The environment values to be set at runtime for a Flex Template.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalExperiments** | **List&lt;String&gt;** | Additional experiment flags for the job. |  [optional] |
|**additionalUserLabels** | **Map&lt;String, String&gt;** | Additional user labels to be specified for the job. Keys and values must follow the restrictions specified in the [labeling restrictions](https://cloud.google.com/compute/docs/labeling-resources#restrictions). An object containing a list of key/value pairs. Example: &#x60;{ \&quot;name\&quot;: \&quot;wrench\&quot;, \&quot;mass\&quot;: \&quot;1kg\&quot;, \&quot;count\&quot;: \&quot;3\&quot; }&#x60;. |  [optional] |
|**enableStreamingEngine** | **Boolean** | Whether to enable Streaming Engine for the job. |  [optional] |
|**flexrsGoal** | [**FlexrsGoalEnum**](#FlexrsGoalEnum) | Set FlexRS goal for the job. https://cloud.google.com/dataflow/docs/guides/flexrs |  [optional] |
|**ipConfiguration** | [**IpConfigurationEnum**](#IpConfigurationEnum) | Configuration for VM IPs. |  [optional] |
|**kmsKeyName** | **String** | Name for the Cloud KMS key for the job. Key format is: projects//locations//keyRings//cryptoKeys/ |  [optional] |
|**machineType** | **String** | The machine type to use for the job. Defaults to the value from the template if not specified. |  [optional] |
|**maxWorkers** | **Integer** | The maximum number of Compute Engine instances to be made available to your pipeline during execution, from 1 to 1000. |  [optional] |
|**network** | **String** | Network to which VMs will be assigned. If empty or unspecified, the service will use the network \&quot;default\&quot;. |  [optional] |
|**numWorkers** | **Integer** | The initial number of Compute Engine instances for the job. |  [optional] |
|**serviceAccountEmail** | **String** | The email address of the service account to run the job as. |  [optional] |
|**subnetwork** | **String** | Subnetwork to which VMs will be assigned, if desired. You can specify a subnetwork using either a complete URL or an abbreviated path. Expected to be of the form \&quot;https://www.googleapis.com/compute/v1/projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNETWORK\&quot; or \&quot;regions/REGION/subnetworks/SUBNETWORK\&quot;. If the subnetwork is located in a Shared VPC network, you must use the complete URL. |  [optional] |
|**tempLocation** | **String** | The Cloud Storage path to use for temporary files. Must be a valid Cloud Storage URL, beginning with &#x60;gs://&#x60;. |  [optional] |
|**workerRegion** | **String** | The Compute Engine region (https://cloud.google.com/compute/docs/regions-zones/regions-zones) in which worker processing should occur, e.g. \&quot;us-west1\&quot;. Mutually exclusive with worker_zone. If neither worker_region nor worker_zone is specified, defaults to the control plane region. |  [optional] |
|**workerZone** | **String** | The Compute Engine zone (https://cloud.google.com/compute/docs/regions-zones/regions-zones) in which worker processing should occur, e.g. \&quot;us-west1-a\&quot;. Mutually exclusive with worker_region. If neither worker_region nor worker_zone is specified, a zone in the control plane region is chosen based on available capacity. If both &#x60;worker_zone&#x60; and &#x60;zone&#x60; are set, &#x60;worker_zone&#x60; takes precedence. |  [optional] |
|**zone** | **String** | The Compute Engine [availability zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones) for launching worker instances to run your pipeline. In the future, worker_zone will take precedence. |  [optional] |



## Enum: FlexrsGoalEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;FLEXRS_UNSPECIFIED&quot; |
| SPEED_OPTIMIZED | &quot;FLEXRS_SPEED_OPTIMIZED&quot; |
| COST_OPTIMIZED | &quot;FLEXRS_COST_OPTIMIZED&quot; |



## Enum: IpConfigurationEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;WORKER_IP_UNSPECIFIED&quot; |
| PUBLIC | &quot;WORKER_IP_PUBLIC&quot; |
| PRIVATE | &quot;WORKER_IP_PRIVATE&quot; |



