

# VcenterSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caCerts** | **String** | Concatenated X.509 certificates in Base64 encoded DER format. Each certificate must start with -----BEGIN CERTIFICATE----- and end with -----END CERTIFICATE-----. Use an empty string to remove the existing certificates for the vCenter. |  [optional] |
|**configuredSlaDomainId** | **String** | The ID of the SLA Domain configured directly on the Rubrik object. |  |
|**configuredSlaDomainName** | **String** | The name of the SLA Domain configured directly on the Rubrik object. |  |
|**configuredSlaDomainType** | **ConfiguredSlaType** |  |  [optional] |
|**id** | **String** | The ID of the Rubrik object. |  |
|**isConfiguredSlaDomainRetentionLocked** | **Boolean** | Indicates whether the configured SLA Domain is Retention Locked. When this value is &#39;true&#39;, the configured SLA Domain is a Retention Lock SLA Domain. |  [optional] |
|**name** | **String** | The name of the Rubrik object. |  |
|**primaryClusterId** | **String** | The ID of the cluster that manages the Rubrik object. |  |
|**slaLastUpdateTime** | **OffsetDateTime** | The UTC time when the SLA Domain was last updated. |  [optional] |
|**computeVisibilityFilter** | [**List&lt;ClusterVisibilityInfo&gt;**](ClusterVisibilityInfo.md) | Compute clusters that are visible to this Rubrik Cluster. All other compute resources are hidden. If &#39;computeVisibilityFilter&#39; is not specified, all resources are visible. If &#39;hostGroupFilter&#39; is not specified for a compute cluster, all compute resources in the compute cluster are visible. If a &#39;hostGroupFilter&#39; is specified for a compute cluster, only vms that currently reside on these hosts are visible. |  |
|**configuredSlaDomainPolarisManagedId** | **String** | Optional field containing Polaris managed id of the configured SLA domain if it is Polaris managed. |  [optional] |
|**conflictResolutionAuthz** | [**ConflictResolutionAuthzEnum**](#ConflictResolutionAuthzEnum) | Set to &#39;AllowAutoConflictResolution&#39; to link the relic virtual machine objects of a virtual machine to the current object for the virtual machine or to &#39;NoConflictResolution&#39; to prevent linking. The Rubrik cluster generates a unique ID for each virtual machine when a vCenter Server is added. When a virtual machine changes to another vCenter Server or unregisters and registers with the same vCenter Server, a new unique ID is generated for that virtual machine. When this happens, the virtual machine object associated with the original ID becomes a relic. This option links relic virtual machine objects with the current virtual machine object of a specific virtual machine, and makes the collective snapshot history available through the current object. Default value is &#39;NoConflictResolution&#39;. |  [optional] |
|**connectionStatus** | [**RefreshableObjectConnectionStatus**](RefreshableObjectConnectionStatus.md) |  |  |
|**hostname** | **String** |  |  |
|**isIoFilterInstalled** | **Boolean** | A Boolean value that specifies whether Rubrik IO filters are installed on any compute clusters in the vCenter. When this value is &#39;true,&#39; Rubrik IO filters are present on at least one compute cluster in the vCenter. When this value is &#39;false,&#39; no Rubrik IO filters are present on any compute clusters in the vCenter. |  [optional] |
|**isVmc** | **Boolean** | Indicates if the vCenter is a VMC instance. |  [optional] |
|**lastRefreshTime** | **OffsetDateTime** | Optional field containing the last time that a vcenter was refreshed (either lite or full). |  [optional] |
|**username** | **String** |  |  |
|**version** | **String** | Version of vCenter. |  |



## Enum: ConflictResolutionAuthzEnum

| Name | Value |
|---- | -----|
| ALLOW_AUTO_CONFLICT_RESOLUTION | &quot;AllowAutoConflictResolution&quot; |
| NO_CONFLICT_RESOLUTION | &quot;NoConflictResolution&quot; |



