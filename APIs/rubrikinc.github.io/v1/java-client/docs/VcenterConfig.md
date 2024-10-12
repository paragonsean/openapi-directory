

# VcenterConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caCerts** | **String** | Concatenated X.509 certificates in Base64 encoded DER format. Each certificate must start with -----BEGIN CERTIFICATE----- and end with -----END CERTIFICATE-----. |  [optional] |
|**computeVisibilityFilter** | [**List&lt;ClusterVisibilityConfig&gt;**](ClusterVisibilityConfig.md) | Select compute clusters that must be visible to this Rubrik cluster. All other compute resources are hidden. If &#39;computeVisibilityFilter&#39; is not specified, all resources are visible. If &#39;hostGroupFilter&#39; is not specified for a compute cluster, all compute resources in the compute cluster are visible. If &#39;hostGroupFilter&#39; is specified for a compute cluster, only virtual machinesthat currently reside on these hosts are visible. For the stretched cluster configuration (vMSC), specify the appropriate host groups. |  [optional] |
|**conflictResolutionAuthz** | [**ConflictResolutionAuthzEnum**](#ConflictResolutionAuthzEnum) | Set to &#39;AllowAutoConflictResolution&#39; to link the relic virtual machine objects of a virtual machine to the current object for the virtual machine or to &#39;NoConflictResolution&#39; to prevent linking. The Rubrik cluster generates a unique ID for each virtual machine when a vCenter Server is added. When a virtual machine changes to another vCenter Server or unregisters and registers with the same vCenter Server, a new unique ID is generated for that virtual machine. When this happens, the virtual machine object associated with the original ID becomes a relic. This option links relic virtual machine objects with the current virtual machine object of a specific virtual machine, and makes the collective snapshot history available through the current object. Default value is &#39;NoConflictResolution&#39;. |  [optional] |
|**hostname** | **String** |  |  |
|**password** | **String** |  |  |
|**username** | **String** |  |  |



## Enum: ConflictResolutionAuthzEnum

| Name | Value |
|---- | -----|
| ALLOW_AUTO_CONFLICT_RESOLUTION | &quot;AllowAutoConflictResolution&quot; |
| NO_CONFLICT_RESOLUTION | &quot;NoConflictResolution&quot; |



