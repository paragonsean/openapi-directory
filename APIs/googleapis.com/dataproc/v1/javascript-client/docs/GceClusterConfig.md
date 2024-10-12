# CloudDataprocApi.GceClusterConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidentialInstanceConfig** | [**ConfidentialInstanceConfig**](ConfidentialInstanceConfig.md) |  | [optional] 
**internalIpOnly** | **Boolean** | Optional. If true, all instances in the cluster will only have internal IP addresses. By default, clusters are not restricted to internal IP addresses, and will have ephemeral external IP addresses assigned to each instance. This internal_ip_only restriction can only be enabled for subnetwork enabled networks, and all off-cluster dependencies must be configured to be accessible without external IP addresses. | [optional] 
**metadata** | **{String: String}** | Optional. The Compute Engine metadata entries to add to all instances (see Project and instance metadata (https://cloud.google.com/compute/docs/storing-retrieving-metadata#project_and_instance_metadata)). | [optional] 
**networkUri** | **String** | Optional. The Compute Engine network to be used for machine communications. Cannot be specified with subnetwork_uri. If neither network_uri nor subnetwork_uri is specified, the \&quot;default\&quot; network of the project is used, if it exists. Cannot be a \&quot;Custom Subnet Network\&quot; (see Using Subnetworks (https://cloud.google.com/compute/docs/subnetworks) for more information).A full URL, partial URI, or short name are valid. Examples: https://www.googleapis.com/compute/v1/projects/[project_id]/global/networks/default projects/[project_id]/global/networks/default default | [optional] 
**nodeGroupAffinity** | [**NodeGroupAffinity**](NodeGroupAffinity.md) |  | [optional] 
**privateIpv6GoogleAccess** | **String** | Optional. The type of IPv6 access for a cluster. | [optional] 
**reservationAffinity** | [**ReservationAffinity**](ReservationAffinity.md) |  | [optional] 
**serviceAccount** | **String** | Optional. The Dataproc service account (https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts#service_accounts_in_dataproc) (also see VM Data Plane identity (https://cloud.google.com/dataproc/docs/concepts/iam/dataproc-principals#vm_service_account_data_plane_identity)) used by Dataproc cluster VM instances to access Google Cloud Platform services.If not specified, the Compute Engine default service account (https://cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used. | [optional] 
**serviceAccountScopes** | **[String]** | Optional. The URIs of service account scopes to be included in Compute Engine instances. The following base set of scopes is always included: https://www.googleapis.com/auth/cloud.useraccounts.readonly https://www.googleapis.com/auth/devstorage.read_write https://www.googleapis.com/auth/logging.writeIf no scopes are specified, the following defaults are also provided: https://www.googleapis.com/auth/bigquery https://www.googleapis.com/auth/bigtable.admin.table https://www.googleapis.com/auth/bigtable.data https://www.googleapis.com/auth/devstorage.full_control | [optional] 
**shieldedInstanceConfig** | [**ShieldedInstanceConfig**](ShieldedInstanceConfig.md) |  | [optional] 
**subnetworkUri** | **String** | Optional. The Compute Engine subnetwork to be used for machine communications. Cannot be specified with network_uri.A full URL, partial URI, or short name are valid. Examples: https://www.googleapis.com/compute/v1/projects/[project_id]/regions/[region]/subnetworks/sub0 projects/[project_id]/regions/[region]/subnetworks/sub0 sub0 | [optional] 
**tags** | **[String]** | The Compute Engine tags to add to all instances (see Tagging instances (https://cloud.google.com/compute/docs/label-or-tag-resources#tags)). | [optional] 
**zoneUri** | **String** | Optional. The Compute Engine zone where the Dataproc cluster will be located. If omitted, the service will pick a zone in the cluster&#39;s Compute Engine region. On a get request, zone will always be present.A full URL, partial URI, or short name are valid. Examples: https://www.googleapis.com/compute/v1/projects/[project_id]/zones/[zone] projects/[project_id]/zones/[zone] [zone] | [optional] 



## Enum: PrivateIpv6GoogleAccessEnum


* `PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED` (value: `"PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED"`)

* `INHERIT_FROM_SUBNETWORK` (value: `"INHERIT_FROM_SUBNETWORK"`)

* `OUTBOUND` (value: `"OUTBOUND"`)

* `BIDIRECTIONAL` (value: `"BIDIRECTIONAL"`)




