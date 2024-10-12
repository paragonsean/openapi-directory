# AlloyDbApi.NetworkConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocatedIpRange** | **String** | Optional. Name of the allocated IP range for the private IP AlloyDB cluster, for example: \&quot;google-managed-services-default\&quot;. If set, the instance IPs for this cluster will be created in the allocated range. The range name must comply with RFC 1035. Specifically, the name must be 1-63 characters long and match the regular expression &#x60;[a-z]([-a-z0-9]*[a-z0-9])?&#x60;. Field name is intended to be consistent with Cloud SQL. | [optional] 
**network** | **String** | Optional. The resource link for the VPC network in which cluster resources are created and from which they are accessible via Private IP. The network must belong to the same project as the cluster. It is specified in the form: &#x60;projects/{project_number}/global/networks/{network_id}&#x60;. This is required to create a cluster. | [optional] 


