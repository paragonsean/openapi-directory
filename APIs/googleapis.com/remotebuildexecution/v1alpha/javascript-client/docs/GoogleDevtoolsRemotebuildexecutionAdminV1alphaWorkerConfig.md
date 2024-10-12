# RemoteBuildExecutionApi.GoogleDevtoolsRemotebuildexecutionAdminV1alphaWorkerConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerator** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaAcceleratorConfig**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaAcceleratorConfig.md) |  | [optional] 
**attachedDisks** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaDisks**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaDisks.md) |  | [optional] 
**diskSizeGb** | **String** | Required. Size of the disk attached to the worker, in GB. See https://cloud.google.com/compute/docs/disks/ | [optional] 
**diskType** | **String** | Required. Disk Type to use for the worker. See [Storage options](https://cloud.google.com/compute/docs/disks/#introduction). Currently only &#x60;pd-standard&#x60; and &#x60;pd-ssd&#x60; are supported. | [optional] 
**labels** | **{String: String}** | Labels associated with the workers. Label keys and values can be no longer than 63 characters, can only contain lowercase letters, numeric characters, underscores and dashes. International letters are permitted. Label keys must start with a letter. Label values are optional. There can not be more than 64 labels per resource. | [optional] 
**machineType** | **String** | Required. Machine type of the worker, such as &#x60;e2-standard-2&#x60;. See https://cloud.google.com/compute/docs/machine-types for a list of supported machine types. Note that &#x60;f1-micro&#x60; and &#x60;g1-small&#x60; are not yet supported. | [optional] 
**maxConcurrentActions** | **String** | The maximum number of actions a worker can execute concurrently. | [optional] 
**minCpuPlatform** | **String** | Minimum CPU platform to use when creating the worker. See [CPU Platforms](https://cloud.google.com/compute/docs/cpu-platforms). | [optional] 
**networkAccess** | **String** | Determines the type of network access granted to workers. Possible values: - \&quot;public\&quot;: Workers can connect to the public internet. - \&quot;private\&quot;: Workers can only connect to Google APIs and services. - \&quot;restricted-private\&quot;: Workers can only connect to Google APIs that are reachable through &#x60;restricted.googleapis.com&#x60; (&#x60;199.36.153.4/30&#x60;). | [optional] 
**reserved** | **Boolean** | Determines whether the worker is reserved (equivalent to a Compute Engine on-demand VM and therefore won&#39;t be preempted). See [Preemptible VMs](https://cloud.google.com/preemptible-vms/) for more details. | [optional] 
**soleTenantNodeType** | **String** | The node type name to be used for sole-tenant nodes. | [optional] 
**userServiceAccounts** | **[String]** | Optional. List of user service accounts. The last service account in the list is what the user code will run as. The rest of the service accounts constitute the impersonation chain. For example, if len(user_service_accounts) &#x3D;&#x3D; 2 and if the VM&#39;s service account is RBE&#39;s P4SA, then RBE&#39;S P4SA should be granted the Service Account Token Creator role on user_service_accounts[0] and user_service_accounts[0] should be granted the Service Account Token Creator role on user_service_accounts[1]. | [optional] 
**vmImage** | **String** | The name of the image used by each VM. | [optional] 
**zones** | **[String]** | Optional. Zones in the region where the pool VMs should be. Leave empty for no restrictions. | [optional] 


