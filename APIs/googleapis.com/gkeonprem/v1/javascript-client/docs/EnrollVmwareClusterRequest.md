# AnthosOnPremApi.EnrollVmwareClusterRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adminClusterMembership** | **String** | Required. The admin cluster this VMware user cluster belongs to. This is the full resource name of the admin cluster&#39;s fleet membership. In the future, references to other resource types might be allowed if admin clusters are modeled as their own resources. | [optional] 
**localName** | **String** | Optional. The object name of the VMware OnPremUserCluster custom resource on the associated admin cluster. This field is used to support conflicting resource names when enrolling existing clusters to the API. When not provided, this field will resolve to the vmware_cluster_id. Otherwise, it must match the object name of the VMware OnPremUserCluster custom resource. It is not modifiable outside / beyond the enrollment operation. | [optional] 
**validateOnly** | **Boolean** | Validate the request without actually doing any updates. | [optional] 
**vmwareClusterId** | **String** | User provided OnePlatform identifier that is used as part of the resource name. This must be unique among all GKE on-prem clusters within a project and location and will return a 409 if the cluster already exists. (https://tools.ietf.org/html/rfc1123) format. | [optional] 


