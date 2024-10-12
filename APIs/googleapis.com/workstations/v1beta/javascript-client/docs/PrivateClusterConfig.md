# CloudWorkstationsApi.PrivateClusterConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedProjects** | **[String]** | Optional. Additional projects that are allowed to attach to the workstation cluster&#39;s service attachment. By default, the workstation cluster&#39;s project and the VPC host project (if different) are allowed. | [optional] 
**clusterHostname** | **String** | Output only. Hostname for the workstation cluster. This field will be populated only when private endpoint is enabled. To access workstations in the workstation cluster, create a new DNS zone mapping this domain name to an internal IP address and a forwarding rule mapping that address to the service attachment. | [optional] [readonly] 
**enablePrivateEndpoint** | **Boolean** | Immutable. Whether Workstations endpoint is private. | [optional] 
**serviceAttachmentUri** | **String** | Output only. Service attachment URI for the workstation cluster. The service attachemnt is created when private endpoint is enabled. To access workstations in the workstation cluster, configure access to the managed service using [Private Service Connect](https://cloud.google.com/vpc/docs/configure-private-service-connect-services). | [optional] [readonly] 


