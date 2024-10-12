# CloudFilestoreApi.GoogleCloudSaasacceleratorManagementProvidersV1Instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumerDefinedName** | **String** | consumer_defined_name is the name of the instance set by the service consumers. Generally this is different from the &#x60;name&#x60; field which reperesents the system-assigned id of the instance which the service consumers do not recognize. This is a required field for tenants onboarding to Maintenance Window notifications (go/slm-rollout-maintenance-policies#prerequisites). | [optional] 
**createTime** | **String** | Output only. Timestamp when the resource was created. | [optional] [readonly] 
**instanceType** | **String** | Optional. The instance_type of this instance of format: projects/{project_number}/locations/{location_id}/instanceTypes/{instance_type_id}. Instance Type represents a high-level tier or SKU of the service that this instance belong to. When enabled(eg: Maintenance Rollout), Rollout uses &#39;instance_type&#39; along with &#39;software_versions&#39; to determine whether instance needs an update or not. | [optional] 
**labels** | **{String: String}** | Optional. Resource labels to represent user provided metadata. Each label is a key-value pair, where both the key and the value are arbitrary strings provided by the user. | [optional] 
**maintenancePolicyNames** | **{String: String}** | Optional. The MaintenancePolicies that have been attached to the instance. The key must be of the type name of the oneof policy name defined in MaintenancePolicy, and the referenced policy must define the same policy type. For details, please refer to go/mr-user-guide. Should not be set if maintenance_settings.maintenance_policies is set. | [optional] 
**maintenanceSchedules** | [**{String: GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSchedule}**](GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSchedule.md) | The MaintenanceSchedule contains the scheduling information of published maintenance schedule with same key as software_versions. | [optional] 
**maintenanceSettings** | [**GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings**](GoogleCloudSaasacceleratorManagementProvidersV1MaintenanceSettings.md) |  | [optional] 
**name** | **String** | Unique name of the resource. It uses the form: &#x60;projects/{project_number}/locations/{location_id}/instances/{instance_id}&#x60; Note: This name is passed, stored and logged across the rollout system. So use of consumer project_id or any other consumer PII in the name is strongly discouraged for wipeout (go/wipeout) compliance. See go/elysium/project_ids#storage-guidance for more details. | [optional] 
**notificationParameters** | [**{String: GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameter}**](GoogleCloudSaasacceleratorManagementProvidersV1NotificationParameter.md) | Optional. notification_parameter are information that service producers may like to include that is not relevant to Rollout. This parameter will only be passed to Gamma and Cloud Logging for notification/logging purpose. | [optional] 
**producerMetadata** | **{String: String}** | Output only. Custom string attributes used primarily to expose producer-specific information in monitoring dashboards. See go/get-instance-metadata. | [optional] [readonly] 
**provisionedResources** | [**[GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource]**](GoogleCloudSaasacceleratorManagementProvidersV1ProvisionedResource.md) | Output only. The list of data plane resources provisioned for this instance, e.g. compute VMs. See go/get-instance-metadata. | [optional] [readonly] 
**slmInstanceTemplate** | **String** | Link to the SLM instance template. Only populated when updating SLM instances via SSA&#39;s Actuation service adaptor. Service producers with custom control plane (e.g. Cloud SQL) doesn&#39;t need to populate this field. Instead they should use software_versions. | [optional] 
**sloMetadata** | [**GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata**](GoogleCloudSaasacceleratorManagementProvidersV1SloMetadata.md) |  | [optional] 
**softwareVersions** | **{String: String}** | Software versions that are used to deploy this instance. This can be mutated by rollout services. | [optional] 
**state** | **String** | Output only. Current lifecycle state of the resource (e.g. if it&#39;s being created or ready to use). | [optional] [readonly] 
**tenantProjectId** | **String** | Output only. ID of the associated GCP tenant project. See go/get-instance-metadata. | [optional] [readonly] 
**updateTime** | **String** | Output only. Timestamp when the resource was last modified. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `READY` (value: `"READY"`)

* `UPDATING` (value: `"UPDATING"`)

* `REPAIRING` (value: `"REPAIRING"`)

* `DELETING` (value: `"DELETING"`)

* `ERROR` (value: `"ERROR"`)




