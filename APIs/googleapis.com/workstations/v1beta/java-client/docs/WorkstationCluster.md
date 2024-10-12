

# WorkstationCluster

A workstation cluster resource in the Cloud Workstations API. Defines a group of workstations in a particular region and the VPC network they're attached to.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | **Map&lt;String, String&gt;** | Optional. Client-specified annotations. |  [optional] |
|**conditions** | [**List&lt;Status&gt;**](Status.md) | Output only. Status conditions describing the workstation cluster&#39;s current state. |  [optional] [readonly] |
|**controlPlaneIp** | **String** | Output only. The private IP address of the control plane for this workstation cluster. Workstation VMs need access to this IP address to work with the service, so make sure that your firewall rules allow egress from the workstation VMs to this address. |  [optional] [readonly] |
|**createTime** | **String** | Output only. Time when this workstation cluster was created. |  [optional] [readonly] |
|**degraded** | **Boolean** | Output only. Whether this workstation cluster is in degraded mode, in which case it may require user action to restore full functionality. Details can be found in conditions. |  [optional] [readonly] |
|**deleteTime** | **String** | Output only. Time when this workstation cluster was soft-deleted. |  [optional] [readonly] |
|**displayName** | **String** | Optional. Human-readable name for this workstation cluster. |  [optional] |
|**domainConfig** | [**DomainConfig**](DomainConfig.md) |  |  [optional] |
|**etag** | **String** | Optional. Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation cluster and that are also propagated to the underlying Compute Engine resources. |  [optional] |
|**name** | **String** | Identifier. Full name of this workstation cluster. |  [optional] |
|**network** | **String** | Immutable. Name of the Compute Engine network in which instances associated with this workstation cluster will be created. |  [optional] |
|**privateClusterConfig** | [**PrivateClusterConfig**](PrivateClusterConfig.md) |  |  [optional] |
|**reconciling** | **Boolean** | Output only. Indicates whether this workstation cluster is currently being updated to match its intended state. |  [optional] [readonly] |
|**subnetwork** | **String** | Immutable. Name of the Compute Engine subnetwork in which instances associated with this workstation cluster will be created. Must be part of the subnetwork specified for this workstation cluster. |  [optional] |
|**uid** | **String** | Output only. A system-assigned unique identifier for this workstation cluster. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Time when this workstation cluster was most recently updated. |  [optional] [readonly] |



